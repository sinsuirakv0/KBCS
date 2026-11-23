# v16.0.0 → v16.0.1 · 最優先の変更候補 (27)

[一覧の目次](README.md)

<a id="compare-449c55e2b6bb550a30ccd3e962c6c1e3"></a>

### [`006256d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md) → [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) FUN_00625718

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00624c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md) [`006256d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00625878",
      "incomplete_value": false,
      "site": "00625880",
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
      "definition_site": "00625838",
      "incomplete_value": false,
      "site": "00625840",
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
      "definition_site": "00625934",
      "incomplete_value": false,
      "site": "0062593c",
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
      "definition_site": "006258f4",
      "incomplete_value": false,
      "site": "006258fc",
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
      "definition_site": "0062594c",
      "incomplete_value": false,
      "site": "00625958",
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
      "definition_site": "0062590c",
      "incomplete_value": false,
      "site": "00625918",
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
      "00625878",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00625934",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0062594c",
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
      "00625878",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00625934",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0062594c",
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

- 旧版 [`00625840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md#insn-00625840) · [`006258fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md#insn-006258fc) · [`00625918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md#insn-00625918)
- 新版 `00625880`（命令位置の公開資料なし） · `0062593c`（命令位置の公開資料なし） · `00625958`（命令位置の公開資料なし）

~~~diff
- 00625840 ["INT_ADD", "register:40f0:8", ["const:625840:8", "const:4:8"]]
- 00625840 ["CALL", null, ["callee:00441e94:8"]]
+ 00625880 ["INT_ADD", "register:40f0:8", ["const:625880:8", "const:4:8"]]
+ 00625880 ["CALL", null, ["callee:00441e94:8"]]
- 00625840 bytes 8571f897
+ 00625880 bytes 8571f897
- 006258fc ["INT_ADD", "register:40f0:8", ["const:6258fc:8", "const:4:8"]]
- 006258fc ["CALL", null, ["callee:00441e94:8"]]
+ 0062593c ["INT_ADD", "register:40f0:8", ["const:62593c:8", "const:4:8"]]
+ 0062593c ["CALL", null, ["callee:00441e94:8"]]
- 006258fc bytes 5671f897
+ 0062593c bytes 5671f897
- 00625918 ["INT_ADD", "register:40f0:8", ["const:625918:8", "const:4:8"]]
- 00625918 ["CALL", null, ["callee:004427f4:8"]]
+ 00625958 ["INT_ADD", "register:40f0:8", ["const:625958:8", "const:4:8"]]
+ 00625958 ["CALL", null, ["callee:004427f4:8"]]
- 00625918 bytes a773f897
+ 00625958 bytes a773f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-004a0e842a25dc00c821aafb51146d07"></a>

### [`006261dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006261dc.md) → [`0062621c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062621c.md) FUN_0062621c

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
      "definition_site": "00626240",
      "incomplete_value": false,
      "site": "00626240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626200",
      "incomplete_value": false,
      "site": "00626200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "00626240",
      "DATA",
      [
        "storage",
        "00c72658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626240",
      "DATA",
      [
        "storage",
        "00c72a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006261f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006261dc.md#insn-006261f0) · [`006261fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006261dc.md#insn-006261fc)
- 新版 `00626230`（命令位置の公開資料なし） · `0062623c`（命令位置の公開資料なし）

~~~diff
- 006261f0 ["INT_ADD", "register:40f0:8", ["const:6261f0:8", "const:4:8"]]
- 006261f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626230 ["INT_ADD", "register:40f0:8", ["const:626230:8", "const:4:8"]]
+ 00626230 ["CALL", null, ["callee:00c57e90:8"]]
- 006261f0 bytes 28c61894
+ 00626230 bytes 18c71894
- 006261fc ["COPY", "tmp:0:8", ["const:658:8"]]
- 006261fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006261fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006261fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0062623c ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0062623c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0062623c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0062623c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006261fc bytes 08611991
+ 0062623c bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aff1d8affd91389ed6566da70339060"></a>

### [`00626210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626210.md) → [`00626250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626250.md) FUN_00626250

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
      "definition_site": "0062625c",
      "incomplete_value": false,
      "site": "0062625c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062621c",
      "incomplete_value": false,
      "site": "0062621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "0062625c",
      "DATA",
      [
        "storage",
        "00c72658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0062625c",
      "DATA",
      [
        "storage",
        "00c72a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626210.md#insn-00626218)
- 新版 `00626258`（命令位置の公開資料なし）

~~~diff
- 00626218 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00626218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00626218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00626218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00626258 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00626258 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00626258 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00626258 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00626218 bytes 29611991
+ 00626258 bytes 29612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480d46b3a4b842ef0c34e46297fc8085"></a>

### [`0062622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062622c.md) → [`0062626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062626c.md) FUN_0062626c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0062647c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062647c.md) [`00626480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626480.md) [`008883e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/008883e8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006264bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264bc.md) [`006264c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264c0.md) [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00626320",
      "incomplete_value": true,
      "site": "00626320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006262e0",
      "incomplete_value": true,
      "site": "006262e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:398:8"
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
      "definition_site": "00626324",
      "incomplete_value": true,
      "site": "00626324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006262e4",
      "incomplete_value": true,
      "site": "006262e4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062636c",
      "incomplete_value": false,
      "site": "0062636c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062632c",
      "incomplete_value": false,
      "site": "0062632c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "006262a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006262bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00626310",
      "READ",
      [
        "storage",
        "002b8398",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006262a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006262bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00626310",
      "READ",
      [
        "storage",
        "002b83d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062622c.md#insn-00626260) · [`0062627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062622c.md#insn-0062627c) · [`00626324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062622c.md#insn-00626324)
- 新版 `006262a0`（命令位置の公開資料なし） · `006262bc`（命令位置の公開資料なし） · `00626364`（命令位置の公開資料なし）

~~~diff
- 00626260 ["INT_ADD", "register:40f0:8", ["const:626260:8", "const:4:8"]]
- 00626260 ["CALL", null, ["ram:47acb4:8"]]
+ 006262a0 ["INT_ADD", "register:40f0:8", ["const:6262a0:8", "const:4:8"]]
+ 006262a0 ["CALL", null, ["ram:47acf4:8"]]
- 00626260 bytes 9552f997
+ 006262a0 bytes 9552f997
- 0062627c ["INT_ADD", "register:40f0:8", ["const:62627c:8", "const:4:8"]]
- 0062627c ["CALL", null, ["ram:47acb4:8"]]
+ 006262bc ["INT_ADD", "register:40f0:8", ["const:6262bc:8", "const:4:8"]]
+ 006262bc ["CALL", null, ["ram:47acf4:8"]]
- 0062627c bytes 8e52f997
+ 006262bc bytes 8e52f997
- 00626324 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00626324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626364 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00626364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626324 bytes 08211b91
+ 00626364 bytes 08212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c58f7015b27c0d243a942c5b55b5d799"></a>

### [`00626434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626434.md) → [`00626474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626474.md) FUN_00626474

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
      "definition_site": "00626498",
      "incomplete_value": false,
      "site": "00626498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626458",
      "incomplete_value": false,
      "site": "00626458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00626498",
      "DATA",
      [
        "storage",
        "00c726c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626498",
      "DATA",
      [
        "storage",
        "00c72ac8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626434.md#insn-00626448) · [`00626454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626434.md#insn-00626454)
- 新版 `00626488`（命令位置の公開資料なし） · `00626494`（命令位置の公開資料なし）

~~~diff
- 00626448 ["INT_ADD", "register:40f0:8", ["const:626448:8", "const:4:8"]]
- 00626448 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626488 ["INT_ADD", "register:40f0:8", ["const:626488:8", "const:4:8"]]
+ 00626488 ["CALL", null, ["callee:00c57e90:8"]]
- 00626448 bytes 92c51894
+ 00626488 bytes 82c61894
- 00626454 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00626454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626494 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00626494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626454 bytes 08211b91
+ 00626494 bytes 08212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c420e9088a82c59d3667641654586a1"></a>

### [`00626468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626468.md) → [`006264a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264a8.md) FUN_006264a8

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
      "definition_site": "006264b4",
      "incomplete_value": false,
      "site": "006264b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626474",
      "incomplete_value": false,
      "site": "00626474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "006264b4",
      "DATA",
      [
        "storage",
        "00c726c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006264b4",
      "DATA",
      [
        "storage",
        "00c72ac8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626468.md#insn-00626470)
- 新版 `006264b0`（命令位置の公開資料なし）

~~~diff
- 00626470 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00626470 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00626470 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00626470 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006264b0 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 006264b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006264b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006264b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00626470 bytes 29211b91
+ 006264b0 bytes 29212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01510226a9cc0ae2d494d9c6c61c8096"></a>

### [`00626484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md) → [`006264c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264c4.md) FUN_006264c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 15件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`00626774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626774.md) [`00626778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626778.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) [`006267b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006267b4.md) [`006267b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006267b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.34% / 新版 91.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062652c",
      "incomplete_value": true,
      "site": "0062652c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006264ec",
      "incomplete_value": true,
      "site": "006264ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e41:8"
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
      "definition_site": "00626530",
      "incomplete_value": true,
      "site": "00626530",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006264f0",
      "incomplete_value": true,
      "site": "006264f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062654c",
      "incomplete_value": false,
      "site": "0062654c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062650c",
      "incomplete_value": false,
      "site": "0062650c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "0062651c",
      "READ",
      [
        "storage",
        "002b1e41",
        null,
        "string"
      ]
    ],
    [
      "00626520",
      "READ",
      [
        "storage",
        "002b1e46",
        null,
        "string"
      ]
    ],
    [
      "0062654c",
      "DATA",
      [
        "storage",
        "00c72738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0062651c",
      "READ",
      [
        "storage",
        "002b1e81",
        null,
        "string"
      ]
    ],
    [
      "00626520",
      "READ",
      [
        "storage",
        "002b1e86",
        null,
        "string"
      ]
    ],
    [
      "0062654c",
      "DATA",
      [
        "storage",
        "00c72b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006264cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md#insn-006264cc) · [`00626530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md#insn-00626530) · [`006264b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md#insn-006264b8)
- 新版 `0062650c`（命令位置の公開資料なし） · `00626570`（命令位置の公開資料なし） · `006264f8`（命令位置の公開資料なし）

~~~diff
- 006264cc ["INT_ADD", "register:40f0:8", ["const:6264cc:8", "const:4:8"]]
- 006264cc ["CALL", null, ["callee:00611e60:8"]]
+ 0062650c ["INT_ADD", "register:40f0:8", ["const:62650c:8", "const:4:8"]]
+ 0062650c ["CALL", null, ["callee:00611e60:8"]]
- 006264cc bytes 55aeff97
+ 0062650c bytes 55aeff97
- 00626530 ["INT_ADD", "register:40f0:8", ["const:626530:8", "const:4:8"]]
- 00626530 ["CALL", null, ["callee:008bacc8:8"]]
+ 00626570 ["INT_ADD", "register:40f0:8", ["const:626570:8", "const:4:8"]]
+ 00626570 ["CALL", null, ["callee:008bacc8:8"]]
- 00626530 bytes d5510a94
+ 00626570 bytes d6510a94
- 006264b8 ["INT_ADD", "register:40f0:8", ["const:6264b8:8", "const:4:8"]]
- 006264b8 ["CALL", null, ["callee:0048ce84:8"]]
+ 006264f8 ["INT_ADD", "register:40f0:8", ["const:6264f8:8", "const:4:8"]]
+ 006264f8 ["CALL", null, ["callee:0048ce84:8"]]
- 006264b8 bytes 639af997
+ 006264f8 bytes 639af997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fc7846b8f453b2853f0b9adaeda632"></a>

### [`00626760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626760.md) → [`006267a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006267a0.md) FUN_006267a0

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
      "definition_site": "006267ac",
      "incomplete_value": false,
      "site": "006267ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062676c",
      "incomplete_value": false,
      "site": "0062676c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "006267ac",
      "DATA",
      [
        "storage",
        "00c72738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006267ac",
      "DATA",
      [
        "storage",
        "00c72b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626760.md#insn-00626768)
- 新版 `006267a8`（命令位置の公開資料なし）

~~~diff
- 00626768 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00626768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00626768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00626768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006267a8 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 006267a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006267a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006267a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00626768 bytes 29e11c91
+ 006267a8 bytes 29e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1705f6321fc9d7258a716666105d483"></a>

### [`0062677c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md) → [`006267bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006267bc.md) FUN_006267bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "00626810",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006267d0",
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
      "00626810",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00626810",
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

- 旧版 [`006267d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md#insn-006267d0) · [`006267dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062677c.md#insn-006267dc)
- 新版 `00626810`（命令位置の公開資料なし） · `0062681c`（命令位置の公開資料なし）

~~~diff
- 006267d0 ["INT_ADD", "register:40f0:8", ["const:6267d0:8", "const:4:8"]]
- 006267d0 ["CALL", null, ["ram:47acb4:8"]]
+ 00626810 ["INT_ADD", "register:40f0:8", ["const:626810:8", "const:4:8"]]
+ 00626810 ["CALL", null, ["ram:47acf4:8"]]
- 006267d0 bytes 3951f997
+ 00626810 bytes 3951f997
- 006267dc ["INT_ADD", "register:40f0:8", ["const:6267dc:8", "const:4:8"]]
- 006267dc ["CALL", null, ["callee:0047cdd4:8"]]
+ 0062681c ["INT_ADD", "register:40f0:8", ["const:62681c:8", "const:4:8"]]
+ 0062681c ["CALL", null, ["callee:0047cdd4:8"]]
- 006267dc bytes 6e59f997
+ 0062681c bytes 6e59f997
~~~


<a id="compare-40b825f4b27046b33f384ca1df9ab05d"></a>

### [`0062681c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062681c.md) → [`0062685c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062685c.md) FUN_0062685c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626870",
      "incomplete_value": false,
      "site": "00626874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626830",
      "incomplete_value": false,
      "site": "00626834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "00626874",
      "DATA",
      [
        "storage",
        "00c727b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626874",
      "DATA",
      [
        "storage",
        "00c72bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062681c.md#insn-00626828) · [`00626830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062681c.md#insn-00626830)
- 新版 `00626868`（命令位置の公開資料なし） · `00626870`（命令位置の公開資料なし）

~~~diff
- 00626828 ["INT_ADD", "register:40f0:8", ["const:626828:8", "const:4:8"]]
- 00626828 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626868 ["INT_ADD", "register:40f0:8", ["const:626868:8", "const:4:8"]]
+ 00626868 ["CALL", null, ["callee:00c57e90:8"]]
- 00626828 bytes 9ac41894
+ 00626868 bytes 8ac51894
- 00626830 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00626830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626870 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00626870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626830 bytes 08e11e91
+ 00626870 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3106bfb9677e8b02f17822241099c2f"></a>

### [`00626840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626840.md) → [`00626880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626880.md) FUN_00626880

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626884",
      "incomplete_value": false,
      "site": "00626888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626844",
      "incomplete_value": false,
      "site": "00626848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "00626888",
      "DATA",
      [
        "storage",
        "00c727b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626888",
      "DATA",
      [
        "storage",
        "00c72bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626840.md#insn-00626844)
- 新版 `00626884`（命令位置の公開資料なし）

~~~diff
- 00626844 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00626844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626884 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00626884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626844 bytes 08e11e91
+ 00626884 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40597f8299bc45f34ccd2a1bbd97f06c"></a>

### [`00626858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md) → [`00626898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626898.md) FUN_00626898

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
      "site": "006268bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062687c",
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
      "006268bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006268bc",
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

- 旧版 [`0062687c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md#insn-0062687c) · [`00626888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626858.md#insn-00626888)
- 新版 `006268bc`（命令位置の公開資料なし） · `006268c8`（命令位置の公開資料なし）

~~~diff
- 0062687c ["INT_ADD", "register:40f0:8", ["const:62687c:8", "const:4:8"]]
- 0062687c ["CALL", null, ["ram:47acb4:8"]]
+ 006268bc ["INT_ADD", "register:40f0:8", ["const:6268bc:8", "const:4:8"]]
+ 006268bc ["CALL", null, ["ram:47acf4:8"]]
- 0062687c bytes 0e51f997
+ 006268bc bytes 0e51f997
- 00626888 ["INT_ADD", "register:40f0:8", ["const:626888:8", "const:4:8"]]
- 00626888 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006268c8 ["INT_ADD", "register:40f0:8", ["const:6268c8:8", "const:4:8"]]
+ 006268c8 ["CALL", null, ["callee:0047cdd4:8"]]
- 00626888 bytes 4359f997
+ 006268c8 bytes 4359f997
~~~


<a id="compare-d963880a6796975ca10e14c2ae0527c2"></a>

### [`006268cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006268cc.md) → [`0062690c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062690c.md) FUN_0062690c

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
      "definition_site": "00626930",
      "incomplete_value": false,
      "site": "00626930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006268f0",
      "incomplete_value": false,
      "site": "006268f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "00626930",
      "DATA",
      [
        "storage",
        "00c72858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626930",
      "DATA",
      [
        "storage",
        "00c72c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006268e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006268cc.md#insn-006268e0) · [`006268ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006268cc.md#insn-006268ec)
- 新版 `00626920`（命令位置の公開資料なし） · `0062692c`（命令位置の公開資料なし）

~~~diff
- 006268e0 ["INT_ADD", "register:40f0:8", ["const:6268e0:8", "const:4:8"]]
- 006268e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626920 ["INT_ADD", "register:40f0:8", ["const:626920:8", "const:4:8"]]
+ 00626920 ["CALL", null, ["callee:00c57e90:8"]]
- 006268e0 bytes 6cc41894
+ 00626920 bytes 5cc51894
- 006268ec ["COPY", "tmp:0:8", ["const:858:8"]]
- 006268ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006268ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006268ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0062692c ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 0062692c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0062692c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0062692c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006268ec bytes 08612191
+ 0062692c bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7f359492a132d1daa6904571102b22"></a>

### [`00626900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626900.md) → [`00626940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626940.md) FUN_00626940

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
      "definition_site": "0062694c",
      "incomplete_value": false,
      "site": "0062694c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062690c",
      "incomplete_value": false,
      "site": "0062690c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0062694c",
      "DATA",
      [
        "storage",
        "00c72858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0062694c",
      "DATA",
      [
        "storage",
        "00c72c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626900.md#insn-00626908)
- 新版 `00626948`（命令位置の公開資料なし）

~~~diff
- 00626908 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00626908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00626908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00626908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00626948 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 00626948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00626948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00626948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00626908 bytes 29612191
+ 00626948 bytes 29613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a40f4eebea0f1cd8f0afb100ecf98b3"></a>

### [`0062691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062691c.md) → [`0062695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062695c.md) FUN_0062695c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "site": "00626984",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626944",
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
      "00626984",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00626984",
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

- 旧版 [`00626944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062691c.md#insn-00626944) · [`00626950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/0062691c.md#insn-00626950)
- 新版 `00626984`（命令位置の公開資料なし） · `00626990`（命令位置の公開資料なし）

~~~diff
- 00626944 ["INT_ADD", "register:40f0:8", ["const:626944:8", "const:4:8"]]
- 00626944 ["CALL", null, ["ram:47acb4:8"]]
+ 00626984 ["INT_ADD", "register:40f0:8", ["const:626984:8", "const:4:8"]]
+ 00626984 ["CALL", null, ["ram:47acf4:8"]]
- 00626944 bytes dc50f997
+ 00626984 bytes dc50f997
- 00626950 ["INT_ADD", "register:40f0:8", ["const:626950:8", "const:4:8"]]
- 00626950 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00626990 ["INT_ADD", "register:40f0:8", ["const:626990:8", "const:4:8"]]
+ 00626990 ["CALL", null, ["callee:0047cdd4:8"]]
- 00626950 bytes 1159f997
+ 00626990 bytes 1159f997
~~~


<a id="compare-8bc6f209a1f46370e82a5c64cabcf0b9"></a>

### [`006269b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269b8.md) → [`006269f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006269f8.md) FUN_006269f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626a0c",
      "incomplete_value": false,
      "site": "00626a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006269cc",
      "incomplete_value": false,
      "site": "006269d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00626a10",
      "DATA",
      [
        "storage",
        "00c728d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626a10",
      "DATA",
      [
        "storage",
        "00c72cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006269c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269b8.md#insn-006269c4) · [`006269cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269b8.md#insn-006269cc)
- 新版 `00626a04`（命令位置の公開資料なし） · `00626a0c`（命令位置の公開資料なし）

~~~diff
- 006269c4 ["INT_ADD", "register:40f0:8", ["const:6269c4:8", "const:4:8"]]
- 006269c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626a04 ["INT_ADD", "register:40f0:8", ["const:626a04:8", "const:4:8"]]
+ 00626a04 ["CALL", null, ["callee:00c57e90:8"]]
- 006269c4 bytes 33c41894
+ 00626a04 bytes 23c51894
- 006269cc ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 006269cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006269cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006269cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626a0c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00626a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006269cc bytes 08612391
+ 00626a0c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad2cd6e04629026b20394878c621a292"></a>

### [`006269dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269dc.md) → [`00626a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a1c.md) FUN_00626a1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626a20",
      "incomplete_value": false,
      "site": "00626a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006269e0",
      "incomplete_value": false,
      "site": "006269e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00626a24",
      "DATA",
      [
        "storage",
        "00c728d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626a24",
      "DATA",
      [
        "storage",
        "00c72cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006269e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269dc.md#insn-006269e0)
- 新版 `00626a20`（命令位置の公開資料なし）

~~~diff
- 006269e0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 006269e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006269e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006269e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626a20 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00626a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006269e0 bytes 08612391
+ 00626a20 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-079f39defeb0efc75421ff49450335fa"></a>

### [`006269f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md) → [`00626a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a34.md) FUN_00626a34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00626af8",
      "incomplete_value": true,
      "site": "00626af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:363:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626ab8",
      "incomplete_value": true,
      "site": "00626ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:323:8"
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
      "definition_site": "00626aec",
      "incomplete_value": true,
      "site": "00626afc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00626aac",
      "incomplete_value": true,
      "site": "00626abc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626a5c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626a1c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00626a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00626a80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00626ae4",
      "READ",
      [
        "storage",
        "002c1323",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00626a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00626a80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00626ae4",
      "READ",
      [
        "storage",
        "002c1363",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md#insn-00626a1c) · [`00626a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md#insn-00626a40) · [`00626a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md#insn-00626a78)
- 新版 `00626a5c`（命令位置の公開資料なし） · `00626a80`（命令位置の公開資料なし） · `00626ab8`（命令位置の公開資料なし）

~~~diff
- 00626a1c ["INT_ADD", "register:40f0:8", ["const:626a1c:8", "const:4:8"]]
- 00626a1c ["CALL", null, ["ram:48ccb8:8"]]
+ 00626a5c ["INT_ADD", "register:40f0:8", ["const:626a5c:8", "const:4:8"]]
+ 00626a5c ["CALL", null, ["ram:48ccf8:8"]]
- 00626a1c bytes a798f997
+ 00626a5c bytes a798f997
- 00626a40 ["INT_ADD", "register:40f0:8", ["const:626a40:8", "const:4:8"]]
- 00626a40 ["CALL", null, ["ram:47acb4:8"]]
+ 00626a80 ["INT_ADD", "register:40f0:8", ["const:626a80:8", "const:4:8"]]
+ 00626a80 ["CALL", null, ["ram:47acf4:8"]]
- 00626a40 bytes 9d50f997
+ 00626a80 bytes 9d50f997
- 00626a78 ["INT_ADD", "register:40f0:8", ["const:626a78:8", "const:4:8"]]
- 00626a78 ["CALL", null, ["callee:008514f8:8"]]
+ 00626ab8 ["INT_ADD", "register:40f0:8", ["const:626ab8:8", "const:4:8"]]
+ 00626ab8 ["CALL", null, ["callee:008514f8:8"]]
- 00626a78 bytes 90aa0894
+ 00626ab8 bytes 90aa0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f85328362fa64d1e9b48f95cc82f43"></a>

### [`00626c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c30.md) → [`00626c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626c70.md) FUN_00626c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626c84",
      "incomplete_value": false,
      "site": "00626c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626c44",
      "incomplete_value": false,
      "site": "00626c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00626c88",
      "DATA",
      [
        "storage",
        "00c72958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626c88",
      "DATA",
      [
        "storage",
        "00c72d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c30.md#insn-00626c3c) · [`00626c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c30.md#insn-00626c44)
- 新版 `00626c7c`（命令位置の公開資料なし） · `00626c84`（命令位置の公開資料なし）

~~~diff
- 00626c3c ["INT_ADD", "register:40f0:8", ["const:626c3c:8", "const:4:8"]]
- 00626c3c ["CALL", null, ["callee:00c57e90:8"]]
+ 00626c7c ["INT_ADD", "register:40f0:8", ["const:626c7c:8", "const:4:8"]]
+ 00626c7c ["CALL", null, ["callee:00c57e90:8"]]
- 00626c3c bytes 95c31894
+ 00626c7c bytes 85c41894
- 00626c44 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00626c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626c84 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00626c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626c44 bytes 08612591
+ 00626c84 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b5fdc68721019cb8ed5e64585bc81ad"></a>

### [`00626c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c54.md) → [`00626c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626c94.md) FUN_00626c94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626c98",
      "incomplete_value": false,
      "site": "00626c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626c58",
      "incomplete_value": false,
      "site": "00626c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00626c9c",
      "DATA",
      [
        "storage",
        "00c72958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626c9c",
      "DATA",
      [
        "storage",
        "00c72d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626c54.md#insn-00626c58)
- 新版 `00626c98`（命令位置の公開資料なし）

~~~diff
- 00626c58 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00626c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626c98 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00626c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626c58 bytes 08612591
+ 00626c98 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d03ca3e068ed3679b302a341fde4ca"></a>

### [`00626cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626cf0.md) → [`00626d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626d30.md) FUN_00626d30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626d44",
      "incomplete_value": false,
      "site": "00626d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626d04",
      "incomplete_value": false,
      "site": "00626d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00626d48",
      "DATA",
      [
        "storage",
        "00c729e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626d48",
      "DATA",
      [
        "storage",
        "00c72de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626cf0.md#insn-00626cfc) · [`00626d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626cf0.md#insn-00626d04)
- 新版 `00626d3c`（命令位置の公開資料なし） · `00626d44`（命令位置の公開資料なし）

~~~diff
- 00626cfc ["INT_ADD", "register:40f0:8", ["const:626cfc:8", "const:4:8"]]
- 00626cfc ["CALL", null, ["callee:00c57e90:8"]]
+ 00626d3c ["INT_ADD", "register:40f0:8", ["const:626d3c:8", "const:4:8"]]
+ 00626d3c ["CALL", null, ["callee:00c57e90:8"]]
- 00626cfc bytes 65c31894
+ 00626d3c bytes 55c41894
- 00626d04 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00626d04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626d04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626d04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626d44 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00626d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626d04 bytes 08a12791
+ 00626d44 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e5e5889d15e64a94c3eb797904b7f0"></a>

### [`00626d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d14.md) → [`00626d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626d54.md) FUN_00626d54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626d58",
      "incomplete_value": false,
      "site": "00626d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626d18",
      "incomplete_value": false,
      "site": "00626d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00626d5c",
      "DATA",
      [
        "storage",
        "00c729e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626d5c",
      "DATA",
      [
        "storage",
        "00c72de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d14.md#insn-00626d18)
- 新版 `00626d58`（命令位置の公開資料なし）

~~~diff
- 00626d18 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00626d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626d58 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00626d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626d18 bytes 08a12791
+ 00626d58 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb9dd256039d6a980c949f271f623e0"></a>

### [`00626d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d2c.md) → [`00626d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626d6c.md) FUN_00626d6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00626d80",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626d40",
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
      "00626d80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00626d80",
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

- 旧版 [`00626d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d2c.md#insn-00626d40)
- 新版 `00626d80`（命令位置の公開資料なし）

~~~diff
- 00626d40 ["INT_ADD", "register:40f0:8", ["const:626d40:8", "const:4:8"]]
- 00626d40 ["CALL", null, ["ram:47acb4:8"]]
+ 00626d80 ["INT_ADD", "register:40f0:8", ["const:626d80:8", "const:4:8"]]
+ 00626d80 ["CALL", null, ["ram:47acf4:8"]]
- 00626d40 bytes dd4ff997
+ 00626d80 bytes dd4ff997
~~~


<a id="compare-399b9b4ff4c16c63406bf14decab3585"></a>

### [`00626d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d84.md) → [`00626dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626dc4.md) FUN_00626dc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626dd8",
      "incomplete_value": false,
      "site": "00626ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626d98",
      "incomplete_value": false,
      "site": "00626d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00626ddc",
      "DATA",
      [
        "storage",
        "00c72a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626ddc",
      "DATA",
      [
        "storage",
        "00c72e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d84.md#insn-00626d90) · [`00626d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d84.md#insn-00626d98)
- 新版 `00626dd0`（命令位置の公開資料なし） · `00626dd8`（命令位置の公開資料なし）

~~~diff
- 00626d90 ["INT_ADD", "register:40f0:8", ["const:626d90:8", "const:4:8"]]
- 00626d90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626dd0 ["INT_ADD", "register:40f0:8", ["const:626dd0:8", "const:4:8"]]
+ 00626dd0 ["CALL", null, ["callee:00c57e90:8"]]
- 00626d90 bytes 40c31894
+ 00626dd0 bytes 30c41894
- 00626d98 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00626d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626dd8 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00626dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626d98 bytes 08a12991
+ 00626dd8 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d75a7a98f647301945fc76d440c5b6"></a>

### [`00626da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626da8.md) → [`00626de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626de8.md) FUN_00626de8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626dec",
      "incomplete_value": false,
      "site": "00626df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626dac",
      "incomplete_value": false,
      "site": "00626db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00626df0",
      "DATA",
      [
        "storage",
        "00c72a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626df0",
      "DATA",
      [
        "storage",
        "00c72e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626da8.md#insn-00626dac)
- 新版 `00626dec`（命令位置の公開資料なし）

~~~diff
- 00626dac ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00626dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626dec ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00626dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626dac bytes 08a12991
+ 00626dec bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85723e51891e3a647e165460018443d9"></a>

### [`00626dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626dc0.md) → [`00626e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626e00.md) FUN_00626e00

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
      "site": "00626e24",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626de4",
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
      "00626e24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00626e24",
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

- 旧版 [`00626de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626dc0.md#insn-00626de4) · [`00626df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626dc0.md#insn-00626df0)
- 新版 `00626e24`（命令位置の公開資料なし） · `00626e30`（命令位置の公開資料なし）

~~~diff
- 00626de4 ["INT_ADD", "register:40f0:8", ["const:626de4:8", "const:4:8"]]
- 00626de4 ["CALL", null, ["ram:47acb4:8"]]
+ 00626e24 ["INT_ADD", "register:40f0:8", ["const:626e24:8", "const:4:8"]]
+ 00626e24 ["CALL", null, ["ram:47acf4:8"]]
- 00626de4 bytes b44ff997
+ 00626e24 bytes b44ff997
- 00626df0 ["INT_ADD", "register:40f0:8", ["const:626df0:8", "const:4:8"]]
- 00626df0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00626e30 ["INT_ADD", "register:40f0:8", ["const:626e30:8", "const:4:8"]]
+ 00626e30 ["CALL", null, ["callee:0047cdd4:8"]]
- 00626df0 bytes e957f997
+ 00626e30 bytes e957f997
~~~


<a id="compare-4f170c0dcea5a7843bfe578739378034"></a>

### [`00626e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626e6c.md) → [`00626eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626eac.md) FUN_00626eac

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
      "definition_site": "00626eb8",
      "incomplete_value": false,
      "site": "00626eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626e78",
      "incomplete_value": false,
      "site": "00626e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00626eb8",
      "DATA",
      [
        "storage",
        "00c72ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626eb8",
      "DATA",
      [
        "storage",
        "00c72ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626e6c.md#insn-00626e74)
- 新版 `00626eb4`（命令位置の公開資料なし）

~~~diff
- 00626e74 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00626e74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00626e74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00626e74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00626eb4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00626eb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00626eb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00626eb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00626e74 bytes 29a12b91
+ 00626eb4 bytes 29a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0e4e8238f3a75c40e700bb297c31f48"></a>

### [`00626ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ecc.md) → [`00626f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626f0c.md) FUN_00626f0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626f20",
      "incomplete_value": false,
      "site": "00626f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626ee0",
      "incomplete_value": false,
      "site": "00626ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00626f24",
      "DATA",
      [
        "storage",
        "00c72b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626f24",
      "DATA",
      [
        "storage",
        "00c72f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ecc.md#insn-00626ed8) · [`00626ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ecc.md#insn-00626ee0)
- 新版 `00626f18`（命令位置の公開資料なし） · `00626f20`（命令位置の公開資料なし）

~~~diff
- 00626ed8 ["INT_ADD", "register:40f0:8", ["const:626ed8:8", "const:4:8"]]
- 00626ed8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00626f18 ["INT_ADD", "register:40f0:8", ["const:626f18:8", "const:4:8"]]
+ 00626f18 ["CALL", null, ["callee:00c57e90:8"]]
- 00626ed8 bytes eec21894
+ 00626f18 bytes dec31894
- 00626ee0 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00626ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626f20 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00626f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626ee0 bytes 08a12d91
+ 00626f20 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b648787df1c25efa736f9153b23ade"></a>

### [`00626ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ef0.md) → [`00626f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626f30.md) FUN_00626f30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00626f34",
      "incomplete_value": false,
      "site": "00626f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00626ef4",
      "incomplete_value": false,
      "site": "00626ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00626f38",
      "DATA",
      [
        "storage",
        "00c72b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626f38",
      "DATA",
      [
        "storage",
        "00c72f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00626ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ef0.md#insn-00626ef4)
- 新版 `00626f34`（命令位置の公開資料なし）

~~~diff
- 00626ef4 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00626ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00626ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00626ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00626f34 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00626f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00626f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00626f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00626ef4 bytes 08a12d91
+ 00626f34 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce38a397dd188af539217fc10a48dfa3"></a>

### [`00626f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626f08.md) → [`00626f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626f48.md) FUN_00626f48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "00626f70",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00626f30",
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
      "00626f70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00626f70",
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

- 旧版 [`00626f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626f08.md#insn-00626f30) · [`00626f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626f08.md#insn-00626f3c) · [`00626f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626f08.md#insn-00626f54)
- 新版 `00626f70`（命令位置の公開資料なし） · `00626f7c`（命令位置の公開資料なし） · `00626f94`（命令位置の公開資料なし）

~~~diff
- 00626f30 ["INT_ADD", "register:40f0:8", ["const:626f30:8", "const:4:8"]]
- 00626f30 ["CALL", null, ["ram:47acb4:8"]]
+ 00626f70 ["INT_ADD", "register:40f0:8", ["const:626f70:8", "const:4:8"]]
+ 00626f70 ["CALL", null, ["ram:47acf4:8"]]
- 00626f30 bytes 614ff997
+ 00626f70 bytes 614ff997
- 00626f3c ["INT_ADD", "register:40f0:8", ["const:626f3c:8", "const:4:8"]]
- 00626f3c ["CALL", null, ["callee:0047cdd4:8"]]
+ 00626f7c ["INT_ADD", "register:40f0:8", ["const:626f7c:8", "const:4:8"]]
+ 00626f7c ["CALL", null, ["callee:0047cdd4:8"]]
- 00626f3c bytes 9657f997
+ 00626f7c bytes 9657f997
- 00626f54 ["INT_ADD", "register:40f0:8", ["const:626f54:8", "const:4:8"]]
- 00626f54 ["CALL", null, ["callee:008514f8:8"]]
+ 00626f94 ["INT_ADD", "register:40f0:8", ["const:626f94:8", "const:4:8"]]
+ 00626f94 ["CALL", null, ["callee:008514f8:8"]]
- 00626f54 bytes 59a90894
+ 00626f94 bytes 59a90894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24cc188b648bc93954e23a0bc3308f29"></a>

### [`00627064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md) → [`006270a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/006270a4.md) FUN_006270a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006270c8",
      "incomplete_value": false,
      "site": "006270cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627088",
      "incomplete_value": false,
      "site": "0062708c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "006270cc",
      "DATA",
      [
        "storage",
        "00c72be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006270cc",
      "DATA",
      [
        "storage",
        "00c72fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md#insn-00627078) · [`00627088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md#insn-00627088)
- 新版 `006270b8`（命令位置の公開資料なし） · `006270c8`（命令位置の公開資料なし）

~~~diff
- 00627078 ["INT_ADD", "register:40f0:8", ["const:627078:8", "const:4:8"]]
- 00627078 ["CALL", null, ["callee:00c57e90:8"]]
+ 006270b8 ["INT_ADD", "register:40f0:8", ["const:6270b8:8", "const:4:8"]]
+ 006270b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00627078 bytes 86c21894
+ 006270b8 bytes 76c31894
- 00627088 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00627088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00627088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00627088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006270c8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 006270c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006270c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006270c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00627088 bytes 08a12f91
+ 006270c8 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18af8437c5b573899266c506e5bc02b9"></a>

### [`006270a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270a4.md) → [`006270e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/006270e4.md) FUN_006270e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006270e8",
      "incomplete_value": false,
      "site": "006270ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006270a8",
      "incomplete_value": false,
      "site": "006270ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "006270ec",
      "DATA",
      [
        "storage",
        "00c72be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006270ec",
      "DATA",
      [
        "storage",
        "00c72fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006270a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270a4.md#insn-006270a8)
- 新版 `006270e8`（命令位置の公開資料なし）

~~~diff
- 006270a8 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 006270a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006270a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006270a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006270e8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 006270e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006270e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006270e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006270a8 bytes 08a12f91
+ 006270e8 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2383cb186618bf8f5b347be3d1f6b5a"></a>

### [`006270cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md) → [`0062710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/0062710c.md) FUN_0062710c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00627210",
      "incomplete_value": true,
      "site": "00627220",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006271d0",
      "incomplete_value": true,
      "site": "006271e0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f0a:8"
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
      "definition_site": "00627214",
      "incomplete_value": true,
      "site": "00627224",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006271d4",
      "incomplete_value": true,
      "site": "006271e4",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "definition_site": "00627218",
      "incomplete_value": true,
      "site": "00627228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006271d8",
      "incomplete_value": true,
      "site": "006271e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a50:8"
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
      "00627164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00627174",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "00627210",
      "READ",
      [
        "storage",
        "002bef0a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00627164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00627174",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "00627210",
      "READ",
      [
        "storage",
        "002bef4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md#insn-00627124) · [`00627134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md#insn-00627134) · [`006271a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md#insn-006271a4)
- 新版 `00627164`（命令位置の公開資料なし） · `00627174`（命令位置の公開資料なし） · `006271e4`（命令位置の公開資料なし）

~~~diff
- 00627124 ["INT_ADD", "register:40f0:8", ["const:627124:8", "const:4:8"]]
- 00627124 ["CALL", null, ["ram:47acb4:8"]]
+ 00627164 ["INT_ADD", "register:40f0:8", ["const:627164:8", "const:4:8"]]
+ 00627164 ["CALL", null, ["ram:47acf4:8"]]
- 00627124 bytes e44ef997
+ 00627164 bytes e44ef997
- 00627134 ["INT_ADD", "register:40f0:8", ["const:627134:8", "const:4:8"]]
- 00627134 ["CALL", null, ["ram:71be98:8"]]
+ 00627174 ["INT_ADD", "register:40f0:8", ["const:627174:8", "const:4:8"]]
+ 00627174 ["CALL", null, ["ram:71bed8:8"]]
- 00627134 bytes 59d30394
+ 00627174 bytes 59d30394
- 006271a4 ["INT_ADD", "register:40f0:8", ["const:6271a4:8", "const:4:8"]]
- 006271a4 ["CALL", null, ["callee:008514f8:8"]]
+ 006271e4 ["INT_ADD", "register:40f0:8", ["const:6271e4:8", "const:4:8"]]
+ 006271e4 ["CALL", null, ["callee:008514f8:8"]]
- 006271a4 bytes c5a80894
+ 006271e4 bytes c5a80894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d7af14588afdbfc854eab4af77bb58"></a>

### [`0062779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md) → [`006277dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/006277dc.md) FUN_006277dc

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
      "definition_site": "006277fc",
      "incomplete_value": false,
      "site": "00627800",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006277bc",
      "incomplete_value": false,
      "site": "006277c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "00627800",
      "DATA",
      [
        "storage",
        "00c72c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00627800",
      "DATA",
      [
        "storage",
        "00c73058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006277b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md#insn-006277b0) · [`006277b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md#insn-006277b8) · [`006277bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md#insn-006277bc)
- 新版 `006277f0`（命令位置の公開資料なし） · `006277f8`（命令位置の公開資料なし） · `006277fc`（命令位置の公開資料なし）

~~~diff
- 006277b0 ["INT_ADD", "register:40f0:8", ["const:6277b0:8", "const:4:8"]]
- 006277b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 006277f0 ["INT_ADD", "register:40f0:8", ["const:6277f0:8", "const:4:8"]]
+ 006277f0 ["CALL", null, ["callee:00c57e90:8"]]
- 006277b0 bytes b8c01894
+ 006277f0 bytes a8c11894
- 006277b8 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 006277f8 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 006277b8 bytes 483200f0
+ 006277f8 bytes 68320090
- 006277bc ["COPY", "tmp:0:8", ["const:c58:8"]]
- 006277bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006277bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006277bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006277fc ["COPY", "tmp:0:8", ["const:58:8"]]
+ 006277fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006277fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006277fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006277bc bytes 08613191
+ 006277fc bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b96ad0959e68541d2a717807c862de"></a>

### [`006277d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006277d4.md) → [`00627814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627814.md) FUN_00627814

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
      "definition_site": "00627818",
      "incomplete_value": false,
      "site": "0062781c",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006277d8",
      "incomplete_value": false,
      "site": "006277dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "0062781c",
      "DATA",
      [
        "storage",
        "00c72c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0062781c",
      "DATA",
      [
        "storage",
        "00c73058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006277d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006277d4.md#insn-006277d4) · [`006277d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006277d4.md#insn-006277d8)
- 新版 `00627814`（命令位置の公開資料なし） · `00627818`（命令位置の公開資料なし）

~~~diff
- 006277d4 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00627814 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 006277d4 bytes 483200f0
+ 00627814 bytes 68320090
- 006277d8 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 006277d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006277d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006277d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00627818 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00627818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00627818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00627818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006277d8 bytes 08613191
+ 00627818 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b9987f818b2559e325e9651cb78d95"></a>

### [`00627c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md) → [`00627c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627c78.md) FUN_00627c78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00627c8c",
      "incomplete_value": false,
      "site": "00627c90",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627c4c",
      "incomplete_value": false,
      "site": "00627c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00627c90",
      "DATA",
      [
        "storage",
        "00c72ce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00627c90",
      "DATA",
      [
        "storage",
        "00c730e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md#insn-00627c44) · [`00627c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md#insn-00627c48) · [`00627c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md#insn-00627c4c)
- 新版 `00627c84`（命令位置の公開資料なし） · `00627c88`（命令位置の公開資料なし） · `00627c8c`（命令位置の公開資料なし）

~~~diff
- 00627c44 ["INT_ADD", "register:40f0:8", ["const:627c44:8", "const:4:8"]]
- 00627c44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00627c84 ["INT_ADD", "register:40f0:8", ["const:627c84:8", "const:4:8"]]
+ 00627c84 ["CALL", null, ["callee:00c57e90:8"]]
- 00627c44 bytes 93bf1894
+ 00627c84 bytes 83c01894
- 00627c48 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00627c88 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00627c48 bytes 483200f0
+ 00627c88 bytes 68320090
- 00627c4c ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00627c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00627c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00627c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00627c8c ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00627c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00627c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00627c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00627c4c bytes 08a13391
+ 00627c8c bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d7b844fd403dbf571d60c64efd3655"></a>

### [`00627c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md) → [`00627cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627cb4.md) FUN_00627cb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00627d04",
      "incomplete_value": false,
      "site": "00627d14",
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
      "definition_site": "00627cc4",
      "incomplete_value": false,
      "site": "00627cd4",
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
      "definition_site": "00627d0c",
      "incomplete_value": false,
      "site": "00627d14",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627ccc",
      "incomplete_value": false,
      "site": "00627cd4",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00627e20",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00627de0",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00627cf8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00627d04",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00627d0c",
      "PARAM",
      [
        "storage",
        "00c71578",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00627cf8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00627d04",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00627d0c",
      "PARAM",
      [
        "storage",
        "00c71978",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md#insn-00627cd4) · [`00627de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md#insn-00627de0) · [`00627cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c74.md#insn-00627cac)
- 新版 `00627d14`（命令位置の公開資料なし） · `00627e20`（命令位置の公開資料なし） · `00627cec`（命令位置の公開資料なし）

~~~diff
- 00627cd4 ["INT_ADD", "register:40f0:8", ["const:627cd4:8", "const:4:8"]]
- 00627cd4 ["CALL", null, ["callee:00c58610:8"]]
+ 00627d14 ["INT_ADD", "register:40f0:8", ["const:627d14:8", "const:4:8"]]
+ 00627d14 ["CALL", null, ["callee:00c58610:8"]]
- 00627cd4 bytes 4fc11894
+ 00627d14 bytes 3fc21894
- 00627de0 ["INT_ADD", "register:40f0:8", ["const:627de0:8", "const:4:8"]]
- 00627de0 ["CALL", null, ["ram:71be98:8"]]
+ 00627e20 ["INT_ADD", "register:40f0:8", ["const:627e20:8", "const:4:8"]]
+ 00627e20 ["CALL", null, ["ram:71bed8:8"]]
- 00627de0 bytes 2ed00394
+ 00627e20 bytes 2ed00394
- 00627cac ["INT_ADD", "register:40f0:8", ["const:627cac:8", "const:4:8"]]
- 00627cac ["CALL", null, ["callee:008b9290:8"]]
+ 00627cec ["INT_ADD", "register:40f0:8", ["const:627cec:8", "const:4:8"]]
+ 00627cec ["CALL", null, ["callee:008b9290:8"]]
- 00627cac bytes 68450a94
+ 00627cec bytes 69450a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fde9c3394026faf72f5aaf44426332f"></a>

### [`00627e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627e78.md) → [`00627eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627eb8.md) FUN_00627eb8

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
      "definition_site": "00627edc",
      "incomplete_value": false,
      "site": "00627edc",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627e9c",
      "incomplete_value": false,
      "site": "00627e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "00627edc",
      "DATA",
      [
        "storage",
        "00c72d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00627edc",
      "DATA",
      [
        "storage",
        "00c73178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627e78.md#insn-00627e8c) · [`00627e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627e78.md#insn-00627e94) · [`00627e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627e78.md#insn-00627e98)
- 新版 `00627ecc`（命令位置の公開資料なし） · `00627ed4`（命令位置の公開資料なし） · `00627ed8`（命令位置の公開資料なし）

~~~diff
- 00627e8c ["INT_ADD", "register:40f0:8", ["const:627e8c:8", "const:4:8"]]
- 00627e8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00627ecc ["INT_ADD", "register:40f0:8", ["const:627ecc:8", "const:4:8"]]
+ 00627ecc ["CALL", null, ["callee:00c57e90:8"]]
- 00627e8c bytes 01bf1894
+ 00627ecc bytes f1bf1894
- 00627e94 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00627ed4 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00627e94 bytes 483200f0
+ 00627ed4 bytes 68320090
- 00627e98 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00627e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00627e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00627e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00627ed8 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 00627ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00627ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00627ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00627e98 bytes 08e13591
+ 00627ed8 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36cabc9092cf82453a908fccb8b2109a"></a>

### [`00627eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627eac.md) → [`00627eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627eec.md) FUN_00627eec

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
      "definition_site": "00627ef8",
      "incomplete_value": false,
      "site": "00627ef8",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627eb8",
      "incomplete_value": false,
      "site": "00627eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "00627ef8",
      "DATA",
      [
        "storage",
        "00c72d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00627ef8",
      "DATA",
      [
        "storage",
        "00c73178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00627eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627eac.md#insn-00627eb0) · [`00627eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627eac.md#insn-00627eb4)
- 新版 `00627ef0`（命令位置の公開資料なし） · `00627ef4`（命令位置の公開資料なし）

~~~diff
- 00627eb0 ["COPY", "register:4048:8", ["const:c72000:8"]]
+ 00627ef0 ["COPY", "register:4048:8", ["const:c73000:8"]]
- 00627eb0 bytes 493200f0
+ 00627ef0 bytes 69320090
- 00627eb4 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00627eb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00627eb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00627eb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00627ef4 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 00627ef4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00627ef4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00627ef4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00627eb4 bytes 29e13591
+ 00627ef4 bytes 29e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30fc689088b7a4ebe30949aef3480e7e"></a>

### [`00627ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627ec8.md) → [`00627f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627f08.md) FUN_00627f08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "00627f30",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00627ef0",
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
      "00627f30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00627f30",
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

- 旧版 [`00627ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627ec8.md#insn-00627ef0) · [`00627efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627ec8.md#insn-00627efc)
- 新版 `00627f30`（命令位置の公開資料なし） · `00627f3c`（命令位置の公開資料なし）

~~~diff
- 00627ef0 ["INT_ADD", "register:40f0:8", ["const:627ef0:8", "const:4:8"]]
- 00627ef0 ["CALL", null, ["ram:47acb4:8"]]
+ 00627f30 ["INT_ADD", "register:40f0:8", ["const:627f30:8", "const:4:8"]]
+ 00627f30 ["CALL", null, ["ram:47acf4:8"]]
- 00627ef0 bytes 714bf997
+ 00627f30 bytes 714bf997
- 00627efc ["INT_ADD", "register:40f0:8", ["const:627efc:8", "const:4:8"]]
- 00627efc ["CALL", null, ["callee:0047cdd4:8"]]
+ 00627f3c ["INT_ADD", "register:40f0:8", ["const:627f3c:8", "const:4:8"]]
+ 00627f3c ["CALL", null, ["callee:0047cdd4:8"]]
- 00627efc bytes a653f997
+ 00627f3c bytes a653f997
~~~


<a id="compare-a9b9e610206232a47c7cee199f454e35"></a>

### [`00628120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md) → [`00628160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628160.md) FUN_00628160

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00627f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627f54.md) [`00628120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00627f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/00627f94.md) [`00628160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628160.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006282d4",
      "incomplete_value": false,
      "site": "006282e0",
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
      "definition_site": "00628294",
      "incomplete_value": false,
      "site": "006282a0",
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
      "definition_site": "0062838c",
      "incomplete_value": false,
      "site": "00628394",
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
      "definition_site": "0062834c",
      "incomplete_value": false,
      "site": "00628354",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006283a4",
      "incomplete_value": true,
      "site": "006283b4",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00628364",
      "incomplete_value": true,
      "site": "00628374",
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
            "const:ea9:8"
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
      "006282d4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0062838c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "006283a4",
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
      "006282d4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0062838c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006283a4",
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

- 旧版 [`006282a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md#insn-006282a0) · [`00628354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md#insn-00628354) · [`00628374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md#insn-00628374)
- 新版 `006282e0`（命令位置の公開資料なし） · `00628394`（命令位置の公開資料なし） · `006283b4`（命令位置の公開資料なし）

~~~diff
- 006282a0 ["INT_ADD", "register:40f0:8", ["const:6282a0:8", "const:4:8"]]
- 006282a0 ["CALL", null, ["callee:00441e94:8"]]
+ 006282e0 ["INT_ADD", "register:40f0:8", ["const:6282e0:8", "const:4:8"]]
+ 006282e0 ["CALL", null, ["callee:00441e94:8"]]
- 006282a0 bytes ed66f897
+ 006282e0 bytes ed66f897
- 00628354 ["INT_ADD", "register:40f0:8", ["const:628354:8", "const:4:8"]]
- 00628354 ["CALL", null, ["callee:00441e94:8"]]
+ 00628394 ["INT_ADD", "register:40f0:8", ["const:628394:8", "const:4:8"]]
+ 00628394 ["CALL", null, ["callee:00441e94:8"]]
- 00628354 bytes c066f897
+ 00628394 bytes c066f897
- 00628374 ["INT_ADD", "register:40f0:8", ["const:628374:8", "const:4:8"]]
- 00628374 ["CALL", null, ["callee:004427f4:8"]]
+ 006283b4 ["INT_ADD", "register:40f0:8", ["const:6283b4:8", "const:4:8"]]
+ 006283b4 ["CALL", null, ["callee:004427f4:8"]]
- 00628374 bytes 1069f897
+ 006283b4 bytes 1069f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b64443bb7c6fea9b1781c609e8dc395"></a>

### [`00628d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md) → [`00628d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628d44.md) FUN_00628d44

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00628120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628120.md) [`00628d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00628160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628160.md) [`00628d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00628/00628d44.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00628eb8",
      "incomplete_value": false,
      "site": "00628ec0",
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
      "definition_site": "00628e78",
      "incomplete_value": false,
      "site": "00628e80",
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
      "definition_site": "00628f94",
      "incomplete_value": false,
      "site": "00628fa0",
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
      "definition_site": "00628f54",
      "incomplete_value": false,
      "site": "00628f60",
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
      "definition_site": "00629044",
      "incomplete_value": false,
      "site": "00629050",
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
      "definition_site": "00629004",
      "incomplete_value": false,
      "site": "00629010",
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
      "00628eb8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00628f78",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00628f94",
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
      "00628eb8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00628f78",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00628f94",
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

- 旧版 [`00628e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md#insn-00628e80) · [`00628f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md#insn-00628f60) · [`00629010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00628/00628d04.md#insn-00629010)
- 新版 `00628ec0`（命令位置の公開資料なし） · `00628fa0`（命令位置の公開資料なし） · `00629050`（命令位置の公開資料なし）

~~~diff
- 00628e80 ["INT_ADD", "register:40f0:8", ["const:628e80:8", "const:4:8"]]
- 00628e80 ["CALL", null, ["callee:00441e94:8"]]
+ 00628ec0 ["INT_ADD", "register:40f0:8", ["const:628ec0:8", "const:4:8"]]
+ 00628ec0 ["CALL", null, ["callee:00441e94:8"]]
- 00628e80 bytes f563f897
+ 00628ec0 bytes f563f897
- 00628f60 ["INT_ADD", "register:40f0:8", ["const:628f60:8", "const:4:8"]]
- 00628f60 ["CALL", null, ["callee:004427f4:8"]]
+ 00628fa0 ["INT_ADD", "register:40f0:8", ["const:628fa0:8", "const:4:8"]]
+ 00628fa0 ["CALL", null, ["callee:004427f4:8"]]
- 00628f60 bytes 1566f897
+ 00628fa0 bytes 1566f897
- 00629010 ["INT_ADD", "register:40f0:8", ["const:629010:8", "const:4:8"]]
- 00629010 ["CALL", null, ["callee:004427f4:8"]]
+ 00629050 ["INT_ADD", "register:40f0:8", ["const:629050:8", "const:4:8"]]
+ 00629050 ["CALL", null, ["callee:004427f4:8"]]
- 00629010 bytes e965f897
+ 00629050 bytes e965f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d19e9cd36863a7559268856599fcbf"></a>

### [`00629758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629758.md) → [`00629798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629798.md) _INIT_77

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006297d4",
      "incomplete_value": true,
      "site": "006297f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00629794",
      "incomplete_value": true,
      "site": "006297b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006297f8",
      "incomplete_value": true,
      "site": "00629814",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006297b8",
      "incomplete_value": true,
      "site": "006297d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00629818",
      "incomplete_value": true,
      "site": "00629834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006297d8",
      "incomplete_value": true,
      "site": "006297f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006297d4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006297f8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00629818",
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
      "006297d4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006297f8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00629818",
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

- 旧版 [`006297f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629758.md#insn-006297f0) · [`0062998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629758.md#insn-0062998c) · [`00629784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629758.md#insn-00629784)
- 新版 `00629830`（命令位置の公開資料なし） · `006299cc`（命令位置の公開資料なし） · `006297c4`（命令位置の公開資料なし）

~~~diff
- 006297f0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006297f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006297f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006297f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00629830 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00629830 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00629830 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00629830 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006297f0 bytes 4a553a91
+ 00629830 bytes 4a893d91
- 0062998c ["INT_ADD", "register:40f0:8", ["const:62998c:8", "const:4:8"]]
- 0062998c ["CALL", null, ["callee:00c57e30:8"]]
+ 006299cc ["INT_ADD", "register:40f0:8", ["const:6299cc:8", "const:4:8"]]
+ 006299cc ["CALL", null, ["callee:00c57e30:8"]]
- 0062998c bytes 29b81894
+ 006299cc bytes 19b91894
- 00629784 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00629784 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00629784 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00629784 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006297c4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 006297c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006297c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006297c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00629784 bytes 73621791
+ 006297c4 bytes 73622791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b138742db6af461794ba24b31b9d2377"></a>

### [`00629d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629d80.md) → [`00629dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629dc0.md) FUN_00629dc0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) · 呼出先 6件 [`00489154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009ccb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb7c.md) · 呼出先 6件 [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00629e10",
      "incomplete_value": true,
      "site": "00629e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:600:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00629dd0",
      "incomplete_value": true,
      "site": "00629dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
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
      "definition_site": "00629e14",
      "incomplete_value": true,
      "site": "00629e14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00629dd4",
      "incomplete_value": true,
      "site": "00629dd4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00629e50",
      "incomplete_value": true,
      "site": "00629e60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00629e10",
      "incomplete_value": true,
      "site": "00629e20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da1:8"
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
      "00629dfc",
      "READ",
      [
        "storage",
        "002bb5c0",
        null,
        null
      ]
    ],
    [
      "00629e04",
      "READ",
      [
        "storage",
        "002bb5c5",
        null,
        "string"
      ]
    ],
    [
      "00629e50",
      "READ",
      [
        "storage",
        "002a8da1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00629dfc",
      "READ",
      [
        "storage",
        "002bb600",
        null,
        null
      ]
    ],
    [
      "00629e04",
      "READ",
      [
        "storage",
        "002bb605",
        null,
        "string"
      ]
    ],
    [
      "00629e50",
      "READ",
      [
        "storage",
        "002a8e6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00629dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629d80.md#insn-00629dac) · [`00629db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629d80.md#insn-00629db8) · [`00629df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629d80.md#insn-00629df0)
- 新版 `00629dec`（命令位置の公開資料なし） · `00629df8`（命令位置の公開資料なし） · `00629e30`（命令位置の公開資料なし）

~~~diff
- 00629dac ["INT_ADD", "register:40f0:8", ["const:629dac:8", "const:4:8"]]
- 00629dac ["CALL", null, ["callee:008514f8:8"]]
+ 00629dec ["INT_ADD", "register:40f0:8", ["const:629dec:8", "const:4:8"]]
+ 00629dec ["CALL", null, ["callee:008514f8:8"]]
- 00629dac bytes c39d0894
+ 00629dec bytes c39d0894
- 00629db8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00629db8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00629db8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00629db8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00629df8 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00629df8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00629df8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00629df8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00629db8 bytes 29011791
+ 00629df8 bytes 29011891
- 00629df0 ["INT_ADD", "register:40f0:8", ["const:629df0:8", "const:4:8"]]
- 00629df0 ["CALL", null, ["callee:0048ce54:8"]]
+ 00629e30 ["INT_ADD", "register:40f0:8", ["const:629e30:8", "const:4:8"]]
+ 00629e30 ["CALL", null, ["callee:0048ce54:8"]]
- 00629df0 bytes 098cf997
+ 00629e30 bytes 098cf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3250904b9454242811130e9d82c80d4"></a>

### [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) → [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) FUN_0062a23c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 15件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 15件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.08% / 新版 97.08%

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
      "site": "0062a288",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062a248",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "0062a300",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062a2c0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062a390",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062a350",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062a288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0062a300",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0062a390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0062a288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0062a300",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0062a390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062a248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md#insn-0062a248) · [`0062a2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md#insn-0062a2c0) · [`0062a350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md#insn-0062a350)
- 新版 `0062a288`（命令位置の公開資料なし） · `0062a300`（命令位置の公開資料なし） · `0062a390`（命令位置の公開資料なし）

~~~diff
- 0062a248 ["INT_ADD", "register:40f0:8", ["const:62a248:8", "const:4:8"]]
- 0062a248 ["CALL", null, ["ram:46c984:8"]]
+ 0062a288 ["INT_ADD", "register:40f0:8", ["const:62a288:8", "const:4:8"]]
+ 0062a288 ["CALL", null, ["ram:46c9c4:8"]]
- 0062a248 bytes cf09f997
+ 0062a288 bytes cf09f997
- 0062a2c0 ["INT_ADD", "register:40f0:8", ["const:62a2c0:8", "const:4:8"]]
- 0062a2c0 ["CALL", null, ["ram:46c984:8"]]
+ 0062a300 ["INT_ADD", "register:40f0:8", ["const:62a300:8", "const:4:8"]]
+ 0062a300 ["CALL", null, ["ram:46c9c4:8"]]
- 0062a2c0 bytes b109f997
+ 0062a300 bytes b109f997
- 0062a350 ["INT_ADD", "register:40f0:8", ["const:62a350:8", "const:4:8"]]
- 0062a350 ["CALL", null, ["ram:46c984:8"]]
+ 0062a390 ["INT_ADD", "register:40f0:8", ["const:62a390:8", "const:4:8"]]
+ 0062a390 ["CALL", null, ["ram:46c9c4:8"]]
- 0062a350 bytes 8d09f997
+ 0062a390 bytes 8d09f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130968a0454486b63d69248b5b5a0087"></a>

### [`0062a464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a464.md) → [`0062a4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a4a4.md) _INIT_78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062a504",
      "incomplete_value": true,
      "site": "0062a520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0062a4c4",
      "incomplete_value": true,
      "site": "0062a4e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0062a544",
      "incomplete_value": true,
      "site": "0062a55c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0062a504",
      "incomplete_value": true,
      "site": "0062a51c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062a560",
      "incomplete_value": true,
      "site": "0062a57c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0062a520",
      "incomplete_value": true,
      "site": "0062a53c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062a4e0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0062a504",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0062a524",
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
      "0062a4e0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0062a504",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0062a524",
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

- 旧版 [`0062a4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a464.md#insn-0062a4dc) · [`0062a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a464.md#insn-0062a4fc) · [`0062a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a464.md#insn-0062a698)
- 新版 `0062a51c`（命令位置の公開資料なし） · `0062a53c`（命令位置の公開資料なし） · `0062a6d8`（命令位置の公開資料なし）

~~~diff
- 0062a4dc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0062a4dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0062a4dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0062a4dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0062a51c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0062a51c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0062a51c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0062a51c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0062a4dc bytes 4a093691
+ 0062a51c bytes 4a093791
- 0062a4fc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0062a4fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0062a4fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0062a4fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0062a53c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0062a53c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0062a53c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0062a53c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0062a4fc bytes 4a553a91
+ 0062a53c bytes 4a893d91
- 0062a698 ["INT_ADD", "register:40f0:8", ["const:62a698:8", "const:4:8"]]
- 0062a698 ["CALL", null, ["callee:00c57e30:8"]]
+ 0062a6d8 ["INT_ADD", "register:40f0:8", ["const:62a6d8:8", "const:4:8"]]
+ 0062a6d8 ["CALL", null, ["callee:00c57e30:8"]]
- 0062a698 bytes e6b41894
+ 0062a6d8 bytes d6b51894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514118887463430c8dc5c09981850216"></a>

### [`0062a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md) → [`0062a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a834.md) FUN_0062a834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062b034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md) · 呼出先 19件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0062fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0062b074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b074.md) · 呼出先 19件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0062fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062fa58.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.25% / 新版 89.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062a90c",
      "incomplete_value": true,
      "site": "0062a91c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062a8cc",
      "incomplete_value": true,
      "site": "0062a8dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e37:8"
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
      "definition_site": "0062aa4c",
      "incomplete_value": true,
      "site": "0062aa5c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062aa0c",
      "incomplete_value": true,
      "site": "0062aa1c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:5c:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0062ab5c",
      "incomplete_value": false,
      "site": "0062ab5c",
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
      "definition_site": "0062ab1c",
      "incomplete_value": false,
      "site": "0062ab1c",
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
    "ordinal": 20,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062a90c",
      "READ",
      [
        "storage",
        "002a9e37",
        null,
        "string"
      ]
    ],
    [
      "0062aa38",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0062aa4c",
      "READ",
      [
        "storage",
        "002b505c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0062a90c",
      "READ",
      [
        "storage",
        "002a9f04",
        null,
        "string"
      ]
    ],
    [
      "0062aa38",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0062aa4c",
      "READ",
      [
        "storage",
        "002b509c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md#insn-0062a9dc) · [`0062aa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md#insn-0062aa38) · [`0062aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md#insn-0062aae0)
- 新版 `0062aa1c`（命令位置の公開資料なし） · `0062aa78`（命令位置の公開資料なし） · `0062ab20`（命令位置の公開資料なし）

~~~diff
- 0062a9dc ["INT_ADD", "register:40f0:8", ["const:62a9dc:8", "const:4:8"]]
- 0062a9dc ["CALL", null, ["callee:00a8344c:8"]]
+ 0062aa1c ["INT_ADD", "register:40f0:8", ["const:62aa1c:8", "const:4:8"]]
+ 0062aa1c ["CALL", null, ["callee:00a8344c:8"]]
- 0062a9dc bytes 1e621194
+ 0062aa1c bytes 8c621194
- 0062aa38 ["INT_ADD", "register:40f0:8", ["const:62aa38:8", "const:4:8"]]
- 0062aa38 ["CALL", null, ["callee:0047e60c:8"]]
+ 0062aa78 ["INT_ADD", "register:40f0:8", ["const:62aa78:8", "const:4:8"]]
+ 0062aa78 ["CALL", null, ["callee:0047e60c:8"]]
- 0062aa38 bytes e54ef997
+ 0062aa78 bytes e54ef997
- 0062aae0 ["INT_ADD", "register:40f0:8", ["const:62aae0:8", "const:4:8"]]
- 0062aae0 ["CALL", null, ["callee:00c57e80:8"]]
+ 0062ab20 ["INT_ADD", "register:40f0:8", ["const:62ab20:8", "const:4:8"]]
+ 0062ab20 ["CALL", null, ["callee:00c57e80:8"]]
- 0062aae0 bytes e8b31894
+ 0062ab20 bytes d8b41894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f66bb7e3cfb0719f4d0195ba14ef1aca"></a>

### [`0062ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062ada8.md) → [`0062ade8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062ade8.md) FUN_0062ade8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062c7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c7b0.md) · 呼出先 5件 [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`00728664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728664.md) [`00728680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728680.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md)
- 新版 呼出元 1件 [`0062c7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c7f0.md) · 呼出先 5件 [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`007286a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/007286a4.md) [`007286c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/007286c0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.39% / 新版 99.39%

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
      "site": "0062af44",
      "value": [
        "leaf",
        "ram:71c460:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062af04",
      "value": [
        "leaf",
        "ram:71c420:8"
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
      "0062af44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ]
  ],
  "added": [
    [
      "0062af44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062af04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062ada8.md#insn-0062af04) · [`0062add0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062ada8.md#insn-0062add0) · [`0062ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062ada8.md#insn-0062ae00)
- 新版 `0062af44`（命令位置の公開資料なし） · `0062ae10`（命令位置の公開資料なし） · `0062ae40`（命令位置の公開資料なし）

~~~diff
- 0062af04 ["INT_ADD", "register:40f0:8", ["const:62af04:8", "const:4:8"]]
- 0062af04 ["CALL", null, ["ram:71c420:8"]]
+ 0062af44 ["INT_ADD", "register:40f0:8", ["const:62af44:8", "const:4:8"]]
+ 0062af44 ["CALL", null, ["ram:71c460:8"]]
- 0062af04 bytes 47c50394
+ 0062af44 bytes 47c50394
- 0062add0 ["INT_ADD", "register:40f0:8", ["const:62add0:8", "const:4:8"]]
- 0062add0 ["CALL", null, ["callee:008514f8:8"]]
+ 0062ae10 ["INT_ADD", "register:40f0:8", ["const:62ae10:8", "const:4:8"]]
+ 0062ae10 ["CALL", null, ["callee:008514f8:8"]]
- 0062add0 bytes ba990894
+ 0062ae10 bytes ba990894
- 0062ae00 ["INT_ADD", "register:40f0:8", ["const:62ae00:8", "const:4:8"]]
- 0062ae00 ["CALL", null, ["callee:008514f8:8"]]
+ 0062ae40 ["INT_ADD", "register:40f0:8", ["const:62ae40:8", "const:4:8"]]
+ 0062ae40 ["CALL", null, ["callee:008514f8:8"]]
- 0062ae00 bytes ae990894
+ 0062ae40 bytes ae990894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8f63fdab3dff96713219cdb6b6747f"></a>

### [`0062b034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md) → [`0062b074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b074.md) FUN_0062b074

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) · 呼出先 20件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`0062a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md) [`0062abac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062abac.md)
- 新版 呼出元 1件 [`0062e1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062e1a0.md) · 呼出先 20件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`0062a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a834.md) [`0062abec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062abec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062b2ac",
      "incomplete_value": false,
      "site": "0062b2c0",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062b26c",
      "incomplete_value": false,
      "site": "0062b280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0062b40c",
      "incomplete_value": false,
      "site": "0062b40c",
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
      "definition_site": "0062b3cc",
      "incomplete_value": false,
      "site": "0062b3cc",
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
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0062b410",
      "incomplete_value": false,
      "site": "0062b410",
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
      "definition_site": "0062b3d0",
      "incomplete_value": false,
      "site": "0062b3d0",
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
    "ordinal": 33,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062b0ac",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0062b0c0",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ],
    [
      "0062b0c4",
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
      "0062b0ac",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0062b0c0",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ],
    [
      "0062b0c4",
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

- 旧版 [`0062b060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md#insn-0062b060) · [`0062b0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md#insn-0062b0a0) · [`0062b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md#insn-0062b0e0)
- 新版 `0062b0a0`（命令位置の公開資料なし） · `0062b0e0`（命令位置の公開資料なし） · `0062b120`（命令位置の公開資料なし）

~~~diff
- 0062b060 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0062b060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0062b060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0062b060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0062b0a0 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0062b0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0062b0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0062b0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0062b060 bytes 08e12c91
+ 0062b0a0 bytes 08e13c91
- 0062b0a0 ["INT_ADD", "register:40f0:8", ["const:62b0a0:8", "const:4:8"]]
- 0062b0a0 ["CALL", null, ["callee:0047e8dc:8"]]
+ 0062b0e0 ["INT_ADD", "register:40f0:8", ["const:62b0e0:8", "const:4:8"]]
+ 0062b0e0 ["CALL", null, ["callee:0047e8dc:8"]]
- 0062b0a0 bytes ff4df997
+ 0062b0e0 bytes ff4df997
- 0062b0e0 ["INT_ADD", "register:40f0:8", ["const:62b0e0:8", "const:4:8"]]
- 0062b0e0 ["CALL", null, ["callee:00c57e80:8"]]
+ 0062b120 ["INT_ADD", "register:40f0:8", ["const:62b120:8", "const:4:8"]]
+ 0062b120 ["CALL", null, ["callee:00c57e80:8"]]
- 0062b0e0 bytes 68b21894
+ 0062b120 bytes 58b31894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d78fd1e747cee20fce655d2a9e2f1c3"></a>

### [`0062b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) → [`0062b714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b714.md) FUN_0062b714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`00630a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a9c.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044b148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b148.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00491c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md) [`0062ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062ba20.md)
- 新版 呼出元 2件 [`0062ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062ecfc.md) [`00630adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630adc.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044b188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b188.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00491cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md) [`0062ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062ba60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062b7d8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062b798",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062b7ec",
      "incomplete_value": false,
      "site": "0062b7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e8f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062b7ac",
      "incomplete_value": false,
      "site": "0062b7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e4f:8"
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
      "0062b7d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0062b7ec",
      "PARAM",
      [
        "storage",
        "002b1e4f",
        null,
        "string"
      ]
    ],
    [
      "0062b860",
      "PARAM",
      [
        "storage",
        "002b387b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0062b7d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0062b7ec",
      "PARAM",
      [
        "storage",
        "002b1e8f",
        null,
        "string"
      ]
    ],
    [
      "0062b860",
      "PARAM",
      [
        "storage",
        "002b38bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062b798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md#insn-0062b798) · [`0062b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md#insn-0062b7b4) · [`0062b748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md#insn-0062b748)
- 新版 `0062b7d8`（命令位置の公開資料なし） · `0062b7f4`（命令位置の公開資料なし） · `0062b788`（命令位置の公開資料なし）

~~~diff
- 0062b798 ["INT_ADD", "register:40f0:8", ["const:62b798:8", "const:4:8"]]
- 0062b798 ["CALL", null, ["ram:48ccb8:8"]]
+ 0062b7d8 ["INT_ADD", "register:40f0:8", ["const:62b7d8:8", "const:4:8"]]
+ 0062b7d8 ["CALL", null, ["ram:48ccf8:8"]]
- 0062b798 bytes 4885f997
+ 0062b7d8 bytes 4885f997
- 0062b7b4 ["INT_ADD", "register:40f0:8", ["const:62b7b4:8", "const:4:8"]]
- 0062b7b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0062b7f4 ["INT_ADD", "register:40f0:8", ["const:62b7f4:8", "const:4:8"]]
+ 0062b7f4 ["CALL", null, ["callee:00c57f70:8"]]
- 0062b7b4 bytes efb01894
+ 0062b7f4 bytes dfb11894
- 0062b748 ["INT_ADD", "register:40f0:8", ["const:62b748:8", "const:4:8"]]
- 0062b748 ["CALL", null, ["callee:00c57e90:8"]]
+ 0062b788 ["INT_ADD", "register:40f0:8", ["const:62b788:8", "const:4:8"]]
+ 0062b788 ["CALL", null, ["callee:00c57e90:8"]]
- 0062b748 bytes d2b01894
+ 0062b788 bytes c2b11894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a0eee2d6f01c62af8a429ab43ba6f10"></a>

### [`0062bd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bd9c.md) → [`0062bddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062bddc.md) FUN_0062bddc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) · 呼出先 7件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00a83254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83254.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0062e1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062e1a0.md) · 呼出先 7件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md) [`00a8344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a8344c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062be38",
      "incomplete_value": false,
      "site": "0062be40",
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
            "const:ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062bdf8",
      "incomplete_value": false,
      "site": "0062be00",
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
            "const:6e:8"
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
      "definition_site": "0062befc",
      "incomplete_value": false,
      "site": "0062bf04",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062bebc",
      "incomplete_value": false,
      "site": "0062bec4",
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
            "const:9e8:8"
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
      "0062be38",
      "PARAM",
      [
        "storage",
        "002b506e",
        null,
        "string"
      ]
    ],
    [
      "0062beac",
      "PARAM",
      [
        "storage",
        "002bdb5e",
        null,
        "string"
      ]
    ],
    [
      "0062beb4",
      "PARAM",
      [
        "storage",
        "002b2d3c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0062be38",
      "PARAM",
      [
        "storage",
        "002b50ae",
        null,
        "string"
      ]
    ],
    [
      "0062beac",
      "PARAM",
      [
        "storage",
        "002bdb9e",
        null,
        "string"
      ]
    ],
    [
      "0062beb4",
      "PARAM",
      [
        "storage",
        "002b2d7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bd9c.md#insn-0062be00) · [`0062be84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bd9c.md#insn-0062be84) · [`0062bec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bd9c.md#insn-0062bec4)
- 新版 `0062be40`（命令位置の公開資料なし） · `0062bec4`（命令位置の公開資料なし） · `0062bf04`（命令位置の公開資料なし）

~~~diff
- 0062be00 ["INT_ADD", "register:40f0:8", ["const:62be00:8", "const:4:8"]]
- 0062be00 ["CALL", null, ["callee:00c58190:8"]]
+ 0062be40 ["INT_ADD", "register:40f0:8", ["const:62be40:8", "const:4:8"]]
+ 0062be40 ["CALL", null, ["callee:00c58190:8"]]
- 0062be00 bytes e4af1894
+ 0062be40 bytes d4b01894
- 0062be84 ["INT_ADD", "register:40f0:8", ["const:62be84:8", "const:4:8"]]
- 0062be84 ["CALL", null, ["callee:00c58190:8"]]
+ 0062bec4 ["INT_ADD", "register:40f0:8", ["const:62bec4:8", "const:4:8"]]
+ 0062bec4 ["CALL", null, ["callee:00c58190:8"]]
- 0062be84 bytes c3af1894
+ 0062bec4 bytes b3b01894
- 0062bec4 ["INT_ADD", "register:40f0:8", ["const:62bec4:8", "const:4:8"]]
- 0062bec4 ["CALL", null, ["callee:00c58190:8"]]
+ 0062bf04 ["INT_ADD", "register:40f0:8", ["const:62bf04:8", "const:4:8"]]
+ 0062bf04 ["CALL", null, ["callee:00c58190:8"]]
- 0062bec4 bytes b3af1894
+ 0062bf04 bytes a3b01894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f5fb8ba7f7a8f710a8f7177bdff1d2b"></a>

### [`0062d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md) → [`0062d600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062d/0062d600.md) FUN_0062d600

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`0062e1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062e1a0.md) · 呼出先 24件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062d644",
      "incomplete_value": false,
      "site": "0062d650",
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
      "definition_site": "0062d604",
      "incomplete_value": false,
      "site": "0062d610",
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
      "definition_site": "0062ddc8",
      "incomplete_value": true,
      "site": "0062ddcc",
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
      "definition_site": "0062dd88",
      "incomplete_value": true,
      "site": "0062dd8c",
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
    "ordinal": 128,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062db60",
      "incomplete_value": false,
      "site": "0062db64",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062db20",
      "incomplete_value": false,
      "site": "0062db24",
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
            "const:20d:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062d650",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0062d658",
      "READ",
      [
        "storage",
        "002c1341",
        null,
        "string"
      ]
    ],
    [
      "0062db60",
      "PARAM",
      [
        "storage",
        "002a020d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0062d650",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0062d658",
      "READ",
      [
        "storage",
        "002c1381",
        null,
        "string"
      ]
    ],
    [
      "0062db60",
      "PARAM",
      [
        "storage",
        "002a02da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062d650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md#insn-0062d650) · [`0062db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md#insn-0062db24) · [`0062d5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md#insn-0062d5fc)
- 新版 `0062d690`（命令位置の公開資料なし） · `0062db64`（命令位置の公開資料なし） · `0062d63c`（命令位置の公開資料なし）

~~~diff
- 0062d650 ["INT_ADD", "register:40f0:8", ["const:62d650:8", "const:4:8"]]
- 0062d650 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0062d690 ["INT_ADD", "register:40f0:8", ["const:62d690:8", "const:4:8"]]
+ 0062d690 ["CALL", null, ["callee:00c57eb0:8"]]
- 0062d650 bytes 18a91894
+ 0062d690 bytes 08aa1894
- 0062db24 ["INT_ADD", "register:40f0:8", ["const:62db24:8", "const:4:8"]]
- 0062db24 ["CALL", null, ["callee:00c57f60:8"]]
+ 0062db64 ["INT_ADD", "register:40f0:8", ["const:62db64:8", "const:4:8"]]
+ 0062db64 ["CALL", null, ["callee:00c57f60:8"]]
- 0062db24 bytes 0fa81894
+ 0062db64 bytes ffa81894
- 0062d5fc ["INT_ADD", "register:40f0:8", ["const:62d5fc:8", "const:4:8"]]
- 0062d5fc ["CALL", null, ["callee:00487e20:8"]]
+ 0062d63c ["INT_ADD", "register:40f0:8", ["const:62d63c:8", "const:4:8"]]
+ 0062d63c ["CALL", null, ["callee:00487e20:8"]]
- 0062d5fc bytes f969f997
+ 0062d63c bytes f969f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b564b647e040f982e6285679ffbe0d60"></a>

### [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) → [`0062e1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062e1a0.md) FUN_0062e1a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00629b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b48.md) [`00629ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ca8.md) · 呼出先 25件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`0062b034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b034.md)
- 新版 呼出元 2件 [`00629b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629b88.md) [`00629ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629ce8.md) · 呼出先 25件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`0062b074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b074.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062e9c4",
      "incomplete_value": true,
      "site": "0062e9c4",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062e984",
      "incomplete_value": true,
      "site": "0062e984",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "ordinal": 98,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062eaf0",
      "incomplete_value": false,
      "site": "0062eaf8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062eab0",
      "incomplete_value": false,
      "site": "0062eab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 107,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062e1e4",
      "DATA",
      [
        "storage",
        "003c7884",
        "fde_003c7884",
        "dword"
      ]
    ],
    [
      "0062e1f8",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "0062e20c",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "0062e1e4",
      "DATA",
      [
        "storage",
        "003c7884",
        null,
        "dword"
      ]
    ],
    [
      "0062e1f8",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "0062e20c",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062e194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md#insn-0062e194) · [`0062e198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md#insn-0062e198) · [`0062e1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md#insn-0062e1a8)
- 新版 `0062e1d4`（命令位置の公開資料なし） · `0062e1d8`（命令位置の公開資料なし） · `0062e1e8`（命令位置の公開資料なし）

~~~diff
- 0062e194 ["INT_ADD", "register:40f0:8", ["const:62e194:8", "const:4:8"]]
- 0062e194 ["CALL", null, ["callee:0062d600:8"]]
+ 0062e1d4 ["INT_ADD", "register:40f0:8", ["const:62e1d4:8", "const:4:8"]]
+ 0062e1d4 ["CALL", null, ["callee:0062d600:8"]]
- 0062e194 bytes 0bfdff97
+ 0062e1d4 bytes 0bfdff97
- 0062e198 ["INT_ADD", "register:40f0:8", ["const:62e198:8", "const:4:8"]]
- 0062e198 ["CALL", null, ["callee:008514f8:8"]]
+ 0062e1d8 ["INT_ADD", "register:40f0:8", ["const:62e1d8:8", "const:4:8"]]
+ 0062e1d8 ["CALL", null, ["callee:008514f8:8"]]
- 0062e198 bytes c88c0894
+ 0062e1d8 bytes c88c0894
- 0062e1a8 ["INT_ADD", "register:40f0:8", ["const:62e1a8:8", "const:4:8"]]
- 0062e1a8 ["CALL", null, ["callee:008514f8:8"]]
+ 0062e1e8 ["INT_ADD", "register:40f0:8", ["const:62e1e8:8", "const:4:8"]]
+ 0062e1e8 ["CALL", null, ["callee:008514f8:8"]]
- 0062e1a8 bytes c48c0894
+ 0062e1e8 bytes c48c0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa5ba75bbf1d00a5e6c21f7c57cda838"></a>

### [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) → [`0062ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062ecfc.md) FUN_0062ecfc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00629ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ca8.md) · 呼出先 23件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0044b148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b148.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`00629ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629ce8.md) · 呼出先 23件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044b188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b188.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062ed94",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062ed54",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062ee54",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062ee14",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0062eecc",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062ee8c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062ed40",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "0062ed58",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "0062ed60",
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
      "0062ed40",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "0062ed58",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "0062ed60",
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

- 旧版 [`0062ed54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md#insn-0062ed54) · [`0062ee14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md#insn-0062ee14) · [`0062ee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md#insn-0062ee8c)
- 新版 `0062ed94`（命令位置の公開資料なし） · `0062ee54`（命令位置の公開資料なし） · `0062eecc`（命令位置の公開資料なし）

~~~diff
- 0062ed54 ["INT_ADD", "register:40f0:8", ["const:62ed54:8", "const:4:8"]]
- 0062ed54 ["CALL", null, ["ram:48ccb8:8"]]
+ 0062ed94 ["INT_ADD", "register:40f0:8", ["const:62ed94:8", "const:4:8"]]
+ 0062ed94 ["CALL", null, ["ram:48ccf8:8"]]
- 0062ed54 bytes d977f997
+ 0062ed94 bytes d977f997
- 0062ee14 ["INT_ADD", "register:40f0:8", ["const:62ee14:8", "const:4:8"]]
- 0062ee14 ["CALL", null, ["ram:48ccb8:8"]]
+ 0062ee54 ["INT_ADD", "register:40f0:8", ["const:62ee54:8", "const:4:8"]]
+ 0062ee54 ["CALL", null, ["ram:48ccf8:8"]]
- 0062ee14 bytes a977f997
+ 0062ee54 bytes a977f997
- 0062ee8c ["INT_ADD", "register:40f0:8", ["const:62ee8c:8", "const:4:8"]]
- 0062ee8c ["CALL", null, ["ram:48ccb8:8"]]
+ 0062eecc ["INT_ADD", "register:40f0:8", ["const:62eecc:8", "const:4:8"]]
+ 0062eecc ["CALL", null, ["ram:48ccf8:8"]]
- 0062ee8c bytes 8b77f997
+ 0062eecc bytes 8b77f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f20b820b7388ac371bdfac76b13038"></a>

### [`0062f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f240.md) → [`0062f280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062f280.md) FUN_0062f280

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046b4c8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.97% / 新版 97.97%

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
      "site": "0062f2bc",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062f27c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "0062f3e4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062f3a4",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062f48c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062f44c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 35,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062f2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0062f3a8",
      "READ",
      [
        "storage",
        "00c9b108",
        null,
        "pointer"
      ]
    ],
    [
      "0062f3ac",
      "DATA",
      [
        "storage",
        "00ca3d20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0062f2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0062f3a8",
      "READ",
      [
        "storage",
        "00c9b508",
        null,
        "pointer"
      ]
    ],
    [
      "0062f3ac",
      "DATA",
      [
        "storage",
        "00ca4120",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062f27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f240.md#insn-0062f27c) · [`0062f3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f240.md#insn-0062f3a4) · [`0062f44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f240.md#insn-0062f44c)
- 新版 `0062f2bc`（命令位置の公開資料なし） · `0062f3e4`（命令位置の公開資料なし） · `0062f48c`（命令位置の公開資料なし）

~~~diff
- 0062f27c ["INT_ADD", "register:40f0:8", ["const:62f27c:8", "const:4:8"]]
- 0062f27c ["CALL", null, ["ram:46c984:8"]]
+ 0062f2bc ["INT_ADD", "register:40f0:8", ["const:62f2bc:8", "const:4:8"]]
+ 0062f2bc ["CALL", null, ["ram:46c9c4:8"]]
- 0062f27c bytes c2f5f897
+ 0062f2bc bytes c2f5f897
- 0062f3a4 ["INT_ADD", "register:40f0:8", ["const:62f3a4:8", "const:4:8"]]
- 0062f3a4 ["CALL", null, ["ram:46c984:8"]]
+ 0062f3e4 ["INT_ADD", "register:40f0:8", ["const:62f3e4:8", "const:4:8"]]
+ 0062f3e4 ["CALL", null, ["ram:46c9c4:8"]]
- 0062f3a4 bytes 78f5f897
+ 0062f3e4 bytes 78f5f897
- 0062f44c ["INT_ADD", "register:40f0:8", ["const:62f44c:8", "const:4:8"]]
- 0062f44c ["CALL", null, ["ram:46c984:8"]]
+ 0062f48c ["INT_ADD", "register:40f0:8", ["const:62f48c:8", "const:4:8"]]
+ 0062f48c ["CALL", null, ["ram:46c9c4:8"]]
- 0062f44c bytes 4ef5f897
+ 0062f48c bytes 4ef5f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c9ce1ec2b73fc73e33ffa0926379d6"></a>

### [`0062f7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md) → [`0062f7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062f7e4.md) FUN_0062f7e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 1件 [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) · 呼出先 8件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

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
      "site": "0062f89c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0062f85c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062f83c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "0062f868",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "0062f89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0062f83c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "0062f868",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "0062f89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0062f85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md#insn-0062f85c) · [`0062f7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md#insn-0062f7b4) · [`0062f7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062f7a4.md#insn-0062f7c4)
- 新版 `0062f89c`（命令位置の公開資料なし） · `0062f7f4`（命令位置の公開資料なし） · `0062f804`（命令位置の公開資料なし）

~~~diff
- 0062f85c ["INT_ADD", "register:40f0:8", ["const:62f85c:8", "const:4:8"]]
- 0062f85c ["CALL", null, ["ram:46c984:8"]]
+ 0062f89c ["INT_ADD", "register:40f0:8", ["const:62f89c:8", "const:4:8"]]
+ 0062f89c ["CALL", null, ["ram:46c9c4:8"]]
- 0062f85c bytes 4af4f897
+ 0062f89c bytes 4af4f897
- 0062f7b4 ["INT_ADD", "register:40f0:8", ["const:62f7b4:8", "const:4:8"]]
- 0062f7b4 ["CALL", null, ["callee:008514f8:8"]]
+ 0062f7f4 ["INT_ADD", "register:40f0:8", ["const:62f7f4:8", "const:4:8"]]
+ 0062f7f4 ["CALL", null, ["callee:008514f8:8"]]
- 0062f7b4 bytes 41870894
+ 0062f7f4 bytes 41870894
- 0062f7c4 ["INT_ADD", "register:40f0:8", ["const:62f7c4:8", "const:4:8"]]
- 0062f7c4 ["CALL", null, ["callee:008b79c8:8"]]
+ 0062f804 ["INT_ADD", "register:40f0:8", ["const:62f804:8", "const:4:8"]]
+ 0062f804 ["CALL", null, ["callee:008b79c8:8"]]
- 0062f7c4 bytes 70200a94
+ 0062f804 bytes 71200a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-808fc50669408e48ab04d16e17c5fe08"></a>

### [`0062fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md) → [`0062fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062fa58.md) FUN_0062fa58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0062a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a7f4.md) [`0062fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`008b015c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b015c.md) [`009aebe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009aebe4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 5件 [`0062a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a834.md) [`0062fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062fa58.md) [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) [`008b01a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b01a0.md) [`009aed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009aed80.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062fbdc",
      "incomplete_value": false,
      "site": "0062fbe8",
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
      "definition_site": "0062fb9c",
      "incomplete_value": false,
      "site": "0062fba8",
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
      "definition_site": "0062fd10",
      "incomplete_value": false,
      "site": "0062fd18",
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
      "definition_site": "0062fcd0",
      "incomplete_value": false,
      "site": "0062fcd8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062fd28",
      "incomplete_value": true,
      "site": "0062fd34",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062fce8",
      "incomplete_value": true,
      "site": "0062fcf4",
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
            "const:ea9:8"
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
      "0062fbb8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0062fbdc",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0062fd10",
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
      "0062fbb8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0062fbdc",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0062fd10",
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

- 旧版 [`0062fba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md#insn-0062fba8) · [`0062fcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md#insn-0062fcd8) · [`0062fcf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md#insn-0062fcf4)
- 新版 `0062fbe8`（命令位置の公開資料なし） · `0062fd18`（命令位置の公開資料なし） · `0062fd34`（命令位置の公開資料なし）

~~~diff
- 0062fba8 ["INT_ADD", "register:40f0:8", ["const:62fba8:8", "const:4:8"]]
- 0062fba8 ["CALL", null, ["callee:004427f4:8"]]
+ 0062fbe8 ["INT_ADD", "register:40f0:8", ["const:62fbe8:8", "const:4:8"]]
+ 0062fbe8 ["CALL", null, ["callee:004427f4:8"]]
- 0062fba8 bytes 034bf897
+ 0062fbe8 bytes 034bf897
- 0062fcd8 ["INT_ADD", "register:40f0:8", ["const:62fcd8:8", "const:4:8"]]
- 0062fcd8 ["CALL", null, ["callee:00441e94:8"]]
+ 0062fd18 ["INT_ADD", "register:40f0:8", ["const:62fd18:8", "const:4:8"]]
+ 0062fd18 ["CALL", null, ["callee:00441e94:8"]]
- 0062fcd8 bytes 5f48f897
+ 0062fd18 bytes 5f48f897
- 0062fcf4 ["INT_ADD", "register:40f0:8", ["const:62fcf4:8", "const:4:8"]]
- 0062fcf4 ["CALL", null, ["callee:004427f4:8"]]
+ 0062fd34 ["INT_ADD", "register:40f0:8", ["const:62fd34:8", "const:4:8"]]
+ 0062fd34 ["CALL", null, ["callee:004427f4:8"]]
- 0062fcf4 bytes b04af897
+ 0062fd34 bytes b04af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d621d5748cf3345c5fc2cf25327c9c"></a>

### [`00630244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md) → [`00630284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630284.md) FUN_00630284

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0062fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062f/0062fa18.md) [`00630244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 7件 [`0062fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062f/0062fa58.md) [`00630284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630284.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006303e0",
      "incomplete_value": true,
      "site": "006303e8",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006303a0",
      "incomplete_value": true,
      "site": "006303a8",
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
      "definition_site": "00630550",
      "incomplete_value": true,
      "site": "0063055c",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630510",
      "incomplete_value": true,
      "site": "0063051c",
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
            "const:ea9:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006305e0",
      "incomplete_value": false,
      "site": "006305ec",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006305a0",
      "incomplete_value": false,
      "site": "006305ac",
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
            "const:30f:8"
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
      "006303e0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00630404",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00630538",
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
      "006303e0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00630404",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00630538",
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

- 旧版 [`006303a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md#insn-006303a8) · [`0063051c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md#insn-0063051c) · [`006305ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md#insn-006305ac)
- 新版 `006303e8`（命令位置の公開資料なし） · `0063055c`（命令位置の公開資料なし） · `006305ec`（命令位置の公開資料なし）

~~~diff
- 006303a8 ["INT_ADD", "register:40f0:8", ["const:6303a8:8", "const:4:8"]]
- 006303a8 ["CALL", null, ["callee:00441e94:8"]]
+ 006303e8 ["INT_ADD", "register:40f0:8", ["const:6303e8:8", "const:4:8"]]
+ 006303e8 ["CALL", null, ["callee:00441e94:8"]]
- 006303a8 bytes ab46f897
+ 006303e8 bytes ab46f897
- 0063051c ["INT_ADD", "register:40f0:8", ["const:63051c:8", "const:4:8"]]
- 0063051c ["CALL", null, ["callee:004427f4:8"]]
+ 0063055c ["INT_ADD", "register:40f0:8", ["const:63055c:8", "const:4:8"]]
+ 0063055c ["CALL", null, ["callee:004427f4:8"]]
- 0063051c bytes a648f897
+ 0063055c bytes a648f897
- 006305ac ["INT_ADD", "register:40f0:8", ["const:6305ac:8", "const:4:8"]]
- 006305ac ["CALL", null, ["callee:00441cec:8"]]
+ 006305ec ["INT_ADD", "register:40f0:8", ["const:6305ec:8", "const:4:8"]]
+ 006305ec ["CALL", null, ["callee:00441cec:8"]]
- 006305ac bytes c045f897
+ 006305ec bytes c045f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e00c4b8e3f1ef6864615f730a850802"></a>

### [`00630a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a60.md) → [`00630aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630aa0.md) FUN_00630aa0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630ab4",
      "incomplete_value": false,
      "site": "00630ab8",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630a74",
      "incomplete_value": false,
      "site": "00630a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00630ab8",
      "DATA",
      [
        "storage",
        "00c72df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630ab8",
      "DATA",
      [
        "storage",
        "00c731f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a60.md#insn-00630a6c) · [`00630a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a60.md#insn-00630a70) · [`00630a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a60.md#insn-00630a74)
- 新版 `00630aac`（命令位置の公開資料なし） · `00630ab0`（命令位置の公開資料なし） · `00630ab4`（命令位置の公開資料なし）

~~~diff
- 00630a6c ["INT_ADD", "register:40f0:8", ["const:630a6c:8", "const:4:8"]]
- 00630a6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00630aac ["INT_ADD", "register:40f0:8", ["const:630aac:8", "const:4:8"]]
+ 00630aac ["CALL", null, ["callee:00c57e90:8"]]
- 00630a6c bytes 099c1894
+ 00630aac bytes f99c1894
- 00630a70 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630ab0 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630a70 bytes 083200d0
+ 00630ab0 bytes 083200f0
- 00630a74 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00630a74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630a74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630a74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630ab4 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00630ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630a74 bytes 08e13791
+ 00630ab4 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caec717792c882822105a220fd340cbb"></a>

### [`00630a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a84.md) → [`00630ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630ac4.md) FUN_00630ac4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630ac8",
      "incomplete_value": false,
      "site": "00630acc",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630a88",
      "incomplete_value": false,
      "site": "00630a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00630acc",
      "DATA",
      [
        "storage",
        "00c72df8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630acc",
      "DATA",
      [
        "storage",
        "00c731f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a84.md#insn-00630a84) · [`00630a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a84.md#insn-00630a88)
- 新版 `00630ac4`（命令位置の公開資料なし） · `00630ac8`（命令位置の公開資料なし）

~~~diff
- 00630a84 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630ac4 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630a84 bytes 083200d0
+ 00630ac4 bytes 083200f0
- 00630a88 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00630a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630ac8 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00630ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630a88 bytes 08e13791
+ 00630ac8 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a74558d3e3aa9a70b0e625597d16ee76"></a>

### [`00630a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a9c.md) → [`00630adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630adc.md) FUN_00630adc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0062b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) [`0062d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0f4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0062b714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b714.md) [`0062d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062d/0062d134.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

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
      "site": "00630b04",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630ac4",
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
      "site": "00630b10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630ad0",
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
      "00630b04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00630b10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00630b04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00630b10",
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

- 旧版 [`00630ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a9c.md#insn-00630ac4) · [`00630ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a9c.md#insn-00630ad0) · [`00630b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a9c.md#insn-00630b04)
- 新版 `00630b04`（命令位置の公開資料なし） · `00630b10`（命令位置の公開資料なし） · `00630b44`（命令位置の公開資料なし）

~~~diff
- 00630ac4 ["INT_ADD", "register:40f0:8", ["const:630ac4:8", "const:4:8"]]
- 00630ac4 ["CALL", null, ["ram:47acb4:8"]]
+ 00630b04 ["INT_ADD", "register:40f0:8", ["const:630b04:8", "const:4:8"]]
+ 00630b04 ["CALL", null, ["ram:47acf4:8"]]
- 00630ac4 bytes 7c28f997
+ 00630b04 bytes 7c28f997
- 00630ad0 ["INT_ADD", "register:40f0:8", ["const:630ad0:8", "const:4:8"]]
- 00630ad0 ["CALL", null, ["ram:47acb4:8"]]
+ 00630b10 ["INT_ADD", "register:40f0:8", ["const:630b10:8", "const:4:8"]]
+ 00630b10 ["CALL", null, ["ram:47acf4:8"]]
- 00630ad0 bytes 7928f997
+ 00630b10 bytes 7928f997
- 00630b04 ["INT_ADD", "register:40f0:8", ["const:630b04:8", "const:4:8"]]
- 00630b04 ["CALL", null, ["callee:008514f8:8"]]
+ 00630b44 ["INT_ADD", "register:40f0:8", ["const:630b44:8", "const:4:8"]]
+ 00630b44 ["CALL", null, ["callee:008514f8:8"]]
- 00630b04 bytes 6d820894
+ 00630b44 bytes 6d820894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-945462e7704209f9133813712c426adf"></a>

### [`00630be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630be0.md) → [`00630c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630c20.md) FUN_00630c20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630c34",
      "incomplete_value": false,
      "site": "00630c38",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630bf4",
      "incomplete_value": false,
      "site": "00630bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "00630c38",
      "DATA",
      [
        "storage",
        "00c72e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630c38",
      "DATA",
      [
        "storage",
        "00c73278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630be0.md#insn-00630bec) · [`00630bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630be0.md#insn-00630bf0) · [`00630bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630be0.md#insn-00630bf4)
- 新版 `00630c2c`（命令位置の公開資料なし） · `00630c30`（命令位置の公開資料なし） · `00630c34`（命令位置の公開資料なし）

~~~diff
- 00630bec ["INT_ADD", "register:40f0:8", ["const:630bec:8", "const:4:8"]]
- 00630bec ["CALL", null, ["callee:00c57e90:8"]]
+ 00630c2c ["INT_ADD", "register:40f0:8", ["const:630c2c:8", "const:4:8"]]
+ 00630c2c ["CALL", null, ["callee:00c57e90:8"]]
- 00630bec bytes a99b1894
+ 00630c2c bytes 999c1894
- 00630bf0 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630c30 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630bf0 bytes 083200d0
+ 00630c30 bytes 083200f0
- 00630bf4 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00630bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630c34 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00630c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630bf4 bytes 08e13991
+ 00630c34 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-520f10a76d9a15f5a3ce95d1281a0f02"></a>

### [`00630c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c04.md) → [`00630c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630c44.md) FUN_00630c44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630c48",
      "incomplete_value": false,
      "site": "00630c4c",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630c08",
      "incomplete_value": false,
      "site": "00630c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "00630c4c",
      "DATA",
      [
        "storage",
        "00c72e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630c4c",
      "DATA",
      [
        "storage",
        "00c73278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c04.md#insn-00630c04) · [`00630c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c04.md#insn-00630c08)
- 新版 `00630c44`（命令位置の公開資料なし） · `00630c48`（命令位置の公開資料なし）

~~~diff
- 00630c04 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630c44 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630c04 bytes 083200d0
+ 00630c44 bytes 083200f0
- 00630c08 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00630c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630c48 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00630c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630c08 bytes 08e13991
+ 00630c48 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d40242a0025e77741fa849123a6c94"></a>

### [`00630c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c1c.md) → [`00630c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630c5c.md) FUN_00630c5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0062d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0f4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0062d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062d/0062d134.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "site": "00630cfc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630cbc",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630d08",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630cc8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00630cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00630d08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00630cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00630d08",
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

- 旧版 [`00630c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c1c.md#insn-00630c7c) · [`00630cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c1c.md#insn-00630cbc) · [`00630cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630c1c.md#insn-00630cc8)
- 新版 `00630cbc`（命令位置の公開資料なし） · `00630cfc`（命令位置の公開資料なし） · `00630d08`（命令位置の公開資料なし）

~~~diff
- 00630c7c ["INT_ADD", "register:40f0:8", ["const:630c7c:8", "const:4:8"]]
- 00630c7c ["CALL", null, ["callee:00a46bb8:8"]]
+ 00630cbc ["INT_ADD", "register:40f0:8", ["const:630cbc:8", "const:4:8"]]
+ 00630cbc ["CALL", null, ["callee:00a46bb8:8"]]
- 00630c7c bytes 51571094
+ 00630cbc bytes bf571094
- 00630cbc ["INT_ADD", "register:40f0:8", ["const:630cbc:8", "const:4:8"]]
- 00630cbc ["CALL", null, ["ram:47acb4:8"]]
+ 00630cfc ["INT_ADD", "register:40f0:8", ["const:630cfc:8", "const:4:8"]]
+ 00630cfc ["CALL", null, ["ram:47acf4:8"]]
- 00630cbc bytes fe27f997
+ 00630cfc bytes fe27f997
- 00630cc8 ["INT_ADD", "register:40f0:8", ["const:630cc8:8", "const:4:8"]]
- 00630cc8 ["CALL", null, ["ram:47acb4:8"]]
+ 00630d08 ["INT_ADD", "register:40f0:8", ["const:630d08:8", "const:4:8"]]
+ 00630d08 ["CALL", null, ["ram:47acf4:8"]]
- 00630cc8 bytes fb27f997
+ 00630d08 bytes fb27f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70e2b9879c45f880179b2927e2d42640"></a>

### [`00630d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d78.md) → [`00630db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630db8.md) FUN_00630db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630dcc",
      "incomplete_value": false,
      "site": "00630dd0",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630d8c",
      "incomplete_value": false,
      "site": "00630d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00630dd0",
      "DATA",
      [
        "storage",
        "00c72ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630dd0",
      "DATA",
      [
        "storage",
        "00c732f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d78.md#insn-00630d84) · [`00630d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d78.md#insn-00630d88) · [`00630d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d78.md#insn-00630d8c)
- 新版 `00630dc4`（命令位置の公開資料なし） · `00630dc8`（命令位置の公開資料なし） · `00630dcc`（命令位置の公開資料なし）

~~~diff
- 00630d84 ["INT_ADD", "register:40f0:8", ["const:630d84:8", "const:4:8"]]
- 00630d84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00630dc4 ["INT_ADD", "register:40f0:8", ["const:630dc4:8", "const:4:8"]]
+ 00630dc4 ["CALL", null, ["callee:00c57e90:8"]]
- 00630d84 bytes 439b1894
+ 00630dc4 bytes 339c1894
- 00630d88 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630dc8 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630d88 bytes 083200d0
+ 00630dc8 bytes 083200f0
- 00630d8c ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00630d8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630d8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630d8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630dcc ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 00630dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630d8c bytes 08e13b91
+ 00630dcc bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0722fe868e3e46cf47238b5764cbe8f7"></a>

### [`00630d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d9c.md) → [`00630ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630ddc.md) FUN_00630ddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00630de0",
      "incomplete_value": false,
      "site": "00630de4",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630da0",
      "incomplete_value": false,
      "site": "00630da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "00630de4",
      "DATA",
      [
        "storage",
        "00c72ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630de4",
      "DATA",
      [
        "storage",
        "00c732f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00630d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d9c.md#insn-00630d9c) · [`00630da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d9c.md#insn-00630da0)
- 新版 `00630ddc`（命令位置の公開資料なし） · `00630de0`（命令位置の公開資料なし）

~~~diff
- 00630d9c ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00630ddc ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00630d9c bytes 083200d0
+ 00630ddc bytes 083200f0
- 00630da0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00630da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00630da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00630da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00630de0 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 00630de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00630de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00630de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00630da0 bytes 08e13b91
+ 00630de0 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65fc15d81b89cbdb57d6a3290f78dbaa"></a>

### [`00630db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630db4.md) → [`00630df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630df4.md) FUN_00630df4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0062d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0f4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0062d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062d/0062d134.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00630e14",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630dd4",
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
      "site": "00630e20",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00630de0",
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
      "00630e14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00630e20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00630e44",
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
      "00630e14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00630e20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00630e44",
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

- 旧版 [`00630dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630db4.md#insn-00630dd4) · [`00630de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630db4.md#insn-00630de0) · [`00630df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630db4.md#insn-00630df4)
- 新版 `00630e14`（命令位置の公開資料なし） · `00630e20`（命令位置の公開資料なし） · `00630e34`（命令位置の公開資料なし）

~~~diff
- 00630dd4 ["INT_ADD", "register:40f0:8", ["const:630dd4:8", "const:4:8"]]
- 00630dd4 ["CALL", null, ["ram:47acb4:8"]]
+ 00630e14 ["INT_ADD", "register:40f0:8", ["const:630e14:8", "const:4:8"]]
+ 00630e14 ["CALL", null, ["ram:47acf4:8"]]
- 00630dd4 bytes b827f997
+ 00630e14 bytes b827f997
- 00630de0 ["INT_ADD", "register:40f0:8", ["const:630de0:8", "const:4:8"]]
- 00630de0 ["CALL", null, ["ram:47acb4:8"]]
+ 00630e20 ["INT_ADD", "register:40f0:8", ["const:630e20:8", "const:4:8"]]
+ 00630e20 ["CALL", null, ["ram:47acf4:8"]]
- 00630de0 bytes b527f997
+ 00630e20 bytes b527f997
- 00630df4 ["INT_ADD", "register:40f0:8", ["const:630df4:8", "const:4:8"]]
- 00630df4 ["CALL", null, ["callee:008514f8:8"]]
+ 00630e34 ["INT_ADD", "register:40f0:8", ["const:630e34:8", "const:4:8"]]
+ 00630e34 ["CALL", null, ["callee:008514f8:8"]]
- 00630df4 bytes b1810894
+ 00630e34 bytes b1810894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f0a709b76439acb76556a83875d169d"></a>

### [`00630e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630e4c.md) → [`00630e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630e8c.md) _INIT_79

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00630ec8",
      "incomplete_value": true,
      "site": "00630ee4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00630e88",
      "incomplete_value": true,
      "site": "00630ea4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00630f2c",
      "incomplete_value": true,
      "site": "00630f44",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "00630eec",
      "incomplete_value": true,
      "site": "00630f04",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "00630f48",
      "incomplete_value": true,
      "site": "00630f64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00630f08",
      "incomplete_value": true,
      "site": "00630f24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00630ec8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00630eec",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00630f0c",
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
      "00630ec8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00630eec",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00630f0c",
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

- 旧版 [`00630ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630e4c.md#insn-00630ec4) · [`00630ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630e4c.md#insn-00630ee4) · [`00631080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630e4c.md#insn-00631080)
- 新版 `00630f04`（命令位置の公開資料なし） · `00630f24`（命令位置の公開資料なし） · `006310c0`（命令位置の公開資料なし）

~~~diff
- 00630ec4 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00630ec4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00630ec4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00630ec4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00630f04 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00630f04 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00630f04 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00630f04 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00630ec4 bytes 4a093691
+ 00630f04 bytes 4a093791
- 00630ee4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00630ee4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00630ee4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00630ee4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00630f24 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00630f24 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00630f24 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00630f24 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00630ee4 bytes 4a553a91
+ 00630f24 bytes 4a893d91
- 00631080 ["INT_ADD", "register:40f0:8", ["const:631080:8", "const:4:8"]]
- 00631080 ["CALL", null, ["callee:00c57e30:8"]]
+ 006310c0 ["INT_ADD", "register:40f0:8", ["const:6310c0:8", "const:4:8"]]
+ 006310c0 ["CALL", null, ["callee:00c57e30:8"]]
- 00631080 bytes 6c9a1894
+ 006310c0 bytes 5c9b1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2a338fcd35568367f696d4dc65d15e"></a>

### [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) → [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) FUN_006312f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00633c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md) · 呼出先 45件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md)
- 新版 呼出元 1件 [`00633c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633c8c.md) · 呼出先 45件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.90% / 新版 89.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `call_target` 2件, `store_destination` 37件, `store_value` 25件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006319b8",
      "incomplete_value": false,
      "site": "006319b8",
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
      "definition_site": "00631978",
      "incomplete_value": false,
      "site": "00631978",
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
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006319bc",
      "incomplete_value": false,
      "site": "006319bc",
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
      "definition_site": "0063197c",
      "incomplete_value": false,
      "site": "0063197c",
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
    "ordinal": 42,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006319b8",
      "incomplete_value": false,
      "site": "006319bc",
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
      "definition_site": "00631978",
      "incomplete_value": false,
      "site": "0063197c",
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
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00631604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0063162c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00631654",
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
      "00631604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0063162c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00631654",
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

- 旧版 [`00631990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md#insn-00631990) · [`0063199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md#insn-0063199c) · [`006319b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md#insn-006319b8)
- 新版 `006319d0`（命令位置の公開資料なし） · `006319dc`（命令位置の公開資料なし） · `006319f8`（命令位置の公開資料なし）

~~~diff
- 00631990 ["INT_ADD", "register:40f0:8", ["const:631990:8", "const:4:8"]]
- 00631990 ["CALL", null, ["callee:00c57e30:8"]]
+ 006319d0 ["INT_ADD", "register:40f0:8", ["const:6319d0:8", "const:4:8"]]
+ 006319d0 ["CALL", null, ["callee:00c57e30:8"]]
- 00631990 bytes 28981894
+ 006319d0 bytes 18991894
- 0063199c ["INT_ADD", "register:40f0:8", ["const:63199c:8", "const:4:8"]]
- 0063199c ["CALL", null, ["callee:00c57e70:8"]]
+ 006319dc ["INT_ADD", "register:40f0:8", ["const:6319dc:8", "const:4:8"]]
+ 006319dc ["CALL", null, ["callee:00c57e70:8"]]
- 0063199c bytes 35981894
+ 006319dc bytes 25991894
- 006319b8 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 006319b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006319b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006319b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006319f8 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 006319f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006319f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006319f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006319b8 bytes 21002c91
+ 006319f8 bytes 21003c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b61c14b748411111602d3e3763c78a"></a>

### [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) → [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) FUN_00632d14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00633c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md) [`00634a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md) · 呼出先 15件 [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md)
- 新版 呼出元 2件 [`00633c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633c8c.md) [`00634a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00634/00634a64.md) · 呼出先 15件 [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.50% / 新版 90.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 8件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00632eb4",
      "incomplete_value": true,
      "site": "00632ecc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00632e74",
      "incomplete_value": true,
      "site": "00632e8c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:1:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "006331b0",
      "incomplete_value": true,
      "site": "006331b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:e64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633170",
      "incomplete_value": true,
      "site": "00633170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:a64:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00633228",
      "incomplete_value": false,
      "site": "00633228",
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
      "definition_site": "006331e8",
      "incomplete_value": false,
      "site": "006331e8",
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
      "00632d54",
      "READ",
      [
        "storage",
        "00ca3a64",
        null,
        "undefined4"
      ]
    ],
    [
      "00632dcc",
      "READ",
      [
        "storage",
        "00ca3a64",
        null,
        "undefined4"
      ]
    ],
    [
      "00632e34",
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
      "00632d54",
      "READ",
      [
        "storage",
        "00ca3e64",
        null,
        "undefined4"
      ]
    ],
    [
      "00632dcc",
      "READ",
      [
        "storage",
        "00ca3e64",
        null,
        "undefined4"
      ]
    ],
    [
      "00632e34",
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

- 旧版 [`00633044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md#insn-00633044) · [`00633084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md#insn-00633084) · [`00633100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md#insn-00633100)
- 新版 `00633084`（命令位置の公開資料なし） · `006330c4`（命令位置の公開資料なし） · `00633140`（命令位置の公開資料なし）

~~~diff
- 00633044 ["INT_ADD", "register:40f0:8", ["const:633044:8", "const:4:8"]]
- 00633044 ["CALL", null, ["callee:006337e4:8"]]
+ 00633084 ["INT_ADD", "register:40f0:8", ["const:633084:8", "const:4:8"]]
+ 00633084 ["CALL", null, ["callee:006337e4:8"]]
- 00633044 bytes d8010094
+ 00633084 bytes d8010094
- 00633084 ["COPY", "register:0:8", ["register:4040:8"]]
- 00633084 ["INT_ADD", "register:40f0:8", ["const:633084:8", "const:4:8"]]
- 00633084 ["CALLIND", null, ["register:0:8"]]
+ 006330c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006330c4 ["INT_ADD", "register:40f0:8", ["const:6330c4:8", "const:4:8"]]
+ 006330c4 ["CALLIND", null, ["register:0:8"]]
- 00633084 bytes 00013fd6
+ 006330c4 bytes 00013fd6
- 00633100 ["INT_ADD", "register:40f0:8", ["const:633100:8", "const:4:8"]]
- 00633100 ["CALL", null, ["callee:00c57e30:8"]]
+ 00633140 ["INT_ADD", "register:40f0:8", ["const:633140:8", "const:4:8"]]
+ 00633140 ["CALL", null, ["callee:00c57e30:8"]]
- 00633100 bytes 4c921894
+ 00633140 bytes 3c931894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159df21e67580c142575578a64cf9975"></a>

### [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) → [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) FUN_00633374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 20件 [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) [`00666be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md) [`0066f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md) [`0067d490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md) · 呼出先 17件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0047eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md) [`0047f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md)
- 新版 呼出元 20件 [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) [`00666320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666320.md) [`00666c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666c28.md) [`0066f838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066f838.md) [`0067d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d4d0.md) · 呼出先 17件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0047ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md) [`0047f14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633440",
      "incomplete_value": false,
      "site": "0063344c",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633400",
      "incomplete_value": false,
      "site": "0063340c",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633540",
      "incomplete_value": false,
      "site": "00633540",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633500",
      "incomplete_value": false,
      "site": "00633500",
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
            "const:8:8"
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
      "0063344c",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "00633540",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ],
    [
      "00633584",
      "READ",
      [
        "storage",
        "00c73030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063344c",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "00633540",
      "DATA",
      [
        "storage",
        "00c73408",
        null,
        "undefined *"
      ]
    ],
    [
      "00633584",
      "READ",
      [
        "storage",
        "00c73430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00633380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md#insn-00633380) · [`0063338c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md#insn-0063338c) · [`006333a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md#insn-006333a0)
- 新版 `006333c0`（命令位置の公開資料なし） · `006333cc`（命令位置の公開資料なし） · `006333e0`（命令位置の公開資料なし）

~~~diff
- 00633380 ["INT_ADD", "register:40f0:8", ["const:633380:8", "const:4:8"]]
- 00633380 ["CALL", null, ["callee:00440f70:8"]]
+ 006333c0 ["INT_ADD", "register:40f0:8", ["const:6333c0:8", "const:4:8"]]
+ 006333c0 ["CALL", null, ["callee:00440f70:8"]]
- 00633380 bytes ec36f897
+ 006333c0 bytes ec36f897
- 0063338c ["INT_ADD", "register:40f0:8", ["const:63338c:8", "const:4:8"]]
- 0063338c ["CALL", null, ["callee:0047ef0c:8"]]
+ 006333cc ["INT_ADD", "register:40f0:8", ["const:6333cc:8", "const:4:8"]]
+ 006333cc ["CALL", null, ["callee:0047ef0c:8"]]
- 0063338c bytes d02ef997
+ 006333cc bytes d02ef997
- 006333a0 ["INT_ADD", "register:40f0:8", ["const:6333a0:8", "const:4:8"]]
- 006333a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006333e0 ["INT_ADD", "register:40f0:8", ["const:6333e0:8", "const:4:8"]]
+ 006333e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 006333a0 bytes c4911894
+ 006333e0 bytes b4921894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dbf53654a4967fb30a6fdf1850bc526"></a>

### [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) → [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) FUN_006337e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) [`0066f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md) [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`008c4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4784.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) [`00489128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md) [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md)
- 新版 呼出元 9件 [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) [`0066f838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066f838.md) [`006b0238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b0/006b0238.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`008c4920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c4/008c4920.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) [`00489168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md) [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633948",
      "incomplete_value": false,
      "site": "00633954",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633908",
      "incomplete_value": false,
      "site": "00633914",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633a50",
      "incomplete_value": false,
      "site": "00633a50",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633a10",
      "incomplete_value": false,
      "site": "00633a10",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00633ad8",
      "incomplete_value": false,
      "site": "00633aec",
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
      "definition_site": "00633a98",
      "incomplete_value": false,
      "site": "00633aac",
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
    "ordinal": 22,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00633954",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "00633a50",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ],
    [
      "00633a94",
      "READ",
      [
        "storage",
        "00c730b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00633954",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "00633a50",
      "DATA",
      [
        "storage",
        "00c73488",
        null,
        "undefined *"
      ]
    ],
    [
      "00633a94",
      "READ",
      [
        "storage",
        "00c734b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00633aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md#insn-00633aac) · [`00633aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md#insn-00633aec) · [`00633818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md#insn-00633818)
- 新版 `00633aec`（命令位置の公開資料なし） · `00633b2c`（命令位置の公開資料なし） · `00633858`（命令位置の公開資料なし）

~~~diff
- 00633aac ["INT_ADD", "register:40f0:8", ["const:633aac:8", "const:4:8"]]
- 00633aac ["CALL", null, ["callee:0047f45c:8"]]
+ 00633aec ["INT_ADD", "register:40f0:8", ["const:633aec:8", "const:4:8"]]
+ 00633aec ["CALL", null, ["callee:0047f45c:8"]]
- 00633aac bytes 5c2ef997
+ 00633aec bytes 5c2ef997
- 00633aec ["INT_ADD", "register:40f0:8", ["const:633aec:8", "const:4:8"]]
- 00633aec ["CALL", null, ["callee:00c57eb0:8"]]
+ 00633b2c ["INT_ADD", "register:40f0:8", ["const:633b2c:8", "const:4:8"]]
+ 00633b2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00633aec bytes f18f1894
+ 00633b2c bytes e1901894
- 00633818 ["INT_ADD", "register:40f0:8", ["const:633818:8", "const:4:8"]]
- 00633818 ["CALL", null, ["callee:0043bb20:8"]]
+ 00633858 ["INT_ADD", "register:40f0:8", ["const:633858:8", "const:4:8"]]
+ 00633858 ["CALL", null, ["callee:0043bb20:8"]]
- 00633818 bytes b220f897
+ 00633858 bytes b220f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc23b9cd703d96149949147ecd4234b7"></a>

### [`00633c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md) → [`00633c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633c8c.md) FUN_00633c8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00629ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ca8.md) · 呼出先 26件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md)
- 新版 呼出元 1件 [`00629ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629ce8.md) · 呼出先 26件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00634728",
      "incomplete_value": false,
      "site": "00634728",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006346e8",
      "incomplete_value": false,
      "site": "006346e8",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "ordinal": 101,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00633ccc",
      "incomplete_value": true,
      "site": "00633ccc",
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
      "definition_site": "00633c8c",
      "incomplete_value": true,
      "site": "00633c8c",
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
      "definition_site": "00633cd4",
      "incomplete_value": false,
      "site": "00633ce8",
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
      "definition_site": "00633c94",
      "incomplete_value": false,
      "site": "00633ca8",
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
      "00633cc4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00633cd4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00633cdc",
      "PARAM",
      [
        "storage",
        "00c730f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00633cc4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00633cd4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00633cdc",
      "PARAM",
      [
        "storage",
        "00c734f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00633ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md#insn-00633ca8) · [`006344dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md#insn-006344dc) · [`00633c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md#insn-00633c84)
- 新版 `00633ce8`（命令位置の公開資料なし） · `0063451c`（命令位置の公開資料なし） · `00633cc4`（命令位置の公開資料なし）

~~~diff
- 00633ca8 ["INT_ADD", "register:40f0:8", ["const:633ca8:8", "const:4:8"]]
- 00633ca8 ["CALL", null, ["callee:00c58610:8"]]
+ 00633ce8 ["INT_ADD", "register:40f0:8", ["const:633ce8:8", "const:4:8"]]
+ 00633ce8 ["CALL", null, ["callee:00c58610:8"]]
- 00633ca8 bytes 5a911894
+ 00633ce8 bytes 4a921894
- 006344dc ["INT_ADD", "register:40f0:8", ["const:6344dc:8", "const:4:8"]]
- 006344dc ["CALL", null, ["ram:46c984:8"]]
+ 0063451c ["INT_ADD", "register:40f0:8", ["const:63451c:8", "const:4:8"]]
+ 0063451c ["CALL", null, ["ram:46c9c4:8"]]
- 006344dc bytes 2ae1f897
+ 0063451c bytes 2ae1f897
- 00633c84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 00633c84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00633cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 00633cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00633c84 bytes 08bd42f9
+ 00633cc4 bytes 08bd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f62fdeadc822fdc9644bdf3305f2b0b"></a>

### [`00634a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md) → [`00634a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00634/00634a64.md) FUN_00634a64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00629ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ca8.md) · 呼出先 18件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00632cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00632/00632cd4.md) [`006368b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368b0.md)
- 新版 呼出元 1件 [`00629ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629ce8.md) · 呼出先 18件 [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00632d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00632/00632d14.md) [`006368f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006368f0.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00634b04",
      "incomplete_value": false,
      "site": "00634b0c",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00634ac4",
      "incomplete_value": false,
      "site": "00634acc",
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
            "const:1a0:8"
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
      "definition_site": "00634b80",
      "incomplete_value": false,
      "site": "00634b88",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00634b40",
      "incomplete_value": false,
      "site": "00634b48",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00634a9c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00634a5c",
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
      "00634a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00634aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00634b0c",
      "DATA",
      [
        "storage",
        "00c731a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00634a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00634aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00634b0c",
      "DATA",
      [
        "storage",
        "00c735a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00634a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md#insn-00634a5c) · [`00634aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md#insn-00634aac) · [`00634efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/00634a24.md#insn-00634efc)
- 新版 `00634a9c`（命令位置の公開資料なし） · `00634aec`（命令位置の公開資料なし） · `00634f3c`（命令位置の公開資料なし）

~~~diff
- 00634a5c ["INT_ADD", "register:40f0:8", ["const:634a5c:8", "const:4:8"]]
- 00634a5c ["CALL", null, ["ram:47acb4:8"]]
+ 00634a9c ["INT_ADD", "register:40f0:8", ["const:634a9c:8", "const:4:8"]]
+ 00634a9c ["CALL", null, ["ram:47acf4:8"]]
- 00634a5c bytes 9618f997
+ 00634a9c bytes 9618f997
- 00634aac ["INT_ADD", "register:40f0:8", ["const:634aac:8", "const:4:8"]]
- 00634aac ["CALL", null, ["ram:47acb4:8"]]
+ 00634aec ["INT_ADD", "register:40f0:8", ["const:634aec:8", "const:4:8"]]
+ 00634aec ["CALL", null, ["ram:47acf4:8"]]
- 00634aac bytes 8218f997
+ 00634aec bytes 8218f997
- 00634efc ["INT_ADD", "register:40f0:8", ["const:634efc:8", "const:4:8"]]
- 00634efc ["CALL", null, ["ram:47acb4:8"]]
+ 00634f3c ["INT_ADD", "register:40f0:8", ["const:634f3c:8", "const:4:8"]]
+ 00634f3c ["CALL", null, ["ram:47acf4:8"]]
- 00634efc bytes 6e17f997
+ 00634f3c bytes 6e17f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef0465ea67edb57471a8d814dd4629fa"></a>

### [`006350c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md) → [`00635104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635104.md) FUN_00635104

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) · 呼出先 12件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) · 呼出先 12件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00635210",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006351d0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063525c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063521c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006352ac",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063526c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00635210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0063525c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006352ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00635210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0063525c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006352ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006351d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md#insn-006351d0) · [`0063521c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md#insn-0063521c) · [`0063526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006350c4.md#insn-0063526c)
- 新版 `00635210`（命令位置の公開資料なし） · `0063525c`（命令位置の公開資料なし） · `006352ac`（命令位置の公開資料なし）

~~~diff
- 006351d0 ["INT_ADD", "register:40f0:8", ["const:6351d0:8", "const:4:8"]]
- 006351d0 ["CALL", null, ["ram:46c984:8"]]
+ 00635210 ["INT_ADD", "register:40f0:8", ["const:635210:8", "const:4:8"]]
+ 00635210 ["CALL", null, ["ram:46c9c4:8"]]
- 006351d0 bytes edddf897
+ 00635210 bytes edddf897
- 0063521c ["INT_ADD", "register:40f0:8", ["const:63521c:8", "const:4:8"]]
- 0063521c ["CALL", null, ["ram:46c984:8"]]
+ 0063525c ["INT_ADD", "register:40f0:8", ["const:63525c:8", "const:4:8"]]
+ 0063525c ["CALL", null, ["ram:46c9c4:8"]]
- 0063521c bytes daddf897
+ 0063525c bytes daddf897
- 0063526c ["INT_ADD", "register:40f0:8", ["const:63526c:8", "const:4:8"]]
- 0063526c ["CALL", null, ["ram:46c984:8"]]
+ 006352ac ["INT_ADD", "register:40f0:8", ["const:6352ac:8", "const:4:8"]]
+ 006352ac ["CALL", null, ["ram:46c9c4:8"]]
- 0063526c bytes c6ddf897
+ 006352ac bytes c6ddf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c76171ae267fabd0ca63733d231e1a2"></a>

### [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) → [`006354f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006354f0.md) FUN_006354f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 8件 [`00497aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md) [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) [`00635678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635678.md) [`0063567c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/0063567c.md)
- 新版 呼出元 3件 [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 8件 [`00497ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497ae4.md) [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) [`00497df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md) [`006356b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006356b8.md) [`006356bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006356bc.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00635550",
      "incomplete_value": false,
      "site": "00635558",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635510",
      "incomplete_value": false,
      "site": "00635518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "00635558",
      "DATA",
      [
        "storage",
        "00c72f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00635590",
      "READ",
      [
        "storage",
        "00c72f98",
        null,
        "pointer"
      ]
    ],
    [
      "00635590",
      "READ",
      [
        "storage",
        "00c72fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635558",
      "DATA",
      [
        "storage",
        "00c73378",
        null,
        "undefined *"
      ]
    ],
    [
      "00635590",
      "READ",
      [
        "storage",
        "00c73398",
        null,
        "pointer"
      ]
    ],
    [
      "00635590",
      "READ",
      [
        "storage",
        "00c733a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006354e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md#insn-006354e0) · [`006354e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md#insn-006354e8) · [`006354fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md#insn-006354fc)
- 新版 `00635520`（命令位置の公開資料なし） · `00635528`（命令位置の公開資料なし） · `0063553c`（命令位置の公開資料なし）

~~~diff
- 006354e0 ["INT_ADD", "register:40f0:8", ["const:6354e0:8", "const:4:8"]]
- 006354e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00635520 ["INT_ADD", "register:40f0:8", ["const:635520:8", "const:4:8"]]
+ 00635520 ["CALL", null, ["callee:00c57e90:8"]]
- 006354e0 bytes 6c891894
+ 00635520 bytes 5c8a1894
- 006354e8 ["INT_ADD", "register:40f0:8", ["const:6354e8:8", "const:4:8"]]
- 006354e8 ["CALL", null, ["callee:00497ae4:8"]]
+ 00635528 ["INT_ADD", "register:40f0:8", ["const:635528:8", "const:4:8"]]
+ 00635528 ["CALL", null, ["callee:00497ae4:8"]]
- 006354e8 bytes 6f89f997
+ 00635528 bytes 6f89f997
- 006354fc ["INT_ADD", "register:40f0:8", ["const:6354fc:8", "const:4:8"]]
- 006354fc ["CALL", null, ["callee:00497c7c:8"]]
+ 0063553c ["INT_ADD", "register:40f0:8", ["const:63553c:8", "const:4:8"]]
+ 0063553c ["CALL", null, ["callee:00497c7c:8"]]
- 006354fc bytes d089f997
+ 0063553c bytes d089f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de196d410d8dc8a5325e3dd1820e4574"></a>

### [`00635644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635644.md) → [`00635684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635684.md) FUN_00635684

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00635698",
      "incomplete_value": false,
      "site": "0063569c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635658",
      "incomplete_value": false,
      "site": "0063565c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "0063569c",
      "DATA",
      [
        "storage",
        "00c72f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063569c",
      "DATA",
      [
        "storage",
        "00c73378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635644.md#insn-00635650) · [`00635654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635644.md#insn-00635654) · [`00635658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635644.md#insn-00635658)
- 新版 `00635690`（命令位置の公開資料なし） · `00635694`（命令位置の公開資料なし） · `00635698`（命令位置の公開資料なし）

~~~diff
- 00635650 ["INT_ADD", "register:40f0:8", ["const:635650:8", "const:4:8"]]
- 00635650 ["CALL", null, ["callee:00c57e90:8"]]
+ 00635690 ["INT_ADD", "register:40f0:8", ["const:635690:8", "const:4:8"]]
+ 00635690 ["CALL", null, ["callee:00c57e90:8"]]
- 00635650 bytes 10891894
+ 00635690 bytes 008a1894
- 00635654 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 00635694 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00635654 bytes e83100b0
+ 00635694 bytes e83100d0
- 00635658 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00635658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00635658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00635658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00635698 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00635698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00635698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00635698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00635658 bytes 08e13d91
+ 00635698 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d0fb23275a69208fe653ed52010e969"></a>

### [`00635668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635668.md) → [`006356a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006356a8.md) FUN_006356a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006356ac",
      "incomplete_value": false,
      "site": "006356b0",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063566c",
      "incomplete_value": false,
      "site": "00635670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "006356b0",
      "DATA",
      [
        "storage",
        "00c72f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006356b0",
      "DATA",
      [
        "storage",
        "00c73378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635668.md#insn-00635668) · [`0063566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635668.md#insn-0063566c)
- 新版 `006356a8`（命令位置の公開資料なし） · `006356ac`（命令位置の公開資料なし）

~~~diff
- 00635668 ["COPY", "register:4040:8", ["const:c72000:8"]]
+ 006356a8 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00635668 bytes e83100b0
+ 006356a8 bytes e83100d0
- 0063566c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0063566c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0063566c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0063566c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006356ac ["COPY", "tmp:0:8", ["const:378:8"]]
+ 006356ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006356ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006356ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0063566c bytes 08e13d91
+ 006356ac bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19dab59e036b9098b27c6cace6a0d27"></a>

### [`006356ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006356ac.md) → [`006356ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006356ec.md) FUN_006356ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00635704",
      "incomplete_value": false,
      "site": "00635708",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006356c4",
      "incomplete_value": false,
      "site": "006356c8",
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
            "const:8:8"
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
      "00635708",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635708",
      "DATA",
      [
        "storage",
        "00c73408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006356c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006356ac.md#insn-006356c4) · [`006356f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006356ac.md#insn-006356f0) · [`00635700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006356ac.md#insn-00635700)
- 新版 `00635704`（命令位置の公開資料なし） · `00635730`（命令位置の公開資料なし） · `00635740`（命令位置の公開資料なし）

~~~diff
- 006356c4 ["COPY", "tmp:0:8", ["const:8:8"]]
- 006356c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006356c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006356c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00635704 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00635704 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00635704 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00635704 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006356c4 bytes 29210091
+ 00635704 bytes 29211091
- 006356f0 ["INT_ADD", "register:40f0:8", ["const:6356f0:8", "const:4:8"]]
- 006356f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00635730 ["INT_ADD", "register:40f0:8", ["const:635730:8", "const:4:8"]]
+ 00635730 ["CALL", null, ["callee:00c57eb0:8"]]
- 006356f0 bytes f0881894
+ 00635730 bytes e0891894
- 00635700 ["INT_ADD", "register:40f0:8", ["const:635700:8", "const:4:8"]]
- 00635700 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00635740 ["INT_ADD", "register:40f0:8", ["const:635740:8", "const:4:8"]]
+ 00635740 ["CALL", null, ["callee:00c57eb0:8"]]
- 00635700 bytes ec881894
+ 00635740 bytes dc891894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baba0896837b739ac8b20cc3a0f048af"></a>

### [`00635718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md) → [`00635758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635758.md) FUN_00635758

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00635770",
      "incomplete_value": false,
      "site": "00635774",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635730",
      "incomplete_value": false,
      "site": "00635734",
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
            "const:8:8"
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
      "00635774",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635774",
      "DATA",
      [
        "storage",
        "00c73408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md#insn-00635774) · [`00635730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md#insn-00635730) · [`0063574c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md#insn-0063574c)
- 新版 `006357b4`（命令位置の公開資料なし） · `00635770`（命令位置の公開資料なし） · `0063578c`（命令位置の公開資料なし）

~~~diff
- 00635774 ["INT_ADD", "register:40f0:8", ["const:635774:8", "const:4:8"]]
- 00635774 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006357b4 ["INT_ADD", "register:40f0:8", ["const:6357b4:8", "const:4:8"]]
+ 006357b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00635774 bytes cf881894
+ 006357b4 bytes bf891894
- 00635730 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00635730 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00635730 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00635730 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00635770 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00635770 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00635770 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00635770 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00635730 bytes 29210091
+ 00635770 bytes 29211091
- 0063574c ["INT_ADD", "register:40f0:8", ["const:63574c:8", "const:4:8"]]
- 0063574c ["CALL", null, ["callee:00c57e80:8"]]
+ 0063578c ["INT_ADD", "register:40f0:8", ["const:63578c:8", "const:4:8"]]
+ 0063578c ["CALL", null, ["callee:00c57e80:8"]]
- 0063574c bytes cd881894
+ 0063578c bytes bd891894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f9d8f8eb1878e2ab0de833a6707242f"></a>

### [`00635784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635784.md) → [`006357c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006357c4.md) FUN_006357c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`006359c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006359c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00635a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635a00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "006357e8",
      "incomplete_value": false,
      "site": "006357e8",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006357a8",
      "incomplete_value": false,
      "site": "006357a8",
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
            "const:8:8"
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
      "006357e8",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006357e8",
      "DATA",
      [
        "storage",
        "00c73408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635784.md#insn-00635798) · [`006357a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635784.md#insn-006357a4) · [`006357b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635784.md#insn-006357b0)
- 新版 `006357d8`（命令位置の公開資料なし） · `006357e4`（命令位置の公開資料なし） · `006357f0`（命令位置の公開資料なし）

~~~diff
- 00635798 ["INT_ADD", "register:40f0:8", ["const:635798:8", "const:4:8"]]
- 00635798 ["CALL", null, ["callee:00c57e90:8"]]
+ 006357d8 ["INT_ADD", "register:40f0:8", ["const:6357d8:8", "const:4:8"]]
+ 006357d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00635798 bytes be881894
+ 006357d8 bytes ae891894
- 006357a4 ["COPY", "tmp:0:8", ["const:8:8"]]
- 006357a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006357a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006357a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006357e4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 006357e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006357e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006357e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006357a4 bytes 08210091
+ 006357e4 bytes 08211091
- 006357b0 ["INT_ADD", "register:40f0:8", ["const:6357b0:8", "const:4:8"]]
- 006357b0 ["CALL", null, ["callee:00635a00:8"]]
+ 006357f0 ["INT_ADD", "register:40f0:8", ["const:6357f0:8", "const:4:8"]]
+ 006357f0 ["CALL", null, ["callee:00635a00:8"]]
- 006357b0 bytes 84000094
+ 006357f0 bytes 84000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af3dc9d967e182b796ad22d54625284f"></a>

### [`006357d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006357d8.md) → [`00635818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635818.md) FUN_00635818

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`006359c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006359c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00635a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635a00.md)

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
      "definition_site": "00635824",
      "incomplete_value": false,
      "site": "00635824",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006357e4",
      "incomplete_value": false,
      "site": "006357e4",
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
            "const:8:8"
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
      "00635824",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635824",
      "DATA",
      [
        "storage",
        "00c73408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006357dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006357d8.md#insn-006357dc)
- 新版 `0063581c`（命令位置の公開資料なし）

~~~diff
- 006357dc ["COPY", "tmp:0:8", ["const:8:8"]]
- 006357dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006357dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006357dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063581c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0063581c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063581c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063581c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006357dc bytes 08210091
+ 0063581c bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f7706a237548a9c3a279f7082c74af"></a>

### [`00635c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md) → [`00635c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635c84.md) FUN_00635c84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00635c9c",
      "incomplete_value": false,
      "site": "00635ca0",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635c5c",
      "incomplete_value": false,
      "site": "00635c60",
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
      "00635ca0",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635ca0",
      "DATA",
      [
        "storage",
        "00c73488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md#insn-00635c5c) · [`00635c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md#insn-00635c88) · [`00635c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md#insn-00635c98)
- 新版 `00635c9c`（命令位置の公開資料なし） · `00635cc8`（命令位置の公開資料なし） · `00635cd8`（命令位置の公開資料なし）

~~~diff
- 00635c5c ["COPY", "tmp:0:8", ["const:88:8"]]
- 00635c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00635c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00635c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00635c9c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00635c9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00635c9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00635c9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00635c5c bytes 29210291
+ 00635c9c bytes 29211291
- 00635c88 ["INT_ADD", "register:40f0:8", ["const:635c88:8", "const:4:8"]]
- 00635c88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00635cc8 ["INT_ADD", "register:40f0:8", ["const:635cc8:8", "const:4:8"]]
+ 00635cc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00635c88 bytes 8a871894
+ 00635cc8 bytes 7a881894
- 00635c98 ["INT_ADD", "register:40f0:8", ["const:635c98:8", "const:4:8"]]
- 00635c98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00635cd8 ["INT_ADD", "register:40f0:8", ["const:635cd8:8", "const:4:8"]]
+ 00635cd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00635c98 bytes 86871894
+ 00635cd8 bytes 76881894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b3a69b2fc3b85744adf026e3405b236"></a>

### [`00635cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md) → [`00635cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635cf0.md) FUN_00635cf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00635d08",
      "incomplete_value": false,
      "site": "00635d0c",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635cc8",
      "incomplete_value": false,
      "site": "00635ccc",
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
      "00635d0c",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635d0c",
      "DATA",
      [
        "storage",
        "00c73488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md#insn-00635d0c) · [`00635cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md#insn-00635cc8) · [`00635ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md#insn-00635ce4)
- 新版 `00635d4c`（命令位置の公開資料なし） · `00635d08`（命令位置の公開資料なし） · `00635d24`（命令位置の公開資料なし）

~~~diff
- 00635d0c ["INT_ADD", "register:40f0:8", ["const:635d0c:8", "const:4:8"]]
- 00635d0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00635d4c ["INT_ADD", "register:40f0:8", ["const:635d4c:8", "const:4:8"]]
+ 00635d4c ["CALL", null, ["callee:00c57eb0:8"]]
- 00635d0c bytes 69871894
+ 00635d4c bytes 59881894
- 00635cc8 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00635cc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00635cc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00635cc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00635d08 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00635d08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00635d08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00635d08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00635cc8 bytes 29210291
+ 00635d08 bytes 29211291
- 00635ce4 ["INT_ADD", "register:40f0:8", ["const:635ce4:8", "const:4:8"]]
- 00635ce4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00635d24 ["INT_ADD", "register:40f0:8", ["const:635d24:8", "const:4:8"]]
+ 00635d24 ["CALL", null, ["callee:00c57e80:8"]]
- 00635ce4 bytes 67871894
+ 00635d24 bytes 57881894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab955c6b23a0a2ef6ec0eb490203fd9"></a>

### [`00635d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d1c.md) → [`00635d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635d5c.md) FUN_00635d5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00635f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635f58.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00635f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635f98.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00635d80",
      "incomplete_value": false,
      "site": "00635d80",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635d40",
      "incomplete_value": false,
      "site": "00635d40",
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
            "const:88:8"
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
      "00635d80",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635d80",
      "DATA",
      [
        "storage",
        "00c73488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d1c.md#insn-00635d30) · [`00635d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d1c.md#insn-00635d3c) · [`00635d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d1c.md#insn-00635d48)
- 新版 `00635d70`（命令位置の公開資料なし） · `00635d7c`（命令位置の公開資料なし） · `00635d88`（命令位置の公開資料なし）

~~~diff
- 00635d30 ["INT_ADD", "register:40f0:8", ["const:635d30:8", "const:4:8"]]
- 00635d30 ["CALL", null, ["callee:00c57e90:8"]]
+ 00635d70 ["INT_ADD", "register:40f0:8", ["const:635d70:8", "const:4:8"]]
+ 00635d70 ["CALL", null, ["callee:00c57e90:8"]]
- 00635d30 bytes 58871894
+ 00635d70 bytes 48881894
- 00635d3c ["COPY", "tmp:0:8", ["const:88:8"]]
- 00635d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00635d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00635d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00635d7c ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00635d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00635d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00635d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00635d3c bytes 08210291
+ 00635d7c bytes 08211291
- 00635d48 ["INT_ADD", "register:40f0:8", ["const:635d48:8", "const:4:8"]]
- 00635d48 ["CALL", null, ["callee:00635f98:8"]]
+ 00635d88 ["INT_ADD", "register:40f0:8", ["const:635d88:8", "const:4:8"]]
+ 00635d88 ["CALL", null, ["callee:00635f98:8"]]
- 00635d48 bytes 84000094
+ 00635d88 bytes 84000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b798ce4eac76236d139cfbd17f15197"></a>

### [`00635d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d70.md) → [`00635db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635db0.md) FUN_00635db0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00635f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635f58.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00635f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635f98.md)

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
      "definition_site": "00635dbc",
      "incomplete_value": false,
      "site": "00635dbc",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635d7c",
      "incomplete_value": false,
      "site": "00635d7c",
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
      "00635dbc",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635dbc",
      "DATA",
      [
        "storage",
        "00c73488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635d70.md#insn-00635d74)
- 新版 `00635db4`（命令位置の公開資料なし）

~~~diff
- 00635d74 ["COPY", "tmp:0:8", ["const:88:8"]]
- 00635d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00635d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00635d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00635db4 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00635db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00635db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00635db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00635d74 bytes 08210291
+ 00635db4 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7e2a04e78a4ca3c83dddb1566bd101"></a>

### [`0063648c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063648c.md) → [`006364cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006364cc.md) FUN_006364cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00636230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636230.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00636270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636270.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "006364d8",
      "incomplete_value": false,
      "site": "006364dc",
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
      "definition_site": "00636498",
      "incomplete_value": false,
      "site": "0063649c",
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
      "006364d8",
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
      "006364d8",
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

- 旧版 [`0063649c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063648c.md#insn-0063649c) · [`00636498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063648c.md#insn-00636498)
- 新版 `006364dc`（命令位置の公開資料なし） · `006364d8`（命令位置の公開資料なし）

~~~diff
- 0063649c ["INT_ADD", "register:40f0:8", ["const:63649c:8", "const:4:8"]]
- 0063649c ["CALL", null, ["callee:0043b778:8"]]
+ 006364dc ["INT_ADD", "register:40f0:8", ["const:6364dc:8", "const:4:8"]]
+ 006364dc ["CALL", null, ["callee:0043b778:8"]]
- 0063649c bytes a714f897
+ 006364dc bytes a714f897
- 00636498 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00636498 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00636498 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00636498 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006364d8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 006364d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006364d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006364d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00636498 bytes 00303c91
+ 006364d8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53fd504dfbb575c1d8fb5b39b1842445"></a>

### [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md) → [`0063674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063674c.md) FUN_0063674c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00636584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636584.md) [`00652d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652d20.md) [`00741238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md) [`00792e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md) [`00794194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 6件 [`006365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006365c4.md) [`00652d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652d60.md) [`00741278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/00741278.md) [`00792eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792eb4.md) [`007941d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007941d4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00636758",
      "incomplete_value": false,
      "site": "0063675c",
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
      "definition_site": "00636718",
      "incomplete_value": false,
      "site": "0063671c",
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
      "00636758",
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
      "00636758",
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

- 旧版 [`0063671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md#insn-0063671c) · [`00636718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md#insn-00636718)
- 新版 `0063675c`（命令位置の公開資料なし） · `00636758`（命令位置の公開資料なし）

~~~diff
- 0063671c ["INT_ADD", "register:40f0:8", ["const:63671c:8", "const:4:8"]]
- 0063671c ["CALL", null, ["callee:0043b778:8"]]
+ 0063675c ["INT_ADD", "register:40f0:8", ["const:63675c:8", "const:4:8"]]
+ 0063675c ["CALL", null, ["callee:0043b778:8"]]
- 0063671c bytes 0714f897
+ 0063675c bytes 0714f897
- 00636718 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00636718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00636718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00636718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00636758 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00636758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00636758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00636758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00636718 bytes 00303c91
+ 00636758 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a77369ed2624abddf70a3e5621432c4b"></a>

### [`00636724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636724.md) → [`00636764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636764.md) FUN_00636764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00636778",
      "incomplete_value": false,
      "site": "0063677c",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00636738",
      "incomplete_value": false,
      "site": "0063673c",
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
      "0063677c",
      "DATA",
      [
        "storage",
        "00c73120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063677c",
      "DATA",
      [
        "storage",
        "00c73520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00636730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636724.md#insn-00636730) · [`00636738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636724.md#insn-00636738)
- 新版 `00636770`（命令位置の公開資料なし） · `00636778`（命令位置の公開資料なし）

~~~diff
- 00636730 ["INT_ADD", "register:40f0:8", ["const:636730:8", "const:4:8"]]
- 00636730 ["CALL", null, ["callee:00c57e90:8"]]
+ 00636770 ["INT_ADD", "register:40f0:8", ["const:636770:8", "const:4:8"]]
+ 00636770 ["CALL", null, ["callee:00c57e90:8"]]
- 00636730 bytes d8841894
+ 00636770 bytes c8851894
- 00636738 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00636738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00636738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00636738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00636778 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00636778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00636778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00636778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00636738 bytes 08810491
+ 00636778 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b4d6e4faa0b44ecf4e0afec0fe530bf"></a>

### [`00636748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636748.md) → [`00636788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636788.md) FUN_00636788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0063678c",
      "incomplete_value": true,
      "site": "00636790",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063674c",
      "incomplete_value": true,
      "site": "00636750",
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
      "00636790",
      "DATA",
      [
        "storage",
        "00c73120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00636790",
      "DATA",
      [
        "storage",
        "00c73520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063674c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636748.md#insn-0063674c)
- 新版 `0063678c`（命令位置の公開資料なし）

~~~diff
- 0063674c ["COPY", "tmp:0:8", ["const:120:8"]]
- 0063674c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0063674c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0063674c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063678c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0063678c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063678c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063678c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0063674c bytes 08810491
+ 0063678c bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6de6105e5aabb6fa08152236f638dfa0"></a>

### [`00636760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636760.md) → [`006367a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006367a0.md) FUN_006367a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00629ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ae8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00629b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629b28.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "00636840",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00636800",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063684c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063680c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00636840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0063684c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00636840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0063684c",
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

- 旧版 [`006367c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636760.md#insn-006367c0) · [`00636800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636760.md#insn-00636800) · [`0063680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636760.md#insn-0063680c)
- 新版 `00636800`（命令位置の公開資料なし） · `00636840`（命令位置の公開資料なし） · `0063684c`（命令位置の公開資料なし）

~~~diff
- 006367c0 ["INT_ADD", "register:40f0:8", ["const:6367c0:8", "const:4:8"]]
- 006367c0 ["CALL", null, ["callee:00a46bb8:8"]]
+ 00636800 ["INT_ADD", "register:40f0:8", ["const:636800:8", "const:4:8"]]
+ 00636800 ["CALL", null, ["callee:00a46bb8:8"]]
- 006367c0 bytes 80401094
+ 00636800 bytes ee401094
- 00636800 ["INT_ADD", "register:40f0:8", ["const:636800:8", "const:4:8"]]
- 00636800 ["CALL", null, ["ram:47acb4:8"]]
+ 00636840 ["INT_ADD", "register:40f0:8", ["const:636840:8", "const:4:8"]]
+ 00636840 ["CALL", null, ["ram:47acf4:8"]]
- 00636800 bytes 2d11f997
+ 00636840 bytes 2d11f997
- 0063680c ["INT_ADD", "register:40f0:8", ["const:63680c:8", "const:4:8"]]
- 0063680c ["CALL", null, ["ram:47acb4:8"]]
+ 0063684c ["INT_ADD", "register:40f0:8", ["const:63684c:8", "const:4:8"]]
+ 0063684c ["CALL", null, ["ram:47acf4:8"]]
- 0063680c bytes 2a11f997
+ 0063684c bytes 2a11f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f5375a082293b3fc633e63ade1b54c"></a>

### [`0063687c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063687c.md) → [`006368bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006368bc.md) FUN_006368bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006368d0",
      "incomplete_value": false,
      "site": "006368d4",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00636890",
      "incomplete_value": false,
      "site": "00636894",
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
            "const:1a0:8"
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
      "006368d4",
      "DATA",
      [
        "storage",
        "00c731a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006368d4",
      "DATA",
      [
        "storage",
        "00c735a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00636888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063687c.md#insn-00636888) · [`00636890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063687c.md#insn-00636890)
- 新版 `006368c8`（命令位置の公開資料なし） · `006368d0`（命令位置の公開資料なし）

~~~diff
- 00636888 ["INT_ADD", "register:40f0:8", ["const:636888:8", "const:4:8"]]
- 00636888 ["CALL", null, ["callee:00c57e90:8"]]
+ 006368c8 ["INT_ADD", "register:40f0:8", ["const:6368c8:8", "const:4:8"]]
+ 006368c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00636888 bytes 82841894
+ 006368c8 bytes 72851894
- 00636890 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00636890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00636890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00636890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006368d0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 006368d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006368d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006368d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00636890 bytes 08810691
+ 006368d0 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016195bbd74a3ae6dd27e9cbc63ad2f6"></a>

### [`006368a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368a0.md) → [`006368e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006368e0.md) FUN_006368e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006368e4",
      "incomplete_value": false,
      "site": "006368e8",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006368a4",
      "incomplete_value": false,
      "site": "006368a8",
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
      "006368e8",
      "DATA",
      [
        "storage",
        "00c731a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006368e8",
      "DATA",
      [
        "storage",
        "00c735a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006368a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368a0.md#insn-006368a4)
- 新版 `006368e4`（命令位置の公開資料なし）

~~~diff
- 006368a4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 006368a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006368a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006368a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006368e4 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 006368e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006368e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006368e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006368a4 bytes 08810691
+ 006368e4 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db2ac136db6843260eaa1171b0c1041"></a>

### [`006368b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368b8.md) → [`006368f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006368f8.md) FUN_006368f8

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
      "site": "0063691c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006368dc",
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
      "0063691c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0063691c",
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

- 旧版 [`006368dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368b8.md#insn-006368dc) · [`006368e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006368b8.md#insn-006368e8)
- 新版 `0063691c`（命令位置の公開資料なし） · `00636928`（命令位置の公開資料なし）

~~~diff
- 006368dc ["INT_ADD", "register:40f0:8", ["const:6368dc:8", "const:4:8"]]
- 006368dc ["CALL", null, ["ram:47acb4:8"]]
+ 0063691c ["INT_ADD", "register:40f0:8", ["const:63691c:8", "const:4:8"]]
+ 0063691c ["CALL", null, ["ram:47acf4:8"]]
- 006368dc bytes f610f997
+ 0063691c bytes f610f997
- 006368e8 ["INT_ADD", "register:40f0:8", ["const:6368e8:8", "const:4:8"]]
- 006368e8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00636928 ["INT_ADD", "register:40f0:8", ["const:636928:8", "const:4:8"]]
+ 00636928 ["CALL", null, ["callee:0047cdd4:8"]]
- 006368e8 bytes 2b19f997
+ 00636928 bytes 2b19f997
~~~


<a id="compare-69649069c60307bbfdd4cbcba8fda9af"></a>

### [`0063692c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063692c.md) → [`0063696c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063696c.md) FUN_0063696c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00636980",
      "incomplete_value": false,
      "site": "00636984",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00636940",
      "incomplete_value": false,
      "site": "00636944",
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
            "const:220:8"
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
      "00636984",
      "DATA",
      [
        "storage",
        "00c73220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00636984",
      "DATA",
      [
        "storage",
        "00c73620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00636938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063692c.md#insn-00636938) · [`00636940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063692c.md#insn-00636940)
- 新版 `00636978`（命令位置の公開資料なし） · `00636980`（命令位置の公開資料なし）

~~~diff
- 00636938 ["INT_ADD", "register:40f0:8", ["const:636938:8", "const:4:8"]]
- 00636938 ["CALL", null, ["callee:00c57e90:8"]]
+ 00636978 ["INT_ADD", "register:40f0:8", ["const:636978:8", "const:4:8"]]
+ 00636978 ["CALL", null, ["callee:00c57e90:8"]]
- 00636938 bytes 56841894
+ 00636978 bytes 46851894
- 00636940 ["COPY", "tmp:0:8", ["const:220:8"]]
- 00636940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00636940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00636940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00636980 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00636980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00636980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00636980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00636940 bytes 08810891
+ 00636980 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-def6113198d9371890a47a739dda5516"></a>

### [`00636950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636950.md) → [`00636990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636990.md) FUN_00636990

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00636994",
      "incomplete_value": false,
      "site": "00636998",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00636954",
      "incomplete_value": false,
      "site": "00636958",
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
      "00636998",
      "DATA",
      [
        "storage",
        "00c73220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00636998",
      "DATA",
      [
        "storage",
        "00c73620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00636954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636950.md#insn-00636954)
- 新版 `00636994`（命令位置の公開資料なし）

~~~diff
- 00636954 ["COPY", "tmp:0:8", ["const:220:8"]]
- 00636954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00636954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00636954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00636994 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00636994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00636994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00636994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00636954 bytes 08810891
+ 00636994 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c543d0534521b750ee66228996f273ad"></a>

### [`00636968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636968.md) → [`006369a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/006369a8.md) FUN_006369a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00636a18",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006369d8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00636c04",
      "incomplete_value": false,
      "site": "00636c14",
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
      "definition_site": "00636bc4",
      "incomplete_value": false,
      "site": "00636bd4",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00636c0c",
      "incomplete_value": false,
      "site": "00636c14",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00636bcc",
      "incomplete_value": false,
      "site": "00636bd4",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00636a18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00636bf8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00636c04",
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
      "00636a18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00636bf8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00636c04",
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

- 旧版 [`006369d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636968.md#insn-006369d8) · [`00636bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636968.md#insn-00636bd4) · [`00636bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636968.md#insn-00636bec)
- 新版 `00636a18`（命令位置の公開資料なし） · `00636c14`（命令位置の公開資料なし） · `00636c2c`（命令位置の公開資料なし）

~~~diff
- 006369d8 ["INT_ADD", "register:40f0:8", ["const:6369d8:8", "const:4:8"]]
- 006369d8 ["CALL", null, ["ram:46c984:8"]]
+ 00636a18 ["INT_ADD", "register:40f0:8", ["const:636a18:8", "const:4:8"]]
+ 00636a18 ["CALL", null, ["ram:46c9c4:8"]]
- 006369d8 bytes ebd7f897
+ 00636a18 bytes ebd7f897
- 00636bd4 ["INT_ADD", "register:40f0:8", ["const:636bd4:8", "const:4:8"]]
- 00636bd4 ["CALL", null, ["callee:00c58610:8"]]
+ 00636c14 ["INT_ADD", "register:40f0:8", ["const:636c14:8", "const:4:8"]]
+ 00636c14 ["CALL", null, ["callee:00c58610:8"]]
- 00636bd4 bytes 8f851894
+ 00636c14 bytes 7f861894
- 00636bec ["INT_ADD", "register:40f0:8", ["const:636bec:8", "const:4:8"]]
- 00636bec ["CALL", null, ["ram:46c984:8"]]
+ 00636c2c ["INT_ADD", "register:40f0:8", ["const:636c2c:8", "const:4:8"]]
+ 00636c2c ["CALL", null, ["ram:46c9c4:8"]]
- 00636bec bytes 66d7f897
+ 00636c2c bytes 66d7f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b938603271e91aaeecf21dc26132ab"></a>

### [`00636cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636cc8.md) → [`00636d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636d08.md) _INIT_80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00636d44",
      "incomplete_value": true,
      "site": "00636d60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00636d04",
      "incomplete_value": true,
      "site": "00636d20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00636d68",
      "incomplete_value": true,
      "site": "00636d84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00636d28",
      "incomplete_value": true,
      "site": "00636d44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00636d88",
      "incomplete_value": true,
      "site": "00636da4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00636d48",
      "incomplete_value": true,
      "site": "00636d64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00636d44",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00636d68",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00636d88",
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
      "00636d44",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00636d68",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00636d88",
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

- 旧版 [`00636d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636cc8.md#insn-00636d60) · [`00636efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636cc8.md#insn-00636efc) · [`00636cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636cc8.md#insn-00636cf4)
- 新版 `00636da0`（命令位置の公開資料なし） · `00636f3c`（命令位置の公開資料なし） · `00636d34`（命令位置の公開資料なし）

~~~diff
- 00636d60 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00636d60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00636d60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00636d60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00636da0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00636da0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00636da0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00636da0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00636d60 bytes 4a553a91
+ 00636da0 bytes 4a893d91
- 00636efc ["INT_ADD", "register:40f0:8", ["const:636efc:8", "const:4:8"]]
- 00636efc ["CALL", null, ["callee:00c57e30:8"]]
+ 00636f3c ["INT_ADD", "register:40f0:8", ["const:636f3c:8", "const:4:8"]]
+ 00636f3c ["CALL", null, ["callee:00c57e30:8"]]
- 00636efc bytes cd821894
+ 00636f3c bytes bd831894
- 00636cf4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00636cf4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00636cf4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00636cf4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00636d34 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00636d34 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00636d34 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00636d34 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00636cf4 bytes 73821891
+ 00636d34 bytes 73822891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66fad60bd37df7bf58eafb8fc200d730"></a>

### [`006376a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006376a8.md) → [`006376e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/006376e8.md) FUN_006376e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`006375d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006375d0.md) [`00638dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00638/00638dac.md) · 呼出先 4件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00637610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637610.md) [`00638dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00638/00638dec.md) · 呼出先 4件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00637730",
      "incomplete_value": true,
      "site": "00637730",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:db3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006376f0",
      "incomplete_value": true,
      "site": "006376f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d73:8"
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
      "0063771c",
      "READ",
      [
        "storage",
        "002b3d73",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063771c",
      "READ",
      [
        "storage",
        "002b3db3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006376cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006376a8.md#insn-006376cc) · [`006376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006376a8.md#insn-006376d4) · [`00637704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006376a8.md#insn-00637704)
- 新版 `0063770c`（命令位置の公開資料なし） · `00637714`（命令位置の公開資料なし） · `00637744`（命令位置の公開資料なし）

~~~diff
- 006376cc ["INT_ADD", "register:40f0:8", ["const:6376cc:8", "const:4:8"]]
- 006376cc ["CALL", null, ["callee:00550c2c:8"]]
+ 0063770c ["INT_ADD", "register:40f0:8", ["const:63770c:8", "const:4:8"]]
+ 0063770c ["CALL", null, ["callee:00550c2c:8"]]
- 006376cc bytes 4865fc97
+ 0063770c bytes 4865fc97
- 006376d4 ["COPY", "tmp:0:8", ["const:d73:8"]]
- 006376d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006376d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006376d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00637714 ["COPY", "tmp:0:8", ["const:db3:8"]]
+ 00637714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00637714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00637714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006376d4 bytes 29cd3591
+ 00637714 bytes 29cd3691
- 00637704 ["INT_ADD", "register:40f0:8", ["const:637704:8", "const:4:8"]]
- 00637704 ["CALL", null, ["callee:0043dba4:8"]]
+ 00637744 ["INT_ADD", "register:40f0:8", ["const:637744:8", "const:4:8"]]
+ 00637744 ["CALL", null, ["callee:0043dba4:8"]]
- 00637704 bytes 1819f897
+ 00637744 bytes 1819f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21195304c7fb4edeff2cbcf417e0b23f"></a>

### [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) → [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) FUN_00637850

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 31件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 31件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00637948",
      "incomplete_value": true,
      "site": "00637948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637908",
      "incomplete_value": true,
      "site": "00637908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:27d:8"
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
      "definition_site": "00637a18",
      "incomplete_value": true,
      "site": "00637a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006379d8",
      "incomplete_value": true,
      "site": "006379d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00637f90",
      "incomplete_value": true,
      "site": "00637f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637f50",
      "incomplete_value": true,
      "site": "00637f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:28a:8"
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
      "006378c8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "00637934",
      "READ",
      [
        "storage",
        "002b627d",
        null,
        "string"
      ]
    ],
    [
      "00637960",
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006378c8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "00637934",
      "READ",
      [
        "storage",
        "002b62bd",
        null,
        "string"
      ]
    ],
    [
      "00637960",
      "PARAM",
      [
        "storage",
        "002b9f30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md#insn-00637928) · [`00638938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md#insn-00638938) · [`00637864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md#insn-00637864)
- 新版 `00637968`（命令位置の公開資料なし） · `00638978`（命令位置の公開資料なし） · `006378a4`（命令位置の公開資料なし）

~~~diff
- 00637928 ["INT_ADD", "register:40f0:8", ["const:637928:8", "const:4:8"]]
- 00637928 ["CALL", null, ["callee:00c57f70:8"]]
+ 00637968 ["INT_ADD", "register:40f0:8", ["const:637968:8", "const:4:8"]]
+ 00637968 ["CALL", null, ["callee:00c57f70:8"]]
- 00637928 bytes 92801894
+ 00637968 bytes 82811894
- 00638938 ["COPY", "register:0:8", ["register:4040:8"]]
- 00638938 ["INT_ADD", "register:40f0:8", ["const:638938:8", "const:4:8"]]
- 00638938 ["CALLIND", null, ["register:0:8"]]
+ 00638978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00638978 ["INT_ADD", "register:40f0:8", ["const:638978:8", "const:4:8"]]
+ 00638978 ["CALLIND", null, ["register:0:8"]]
- 00638938 bytes 00013fd6
+ 00638978 bytes 00013fd6
- 00637864 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 00637864 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00637864 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00637864 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 006378a4 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 006378a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 006378a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 006378a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00637864 bytes b5d61a91
+ 006378a4 bytes b5d61b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

