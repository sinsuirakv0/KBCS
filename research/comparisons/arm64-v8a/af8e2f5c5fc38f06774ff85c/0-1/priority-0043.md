# v15.7.2 → v15.7.3 · 最優先の変更候補 (43)

[一覧の目次](README.md)

<a id="compare-914904aee649a40992183f7ebe3af229"></a>

### [`00873294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873294.md) → [`00873294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873294.md) FUN_00873294

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
      "definition_site": "008732a8",
      "incomplete_value": false,
      "site": "008732ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008732a8",
      "incomplete_value": false,
      "site": "008732ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "008732ac",
      "DATA",
      [
        "storage",
        "00c04a48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008732ac",
      "DATA",
      [
        "storage",
        "00c04af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873294.md#insn-008732a8)
- 新版 `008732a8`（命令位置の公開資料なし）

~~~diff
- 008732a8 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 008732a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008732a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008732a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 008732a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008732a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008732a8 bytes 08212991
+ 008732a8 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94edb9d50c2d00b9624286cb35bdf6a"></a>

### [`008732b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008732b8.md) → [`008732b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732b8.md) FUN_008732b8

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
      "definition_site": "008732bc",
      "incomplete_value": false,
      "site": "008732c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008732bc",
      "incomplete_value": false,
      "site": "008732c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "008732c0",
      "DATA",
      [
        "storage",
        "00c04a48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008732c0",
      "DATA",
      [
        "storage",
        "00c04af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008732b8.md#insn-008732bc)
- 新版 `008732bc`（命令位置の公開資料なし）

~~~diff
- 008732bc ["COPY", "tmp:0:8", ["const:a48:8"]]
- 008732bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008732bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008732bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 008732bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008732bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008732bc bytes 08212991
+ 008732bc bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-299ac0dc3464995c0155cd13438ca18a"></a>

### [`008732d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008732d0.md) → [`008732d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008732d0.md) FUN_008732d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873304",
      "incomplete_value": true,
      "site": "00873318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873304",
      "incomplete_value": true,
      "site": "00873318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "00873304",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873304",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008732fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008732d0.md#insn-008732fc)
- 新版 `008732fc`（命令位置の公開資料なし）

~~~diff
- 008732fc ["COPY", "tmp:0:8", ["const:d56:8"]]
- 008732fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008732fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008732fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 008732fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008732fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008732fc bytes 29593591
+ 008732fc bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f2240c8891cd650d13d85978240005"></a>

### [`008733fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008733fc.md) → [`008733fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008733fc.md) FUN_008733fc

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
      "definition_site": "00873410",
      "incomplete_value": false,
      "site": "00873414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873410",
      "incomplete_value": false,
      "site": "00873414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00873414",
      "DATA",
      [
        "storage",
        "00c04ac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873414",
      "DATA",
      [
        "storage",
        "00c04b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008733fc.md#insn-00873410)
- 新版 `00873410`（命令位置の公開資料なし）

~~~diff
- 00873410 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00873410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00873410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873410 bytes 08212b91
+ 00873410 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef7641984c7d45655c426d2e98ee238"></a>

### [`00873420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873420.md) → [`00873420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873420.md) FUN_00873420

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
      "definition_site": "00873424",
      "incomplete_value": false,
      "site": "00873428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873424",
      "incomplete_value": false,
      "site": "00873428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00873428",
      "DATA",
      [
        "storage",
        "00c04ac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873428",
      "DATA",
      [
        "storage",
        "00c04b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873420.md#insn-00873424)
- 新版 `00873424`（命令位置の公開資料なし）

~~~diff
- 00873424 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00873424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00873424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873424 bytes 08212b91
+ 00873424 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5c6d41c1e20da946e8606988a98fd7"></a>

### [`00873438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873438.md) → [`00873438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873438.md) FUN_00873438

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051c/0051c140.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0051c140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008734ac",
      "incomplete_value": true,
      "site": "008734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008734ac",
      "incomplete_value": true,
      "site": "008734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b18:8"
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
      "definition_site": "008734b0",
      "incomplete_value": true,
      "site": "008734c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008734b0",
      "incomplete_value": true,
      "site": "008734c0",
      "value": [
        "LOAD",
        "16",
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
      "008734ac",
      "READ",
      [
        "storage",
        "002a4b18",
        null,
        "string"
      ]
    ],
    [
      "008734b0",
      "READ",
      [
        "storage",
        "002a4b24",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008734ac",
      "READ",
      [
        "storage",
        "002a4b11",
        null,
        "string"
      ]
    ],
    [
      "008734b0",
      "READ",
      [
        "storage",
        "002a4b1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008734a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873438.md#insn-008734a4) · [`008734a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873438.md#insn-008734a8)
- 新版 `008734a4`（命令位置の公開資料なし） · `008734a8`（命令位置の公開資料なし）

~~~diff
- 008734a4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008734a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008734a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008734a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["COPY", "tmp:0:8", ["const:b11:8"]]
+ 008734a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008734a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008734a4 bytes 08612c91
+ 008734a4 bytes 08452c91
- 008734a8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 008734a8 bytes e9d1ffd0
+ 008734a8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 008734a8 bytes e9d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fd279a383deeff70347997223b134f"></a>

### [`0087363c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/0087363c.md) → [`0087363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/0087363c.md) FUN_0087363c

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
      "definition_site": "00873650",
      "incomplete_value": false,
      "site": "00873654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873650",
      "incomplete_value": false,
      "site": "00873654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00873654",
      "DATA",
      [
        "storage",
        "00c04b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873654",
      "DATA",
      [
        "storage",
        "00c04bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/0087363c.md#insn-00873650)
- 新版 `00873650`（命令位置の公開資料なし）

~~~diff
- 00873650 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00873650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00873650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873650 bytes 08212d91
+ 00873650 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32787d80b30535f166713743393c39e8"></a>

### [`00873660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873660.md) → [`00873660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873660.md) FUN_00873660

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
      "definition_site": "00873664",
      "incomplete_value": false,
      "site": "00873668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873664",
      "incomplete_value": false,
      "site": "00873668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00873668",
      "DATA",
      [
        "storage",
        "00c04b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873668",
      "DATA",
      [
        "storage",
        "00c04bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873660.md#insn-00873664)
- 新版 `00873664`（命令位置の公開資料なし）

~~~diff
- 00873664 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00873664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00873664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873664 bytes 08212d91
+ 00873664 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1efbc0fc88a6a672b48f9e9adc74a6e5"></a>

### [`00873678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873678.md) → [`00873678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873678.md) FUN_00873678

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008736ac",
      "incomplete_value": true,
      "site": "008736c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008736ac",
      "incomplete_value": true,
      "site": "008736c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
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
      "008736ac",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008736ac",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008736a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873678.md#insn-008736a4)
- 新版 `008736a4`（命令位置の公開資料なし）

~~~diff
- 008736a4 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 008736a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008736a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008736a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 008736a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008736a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008736a4 bytes 29593591
+ 008736a4 bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41461f77bcb11c14f05cee4341f83169"></a>

### [`008737a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737a4.md) → [`008737a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737a4.md) FUN_008737a4

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
      "definition_site": "008737b8",
      "incomplete_value": false,
      "site": "008737bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008737b8",
      "incomplete_value": false,
      "site": "008737bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "008737bc",
      "DATA",
      [
        "storage",
        "00c04bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008737bc",
      "DATA",
      [
        "storage",
        "00c04c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008737b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737a4.md#insn-008737b8)
- 新版 `008737b8`（命令位置の公開資料なし）

~~~diff
- 008737b8 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 008737b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008737b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008737b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 008737b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008737b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008737b8 bytes 08212f91
+ 008737b8 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51dcaac2c15355d73623240e3ffa840a"></a>

### [`008737c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737c8.md) → [`008737c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737c8.md) FUN_008737c8

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
      "definition_site": "008737cc",
      "incomplete_value": false,
      "site": "008737d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008737cc",
      "incomplete_value": false,
      "site": "008737d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "008737d0",
      "DATA",
      [
        "storage",
        "00c04bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008737d0",
      "DATA",
      [
        "storage",
        "00c04c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008737cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737c8.md#insn-008737cc)
- 新版 `008737cc`（命令位置の公開資料なし）

~~~diff
- 008737cc ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 008737cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008737cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008737cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 008737cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008737cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008737cc bytes 08212f91
+ 008737cc bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6fc7027bb20b4345d6f9c307e70b09b"></a>

### [`008737e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737e0.md) → [`008737e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/008737e0.md) FUN_008737e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.82% / 新版 90.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873874",
      "incomplete_value": true,
      "site": "00873884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873874",
      "incomplete_value": true,
      "site": "00873884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3b:8"
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
      "definition_site": "00873878",
      "incomplete_value": true,
      "site": "00873888",
      "value": [
        "LOAD",
        "16",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873878",
      "incomplete_value": true,
      "site": "00873888",
      "value": [
        "LOAD",
        "16",
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
                "const:e:8"
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
      "00873874",
      "READ",
      [
        "storage",
        "002ae03b",
        null,
        "string"
      ]
    ],
    [
      "00873878",
      "READ",
      [
        "storage",
        "002ae049",
        null,
        "string"
      ]
    ],
    [
      "008738e8",
      "READ",
      [
        "storage",
        "002acf35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873874",
      "READ",
      [
        "storage",
        "002adfa7",
        null,
        "string"
      ]
    ],
    [
      "00873878",
      "READ",
      [
        "storage",
        "002adfb5",
        null,
        "string"
      ]
    ],
    [
      "008738e8",
      "READ",
      [
        "storage",
        "002acf2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737e0.md#insn-00873868) · [`0087386c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737e0.md#insn-0087386c) · [`00873870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/008737e0.md#insn-00873870)
- 新版 `00873868`（命令位置の公開資料なし） · `0087386c`（命令位置の公開資料なし）

~~~diff
- 00873868 ["COPY", "register:4040:8", ["const:2ae000:8"]]
+ 00873868 ["COPY", "register:4040:8", ["const:2ad000:8"]]
- 00873868 bytes c8d1fff0
+ 00873868 bytes c8d1ffd0
- 0087386c ["COPY", "tmp:0:8", ["const:3b:8"]]
- 0087386c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087386c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087386c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087386c ["COPY", "tmp:0:8", ["const:fa7:8"]]
+ 0087386c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087386c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087386c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087386c bytes 08ed0091
+ 0087386c bytes 089d3e91
- 00873870 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00873870 bytes e9d1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f38094014301692b69e43733185a12"></a>

### [`00873a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a0c.md) → [`00873a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a0c.md) FUN_00873a0c

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
      "definition_site": "00873a20",
      "incomplete_value": false,
      "site": "00873a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873a20",
      "incomplete_value": false,
      "site": "00873a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00873a24",
      "DATA",
      [
        "storage",
        "00c04c48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873a24",
      "DATA",
      [
        "storage",
        "00c04cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a0c.md#insn-00873a20)
- 新版 `00873a20`（命令位置の公開資料なし）

~~~diff
- 00873a20 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00873a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00873a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873a20 bytes 08213191
+ 00873a20 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7189632dd59cf25a7b427937210706b1"></a>

### [`00873a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a30.md) → [`00873a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a30.md) FUN_00873a30

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
      "definition_site": "00873a34",
      "incomplete_value": false,
      "site": "00873a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873a34",
      "incomplete_value": false,
      "site": "00873a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00873a38",
      "DATA",
      [
        "storage",
        "00c04c48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873a38",
      "DATA",
      [
        "storage",
        "00c04cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a30.md#insn-00873a34)
- 新版 `00873a34`（命令位置の公開資料なし）

~~~diff
- 00873a34 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00873a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00873a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873a34 bytes 08213191
+ 00873a34 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9402d9db4bad438a0e58d0c52682bd"></a>

### [`00873a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a48.md) → [`00873a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873a48.md) FUN_00873a48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873ad0",
      "incomplete_value": true,
      "site": "00873ae0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873ad0",
      "incomplete_value": true,
      "site": "00873ae0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f35:8"
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
      "definition_site": "00873ad0",
      "incomplete_value": true,
      "site": "00873ae0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00873ad0",
      "incomplete_value": true,
      "site": "00873ae0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873b4c",
      "incomplete_value": true,
      "site": "00873b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b4c",
      "incomplete_value": true,
      "site": "00873b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
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
      "00873ad0",
      "READ",
      [
        "storage",
        "002acf35",
        null,
        "string"
      ]
    ],
    [
      "00873ad0",
      "READ",
      [
        "storage",
        "002acf45",
        null,
        "string"
      ]
    ],
    [
      "00873b4c",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873ad0",
      "READ",
      [
        "storage",
        "002acf2c",
        null,
        "string"
      ]
    ],
    [
      "00873ad0",
      "READ",
      [
        "storage",
        "002acf3c",
        null,
        "string"
      ]
    ],
    [
      "00873b4c",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a48.md#insn-00873acc) · [`00873b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873a48.md#insn-00873b44)
- 新版 `00873acc`（命令位置の公開資料なし） · `00873b44`（命令位置の公開資料なし）

~~~diff
- 00873acc ["COPY", "tmp:0:8", ["const:f35:8"]]
- 00873acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873acc ["COPY", "tmp:0:8", ["const:f2c:8"]]
+ 00873acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873acc bytes 08d53c91
+ 00873acc bytes 08b13c91
- 00873b44 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00873b44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00873b44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00873b44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 00873b44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00873b44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00873b44 bytes 29593591
+ 00873b44 bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b6c3f291b7133e7d5231fff2437ea21"></a>

### [`00873c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c2c.md) → [`00873c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c2c.md) FUN_00873c2c

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
      "definition_site": "00873c40",
      "incomplete_value": false,
      "site": "00873c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c40",
      "incomplete_value": false,
      "site": "00873c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00873c44",
      "DATA",
      [
        "storage",
        "00c04cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873c44",
      "DATA",
      [
        "storage",
        "00c04d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c2c.md#insn-00873c40)
- 新版 `00873c40`（命令位置の公開資料なし）

~~~diff
- 00873c40 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00873c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00873c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873c40 bytes 08213391
+ 00873c40 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e9c7d4349344d202bf0c2af246b49f"></a>

### [`00873c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c50.md) → [`00873c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c50.md) FUN_00873c50

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
      "definition_site": "00873c54",
      "incomplete_value": false,
      "site": "00873c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873c54",
      "incomplete_value": false,
      "site": "00873c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00873c58",
      "DATA",
      [
        "storage",
        "00c04cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873c58",
      "DATA",
      [
        "storage",
        "00c04d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c50.md#insn-00873c54)
- 新版 `00873c54`（命令位置の公開資料なし）

~~~diff
- 00873c54 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00873c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00873c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873c54 bytes 08213391
+ 00873c54 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67cc81bf76b3290cfe457fd0eb67e753"></a>

### [`00873c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c68.md) → [`00873c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00873/00873c68.md) FUN_00873c68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873e1c",
      "incomplete_value": false,
      "site": "00873e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e1c",
      "incomplete_value": false,
      "site": "00873e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00873e1c",
      "DATA",
      [
        "storage",
        "00c04d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04d58",
        null,
        "pointer"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873e1c",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e08",
        null,
        "pointer"
      ]
    ],
    [
      "00873ea0",
      "READ",
      [
        "storage",
        "00c04e10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00873/00873c68.md#insn-00873e14)
- 新版 `00873e14`（命令位置の公開資料なし）

~~~diff
- 00873e14 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00873e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00873e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873e14 bytes 08e13491
+ 00873e14 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b852c262ba3b983dd1ae9fd18a64ca54"></a>

### [`00874088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874088.md) → [`00874088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874088.md) FUN_00874088

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
      "definition_site": "0087409c",
      "incomplete_value": false,
      "site": "008740a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087409c",
      "incomplete_value": false,
      "site": "008740a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "008740a0",
      "DATA",
      [
        "storage",
        "00c04d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008740a0",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087409c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874088.md#insn-0087409c)
- 新版 `0087409c`（命令位置の公開資料なし）

~~~diff
- 0087409c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0087409c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087409c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087409c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0087409c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087409c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087409c bytes 08e13491
+ 0087409c bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fb25d4f63be04257854d08afb276511"></a>

### [`008740ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740ac.md) → [`008740ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740ac.md) FUN_008740ac

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
      "definition_site": "008740b0",
      "incomplete_value": false,
      "site": "008740b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008740b0",
      "incomplete_value": false,
      "site": "008740b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008740b4",
      "DATA",
      [
        "storage",
        "00c04d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008740b4",
      "DATA",
      [
        "storage",
        "00c04de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008740b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740ac.md#insn-008740b0)
- 新版 `008740b0`（命令位置の公開資料なし）

~~~diff
- 008740b0 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 008740b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008740b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008740b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 008740b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008740b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008740b0 bytes 08e13491
+ 008740b0 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5be1423470222af544005ff0ce78bae6"></a>

### [`008740c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740c4.md) → [`008740c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008740c4.md) FUN_008740c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0042c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md) [`0058e620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058e620.md) [`0058e878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058e/0058e878.md) [`005902dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/005902dc.md) [`0073eb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073eb44.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0058e620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e620.md) [`0058e878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058e/0058e878.md) [`005902dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/005902dc.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087410c",
      "incomplete_value": false,
      "site": "00874114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087410c",
      "incomplete_value": false,
      "site": "00874114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "definition_site": "00874190",
      "incomplete_value": false,
      "site": "00874198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874190",
      "incomplete_value": false,
      "site": "00874198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00874114",
      "DATA",
      [
        "storage",
        "00c04da8",
        null,
        "undefined *"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04dc8",
        null,
        "pointer"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874114",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04e78",
        null,
        "pointer"
      ]
    ],
    [
      "00874184",
      "READ",
      [
        "storage",
        "00c04e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087410c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740c4.md#insn-0087410c) · [`00874190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008740c4.md#insn-00874190)
- 新版 `0087410c`（命令位置の公開資料なし） · `00874190`（命令位置の公開資料なし）

~~~diff
- 0087410c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0087410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0087410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087410c bytes 08a13691
+ 0087410c bytes 08613991
- 00874190 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00874190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00874190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874190 bytes 08a13891
+ 00874190 bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fac8c9e431b3d0a8425163d61bdcdec8"></a>

### [`00874288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874288.md) → [`00874288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874288.md) FUN_00874288

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
      "definition_site": "0087429c",
      "incomplete_value": false,
      "site": "008742a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087429c",
      "incomplete_value": false,
      "site": "008742a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "008742a0",
      "DATA",
      [
        "storage",
        "00c04da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008742a0",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087429c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874288.md#insn-0087429c)
- 新版 `0087429c`（命令位置の公開資料なし）

~~~diff
- 0087429c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0087429c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087429c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087429c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0087429c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087429c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087429c bytes 08a13691
+ 0087429c bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b915f4d52db82d75e92a8cd8b246e0"></a>

### [`008742ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008742ac.md) → [`008742ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008742ac.md) FUN_008742ac

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
      "definition_site": "008742b0",
      "incomplete_value": false,
      "site": "008742b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008742b0",
      "incomplete_value": false,
      "site": "008742b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "008742b4",
      "DATA",
      [
        "storage",
        "00c04da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008742b4",
      "DATA",
      [
        "storage",
        "00c04e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008742b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008742ac.md#insn-008742b0)
- 新版 `008742b0`（命令位置の公開資料なし）

~~~diff
- 008742b0 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 008742b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008742b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008742b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 008742b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008742b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008742b0 bytes 08a13691
+ 008742b0 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3ff627dd9267398aab9e6771a379c4"></a>

### [`00874328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874328.md) → [`00874328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874328.md) FUN_00874328

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
      "definition_site": "0087433c",
      "incomplete_value": false,
      "site": "00874340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087433c",
      "incomplete_value": false,
      "site": "00874340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00874340",
      "DATA",
      [
        "storage",
        "00c04e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874340",
      "DATA",
      [
        "storage",
        "00c04ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087433c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874328.md#insn-0087433c)
- 新版 `0087433c`（命令位置の公開資料なし）

~~~diff
- 0087433c ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0087433c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087433c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087433c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 0087433c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087433c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087433c bytes 08a13891
+ 0087433c bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfa80bfb0fa54c55e153b23e93c2de43"></a>

### [`0087434c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087434c.md) → [`0087434c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087434c.md) FUN_0087434c

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
      "definition_site": "00874350",
      "incomplete_value": false,
      "site": "00874354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874350",
      "incomplete_value": false,
      "site": "00874354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00874354",
      "DATA",
      [
        "storage",
        "00c04e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874354",
      "DATA",
      [
        "storage",
        "00c04ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087434c.md#insn-00874350)
- 新版 `00874350`（命令位置の公開資料なし）

~~~diff
- 00874350 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00874350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00874350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874350 bytes 08a13891
+ 00874350 bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b6a734ad819266b978d1a61d1211ed"></a>

### [`008743b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743b0.md) → [`008743b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743b0.md) FUN_008743b0

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
      "definition_site": "008743c4",
      "incomplete_value": false,
      "site": "008743c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008743c4",
      "incomplete_value": false,
      "site": "008743c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "008743c8",
      "DATA",
      [
        "storage",
        "00c04ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008743c8",
      "DATA",
      [
        "storage",
        "00c04f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008743c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743b0.md#insn-008743c4)
- 新版 `008743c4`（命令位置の公開資料なし）

~~~diff
- 008743c4 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 008743c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008743c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008743c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 008743c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008743c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008743c4 bytes 08213b91
+ 008743c4 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8040780cb6566a28d14a4b4acaf42d"></a>

### [`008743d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743d4.md) → [`008743d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743d4.md) FUN_008743d4

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
      "definition_site": "008743d8",
      "incomplete_value": false,
      "site": "008743dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008743d8",
      "incomplete_value": false,
      "site": "008743dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "008743dc",
      "DATA",
      [
        "storage",
        "00c04ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008743dc",
      "DATA",
      [
        "storage",
        "00c04f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008743d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743d4.md#insn-008743d8)
- 新版 `008743d8`（命令位置の公開資料なし）

~~~diff
- 008743d8 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 008743d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008743d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008743d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 008743d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008743d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008743d8 bytes 08213b91
+ 008743d8 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c8a66157312df50cbc349d521cb8a13"></a>

### [`008743ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743ec.md) → [`008743ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008743ec.md) FUN_008743ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00833158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00833/00833158.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00833158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874444",
      "incomplete_value": true,
      "site": "00874454",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874444",
      "incomplete_value": true,
      "site": "00874454",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f35:8"
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
      "definition_site": "00874444",
      "incomplete_value": true,
      "site": "00874454",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00874444",
      "incomplete_value": true,
      "site": "00874454",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874474",
      "incomplete_value": true,
      "site": "00874484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874474",
      "incomplete_value": true,
      "site": "00874484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d56:8"
              ]
            ]
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
      "00874444",
      "READ",
      [
        "storage",
        "002acf35",
        null,
        "string"
      ]
    ],
    [
      "00874444",
      "READ",
      [
        "storage",
        "002acf45",
        null,
        "string"
      ]
    ],
    [
      "00874474",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874444",
      "READ",
      [
        "storage",
        "002acf2c",
        null,
        "string"
      ]
    ],
    [
      "00874444",
      "READ",
      [
        "storage",
        "002acf3c",
        null,
        "string"
      ]
    ],
    [
      "00874474",
      "READ",
      [
        "storage",
        "00292de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743ec.md#insn-00874440) · [`0087446c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008743ec.md#insn-0087446c)
- 新版 `00874440`（命令位置の公開資料なし） · `0087446c`（命令位置の公開資料なし）

~~~diff
- 00874440 ["COPY", "tmp:0:8", ["const:f35:8"]]
- 00874440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["COPY", "tmp:0:8", ["const:f2c:8"]]
+ 00874440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874440 bytes 08d53c91
+ 00874440 bytes 08b13c91
- 0087446c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 0087446c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087446c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087446c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["COPY", "tmp:0:8", ["const:de3:8"]]
+ 0087446c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087446c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087446c bytes 29593591
+ 0087446c bytes 298d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2658923071630febbec952df72739c"></a>

### [`00874538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874538.md) → [`00874538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874538.md) FUN_00874538

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
      "definition_site": "0087454c",
      "incomplete_value": false,
      "site": "00874550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087454c",
      "incomplete_value": false,
      "site": "00874550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00874550",
      "DATA",
      [
        "storage",
        "00c04f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874550",
      "DATA",
      [
        "storage",
        "00c04ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087454c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874538.md#insn-0087454c)
- 新版 `0087454c`（命令位置の公開資料なし）

~~~diff
- 0087454c ["COPY", "tmp:0:8", ["const:f48:8"]]
- 0087454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 0087454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087454c bytes 08213d91
+ 0087454c bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcd43cace1bac9f708b7bac794215ffa"></a>

### [`0087455c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087455c.md) → [`0087455c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087455c.md) FUN_0087455c

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
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00874564",
      "DATA",
      [
        "storage",
        "00c04f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874564",
      "DATA",
      [
        "storage",
        "00c04ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087455c.md#insn-00874560)
- 新版 `00874560`（命令位置の公開資料なし）

~~~diff
- 00874560 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00874560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00874560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874560 bytes 08213d91
+ 00874560 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2111c5858befb14dfbc59bc117aad2f"></a>

### [`00874684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874684.md) → [`00874684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874684.md) FUN_00874684

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
      "definition_site": "00874698",
      "incomplete_value": false,
      "site": "0087469c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874698",
      "incomplete_value": false,
      "site": "0087469c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "0087469c",
      "DATA",
      [
        "storage",
        "00c04fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087469c",
      "DATA",
      [
        "storage",
        "00c05088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874684.md#insn-00874694) · [`00874698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874684.md#insn-00874698)
- 新版 `00874694`（命令位置の公開資料なし） · `00874698`（命令位置の公開資料なし）

~~~diff
- 00874694 ["COPY", "register:4040:8", ["const:c04000:8"]]
+ 00874694 ["COPY", "register:4040:8", ["const:c05000:8"]]
- 00874694 bytes 881c0090
+ 00874694 bytes 881c00b0
- 00874698 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00874698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00874698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874698 bytes 08613f91
+ 00874698 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e651a4722945fe80e7e91353021e2d"></a>

### [`008746a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746a8.md) → [`008746a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746a8.md) FUN_008746a8

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
      "definition_site": "008746ac",
      "incomplete_value": false,
      "site": "008746b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008746ac",
      "incomplete_value": false,
      "site": "008746b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c04000:8"
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
      "008746b0",
      "DATA",
      [
        "storage",
        "00c04fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008746b0",
      "DATA",
      [
        "storage",
        "00c05088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008746a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746a8.md#insn-008746a8) · [`008746ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746a8.md#insn-008746ac)
- 新版 `008746a8`（命令位置の公開資料なし） · `008746ac`（命令位置の公開資料なし）

~~~diff
- 008746a8 ["COPY", "register:4040:8", ["const:c04000:8"]]
+ 008746a8 ["COPY", "register:4040:8", ["const:c05000:8"]]
- 008746a8 bytes 881c0090
+ 008746a8 bytes 881c00b0
- 008746ac ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 008746ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008746ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008746ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["COPY", "tmp:0:8", ["const:88:8"]]
+ 008746ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008746ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008746ac bytes 08613f91
+ 008746ac bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab22871893c6eefa86d3374be73fa382"></a>

### [`008746c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746c0.md) → [`008746c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/008746c0.md) FUN_008746c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042c07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874748",
      "incomplete_value": true,
      "site": "0087475c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874748",
      "incomplete_value": true,
      "site": "0087475c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5b:8"
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
      "definition_site": "008747c0",
      "incomplete_value": true,
      "site": "008747c0",
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
                "const:d1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008747c0",
      "incomplete_value": true,
      "site": "008747c0",
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
                "const:d15:8"
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
      "definition_site": "008747b4",
      "incomplete_value": true,
      "site": "008747c4",
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
      "definition_site": "008747b4",
      "incomplete_value": true,
      "site": "008747c4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00874748",
      "READ",
      [
        "storage",
        "002a1b5b",
        null,
        "string"
      ]
    ],
    [
      "008747b0",
      "READ",
      [
        "storage",
        "002aad15",
        null,
        "string"
      ]
    ],
    [
      "008747b4",
      "READ",
      [
        "storage",
        "002aad1c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874748",
      "READ",
      [
        "storage",
        "002a1be8",
        null,
        "string"
      ]
    ],
    [
      "008747b0",
      "READ",
      [
        "storage",
        "002aad1b",
        null,
        "string"
      ]
    ],
    [
      "008747b4",
      "READ",
      [
        "storage",
        "002aad22",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746c0.md#insn-00874740) · [`008747a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/008746c0.md#insn-008747a8)
- 新版 `00874740`（命令位置の公開資料なし） · `008747a8`（命令位置の公開資料なし）

~~~diff
- 00874740 ["COPY", "tmp:0:8", ["const:b5b:8"]]
- 00874740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00874740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874740 bytes 296d2d91
+ 00874740 bytes 29a12f91
- 008747a8 ["COPY", "tmp:0:8", ["const:d15:8"]]
- 008747a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008747a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008747a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008747a8 ["COPY", "tmp:0:8", ["const:d1b:8"]]
+ 008747a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008747a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008747a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008747a8 bytes 29553491
+ 008747a8 bytes 296d3491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1371117a55ca509446e213a2dc87d83"></a>

### [`0087491c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087491c.md) → [`0087491c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/0087491c.md) FUN_0087491c

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
      "definition_site": "00874930",
      "incomplete_value": false,
      "site": "00874934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874930",
      "incomplete_value": false,
      "site": "00874934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00874934",
      "DATA",
      [
        "storage",
        "00c05058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874934",
      "DATA",
      [
        "storage",
        "00c05108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/0087491c.md#insn-00874930)
- 新版 `00874930`（命令位置の公開資料なし）

~~~diff
- 00874930 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00874930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00874930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874930 bytes 08610191
+ 00874930 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-783146968d919a7adb99c0b59b8af868"></a>

### [`00874940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874940.md) → [`00874940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874940.md) FUN_00874940

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
      "definition_site": "00874944",
      "incomplete_value": false,
      "site": "00874948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874944",
      "incomplete_value": false,
      "site": "00874948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00874948",
      "DATA",
      [
        "storage",
        "00c05058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874948",
      "DATA",
      [
        "storage",
        "00c05108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874940.md#insn-00874944)
- 新版 `00874944`（命令位置の公開資料なし）

~~~diff
- 00874944 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00874944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00874944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874944 bytes 08610191
+ 00874944 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d877eccb22cb23010ca4c61e01fd0db"></a>

### [`00874958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874958.md) → [`00874958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874958.md) FUN_00874958

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0042c07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0042c07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c07c.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874a1c",
      "incomplete_value": true,
      "site": "00874a34",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:bfb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874a1c",
      "incomplete_value": true,
      "site": "00874a34",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b6e:8"
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
      "00874a1c",
      "READ",
      [
        "storage",
        "002a1b6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874a1c",
      "READ",
      [
        "storage",
        "002a1bfb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874958.md#insn-00874a14)
- 新版 `00874a14`（命令位置の公開資料なし）

~~~diff
- 00874a14 ["COPY", "tmp:0:8", ["const:b6e:8"]]
- 00874a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["COPY", "tmp:0:8", ["const:bfb:8"]]
+ 00874a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874a14 bytes 29b92d91
+ 00874a14 bytes 29ed2f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf1bcf4528af6652c16b4cbe7f165891"></a>

### [`00874ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md) → [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) FUN_00874ae8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008648a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md) [`00874ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "00874c40",
      "incomplete_value": true,
      "site": "00874c48",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c40",
      "incomplete_value": true,
      "site": "00874c48",
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
      "definition_site": "00874da0",
      "incomplete_value": false,
      "site": "00874da8",
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
      "definition_site": "00874da0",
      "incomplete_value": false,
      "site": "00874da8",
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
      "definition_site": "00874e48",
      "incomplete_value": false,
      "site": "00874e54",
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
      "definition_site": "00874e48",
      "incomplete_value": false,
      "site": "00874e54",
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
      "00874c40",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00874da0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00874e48",
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
      "00874c40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00874da0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00874e48",
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

- 旧版 [`00874c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md#insn-00874c40) · [`00874da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md#insn-00874da0) · [`00874e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md#insn-00874e48)
- 新版 `00874c40`（命令位置の公開資料なし） · `00874da0`（命令位置の公開資料なし） · `00874e48`（命令位置の公開資料なし）

~~~diff
- 00874c40 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00874c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00874c40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874c40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874c40 bytes 21440c91
+ 00874c40 bytes 21280c91
- 00874da0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00874da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00874da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874da0 bytes 21d40b91
+ 00874da0 bytes 21b80b91
- 00874e48 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00874e48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00874e48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00874e48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00874e48 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00874e48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00874e48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00874e48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00874e48 bytes 21681f91
+ 00874e48 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00233827eef4d1ee0f16016ce7be82d9"></a>

### [`008752f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/008752f4.md) → [`008752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md) FUN_008752f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`008648a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) [`00874ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00874/00874ae8.md) [`008752f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/008752f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`00874ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00874/00874ae8.md) [`008752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/008752f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00875444",
      "incomplete_value": false,
      "site": "0087544c",
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
      "definition_site": "00875444",
      "incomplete_value": false,
      "site": "0087544c",
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
      "definition_site": "008755a0",
      "incomplete_value": false,
      "site": "008755a8",
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
      "definition_site": "008755a0",
      "incomplete_value": false,
      "site": "008755a8",
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
      "definition_site": "00875644",
      "incomplete_value": false,
      "site": "00875650",
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
      "definition_site": "00875644",
      "incomplete_value": false,
      "site": "00875650",
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
      "00875444",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008755a0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00875644",
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
      "00875444",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008755a0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00875644",
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

- 旧版 [`00875444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/008752f4.md#insn-00875444) · [`008755a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/008752f4.md#insn-008755a0) · [`00875644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/008752f4.md#insn-00875644)
- 新版 `00875444`（命令位置の公開資料なし） · `008755a0`（命令位置の公開資料なし） · `00875644`（命令位置の公開資料なし）

~~~diff
- 00875444 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00875444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00875444 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875444 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875444 bytes 21440c91
+ 00875444 bytes 21280c91
- 008755a0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008755a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008755a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008755a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008755a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008755a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008755a0 bytes 21d40b91
+ 008755a0 bytes 21b80b91
- 00875644 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00875644 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875644 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875644 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875644 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00875644 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875644 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875644 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875644 bytes 21681f91
+ 00875644 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0205147283c2884ddcc325c859f3f11"></a>

### [`00875c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md) → [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) FUN_00875c24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00875adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875adc.md) [`00875c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00875adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875adc.md) [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00875da0",
      "incomplete_value": false,
      "site": "00875da8",
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
      "definition_site": "00875da0",
      "incomplete_value": false,
      "site": "00875da8",
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
      "definition_site": "00875e68",
      "incomplete_value": false,
      "site": "00875e70",
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
      "definition_site": "00875e68",
      "incomplete_value": false,
      "site": "00875e70",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00876304",
      "incomplete_value": false,
      "site": "00876310",
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
      "definition_site": "00876304",
      "incomplete_value": false,
      "site": "00876310",
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
      "00875da0",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00875e68",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00876190",
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00875da0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00875e68",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00876190",
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md#insn-00875da0) · [`00875e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md#insn-00875e68) · [`00876190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md#insn-00876190)
- 新版 `00875da0`（命令位置の公開資料なし） · `00875e68`（命令位置の公開資料なし） · `00876190`（命令位置の公開資料なし）

~~~diff
- 00875da0 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00875da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00875da0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875da0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875da0 bytes 21440c91
+ 00875da0 bytes 21280c91
- 00875e68 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00875e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00875e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00875e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00875e68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00875e68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00875e68 bytes 21d40b91
+ 00875e68 bytes 21b80b91
- 00876190 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00876190 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00876190 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00876190 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00876190 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00876190 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00876190 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00876190 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00876190 bytes 63941791
+ 00876190 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3a73226cdeef626414ddce10855088"></a>

### [`00876698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md) → [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) FUN_00876698

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00875c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00875/00875c24.md) [`00876698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00875c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00875/00875c24.md) [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008767fc",
      "incomplete_value": false,
      "site": "00876804",
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
      "definition_site": "008767fc",
      "incomplete_value": false,
      "site": "00876804",
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
      "definition_site": "0087695c",
      "incomplete_value": false,
      "site": "00876964",
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
      "definition_site": "0087695c",
      "incomplete_value": false,
      "site": "00876964",
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
      "definition_site": "00876c78",
      "incomplete_value": false,
      "site": "00876c88",
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
      "definition_site": "00876c78",
      "incomplete_value": false,
      "site": "00876c88",
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
      "008767fc",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087695c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00876a04",
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
      "008767fc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087695c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00876a04",
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

- 旧版 [`008767fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md#insn-008767fc) · [`0087695c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md#insn-0087695c) · [`00876a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md#insn-00876a04)
- 新版 `008767fc`（命令位置の公開資料なし） · `0087695c`（命令位置の公開資料なし） · `00876a04`（命令位置の公開資料なし）

~~~diff
- 008767fc ["COPY", "tmp:0:8", ["const:311:8"]]
- 008767fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008767fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008767fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008767fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008767fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008767fc bytes 21440c91
+ 008767fc bytes 21280c91
- 0087695c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087695c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087695c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087695c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087695c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087695c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087695c bytes 21d40b91
+ 0087695c bytes 21b80b91
- 00876a04 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00876a04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00876a04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00876a04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00876a04 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00876a04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00876a04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00876a04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00876a04 bytes 21681f91
+ 00876a04 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1326c4959828855da0af7d0eea56149f"></a>

### [`00877014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877014.md) → [`00877014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md) FUN_00877014

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00876698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00876/00876698.md) [`00877014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877014.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00876698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00876/00876698.md) [`00877014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877014.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087716c",
      "incomplete_value": false,
      "site": "00877174",
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
      "definition_site": "0087716c",
      "incomplete_value": false,
      "site": "00877174",
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
      "definition_site": "008772c8",
      "incomplete_value": false,
      "site": "008772d0",
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
      "definition_site": "008772c8",
      "incomplete_value": false,
      "site": "008772d0",
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
      "definition_site": "0087736c",
      "incomplete_value": false,
      "site": "00877378",
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
      "definition_site": "0087736c",
      "incomplete_value": false,
      "site": "00877378",
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
      "0087716c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "008772c8",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087736c",
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
      "0087716c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008772c8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087736c",
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

- 旧版 [`0087716c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877014.md#insn-0087716c) · [`008772c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877014.md#insn-008772c8) · [`0087736c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877014.md#insn-0087736c)
- 新版 `0087716c`（命令位置の公開資料なし） · `008772c8`（命令位置の公開資料なし） · `0087736c`（命令位置の公開資料なし）

~~~diff
- 0087716c ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087716c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087716c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087716c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087716c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087716c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087716c bytes 21440c91
+ 0087716c bytes 21280c91
- 008772c8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 008772c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008772c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008772c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 008772c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008772c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008772c8 bytes 21d40b91
+ 008772c8 bytes 21b80b91
- 0087736c ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087736c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087736c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087736c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087736c ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087736c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087736c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087736c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087736c bytes 21681f91
+ 0087736c bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de60a060f72db364b7d5e1d1c66feec0"></a>

### [`0087796c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/0087796c.md) → [`0087796c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/0087796c.md) FUN_0087796c

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
      "definition_site": "00877980",
      "incomplete_value": false,
      "site": "00877984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877980",
      "incomplete_value": false,
      "site": "00877984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00877984",
      "DATA",
      [
        "storage",
        "00c050d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877984",
      "DATA",
      [
        "storage",
        "00c05188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/0087796c.md#insn-00877980)
- 新版 `00877980`（命令位置の公開資料なし）

~~~diff
- 00877980 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00877980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00877980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877980 bytes 08610391
+ 00877980 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fadce27adfcbcfc9ae1f35e4904e3c"></a>

### [`00877990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877990.md) → [`00877990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877990.md) FUN_00877990

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
      "definition_site": "00877994",
      "incomplete_value": false,
      "site": "00877998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877994",
      "incomplete_value": false,
      "site": "00877998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00877998",
      "DATA",
      [
        "storage",
        "00c050d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877998",
      "DATA",
      [
        "storage",
        "00c05188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877990.md#insn-00877994)
- 新版 `00877994`（命令位置の公開資料なし）

~~~diff
- 00877994 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00877994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00877994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877994 bytes 08610391
+ 00877994 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b790b67aa2b0e397a1eb8f27f7d84fc8"></a>

### [`008779f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/008779f4.md) → [`008779f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/008779f4.md) FUN_008779f4

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
      "definition_site": "00877a18",
      "incomplete_value": false,
      "site": "00877a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877a18",
      "incomplete_value": false,
      "site": "00877a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00877a18",
      "DATA",
      [
        "storage",
        "00c05158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877a18",
      "DATA",
      [
        "storage",
        "00c05208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/008779f4.md#insn-00877a14)
- 新版 `00877a14`（命令位置の公開資料なし）

~~~diff
- 00877a14 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00877a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00877a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00877a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00877a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00877a14 bytes 08610591
+ 00877a14 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8988df13cbac30b001d1ec332f5fe2"></a>

### [`00877a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md) → [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) FUN_00877a44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449b7c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00877aa8",
      "incomplete_value": true,
      "site": "00877aa8",
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
                "const:b0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877aa8",
      "incomplete_value": true,
      "site": "00877aa8",
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
                "const:a7d:8"
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
      "definition_site": "00877aac",
      "incomplete_value": true,
      "site": "00877aac",
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
      "definition_site": "00877aac",
      "incomplete_value": true,
      "site": "00877aac",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00877b04",
      "incomplete_value": false,
      "site": "00877b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877b04",
      "incomplete_value": false,
      "site": "00877b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "00877a74",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24cb8",
        null,
        "undefined4"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24cbc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00877a74",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00877a80",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md#insn-00877a74) · [`00877a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md#insn-00877a90) · [`00877afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00877/00877a44.md#insn-00877afc)
- 新版 `00877a74`（命令位置の公開資料なし） · `00877a90`（命令位置の公開資料なし） · `00877afc`（命令位置の公開資料なし）

~~~diff
- 00877a74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
- 00877a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00877a74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
+ 00877a74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00877a74 bytes 293d46f9
+ 00877a74 bytes 299546f9
- 00877a90 ["COPY", "tmp:0:8", ["const:a7d:8"]]
- 00877a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["COPY", "tmp:0:8", ["const:b0a:8"]]
+ 00877a90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877a90 bytes 29f52991
+ 00877a90 bytes 29292c91
- 00877afc ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00877afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00877afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877afc bytes 29210791
+ 00877afc bytes 29e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0cc133927101158b057d5785e31f37a"></a>

### [`008786ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008786ac.md) → [`008786ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786ac.md) FUN_008786ac

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
      "definition_site": "008786cc",
      "incomplete_value": false,
      "site": "008786d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008786cc",
      "incomplete_value": false,
      "site": "008786d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008786d0",
      "DATA",
      [
        "storage",
        "00c051c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008786d0",
      "DATA",
      [
        "storage",
        "00c05278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008786cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008786ac.md#insn-008786cc)
- 新版 `008786cc`（命令位置の公開資料なし）

~~~diff
- 008786cc ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 008786cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008786cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008786cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["COPY", "tmp:0:8", ["const:278:8"]]
+ 008786cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008786cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008786cc bytes 08210791
+ 008786cc bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f6470a715bea804295bcf8ef98340cc"></a>

### [`008786e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008786e4.md) → [`008786e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008786e4.md) FUN_008786e4

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
      "definition_site": "008786e8",
      "incomplete_value": false,
      "site": "008786ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008786e8",
      "incomplete_value": false,
      "site": "008786ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008786ec",
      "DATA",
      [
        "storage",
        "00c051c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008786ec",
      "DATA",
      [
        "storage",
        "00c05278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008786e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008786e4.md#insn-008786e8)
- 新版 `008786e8`（命令位置の公開資料なし）

~~~diff
- 008786e8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 008786e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008786e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008786e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 008786e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008786e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008786e8 bytes 08210791
+ 008786e8 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd59d5201fc934c83b26b3008f1f7d7"></a>

### [`0087898c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/0087898c.md) → [`0087898c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/0087898c.md) FUN_0087898c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008780d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008780d4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008780d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008780d4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00878998",
      "incomplete_value": false,
      "site": "0087899c",
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
      "definition_site": "00878998",
      "incomplete_value": false,
      "site": "0087899c",
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
      "00878998",
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
      "00878998",
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

- 旧版 [`00878998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/0087898c.md#insn-00878998)
- 新版 `00878998`（命令位置の公開資料なし）

~~~diff
- 00878998 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00878998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00878998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00878998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00878998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00878998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00878998 bytes 00280c91
+ 00878998 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc2cdece5e010f50c75e31c861f3b0e"></a>

### [`008789a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008789a4.md) → [`008789a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789a4.md) FUN_008789a4

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
      "definition_site": "008789b8",
      "incomplete_value": false,
      "site": "008789bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008789b8",
      "incomplete_value": false,
      "site": "008789bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "008789bc",
      "DATA",
      [
        "storage",
        "00c05258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008789bc",
      "DATA",
      [
        "storage",
        "00c05308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008789b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008789a4.md#insn-008789b8)
- 新版 `008789b8`（命令位置の公開資料なし）

~~~diff
- 008789b8 ["COPY", "tmp:0:8", ["const:258:8"]]
- 008789b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008789b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008789b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 008789b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008789b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008789b8 bytes 08610991
+ 008789b8 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320e965545c262398653b901afc5c9d7"></a>

### [`008789c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008789c8.md) → [`008789c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/008789c8.md) FUN_008789c8

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
      "definition_site": "008789cc",
      "incomplete_value": false,
      "site": "008789d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008789cc",
      "incomplete_value": false,
      "site": "008789d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "008789d0",
      "DATA",
      [
        "storage",
        "00c05258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008789d0",
      "DATA",
      [
        "storage",
        "00c05308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008789cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/008789c8.md#insn-008789cc)
- 新版 `008789cc`（命令位置の公開資料なし）

~~~diff
- 008789cc ["COPY", "tmp:0:8", ["const:258:8"]]
- 008789cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008789cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008789cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["COPY", "tmp:0:8", ["const:308:8"]]
+ 008789cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008789cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008789cc bytes 08610991
+ 008789cc bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0739d6b7a537e4eaf81a9928fe701b67"></a>

### [`00878a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878a6c.md) → [`00878a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878a6c.md) FUN_00878a6c

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
      "definition_site": "00878a70",
      "incomplete_value": false,
      "site": "00878a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878a70",
      "incomplete_value": false,
      "site": "00878a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00878a74",
      "DATA",
      [
        "storage",
        "00c052d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00878a74",
      "DATA",
      [
        "storage",
        "00c05388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878a6c.md#insn-00878a70)
- 新版 `00878a70`（命令位置の公開資料なし）

~~~diff
- 00878a70 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00878a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00878a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00878a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00878a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00878a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00878a70 bytes 08610b91
+ 00878a70 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8fa6ddb68d0356d780d5f6d9f9d968"></a>

### [`00878ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878ac4.md) → [`00878ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878ac4.md) FUN_00878ac4

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
      "definition_site": "00878ae8",
      "incomplete_value": false,
      "site": "00878ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878ae8",
      "incomplete_value": false,
      "site": "00878ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00878ae8",
      "DATA",
      [
        "storage",
        "00c05358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00878ae8",
      "DATA",
      [
        "storage",
        "00c05408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878ac4.md#insn-00878ae4)
- 新版 `00878ae4`（命令位置の公開資料なし）

~~~diff
- 00878ae4 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00878ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00878ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00878ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00878ae4 bytes 08610d91
+ 00878ae4 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c3e2c316bf1ae5f898141d5b9e9ab1f"></a>

### [`00878b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md) → [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) FUN_00878b14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449b7c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.41% / 新版 95.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00878b78",
      "incomplete_value": true,
      "site": "00878b78",
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
                "const:b0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878b78",
      "incomplete_value": true,
      "site": "00878b78",
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
                "const:a7d:8"
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
      "definition_site": "00878b7c",
      "incomplete_value": true,
      "site": "00878b7c",
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
      "definition_site": "00878b7c",
      "incomplete_value": true,
      "site": "00878b7c",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878bd4",
      "incomplete_value": false,
      "site": "00878bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878bd4",
      "incomplete_value": false,
      "site": "00878bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "00878b44",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24cb8",
        null,
        "undefined4"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24cbc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00878b44",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00878b50",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md#insn-00878b44) · [`00878b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md#insn-00878b60) · [`00878bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878b14.md#insn-00878bcc)
- 新版 `00878b44`（命令位置の公開資料なし） · `00878b60`（命令位置の公開資料なし） · `00878bcc`（命令位置の公開資料なし）

~~~diff
- 00878b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
- 00878b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00878b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
+ 00878b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00878b44 bytes 293d46f9
+ 00878b44 bytes 299546f9
- 00878b60 ["COPY", "tmp:0:8", ["const:a7d:8"]]
- 00878b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00878b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00878b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["COPY", "tmp:0:8", ["const:b0a:8"]]
+ 00878b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00878b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00878b60 bytes 29f52991
+ 00878b60 bytes 29292c91
- 00878bcc ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 00878bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00878bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00878bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00878bcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00878bcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00878bcc bytes 29210f91
+ 00878bcc bytes 29e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ad2a6827429a27776445526ab78c4a"></a>

### [`00879758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879758.md) → [`00879758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879758.md) FUN_00879758

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
      "definition_site": "0087975c",
      "incomplete_value": false,
      "site": "00879760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087975c",
      "incomplete_value": false,
      "site": "00879760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "00879760",
      "DATA",
      [
        "storage",
        "00c053c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879760",
      "DATA",
      [
        "storage",
        "00c05478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087975c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879758.md#insn-0087975c)
- 新版 `0087975c`（命令位置の公開資料なし）

~~~diff
- 0087975c ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0087975c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087975c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087975c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["COPY", "tmp:0:8", ["const:478:8"]]
+ 0087975c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087975c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087975c bytes 08210f91
+ 0087975c bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952ecfde6d257a1b97d3c1e5dab24132"></a>

### [`00879a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a00.md) → [`00879a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a00.md) FUN_00879a00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087919c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/0087919c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0087919c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/0087919c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00879a0c",
      "incomplete_value": false,
      "site": "00879a10",
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
      "definition_site": "00879a0c",
      "incomplete_value": false,
      "site": "00879a10",
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
      "00879a0c",
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
      "00879a0c",
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

- 旧版 [`00879a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a00.md#insn-00879a0c)
- 新版 `00879a0c`（命令位置の公開資料なし）

~~~diff
- 00879a0c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00879a0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00879a0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00879a0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00879a0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00879a0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00879a0c bytes 00280c91
+ 00879a0c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bc1cf8a28c991ea815c2bee80639a05"></a>

### [`00879a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a18.md) → [`00879a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a18.md) FUN_00879a18

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
      "definition_site": "00879a2c",
      "incomplete_value": false,
      "site": "00879a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879a2c",
      "incomplete_value": false,
      "site": "00879a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "00879a30",
      "DATA",
      [
        "storage",
        "00c05458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879a30",
      "DATA",
      [
        "storage",
        "00c05508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a18.md#insn-00879a2c)
- 新版 `00879a2c`（命令位置の公開資料なし）

~~~diff
- 00879a2c ["COPY", "tmp:0:8", ["const:458:8"]]
- 00879a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00879a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879a2c bytes 08611191
+ 00879a2c bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-392cbdff09bd8ab304ba0ab972ff2fdb"></a>

### [`00879a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a3c.md) → [`00879a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879a3c.md) FUN_00879a3c

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
      "definition_site": "00879a40",
      "incomplete_value": false,
      "site": "00879a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879a40",
      "incomplete_value": false,
      "site": "00879a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "00879a44",
      "DATA",
      [
        "storage",
        "00c05458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879a44",
      "DATA",
      [
        "storage",
        "00c05508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879a3c.md#insn-00879a40)
- 新版 `00879a40`（命令位置の公開資料なし）

~~~diff
- 00879a40 ["COPY", "tmp:0:8", ["const:458:8"]]
- 00879a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00879a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879a40 bytes 08611191
+ 00879a40 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5728ed72c98412e8864060c53bf0d97b"></a>

### [`00879ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879ac8.md) → [`00879ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879ac8.md) FUN_00879ac8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879adc",
      "incomplete_value": true,
      "site": "00879ae0",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879adc",
      "incomplete_value": true,
      "site": "00879ae0",
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
            "const:4d8:8"
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
      "00879ae0",
      "DATA",
      [
        "storage",
        "00c054d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879ae0",
      "DATA",
      [
        "storage",
        "00c05588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879ac8.md#insn-00879adc)
- 新版 `00879adc`（命令位置の公開資料なし）

~~~diff
- 00879adc ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00879adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00879adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879adc bytes 08611391
+ 00879adc bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3c61c82bfe566a3d62f326f3edfd9b6"></a>

### [`00879aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879aec.md) → [`00879aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879aec.md) FUN_00879aec

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
      "definition_site": "00879af0",
      "incomplete_value": true,
      "site": "00879af4",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879af0",
      "incomplete_value": true,
      "site": "00879af4",
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
            "const:4d8:8"
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
      "00879af4",
      "DATA",
      [
        "storage",
        "00c054d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879af4",
      "DATA",
      [
        "storage",
        "00c05588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879aec.md#insn-00879af0)
- 新版 `00879af0`（命令位置の公開資料なし）

~~~diff
- 00879af0 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00879af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00879af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879af0 bytes 08611391
+ 00879af0 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d43ead6c1b8f906e2b56c3bdb220bc0"></a>

### [`00879b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b58.md) → [`00879b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b58.md) FUN_00879b58

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
      "definition_site": "00879b5c",
      "incomplete_value": false,
      "site": "00879b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879b5c",
      "incomplete_value": false,
      "site": "00879b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
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
      "00879b60",
      "DATA",
      [
        "storage",
        "00c05558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879b60",
      "DATA",
      [
        "storage",
        "00c05608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b58.md#insn-00879b5c)
- 新版 `00879b5c`（命令位置の公開資料なし）

~~~diff
- 00879b5c ["COPY", "tmp:0:8", ["const:558:8"]]
- 00879b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00879b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879b5c bytes 08611591
+ 00879b5c bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d43d7978eddd848fd08627e40770ff5"></a>

### [`00879b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b70.md) → [`00879b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879b70.md) FUN_00879b70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`008309c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00830/008309c8.md) [`00879df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879df0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`008309c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/008309c8.md) [`00879df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879df0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00879c5c",
      "incomplete_value": false,
      "site": "00879c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879c5c",
      "incomplete_value": false,
      "site": "00879c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00879c38",
      "READ",
      [
        "storage",
        "002a88ee",
        null,
        "string"
      ]
    ],
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a7aff",
        null,
        "string"
      ]
    ],
    [
      "00879c3c",
      "READ",
      [
        "storage",
        "002a88fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a885a",
        null,
        "string"
      ]
    ],
    [
      "00879c38",
      "READ",
      [
        "storage",
        "002a7a6b",
        null,
        "string"
      ]
    ],
    [
      "00879c3c",
      "READ",
      [
        "storage",
        "002a8867",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b70.md#insn-00879c18) · [`00879c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b70.md#insn-00879c24) · [`00879c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879b70.md#insn-00879c5c)
- 新版 `00879c18`（命令位置の公開資料なし） · `00879c24`（命令位置の公開資料なし） · `00879c5c`（命令位置の公開資料なし）

~~~diff
- 00879c18 ["COPY", "tmp:0:8", ["const:8ee:8"]]
- 00879c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["COPY", "tmp:0:8", ["const:85a:8"]]
+ 00879c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879c18 bytes 08b92391
+ 00879c18 bytes 08692191
- 00879c24 ["COPY", "tmp:0:8", ["const:aff:8"]]
- 00879c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["COPY", "tmp:0:8", ["const:a6b:8"]]
+ 00879c24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879c24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879c24 bytes 29fd2b91
+ 00879c24 bytes 29ad2991
- 00879c5c ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00879c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00879c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879c5c bytes 08211791
+ 00879c5c bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250fe2564ffb8bff44518488ebc6266d"></a>

### [`00879dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879dbc.md) → [`00879dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879dbc.md) FUN_00879dbc

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
      "definition_site": "00879dd0",
      "incomplete_value": false,
      "site": "00879dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879dd0",
      "incomplete_value": false,
      "site": "00879dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00879dd4",
      "DATA",
      [
        "storage",
        "00c055c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879dd4",
      "DATA",
      [
        "storage",
        "00c05678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879dbc.md#insn-00879dd0)
- 新版 `00879dd0`（命令位置の公開資料なし）

~~~diff
- 00879dd0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00879dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00879dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879dd0 bytes 08211791
+ 00879dd0 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-112356f08db5421b3324462340d4c67f"></a>

### [`00879de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879de0.md) → [`00879de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879de0.md) FUN_00879de0

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
      "definition_site": "00879de4",
      "incomplete_value": false,
      "site": "00879de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879de4",
      "incomplete_value": false,
      "site": "00879de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00879de8",
      "DATA",
      [
        "storage",
        "00c055c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879de8",
      "DATA",
      [
        "storage",
        "00c05678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879de0.md#insn-00879de4)
- 新版 `00879de4`（命令位置の公開資料なし）

~~~diff
- 00879de4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00879de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00879de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879de4 bytes 08211791
+ 00879de4 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da3fe0dc1cfccb081c846cb97f2061a7"></a>

### [`00879e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879e6c.md) → [`00879e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879e6c.md) FUN_00879e6c

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
      "definition_site": "00879e80",
      "incomplete_value": false,
      "site": "00879e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e80",
      "incomplete_value": false,
      "site": "00879e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00879e84",
      "DATA",
      [
        "storage",
        "00c05658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879e84",
      "DATA",
      [
        "storage",
        "00c05708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879e6c.md#insn-00879e80)
- 新版 `00879e80`（命令位置の公開資料なし）

~~~diff
- 00879e80 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00879e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00879e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879e80 bytes 08611991
+ 00879e80 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b555bd9237536b9d1bc26804f7fd0c1"></a>

### [`00879e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879e90.md) → [`00879e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879e90.md) FUN_00879e90

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
      "definition_site": "00879e94",
      "incomplete_value": false,
      "site": "00879e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e94",
      "incomplete_value": false,
      "site": "00879e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00879e98",
      "DATA",
      [
        "storage",
        "00c05658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879e98",
      "DATA",
      [
        "storage",
        "00c05708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879e90.md#insn-00879e94)
- 新版 `00879e94`（命令位置の公開資料なし）

~~~diff
- 00879e94 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00879e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879e94 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00879e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879e94 bytes 08611991
+ 00879e94 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b536dcd30291b24e775332cf7e74e31"></a>

### [`00879fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fa8.md) → [`00879fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fa8.md) FUN_00879fa8

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
      "definition_site": "00879fbc",
      "incomplete_value": false,
      "site": "00879fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879fbc",
      "incomplete_value": false,
      "site": "00879fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00879fc0",
      "DATA",
      [
        "storage",
        "00c056c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879fc0",
      "DATA",
      [
        "storage",
        "00c05778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fa8.md#insn-00879fbc)
- 新版 `00879fbc`（命令位置の公開資料なし）

~~~diff
- 00879fbc ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00879fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00879fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879fbc bytes 08211b91
+ 00879fbc bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265b27b6fcebcbc908b806ed693fd4bc"></a>

### [`00879fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fcc.md) → [`00879fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fcc.md) FUN_00879fcc

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
      "definition_site": "00879fd0",
      "incomplete_value": false,
      "site": "00879fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879fd0",
      "incomplete_value": false,
      "site": "00879fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00879fd4",
      "DATA",
      [
        "storage",
        "00c056c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00879fd4",
      "DATA",
      [
        "storage",
        "00c05778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fcc.md#insn-00879fd0)
- 新版 `00879fd0`（命令位置の公開資料なし）

~~~diff
- 00879fd0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00879fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00879fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00879fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00879fd0 bytes 08211b91
+ 00879fd0 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a86c8fc1872ae6a04dce94acdbb1f2"></a>

### [`00879fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fe4.md) → [`00879fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879fe4.md) FUN_00879fe4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0087a124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a124.md) [`0087a128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a128.md) [`00ada6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada6ac.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0087a124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a124.md) [`0087a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a128.md) [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0087a010",
      "incomplete_value": false,
      "site": "0087a018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a010",
      "incomplete_value": false,
      "site": "0087a018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0087a018",
      "DATA",
      [
        "storage",
        "00c05738",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05758",
        null,
        "pointer"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a018",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05808",
        null,
        "pointer"
      ]
    ],
    [
      "0087a04c",
      "READ",
      [
        "storage",
        "00c05810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879fe4.md#insn-0087a010)
- 新版 `0087a010`（命令位置の公開資料なし）

~~~diff
- 0087a010 ["COPY", "tmp:0:8", ["const:738:8"]]
- 0087a010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0087a010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a010 bytes 08e11c91
+ 0087a010 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cec257096340909e6a7851f2ba37d1f"></a>

### [`0087a0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a0f0.md) → [`0087a0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a0f0.md) FUN_0087a0f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a104",
      "incomplete_value": true,
      "site": "0087a108",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a104",
      "incomplete_value": true,
      "site": "0087a108",
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
            "const:738:8"
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
      "0087a108",
      "DATA",
      [
        "storage",
        "00c05738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a108",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a0f0.md#insn-0087a104)
- 新版 `0087a104`（命令位置の公開資料なし）

~~~diff
- 0087a104 ["COPY", "tmp:0:8", ["const:738:8"]]
- 0087a104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0087a104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a104 bytes 08e11c91
+ 0087a104 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e60d92f1bd769ebca29293266239b23"></a>

### [`0087a114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a114.md) → [`0087a114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a114.md) FUN_0087a114

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
      "definition_site": "0087a118",
      "incomplete_value": false,
      "site": "0087a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a118",
      "incomplete_value": false,
      "site": "0087a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0087a11c",
      "DATA",
      [
        "storage",
        "00c05738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a11c",
      "DATA",
      [
        "storage",
        "00c057e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a114.md#insn-0087a118)
- 新版 `0087a118`（命令位置の公開資料なし）

~~~diff
- 0087a118 ["COPY", "tmp:0:8", ["const:738:8"]]
- 0087a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0087a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a118 bytes 08e11c91
+ 0087a118 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe936ea7a4806065c88690f018a32bb"></a>

### [`0087a12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a12c.md) → [`0087a12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a12c.md) FUN_0087a12c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f2/006f23b4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a274",
      "incomplete_value": false,
      "site": "0087a274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a274",
      "incomplete_value": false,
      "site": "0087a274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "0087a19c",
      "READ",
      [
        "storage",
        "00293b96",
        null,
        "string"
      ]
    ],
    [
      "0087a274",
      "DATA",
      [
        "storage",
        "00c057a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a2cc",
      "READ",
      [
        "storage",
        "00c057c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087a19c",
      "READ",
      [
        "storage",
        "00293c23",
        null,
        "string"
      ]
    ],
    [
      "0087a274",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ],
    [
      "0087a2cc",
      "READ",
      [
        "storage",
        "00c05878",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a12c.md#insn-0087a194) · [`0087a26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a12c.md#insn-0087a26c) · [`0087a270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a12c.md#insn-0087a270)
- 新版 `0087a194`（命令位置の公開資料なし） · `0087a26c`（命令位置の公開資料なし）

~~~diff
- 0087a194 ["COPY", "tmp:0:8", ["const:b96:8"]]
- 0087a194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087a194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087a194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["COPY", "tmp:0:8", ["const:c23:8"]]
+ 0087a194 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087a194 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087a194 bytes 29592e91
+ 0087a194 bytes 298d3091
- 0087a26c ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0087a26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0087a26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a26c bytes 08a11e91
+ 0087a26c bytes 08612191
- 0087a270 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
- 0087a270 bytes b30301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a4aa37e7c972774a18d7cfd15f8770"></a>

### [`0087a4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a4d4.md) → [`0087a4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a4d4.md) FUN_0087a4d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a4e8",
      "incomplete_value": true,
      "site": "0087a4ec",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a4e8",
      "incomplete_value": true,
      "site": "0087a4ec",
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
            "const:7a8:8"
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
      "0087a4ec",
      "DATA",
      [
        "storage",
        "00c057a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a4ec",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a4d4.md#insn-0087a4e8)
- 新版 `0087a4e8`（命令位置の公開資料なし）

~~~diff
- 0087a4e8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0087a4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0087a4e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a4e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a4e8 bytes 08a11e91
+ 0087a4e8 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a6ca02c38585b2e1f02b9fdf545c8f6"></a>

### [`0087a584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a584.md) → [`0087a584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a584.md) FUN_0087a584

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
      "definition_site": "0087a598",
      "incomplete_value": false,
      "site": "0087a59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a598",
      "incomplete_value": false,
      "site": "0087a59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0087a59c",
      "DATA",
      [
        "storage",
        "00c05858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087a59c",
      "DATA",
      [
        "storage",
        "00c05908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a584.md#insn-0087a598)
- 新版 `0087a598`（命令位置の公開資料なし）

~~~diff
- 0087a598 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0087a598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 0087a598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a598 bytes 08612191
+ 0087a598 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f3de2999b8a84d695bc765b8bc7489"></a>

### [`0087a5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a5c0.md) → [`0087a5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087a5c0.md) FUN_0087a5c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md)
- 新版 呼出元 0件  · 呼出先 20件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:152:8"
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
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0087a658",
      "incomplete_value": true,
      "site": "0087a668",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0087a6e4",
      "incomplete_value": true,
      "site": "0087a6f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087a6e4",
      "incomplete_value": true,
      "site": "0087a6f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2de:8"
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
      "0087a658",
      "READ",
      [
        "storage",
        "00297152",
        null,
        "string"
      ]
    ],
    [
      "0087a658",
      "READ",
      [
        "storage",
        "00297162",
        null,
        "string"
      ]
    ],
    [
      "0087a6e4",
      "READ",
      [
        "storage",
        "0029a2de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087a658",
      "READ",
      [
        "storage",
        "002971df",
        null,
        "string"
      ]
    ],
    [
      "0087a658",
      "READ",
      [
        "storage",
        "002971ef",
        null,
        "string"
      ]
    ],
    [
      "0087a6e4",
      "READ",
      [
        "storage",
        "0029a36b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087a650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a5c0.md#insn-0087a650) · [`0087a654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087a5c0.md#insn-0087a654)
- 新版 `0087a650`（命令位置の公開資料なし） · `0087a654`（命令位置の公開資料なし）

~~~diff
- 0087a650 ["COPY", "tmp:0:8", ["const:152:8"]]
- 0087a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["COPY", "tmp:0:8", ["const:1df:8"]]
+ 0087a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087a650 bytes 08490591
+ 0087a650 bytes 087d0791
- 0087a654 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0087a654 bytes a9d1fff0
+ 0087a654 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0087a654 bytes a9d1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b57bde0e0237f1f4880269affe540af0"></a>

### [`0087aa04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa04.md) → [`0087aa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa04.md) FUN_0087aa04

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
      "definition_site": "0087aa18",
      "incomplete_value": false,
      "site": "0087aa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa18",
      "incomplete_value": false,
      "site": "0087aa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0087aa1c",
      "DATA",
      [
        "storage",
        "00c058c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa1c",
      "DATA",
      [
        "storage",
        "00c05978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa04.md#insn-0087aa18)
- 新版 `0087aa18`（命令位置の公開資料なし）

~~~diff
- 0087aa18 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0087aa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 0087aa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa18 bytes 08212391
+ 0087aa18 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f1a664a685e13410d79fee7e99d61bf"></a>

### [`0087aa28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa28.md) → [`0087aa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa28.md) FUN_0087aa28

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
      "definition_site": "0087aa2c",
      "incomplete_value": false,
      "site": "0087aa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa2c",
      "incomplete_value": false,
      "site": "0087aa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0087aa30",
      "DATA",
      [
        "storage",
        "00c058c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa30",
      "DATA",
      [
        "storage",
        "00c05978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa28.md#insn-0087aa2c)
- 新版 `0087aa2c`（命令位置の公開資料なし）

~~~diff
- 0087aa2c ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0087aa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["COPY", "tmp:0:8", ["const:978:8"]]
+ 0087aa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa2c bytes 08212391
+ 0087aa2c bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-586dd3449f4508b07132f325bdd0ff8e"></a>

### [`0087aa84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa84.md) → [`0087aa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aa84.md) FUN_0087aa84

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
      "definition_site": "0087aa98",
      "incomplete_value": false,
      "site": "0087aa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa98",
      "incomplete_value": false,
      "site": "0087aa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0087aa9c",
      "DATA",
      [
        "storage",
        "00c05948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa9c",
      "DATA",
      [
        "storage",
        "00c059f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aa84.md#insn-0087aa98)
- 新版 `0087aa98`（命令位置の公開資料なし）

~~~diff
- 0087aa98 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0087aa98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 0087aa98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aa98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aa98 bytes 08212591
+ 0087aa98 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdf5e8b05236fe6a590d96f863f4bf52"></a>

### [`0087aaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aaa8.md) → [`0087aaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087aaa8.md) FUN_0087aaa8

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
      "definition_site": "0087aaac",
      "incomplete_value": false,
      "site": "0087aab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aaac",
      "incomplete_value": false,
      "site": "0087aab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "0087aab0",
      "DATA",
      [
        "storage",
        "00c05948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aab0",
      "DATA",
      [
        "storage",
        "00c059f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087aaa8.md#insn-0087aaac)
- 新版 `0087aaac`（命令位置の公開資料なし）

~~~diff
- 0087aaac ["COPY", "tmp:0:8", ["const:948:8"]]
- 0087aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 0087aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087aaac bytes 08212591
+ 0087aaac bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04f51b6b5c6330445d7285db0e7cdf20"></a>

### [`0087ab04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab04.md) → [`0087ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab04.md) FUN_0087ab04

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
      "definition_site": "0087ab28",
      "incomplete_value": false,
      "site": "0087ab28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab28",
      "incomplete_value": false,
      "site": "0087ab28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c05000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0087ab28",
      "DATA",
      [
        "storage",
        "00c059d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ab28",
      "DATA",
      [
        "storage",
        "00c05a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab04.md#insn-0087ab24)
- 新版 `0087ab24`（命令位置の公開資料なし）

~~~diff
- 0087ab24 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0087ab24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 0087ab24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ab24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087ab24 bytes 08612791
+ 0087ab24 bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6d2571e36701785bdc4a0faacfe6721"></a>

### [`0087ab38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab38.md) → [`0087ab38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab38.md) FUN_0087ab38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0087ab44",
      "incomplete_value": true,
      "site": "0087ab44",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab44",
      "incomplete_value": true,
      "site": "0087ab44",
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
      "0087ab44",
      "DATA",
      [
        "storage",
        "00c059d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ab44",
      "DATA",
      [
        "storage",
        "00c05a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab38.md#insn-0087ab40)
- 新版 `0087ab40`（命令位置の公開資料なし）

~~~diff
- 0087ab40 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0087ab40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 0087ab40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ab40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087ab40 bytes 29612791
+ 0087ab40 bytes 29212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aea358ef47e52ecab6835b1765ef4e0"></a>

### [`0087ab54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab54.md) → [`0087ab54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087ab54.md) FUN_0087ab54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00708fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00708/00708fe4.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00a4ec40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4e/00a4ec40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00708fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00708/00708fe4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a4ec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a4e/00a4ec40.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0087ab8c",
      "incomplete_value": true,
      "site": "0087ab8c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab8c",
      "incomplete_value": true,
      "site": "0087ab8c",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087ab7c",
      "READ",
      [
        "storage",
        "0109e5f0",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ab8c",
      "WRITE",
      [
        "storage",
        "0109e5f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087ab7c",
      "READ",
      [
        "storage",
        "0109e6b0",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ab8c",
      "WRITE",
      [
        "storage",
        "0109e6b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ab8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab54.md#insn-0087ab8c) · [`0087ab7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087ab54.md#insn-0087ab7c)
- 新版 `0087ab8c`（命令位置の公開資料なし） · `0087ab7c`（命令位置の公開資料なし）

~~~diff
- 0087ab8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0087ab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0087ab8c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:5f0:8"]]
- 0087ab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0087ab8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0087ab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0087ab8c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:6b0:8"]]
+ 0087ab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0087ab8c bytes 1fc11739
+ 0087ab8c bytes 1fc11a39
- 0087ab7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5f0:8"]]
- 0087ab7c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0087ab7c ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0087ab7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6b0:8"]]
+ 0087ab7c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0087ab7c ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0087ab7c bytes 09c15739
+ 0087ab7c bytes 09c15a39
~~~


<a id="compare-3bc48f400cc87d1d89d7950049704d77"></a>

### [`0087acb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087acb4.md) → [`0087acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md) FUN_0087acb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00870/00870980.md) [`0087acb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087acb4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870980.md) [`0087acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087a/0087acb4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087ae10",
      "incomplete_value": false,
      "site": "0087ae18",
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
      "definition_site": "0087ae10",
      "incomplete_value": false,
      "site": "0087ae18",
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
      "definition_site": "0087af68",
      "incomplete_value": false,
      "site": "0087af70",
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
      "definition_site": "0087af68",
      "incomplete_value": false,
      "site": "0087af70",
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
      "definition_site": "0087b010",
      "incomplete_value": false,
      "site": "0087b01c",
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
      "definition_site": "0087b010",
      "incomplete_value": false,
      "site": "0087b01c",
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
      "0087ae10",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087af68",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087b010",
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
      "0087ae10",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087af68",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087b010",
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

- 旧版 [`0087ae10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087acb4.md#insn-0087ae10) · [`0087af68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087acb4.md#insn-0087af68) · [`0087b010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087a/0087acb4.md#insn-0087b010)
- 新版 `0087ae10`（命令位置の公開資料なし） · `0087af68`（命令位置の公開資料なし） · `0087b010`（命令位置の公開資料なし）

~~~diff
- 0087ae10 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087ae10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ae10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ae10 bytes 21440c91
+ 0087ae10 bytes 21280c91
- 0087af68 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087af68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087af68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087af68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087af68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087af68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087af68 bytes 21d40b91
+ 0087af68 bytes 21b80b91
- 0087b010 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087b010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b010 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087b010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b010 bytes 21681f91
+ 0087b010 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a641d82cf36849099788aa9871f72e07"></a>

### [`0087b620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md) → [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) FUN_0087b620

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) [`0087b620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md) [`0097a22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087b7a4",
      "incomplete_value": false,
      "site": "0087b7ac",
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
      "definition_site": "0087b7a4",
      "incomplete_value": false,
      "site": "0087b7ac",
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
      "definition_site": "0087bc00",
      "incomplete_value": false,
      "site": "0087bc10",
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
      "definition_site": "0087bc00",
      "incomplete_value": false,
      "site": "0087bc10",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087bcb8",
      "incomplete_value": false,
      "site": "0087bcc0",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bcb8",
      "incomplete_value": false,
      "site": "0087bcc0",
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
            "const:7d9:8"
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
      "0087b7a4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087b8fc",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087b9a4",
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
      "0087b7a4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087b8fc",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087b9a4",
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

- 旧版 [`0087b7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md#insn-0087b7a4) · [`0087b8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md#insn-0087b8fc) · [`0087b9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md#insn-0087b9a4)
- 新版 `0087b7a4`（命令位置の公開資料なし） · `0087b8fc`（命令位置の公開資料なし） · `0087b9a4`（命令位置の公開資料なし）

~~~diff
- 0087b7a4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087b7a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087b7a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b7a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b7a4 bytes 21440c91
+ 0087b7a4 bytes 21280c91
- 0087b8fc ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087b8fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087b8fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b8fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b8fc bytes 21d40b91
+ 0087b8fc bytes 21b80b91
- 0087b9a4 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087b9a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087b9a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087b9a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087b9a4 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087b9a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b9a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087b9a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087b9a4 bytes 21681f91
+ 0087b9a4 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d82529f5f653479a63f5d8b20b1dd4"></a>

### [`0087bed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md) → [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) FUN_0087bed0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087b620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087b620.md) [`0087bed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087b620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087b620.md) [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087c048",
      "incomplete_value": false,
      "site": "0087c050",
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
      "definition_site": "0087c048",
      "incomplete_value": false,
      "site": "0087c050",
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
      "definition_site": "0087c1a0",
      "incomplete_value": false,
      "site": "0087c1a8",
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
      "definition_site": "0087c1a0",
      "incomplete_value": false,
      "site": "0087c1a8",
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
      "definition_site": "0087c248",
      "incomplete_value": false,
      "site": "0087c254",
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
      "definition_site": "0087c248",
      "incomplete_value": false,
      "site": "0087c254",
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
      "0087c048",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087c1a0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087c248",
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
      "0087c048",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087c1a0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087c248",
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

- 旧版 [`0087c048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md#insn-0087c048) · [`0087c1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md#insn-0087c1a0) · [`0087c248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md#insn-0087c248)
- 新版 `0087c048`（命令位置の公開資料なし） · `0087c1a0`（命令位置の公開資料なし） · `0087c248`（命令位置の公開資料なし）

~~~diff
- 0087c048 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087c048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087c048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c048 bytes 21440c91
+ 0087c048 bytes 21280c91
- 0087c1a0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087c1a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087c1a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c1a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c1a0 bytes 21d40b91
+ 0087c1a0 bytes 21b80b91
- 0087c248 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087c248 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c248 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c248 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c248 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087c248 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c248 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c248 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c248 bytes 21681f91
+ 0087c248 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fee643303e49322b0c5596da466f350"></a>

### [`0087c758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md) → [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) FUN_0087c758

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087bed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087b/0087bed0.md) [`0087c758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087bed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087b/0087bed0.md) [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087c8cc",
      "incomplete_value": false,
      "site": "0087c8d4",
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
      "definition_site": "0087c8cc",
      "incomplete_value": false,
      "site": "0087c8d4",
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
      "definition_site": "0087ca24",
      "incomplete_value": true,
      "site": "0087ca2c",
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
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ca24",
      "incomplete_value": true,
      "site": "0087ca2c",
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
      "definition_site": "0087cacc",
      "incomplete_value": true,
      "site": "0087cad8",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087cacc",
      "incomplete_value": true,
      "site": "0087cad8",
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
      "0087c8cc",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087ca24",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087cacc",
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
      "0087c8cc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087ca24",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087cacc",
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

- 旧版 [`0087c8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md#insn-0087c8cc) · [`0087ca24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md#insn-0087ca24) · [`0087cacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md#insn-0087cacc)
- 新版 `0087c8cc`（命令位置の公開資料なし） · `0087ca24`（命令位置の公開資料なし） · `0087cacc`（命令位置の公開資料なし）

~~~diff
- 0087c8cc ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087c8cc bytes 21440c91
+ 0087c8cc bytes 21280c91
- 0087ca24 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087ca24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087ca24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087ca24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087ca24 bytes 21d40b91
+ 0087ca24 bytes 21b80b91
- 0087cacc ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087cacc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087cacc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087cacc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087cacc ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087cacc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087cacc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087cacc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087cacc bytes 21681f91
+ 0087cacc bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf3066c7a0d64ba1fabe4a0805cffd08"></a>

### [`0087cfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md) → [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) FUN_0087cfbc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0087c758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087c758.md) [`0087cfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md) [`00979584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979584.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0087c758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087c758.md) [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) [`00979584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "0087d124",
      "incomplete_value": false,
      "site": "0087d12c",
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
      "definition_site": "0087d124",
      "incomplete_value": false,
      "site": "0087d12c",
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
      "definition_site": "0087d27c",
      "incomplete_value": false,
      "site": "0087d284",
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
      "definition_site": "0087d27c",
      "incomplete_value": false,
      "site": "0087d284",
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
      "definition_site": "0087d324",
      "incomplete_value": false,
      "site": "0087d330",
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
      "definition_site": "0087d324",
      "incomplete_value": false,
      "site": "0087d330",
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
      "0087d124",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087d27c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087d324",
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
      "0087d124",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087d27c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087d324",
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

- 旧版 [`0087d124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md#insn-0087d124) · [`0087d27c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md#insn-0087d27c) · [`0087d324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md#insn-0087d324)
- 新版 `0087d124`（命令位置の公開資料なし） · `0087d27c`（命令位置の公開資料なし） · `0087d324`（命令位置の公開資料なし）

~~~diff
- 0087d124 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087d124 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d124 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d124 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087d124 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d124 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d124 bytes 21440c91
+ 0087d124 bytes 21280c91
- 0087d27c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087d27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087d27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d27c bytes 21d40b91
+ 0087d27c bytes 21b80b91
- 0087d324 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087d324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087d324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087d324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087d324 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087d324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087d324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087d324 bytes 21681f91
+ 0087d324 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0020bd755c5ee1d90139f2d99df8ddbe"></a>

### [`0087d9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md) → [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) FUN_0087d9b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00870/00870c7c.md) [`0087d9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870c7c.md) [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dc94",
      "incomplete_value": false,
      "site": "0087dc9c",
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
      "definition_site": "0087dc94",
      "incomplete_value": false,
      "site": "0087dc9c",
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
      "definition_site": "0087dd3c",
      "incomplete_value": true,
      "site": "0087dd48",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dd3c",
      "incomplete_value": true,
      "site": "0087dd48",
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
      "definition_site": "0087dfc0",
      "incomplete_value": false,
      "site": "0087dfd0",
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
      "definition_site": "0087dfc0",
      "incomplete_value": false,
      "site": "0087dfd0",
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
      "0087db3c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087dc94",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087dd3c",
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
      "0087db3c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087dc94",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087dd3c",
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

- 旧版 [`0087db3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md#insn-0087db3c) · [`0087dc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md#insn-0087dc94) · [`0087dd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md#insn-0087dd3c)
- 新版 `0087db3c`（命令位置の公開資料なし） · `0087dc94`（命令位置の公開資料なし） · `0087dd3c`（命令位置の公開資料なし）

~~~diff
- 0087db3c ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087db3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087db3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087db3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087db3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087db3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087db3c bytes 21440c91
+ 0087db3c bytes 21280c91
- 0087dc94 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087dc94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087dc94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dc94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087dc94 bytes 21d40b91
+ 0087dc94 bytes 21b80b91
- 0087dd3c ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087dd3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087dd3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087dd3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087dd3c ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087dd3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dd3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087dd3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087dd3c bytes 21681f91
+ 0087dd3c bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4d495a43de4d1bdf9ee99e45878552"></a>

### [`0087e398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md) → [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) FUN_0087e398

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087d9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087d/0087d9b4.md) [`0087e398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087d/0087d9b4.md) [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087e518",
      "incomplete_value": false,
      "site": "0087e520",
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
      "definition_site": "0087e518",
      "incomplete_value": false,
      "site": "0087e520",
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
      "definition_site": "0087e670",
      "incomplete_value": false,
      "site": "0087e678",
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
      "definition_site": "0087e670",
      "incomplete_value": false,
      "site": "0087e678",
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
      "definition_site": "0087e99c",
      "incomplete_value": false,
      "site": "0087e9ac",
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
      "definition_site": "0087e99c",
      "incomplete_value": false,
      "site": "0087e9ac",
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
      "0087e518",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087e670",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087e718",
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
      "0087e518",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087e670",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087e718",
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

- 旧版 [`0087e518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md#insn-0087e518) · [`0087e670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md#insn-0087e670) · [`0087e718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md#insn-0087e718)
- 新版 `0087e518`（命令位置の公開資料なし） · `0087e670`（命令位置の公開資料なし） · `0087e718`（命令位置の公開資料なし）

~~~diff
- 0087e518 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087e518 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e518 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e518 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087e518 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e518 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e518 bytes 21440c91
+ 0087e518 bytes 21280c91
- 0087e670 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087e670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087e670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e670 bytes 21d40b91
+ 0087e670 bytes 21b80b91
- 0087e718 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087e718 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087e718 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087e718 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087e718 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087e718 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e718 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087e718 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087e718 bytes 21681f91
+ 0087e718 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e061de438d1ca502bb3d664ca4b7934"></a>

### [`0087ed74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md) → [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) FUN_0087ed74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087e398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087e398.md) [`0087ed74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087e398.md) [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087eeec",
      "incomplete_value": false,
      "site": "0087eef4",
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
      "definition_site": "0087eeec",
      "incomplete_value": false,
      "site": "0087eef4",
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
      "definition_site": "0087f044",
      "incomplete_value": false,
      "site": "0087f04c",
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
      "definition_site": "0087f044",
      "incomplete_value": false,
      "site": "0087f04c",
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
      "definition_site": "0087f0ec",
      "incomplete_value": true,
      "site": "0087f0f8",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f0ec",
      "incomplete_value": true,
      "site": "0087f0f8",
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
      "0087eeec",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087f044",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087f0ec",
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
      "0087eeec",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087f044",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087f0ec",
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

- 旧版 [`0087eeec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md#insn-0087eeec) · [`0087f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md#insn-0087f044) · [`0087f0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md#insn-0087f0ec)
- 新版 `0087eeec`（命令位置の公開資料なし） · `0087f044`（命令位置の公開資料なし） · `0087f0ec`（命令位置の公開資料なし）

~~~diff
- 0087eeec ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087eeec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087eeec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087eeec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087eeec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087eeec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087eeec bytes 21440c91
+ 0087eeec bytes 21280c91
- 0087f044 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087f044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087f044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f044 bytes 21d40b91
+ 0087f044 bytes 21b80b91
- 0087f0ec ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0087f0ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f0ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f0ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f0ec ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0087f0ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f0ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f0ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f0ec bytes 21681f91
+ 0087f0ec bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232e6ad648c17a58814cb28d20c3145f"></a>

### [`0087f724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md) → [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) FUN_0087f724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087ed74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087e/0087ed74.md) [`0087f724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087ed74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087e/0087ed74.md) [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087f8a4",
      "incomplete_value": false,
      "site": "0087f8ac",
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
      "definition_site": "0087f8a4",
      "incomplete_value": false,
      "site": "0087f8ac",
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
      "definition_site": "0087f95c",
      "incomplete_value": false,
      "site": "0087f964",
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
      "definition_site": "0087f95c",
      "incomplete_value": false,
      "site": "0087f964",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087fc4c",
      "incomplete_value": true,
      "site": "0087fc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087fc4c",
      "incomplete_value": true,
      "site": "0087fc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087f8a4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0087f95c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0087fc4c",
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087f8a4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0087f95c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0087fc4c",
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md#insn-0087f8a4) · [`0087f95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md#insn-0087f95c) · [`0087fc4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md#insn-0087fc4c)
- 新版 `0087f8a4`（命令位置の公開資料なし） · `0087f95c`（命令位置の公開資料なし） · `0087fc4c`（命令位置の公開資料なし）

~~~diff
- 0087f8a4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0087f8a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0087f8a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f8a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f8a4 bytes 21440c91
+ 0087f8a4 bytes 21280c91
- 0087f95c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0087f95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0087f95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0087f95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0087f95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0087f95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0087f95c bytes 21d40b91
+ 0087f95c bytes 21b80b91
- 0087fc4c ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0087fc4c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0087fc4c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0087fc4c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0087fc4c ["COPY", "tmp:0:8", ["const:672:8"]]
+ 0087fc4c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0087fc4c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0087fc4c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0087fc4c bytes 63941791
+ 0087fc4c bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5fe56dfedfa85b396446da7c312d6e8"></a>

### [`0088004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md) → [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) FUN_0088004c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0087f724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087f/0087f724.md) [`0088004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0087f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087f/0087f724.md) [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008801ac",
      "incomplete_value": false,
      "site": "008801b4",
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
      "definition_site": "008801ac",
      "incomplete_value": false,
      "site": "008801b4",
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
      "definition_site": "00880304",
      "incomplete_value": false,
      "site": "0088030c",
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
      "definition_site": "00880304",
      "incomplete_value": false,
      "site": "0088030c",
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
      "definition_site": "008803ac",
      "incomplete_value": false,
      "site": "008803b8",
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
      "definition_site": "008803ac",
      "incomplete_value": false,
      "site": "008803b8",
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
      "008801ac",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00880304",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008803ac",
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
      "008801ac",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00880304",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008803ac",
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

- 旧版 [`008801ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md#insn-008801ac) · [`00880304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md#insn-00880304) · [`008803ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md#insn-008803ac)
- 新版 `008801ac`（命令位置の公開資料なし） · `00880304`（命令位置の公開資料なし） · `008803ac`（命令位置の公開資料なし）

~~~diff
- 008801ac ["COPY", "tmp:0:8", ["const:311:8"]]
- 008801ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008801ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008801ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008801ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008801ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008801ac bytes 21440c91
+ 008801ac bytes 21280c91
- 00880304 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00880304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00880304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00880304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00880304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00880304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00880304 bytes 21d40b91
+ 00880304 bytes 21b80b91
- 008803ac ["COPY", "tmp:0:8", ["const:7da:8"]]
- 008803ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008803ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008803ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008803ac ["COPY", "tmp:0:8", ["const:867:8"]]
+ 008803ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008803ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008803ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008803ac bytes 21681f91
+ 008803ac bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b128e716ccbe7b7f0ba2ffaa160f2e27"></a>

### [`00880878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md) → [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) FUN_00880878

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0088004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/0088004c.md) [`00880878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0088004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/0088004c.md) [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008809d4",
      "incomplete_value": false,
      "site": "008809dc",
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
      "definition_site": "008809d4",
      "incomplete_value": false,
      "site": "008809dc",
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
      "definition_site": "00880b2c",
      "incomplete_value": false,
      "site": "00880b34",
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
      "definition_site": "00880b2c",
      "incomplete_value": false,
      "site": "00880b34",
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
      "definition_site": "00880bd4",
      "incomplete_value": false,
      "site": "00880be0",
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
      "definition_site": "00880bd4",
      "incomplete_value": false,
      "site": "00880be0",
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
      "008809d4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00880b2c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00880bd4",
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
      "008809d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00880b2c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00880bd4",
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

- 旧版 [`008809d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md#insn-008809d4) · [`00880b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md#insn-00880b2c) · [`00880bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md#insn-00880bd4)
- 新版 `008809d4`（命令位置の公開資料なし） · `00880b2c`（命令位置の公開資料なし） · `00880bd4`（命令位置の公開資料なし）

~~~diff
- 008809d4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 008809d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008809d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008809d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008809d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008809d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008809d4 bytes 21440c91
+ 008809d4 bytes 21280c91
- 00880b2c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00880b2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00880b2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00880b2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00880b2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00880b2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00880b2c bytes 21d40b91
+ 00880b2c bytes 21b80b91
- 00880bd4 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00880bd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00880bd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00880bd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00880bd4 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00880bd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00880bd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00880bd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00880bd4 bytes 21681f91
+ 00880bd4 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ae21d2bcf66a76764da9977da7ecead"></a>

### [`00881090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md) → [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) FUN_00881090

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00880878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00880/00880878.md) [`00881090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00880878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00880/00880878.md) [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008811ec",
      "incomplete_value": false,
      "site": "008811f4",
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
      "definition_site": "008811ec",
      "incomplete_value": false,
      "site": "008811f4",
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
      "definition_site": "00881344",
      "incomplete_value": false,
      "site": "0088134c",
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
      "definition_site": "00881344",
      "incomplete_value": false,
      "site": "0088134c",
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
      "definition_site": "008813ec",
      "incomplete_value": false,
      "site": "008813f8",
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
      "definition_site": "008813ec",
      "incomplete_value": false,
      "site": "008813f8",
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
      "008811ec",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00881344",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "008813ec",
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
      "008811ec",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00881344",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008813ec",
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

- 旧版 [`008811ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md#insn-008811ec) · [`00881344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md#insn-00881344) · [`008813ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md#insn-008813ec)
- 新版 `008811ec`（命令位置の公開資料なし） · `00881344`（命令位置の公開資料なし） · `008813ec`（命令位置の公開資料なし）

~~~diff
- 008811ec ["COPY", "tmp:0:8", ["const:311:8"]]
- 008811ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008811ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008811ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 008811ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008811ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008811ec bytes 21440c91
+ 008811ec bytes 21280c91
- 00881344 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00881344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00881344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881344 bytes 21d40b91
+ 00881344 bytes 21b80b91
- 008813ec ["COPY", "tmp:0:8", ["const:7da:8"]]
- 008813ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008813ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008813ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008813ec ["COPY", "tmp:0:8", ["const:867:8"]]
+ 008813ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008813ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008813ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008813ec bytes 21681f91
+ 008813ec bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02883f0143197baab7898a8da7e076af"></a>

### [`008818a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md) → [`008818a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md) FUN_008818a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00881090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/00881090.md) [`008818a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md) [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`00881090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/00881090.md) [`008818a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md) [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00881a00",
      "incomplete_value": false,
      "site": "00881a08",
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
      "definition_site": "00881a00",
      "incomplete_value": false,
      "site": "00881a08",
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
      "definition_site": "00881c00",
      "incomplete_value": false,
      "site": "00881c0c",
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
      "definition_site": "00881c00",
      "incomplete_value": false,
      "site": "00881c0c",
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
      "definition_site": "00881e1c",
      "incomplete_value": false,
      "site": "00881e2c",
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
      "definition_site": "00881e1c",
      "incomplete_value": false,
      "site": "00881e2c",
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
      "00881a00",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00881b58",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00881c00",
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
      "00881a00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00881b58",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00881c00",
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

- 旧版 [`00881a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md#insn-00881a00) · [`00881b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md#insn-00881b58) · [`00881c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md#insn-00881c00)
- 新版 `00881a00`（命令位置の公開資料なし） · `00881b58`（命令位置の公開資料なし） · `00881c00`（命令位置の公開資料なし）

~~~diff
- 00881a00 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00881a00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881a00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881a00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00881a00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881a00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881a00 bytes 21440c91
+ 00881a00 bytes 21280c91
- 00881b58 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00881b58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881b58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881b58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00881b58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881b58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881b58 bytes 21d40b91
+ 00881b58 bytes 21b80b91
- 00881c00 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00881c00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00881c00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00881c00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00881c00 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00881c00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00881c00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00881c00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00881c00 bytes 21681f91
+ 00881c00 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baba95ade545b9bfb09b69ba406fd763"></a>

### [`008820ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md) → [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) FUN_008820ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00870df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00870/00870df0.md) [`008820ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00870df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00870/00870df0.md) [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882208",
      "incomplete_value": false,
      "site": "00882210",
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
      "definition_site": "00882208",
      "incomplete_value": false,
      "site": "00882210",
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
      "definition_site": "0088267c",
      "incomplete_value": false,
      "site": "0088268c",
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
      "definition_site": "0088267c",
      "incomplete_value": false,
      "site": "0088268c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882758",
      "incomplete_value": false,
      "site": "00882760",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00882758",
      "incomplete_value": false,
      "site": "00882760",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882208",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00882360",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00882408",
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
      "00882208",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00882360",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00882408",
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

- 旧版 [`00882208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md#insn-00882208) · [`00882360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md#insn-00882360) · [`00882408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md#insn-00882408)
- 新版 `00882208`（命令位置の公開資料なし） · `00882360`（命令位置の公開資料なし） · `00882408`（命令位置の公開資料なし）

~~~diff
- 00882208 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00882208 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882208 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882208 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00882208 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882208 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882208 bytes 21440c91
+ 00882208 bytes 21280c91
- 00882360 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00882360 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882360 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882360 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00882360 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882360 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882360 bytes 21d40b91
+ 00882360 bytes 21b80b91
- 00882408 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00882408 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882408 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882408 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882408 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00882408 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882408 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882408 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882408 bytes 21681f91
+ 00882408 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c23afbf71653cbf0b87d6a08c6530c1"></a>

### [`00882a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/00882a18.md) → [`00882a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md) FUN_00882a18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008820ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/008820ac.md) [`00882a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/00882a18.md) [`00a39ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a39/00a39ff4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`008820ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/008820ac.md) [`00882a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00882/00882a18.md) [`00a39ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a39/00a39ff4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882b84",
      "incomplete_value": false,
      "site": "00882b8c",
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
      "definition_site": "00882b84",
      "incomplete_value": false,
      "site": "00882b8c",
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
      "definition_site": "00882c3c",
      "incomplete_value": false,
      "site": "00882c44",
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
      "definition_site": "00882c3c",
      "incomplete_value": false,
      "site": "00882c44",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882f1c",
      "incomplete_value": false,
      "site": "00882f2c",
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
      "definition_site": "00882f1c",
      "incomplete_value": false,
      "site": "00882f2c",
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
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882b84",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00882c3c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00882f1c",
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00882b84",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00882c3c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00882f1c",
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/00882a18.md#insn-00882b84) · [`00882c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/00882a18.md#insn-00882c3c) · [`00882f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00882/00882a18.md#insn-00882f1c)
- 新版 `00882b84`（命令位置の公開資料なし） · `00882c3c`（命令位置の公開資料なし） · `00882f1c`（命令位置の公開資料なし）

~~~diff
- 00882b84 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00882b84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882b84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882b84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00882b84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882b84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882b84 bytes 21440c91
+ 00882b84 bytes 21280c91
- 00882c3c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00882c3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00882c3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00882c3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00882c3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00882c3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00882c3c bytes 21d40b91
+ 00882c3c bytes 21b80b91
- 00882f1c ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00882f1c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00882f1c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00882f1c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00882f1c ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00882f1c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00882f1c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00882f1c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00882f1c bytes 63941791
+ 00882f1c bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c5683a724e3329025270079601dbf6b"></a>

### [`008832e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008832e8.md) → [`008832e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008832e8.md) _INIT_163

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 79.33% / 新版 79.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 7件, `store_value` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883324",
      "incomplete_value": true,
      "site": "00883340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883324",
      "incomplete_value": true,
      "site": "00883340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883348",
      "incomplete_value": true,
      "site": "00883364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883348",
      "incomplete_value": true,
      "site": "00883364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883368",
      "incomplete_value": true,
      "site": "00883384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00883368",
      "incomplete_value": true,
      "site": "00883384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00883324",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00883348",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00883368",
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
      "00883324",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00883348",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00883368",
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

- 旧版 [`00883520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008832e8.md#insn-00883520) · [`00883560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008832e8.md#insn-00883560)
- 新版 `00883520`（命令位置の公開資料なし）

~~~diff
- 00883520 ["INT_ADD", "register:40f0:8", ["const:883520:8", "const:4:8"]]
- 00883520 ["CALL", null, ["callee:00bdaf90:8"]]
- 00883520 bytes 705e0d94
+ 00883520 ["INT_ADD", "register:40f0:8", ["const:883520:8", "const:4:8"]]
+ 00883520 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00883520 bytes 9c5e0d94
- 00883560 ["INT_ADD", "register:40f0:8", ["const:883560:8", "const:4:8"]]
- 00883560 ["CALL", null, ["callee:00bdaf90:8"]]
- 00883560 bytes 605e0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d10393f4faa26e44e94ea554bdb94dd2"></a>

### [`008836f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008836f4.md) → [`008836f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md) FUN_008836f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md) · 呼出先 5件 [`00884834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/00884834.md) [`00884900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/00884900.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) · 呼出先 5件 [`00884834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884834.md) [`00884900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884900.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883758",
      "incomplete_value": true,
      "site": "00883758",
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
      "definition_site": "00883758",
      "incomplete_value": true,
      "site": "00883758",
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
      "00883750",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "00883758",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "00883820",
      "READ",
      [
        "storage",
        "00c24608",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00883750",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00883758",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00883820",
      "READ",
      [
        "storage",
        "00c246b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008836f4.md#insn-00883750) · [`00883818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008836f4.md#insn-00883818)
- 新版 `00883750`（命令位置の公開資料なし） · `00883818`（命令位置の公開資料なし）

~~~diff
- 00883750 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00883750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883750 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 00883750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00883750 bytes 083942f9
+ 00883750 bytes 089142f9
- 00883818 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00883818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00883818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00883818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00883818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00883818 bytes 08211891
+ 00883818 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628e032edb8c201cd3b2a4e26f7092f1"></a>

### [`00883bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md) → [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) FUN_00883bb8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 56件 [`005a33f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md) [`005e97d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e9/005e97d8.md) [`005ecde0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ec/005ecde0.md) [`005ee758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ee/005ee758.md) [`005efbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ef/005efbac.md) · 呼出先 3件 [`009e9760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9760.md) [`009e9afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9afc.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 56件 [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) [`005e97d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e9/005e97d8.md) [`005ecde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ec/005ecde0.md) [`005ee758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ee/005ee758.md) [`005efbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ef/005efbac.md) · 呼出先 3件 [`009e9760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9760.md) [`009e9afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9afc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00883bfc",
      "incomplete_value": true,
      "site": "00883c00",
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00883bfc",
      "incomplete_value": true,
      "site": "00883c00",
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:678:8"
              ]
            ]
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
      "00883bf8",
      "READ",
      [
        "storage",
        "00c1b670",
        null,
        "pointer"
      ]
    ],
    [
      "00883bf8",
      "PARAM",
      [
        "storage",
        "00c0bc58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00883bfc",
      "READ",
      [
        "storage",
        "00c1b678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00883bf8",
      "READ",
      [
        "storage",
        "00c1b720",
        null,
        "pointer"
      ]
    ],
    [
      "00883bf8",
      "PARAM",
      [
        "storage",
        "00c0bd08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00883bfc",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md#insn-00883bf8) · [`00883bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md#insn-00883bfc)
- 新版 `00883bf8`（命令位置の公開資料なし） · `00883bfc`（命令位置の公開資料なし）

~~~diff
- 00883bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:670:8"]]
- 00883bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883bf8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:720:8"]]
+ 00883bf8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00883bf8 bytes 213843f9
+ 00883bf8 bytes 219043f9
- 00883bfc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:678:8"]]
- 00883bfc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883bfc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:728:8"]]
+ 00883bfc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00883bfc bytes 423c43f9
+ 00883bfc bytes 429443f9
~~~


<a id="compare-a5af0a7ad8102f17c416246c5d160ebb"></a>

### [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md) → [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) FUN_00883e08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 70件 [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005eb/005eb040.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`008836f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/008836f4.md) [`00884834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/00884834.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 70件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`008836f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/008836f4.md) [`00884834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/00884834.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883f7c",
      "incomplete_value": true,
      "site": "00883f7c",
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
      "definition_site": "00883f7c",
      "incomplete_value": true,
      "site": "00883f7c",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00883f74",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "00883f7c",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883f74",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "00883f7c",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md#insn-00883f74)
- 新版 `00883f74`（命令位置の公開資料なし）

~~~diff
- 00883f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00883f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00883f74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 00883f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00883f74 bytes 083942f9
+ 00883f74 bytes 089142f9
~~~


