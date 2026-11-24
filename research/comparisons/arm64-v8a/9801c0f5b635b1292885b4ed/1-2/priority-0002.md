# v16.0.0 → v16.0.1 · 最優先の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-4db871e57112939083f0ad067dc43522"></a>

### [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) → [`0044b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md) FUN_0044b584

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00477e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md) · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.64% / 新版 83.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b5c4",
      "incomplete_value": true,
      "site": "0044b5d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:550:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b584",
      "incomplete_value": true,
      "site": "0044b590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
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
      "definition_site": "0044b5c0",
      "incomplete_value": true,
      "site": "0044b5d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eb4:8"
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
      "definition_site": "0044b5c0",
      "incomplete_value": true,
      "site": "0044b5d4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
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
      "0044b5c0",
      "READ",
      [
        "storage",
        "002c0eb4",
        null,
        "string"
      ]
    ],
    [
      "0044b5c0",
      "READ",
      [
        "storage",
        "002c0ec4",
        null,
        "string"
      ]
    ],
    [
      "0044b5c4",
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044b5c0",
      "READ",
      [
        "storage",
        "002c0ef4",
        null,
        "string"
      ]
    ],
    [
      "0044b5c0",
      "READ",
      [
        "storage",
        "002c0f04",
        null,
        "string"
      ]
    ],
    [
      "0044b5c4",
      "READ",
      [
        "storage",
        "002c2550",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md#insn-0044b5b4) · [`0044b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md#insn-0044b5f4) · [`0044b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md#insn-0044b570)
- 新版 [`0044b5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md#insn-0044b5f4) · [`0044b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md#insn-0044b634) · [`0044b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md#insn-0044b5b0)

~~~diff
- 0044b5b4 ["INT_ADD", "register:40f0:8", ["const:44b5b4:8", "const:4:8"]]
- 0044b5b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044b5f4 ["INT_ADD", "register:40f0:8", ["const:44b5f4:8", "const:4:8"]]
+ 0044b5f4 ["CALL", null, ["callee:00c57f70:8"]]
- 0044b5b4 bytes 6f312094
+ 0044b5f4 bytes 5f322094
- 0044b5f4 ["INT_ADD", "register:40f0:8", ["const:44b5f4:8", "const:4:8"]]
- 0044b5f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044b634 ["INT_ADD", "register:40f0:8", ["const:44b634:8", "const:4:8"]]
+ 0044b634 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044b5f4 bytes 2f312094
+ 0044b634 bytes 1f322094
- 0044b570 ["INT_ADD", "register:40f0:8", ["const:44b570:8", "const:4:8"]]
- 0044b570 ["CALL", null, ["callee:00c57e90:8"]]
+ 0044b5b0 ["INT_ADD", "register:40f0:8", ["const:44b5b0:8", "const:4:8"]]
+ 0044b5b0 ["CALL", null, ["callee:00c57e90:8"]]
- 0044b570 bytes 48312094
+ 0044b5b0 bytes 38322094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29203b02f14aa0d7af2cc71d2e8e0a85"></a>

### [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) → [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) FUN_0044b700

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b724",
      "incomplete_value": true,
      "site": "0044b73c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b6e4",
      "incomplete_value": true,
      "site": "0044b6fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:620:8"
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
      "definition_site": "0044b730",
      "incomplete_value": true,
      "site": "0044b740",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b6f0",
      "incomplete_value": true,
      "site": "0044b700",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f24:8"
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
      "definition_site": "0044b730",
      "incomplete_value": true,
      "site": "0044b740",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b6f0",
      "incomplete_value": true,
      "site": "0044b700",
      "value": [
        "LOAD",
        "16",
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
      "0044b724",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ],
    [
      "0044b730",
      "READ",
      [
        "storage",
        "002b9f24",
        null,
        "string"
      ]
    ],
    [
      "0044b730",
      "READ",
      [
        "storage",
        "002b9f34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b724",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ],
    [
      "0044b730",
      "READ",
      [
        "storage",
        "002b9f64",
        null,
        "string"
      ]
    ],
    [
      "0044b730",
      "READ",
      [
        "storage",
        "002b9f74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md#insn-0044b6d4) · [`0044b6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md#insn-0044b6e4) · [`0044b6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md#insn-0044b6e8)
- 新版 [`0044b714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md#insn-0044b714) · [`0044b724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md#insn-0044b724)

~~~diff
- 0044b6d4 ["INT_ADD", "register:40f0:8", ["const:44b6d4:8", "const:4:8"]]
- 0044b6d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0044b714 ["INT_ADD", "register:40f0:8", ["const:44b714:8", "const:4:8"]]
+ 0044b714 ["CALL", null, ["callee:00c57e90:8"]]
- 0044b6d4 bytes ef302094
+ 0044b714 bytes df312094
- 0044b6e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:620:8"]]
- 0044b6e4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b6e4 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b6e4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:660:8"]]
+ 0044b724 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b724 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b724 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b6e4 bytes 0089c13d
+ 0044b724 bytes 0099c13d
- 0044b6e8 ["COPY", "register:4040:8", ["const:2b9000:8"]]
- 0044b6e8 bytes 68f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-692f332ad94bd4c2df86407b2c7a9c54"></a>

### [`0044b714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b714.md) → [`0044b754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b754.md) FUN_0044b754

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`005a7528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7528.md) [`005a8538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8538.md) [`005a9778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9778.md) [`005aaea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aaea0.md) [`005ac010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac010.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 7件 [`005a7568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7568.md) [`005a8578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8578.md) [`005a97b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97b8.md) [`005aaee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee0.md) [`005ac050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac050.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b77c",
      "incomplete_value": true,
      "site": "0044b788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b73c",
      "incomplete_value": true,
      "site": "0044b748",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc0:8"
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
      "definition_site": "0044b778",
      "incomplete_value": true,
      "site": "0044b78c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:7e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b738",
      "incomplete_value": true,
      "site": "0044b74c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:7a7:8"
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
      "definition_site": "0044b778",
      "incomplete_value": true,
      "site": "0044b78c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b738",
      "incomplete_value": true,
      "site": "0044b74c",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044b778",
      "READ",
      [
        "storage",
        "002af7a7",
        null,
        "string"
      ]
    ],
    [
      "0044b778",
      "READ",
      [
        "storage",
        "002af7b7",
        null,
        "string"
      ]
    ],
    [
      "0044b77c",
      "READ",
      [
        "storage",
        "002c2dc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044b778",
      "READ",
      [
        "storage",
        "002af7e7",
        null,
        "string"
      ]
    ],
    [
      "0044b778",
      "READ",
      [
        "storage",
        "002af7f7",
        null,
        "string"
      ]
    ],
    [
      "0044b77c",
      "READ",
      [
        "storage",
        "002c2e00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b714.md#insn-0044b728) · [`0044b730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b714.md#insn-0044b730) · [`0044b734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b714.md#insn-0044b734)
- 新版 [`0044b768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b754.md#insn-0044b768) · [`0044b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b754.md#insn-0044b770)

~~~diff
- 0044b728 ["INT_ADD", "register:40f0:8", ["const:44b728:8", "const:4:8"]]
- 0044b728 ["CALL", null, ["callee:00c57e90:8"]]
+ 0044b768 ["INT_ADD", "register:40f0:8", ["const:44b768:8", "const:4:8"]]
+ 0044b768 ["CALL", null, ["callee:00c57e90:8"]]
- 0044b728 bytes da302094
+ 0044b768 bytes ca312094
- 0044b730 ["COPY", "tmp:0:8", ["const:7a7:8"]]
- 0044b730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044b730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044b730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044b770 ["COPY", "tmp:0:8", ["const:7e7:8"]]
+ 0044b770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044b730 bytes 089d1e91
+ 0044b770 bytes 089d1f91
- 0044b734 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0044b734 bytes a9f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-960ce9230c4fcda0a77d3a14f2f93ba6"></a>

### [`0044b764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md) → [`0044b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md) FUN_0044b7a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0044b7c8",
      "incomplete_value": true,
      "site": "0044b7dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044b788",
      "incomplete_value": true,
      "site": "0044b79c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b7d4",
      "incomplete_value": true,
      "site": "0044b7e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b794",
      "incomplete_value": true,
      "site": "0044b7a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:858:8"
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
      "definition_site": "0044b7d4",
      "incomplete_value": true,
      "site": "0044b7e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b794",
      "incomplete_value": true,
      "site": "0044b7a0",
      "value": [
        "LOAD",
        "16",
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
      "0044b7c8",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "0044b7d4",
      "READ",
      [
        "storage",
        "002b3858",
        null,
        "string"
      ]
    ],
    [
      "0044b7d4",
      "READ",
      [
        "storage",
        "002b3868",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b7c8",
      "READ",
      [
        "storage",
        "002c32a0",
        null,
        null
      ]
    ],
    [
      "0044b7d4",
      "READ",
      [
        "storage",
        "002b3898",
        null,
        "string"
      ]
    ],
    [
      "0044b7d4",
      "READ",
      [
        "storage",
        "002b38a8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md#insn-0044b778) · [`0044b788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md#insn-0044b788) · [`0044b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md#insn-0044b78c)
- 新版 [`0044b7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md#insn-0044b7b8) · [`0044b7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md#insn-0044b7c8)

~~~diff
- 0044b778 ["INT_ADD", "register:40f0:8", ["const:44b778:8", "const:4:8"]]
- 0044b778 ["CALL", null, ["callee:00c57e90:8"]]
+ 0044b7b8 ["INT_ADD", "register:40f0:8", ["const:44b7b8:8", "const:4:8"]]
+ 0044b7b8 ["CALL", null, ["callee:00c57e90:8"]]
- 0044b778 bytes c6302094
+ 0044b7b8 bytes b6312094
- 0044b788 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
- 0044b788 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b788 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b788 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b7c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 0044b7c8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b7c8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b7c8 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b788 bytes 0099c03d
+ 0044b7c8 bytes 00a9c03d
- 0044b78c ["COPY", "register:4040:8", ["const:2b3000:8"]]
- 0044b78c bytes 48f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc3b5514109d710b63c7597e8cd1d03b"></a>

### [`0044b804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md) → [`0044b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md) FUN_0044b844

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b868",
      "incomplete_value": true,
      "site": "0044b880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044b828",
      "incomplete_value": true,
      "site": "0044b840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b834",
      "incomplete_value": true,
      "site": "0044b844",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dce:8"
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
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b884",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b834",
      "incomplete_value": true,
      "site": "0044b844",
      "value": [
        "LOAD",
        "16",
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
      "0044b868",
      "READ",
      [
        "storage",
        "002c2c70",
        null,
        null
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b5dce",
        null,
        "string"
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b5dde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b868",
      "READ",
      [
        "storage",
        "002c2cb0",
        null,
        null
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b5e0e",
        null,
        "string"
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b5e1e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md#insn-0044b818) · [`0044b828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md#insn-0044b828) · [`0044b82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md#insn-0044b82c)
- 新版 [`0044b858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md#insn-0044b858) · [`0044b868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md#insn-0044b868)

~~~diff
- 0044b818 ["INT_ADD", "register:40f0:8", ["const:44b818:8", "const:4:8"]]
- 0044b818 ["CALL", null, ["callee:00c57e90:8"]]
+ 0044b858 ["INT_ADD", "register:40f0:8", ["const:44b858:8", "const:4:8"]]
+ 0044b858 ["CALL", null, ["callee:00c57e90:8"]]
- 0044b818 bytes 9e302094
+ 0044b858 bytes 8e312094
- 0044b828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
- 0044b828 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b828 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b828 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 0044b868 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b868 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b868 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b828 bytes 001dc33d
+ 0044b868 bytes 002dc33d
- 0044b82c ["COPY", "register:4040:8", ["const:2b5000:8"]]
- 0044b82c bytes 48f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a281b97a2a03f245ee30b05176ceff"></a>

### [`0044b858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md) → [`0044b898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md) FUN_0044b898

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b8b4",
      "incomplete_value": false,
      "site": "0044b8cc",
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
            "const:e33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b874",
      "incomplete_value": false,
      "site": "0044b88c",
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
            "const:df3:8"
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
      "definition_site": "0044b8c0",
      "incomplete_value": false,
      "site": "0044b8cc",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b880",
      "incomplete_value": false,
      "site": "0044b88c",
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
            "const:668:8"
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
      "definition_site": "0044b8d4",
      "incomplete_value": false,
      "site": "0044b8dc",
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
            "const:605:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b894",
      "incomplete_value": false,
      "site": "0044b89c",
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
            "const:529:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044b8b4",
      "PARAM",
      [
        "storage",
        "002b5df3",
        null,
        "string"
      ]
    ],
    [
      "0044b8c0",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b8d4",
      "PARAM",
      [
        "storage",
        "002a7529",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b8b4",
      "PARAM",
      [
        "storage",
        "002b5e33",
        null,
        "string"
      ]
    ],
    [
      "0044b8c0",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b8d4",
      "PARAM",
      [
        "storage",
        "002a7605",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b88c) · [`0044b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b89c) · [`0044b874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md#insn-0044b874)
- 新版 [`0044b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8cc) · [`0044b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8dc) · [`0044b8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8b4)

~~~diff
- 0044b88c ["INT_ADD", "register:40f0:8", ["const:44b88c:8", "const:4:8"]]
- 0044b88c ["CALL", null, ["callee:00c580b0:8"]]
+ 0044b8cc ["INT_ADD", "register:40f0:8", ["const:44b8cc:8", "const:4:8"]]
+ 0044b8cc ["CALL", null, ["callee:00c580b0:8"]]
- 0044b88c bytes 09312094
+ 0044b8cc bytes f9312094
- 0044b89c ["INT_ADD", "register:40f0:8", ["const:44b89c:8", "const:4:8"]]
- 0044b89c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044b8dc ["INT_ADD", "register:40f0:8", ["const:44b8dc:8", "const:4:8"]]
+ 0044b8dc ["CALL", null, ["callee:00c57f70:8"]]
- 0044b89c bytes b5302094
+ 0044b8dc bytes a5312094
- 0044b874 ["COPY", "tmp:0:8", ["const:df3:8"]]
- 0044b874 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044b874 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044b874 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044b8b4 ["COPY", "tmp:0:8", ["const:e33:8"]]
+ 0044b8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044b874 bytes 00cc3791
+ 0044b8b4 bytes 00cc3891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10885f4501396e9fe7c55db14f3c230c"></a>

### [`0044b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md) → [`0044b958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md) FUN_0044b958

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b974",
      "incomplete_value": false,
      "site": "0044b98c",
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
            "const:414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b934",
      "incomplete_value": false,
      "site": "0044b94c",
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
            "const:338:8"
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
      "definition_site": "0044b980",
      "incomplete_value": false,
      "site": "0044b98c",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b940",
      "incomplete_value": false,
      "site": "0044b94c",
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
            "const:668:8"
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
      "definition_site": "0044b994",
      "incomplete_value": false,
      "site": "0044b99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:94f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b954",
      "incomplete_value": false,
      "site": "0044b95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:90f:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044b974",
      "PARAM",
      [
        "storage",
        "002a6338",
        null,
        "string"
      ]
    ],
    [
      "0044b980",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b994",
      "PARAM",
      [
        "storage",
        "002b090f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b974",
      "PARAM",
      [
        "storage",
        "002a6414",
        null,
        "string"
      ]
    ],
    [
      "0044b980",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b994",
      "PARAM",
      [
        "storage",
        "002b094f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b94c) · [`0044b95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b95c) · [`0044b934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md#insn-0044b934)
- 新版 [`0044b98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b98c) · [`0044b99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b99c) · [`0044b974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b974)

~~~diff
- 0044b94c ["INT_ADD", "register:40f0:8", ["const:44b94c:8", "const:4:8"]]
- 0044b94c ["CALL", null, ["callee:00c580b0:8"]]
+ 0044b98c ["INT_ADD", "register:40f0:8", ["const:44b98c:8", "const:4:8"]]
+ 0044b98c ["CALL", null, ["callee:00c580b0:8"]]
- 0044b94c bytes d9302094
+ 0044b98c bytes c9312094
- 0044b95c ["INT_ADD", "register:40f0:8", ["const:44b95c:8", "const:4:8"]]
- 0044b95c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044b99c ["INT_ADD", "register:40f0:8", ["const:44b99c:8", "const:4:8"]]
+ 0044b99c ["CALL", null, ["callee:00c57f70:8"]]
- 0044b95c bytes 85302094
+ 0044b99c bytes 75312094
- 0044b934 ["COPY", "tmp:0:8", ["const:338:8"]]
- 0044b934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044b934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044b934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044b974 ["COPY", "tmp:0:8", ["const:414:8"]]
+ 0044b974 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b974 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b974 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044b934 bytes 00e00c91
+ 0044b974 bytes 00501091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7a42f53fb584e33aa8ce28b56e88617"></a>

### [`0044b9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md) → [`0044ba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md) FUN_0044ba18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ba34",
      "incomplete_value": false,
      "site": "0044ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:95d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b9f4",
      "incomplete_value": false,
      "site": "0044ba0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:91d:8"
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
      "definition_site": "0044ba40",
      "incomplete_value": false,
      "site": "0044ba4c",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ba00",
      "incomplete_value": false,
      "site": "0044ba0c",
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
            "const:668:8"
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
      "definition_site": "0044ba54",
      "incomplete_value": false,
      "site": "0044ba5c",
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
            "const:35a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ba14",
      "incomplete_value": false,
      "site": "0044ba1c",
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
            "const:27e:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044ba34",
      "PARAM",
      [
        "storage",
        "002b091d",
        null,
        "string"
      ]
    ],
    [
      "0044ba40",
      "PARAM",
      [
        "storage",
        "00ca4668",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba54",
      "PARAM",
      [
        "storage",
        "002a527e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ba34",
      "PARAM",
      [
        "storage",
        "002b095d",
        null,
        "string"
      ]
    ],
    [
      "0044ba40",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba54",
      "PARAM",
      [
        "storage",
        "002a535a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044ba0c) · [`0044ba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044ba1c) · [`0044b9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md#insn-0044b9f4)
- 新版 [`0044ba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba4c) · [`0044ba5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba5c) · [`0044ba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba34)

~~~diff
- 0044ba0c ["INT_ADD", "register:40f0:8", ["const:44ba0c:8", "const:4:8"]]
- 0044ba0c ["CALL", null, ["callee:00c580b0:8"]]
+ 0044ba4c ["INT_ADD", "register:40f0:8", ["const:44ba4c:8", "const:4:8"]]
+ 0044ba4c ["CALL", null, ["callee:00c580b0:8"]]
- 0044ba0c bytes a9302094
+ 0044ba4c bytes 99312094
- 0044ba1c ["INT_ADD", "register:40f0:8", ["const:44ba1c:8", "const:4:8"]]
- 0044ba1c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ba5c ["INT_ADD", "register:40f0:8", ["const:44ba5c:8", "const:4:8"]]
+ 0044ba5c ["CALL", null, ["callee:00c57f70:8"]]
- 0044ba1c bytes 55302094
+ 0044ba5c bytes 45312094
- 0044b9f4 ["COPY", "tmp:0:8", ["const:91d:8"]]
- 0044b9f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044b9f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044b9f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044ba34 ["COPY", "tmp:0:8", ["const:95d:8"]]
+ 0044ba34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044ba34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044ba34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044b9f4 bytes 00742491
+ 0044ba34 bytes 00742591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2a6f87bd631619e8900ad81ea04a9f"></a>

### [`0044ba98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md) → [`0044bad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md) FUN_0044bad8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006a9724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a9/006a9724.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`006a9764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a9/006a9764.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bb00",
      "incomplete_value": true,
      "site": "0044bb10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bac0",
      "incomplete_value": true,
      "site": "0044bad0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044bb14",
      "incomplete_value": true,
      "site": "0044bb14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044bad4",
      "incomplete_value": true,
      "site": "0044bad4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bb20",
      "incomplete_value": false,
      "site": "0044bb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bae0",
      "incomplete_value": false,
      "site": "0044bae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044bb00",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bb08",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bb20",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bb00",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bb08",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bb20",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bae0) · [`0044bae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bae8) · [`0044bb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044ba98.md#insn-0044bb10)
- 新版 [`0044bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb20) · [`0044bb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb28) · [`0044bb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb50)

~~~diff
- 0044bae0 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044bae0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bae0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bae0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bb20 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044bb20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bb20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bb20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bae0 bytes 21243491
+ 0044bb20 bytes 21583791
- 0044bae8 ["INT_ADD", "register:40f0:8", ["const:44bae8:8", "const:4:8"]]
- 0044bae8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044bb28 ["INT_ADD", "register:40f0:8", ["const:44bb28:8", "const:4:8"]]
+ 0044bb28 ["CALL", null, ["callee:00c57f70:8"]]
- 0044bae8 bytes 22302094
+ 0044bb28 bytes 12312094
- 0044bb10 ["INT_ADD", "register:40f0:8", ["const:44bb10:8", "const:4:8"]]
- 0044bb10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044bb50 ["INT_ADD", "register:40f0:8", ["const:44bb50:8", "const:4:8"]]
+ 0044bb50 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044bb10 bytes e82f2094
+ 0044bb50 bytes d8302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fac5c4103f26eaec7406cb3d2a838a7a"></a>

### [`0044bbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md) → [`0044bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md) FUN_0044bbf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bc18",
      "incomplete_value": true,
      "site": "0044bc28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bbd8",
      "incomplete_value": true,
      "site": "0044bbe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044bc2c",
      "incomplete_value": true,
      "site": "0044bc2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044bbec",
      "incomplete_value": true,
      "site": "0044bbec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bc38",
      "incomplete_value": false,
      "site": "0044bc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bbf8",
      "incomplete_value": false,
      "site": "0044bc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044bc18",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bc20",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bc38",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bc18",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bc20",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bc38",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bbf8) · [`0044bc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bc00) · [`0044bc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bbb0.md#insn-0044bc28)
- 新版 [`0044bc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc38) · [`0044bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc40) · [`0044bc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc68)

~~~diff
- 0044bbf8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044bbf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bbf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bbf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bc38 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044bc38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bc38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bc38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bbf8 bytes 21243491
+ 0044bc38 bytes 21583791
- 0044bc00 ["INT_ADD", "register:40f0:8", ["const:44bc00:8", "const:4:8"]]
- 0044bc00 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044bc40 ["INT_ADD", "register:40f0:8", ["const:44bc40:8", "const:4:8"]]
+ 0044bc40 ["CALL", null, ["callee:00c57f70:8"]]
- 0044bc00 bytes dc2f2094
+ 0044bc40 bytes cc302094
- 0044bc28 ["INT_ADD", "register:40f0:8", ["const:44bc28:8", "const:4:8"]]
- 0044bc28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044bc68 ["INT_ADD", "register:40f0:8", ["const:44bc68:8", "const:4:8"]]
+ 0044bc68 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044bc28 bytes a22f2094
+ 0044bc68 bytes 92302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002eb6f4790c0a4705ffaff66aa068a1"></a>

### [`0044bcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md) → [`0044bd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md) FUN_0044bd08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bd34",
      "incomplete_value": true,
      "site": "0044bd48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bcf4",
      "incomplete_value": true,
      "site": "0044bd08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044bd4c",
      "incomplete_value": true,
      "site": "0044bd4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044bd0c",
      "incomplete_value": true,
      "site": "0044bd0c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bd58",
      "incomplete_value": false,
      "site": "0044bd60",
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
            "const:dea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bd18",
      "incomplete_value": false,
      "site": "0044bd20",
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
            "const:daa:8"
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
      "0044bd34",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bd40",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bd58",
      "PARAM",
      [
        "storage",
        "002b5daa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bd34",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bd40",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bd58",
      "PARAM",
      [
        "storage",
        "002b5dea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bd18) · [`0044bd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bd20) · [`0044bd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bcc8.md#insn-0044bd48)
- 新版 [`0044bd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd58) · [`0044bd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd60) · [`0044bd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd88)

~~~diff
- 0044bd18 ["COPY", "tmp:0:8", ["const:daa:8"]]
- 0044bd18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bd18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bd18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bd58 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 0044bd58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bd58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bd58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bd18 bytes 21a83691
+ 0044bd58 bytes 21a83791
- 0044bd20 ["INT_ADD", "register:40f0:8", ["const:44bd20:8", "const:4:8"]]
- 0044bd20 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044bd60 ["INT_ADD", "register:40f0:8", ["const:44bd60:8", "const:4:8"]]
+ 0044bd60 ["CALL", null, ["callee:00c57f70:8"]]
- 0044bd20 bytes 942f2094
+ 0044bd60 bytes 84302094
- 0044bd48 ["INT_ADD", "register:40f0:8", ["const:44bd48:8", "const:4:8"]]
- 0044bd48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044bd88 ["INT_ADD", "register:40f0:8", ["const:44bd88:8", "const:4:8"]]
+ 0044bd88 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044bd48 bytes 5a2f2094
+ 0044bd88 bytes 4a302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b27ffcc44c3326b6b1cef9c9bf85b49"></a>

### [`0044bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md) → [`0044bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md) FUN_0044bf14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bf3c",
      "incomplete_value": true,
      "site": "0044bf4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044befc",
      "incomplete_value": true,
      "site": "0044bf0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044bf50",
      "incomplete_value": true,
      "site": "0044bf50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044bf10",
      "incomplete_value": true,
      "site": "0044bf10",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bf5c",
      "incomplete_value": false,
      "site": "0044bf64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bf1c",
      "incomplete_value": false,
      "site": "0044bf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044bf3c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044bf44",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044bf5c",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bf3c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bf44",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bf5c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044bf1c) · [`0044bf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044bf24) · [`0044bf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md#insn-0044bf4c)
- 新版 [`0044bf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf5c) · [`0044bf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf64) · [`0044bf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf8c)

~~~diff
- 0044bf1c ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044bf1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bf1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bf1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bf5c ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044bf5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bf5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bf5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bf1c bytes 21243491
+ 0044bf5c bytes 21583791
- 0044bf24 ["INT_ADD", "register:40f0:8", ["const:44bf24:8", "const:4:8"]]
- 0044bf24 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044bf64 ["INT_ADD", "register:40f0:8", ["const:44bf64:8", "const:4:8"]]
+ 0044bf64 ["CALL", null, ["callee:00c57f70:8"]]
- 0044bf24 bytes 132f2094
+ 0044bf64 bytes 03302094
- 0044bf4c ["INT_ADD", "register:40f0:8", ["const:44bf4c:8", "const:4:8"]]
- 0044bf4c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044bf8c ["INT_ADD", "register:40f0:8", ["const:44bf8c:8", "const:4:8"]]
+ 0044bf8c ["CALL", null, ["callee:00c57eb0:8"]]
- 0044bf4c bytes d92e2094
+ 0044bf8c bytes c92f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd3100d5cb22bc2e13d3a6011fb88090"></a>

### [`0044bfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md) → [`0044c02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md) FUN_0044c02c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c054",
      "incomplete_value": true,
      "site": "0044c064",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c014",
      "incomplete_value": true,
      "site": "0044c024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c068",
      "incomplete_value": true,
      "site": "0044c068",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c028",
      "incomplete_value": true,
      "site": "0044c028",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c074",
      "incomplete_value": false,
      "site": "0044c07c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c034",
      "incomplete_value": false,
      "site": "0044c03c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c054",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c05c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c074",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c054",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c05c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c074",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c034) · [`0044c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c03c) · [`0044c064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md#insn-0044c064)
- 新版 [`0044c074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c074) · [`0044c07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c07c) · [`0044c0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c0a4)

~~~diff
- 0044c034 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c034 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c034 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c034 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c074 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c034 bytes 21243491
+ 0044c074 bytes 21583791
- 0044c03c ["INT_ADD", "register:40f0:8", ["const:44c03c:8", "const:4:8"]]
- 0044c03c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c07c ["INT_ADD", "register:40f0:8", ["const:44c07c:8", "const:4:8"]]
+ 0044c07c ["CALL", null, ["callee:00c57f70:8"]]
- 0044c03c bytes cd2e2094
+ 0044c07c bytes bd2f2094
- 0044c064 ["INT_ADD", "register:40f0:8", ["const:44c064:8", "const:4:8"]]
- 0044c064 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c0a4 ["INT_ADD", "register:40f0:8", ["const:44c0a4:8", "const:4:8"]]
+ 0044c0a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c064 bytes 932e2094
+ 0044c0a4 bytes 832f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde74212f4bb2a3de6348c93c4c3dd0f"></a>

### [`0044c104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md) → [`0044c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md) FUN_0044c144

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c16c",
      "incomplete_value": true,
      "site": "0044c17c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c12c",
      "incomplete_value": true,
      "site": "0044c13c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c180",
      "incomplete_value": true,
      "site": "0044c180",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c140",
      "incomplete_value": true,
      "site": "0044c140",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c18c",
      "incomplete_value": false,
      "site": "0044c194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c14c",
      "incomplete_value": false,
      "site": "0044c154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c16c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c174",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c18c",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c16c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c174",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c18c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c14c) · [`0044c154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c154) · [`0044c17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c104.md#insn-0044c17c)
- 新版 [`0044c18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c18c) · [`0044c194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c194) · [`0044c1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c1bc)

~~~diff
- 0044c14c ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c14c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c14c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c14c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c18c ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c18c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c18c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c18c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c14c bytes 21243491
+ 0044c18c bytes 21583791
- 0044c154 ["INT_ADD", "register:40f0:8", ["const:44c154:8", "const:4:8"]]
- 0044c154 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c194 ["INT_ADD", "register:40f0:8", ["const:44c194:8", "const:4:8"]]
+ 0044c194 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c154 bytes 872e2094
+ 0044c194 bytes 772f2094
- 0044c17c ["INT_ADD", "register:40f0:8", ["const:44c17c:8", "const:4:8"]]
- 0044c17c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c1bc ["INT_ADD", "register:40f0:8", ["const:44c1bc:8", "const:4:8"]]
+ 0044c1bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c17c bytes 4d2e2094
+ 0044c1bc bytes 3d2f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bacbe4d9a94210a60269c3cf92b0fad7"></a>

### [`0044c21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md) → [`0044c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md) FUN_0044c25c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c284",
      "incomplete_value": true,
      "site": "0044c294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c244",
      "incomplete_value": true,
      "site": "0044c254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c298",
      "incomplete_value": true,
      "site": "0044c298",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c258",
      "incomplete_value": true,
      "site": "0044c258",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c2a4",
      "incomplete_value": false,
      "site": "0044c2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c264",
      "incomplete_value": false,
      "site": "0044c26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c284",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c28c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c2a4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c284",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c28c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c2a4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c264) · [`0044c26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c26c) · [`0044c294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c21c.md#insn-0044c294)
- 新版 [`0044c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2a4) · [`0044c2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2ac) · [`0044c2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2d4)

~~~diff
- 0044c264 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c264 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c264 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c264 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c2a4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c2a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c2a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c2a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c264 bytes 21243491
+ 0044c2a4 bytes 21583791
- 0044c26c ["INT_ADD", "register:40f0:8", ["const:44c26c:8", "const:4:8"]]
- 0044c26c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c2ac ["INT_ADD", "register:40f0:8", ["const:44c2ac:8", "const:4:8"]]
+ 0044c2ac ["CALL", null, ["callee:00c57f70:8"]]
- 0044c26c bytes 412e2094
+ 0044c2ac bytes 312f2094
- 0044c294 ["INT_ADD", "register:40f0:8", ["const:44c294:8", "const:4:8"]]
- 0044c294 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c2d4 ["INT_ADD", "register:40f0:8", ["const:44c2d4:8", "const:4:8"]]
+ 0044c2d4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c294 bytes 072e2094
+ 0044c2d4 bytes f72e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b320f96d3cac0351dd92e6212ed606a"></a>

### [`0044c334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c334.md) → [`0044c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md) FUN_0044c374

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c39c",
      "incomplete_value": true,
      "site": "0044c3ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c35c",
      "incomplete_value": true,
      "site": "0044c36c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c3b0",
      "incomplete_value": true,
      "site": "0044c3b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c370",
      "incomplete_value": true,
      "site": "0044c370",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c3bc",
      "incomplete_value": false,
      "site": "0044c3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c37c",
      "incomplete_value": false,
      "site": "0044c384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c39c",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c3a4",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c3bc",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c39c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c3a4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c3bc",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c334.md#insn-0044c37c) · [`0044c384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c334.md#insn-0044c384) · [`0044c3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c334.md#insn-0044c3ac)
- 新版 [`0044c3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3bc) · [`0044c3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3c4) · [`0044c3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3ec)

~~~diff
- 0044c37c ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c37c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c37c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c37c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c3bc ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c37c bytes 21243491
+ 0044c3bc bytes 21583791
- 0044c384 ["INT_ADD", "register:40f0:8", ["const:44c384:8", "const:4:8"]]
- 0044c384 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c3c4 ["INT_ADD", "register:40f0:8", ["const:44c3c4:8", "const:4:8"]]
+ 0044c3c4 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c384 bytes fb2d2094
+ 0044c3c4 bytes eb2e2094
- 0044c3ac ["INT_ADD", "register:40f0:8", ["const:44c3ac:8", "const:4:8"]]
- 0044c3ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c3ec ["INT_ADD", "register:40f0:8", ["const:44c3ec:8", "const:4:8"]]
+ 0044c3ec ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c3ac bytes c12d2094
+ 0044c3ec bytes b12e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435a8ae5c06f1d61ce2f0660106fb5bf"></a>

### [`0044c44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c44c.md) → [`0044c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md) FUN_0044c48c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007aecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007aed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c4b4",
      "incomplete_value": true,
      "site": "0044c4c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c474",
      "incomplete_value": true,
      "site": "0044c484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c4c8",
      "incomplete_value": true,
      "site": "0044c4c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c488",
      "incomplete_value": true,
      "site": "0044c488",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c4d4",
      "incomplete_value": false,
      "site": "0044c4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c494",
      "incomplete_value": false,
      "site": "0044c49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c4b4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c4bc",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c4d4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c4b4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c4bc",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c4d4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c44c.md#insn-0044c494) · [`0044c49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c44c.md#insn-0044c49c) · [`0044c4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c44c.md#insn-0044c4c4)
- 新版 [`0044c4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c4d4) · [`0044c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c4dc) · [`0044c504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c504)

~~~diff
- 0044c494 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c494 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c494 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c494 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c4d4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c4d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c4d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c4d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c494 bytes 21243491
+ 0044c4d4 bytes 21583791
- 0044c49c ["INT_ADD", "register:40f0:8", ["const:44c49c:8", "const:4:8"]]
- 0044c49c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c4dc ["INT_ADD", "register:40f0:8", ["const:44c4dc:8", "const:4:8"]]
+ 0044c4dc ["CALL", null, ["callee:00c57f70:8"]]
- 0044c49c bytes b52d2094
+ 0044c4dc bytes a52e2094
- 0044c4c4 ["INT_ADD", "register:40f0:8", ["const:44c4c4:8", "const:4:8"]]
- 0044c4c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c504 ["INT_ADD", "register:40f0:8", ["const:44c504:8", "const:4:8"]]
+ 0044c504 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c4c4 bytes 7b2d2094
+ 0044c504 bytes 6b2e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-424741dc6209e69488212a86ae7de254"></a>

### [`0044c564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md) → [`0044c5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md) FUN_0044c5a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00814bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/00814bb8.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`00814bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814bf8.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c5cc",
      "incomplete_value": true,
      "site": "0044c5dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c58c",
      "incomplete_value": true,
      "site": "0044c59c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c5e0",
      "incomplete_value": true,
      "site": "0044c5e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c5a0",
      "incomplete_value": true,
      "site": "0044c5a0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c5ec",
      "incomplete_value": false,
      "site": "0044c5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c5ac",
      "incomplete_value": false,
      "site": "0044c5b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c5cc",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c5d4",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c5ec",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c5cc",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c5d4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c5ec",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c5ac) · [`0044c5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c5b4) · [`0044c5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c564.md#insn-0044c5dc)
- 新版 [`0044c5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c5ec) · [`0044c5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c5f4) · [`0044c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c61c)

~~~diff
- 0044c5ac ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c5ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c5ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c5ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c5ec ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c5ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c5ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c5ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c5ac bytes 21243491
+ 0044c5ec bytes 21583791
- 0044c5b4 ["INT_ADD", "register:40f0:8", ["const:44c5b4:8", "const:4:8"]]
- 0044c5b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c5f4 ["INT_ADD", "register:40f0:8", ["const:44c5f4:8", "const:4:8"]]
+ 0044c5f4 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c5b4 bytes 6f2d2094
+ 0044c5f4 bytes 5f2e2094
- 0044c5dc ["INT_ADD", "register:40f0:8", ["const:44c5dc:8", "const:4:8"]]
- 0044c5dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c61c ["INT_ADD", "register:40f0:8", ["const:44c61c:8", "const:4:8"]]
+ 0044c61c ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c5dc bytes 352d2094
+ 0044c61c bytes 252e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2b6a88d152761d897276935fe422f9"></a>

### [`0044c67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md) → [`0044c6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md) FUN_0044c6bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c6e4",
      "incomplete_value": true,
      "site": "0044c6f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c6a4",
      "incomplete_value": true,
      "site": "0044c6b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c6f8",
      "incomplete_value": true,
      "site": "0044c6f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c6b8",
      "incomplete_value": true,
      "site": "0044c6b8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c704",
      "incomplete_value": false,
      "site": "0044c70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c6c4",
      "incomplete_value": false,
      "site": "0044c6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c6e4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c6ec",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c704",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c6e4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c6ec",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c704",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c6c4) · [`0044c6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c6cc) · [`0044c6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c67c.md#insn-0044c6f4)
- 新版 [`0044c704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c704) · [`0044c70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c70c) · [`0044c734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c734)

~~~diff
- 0044c6c4 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c6c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c6c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c6c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c704 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c6c4 bytes 21243491
+ 0044c704 bytes 21583791
- 0044c6cc ["INT_ADD", "register:40f0:8", ["const:44c6cc:8", "const:4:8"]]
- 0044c6cc ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c70c ["INT_ADD", "register:40f0:8", ["const:44c70c:8", "const:4:8"]]
+ 0044c70c ["CALL", null, ["callee:00c57f70:8"]]
- 0044c6cc bytes 292d2094
+ 0044c70c bytes 192e2094
- 0044c6f4 ["INT_ADD", "register:40f0:8", ["const:44c6f4:8", "const:4:8"]]
- 0044c6f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c734 ["INT_ADD", "register:40f0:8", ["const:44c734:8", "const:4:8"]]
+ 0044c734 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c6f4 bytes ef2c2094
+ 0044c734 bytes df2d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839ac9e66081b7bb4efa9233b23cee32"></a>

### [`0044c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md) → [`0044c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md) FUN_0044c7d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) · 呼出先 4件 [`0044b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b214.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) · 呼出先 4件 [`0044b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b254.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c800",
      "incomplete_value": false,
      "site": "0044c808",
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
            "const:f7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c7c0",
      "incomplete_value": false,
      "site": "0044c7c8",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044c800",
      "PARAM",
      [
        "storage",
        "002b7f3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c800",
      "PARAM",
      [
        "storage",
        "002b7f7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7c8) · [`0044c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7b8) · [`0044c7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md#insn-0044c7c0)
- 新版 [`0044c808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c808) · [`0044c7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c7f8) · [`0044c800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c800)

~~~diff
- 0044c7c8 ["INT_ADD", "register:40f0:8", ["const:44c7c8:8", "const:4:8"]]
- 0044c7c8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c808 ["INT_ADD", "register:40f0:8", ["const:44c808:8", "const:4:8"]]
+ 0044c808 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c7c8 bytes ea2c2094
+ 0044c808 bytes da2d2094
- 0044c7b8 ["INT_ADD", "register:40f0:8", ["const:44c7b8:8", "const:4:8"]]
- 0044c7b8 ["CALL", null, ["callee:0044b254:8"]]
+ 0044c7f8 ["INT_ADD", "register:40f0:8", ["const:44c7f8:8", "const:4:8"]]
+ 0044c7f8 ["CALL", null, ["callee:0044b254:8"]]
- 0044c7b8 bytes 97faff97
+ 0044c7f8 bytes 97faff97
- 0044c7c0 ["COPY", "tmp:0:8", ["const:f3e:8"]]
- 0044c7c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c7c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c7c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c800 ["COPY", "tmp:0:8", ["const:f7e:8"]]
+ 0044c800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c7c0 bytes 21f83c91
+ 0044c800 bytes 21f83d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c724159a7718c4570da6e46463e3a173"></a>

### [`0044c844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md) → [`0044c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md) FUN_0044c884

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`008cb434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c8ac",
      "incomplete_value": true,
      "site": "0044c8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c86c",
      "incomplete_value": true,
      "site": "0044c87c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c8c0",
      "incomplete_value": true,
      "site": "0044c8c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c880",
      "incomplete_value": true,
      "site": "0044c880",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c8cc",
      "incomplete_value": false,
      "site": "0044c8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c88c",
      "incomplete_value": false,
      "site": "0044c894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c8ac",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c8b4",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c8cc",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c8ac",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c8b4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c8cc",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c88c) · [`0044c894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c894) · [`0044c8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c844.md#insn-0044c8bc)
- 新版 [`0044c8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8cc) · [`0044c8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8d4) · [`0044c8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8fc)

~~~diff
- 0044c88c ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c88c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c88c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c88c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c8cc ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c88c bytes 21243491
+ 0044c8cc bytes 21583791
- 0044c894 ["INT_ADD", "register:40f0:8", ["const:44c894:8", "const:4:8"]]
- 0044c894 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c8d4 ["INT_ADD", "register:40f0:8", ["const:44c8d4:8", "const:4:8"]]
+ 0044c8d4 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c894 bytes b72c2094
+ 0044c8d4 bytes a72d2094
- 0044c8bc ["INT_ADD", "register:40f0:8", ["const:44c8bc:8", "const:4:8"]]
- 0044c8bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044c8fc ["INT_ADD", "register:40f0:8", ["const:44c8fc:8", "const:4:8"]]
+ 0044c8fc ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c8bc bytes 7d2c2094
+ 0044c8fc bytes 6d2d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5459e5efe2c5708083b880107c2aa4f0"></a>

### [`0044c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md) → [`0044c99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md) FUN_0044c99c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e01c.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00a3e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e214.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c9c8",
      "incomplete_value": true,
      "site": "0044c9dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c988",
      "incomplete_value": true,
      "site": "0044c99c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044c9e0",
      "incomplete_value": true,
      "site": "0044c9e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044c9a0",
      "incomplete_value": true,
      "site": "0044c9a0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c9ec",
      "incomplete_value": false,
      "site": "0044c9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c9ac",
      "incomplete_value": false,
      "site": "0044c9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044c9c8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044c9d4",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044c9ec",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c9c8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c9d4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c9ec",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044c9ac) · [`0044c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044c9b4) · [`0044c9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c95c.md#insn-0044c9dc)
- 新版 [`0044c9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044c9ec) · [`0044c9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044c9f4) · [`0044ca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044ca1c)

~~~diff
- 0044c9ac ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044c9ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c9ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c9ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c9ec ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044c9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c9ac bytes 21243491
+ 0044c9ec bytes 21583791
- 0044c9b4 ["INT_ADD", "register:40f0:8", ["const:44c9b4:8", "const:4:8"]]
- 0044c9b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044c9f4 ["INT_ADD", "register:40f0:8", ["const:44c9f4:8", "const:4:8"]]
+ 0044c9f4 ["CALL", null, ["callee:00c57f70:8"]]
- 0044c9b4 bytes 6f2c2094
+ 0044c9f4 bytes 5f2d2094
- 0044c9dc ["INT_ADD", "register:40f0:8", ["const:44c9dc:8", "const:4:8"]]
- 0044c9dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ca1c ["INT_ADD", "register:40f0:8", ["const:44ca1c:8", "const:4:8"]]
+ 0044ca1c ["CALL", null, ["callee:00c57eb0:8"]]
- 0044c9dc bytes 352c2094
+ 0044ca1c bytes 252d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ab66fb72e6c185356c4fab212f13d86"></a>

### [`0044cb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md) → [`0044cba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md) FUN_0044cba8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e01c.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00a3e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e214.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cbd4",
      "incomplete_value": true,
      "site": "0044cbe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cb94",
      "incomplete_value": true,
      "site": "0044cba8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044cbec",
      "incomplete_value": true,
      "site": "0044cbec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044cbac",
      "incomplete_value": true,
      "site": "0044cbac",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044cbf8",
      "incomplete_value": false,
      "site": "0044cc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cbb8",
      "incomplete_value": false,
      "site": "0044cbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044cbd4",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cbe0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044cbf8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cbd4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044cbe0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044cbf8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044cbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cbb8) · [`0044cbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cbc0) · [`0044cbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cb68.md#insn-0044cbe8)
- 新版 [`0044cbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cbf8) · [`0044cc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cc00) · [`0044cc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cc28)

~~~diff
- 0044cbb8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044cbb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044cbb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044cbb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044cbf8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044cbf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044cbf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044cbf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044cbb8 bytes 21243491
+ 0044cbf8 bytes 21583791
- 0044cbc0 ["INT_ADD", "register:40f0:8", ["const:44cbc0:8", "const:4:8"]]
- 0044cbc0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044cc00 ["INT_ADD", "register:40f0:8", ["const:44cc00:8", "const:4:8"]]
+ 0044cc00 ["CALL", null, ["callee:00c57f70:8"]]
- 0044cbc0 bytes ec2b2094
+ 0044cc00 bytes dc2c2094
- 0044cbe8 ["INT_ADD", "register:40f0:8", ["const:44cbe8:8", "const:4:8"]]
- 0044cbe8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044cc28 ["INT_ADD", "register:40f0:8", ["const:44cc28:8", "const:4:8"]]
+ 0044cc28 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044cbe8 bytes b22b2094
+ 0044cc28 bytes a22c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa1cafde829bc37527eb1deaf35ea3bd"></a>

### [`0044cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md) → [`0044cdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md) FUN_0044cdb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`008fed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fed30.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cde0",
      "incomplete_value": true,
      "site": "0044cdf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cda0",
      "incomplete_value": true,
      "site": "0044cdb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044cdf8",
      "incomplete_value": true,
      "site": "0044cdf8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044cdb8",
      "incomplete_value": true,
      "site": "0044cdb8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ce04",
      "incomplete_value": false,
      "site": "0044ce0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cdc4",
      "incomplete_value": false,
      "site": "0044cdcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044cde0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cdec",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ce04",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cde0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044cdec",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ce04",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044cdc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044cdc4) · [`0044cdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044cdcc) · [`0044cdf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cd74.md#insn-0044cdf4)
- 新版 [`0044ce04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce04) · [`0044ce0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce0c) · [`0044ce34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce34)

~~~diff
- 0044cdc4 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044cdc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044cdc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044cdc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ce04 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044ce04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ce04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ce04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044cdc4 bytes 21243491
+ 0044ce04 bytes 21583791
- 0044cdcc ["INT_ADD", "register:40f0:8", ["const:44cdcc:8", "const:4:8"]]
- 0044cdcc ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ce0c ["INT_ADD", "register:40f0:8", ["const:44ce0c:8", "const:4:8"]]
+ 0044ce0c ["CALL", null, ["callee:00c57f70:8"]]
- 0044cdcc bytes 692b2094
+ 0044ce0c bytes 592c2094
- 0044cdf4 ["INT_ADD", "register:40f0:8", ["const:44cdf4:8", "const:4:8"]]
- 0044cdf4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ce34 ["INT_ADD", "register:40f0:8", ["const:44ce34:8", "const:4:8"]]
+ 0044ce34 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044cdf4 bytes 2f2b2094
+ 0044ce34 bytes 1f2c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c6deebc65f5af96f7c5fa6b5fdde3ce"></a>

### [`0044cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md) → [`0044cfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md) FUN_0044cfc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`008fed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fed30.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cfec",
      "incomplete_value": true,
      "site": "0044d000",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cfac",
      "incomplete_value": true,
      "site": "0044cfc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d004",
      "incomplete_value": true,
      "site": "0044d004",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044cfc4",
      "incomplete_value": true,
      "site": "0044cfc4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d010",
      "incomplete_value": false,
      "site": "0044d018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cfd0",
      "incomplete_value": false,
      "site": "0044cfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044cfec",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044cff8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d010",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cfec",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044cff8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d010",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044cfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044cfd0) · [`0044cfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044cfd8) · [`0044d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044cf80.md#insn-0044d000)
- 新版 [`0044d010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d010) · [`0044d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d018) · [`0044d040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d040)

~~~diff
- 0044cfd0 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044cfd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044cfd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044cfd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d010 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044cfd0 bytes 21243491
+ 0044d010 bytes 21583791
- 0044cfd8 ["INT_ADD", "register:40f0:8", ["const:44cfd8:8", "const:4:8"]]
- 0044cfd8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d018 ["INT_ADD", "register:40f0:8", ["const:44d018:8", "const:4:8"]]
+ 0044d018 ["CALL", null, ["callee:00c57f70:8"]]
- 0044cfd8 bytes e62a2094
+ 0044d018 bytes d62b2094
- 0044d000 ["INT_ADD", "register:40f0:8", ["const:44d000:8", "const:4:8"]]
- 0044d000 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d040 ["INT_ADD", "register:40f0:8", ["const:44d040:8", "const:4:8"]]
+ 0044d040 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d000 bytes ac2a2094
+ 0044d040 bytes 9c2b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb9f45126879c5b189b175ec2ed954f4"></a>

### [`0044d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md) → [`0044d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md) FUN_0044d1cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0091a0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a0f8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`0091a294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091a294.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d204",
      "incomplete_value": true,
      "site": "0044d218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d1c4",
      "incomplete_value": true,
      "site": "0044d1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d21c",
      "incomplete_value": true,
      "site": "0044d21c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d1dc",
      "incomplete_value": true,
      "site": "0044d1dc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d224",
      "incomplete_value": false,
      "site": "0044d22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d1e4",
      "incomplete_value": false,
      "site": "0044d1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d204",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d208",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d224",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d204",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d208",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d224",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d1e4) · [`0044d1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d1ec) · [`0044d21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d18c.md#insn-0044d21c)
- 新版 [`0044d224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d224) · [`0044d22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d22c) · [`0044d25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d25c)

~~~diff
- 0044d1e4 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d1e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d1e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d1e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d224 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d1e4 bytes 21243491
+ 0044d224 bytes 21583791
- 0044d1ec ["INT_ADD", "register:40f0:8", ["const:44d1ec:8", "const:4:8"]]
- 0044d1ec ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d22c ["INT_ADD", "register:40f0:8", ["const:44d22c:8", "const:4:8"]]
+ 0044d22c ["CALL", null, ["callee:00c57f70:8"]]
- 0044d1ec bytes 612a2094
+ 0044d22c bytes 512b2094
- 0044d21c ["COPY", "tmp:0:8", ["const:dac:8"]]
- 0044d21c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d21c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d21c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d25c ["COPY", "tmp:0:8", ["const:dec:8"]]
+ 0044d25c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d25c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d25c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d21c bytes 21b03691
+ 0044d25c bytes 21b03791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-621ebc5e87671cc6639bd3dd0e9b2a80"></a>

### [`0044d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md) → [`0044d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md) FUN_0044d4c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d4e8",
      "incomplete_value": true,
      "site": "0044d4f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d4a8",
      "incomplete_value": true,
      "site": "0044d4b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d4fc",
      "incomplete_value": true,
      "site": "0044d4fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d4bc",
      "incomplete_value": true,
      "site": "0044d4bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d508",
      "incomplete_value": false,
      "site": "0044d510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d4c8",
      "incomplete_value": false,
      "site": "0044d4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d4e8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d4f0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d508",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d4e8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d4f0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d508",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d4c8) · [`0044d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d4d0) · [`0044d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d480.md#insn-0044d4f8)
- 新版 [`0044d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d508) · [`0044d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d510) · [`0044d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d538)

~~~diff
- 0044d4c8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d4c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d4c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d4c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d508 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d4c8 bytes 21243491
+ 0044d508 bytes 21583791
- 0044d4d0 ["INT_ADD", "register:40f0:8", ["const:44d4d0:8", "const:4:8"]]
- 0044d4d0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d510 ["INT_ADD", "register:40f0:8", ["const:44d510:8", "const:4:8"]]
+ 0044d510 ["CALL", null, ["callee:00c57f70:8"]]
- 0044d4d0 bytes a8292094
+ 0044d510 bytes 982a2094
- 0044d4f8 ["INT_ADD", "register:40f0:8", ["const:44d4f8:8", "const:4:8"]]
- 0044d4f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d538 ["INT_ADD", "register:40f0:8", ["const:44d538:8", "const:4:8"]]
+ 0044d538 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d4f8 bytes 6e292094
+ 0044d538 bytes 5e2a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7a328f53d7f7d7d83b6fd8a9f4b5c75"></a>

### [`0044d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md) → [`0044d5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md) FUN_0044d5d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d600",
      "incomplete_value": true,
      "site": "0044d610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d5c0",
      "incomplete_value": true,
      "site": "0044d5d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d614",
      "incomplete_value": true,
      "site": "0044d614",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d5d4",
      "incomplete_value": true,
      "site": "0044d5d4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d620",
      "incomplete_value": false,
      "site": "0044d628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d5e0",
      "incomplete_value": false,
      "site": "0044d5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d600",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d608",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d620",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d600",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d608",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d620",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d5e0) · [`0044d5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d5e8) · [`0044d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d598.md#insn-0044d610)
- 新版 [`0044d620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d620) · [`0044d628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d628) · [`0044d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d650)

~~~diff
- 0044d5e0 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d5e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d5e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d5e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d620 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d620 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d620 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d620 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d5e0 bytes 21243491
+ 0044d620 bytes 21583791
- 0044d5e8 ["INT_ADD", "register:40f0:8", ["const:44d5e8:8", "const:4:8"]]
- 0044d5e8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d628 ["INT_ADD", "register:40f0:8", ["const:44d628:8", "const:4:8"]]
+ 0044d628 ["CALL", null, ["callee:00c57f70:8"]]
- 0044d5e8 bytes 62292094
+ 0044d628 bytes 522a2094
- 0044d610 ["INT_ADD", "register:40f0:8", ["const:44d610:8", "const:4:8"]]
- 0044d610 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d650 ["INT_ADD", "register:40f0:8", ["const:44d650:8", "const:4:8"]]
+ 0044d650 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d610 bytes 28292094
+ 0044d650 bytes 182a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c37d97540a98ca6954588264f6ea6e16"></a>

### [`0044d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d6b0.md) → [`0044d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md) FUN_0044d6f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d718",
      "incomplete_value": true,
      "site": "0044d728",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d6d8",
      "incomplete_value": true,
      "site": "0044d6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d72c",
      "incomplete_value": true,
      "site": "0044d72c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d6ec",
      "incomplete_value": true,
      "site": "0044d6ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d738",
      "incomplete_value": false,
      "site": "0044d740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d6f8",
      "incomplete_value": false,
      "site": "0044d700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d718",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d720",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d738",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d718",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d720",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d738",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d6b0.md#insn-0044d6f8) · [`0044d700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d6b0.md#insn-0044d700) · [`0044d728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d6b0.md#insn-0044d728)
- 新版 [`0044d738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d738) · [`0044d740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d740) · [`0044d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d768)

~~~diff
- 0044d6f8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d6f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d6f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d6f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d738 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d738 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d738 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d738 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d6f8 bytes 21243491
+ 0044d738 bytes 21583791
- 0044d700 ["INT_ADD", "register:40f0:8", ["const:44d700:8", "const:4:8"]]
- 0044d700 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d740 ["INT_ADD", "register:40f0:8", ["const:44d740:8", "const:4:8"]]
+ 0044d740 ["CALL", null, ["callee:00c57f70:8"]]
- 0044d700 bytes 1c292094
+ 0044d740 bytes 0c2a2094
- 0044d728 ["INT_ADD", "register:40f0:8", ["const:44d728:8", "const:4:8"]]
- 0044d728 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d768 ["INT_ADD", "register:40f0:8", ["const:44d768:8", "const:4:8"]]
+ 0044d768 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d728 bytes e2282094
+ 0044d768 bytes d2292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a666e85391adbecf73b19dda0478eb0f"></a>

### [`0044d7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md) → [`0044d808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md) FUN_0044d808

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d830",
      "incomplete_value": true,
      "site": "0044d840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d7f0",
      "incomplete_value": true,
      "site": "0044d800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d844",
      "incomplete_value": true,
      "site": "0044d844",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d804",
      "incomplete_value": true,
      "site": "0044d804",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d850",
      "incomplete_value": false,
      "site": "0044d858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d810",
      "incomplete_value": false,
      "site": "0044d818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d830",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d838",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d850",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d830",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d838",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d850",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d810) · [`0044d818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d818) · [`0044d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d7c8.md#insn-0044d840)
- 新版 [`0044d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d850) · [`0044d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d858) · [`0044d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d880)

~~~diff
- 0044d810 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d810 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d810 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d810 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d850 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d850 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d850 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d850 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d810 bytes 21243491
+ 0044d850 bytes 21583791
- 0044d818 ["INT_ADD", "register:40f0:8", ["const:44d818:8", "const:4:8"]]
- 0044d818 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d858 ["INT_ADD", "register:40f0:8", ["const:44d858:8", "const:4:8"]]
+ 0044d858 ["CALL", null, ["callee:00c57f70:8"]]
- 0044d818 bytes d6282094
+ 0044d858 bytes c6292094
- 0044d840 ["INT_ADD", "register:40f0:8", ["const:44d840:8", "const:4:8"]]
- 0044d840 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d880 ["INT_ADD", "register:40f0:8", ["const:44d880:8", "const:4:8"]]
+ 0044d880 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d840 bytes 9c282094
+ 0044d880 bytes 8c292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ee6f395f32b0a3436fbd0d974b8897"></a>

### [`0044d8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md) → [`0044d920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md) FUN_0044d920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d948",
      "incomplete_value": true,
      "site": "0044d958",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d908",
      "incomplete_value": true,
      "site": "0044d918",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044d95c",
      "incomplete_value": true,
      "site": "0044d95c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044d91c",
      "incomplete_value": true,
      "site": "0044d91c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d968",
      "incomplete_value": false,
      "site": "0044d970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d928",
      "incomplete_value": false,
      "site": "0044d930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044d948",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044d950",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044d968",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d948",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d950",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d968",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d928) · [`0044d930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d930) · [`0044d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d8e0.md#insn-0044d958)
- 新版 [`0044d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d968) · [`0044d970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d970) · [`0044d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d998)

~~~diff
- 0044d928 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044d928 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d928 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d928 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d968 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044d968 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d968 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d968 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d928 bytes 21243491
+ 0044d968 bytes 21583791
- 0044d930 ["INT_ADD", "register:40f0:8", ["const:44d930:8", "const:4:8"]]
- 0044d930 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044d970 ["INT_ADD", "register:40f0:8", ["const:44d970:8", "const:4:8"]]
+ 0044d970 ["CALL", null, ["callee:00c57f70:8"]]
- 0044d930 bytes 90282094
+ 0044d970 bytes 80292094
- 0044d958 ["INT_ADD", "register:40f0:8", ["const:44d958:8", "const:4:8"]]
- 0044d958 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044d998 ["INT_ADD", "register:40f0:8", ["const:44d998:8", "const:4:8"]]
+ 0044d998 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044d958 bytes 56282094
+ 0044d998 bytes 46292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c53e05697ef1b4e2c92a136d05d833"></a>

### [`0044d9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md) → [`0044da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md) FUN_0044da38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044da60",
      "incomplete_value": true,
      "site": "0044da70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044da20",
      "incomplete_value": true,
      "site": "0044da30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044da74",
      "incomplete_value": true,
      "site": "0044da74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044da34",
      "incomplete_value": true,
      "site": "0044da34",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044da80",
      "incomplete_value": false,
      "site": "0044da88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044da40",
      "incomplete_value": false,
      "site": "0044da48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044da60",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044da68",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044da80",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044da60",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044da68",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044da80",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da40) · [`0044da48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da48) · [`0044da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md#insn-0044da70)
- 新版 [`0044da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044da80) · [`0044da88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044da88) · [`0044dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044dab0)

~~~diff
- 0044da40 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044da40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044da40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044da40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044da80 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044da80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044da80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044da80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044da40 bytes 21243491
+ 0044da80 bytes 21583791
- 0044da48 ["INT_ADD", "register:40f0:8", ["const:44da48:8", "const:4:8"]]
- 0044da48 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044da88 ["INT_ADD", "register:40f0:8", ["const:44da88:8", "const:4:8"]]
+ 0044da88 ["CALL", null, ["callee:00c57f70:8"]]
- 0044da48 bytes 4a282094
+ 0044da88 bytes 3a292094
- 0044da70 ["INT_ADD", "register:40f0:8", ["const:44da70:8", "const:4:8"]]
- 0044da70 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044dab0 ["INT_ADD", "register:40f0:8", ["const:44dab0:8", "const:4:8"]]
+ 0044dab0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044da70 bytes 10282094
+ 0044dab0 bytes 00292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5713fa06adfdd758e219f294c1385d64"></a>

### [`0044db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md) → [`0044db50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md) FUN_0044db50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044db78",
      "incomplete_value": true,
      "site": "0044db88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044db38",
      "incomplete_value": true,
      "site": "0044db48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044db8c",
      "incomplete_value": true,
      "site": "0044db8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044db4c",
      "incomplete_value": true,
      "site": "0044db4c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044db98",
      "incomplete_value": false,
      "site": "0044dba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044db58",
      "incomplete_value": false,
      "site": "0044db60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044db78",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044db80",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044db98",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044db78",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044db80",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044db98",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044db58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db58) · [`0044db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db60) · [`0044db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md#insn-0044db88)
- 新版 [`0044db98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044db98) · [`0044dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044dba0) · [`0044dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044dbc8)

~~~diff
- 0044db58 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044db58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044db58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044db58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044db98 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044db98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044db98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044db98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044db58 bytes 21243491
+ 0044db98 bytes 21583791
- 0044db60 ["INT_ADD", "register:40f0:8", ["const:44db60:8", "const:4:8"]]
- 0044db60 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044dba0 ["INT_ADD", "register:40f0:8", ["const:44dba0:8", "const:4:8"]]
+ 0044dba0 ["CALL", null, ["callee:00c57f70:8"]]
- 0044db60 bytes 04282094
+ 0044dba0 bytes f4282094
- 0044db88 ["INT_ADD", "register:40f0:8", ["const:44db88:8", "const:4:8"]]
- 0044db88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044dbc8 ["INT_ADD", "register:40f0:8", ["const:44dbc8:8", "const:4:8"]]
+ 0044dbc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044db88 bytes ca272094
+ 0044dbc8 bytes ba282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a76e528954257f8c4f137d11f0ae804d"></a>

### [`0044dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md) → [`0044dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md) FUN_0044dc68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dc90",
      "incomplete_value": true,
      "site": "0044dca0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dc50",
      "incomplete_value": true,
      "site": "0044dc60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044dca4",
      "incomplete_value": true,
      "site": "0044dca4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044dc64",
      "incomplete_value": true,
      "site": "0044dc64",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dcb0",
      "incomplete_value": false,
      "site": "0044dcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dc70",
      "incomplete_value": false,
      "site": "0044dc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044dc90",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dc98",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dcb0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dc90",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044dc98",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dcb0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dc70) · [`0044dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dc78) · [`0044dca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dc28.md#insn-0044dca0)
- 新版 [`0044dcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dcb0) · [`0044dcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dcb8) · [`0044dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dce0)

~~~diff
- 0044dc70 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044dc70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dc70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dc70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dcb0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044dcb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dcb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dcb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dc70 bytes 21243491
+ 0044dcb0 bytes 21583791
- 0044dc78 ["INT_ADD", "register:40f0:8", ["const:44dc78:8", "const:4:8"]]
- 0044dc78 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044dcb8 ["INT_ADD", "register:40f0:8", ["const:44dcb8:8", "const:4:8"]]
+ 0044dcb8 ["CALL", null, ["callee:00c57f70:8"]]
- 0044dc78 bytes be272094
+ 0044dcb8 bytes ae282094
- 0044dca0 ["INT_ADD", "register:40f0:8", ["const:44dca0:8", "const:4:8"]]
- 0044dca0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044dce0 ["INT_ADD", "register:40f0:8", ["const:44dce0:8", "const:4:8"]]
+ 0044dce0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044dca0 bytes 84272094
+ 0044dce0 bytes 74282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d13632ffd4a43e9bffc052b51b38bd"></a>

### [`0044dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md) → [`0044dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md) FUN_0044dd80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`0086f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f91c.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dda8",
      "incomplete_value": true,
      "site": "0044ddb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dd68",
      "incomplete_value": true,
      "site": "0044dd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ddbc",
      "incomplete_value": true,
      "site": "0044ddbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044dd7c",
      "incomplete_value": true,
      "site": "0044dd7c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ddc8",
      "incomplete_value": false,
      "site": "0044ddd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dd88",
      "incomplete_value": false,
      "site": "0044dd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044dda8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ddb0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ddc8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dda8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ddb0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ddc8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044dd88) · [`0044dd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044dd90) · [`0044ddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044dd40.md#insn-0044ddb8)
- 新版 [`0044ddc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddc8) · [`0044ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddd0) · [`0044ddf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddf8)

~~~diff
- 0044dd88 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044dd88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dd88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dd88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ddc8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044ddc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ddc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ddc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dd88 bytes 21243491
+ 0044ddc8 bytes 21583791
- 0044dd90 ["INT_ADD", "register:40f0:8", ["const:44dd90:8", "const:4:8"]]
- 0044dd90 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ddd0 ["INT_ADD", "register:40f0:8", ["const:44ddd0:8", "const:4:8"]]
+ 0044ddd0 ["CALL", null, ["callee:00c57f70:8"]]
- 0044dd90 bytes 78272094
+ 0044ddd0 bytes 68282094
- 0044ddb8 ["INT_ADD", "register:40f0:8", ["const:44ddb8:8", "const:4:8"]]
- 0044ddb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ddf8 ["INT_ADD", "register:40f0:8", ["const:44ddf8:8", "const:4:8"]]
+ 0044ddf8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ddb8 bytes 3e272094
+ 0044ddf8 bytes 2e282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79786046100943a420a99d3bceba434b"></a>

### [`0044de58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md) → [`0044de98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md) FUN_0044de98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dec0",
      "incomplete_value": true,
      "site": "0044ded0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044de80",
      "incomplete_value": true,
      "site": "0044de90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ded4",
      "incomplete_value": true,
      "site": "0044ded4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044de94",
      "incomplete_value": true,
      "site": "0044de94",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dee0",
      "incomplete_value": false,
      "site": "0044dee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dea0",
      "incomplete_value": false,
      "site": "0044dea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044dec0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dec8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dee0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dec0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044dec8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dee0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044dea0) · [`0044dea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044dea8) · [`0044ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044de58.md#insn-0044ded0)
- 新版 [`0044dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044dee0) · [`0044dee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044dee8) · [`0044df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044df10)

~~~diff
- 0044dea0 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044dea0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dea0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dea0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dee0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044dee0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dee0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dee0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dea0 bytes 21243491
+ 0044dee0 bytes 21583791
- 0044dea8 ["INT_ADD", "register:40f0:8", ["const:44dea8:8", "const:4:8"]]
- 0044dea8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044dee8 ["INT_ADD", "register:40f0:8", ["const:44dee8:8", "const:4:8"]]
+ 0044dee8 ["CALL", null, ["callee:00c57f70:8"]]
- 0044dea8 bytes 32272094
+ 0044dee8 bytes 22282094
- 0044ded0 ["INT_ADD", "register:40f0:8", ["const:44ded0:8", "const:4:8"]]
- 0044ded0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044df10 ["INT_ADD", "register:40f0:8", ["const:44df10:8", "const:4:8"]]
+ 0044df10 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ded0 bytes f8262094
+ 0044df10 bytes e8272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26d9b4ed70abf7c1eac40741773a96c"></a>

### [`0044df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md) → [`0044dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md) FUN_0044dfb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dfd8",
      "incomplete_value": true,
      "site": "0044dfe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044df98",
      "incomplete_value": true,
      "site": "0044dfa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044dfec",
      "incomplete_value": true,
      "site": "0044dfec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044dfac",
      "incomplete_value": true,
      "site": "0044dfac",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dff8",
      "incomplete_value": false,
      "site": "0044e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dfb8",
      "incomplete_value": false,
      "site": "0044dfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044dfd8",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044dfe0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044dff8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dfd8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044dfe0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dff8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044dfb8) · [`0044dfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044dfc0) · [`0044dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044df70.md#insn-0044dfe8)
- 新版 [`0044dff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044dff8) · [`0044e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044e000) · [`0044e028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044e028)

~~~diff
- 0044dfb8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044dfb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dfb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dfb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dff8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044dff8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dff8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dff8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dfb8 bytes 21243491
+ 0044dff8 bytes 21583791
- 0044dfc0 ["INT_ADD", "register:40f0:8", ["const:44dfc0:8", "const:4:8"]]
- 0044dfc0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e000 ["INT_ADD", "register:40f0:8", ["const:44e000:8", "const:4:8"]]
+ 0044e000 ["CALL", null, ["callee:00c57f70:8"]]
- 0044dfc0 bytes ec262094
+ 0044e000 bytes dc272094
- 0044dfe8 ["INT_ADD", "register:40f0:8", ["const:44dfe8:8", "const:4:8"]]
- 0044dfe8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e028 ["INT_ADD", "register:40f0:8", ["const:44e028:8", "const:4:8"]]
+ 0044e028 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044dfe8 bytes b2262094
+ 0044e028 bytes a2272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c81206761f533b9b7f89fc4bde3952"></a>

### [`0044e088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md) → [`0044e0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md) FUN_0044e0c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e0f0",
      "incomplete_value": true,
      "site": "0044e100",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e0b0",
      "incomplete_value": true,
      "site": "0044e0c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e104",
      "incomplete_value": true,
      "site": "0044e104",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e0c4",
      "incomplete_value": true,
      "site": "0044e0c4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e110",
      "incomplete_value": false,
      "site": "0044e118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e0d0",
      "incomplete_value": false,
      "site": "0044e0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e0f0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e0f8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e110",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e0f0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e0f8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e110",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e0d0) · [`0044e0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e0d8) · [`0044e100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e088.md#insn-0044e100)
- 新版 [`0044e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e110) · [`0044e118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e118) · [`0044e140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e140)

~~~diff
- 0044e0d0 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e0d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e0d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e0d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e110 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e110 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e110 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e110 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e0d0 bytes 21243491
+ 0044e110 bytes 21583791
- 0044e0d8 ["INT_ADD", "register:40f0:8", ["const:44e0d8:8", "const:4:8"]]
- 0044e0d8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e118 ["INT_ADD", "register:40f0:8", ["const:44e118:8", "const:4:8"]]
+ 0044e118 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e0d8 bytes a6262094
+ 0044e118 bytes 96272094
- 0044e100 ["INT_ADD", "register:40f0:8", ["const:44e100:8", "const:4:8"]]
- 0044e100 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e140 ["INT_ADD", "register:40f0:8", ["const:44e140:8", "const:4:8"]]
+ 0044e140 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e100 bytes 6c262094
+ 0044e140 bytes 5c272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3593e1b2b5855bde2b9ba0471fe367"></a>

### [`0044e1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md) → [`0044e1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md) FUN_0044e1e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) [`005faf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005faf94.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e208",
      "incomplete_value": true,
      "site": "0044e218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e1c8",
      "incomplete_value": true,
      "site": "0044e1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e21c",
      "incomplete_value": true,
      "site": "0044e21c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e1dc",
      "incomplete_value": true,
      "site": "0044e1dc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e228",
      "incomplete_value": false,
      "site": "0044e230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e1e8",
      "incomplete_value": false,
      "site": "0044e1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e208",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e210",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e228",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e208",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e210",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e228",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e1e8) · [`0044e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e1f0) · [`0044e218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e1a0.md#insn-0044e218)
- 新版 [`0044e228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e228) · [`0044e230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e230) · [`0044e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e258)

~~~diff
- 0044e1e8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e1e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e1e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e1e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e228 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e228 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e228 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e228 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e1e8 bytes 21243491
+ 0044e228 bytes 21583791
- 0044e1f0 ["INT_ADD", "register:40f0:8", ["const:44e1f0:8", "const:4:8"]]
- 0044e1f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e230 ["INT_ADD", "register:40f0:8", ["const:44e230:8", "const:4:8"]]
+ 0044e230 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e1f0 bytes 60262094
+ 0044e230 bytes 50272094
- 0044e218 ["INT_ADD", "register:40f0:8", ["const:44e218:8", "const:4:8"]]
- 0044e218 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e258 ["INT_ADD", "register:40f0:8", ["const:44e258:8", "const:4:8"]]
+ 0044e258 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e218 bytes 26262094
+ 0044e258 bytes 16272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c29d3c9f9e116a318428c9e4e05e2d7"></a>

### [`0044e2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md) → [`0044e2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md) FUN_0044e2f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e320",
      "incomplete_value": true,
      "site": "0044e330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e2e0",
      "incomplete_value": true,
      "site": "0044e2f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e334",
      "incomplete_value": true,
      "site": "0044e334",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e2f4",
      "incomplete_value": true,
      "site": "0044e2f4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e340",
      "incomplete_value": false,
      "site": "0044e348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e300",
      "incomplete_value": false,
      "site": "0044e308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e320",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e328",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e340",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e320",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e328",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e340",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e300) · [`0044e308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e308) · [`0044e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e2b8.md#insn-0044e330)
- 新版 [`0044e340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e340) · [`0044e348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e348) · [`0044e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e370)

~~~diff
- 0044e300 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e340 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e340 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e340 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e340 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e300 bytes 21243491
+ 0044e340 bytes 21583791
- 0044e308 ["INT_ADD", "register:40f0:8", ["const:44e308:8", "const:4:8"]]
- 0044e308 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e348 ["INT_ADD", "register:40f0:8", ["const:44e348:8", "const:4:8"]]
+ 0044e348 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e308 bytes 1a262094
+ 0044e348 bytes 0a272094
- 0044e330 ["INT_ADD", "register:40f0:8", ["const:44e330:8", "const:4:8"]]
- 0044e330 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e370 ["INT_ADD", "register:40f0:8", ["const:44e370:8", "const:4:8"]]
+ 0044e370 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e330 bytes e0252094
+ 0044e370 bytes d0262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55a6e84eef89015382ec3de7d35b033e"></a>

### [`0044e3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md) → [`0044e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md) FUN_0044e410

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e438",
      "incomplete_value": true,
      "site": "0044e448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e3f8",
      "incomplete_value": true,
      "site": "0044e408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e44c",
      "incomplete_value": true,
      "site": "0044e44c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e40c",
      "incomplete_value": true,
      "site": "0044e40c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e458",
      "incomplete_value": false,
      "site": "0044e460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e418",
      "incomplete_value": false,
      "site": "0044e420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e438",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e440",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e458",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e438",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e440",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e458",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e418) · [`0044e420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e420) · [`0044e448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e3d0.md#insn-0044e448)
- 新版 [`0044e458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e458) · [`0044e460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e460) · [`0044e488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e488)

~~~diff
- 0044e418 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e418 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e418 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e418 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e458 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e458 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e458 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e458 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e418 bytes 21243491
+ 0044e458 bytes 21583791
- 0044e420 ["INT_ADD", "register:40f0:8", ["const:44e420:8", "const:4:8"]]
- 0044e420 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e460 ["INT_ADD", "register:40f0:8", ["const:44e460:8", "const:4:8"]]
+ 0044e460 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e420 bytes d4252094
+ 0044e460 bytes c4262094
- 0044e448 ["INT_ADD", "register:40f0:8", ["const:44e448:8", "const:4:8"]]
- 0044e448 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e488 ["INT_ADD", "register:40f0:8", ["const:44e488:8", "const:4:8"]]
+ 0044e488 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e448 bytes 9a252094
+ 0044e488 bytes 8a262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b51e5751aac4dcef4a1540fdc7fe321"></a>

### [`0044e4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md) → [`0044e528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md) FUN_0044e528

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e550",
      "incomplete_value": true,
      "site": "0044e560",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e510",
      "incomplete_value": true,
      "site": "0044e520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e564",
      "incomplete_value": true,
      "site": "0044e564",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e524",
      "incomplete_value": true,
      "site": "0044e524",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e570",
      "incomplete_value": false,
      "site": "0044e578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e530",
      "incomplete_value": false,
      "site": "0044e538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e550",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e558",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e570",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e550",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e558",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e570",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e530) · [`0044e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e538) · [`0044e560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e4e8.md#insn-0044e560)
- 新版 [`0044e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e570) · [`0044e578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e578) · [`0044e5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e5a0)

~~~diff
- 0044e530 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e530 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e530 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e530 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e570 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e570 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e570 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e570 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e530 bytes 21243491
+ 0044e570 bytes 21583791
- 0044e538 ["INT_ADD", "register:40f0:8", ["const:44e538:8", "const:4:8"]]
- 0044e538 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e578 ["INT_ADD", "register:40f0:8", ["const:44e578:8", "const:4:8"]]
+ 0044e578 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e538 bytes 8e252094
+ 0044e578 bytes 7e262094
- 0044e560 ["INT_ADD", "register:40f0:8", ["const:44e560:8", "const:4:8"]]
- 0044e560 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e5a0 ["INT_ADD", "register:40f0:8", ["const:44e5a0:8", "const:4:8"]]
+ 0044e5a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e560 bytes 54252094
+ 0044e5a0 bytes 44262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7c2c0a25a53941f018ef8940115ad62"></a>

### [`0044e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md) → [`0044e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md) FUN_0044e640

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac0700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0700.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00ac08fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac08fc.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e668",
      "incomplete_value": true,
      "site": "0044e678",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e628",
      "incomplete_value": true,
      "site": "0044e638",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e67c",
      "incomplete_value": true,
      "site": "0044e67c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e63c",
      "incomplete_value": true,
      "site": "0044e63c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e688",
      "incomplete_value": false,
      "site": "0044e690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e648",
      "incomplete_value": false,
      "site": "0044e650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e668",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e670",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e688",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e668",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e670",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e688",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e648) · [`0044e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e650) · [`0044e678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e600.md#insn-0044e678)
- 新版 [`0044e688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e688) · [`0044e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e690) · [`0044e6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e6b8)

~~~diff
- 0044e648 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e648 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e648 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e648 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e688 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e688 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e688 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e688 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e648 bytes 21243491
+ 0044e688 bytes 21583791
- 0044e650 ["INT_ADD", "register:40f0:8", ["const:44e650:8", "const:4:8"]]
- 0044e650 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e690 ["INT_ADD", "register:40f0:8", ["const:44e690:8", "const:4:8"]]
+ 0044e690 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e650 bytes 48252094
+ 0044e690 bytes 38262094
- 0044e678 ["INT_ADD", "register:40f0:8", ["const:44e678:8", "const:4:8"]]
- 0044e678 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e6b8 ["INT_ADD", "register:40f0:8", ["const:44e6b8:8", "const:4:8"]]
+ 0044e6b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e678 bytes 0e252094
+ 0044e6b8 bytes fe252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc3b3874af5134ce848b650742f4273a"></a>

### [`0044e718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md) → [`0044e758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md) FUN_0044e758

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e780",
      "incomplete_value": true,
      "site": "0044e790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e740",
      "incomplete_value": true,
      "site": "0044e750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e794",
      "incomplete_value": true,
      "site": "0044e794",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e754",
      "incomplete_value": true,
      "site": "0044e754",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e7a0",
      "incomplete_value": false,
      "site": "0044e7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e760",
      "incomplete_value": false,
      "site": "0044e768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e780",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e788",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e7a0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e780",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e788",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e7a0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e760) · [`0044e768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e768) · [`0044e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e718.md#insn-0044e790)
- 新版 [`0044e7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7a0) · [`0044e7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7a8) · [`0044e7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7d0)

~~~diff
- 0044e760 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e760 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e760 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e760 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e7a0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e760 bytes 21243491
+ 0044e7a0 bytes 21583791
- 0044e768 ["INT_ADD", "register:40f0:8", ["const:44e768:8", "const:4:8"]]
- 0044e768 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e7a8 ["INT_ADD", "register:40f0:8", ["const:44e7a8:8", "const:4:8"]]
+ 0044e7a8 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e768 bytes 02252094
+ 0044e7a8 bytes f2252094
- 0044e790 ["INT_ADD", "register:40f0:8", ["const:44e790:8", "const:4:8"]]
- 0044e790 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e7d0 ["INT_ADD", "register:40f0:8", ["const:44e7d0:8", "const:4:8"]]
+ 0044e7d0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e790 bytes c8242094
+ 0044e7d0 bytes b8252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79498243154ae9bda9a51dea5bccc353"></a>

### [`0044e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md) → [`0044e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md) FUN_0044e870

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e898",
      "incomplete_value": true,
      "site": "0044e8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e858",
      "incomplete_value": true,
      "site": "0044e868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e8ac",
      "incomplete_value": true,
      "site": "0044e8ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e86c",
      "incomplete_value": true,
      "site": "0044e86c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e8b8",
      "incomplete_value": false,
      "site": "0044e8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e878",
      "incomplete_value": false,
      "site": "0044e880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e898",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e8a0",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e8b8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e898",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e8a0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e8b8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e878) · [`0044e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e880) · [`0044e8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e830.md#insn-0044e8a8)
- 新版 [`0044e8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8b8) · [`0044e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8c0) · [`0044e8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8e8)

~~~diff
- 0044e878 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e878 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e878 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e878 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e8b8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e8b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e8b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e8b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e878 bytes 21243491
+ 0044e8b8 bytes 21583791
- 0044e880 ["INT_ADD", "register:40f0:8", ["const:44e880:8", "const:4:8"]]
- 0044e880 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e8c0 ["INT_ADD", "register:40f0:8", ["const:44e8c0:8", "const:4:8"]]
+ 0044e8c0 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e880 bytes bc242094
+ 0044e8c0 bytes ac252094
- 0044e8a8 ["INT_ADD", "register:40f0:8", ["const:44e8a8:8", "const:4:8"]]
- 0044e8a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044e8e8 ["INT_ADD", "register:40f0:8", ["const:44e8e8:8", "const:4:8"]]
+ 0044e8e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e8a8 bytes 82242094
+ 0044e8e8 bytes 72252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8005279945a17693978522d190edb064"></a>

### [`0044e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md) → [`0044e988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md) FUN_0044e988

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`008e66ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e6/008e66ac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e9b0",
      "incomplete_value": true,
      "site": "0044e9c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e970",
      "incomplete_value": true,
      "site": "0044e980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044e9c4",
      "incomplete_value": true,
      "site": "0044e9c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044e984",
      "incomplete_value": true,
      "site": "0044e984",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e9d0",
      "incomplete_value": false,
      "site": "0044e9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e990",
      "incomplete_value": false,
      "site": "0044e998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044e9b0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044e9b8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044e9d0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e9b0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e9b8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e9d0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e990) · [`0044e998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e998) · [`0044e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md#insn-0044e9c0)
- 新版 [`0044e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044e9d0) · [`0044e9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044e9d8) · [`0044ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044ea00)

~~~diff
- 0044e990 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044e990 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e990 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e990 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e9d0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044e9d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e9d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e9d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e990 bytes 21243491
+ 0044e9d0 bytes 21583791
- 0044e998 ["INT_ADD", "register:40f0:8", ["const:44e998:8", "const:4:8"]]
- 0044e998 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044e9d8 ["INT_ADD", "register:40f0:8", ["const:44e9d8:8", "const:4:8"]]
+ 0044e9d8 ["CALL", null, ["callee:00c57f70:8"]]
- 0044e998 bytes 76242094
+ 0044e9d8 bytes 66252094
- 0044e9c0 ["INT_ADD", "register:40f0:8", ["const:44e9c0:8", "const:4:8"]]
- 0044e9c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ea00 ["INT_ADD", "register:40f0:8", ["const:44ea00:8", "const:4:8"]]
+ 0044ea00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044e9c0 bytes 3c242094
+ 0044ea00 bytes 2c252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d0deeea9bb11b920ef0ca69a267cdbe"></a>

### [`0044eab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md) → [`0044eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md) FUN_0044eaf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044eb18",
      "incomplete_value": true,
      "site": "0044eb28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ead8",
      "incomplete_value": true,
      "site": "0044eae8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044eb2c",
      "incomplete_value": true,
      "site": "0044eb2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044eaec",
      "incomplete_value": true,
      "site": "0044eaec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044eb38",
      "incomplete_value": false,
      "site": "0044eb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044eaf8",
      "incomplete_value": false,
      "site": "0044eb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044eb18",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044eb20",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044eb38",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044eb18",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044eb20",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044eb38",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044eaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eaf8) · [`0044eb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eb00) · [`0044eb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044eab0.md#insn-0044eb28)
- 新版 [`0044eb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb38) · [`0044eb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb40) · [`0044eb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb68)

~~~diff
- 0044eaf8 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044eaf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044eaf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044eaf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044eb38 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044eb38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eb38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eb38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044eaf8 bytes 21243491
+ 0044eb38 bytes 21583791
- 0044eb00 ["INT_ADD", "register:40f0:8", ["const:44eb00:8", "const:4:8"]]
- 0044eb00 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044eb40 ["INT_ADD", "register:40f0:8", ["const:44eb40:8", "const:4:8"]]
+ 0044eb40 ["CALL", null, ["callee:00c57f70:8"]]
- 0044eb00 bytes 1c242094
+ 0044eb40 bytes 0c252094
- 0044eb28 ["INT_ADD", "register:40f0:8", ["const:44eb28:8", "const:4:8"]]
- 0044eb28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044eb68 ["INT_ADD", "register:40f0:8", ["const:44eb68:8", "const:4:8"]]
+ 0044eb68 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044eb28 bytes e2232094
+ 0044eb68 bytes d2242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30320da615de21930cee79d14e1f295"></a>

### [`0044ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md) → [`0044ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md) FUN_0044ec08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ec30",
      "incomplete_value": true,
      "site": "0044ec40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ebf0",
      "incomplete_value": true,
      "site": "0044ec00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ec44",
      "incomplete_value": true,
      "site": "0044ec44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044ec04",
      "incomplete_value": true,
      "site": "0044ec04",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ec50",
      "incomplete_value": false,
      "site": "0044ec58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ec10",
      "incomplete_value": false,
      "site": "0044ec18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044ec30",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ec38",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ec50",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ec30",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ec38",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ec50",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ec10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ec10) · [`0044ec18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ec18) · [`0044ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ebc8.md#insn-0044ec40)
- 新版 [`0044ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec50) · [`0044ec58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec58) · [`0044ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec80)

~~~diff
- 0044ec10 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044ec10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ec10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ec10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ec50 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044ec50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ec50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ec50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ec10 bytes 21243491
+ 0044ec50 bytes 21583791
- 0044ec18 ["INT_ADD", "register:40f0:8", ["const:44ec18:8", "const:4:8"]]
- 0044ec18 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ec58 ["INT_ADD", "register:40f0:8", ["const:44ec58:8", "const:4:8"]]
+ 0044ec58 ["CALL", null, ["callee:00c57f70:8"]]
- 0044ec18 bytes d6232094
+ 0044ec58 bytes c6242094
- 0044ec40 ["INT_ADD", "register:40f0:8", ["const:44ec40:8", "const:4:8"]]
- 0044ec40 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ec80 ["INT_ADD", "register:40f0:8", ["const:44ec80:8", "const:4:8"]]
+ 0044ec80 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ec40 bytes 9c232094
+ 0044ec80 bytes 8c242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6fada6f86c848025d42545fd3b4d7f6"></a>

### [`0044ece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md) → [`0044ed20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md) FUN_0044ed20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008a4c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4c0c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`008a4c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4c50.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ed48",
      "incomplete_value": true,
      "site": "0044ed58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ed08",
      "incomplete_value": true,
      "site": "0044ed18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ed5c",
      "incomplete_value": true,
      "site": "0044ed5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044ed1c",
      "incomplete_value": true,
      "site": "0044ed1c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ed68",
      "incomplete_value": false,
      "site": "0044ed70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ed28",
      "incomplete_value": false,
      "site": "0044ed30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044ed48",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ed50",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ed68",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ed48",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ed50",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ed68",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ed28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ed28) · [`0044ed30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ed30) · [`0044ed58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ece0.md#insn-0044ed58)
- 新版 [`0044ed68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed68) · [`0044ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed70) · [`0044ed98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed98)

~~~diff
- 0044ed28 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044ed28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ed28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ed28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ed68 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044ed68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ed68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ed68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ed28 bytes 21243491
+ 0044ed68 bytes 21583791
- 0044ed30 ["INT_ADD", "register:40f0:8", ["const:44ed30:8", "const:4:8"]]
- 0044ed30 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ed70 ["INT_ADD", "register:40f0:8", ["const:44ed70:8", "const:4:8"]]
+ 0044ed70 ["CALL", null, ["callee:00c57f70:8"]]
- 0044ed30 bytes 90232094
+ 0044ed70 bytes 80242094
- 0044ed58 ["INT_ADD", "register:40f0:8", ["const:44ed58:8", "const:4:8"]]
- 0044ed58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044ed98 ["INT_ADD", "register:40f0:8", ["const:44ed98:8", "const:4:8"]]
+ 0044ed98 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ed58 bytes 56232094
+ 0044ed98 bytes 46242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd35476a5221252528239f0b1dcfb866"></a>

### [`0044edfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md) → [`0044ee3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md) FUN_0044ee3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00783470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007834b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007834b0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ee64",
      "incomplete_value": true,
      "site": "0044ee74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ee24",
      "incomplete_value": true,
      "site": "0044ee34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ee78",
      "incomplete_value": true,
      "site": "0044ee78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044ee38",
      "incomplete_value": true,
      "site": "0044ee38",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ee84",
      "incomplete_value": false,
      "site": "0044ee8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ee44",
      "incomplete_value": false,
      "site": "0044ee4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044ee64",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ee6c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044ee84",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ee64",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ee6c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ee84",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ee44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee44) · [`0044ee4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee4c) · [`0044ee74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md#insn-0044ee74)
- 新版 [`0044ee84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044ee84) · [`0044ee8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044ee8c) · [`0044eeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044eeb4)

~~~diff
- 0044ee44 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044ee44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ee44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ee44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ee84 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044ee84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ee84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ee84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ee44 bytes 21243491
+ 0044ee84 bytes 21583791
- 0044ee4c ["INT_ADD", "register:40f0:8", ["const:44ee4c:8", "const:4:8"]]
- 0044ee4c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044ee8c ["INT_ADD", "register:40f0:8", ["const:44ee8c:8", "const:4:8"]]
+ 0044ee8c ["CALL", null, ["callee:00c57f70:8"]]
- 0044ee4c bytes 49232094
+ 0044ee8c bytes 39242094
- 0044ee74 ["INT_ADD", "register:40f0:8", ["const:44ee74:8", "const:4:8"]]
- 0044ee74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044eeb4 ["INT_ADD", "register:40f0:8", ["const:44eeb4:8", "const:4:8"]]
+ 0044eeb4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ee74 bytes 0f232094
+ 0044eeb4 bytes ff232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d48c75eabddf304960002817d31730a2"></a>

### [`0044ef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md) → [`0044ef54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md) FUN_0044ef54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`008a7860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7860.md) [`008a7af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7af8.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 3件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`008a78a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a78a4.md) [`008a7b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7b3c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ef80",
      "incomplete_value": true,
      "site": "0044ef94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ef40",
      "incomplete_value": true,
      "site": "0044ef54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044ef98",
      "incomplete_value": true,
      "site": "0044ef98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044ef58",
      "incomplete_value": true,
      "site": "0044ef58",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044efa4",
      "incomplete_value": false,
      "site": "0044efac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ef64",
      "incomplete_value": false,
      "site": "0044ef6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044ef80",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044ef8c",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044efa4",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ef80",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ef8c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044efa4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ef64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044ef64) · [`0044ef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044ef6c) · [`0044ef94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ef14.md#insn-0044ef94)
- 新版 [`0044efa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efa4) · [`0044efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efac) · [`0044efd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efd4)

~~~diff
- 0044ef64 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044ef64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ef64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ef64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044efa4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044efa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044efa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044efa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ef64 bytes 21243491
+ 0044efa4 bytes 21583791
- 0044ef6c ["INT_ADD", "register:40f0:8", ["const:44ef6c:8", "const:4:8"]]
- 0044ef6c ["CALL", null, ["callee:00c57f70:8"]]
+ 0044efac ["INT_ADD", "register:40f0:8", ["const:44efac:8", "const:4:8"]]
+ 0044efac ["CALL", null, ["callee:00c57f70:8"]]
- 0044ef6c bytes 01232094
+ 0044efac bytes f1232094
- 0044ef94 ["INT_ADD", "register:40f0:8", ["const:44ef94:8", "const:4:8"]]
- 0044ef94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044efd4 ["INT_ADD", "register:40f0:8", ["const:44efd4:8", "const:4:8"]]
+ 0044efd4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044ef94 bytes c7222094
+ 0044efd4 bytes b7232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80184f90aee4bba611d5a4d161fb4c7c"></a>

### [`0044f120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md) → [`0044f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md) FUN_0044f160

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f188",
      "incomplete_value": true,
      "site": "0044f198",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f148",
      "incomplete_value": true,
      "site": "0044f158",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044f19c",
      "incomplete_value": true,
      "site": "0044f19c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044f15c",
      "incomplete_value": true,
      "site": "0044f15c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f1a8",
      "incomplete_value": false,
      "site": "0044f1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f168",
      "incomplete_value": false,
      "site": "0044f170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044f188",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044f190",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044f1a8",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f188",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044f190",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044f1a8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f168) · [`0044f170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f170) · [`0044f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f120.md#insn-0044f198)
- 新版 [`0044f1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1a8) · [`0044f1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1b0) · [`0044f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1d8)

~~~diff
- 0044f168 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044f168 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f168 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f168 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f1a8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044f1a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f1a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f1a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f168 bytes 21243491
+ 0044f1a8 bytes 21583791
- 0044f170 ["INT_ADD", "register:40f0:8", ["const:44f170:8", "const:4:8"]]
- 0044f170 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044f1b0 ["INT_ADD", "register:40f0:8", ["const:44f1b0:8", "const:4:8"]]
+ 0044f1b0 ["CALL", null, ["callee:00c57f70:8"]]
- 0044f170 bytes 80222094
+ 0044f1b0 bytes 70232094
- 0044f198 ["INT_ADD", "register:40f0:8", ["const:44f198:8", "const:4:8"]]
- 0044f198 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044f1d8 ["INT_ADD", "register:40f0:8", ["const:44f1d8:8", "const:4:8"]]
+ 0044f1d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044f198 bytes 46222094
+ 0044f1d8 bytes 36232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81dbbd4708cf1966e8b05728010d1b22"></a>

### [`0044f238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md) → [`0044f278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md) FUN_0044f278

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f2a0",
      "incomplete_value": true,
      "site": "0044f2b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f260",
      "incomplete_value": true,
      "site": "0044f270",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0044f2b4",
      "incomplete_value": true,
      "site": "0044f2b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044f274",
      "incomplete_value": true,
      "site": "0044f274",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f2c0",
      "incomplete_value": false,
      "site": "0044f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f280",
      "incomplete_value": false,
      "site": "0044f288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d09:8"
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
      "0044f2a0",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044f2a8",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044f2c0",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f2a0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044f2a8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044f2c0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f280) · [`0044f288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f288) · [`0044f2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f238.md#insn-0044f2b0)
- 新版 [`0044f2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2c0) · [`0044f2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2c8) · [`0044f2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2f0)

~~~diff
- 0044f280 ["COPY", "tmp:0:8", ["const:d09:8"]]
- 0044f280 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f280 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f280 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f2c0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
+ 0044f2c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f2c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f2c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f280 bytes 21243491
+ 0044f2c0 bytes 21583791
- 0044f288 ["INT_ADD", "register:40f0:8", ["const:44f288:8", "const:4:8"]]
- 0044f288 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044f2c8 ["INT_ADD", "register:40f0:8", ["const:44f2c8:8", "const:4:8"]]
+ 0044f2c8 ["CALL", null, ["callee:00c57f70:8"]]
- 0044f288 bytes 3a222094
+ 0044f2c8 bytes 2a232094
- 0044f2b0 ["INT_ADD", "register:40f0:8", ["const:44f2b0:8", "const:4:8"]]
- 0044f2b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0044f2f0 ["INT_ADD", "register:40f0:8", ["const:44f2f0:8", "const:4:8"]]
+ 0044f2f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0044f2b0 bytes 00222094
+ 0044f2f0 bytes f0222094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f76987e3ecced99c0bf4cd97380ed97"></a>

### [`0044f350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md) → [`0044f390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md) FUN_0044f390

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f3bc",
      "incomplete_value": false,
      "site": "0044f3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:2d5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f37c",
      "incomplete_value": false,
      "site": "0044f384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "0044f3cc",
      "incomplete_value": false,
      "site": "0044f3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bc5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f38c",
      "incomplete_value": false,
      "site": "0044f398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b85:8"
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
      "0044f3bc",
      "PARAM",
      [
        "storage",
        "002ab208",
        null,
        "string"
      ]
    ],
    [
      "0044f3cc",
      "PARAM",
      [
        "storage",
        "002bfb85",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f3bc",
      "PARAM",
      [
        "storage",
        "002ab2d5",
        null,
        "string"
      ]
    ],
    [
      "0044f3cc",
      "PARAM",
      [
        "storage",
        "002bfbc5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f384) · [`0044f398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f398) · [`0044f37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md#insn-0044f37c)
- 新版 [`0044f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3c4) · [`0044f3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3d8) · [`0044f3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3bc)

~~~diff
- 0044f384 ["INT_ADD", "register:40f0:8", ["const:44f384:8", "const:4:8"]]
- 0044f384 ["CALL", null, ["callee:00c58190:8"]]
+ 0044f3c4 ["INT_ADD", "register:40f0:8", ["const:44f3c4:8", "const:4:8"]]
+ 0044f3c4 ["CALL", null, ["callee:00c58190:8"]]
- 0044f384 bytes 83222094
+ 0044f3c4 bytes 73232094
- 0044f398 ["INT_ADD", "register:40f0:8", ["const:44f398:8", "const:4:8"]]
- 0044f398 ["CALL", null, ["callee:00c580b0:8"]]
+ 0044f3d8 ["INT_ADD", "register:40f0:8", ["const:44f3d8:8", "const:4:8"]]
+ 0044f3d8 ["CALL", null, ["callee:00c580b0:8"]]
- 0044f398 bytes 46222094
+ 0044f3d8 bytes 36232094
- 0044f37c ["COPY", "tmp:0:8", ["const:208:8"]]
- 0044f37c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f37c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f37c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f3bc ["COPY", "tmp:0:8", ["const:2d5:8"]]
+ 0044f3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f37c bytes 21200891
+ 0044f3bc bytes 21540b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-007f8169b733842cfda0921d57dabbcb"></a>

### [`0044f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md) → [`0044f43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md) FUN_0044f43c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f468",
      "incomplete_value": false,
      "site": "0044f470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:2d5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f428",
      "incomplete_value": false,
      "site": "0044f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "0044f478",
      "incomplete_value": false,
      "site": "0044f484",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f438",
      "incomplete_value": false,
      "site": "0044f444",
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
            "const:efe:8"
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
      "0044f468",
      "PARAM",
      [
        "storage",
        "002ab208",
        null,
        "string"
      ]
    ],
    [
      "0044f478",
      "PARAM",
      [
        "storage",
        "002c0efe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f468",
      "PARAM",
      [
        "storage",
        "002ab2d5",
        null,
        "string"
      ]
    ],
    [
      "0044f478",
      "PARAM",
      [
        "storage",
        "002c0f3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f430) · [`0044f444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f444) · [`0044f428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md#insn-0044f428)
- 新版 [`0044f470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f470) · [`0044f484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f484) · [`0044f468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f468)

~~~diff
- 0044f430 ["INT_ADD", "register:40f0:8", ["const:44f430:8", "const:4:8"]]
- 0044f430 ["CALL", null, ["callee:00c58190:8"]]
+ 0044f470 ["INT_ADD", "register:40f0:8", ["const:44f470:8", "const:4:8"]]
+ 0044f470 ["CALL", null, ["callee:00c58190:8"]]
- 0044f430 bytes 58222094
+ 0044f470 bytes 48232094
- 0044f444 ["INT_ADD", "register:40f0:8", ["const:44f444:8", "const:4:8"]]
- 0044f444 ["CALL", null, ["callee:00c580b0:8"]]
+ 0044f484 ["INT_ADD", "register:40f0:8", ["const:44f484:8", "const:4:8"]]
+ 0044f484 ["CALL", null, ["callee:00c580b0:8"]]
- 0044f444 bytes 1b222094
+ 0044f484 bytes 0b232094
- 0044f428 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0044f428 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f428 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f428 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f468 ["COPY", "tmp:0:8", ["const:2d5:8"]]
+ 0044f468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f428 bytes 21200891
+ 0044f468 bytes 21540b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffd99a71915611355e9b620a2c40742d"></a>

### [`0044f4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md) → [`0044f4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md) _INIT_10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 8件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f524",
      "incomplete_value": true,
      "site": "0044f540",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f4e4",
      "incomplete_value": true,
      "site": "0044f500",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f548",
      "incomplete_value": true,
      "site": "0044f564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f508",
      "incomplete_value": true,
      "site": "0044f524",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f568",
      "incomplete_value": true,
      "site": "0044f584",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044f528",
      "incomplete_value": true,
      "site": "0044f544",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0044f524",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0044f548",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0044f568",
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
      "0044f524",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0044f548",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0044f568",
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

- 旧版 [`0044f520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md#insn-0044f520) · [`0044f540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md#insn-0044f540) · [`0044f608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f4a8.md#insn-0044f608)
- 新版 [`0044f560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f560) · [`0044f580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f580) · [`0044f648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f648)

~~~diff
- 0044f520 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0044f520 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0044f520 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0044f520 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044f560 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0044f560 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f560 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f560 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0044f520 bytes 4a093691
+ 0044f560 bytes 4a093791
- 0044f540 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0044f540 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0044f540 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0044f540 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044f580 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0044f580 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f580 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f580 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0044f540 bytes 4a553a91
+ 0044f580 bytes 4a893d91
- 0044f608 ["INT_ADD", "register:40f0:8", ["const:44f608:8", "const:4:8"]]
- 0044f608 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0044f648 ["INT_ADD", "register:40f0:8", ["const:44f648:8", "const:4:8"]]
+ 0044f648 ["CALL", null, ["callee:0043b7f8:8"]]
- 0044f608 bytes 6cb0ff97
+ 0044f648 bytes 6cb0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bffd357545314f57956feac2f87bb1e6"></a>

### [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) → [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md) FUN_0044f898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`0086ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086ddc4.md) [`008a6e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6e08.md) [`008a7264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7264.md) [`008a7464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 6件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086de04.md) [`008a6e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6e4c.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) [`008a74a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a74a8.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f8c4",
      "incomplete_value": false,
      "site": "0044f8c8",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f884",
      "incomplete_value": false,
      "site": "0044f888",
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
            "const:6a0:8"
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
      "definition_site": "0044f8d4",
      "incomplete_value": false,
      "site": "0044f8d8",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f894",
      "incomplete_value": false,
      "site": "0044f898",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f8b4",
      "incomplete_value": true,
      "site": "0044f8bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f874",
      "incomplete_value": true,
      "site": "0044f87c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:698:8"
              ]
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
      "0044f8a8",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8b4",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f8c4",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f8a8",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8b4",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f8c4",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f888) · [`0044f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f898) · [`0044f864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md#insn-0044f864)
- 新版 [`0044f8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8c8) · [`0044f8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8d8) · [`0044f8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8a4)

~~~diff
- 0044f888 ["INT_ADD", "register:40f0:8", ["const:44f888:8", "const:4:8"]]
- 0044f888 ["CALL", null, ["callee:00c57e50:8"]]
+ 0044f8c8 ["INT_ADD", "register:40f0:8", ["const:44f8c8:8", "const:4:8"]]
+ 0044f8c8 ["CALL", null, ["callee:00c57e50:8"]]
- 0044f888 bytes 72202094
+ 0044f8c8 bytes 62212094
- 0044f898 ["INT_ADD", "register:40f0:8", ["const:44f898:8", "const:4:8"]]
- 0044f898 ["CALL", null, ["callee:00c57e70:8"]]
+ 0044f8d8 ["INT_ADD", "register:40f0:8", ["const:44f8d8:8", "const:4:8"]]
+ 0044f8d8 ["CALL", null, ["callee:00c57e70:8"]]
- 0044f898 bytes 76202094
+ 0044f8d8 bytes 66212094
- 0044f864 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0044f864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044f864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044f864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044f8a4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 0044f8a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044f864 bytes 08811a91
+ 0044f8a4 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22345c75e67760bf59386b440418b975"></a>

### [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) → [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) FUN_0044f8e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 23件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0079b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 23件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f90c",
      "incomplete_value": false,
      "site": "0044f910",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8cc",
      "incomplete_value": false,
      "site": "0044f8d0",
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
            "const:6a0:8"
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
      "definition_site": "0044f91c",
      "incomplete_value": false,
      "site": "0044f920",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8dc",
      "incomplete_value": false,
      "site": "0044f8e0",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f8fc",
      "incomplete_value": false,
      "site": "0044f904",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8bc",
      "incomplete_value": false,
      "site": "0044f8c4",
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
            "const:698:8"
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
      "0044f8f0",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8fc",
      "DATA",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f90c",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f8f0",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8fc",
      "DATA",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f90c",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8d0) · [`0044f8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8e0) · [`0044f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md#insn-0044f8ac)
- 新版 [`0044f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f910) · [`0044f920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f920) · [`0044f8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f8ec)

~~~diff
- 0044f8d0 ["INT_ADD", "register:40f0:8", ["const:44f8d0:8", "const:4:8"]]
- 0044f8d0 ["CALL", null, ["callee:00c57e50:8"]]
+ 0044f910 ["INT_ADD", "register:40f0:8", ["const:44f910:8", "const:4:8"]]
+ 0044f910 ["CALL", null, ["callee:00c57e50:8"]]
- 0044f8d0 bytes 60202094
+ 0044f910 bytes 50212094
- 0044f8e0 ["INT_ADD", "register:40f0:8", ["const:44f8e0:8", "const:4:8"]]
- 0044f8e0 ["CALL", null, ["callee:00c57e70:8"]]
+ 0044f920 ["INT_ADD", "register:40f0:8", ["const:44f920:8", "const:4:8"]]
+ 0044f920 ["CALL", null, ["callee:00c57e70:8"]]
- 0044f8e0 bytes 64202094
+ 0044f920 bytes 54212094
- 0044f8ac ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0044f8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044f8ec ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 0044f8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044f8ac bytes 08811a91
+ 0044f8ec bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab8ca034a68eaa4904cd8c93847e3d3"></a>

### [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) → [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) FUN_0044f948

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873a68.md) · 呼出先 10件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`00459f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459f60.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 10件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`00459fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459fa0.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fa9c",
      "incomplete_value": false,
      "site": "0044fa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fa5c",
      "incomplete_value": false,
      "site": "0044fa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f97c",
      "incomplete_value": false,
      "site": "0044f984",
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
            "const:e6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f93c",
      "incomplete_value": false,
      "site": "0044f944",
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
            "const:e2a:8"
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
      "definition_site": "0044f9e8",
      "incomplete_value": true,
      "site": "0044f9f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f9a8",
      "incomplete_value": true,
      "site": "0044f9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
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
      "0044f97c",
      "PARAM",
      [
        "storage",
        "002b5e2a",
        null,
        "string"
      ]
    ],
    [
      "0044f9e8",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "0044f9e8",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f97c",
      "PARAM",
      [
        "storage",
        "002b5e6a",
        null,
        "string"
      ]
    ],
    [
      "0044f9e8",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "0044f9e8",
      "PARAM",
      [
        "storage",
        "00ca5cd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f944) · [`0044f9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f9b0) · [`0044f9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md#insn-0044f9f0)
- 新版 [`0044f984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044f984) · [`0044f9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044f9f0) · [`0044fa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044fa30)

~~~diff
- 0044f944 ["INT_ADD", "register:40f0:8", ["const:44f944:8", "const:4:8"]]
- 0044f944 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044f984 ["INT_ADD", "register:40f0:8", ["const:44f984:8", "const:4:8"]]
+ 0044f984 ["CALL", null, ["callee:00c57f70:8"]]
- 0044f944 bytes 8b202094
+ 0044f984 bytes 7b212094
- 0044f9b0 ["INT_ADD", "register:40f0:8", ["const:44f9b0:8", "const:4:8"]]
- 0044f9b0 ["CALL", null, ["callee:00561d34:8"]]
+ 0044f9f0 ["INT_ADD", "register:40f0:8", ["const:44f9f0:8", "const:4:8"]]
+ 0044f9f0 ["CALL", null, ["callee:00561d34:8"]]
- 0044f9b0 bytes d1480494
+ 0044f9f0 bytes d1480494
- 0044f9f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0044f9f0 ["INT_ADD", "register:40f0:8", ["const:44f9f0:8", "const:4:8"]]
- 0044f9f0 ["CALLIND", null, ["register:0:8"]]
+ 0044fa30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0044fa30 ["INT_ADD", "register:40f0:8", ["const:44fa30:8", "const:4:8"]]
+ 0044fa30 ["CALLIND", null, ["register:0:8"]]
- 0044f9f0 bytes 00013fd6
+ 0044fa30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-492759f175c30d20f8a3ce120480bcfd"></a>

### [`0044fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) → [`0044fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md) FUN_0044fd0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 10件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`0045a728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a728.md) [`0045a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a72c.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 10件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`0045a768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a768.md) [`0045a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a76c.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fde0",
      "incomplete_value": false,
      "site": "0044fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fda0",
      "incomplete_value": false,
      "site": "0044fda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "0044fd38",
      "incomplete_value": false,
      "site": "0044fd40",
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
            "const:f6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fcf8",
      "incomplete_value": false,
      "site": "0044fd00",
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
            "const:f2d:8"
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
      "definition_site": "0044fda4",
      "incomplete_value": true,
      "site": "0044fdac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fd64",
      "incomplete_value": true,
      "site": "0044fd6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
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
      "0044fd38",
      "PARAM",
      [
        "storage",
        "002c0f2d",
        null,
        "string"
      ]
    ],
    [
      "0044fda4",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fda4",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044fd38",
      "PARAM",
      [
        "storage",
        "002c0f6d",
        null,
        "string"
      ]
    ],
    [
      "0044fda4",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fda4",
      "PARAM",
      [
        "storage",
        "00ca5cd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044fd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fd00) · [`0044fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fd6c) · [`0044fcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md#insn-0044fcf0)
- 新版 [`0044fd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fd40) · [`0044fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fdac) · [`0044fd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fd30)

~~~diff
- 0044fd00 ["INT_ADD", "register:40f0:8", ["const:44fd00:8", "const:4:8"]]
- 0044fd00 ["CALL", null, ["callee:00c57f70:8"]]
+ 0044fd40 ["INT_ADD", "register:40f0:8", ["const:44fd40:8", "const:4:8"]]
+ 0044fd40 ["CALL", null, ["callee:00c57f70:8"]]
- 0044fd00 bytes 9c1f2094
+ 0044fd40 bytes 8c202094
- 0044fd6c ["INT_ADD", "register:40f0:8", ["const:44fd6c:8", "const:4:8"]]
- 0044fd6c ["CALL", null, ["callee:00561d34:8"]]
+ 0044fdac ["INT_ADD", "register:40f0:8", ["const:44fdac:8", "const:4:8"]]
+ 0044fdac ["CALL", null, ["callee:00561d34:8"]]
- 0044fd6c bytes e2470494
+ 0044fdac bytes e2470494
- 0044fcf0 ["INT_ADD", "register:40f0:8", ["const:44fcf0:8", "const:4:8"]]
- 0044fcf0 ["CALL", null, ["callee:0044b534:8"]]
+ 0044fd30 ["INT_ADD", "register:40f0:8", ["const:44fd30:8", "const:4:8"]]
+ 0044fd30 ["CALL", null, ["callee:0044b534:8"]]
- 0044fcf0 bytes 01eeff97
+ 0044fd30 bytes 01eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5886368a10af1468de323d199f86eac0"></a>

### [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) → [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) FUN_00450180

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 14件 [`0043db14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db14.md) [`00446540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446540.md) [`0044b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b120.md) [`00550bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf8.md) [`0055ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec40.md)
- 新版 呼出元 4件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 14件 [`0043db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md) [`00446580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446580.md) [`0044b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b160.md) [`00550c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md) [`0055ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004501e8",
      "value": [
        "leaf",
        "ram:55ec88:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004501a8",
      "value": [
        "leaf",
        "ram:55ec48:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004501dc",
      "incomplete_value": false,
      "site": "004501e8",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045019c",
      "incomplete_value": false,
      "site": "004501a8",
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
            "const:6c8:8"
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
      "definition_site": "0045024c",
      "incomplete_value": false,
      "site": "00450250",
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
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045020c",
      "incomplete_value": false,
      "site": "00450210",
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
            "const:6c0:8"
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
      "004501b0",
      "READ",
      [
        "storage",
        "00ca46c0",
        null,
        "undefined1"
      ]
    ],
    [
      "004501c0",
      "READ",
      [
        "storage",
        "00ca46d8",
        null,
        "undefined1"
      ]
    ],
    [
      "004501dc",
      "PARAM",
      [
        "storage",
        "00ca46c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004501b0",
      "READ",
      [
        "storage",
        "00ca4ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "004501c0",
      "READ",
      [
        "storage",
        "00ca4ad8",
        null,
        "undefined1"
      ]
    ],
    [
      "004501dc",
      "PARAM",
      [
        "storage",
        "00ca4ac8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004501a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-004501a8) · [`00450210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-00450210) · [`0045022c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md#insn-0045022c)
- 新版 [`004501e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-004501e8) · [`00450250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-00450250) · [`0045026c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-0045026c)

~~~diff
- 004501a8 ["INT_ADD", "register:40f0:8", ["const:4501a8:8", "const:4:8"]]
- 004501a8 ["CALL", null, ["ram:55ec48:8"]]
+ 004501e8 ["INT_ADD", "register:40f0:8", ["const:4501e8:8", "const:4:8"]]
+ 004501e8 ["CALL", null, ["ram:55ec88:8"]]
- 004501a8 bytes a83a0494
+ 004501e8 bytes a83a0494
- 00450210 ["INT_ADD", "register:40f0:8", ["const:450210:8", "const:4:8"]]
- 00450210 ["CALL", null, ["callee:00c57e50:8"]]
+ 00450250 ["INT_ADD", "register:40f0:8", ["const:450250:8", "const:4:8"]]
+ 00450250 ["CALL", null, ["callee:00c57e50:8"]]
- 00450210 bytes 101e2094
+ 00450250 bytes 001f2094
- 0045022c ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 0045022c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0045022c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0045022c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0045026c ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0045026c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0045026c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0045026c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0045022c bytes 21a01a91
+ 0045026c bytes 21a02a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd1af2f9ce00e1bf2fe2740899397e2d"></a>

### [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) → [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) FUN_0045035c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004503f4",
      "incomplete_value": true,
      "site": "004503f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004503b4",
      "incomplete_value": true,
      "site": "004503b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:165:8"
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
      "definition_site": "00450544",
      "incomplete_value": true,
      "site": "0045054c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450504",
      "incomplete_value": true,
      "site": "0045050c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b0:8"
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
      "004503e4",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "00450544",
      "READ",
      [
        "storage",
        "002c42b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00450588",
      "READ",
      [
        "storage",
        "002c4090",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004503e4",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "00450544",
      "READ",
      [
        "storage",
        "002c42f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00450588",
      "READ",
      [
        "storage",
        "002c40d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-00450374) · [`004503f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-004503f4) · [`00450368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md#insn-00450368)
- 新版 [`004503b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-004503b4) · [`00450434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-00450434) · [`004503a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-004503a8)

~~~diff
- 00450374 ["INT_ADD", "register:40f0:8", ["const:450374:8", "const:4:8"]]
- 00450374 ["CALL", null, ["callee:00596f2c:8"]]
+ 004503b4 ["INT_ADD", "register:40f0:8", ["const:4503b4:8", "const:4:8"]]
+ 004503b4 ["CALL", null, ["callee:00596f2c:8"]]
- 00450374 bytes de1a0594
+ 004503b4 bytes de1a0594
- 004503f4 ["INT_ADD", "register:40f0:8", ["const:4503f4:8", "const:4:8"]]
- 004503f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00450434 ["INT_ADD", "register:40f0:8", ["const:450434:8", "const:4:8"]]
+ 00450434 ["CALL", null, ["callee:00c57eb0:8"]]
- 004503f4 bytes af1d2094
+ 00450434 bytes 9f1e2094
- 00450368 ["INT_ADD", "register:40f0:8", ["const:450368:8", "const:4:8"]]
- 00450368 ["CALL", null, ["callee:00c53cd0:8"]]
+ 004503a8 ["INT_ADD", "register:40f0:8", ["const:4503a8:8", "const:4:8"]]
+ 004503a8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00450368 bytes 520d2094
+ 004503a8 bytes 4a0e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8cab03300c91a6d71b5dd0a8530d9ee"></a>

### [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) → [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) FUN_00450750

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 3件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 3件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00450774",
      "incomplete_value": true,
      "site": "00450794",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450734",
      "incomplete_value": true,
      "site": "00450754",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e36:8"
              ]
            ]
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
      "00450774",
      "READ",
      [
        "storage",
        "0029fe36",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00450774",
      "READ",
      [
        "storage",
        "0029ff03",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045072c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-0045072c) · [`0045076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-0045076c) · [`0045077c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md#insn-0045077c)
- 新版 [`0045076c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-0045076c) · [`004507ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-004507ac) · [`004507bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-004507bc)

~~~diff
- 0045072c ["COPY", "tmp:0:8", ["const:e36:8"]]
- 0045072c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045072c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045072c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045076c ["COPY", "tmp:0:8", ["const:f03:8"]]
+ 0045076c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045076c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045076c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045072c bytes 4ad93891
+ 0045076c bytes 4a0d3c91
- 0045076c ["COPY", "register:0:8", ["register:4048:8"]]
- 0045076c ["INT_ADD", "register:40f0:8", ["const:45076c:8", "const:4:8"]]
- 0045076c ["CALLIND", null, ["register:0:8"]]
+ 004507ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004507ac ["INT_ADD", "register:40f0:8", ["const:4507ac:8", "const:4:8"]]
+ 004507ac ["CALLIND", null, ["register:0:8"]]
- 0045076c bytes 20013fd6
+ 004507ac bytes 20013fd6
- 0045077c ["INT_ADD", "register:40f0:8", ["const:45077c:8", "const:4:8"]]
- 0045077c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004507bc ["INT_ADD", "register:40f0:8", ["const:4507bc:8", "const:4:8"]]
+ 004507bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0045077c bytes cd1c2094
+ 004507bc bytes bd1d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba299d95052e62fc57354ec85b194fd2"></a>

### [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) → [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) FUN_0045084c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004508fc",
      "incomplete_value": true,
      "site": "00450910",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004508bc",
      "incomplete_value": true,
      "site": "004508d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:808:8"
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
      "004508fc",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "004508fc",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004508fc",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "004508fc",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004508d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-004508d0) · [`0045086c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-0045086c) · [`004508a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md#insn-004508a4)
- 新版 [`00450910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-00450910) · [`004508ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-004508ac) · [`004508e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-004508e4)

~~~diff
- 004508d0 ["INT_ADD", "register:40f0:8", ["const:4508d0:8", "const:4:8"]]
- 004508d0 ["CALL", null, ["callee:004509b0:8"]]
+ 00450910 ["INT_ADD", "register:40f0:8", ["const:450910:8", "const:4:8"]]
+ 00450910 ["CALL", null, ["callee:004509b0:8"]]
- 004508d0 bytes 28000094
+ 00450910 bytes 28000094
- 0045086c ["INT_ADD", "register:40f0:8", ["const:45086c:8", "const:4:8"]]
- 0045086c ["CALL", null, ["callee:0043bb20:8"]]
+ 004508ac ["INT_ADD", "register:40f0:8", ["const:4508ac:8", "const:4:8"]]
+ 004508ac ["CALL", null, ["callee:0043bb20:8"]]
- 0045086c bytes 9dacff97
+ 004508ac bytes 9dacff97
- 004508a4 ["INT_ADD", "register:40f0:8", ["const:4508a4:8", "const:4:8"]]
- 004508a4 ["CALL", null, ["callee:0043bb20:8"]]
+ 004508e4 ["INT_ADD", "register:40f0:8", ["const:4508e4:8", "const:4:8"]]
+ 004508e4 ["CALL", null, ["callee:0043bb20:8"]]
- 004508a4 bytes 8facff97
+ 004508e4 bytes 8facff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9b6a45cb1f81674bd5508e5510c780"></a>

### [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) → [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) FUN_004509b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) · 呼出先 28件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044ff1c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md)
- 新版 呼出元 11件 [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 28件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.65% / 新版 91.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 19件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450b18",
      "incomplete_value": true,
      "site": "00450b20",
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
      "definition_site": "00450ad8",
      "incomplete_value": true,
      "site": "00450ae0",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00450b28",
      "incomplete_value": true,
      "site": "00450b28",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
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
      "definition_site": "00450ae8",
      "incomplete_value": true,
      "site": "00450ae8",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
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
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450b28",
      "incomplete_value": true,
      "site": "00450b28",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450ae8",
      "incomplete_value": true,
      "site": "00450ae8",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
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
      "00450b14",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00450b18",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450b1c",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00450b14",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00450b18",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450b1c",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450bb4) · [`00450bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450bf4) · [`00450c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md#insn-00450c30)
- 新版 [`00450bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450bf4) · [`00450c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450c34) · [`00450c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450c70)

~~~diff
- 00450bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00450bb4 ["INT_ADD", "register:40f0:8", ["const:450bb4:8", "const:4:8"]]
- 00450bb4 ["CALLIND", null, ["register:0:8"]]
+ 00450bf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00450bf4 ["INT_ADD", "register:40f0:8", ["const:450bf4:8", "const:4:8"]]
+ 00450bf4 ["CALLIND", null, ["register:0:8"]]
- 00450bb4 bytes 00013fd6
+ 00450bf4 bytes 00013fd6
- 00450bf4 ["INT_ADD", "register:40f0:8", ["const:450bf4:8", "const:4:8"]]
- 00450bf4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00450c34 ["INT_ADD", "register:40f0:8", ["const:450c34:8", "const:4:8"]]
+ 00450c34 ["CALL", null, ["callee:00c580b0:8"]]
- 00450bf4 bytes 2f1c2094
+ 00450c34 bytes 1f1d2094
- 00450c30 ["INT_ADD", "register:40f0:8", ["const:450c30:8", "const:4:8"]]
- 00450c30 ["CALL", null, ["callee:00c580b0:8"]]
+ 00450c70 ["INT_ADD", "register:40f0:8", ["const:450c70:8", "const:4:8"]]
+ 00450c70 ["CALL", null, ["callee:00c580b0:8"]]
- 00450c30 bytes 201c2094
+ 00450c70 bytes 101d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd23217694f900c11b7a8604f3897899"></a>

### [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) → [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) FUN_0045179c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 27件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00458ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ce8.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 27件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00458d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "004517e8",
      "incomplete_value": false,
      "site": "004517ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004517a8",
      "incomplete_value": false,
      "site": "004517ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "004517ec",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ],
    [
      "00451838",
      "READ",
      [
        "storage",
        "00c63368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004517ec",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "00451838",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-00451790) · [`004517a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-004517a8) · [`004517d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md#insn-004517d0)
- 新版 [`004517d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-004517d0) · [`004517e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-004517e8) · [`00451810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-00451810)

~~~diff
- 00451790 ["INT_ADD", "register:40f0:8", ["const:451790:8", "const:4:8"]]
- 00451790 ["CALL", null, ["callee:00c57e90:8"]]
+ 004517d0 ["INT_ADD", "register:40f0:8", ["const:4517d0:8", "const:4:8"]]
+ 004517d0 ["CALL", null, ["callee:00c57e90:8"]]
- 00451790 bytes c0182094
+ 004517d0 bytes b0192094
- 004517a8 ["COPY", "tmp:0:8", ["const:360:8"]]
- 004517a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004517a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004517a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004517e8 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 004517e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004517e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004517e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004517a8 bytes 08810d91
+ 004517e8 bytes 08811d91
- 004517d0 ["INT_ADD", "register:40f0:8", ["const:4517d0:8", "const:4:8"]]
- 004517d0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00451810 ["INT_ADD", "register:40f0:8", ["const:451810:8", "const:4:8"]]
+ 00451810 ["CALL", null, ["callee:0043bb20:8"]]
- 004517d0 bytes c4a8ff97
+ 00451810 bytes c4a8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0237c2f54e9f8eff529a1e4e6ddefb0"></a>

### [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) → [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) FUN_004518b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) · 呼出先 2件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md)
- 新版 呼出元 15件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) [`004973c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md) · 呼出先 2件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004518f4",
      "incomplete_value": true,
      "site": "004518f4",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004518b4",
      "incomplete_value": true,
      "site": "004518b4",
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
            "const:68:8"
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
      "definition_site": "004518f8",
      "incomplete_value": true,
      "site": "004518f8",
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
      "definition_site": "004518b8",
      "incomplete_value": true,
      "site": "004518b8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004518f0",
      "incomplete_value": true,
      "site": "00451900",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004518b0",
      "incomplete_value": true,
      "site": "004518c0",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
      "004518d4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "004518e0",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004518f0",
      "READ",
      [
        "storage",
        "00c92cf8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004518d4",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "004518e0",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004518f0",
      "READ",
      [
        "storage",
        "00c930f8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-00451894) · [`0045189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-0045189c) · [`004518a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md#insn-004518a0)
- 新版 [`004518d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md#insn-004518d4) · [`004518e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md#insn-004518e0)

~~~diff
- 00451894 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:818:8"]]
- 00451894 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004518d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c18:8"]]
+ 004518d4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00451894 bytes f70e44f9
+ 004518d4 bytes f70e46f9
- 0045189c ["COPY", "register:40d0:8", ["register:4000:8"]]
- 0045189c bytes fa0300aa
- 004518a0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:810:8"]]
- 004518a0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004518e0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c10:8"]]
+ 004518e0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 004518a0 bytes d60a44f9
+ 004518e0 bytes d60a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-691cdc1c3b3d1b16a419060782aea63d"></a>

### [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) → [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) FUN_004519d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) · 呼出先 7件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)
- 新版 呼出元 15件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) · 呼出先 7件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00451a84",
      "incomplete_value": false,
      "site": "00451a8c",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451a44",
      "incomplete_value": false,
      "site": "00451a4c",
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
            "const:e4d:8"
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
      "definition_site": "00451ad0",
      "incomplete_value": false,
      "site": "00451ad8",
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
            "const:e8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451a90",
      "incomplete_value": false,
      "site": "00451a98",
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
            "const:e4d:8"
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
      "definition_site": "00451b40",
      "incomplete_value": false,
      "site": "00451b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451b00",
      "incomplete_value": false,
      "site": "00451b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b9a:8"
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
      "00451a4c",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ],
    [
      "00451a84",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "00451ad0",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00451a4c",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ],
    [
      "00451a84",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00451ad0",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451a4c) · [`00451a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451a98) · [`00451ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md#insn-00451ad8)
- 新版 [`00451a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451a8c) · [`00451ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451ad8) · [`00451b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451b18)

~~~diff
- 00451a4c ["INT_ADD", "register:40f0:8", ["const:451a4c:8", "const:4:8"]]
- 00451a4c ["CALL", null, ["callee:004594d0:8"]]
+ 00451a8c ["INT_ADD", "register:40f0:8", ["const:451a8c:8", "const:4:8"]]
+ 00451a8c ["CALL", null, ["callee:004594d0:8"]]
- 00451a4c bytes 911e0094
+ 00451a8c bytes 911e0094
- 00451a98 ["INT_ADD", "register:40f0:8", ["const:451a98:8", "const:4:8"]]
- 00451a98 ["CALL", null, ["callee:004594d0:8"]]
+ 00451ad8 ["INT_ADD", "register:40f0:8", ["const:451ad8:8", "const:4:8"]]
+ 00451ad8 ["CALL", null, ["callee:004594d0:8"]]
- 00451a98 bytes 7e1e0094
+ 00451ad8 bytes 7e1e0094
- 00451ad8 ["INT_ADD", "register:40f0:8", ["const:451ad8:8", "const:4:8"]]
- 00451ad8 ["CALL", null, ["callee:00c58200:8"]]
+ 00451b18 ["INT_ADD", "register:40f0:8", ["const:451b18:8", "const:4:8"]]
+ 00451b18 ["CALL", null, ["callee:00c58200:8"]]
- 00451ad8 bytes ca182094
+ 00451b18 bytes ba192094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df28a059d709356e5a5fa553977ca999"></a>

### [`00451d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md) → [`00451d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md) FUN_00451d4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md) [`00c57dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md) [`00c581c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451d70",
      "incomplete_value": true,
      "site": "00451d78",
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
      "definition_site": "00451d30",
      "incomplete_value": true,
      "site": "00451d38",
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
      "definition_site": "00451d84",
      "incomplete_value": true,
      "site": "00451d84",
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
      "definition_site": "00451d44",
      "incomplete_value": true,
      "site": "00451d44",
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
      "definition_site": "00451d84",
      "incomplete_value": true,
      "site": "00451d84",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451d44",
      "incomplete_value": true,
      "site": "00451d44",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "00451d68",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00451d70",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451d74",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00451d68",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00451d70",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451d74",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d28) · [`00451d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d2c) · [`00451d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d0c.md#insn-00451d40)
- 新版 [`00451d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md#insn-00451d68) · [`00451d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md#insn-00451d80)

~~~diff
- 00451d28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:810:8"]]
- 00451d28 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451d68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c10:8"]]
+ 00451d68 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00451d28 bytes b50a44f9
+ 00451d68 bytes b50a46f9
- 00451d2c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00451d2c bytes f30300aa
- 00451d40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00451d40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451d80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00451d80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00451d40 bytes 29e143f9
+ 00451d80 bytes 29e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34d6ecd7c9f49c0fab97173b232a3faa"></a>

### [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) → [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) FUN_00451ed8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 16件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)
- 新版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 16件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.21% / 新版 93.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00451f60",
      "incomplete_value": false,
      "site": "00451f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451f20",
      "incomplete_value": false,
      "site": "00451f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "00451f88",
      "incomplete_value": false,
      "site": "00451f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451f48",
      "incomplete_value": false,
      "site": "00451f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00451fc4",
      "incomplete_value": true,
      "site": "00451fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451f84",
      "incomplete_value": true,
      "site": "00451f84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
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
      "00451f20",
      "PARAM",
      [
        "storage",
        "002b7f52",
        null,
        "string"
      ]
    ],
    [
      "00451f68",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "00451f88",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00451f20",
      "PARAM",
      [
        "storage",
        "002b7f92",
        null,
        "string"
      ]
    ],
    [
      "00451f68",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "00451f88",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451ee8) · [`00451ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451ed8) · [`00451ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md#insn-00451ee0)
- 新版 [`00451f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f28) · [`00451f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f18) · [`00451f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f20)

~~~diff
- 00451ee8 ["INT_ADD", "register:40f0:8", ["const:451ee8:8", "const:4:8"]]
- 00451ee8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00451f28 ["INT_ADD", "register:40f0:8", ["const:451f28:8", "const:4:8"]]
+ 00451f28 ["CALL", null, ["callee:00c57f70:8"]]
- 00451ee8 bytes 22172094
+ 00451f28 bytes 12182094
- 00451ed8 ["INT_ADD", "register:40f0:8", ["const:451ed8:8", "const:4:8"]]
- 00451ed8 ["CALL", null, ["callee:0044b3f4:8"]]
+ 00451f18 ["INT_ADD", "register:40f0:8", ["const:451f18:8", "const:4:8"]]
+ 00451f18 ["CALL", null, ["callee:0044b3f4:8"]]
- 00451ed8 bytes 37e5ff97
+ 00451f18 bytes 37e5ff97
- 00451ee0 ["COPY", "tmp:0:8", ["const:f52:8"]]
- 00451ee0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00451ee0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00451ee0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00451f20 ["COPY", "tmp:0:8", ["const:f92:8"]]
+ 00451f20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00451f20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00451f20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00451ee0 bytes 21483d91
+ 00451f20 bytes 21483e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c93cf87bfb75eea38dc6115d134630c"></a>

### [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) → [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) FUN_004524e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) · 呼出先 20件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00452b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452b84.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)
- 新版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 20件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`00452bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452bc4.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.31% / 新版 86.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004525bc",
      "incomplete_value": true,
      "site": "004525bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045257c",
      "incomplete_value": true,
      "site": "0045257c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004525c4",
      "incomplete_value": true,
      "site": "004525c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452584",
      "incomplete_value": true,
      "site": "00452584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004525d4",
      "incomplete_value": true,
      "site": "004525d4",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452594",
      "incomplete_value": true,
      "site": "00452594",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045252c",
      "READ",
      [
        "storage",
        "00ca4708",
        null,
        "undefined1"
      ]
    ],
    [
      "0045253c",
      "READ",
      [
        "storage",
        "00ca4728",
        null,
        "undefined1"
      ]
    ],
    [
      "00452548",
      "PARAM",
      [
        "storage",
        "00ca46e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045252c",
      "READ",
      [
        "storage",
        "00ca4b08",
        null,
        "undefined1"
      ]
    ],
    [
      "0045253c",
      "READ",
      [
        "storage",
        "00ca4b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00452548",
      "PARAM",
      [
        "storage",
        "00ca4ae0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045250c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md#insn-0045250c) · [`00452558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md#insn-00452558)
- 新版 [`0045254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md#insn-0045254c) · [`00452598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md#insn-00452598) · [`00452558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md#insn-00452558)

~~~diff
- 0045250c ["INT_ADD", "register:40f0:8", ["const:45250c:8", "const:4:8"]]
- 0045250c ["CALL", null, ["callee:00c580e0:8"]]
+ 0045254c ["INT_ADD", "register:40f0:8", ["const:45254c:8", "const:4:8"]]
+ 0045254c ["CALL", null, ["callee:00c580e0:8"]]
- 0045250c bytes f5152094
+ 0045254c bytes e5162094
- 00452558 ["INT_ADD", "register:40f0:8", ["const:452558:8", "const:4:8"]]
- 00452558 ["CALL", null, ["callee:0045ca98:8"]]
+ 00452598 ["INT_ADD", "register:40f0:8", ["const:452598:8", "const:4:8"]]
+ 00452598 ["CALL", null, ["callee:0045ca98:8"]]
- 00452558 bytes 40290094
+ 00452598 bytes 40290094
+ 00452558 ["COPY", "register:40b0:8", ["const:ca4000:8"]]
+ 00452558 bytes 964200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02dba1d6a0265cb4cea53c4428aa9041"></a>

### [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) → [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) FUN_00452c54

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`0079b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`008a6e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6e08.md) · 呼出先 24件 [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00453198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453198.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md)
- 新版 呼出元 5件 [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`008a6e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6e4c.md) · 呼出先 24件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004531d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004531d8.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d28",
      "incomplete_value": true,
      "site": "00452d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452ce8",
      "incomplete_value": true,
      "site": "00452ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d30",
      "incomplete_value": true,
      "site": "00452d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452cf0",
      "incomplete_value": true,
      "site": "00452cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d40",
      "incomplete_value": true,
      "site": "00452d40",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452d00",
      "incomplete_value": true,
      "site": "00452d00",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00452c98",
      "READ",
      [
        "storage",
        "00ca4760",
        null,
        "undefined1"
      ]
    ],
    [
      "00452ca8",
      "READ",
      [
        "storage",
        "00ca4780",
        null,
        "undefined1"
      ]
    ],
    [
      "00452cb4",
      "PARAM",
      [
        "storage",
        "00ca4734",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00452c98",
      "READ",
      [
        "storage",
        "00ca4b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00452ca8",
      "READ",
      [
        "storage",
        "00ca4b80",
        null,
        "undefined1"
      ]
    ],
    [
      "00452cb4",
      "PARAM",
      [
        "storage",
        "00ca4b34",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00452c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md#insn-00452c78) · [`00452cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md#insn-00452cc4)
- 新版 [`00452cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md#insn-00452cb8) · [`00452d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md#insn-00452d04) · [`00452cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md#insn-00452cc4)

~~~diff
- 00452c78 ["INT_ADD", "register:40f0:8", ["const:452c78:8", "const:4:8"]]
- 00452c78 ["CALL", null, ["callee:00c580e0:8"]]
+ 00452cb8 ["INT_ADD", "register:40f0:8", ["const:452cb8:8", "const:4:8"]]
+ 00452cb8 ["CALL", null, ["callee:00c580e0:8"]]
- 00452c78 bytes 1a142094
+ 00452cb8 bytes 0a152094
- 00452cc4 ["INT_ADD", "register:40f0:8", ["const:452cc4:8", "const:4:8"]]
- 00452cc4 ["CALL", null, ["callee:0045db78:8"]]
+ 00452d04 ["INT_ADD", "register:40f0:8", ["const:452d04:8", "const:4:8"]]
+ 00452d04 ["CALL", null, ["callee:0045db78:8"]]
- 00452cc4 bytes 9d2b0094
+ 00452d04 bytes 9d2b0094
+ 00452cc4 ["COPY", "register:40c0:8", ["const:ca4000:8"]]
+ 00452cc4 bytes 984200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb612198dc8da18704317057069e761"></a>

### [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) → [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) FUN_004532b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b404.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md)
- 新版 呼出元 1件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b444.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453358",
      "incomplete_value": false,
      "site": "00453360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453318",
      "incomplete_value": false,
      "site": "00453320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "0045336c",
      "incomplete_value": false,
      "site": "0045336c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045332c",
      "incomplete_value": false,
      "site": "0045332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00453410",
      "incomplete_value": true,
      "site": "00453420",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:91b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004533d0",
      "incomplete_value": true,
      "site": "004533e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8db:8"
              ]
            ]
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
      "0045330c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b404"
      ]
    ],
    [
      "00453314",
      "PARAM",
      [
        "storage",
        "002c0f4a",
        null,
        "string"
      ]
    ],
    [
      "00453360",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045330c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b444"
      ]
    ],
    [
      "00453314",
      "PARAM",
      [
        "storage",
        "002c0f8a",
        null,
        "string"
      ]
    ],
    [
      "00453360",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004532cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-004532cc) · [`004532dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-004532dc) · [`0045331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md#insn-0045331c)
- 新版 [`0045330c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md#insn-0045330c) · [`0045331c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md#insn-0045331c)

~~~diff
- 004532cc ["INT_ADD", "register:40f0:8", ["const:4532cc:8", "const:4:8"]]
- 004532cc ["CALL", null, ["ram:44b404:8"]]
+ 0045330c ["INT_ADD", "register:40f0:8", ["const:45330c:8", "const:4:8"]]
+ 0045330c ["CALL", null, ["ram:44b444:8"]]
- 004532cc bytes 4ee0ff97
+ 0045330c bytes 4ee0ff97
- 004532dc ["INT_ADD", "register:40f0:8", ["const:4532dc:8", "const:4:8"]]
- 004532dc ["CALL", null, ["callee:00c57f70:8"]]
+ 0045331c ["INT_ADD", "register:40f0:8", ["const:45331c:8", "const:4:8"]]
+ 0045331c ["CALL", null, ["callee:00c57f70:8"]]
- 004532dc bytes 25122094
+ 0045331c bytes 15132094
- 0045331c ["COPY", "register:40e0:8", ["register:4000:8"]]
- 0045331c bytes fc0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b157fd4401abebaf43883873ef37dd"></a>

### [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) → [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) FUN_004539dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 12件 [`00453278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453278.md) [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`0045ee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee1c.md) [`0045f9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9fc.md) [`0045fa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fa4c.md)
- 新版 呼出元 2件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 12件 [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`0045ee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee5c.md) [`0045fa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa3c.md) [`0045fa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453a34",
      "incomplete_value": false,
      "site": "00453a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004539f4",
      "incomplete_value": false,
      "site": "00453a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "definition_site": "00453a68",
      "incomplete_value": false,
      "site": "00453a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453a28",
      "incomplete_value": false,
      "site": "00453a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "definition_site": "00453adc",
      "incomplete_value": false,
      "site": "00453adc",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453a9c",
      "incomplete_value": false,
      "site": "00453a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "00453a44",
      "DATA",
      [
        "storage",
        "00c63a70",
        null,
        "pointer"
      ]
    ],
    [
      "00453a70",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00453adc",
      "DATA",
      [
        "storage",
        "00c63c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00453a44",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ],
    [
      "00453a70",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ],
    [
      "00453adc",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-00453a5c) · [`00453a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-00453a70) · [`004539e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md#insn-004539e8)
- 新版 [`00453a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453a9c) · [`00453ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453ab0) · [`00453a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453a28)

~~~diff
- 00453a5c ["INT_ADD", "register:40f0:8", ["const:453a5c:8", "const:4:8"]]
- 00453a5c ["CALL", null, ["callee:00c580e0:8"]]
+ 00453a9c ["INT_ADD", "register:40f0:8", ["const:453a9c:8", "const:4:8"]]
+ 00453a9c ["CALL", null, ["callee:00c580e0:8"]]
- 00453a5c bytes a1102094
+ 00453a9c bytes 91112094
- 00453a70 ["INT_ADD", "register:40f0:8", ["const:453a70:8", "const:4:8"]]
- 00453a70 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00453ab0 ["INT_ADD", "register:40f0:8", ["const:453ab0:8", "const:4:8"]]
+ 00453ab0 ["CALL", null, ["callee:00c53cd0:8"]]
- 00453a70 bytes 90ff1f94
+ 00453ab0 bytes 88002094
- 004539e8 ["INT_ADD", "register:40f0:8", ["const:4539e8:8", "const:4:8"]]
- 004539e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00453a28 ["INT_ADD", "register:40f0:8", ["const:453a28:8", "const:4:8"]]
+ 00453a28 ["CALL", null, ["callee:00c57e90:8"]]
- 004539e8 bytes 2a102094
+ 00453a28 bytes 1a112094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf090017f3528572bb807b501a3d812"></a>

### [`00453c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md) → [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) FUN_00453cb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b454.md) [`0045080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045080c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)
- 新版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b494.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453d44",
      "incomplete_value": false,
      "site": "00453d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d04",
      "incomplete_value": false,
      "site": "00453d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "00453d60",
      "incomplete_value": false,
      "site": "00453d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d20",
      "incomplete_value": false,
      "site": "00453d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00453e94",
      "incomplete_value": true,
      "site": "00453e9c",
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
      "definition_site": "00453e54",
      "incomplete_value": true,
      "site": "00453e5c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00453cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b454"
      ]
    ],
    [
      "00453d04",
      "PARAM",
      [
        "storage",
        "002ac5ce",
        null,
        "string"
      ]
    ],
    [
      "00453d4c",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00453cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b494"
      ]
    ],
    [
      "00453d04",
      "PARAM",
      [
        "storage",
        "002ac60e",
        null,
        "string"
      ]
    ],
    [
      "00453d4c",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453cbc) · [`00453ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453ccc) · [`00453cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/00453c70.md#insn-00453cfc)
- 新版 [`00453cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453cfc) · [`00453d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453d0c) · [`00453d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453d3c)

~~~diff
- 00453cbc ["INT_ADD", "register:40f0:8", ["const:453cbc:8", "const:4:8"]]
- 00453cbc ["CALL", null, ["ram:44b454:8"]]
+ 00453cfc ["INT_ADD", "register:40f0:8", ["const:453cfc:8", "const:4:8"]]
+ 00453cfc ["CALL", null, ["ram:44b494:8"]]
- 00453cbc bytes e6ddff97
+ 00453cfc bytes e6ddff97
- 00453ccc ["INT_ADD", "register:40f0:8", ["const:453ccc:8", "const:4:8"]]
- 00453ccc ["CALL", null, ["callee:00c57f70:8"]]
+ 00453d0c ["INT_ADD", "register:40f0:8", ["const:453d0c:8", "const:4:8"]]
+ 00453d0c ["CALL", null, ["callee:00c57f70:8"]]
- 00453ccc bytes a90f2094
+ 00453d0c bytes 99102094
- 00453cfc ["INT_ADD", "register:40f0:8", ["const:453cfc:8", "const:4:8"]]
- 00453cfc ["CALL", null, ["callee:00c57e90:8"]]
+ 00453d3c ["INT_ADD", "register:40f0:8", ["const:453d3c:8", "const:4:8"]]
+ 00453d3c ["CALL", null, ["callee:00c57e90:8"]]
- 00453cfc bytes 650f2094
+ 00453d3c bytes 55102094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e5b9d52aefdcb1cd25097a2bb9743ff"></a>

### [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) → [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) FUN_0045440c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 15件 [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) [`004600c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600c4.md) [`004600c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600c8.md) [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md)
- 新版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 15件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`00460104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460104.md) [`00460108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460108.md) [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.37% / 新版 93.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045453c",
      "incomplete_value": true,
      "site": "0045454c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:366:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004544fc",
      "incomplete_value": true,
      "site": "0045450c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:28a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00454540",
      "incomplete_value": true,
      "site": "00454550",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00454500",
      "incomplete_value": true,
      "site": "00454510",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00454544",
      "incomplete_value": true,
      "site": "00454554",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454504",
      "incomplete_value": true,
      "site": "00454514",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "00454444",
      "PARAM",
      [
        "storage",
        "002b8dc6",
        null,
        "string"
      ]
    ],
    [
      "004544b4",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "004544b4",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00454444",
      "PARAM",
      [
        "storage",
        "002b8e06",
        null,
        "string"
      ]
    ],
    [
      "004544b4",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "004544b4",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-0045440c) · [`0045447c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-0045447c) · [`00454530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md#insn-00454530)
- 新版 [`0045444c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-0045444c) · [`004544bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-004544bc) · [`00454570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-00454570)

~~~diff
- 0045440c ["INT_ADD", "register:40f0:8", ["const:45440c:8", "const:4:8"]]
- 0045440c ["CALL", null, ["callee:00c57f70:8"]]
+ 0045444c ["INT_ADD", "register:40f0:8", ["const:45444c:8", "const:4:8"]]
+ 0045444c ["CALL", null, ["callee:00c57f70:8"]]
- 0045440c bytes d90d2094
+ 0045444c bytes c90e2094
- 0045447c ["INT_ADD", "register:40f0:8", ["const:45447c:8", "const:4:8"]]
- 0045447c ["CALL", null, ["callee:00561d34:8"]]
+ 004544bc ["INT_ADD", "register:40f0:8", ["const:4544bc:8", "const:4:8"]]
+ 004544bc ["CALL", null, ["callee:00561d34:8"]]
- 0045447c bytes 1e360494
+ 004544bc bytes 1e360494
- 00454530 ["INT_ADD", "register:40f0:8", ["const:454530:8", "const:4:8"]]
- 00454530 ["CALL", null, ["callee:00561064:8"]]
+ 00454570 ["INT_ADD", "register:40f0:8", ["const:454570:8", "const:4:8"]]
+ 00454570 ["CALL", null, ["callee:00561064:8"]]
- 00454530 bytes bd320494
+ 00454570 bytes bd320494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-990a889e0fe0c08ec6e9dbc0f59bdc15"></a>

### [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) → [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) FUN_00454844

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009bd650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00460700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460700.md) [`004621c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004621c4.md)
- 新版 呼出元 1件 [`009bd7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd7ec.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00460740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460740.md) [`00462204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462204.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454984",
      "incomplete_value": false,
      "site": "00454984",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454944",
      "incomplete_value": false,
      "site": "00454944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454a24",
      "incomplete_value": false,
      "site": "00454a24",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004549e4",
      "incomplete_value": false,
      "site": "004549e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00454884",
      "incomplete_value": false,
      "site": "0045488c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454844",
      "incomplete_value": false,
      "site": "0045484c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:fc1:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00454884",
      "PARAM",
      [
        "storage",
        "002b9fc1",
        null,
        "string"
      ]
    ],
    [
      "00454984",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ],
    [
      "00454a24",
      "DATA",
      [
        "storage",
        "00c63e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00454884",
      "PARAM",
      [
        "storage",
        "002ba001",
        null,
        "string"
      ]
    ],
    [
      "00454984",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ],
    [
      "00454a24",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045484c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-0045484c) · [`00454a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-00454a48) · [`0045483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md#insn-0045483c)
- 新版 [`0045488c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-0045488c) · [`00454a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-00454a88) · [`0045487c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-0045487c)

~~~diff
- 0045484c ["INT_ADD", "register:40f0:8", ["const:45484c:8", "const:4:8"]]
- 0045484c ["CALL", null, ["callee:00c57f70:8"]]
+ 0045488c ["INT_ADD", "register:40f0:8", ["const:45488c:8", "const:4:8"]]
+ 0045488c ["CALL", null, ["callee:00c57f70:8"]]
- 0045484c bytes c90c2094
+ 0045488c bytes b90d2094
- 00454a48 ["INT_ADD", "register:40f0:8", ["const:454a48:8", "const:4:8"]]
- 00454a48 ["CALL", null, ["callee:004509b0:8"]]
+ 00454a88 ["INT_ADD", "register:40f0:8", ["const:454a88:8", "const:4:8"]]
+ 00454a88 ["CALL", null, ["callee:004509b0:8"]]
- 00454a48 bytes caefff97
+ 00454a88 bytes caefff97
- 0045483c ["INT_ADD", "register:40f0:8", ["const:45483c:8", "const:4:8"]]
- 0045483c ["CALL", null, ["callee:0044b700:8"]]
+ 0045487c ["INT_ADD", "register:40f0:8", ["const:45487c:8", "const:4:8"]]
+ 0045487c ["CALL", null, ["callee:0044b700:8"]]
- 0045483c bytes a1dbff97
+ 0045487c bytes a1dbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c6fc1ddb067364e4d58740a25d20ef"></a>

### [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) → [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) FUN_00454d28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ba7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00462554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462554.md) [`00462814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462814.md)
- 新版 呼出元 1件 [`009ba95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba95c.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00462594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462594.md) [`00462854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462854.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454f00",
      "incomplete_value": false,
      "site": "00454f00",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454ec0",
      "incomplete_value": false,
      "site": "00454ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454fa0",
      "incomplete_value": false,
      "site": "00454fa0",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454f60",
      "incomplete_value": false,
      "site": "00454f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00454d6c",
      "incomplete_value": false,
      "site": "00454d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454d2c",
      "incomplete_value": false,
      "site": "00454d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00454d6c",
      "PARAM",
      [
        "storage",
        "002ad5f0",
        null,
        "string"
      ]
    ],
    [
      "00454dcc",
      "PARAM",
      [
        "storage",
        "002a3e95",
        null,
        "string"
      ]
    ],
    [
      "00454f00",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00454d6c",
      "PARAM",
      [
        "storage",
        "002ad630",
        null,
        "string"
      ]
    ],
    [
      "00454dcc",
      "PARAM",
      [
        "storage",
        "002a3f62",
        null,
        "string"
      ]
    ],
    [
      "00454f00",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00454d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454d34) · [`00454d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454d94) · [`00454fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md#insn-00454fc4)
- 新版 [`00454d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00454d74) · [`00454dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00454dd4) · [`00455004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00455004)

~~~diff
- 00454d34 ["INT_ADD", "register:40f0:8", ["const:454d34:8", "const:4:8"]]
- 00454d34 ["CALL", null, ["callee:00c57f70:8"]]
+ 00454d74 ["INT_ADD", "register:40f0:8", ["const:454d74:8", "const:4:8"]]
+ 00454d74 ["CALL", null, ["callee:00c57f70:8"]]
- 00454d34 bytes 8f0b2094
+ 00454d74 bytes 7f0c2094
- 00454d94 ["INT_ADD", "register:40f0:8", ["const:454d94:8", "const:4:8"]]
- 00454d94 ["CALL", null, ["callee:00c57f70:8"]]
+ 00454dd4 ["INT_ADD", "register:40f0:8", ["const:454dd4:8", "const:4:8"]]
+ 00454dd4 ["CALL", null, ["callee:00c57f70:8"]]
- 00454d94 bytes 770b2094
+ 00454dd4 bytes 670c2094
- 00454fc4 ["INT_ADD", "register:40f0:8", ["const:454fc4:8", "const:4:8"]]
- 00454fc4 ["CALL", null, ["callee:004509b0:8"]]
+ 00455004 ["INT_ADD", "register:40f0:8", ["const:455004:8", "const:4:8"]]
+ 00455004 ["CALL", null, ["callee:004509b0:8"]]
- 00454fc4 bytes 6beeff97
+ 00455004 bytes 6beeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e6efd8fe808210bc276f0e61e6ed12e"></a>

### [`004552b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md) → [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) FUN_004552f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) [`00a9a608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a608.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b6c0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00462ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ad4.md) [`00462f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462f50.md)
- 新版 呼出元 2件 [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) [`00a9a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a804.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00462b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b14.md) [`00462f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455438",
      "incomplete_value": false,
      "site": "00455438",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004553f8",
      "incomplete_value": false,
      "site": "004553f8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004554d8",
      "incomplete_value": false,
      "site": "004554d8",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455498",
      "incomplete_value": false,
      "site": "00455498",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00455338",
      "incomplete_value": false,
      "site": "00455340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:63e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004552f8",
      "incomplete_value": false,
      "site": "00455300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:5fe:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00455338",
      "PARAM",
      [
        "storage",
        "002ad5fe",
        null,
        "string"
      ]
    ],
    [
      "00455438",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ],
    [
      "004554d8",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00455338",
      "PARAM",
      [
        "storage",
        "002ad63e",
        null,
        "string"
      ]
    ],
    [
      "00455438",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ],
    [
      "004554d8",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-00455300) · [`004554fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-004554fc) · [`004552f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/004552b8.md#insn-004552f0)
- 新版 [`00455340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-00455340) · [`0045553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-0045553c) · [`00455330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-00455330)

~~~diff
- 00455300 ["INT_ADD", "register:40f0:8", ["const:455300:8", "const:4:8"]]
- 00455300 ["CALL", null, ["callee:00c57f70:8"]]
+ 00455340 ["INT_ADD", "register:40f0:8", ["const:455340:8", "const:4:8"]]
+ 00455340 ["CALL", null, ["callee:00c57f70:8"]]
- 00455300 bytes 1c0a2094
+ 00455340 bytes 0c0b2094
- 004554fc ["INT_ADD", "register:40f0:8", ["const:4554fc:8", "const:4:8"]]
- 004554fc ["CALL", null, ["callee:004509b0:8"]]
+ 0045553c ["INT_ADD", "register:40f0:8", ["const:45553c:8", "const:4:8"]]
+ 0045553c ["CALL", null, ["callee:004509b0:8"]]
- 004554fc bytes 1dedff97
+ 0045553c bytes 1dedff97
- 004552f0 ["INT_ADD", "register:40f0:8", ["const:4552f0:8", "const:4:8"]]
- 004552f0 ["CALL", null, ["callee:0044b700:8"]]
+ 00455330 ["INT_ADD", "register:40f0:8", ["const:455330:8", "const:4:8"]]
+ 00455330 ["CALL", null, ["callee:0044b700:8"]]
- 004552f0 bytes f4d8ff97
+ 00455330 bytes f4d8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2eb425d4da81ed09df059b2b4c0d4d"></a>

### [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) → [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) FUN_004557dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008861c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md) [`00463218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463218.md)
- 新版 呼出元 1件 [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md) [`00463258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463258.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455868",
      "incomplete_value": false,
      "site": "00455870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455828",
      "incomplete_value": false,
      "site": "00455830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "0045588c",
      "incomplete_value": false,
      "site": "0045588c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045584c",
      "incomplete_value": false,
      "site": "0045584c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00455970",
      "incomplete_value": false,
      "site": "00455970",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455930",
      "incomplete_value": false,
      "site": "00455930",
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
            "const:118:8"
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
      "00455820",
      "PARAM",
      [
        "storage",
        "002ab21f",
        null,
        "string"
      ]
    ],
    [
      "00455870",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "0045588c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00455820",
      "PARAM",
      [
        "storage",
        "002ab2ec",
        null,
        "string"
      ]
    ],
    [
      "00455870",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "0045588c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004557e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-004557e8) · [`00455828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-00455828) · [`00455a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md#insn-00455a34)
- 新版 [`00455828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455828) · [`00455868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455868) · [`00455a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455a74)

~~~diff
- 004557e8 ["INT_ADD", "register:40f0:8", ["const:4557e8:8", "const:4:8"]]
- 004557e8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00455828 ["INT_ADD", "register:40f0:8", ["const:455828:8", "const:4:8"]]
+ 00455828 ["CALL", null, ["callee:00c57f70:8"]]
- 004557e8 bytes e2082094
+ 00455828 bytes d2092094
- 00455828 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00455828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00455868 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 00455868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00455868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00455868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455828 bytes 08411a91
+ 00455868 bytes 08412a91
- 00455a34 ["INT_ADD", "register:40f0:8", ["const:455a34:8", "const:4:8"]]
- 00455a34 ["CALL", null, ["callee:004509b0:8"]]
+ 00455a74 ["INT_ADD", "register:40f0:8", ["const:455a74:8", "const:4:8"]]
+ 00455a74 ["CALL", null, ["callee:004509b0:8"]]
- 00455a34 bytes cfebff97
+ 00455a74 bytes cfebff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a13213a43718c37b824ad00e6c4b1e"></a>

### [`00455d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) → [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) FUN_00455d58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0045bd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd8c.md)
- 新版 呼出元 1件 [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.78% / 新版 94.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455de8",
      "incomplete_value": false,
      "site": "00455df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455da8",
      "incomplete_value": false,
      "site": "00455db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "00455e10",
      "incomplete_value": false,
      "site": "00455e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455dd0",
      "incomplete_value": false,
      "site": "00455dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00455e48",
      "incomplete_value": true,
      "site": "00455e48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455e08",
      "incomplete_value": true,
      "site": "00455e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ece:8"
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
      "00455da0",
      "PARAM",
      [
        "storage",
        "002b4b61",
        null,
        "string"
      ]
    ],
    [
      "00455df0",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "00455e10",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00455da0",
      "PARAM",
      [
        "storage",
        "002b4ba1",
        null,
        "string"
      ]
    ],
    [
      "00455df0",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "00455e10",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455d68) · [`00455da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455da8) · [`00455ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md#insn-00455ff0)
- 新版 [`00455da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00455da8) · [`00455de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00455de8) · [`00456030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00456030)

~~~diff
- 00455d68 ["INT_ADD", "register:40f0:8", ["const:455d68:8", "const:4:8"]]
- 00455d68 ["CALL", null, ["callee:00c57f70:8"]]
+ 00455da8 ["INT_ADD", "register:40f0:8", ["const:455da8:8", "const:4:8"]]
+ 00455da8 ["CALL", null, ["callee:00c57f70:8"]]
- 00455d68 bytes 82072094
+ 00455da8 bytes 72082094
- 00455da8 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00455da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00455de8 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 00455de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00455de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00455de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455da8 bytes 08411a91
+ 00455de8 bytes 08412a91
- 00455ff0 ["INT_ADD", "register:40f0:8", ["const:455ff0:8", "const:4:8"]]
- 00455ff0 ["CALL", null, ["callee:004509b0:8"]]
+ 00456030 ["INT_ADD", "register:40f0:8", ["const:456030:8", "const:4:8"]]
+ 00456030 ["CALL", null, ["callee:004509b0:8"]]
- 00455ff0 bytes 60eaff97
+ 00456030 bytes 60eaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f1573a16b9fbe74f2b3753323a09e4"></a>

### [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) → [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) FUN_00456324

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00463f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463f98.md) [`00464c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464c9c.md)
- 新版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00463fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463fd8.md) [`00464cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464cdc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00456464",
      "incomplete_value": false,
      "site": "00456464",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456424",
      "incomplete_value": false,
      "site": "00456424",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00456504",
      "incomplete_value": false,
      "site": "00456504",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004564c4",
      "incomplete_value": false,
      "site": "004564c4",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00456364",
      "incomplete_value": false,
      "site": "0045636c",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456324",
      "incomplete_value": false,
      "site": "0045632c",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00456364",
      "PARAM",
      [
        "storage",
        "002ac5e0",
        null,
        "string"
      ]
    ],
    [
      "00456464",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ],
    [
      "00456504",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00456364",
      "PARAM",
      [
        "storage",
        "002ac620",
        null,
        "string"
      ]
    ],
    [
      "00456464",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ],
    [
      "00456504",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045632c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-0045632c) · [`00456528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-00456528) · [`0045631c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md#insn-0045631c)
- 新版 [`0045636c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-0045636c) · [`00456568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-00456568) · [`0045635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-0045635c)

~~~diff
- 0045632c ["INT_ADD", "register:40f0:8", ["const:45632c:8", "const:4:8"]]
- 0045632c ["CALL", null, ["callee:00c57f70:8"]]
+ 0045636c ["INT_ADD", "register:40f0:8", ["const:45636c:8", "const:4:8"]]
+ 0045636c ["CALL", null, ["callee:00c57f70:8"]]
- 0045632c bytes 11062094
+ 0045636c bytes 01072094
- 00456528 ["INT_ADD", "register:40f0:8", ["const:456528:8", "const:4:8"]]
- 00456528 ["CALL", null, ["callee:004509b0:8"]]
+ 00456568 ["INT_ADD", "register:40f0:8", ["const:456568:8", "const:4:8"]]
+ 00456568 ["CALL", null, ["callee:004509b0:8"]]
- 00456528 bytes 12e9ff97
+ 00456568 bytes 12e9ff97
- 0045631c ["INT_ADD", "register:40f0:8", ["const:45631c:8", "const:4:8"]]
- 0045631c ["CALL", null, ["callee:0044b4e4:8"]]
+ 0045635c ["INT_ADD", "register:40f0:8", ["const:45635c:8", "const:4:8"]]
+ 0045635c ["CALL", null, ["callee:0044b4e4:8"]]
- 0045631c bytes 62d4ff97
+ 0045635c bytes 62d4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e82e87a90058eaf30a2c7fc6791f3e1"></a>

### [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) → [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) FUN_00456808

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`00886a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886a64.md) · 呼出先 11件 [`00464fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464fa4.md) [`00560fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fd4.md) [`00561024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561024.md) [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) [`00561868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md)
- 新版 呼出元 2件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) · 呼出先 11件 [`00464fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464fe4.md) [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md) [`005618a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.13% / 新版 91.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00456894",
      "incomplete_value": true,
      "site": "00456894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456854",
      "incomplete_value": true,
      "site": "00456854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f6e:8"
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
      "definition_site": "00456960",
      "incomplete_value": true,
      "site": "00456960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456920",
      "incomplete_value": true,
      "site": "00456920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e7:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00456964",
      "incomplete_value": true,
      "site": "00456964",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00456924",
      "incomplete_value": true,
      "site": "00456924",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00456844",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "00456844",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ],
    [
      "0045687c",
      "READ",
      [
        "storage",
        "002b7f6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00456844",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "00456844",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "0045687c",
      "READ",
      [
        "storage",
        "002b7fae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-0045680c) · [`00456814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-00456814) · [`004568e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md#insn-004568e0)
- 新版 [`0045684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-0045684c) · [`00456854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-00456854) · [`00456920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-00456920)

~~~diff
- 0045680c ["INT_ADD", "register:40f0:8", ["const:45680c:8", "const:4:8"]]
- 0045680c ["CALL", null, ["callee:00561d34:8"]]
+ 0045684c ["INT_ADD", "register:40f0:8", ["const:45684c:8", "const:4:8"]]
+ 0045684c ["CALL", null, ["callee:00561d34:8"]]
- 0045680c bytes 3a2d0494
+ 0045684c bytes 3a2d0494
- 00456814 ["INT_ADD", "register:40f0:8", ["const:456814:8", "const:4:8"]]
- 00456814 ["CALL", null, ["callee:005618a8:8"]]
+ 00456854 ["INT_ADD", "register:40f0:8", ["const:456854:8", "const:4:8"]]
+ 00456854 ["CALL", null, ["callee:005618a8:8"]]
- 00456814 bytes 152c0494
+ 00456854 bytes 152c0494
- 004568e0 ["INT_ADD", "register:40f0:8", ["const:4568e0:8", "const:4:8"]]
- 004568e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00456920 ["INT_ADD", "register:40f0:8", ["const:456920:8", "const:4:8"]]
+ 00456920 ["CALL", null, ["callee:00c57eb0:8"]]
- 004568e0 bytes 74042094
+ 00456920 bytes 64052094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18fa05a4d583f180f7d521cc26913feb"></a>

### [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) → [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) FUN_00456efc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 22件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.47% / 新版 94.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004570e0",
      "incomplete_value": false,
      "site": "004570e0",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004570a0",
      "incomplete_value": false,
      "site": "004570a0",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004570e4",
      "incomplete_value": false,
      "site": "004570e4",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004570a4",
      "incomplete_value": false,
      "site": "004570a4",
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
            "const:518:8"
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
      "definition_site": "004571d0",
      "incomplete_value": true,
      "site": "004571d8",
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
      "definition_site": "00457190",
      "incomplete_value": true,
      "site": "00457198",
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
      "00456f44",
      "PARAM",
      [
        "storage",
        "002b094e",
        null,
        "string"
      ]
    ],
    [
      "004570e0",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ],
    [
      "004570e4",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00456f44",
      "PARAM",
      [
        "storage",
        "002b098e",
        null,
        "string"
      ]
    ],
    [
      "004570e0",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ],
    [
      "004570e4",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-00456f0c) · [`00456f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-00456f4c) · [`004570cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md#insn-004570cc)
- 新版 [`00456f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-00456f4c) · [`00456f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-00456f8c) · [`0045710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-0045710c)

~~~diff
- 00456f0c ["INT_ADD", "register:40f0:8", ["const:456f0c:8", "const:4:8"]]
- 00456f0c ["CALL", null, ["callee:00c57f70:8"]]
+ 00456f4c ["INT_ADD", "register:40f0:8", ["const:456f4c:8", "const:4:8"]]
+ 00456f4c ["CALL", null, ["callee:00c57f70:8"]]
- 00456f0c bytes 19032094
+ 00456f4c bytes 09042094
- 00456f4c ["INT_ADD", "register:40f0:8", ["const:456f4c:8", "const:4:8"]]
- 00456f4c ["CALL", null, ["callee:00560454:8"]]
+ 00456f8c ["INT_ADD", "register:40f0:8", ["const:456f8c:8", "const:4:8"]]
+ 00456f8c ["CALL", null, ["callee:00560454:8"]]
- 00456f4c bytes 32250494
+ 00456f8c bytes 32250494
- 004570cc ["INT_ADD", "register:40f0:8", ["const:4570cc:8", "const:4:8"]]
- 004570cc ["CALL", null, ["callee:004509b0:8"]]
+ 0045710c ["INT_ADD", "register:40f0:8", ["const:45710c:8", "const:4:8"]]
+ 0045710c ["CALL", null, ["callee:004509b0:8"]]
- 004570cc bytes 29e6ff97
+ 0045710c bytes 29e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-807aca1bd498bd13fa79281ec2405fdc"></a>

### [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) → [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) FUN_00457400

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00886f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md)
- 新版 呼出元 1件 [`00886f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.87% / 新版 93.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004575b8",
      "incomplete_value": false,
      "site": "004575b8",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457578",
      "incomplete_value": false,
      "site": "00457578",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004575bc",
      "incomplete_value": false,
      "site": "004575bc",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045757c",
      "incomplete_value": false,
      "site": "0045757c",
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
            "const:618:8"
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
      "definition_site": "00457678",
      "incomplete_value": true,
      "site": "00457680",
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
      "definition_site": "00457638",
      "incomplete_value": true,
      "site": "00457640",
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
      "00457448",
      "PARAM",
      [
        "storage",
        "002a7594",
        null,
        "string"
      ]
    ],
    [
      "004575b8",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ],
    [
      "004575bc",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00457448",
      "PARAM",
      [
        "storage",
        "002a7670",
        null,
        "string"
      ]
    ],
    [
      "004575b8",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ],
    [
      "004575bc",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-00457410) · [`00457450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-00457450) · [`004575a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md#insn-004575a4)
- 新版 [`00457450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-00457450) · [`00457490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-00457490) · [`004575e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-004575e4)

~~~diff
- 00457410 ["INT_ADD", "register:40f0:8", ["const:457410:8", "const:4:8"]]
- 00457410 ["CALL", null, ["callee:00c57f70:8"]]
+ 00457450 ["INT_ADD", "register:40f0:8", ["const:457450:8", "const:4:8"]]
+ 00457450 ["CALL", null, ["callee:00c57f70:8"]]
- 00457410 bytes d8012094
+ 00457450 bytes c8022094
- 00457450 ["INT_ADD", "register:40f0:8", ["const:457450:8", "const:4:8"]]
- 00457450 ["CALL", null, ["callee:00560454:8"]]
+ 00457490 ["INT_ADD", "register:40f0:8", ["const:457490:8", "const:4:8"]]
+ 00457490 ["CALL", null, ["callee:00560454:8"]]
- 00457450 bytes f1230494
+ 00457490 bytes f1230494
- 004575a4 ["INT_ADD", "register:40f0:8", ["const:4575a4:8", "const:4:8"]]
- 004575a4 ["CALL", null, ["callee:004509b0:8"]]
+ 004575e4 ["INT_ADD", "register:40f0:8", ["const:4575e4:8", "const:4:8"]]
+ 004575e4 ["CALL", null, ["callee:004509b0:8"]]
- 004575a4 bytes f3e4ff97
+ 004575e4 bytes f3e4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e04d0be9c7cf643edd071fa0093352d"></a>

### [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) → [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) FUN_00457878

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · 呼出先 25件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md)
- 新版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 25件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004578d0",
      "incomplete_value": false,
      "site": "004578d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457890",
      "incomplete_value": false,
      "site": "00457898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "definition_site": "004578e4",
      "incomplete_value": false,
      "site": "004578e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004578a4",
      "incomplete_value": false,
      "site": "004578a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "0045799c",
      "incomplete_value": true,
      "site": "0045799c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045795c",
      "incomplete_value": true,
      "site": "0045795c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004578d8",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "004578e4",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "0045798c",
      "READ",
      [
        "storage",
        "002a89dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004578d8",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "004578e4",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "0045798c",
      "READ",
      [
        "storage",
        "002a8aa9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045799c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-0045799c) · [`00457a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-00457a20) · [`00457a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md#insn-00457a80)
- 新版 [`004579dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-004579dc) · [`00457a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-00457a60) · [`00457ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-00457ac0)

~~~diff
- 0045799c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045799c ["INT_ADD", "register:40f0:8", ["const:45799c:8", "const:4:8"]]
- 0045799c ["CALLIND", null, ["register:0:8"]]
+ 004579dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004579dc ["INT_ADD", "register:40f0:8", ["const:4579dc:8", "const:4:8"]]
+ 004579dc ["CALLIND", null, ["register:0:8"]]
- 0045799c bytes 00013fd6
+ 004579dc bytes 00013fd6
- 00457a20 ["INT_ADD", "register:40f0:8", ["const:457a20:8", "const:4:8"]]
- 00457a20 ["CALL", null, ["callee:00c57f70:8"]]
+ 00457a60 ["INT_ADD", "register:40f0:8", ["const:457a60:8", "const:4:8"]]
+ 00457a60 ["CALL", null, ["callee:00c57f70:8"]]
- 00457a20 bytes 54002094
+ 00457a60 bytes 44012094
- 00457a80 ["INT_ADD", "register:40f0:8", ["const:457a80:8", "const:4:8"]]
- 00457a80 ["CALL", null, ["callee:00c57f70:8"]]
+ 00457ac0 ["INT_ADD", "register:40f0:8", ["const:457ac0:8", "const:4:8"]]
+ 00457ac0 ["CALL", null, ["callee:00c57f70:8"]]
- 00457a80 bytes 3c002094
+ 00457ac0 bytes 2c012094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc24a5ba3eeb569949123c79babcd4e6"></a>

### [`004581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md) → [`00458230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md) FUN_00458230

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md)
- 新版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458308",
      "incomplete_value": false,
      "site": "00458310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004582c8",
      "incomplete_value": false,
      "site": "004582d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045832c",
      "incomplete_value": false,
      "site": "0045832c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004582ec",
      "incomplete_value": false,
      "site": "004582ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00458394",
      "incomplete_value": true,
      "site": "00458394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458354",
      "incomplete_value": true,
      "site": "00458354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9dc:8"
              ]
            ]
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
      "00458274",
      "PARAM",
      [
        "storage",
        "002b38ec",
        null,
        "string"
      ]
    ],
    [
      "00458310",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ],
    [
      "0045832c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00458274",
      "PARAM",
      [
        "storage",
        "002b392c",
        null,
        "string"
      ]
    ],
    [
      "00458310",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "0045832c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045823c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-0045823c) · [`00458394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-00458394) · [`004583bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md#insn-004583bc)
- 新版 [`0045827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-0045827c) · [`004583d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-004583d4) · [`004583fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-004583fc)

~~~diff
- 0045823c ["INT_ADD", "register:40f0:8", ["const:45823c:8", "const:4:8"]]
- 0045823c ["CALL", null, ["callee:00c57f70:8"]]
+ 0045827c ["INT_ADD", "register:40f0:8", ["const:45827c:8", "const:4:8"]]
+ 0045827c ["CALL", null, ["callee:00c57f70:8"]]
- 0045823c bytes 4dfe1f94
+ 0045827c bytes 3dff1f94
- 00458394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00458394 ["INT_ADD", "register:40f0:8", ["const:458394:8", "const:4:8"]]
- 00458394 ["CALLIND", null, ["register:0:8"]]
+ 004583d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004583d4 ["INT_ADD", "register:40f0:8", ["const:4583d4:8", "const:4:8"]]
+ 004583d4 ["CALLIND", null, ["register:0:8"]]
- 00458394 bytes 00013fd6
+ 004583d4 bytes 00013fd6
- 004583bc ["INT_ADD", "register:40f0:8", ["const:4583bc:8", "const:4:8"]]
- 004583bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 004583fc ["INT_ADD", "register:40f0:8", ["const:4583fc:8", "const:4:8"]]
+ 004583fc ["CALL", null, ["callee:00c57eb0:8"]]
- 004583bc bytes bdfd1f94
+ 004583fc bytes adfe1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328b4fd6a4609f8958ca1624e4116bcb"></a>

### [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) → [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) FUN_004586cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00466ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ccc.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00466d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d0c.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004588d4",
      "incomplete_value": false,
      "site": "004588d4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458894",
      "incomplete_value": false,
      "site": "00458894",
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
            "const:818:8"
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
      "definition_site": "00458864",
      "incomplete_value": true,
      "site": "0045886c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458824",
      "incomplete_value": true,
      "site": "0045882c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
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
      "004587f4",
      "READ",
      [
        "storage",
        "002a5278",
        null,
        "undefined4"
      ]
    ],
    [
      "004587f8",
      "READ",
      [
        "storage",
        "002a527c",
        null,
        "undefined1"
      ]
    ],
    [
      "00458864",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004587f4",
      "READ",
      [
        "storage",
        "002a5354",
        null,
        "undefined4"
      ]
    ],
    [
      "004587f8",
      "READ",
      [
        "storage",
        "002a5358",
        null,
        "undefined1"
      ]
    ],
    [
      "00458864",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045882c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-0045882c) · [`004586f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-004586f0) · [`00458730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md#insn-00458730)
- 新版 [`0045886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-0045886c) · [`00458730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-00458730) · [`00458770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-00458770)

~~~diff
- 0045882c ["INT_ADD", "register:40f0:8", ["const:45882c:8", "const:4:8"]]
- 0045882c ["CALL", null, ["callee:00561d34:8"]]
+ 0045886c ["INT_ADD", "register:40f0:8", ["const:45886c:8", "const:4:8"]]
+ 0045886c ["CALL", null, ["callee:00561d34:8"]]
- 0045882c bytes 32250494
+ 0045886c bytes 32250494
- 004586f0 ["INT_ADD", "register:40f0:8", ["const:4586f0:8", "const:4:8"]]
- 004586f0 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00458730 ["INT_ADD", "register:40f0:8", ["const:458730:8", "const:4:8"]]
+ 00458730 ["CALL", null, ["callee:00c57fd0:8"]]
- 004586f0 bytes 38fd1f94
+ 00458730 bytes 28fe1f94
- 00458730 ["COPY", "tmp:0:8", ["const:9f7:8"]]
- 00458730 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00458730 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00458730 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00458770 ["COPY", "tmp:0:8", ["const:ac4:8"]]
+ 00458770 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00458770 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00458770 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00458730 bytes 5adf2791
+ 00458770 bytes 5a132b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7e42731bf8db37d63a3c7f8d0165fc9"></a>

### [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) → [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) FUN_00458af0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 11件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044b804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md) [`0044b918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b918.md) [`0045868c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/0045868c.md) [`00466f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f00.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 11件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md) [`0044b958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md) [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) [`00466f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458b78",
      "incomplete_value": false,
      "site": "00458b80",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458b38",
      "incomplete_value": false,
      "site": "00458b40",
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
            "const:898:8"
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
      "00458b80",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ],
    [
      "00458be0",
      "READ",
      [
        "storage",
        "00c648b8",
        null,
        "pointer"
      ]
    ],
    [
      "00458be0",
      "READ",
      [
        "storage",
        "00c648c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00458b80",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ],
    [
      "00458be0",
      "READ",
      [
        "storage",
        "00c64cb8",
        null,
        "pointer"
      ]
    ],
    [
      "00458be0",
      "READ",
      [
        "storage",
        "00c64cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458ad8) · [`00458ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458ae0) · [`00458af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md#insn-00458af0)
- 新版 [`00458b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b18) · [`00458b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b20) · [`00458b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b30)

~~~diff
- 00458ad8 ["INT_ADD", "register:40f0:8", ["const:458ad8:8", "const:4:8"]]
- 00458ad8 ["CALL", null, ["callee:0044b844:8"]]
+ 00458b18 ["INT_ADD", "register:40f0:8", ["const:458b18:8", "const:4:8"]]
+ 00458b18 ["CALL", null, ["callee:0044b844:8"]]
- 00458ad8 bytes 4bcbff97
+ 00458b18 bytes 4bcbff97
- 00458ae0 ["INT_ADD", "register:40f0:8", ["const:458ae0:8", "const:4:8"]]
- 00458ae0 ["CALL", null, ["callee:0044b958:8"]]
+ 00458b20 ["INT_ADD", "register:40f0:8", ["const:458b20:8", "const:4:8"]]
+ 00458b20 ["CALL", null, ["callee:0044b958:8"]]
- 00458ae0 bytes 8ecbff97
+ 00458b20 bytes 8ecbff97
- 00458af0 ["INT_ADD", "register:40f0:8", ["const:458af0:8", "const:4:8"]]
- 00458af0 ["CALL", null, ["callee:0043dba4:8"]]
+ 00458b30 ["INT_ADD", "register:40f0:8", ["const:458b30:8", "const:4:8"]]
+ 00458b30 ["CALL", null, ["callee:0043dba4:8"]]
- 00458af0 bytes 1d94ff97
+ 00458b30 bytes 1d94ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-931c72263d56d8584741142eb4166273"></a>

### [`00459390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459390.md) → [`004593d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593d0.md) FUN_004593d0

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
      "definition_site": "004593d8",
      "incomplete_value": false,
      "site": "004593dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459398",
      "incomplete_value": false,
      "site": "0045939c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
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
      "004593dc",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004593dc",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459390.md#insn-00459398)
- 新版 [`004593d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593d0.md#insn-004593d8)

~~~diff
- 00459398 ["COPY", "tmp:0:8", ["const:360:8"]]
- 00459398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00459398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00459398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004593d8 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 004593d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004593d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004593d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00459398 bytes 29810d91
+ 004593d8 bytes 29811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e35b612535da7fad6582a8b4abc24c"></a>

### [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) → [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) FUN_004593f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 6件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`0059baa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059baa4.md) [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bae4.md) [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004593f8",
      "incomplete_value": false,
      "site": "004593fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004593b8",
      "incomplete_value": false,
      "site": "004593bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
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
      "004593fc",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004593fc",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004593b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md#insn-004593b8) · [`004593dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md#insn-004593dc)
- 新版 [`004593f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md#insn-004593f8) · [`0045941c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md#insn-0045941c)

~~~diff
- 004593b8 ["COPY", "tmp:0:8", ["const:360:8"]]
- 004593b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004593b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004593b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004593f8 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 004593f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004593f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004593f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004593b8 bytes 29810d91
+ 004593f8 bytes 29811d91
- 004593dc ["INT_ADD", "register:40f0:8", ["const:4593dc:8", "const:4:8"]]
- 004593dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045941c ["INT_ADD", "register:40f0:8", ["const:45941c:8", "const:4:8"]]
+ 0045941c ["CALL", null, ["callee:00c57eb0:8"]]
- 004593dc bytes b5f91f94
+ 0045941c bytes a5fa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de830770633bf5a356f8a21830db8e70"></a>

### [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) → [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) FUN_004594d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00466f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md) [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md) [`00488544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488544.md) [`0048cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 25件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00466f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md) [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) [`00488584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488584.md) [`0048cf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459550",
      "incomplete_value": true,
      "site": "00459554",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "old": {
      "definition_site": "00459510",
      "incomplete_value": true,
      "site": "00459514",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:830:8"
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
      "00459550",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00459550",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00459550",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00459550",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-00459514) · [`004594cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-004594cc) · [`00459504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md#insn-00459504)
- 新版 [`00459554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-00459554) · [`0045950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-0045950c) · [`00459544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-00459544)

~~~diff
- 00459514 ["INT_ADD", "register:40f0:8", ["const:459514:8", "const:4:8"]]
- 00459514 ["CALL", null, ["callee:00c58280:8"]]
+ 00459554 ["INT_ADD", "register:40f0:8", ["const:459554:8", "const:4:8"]]
+ 00459554 ["CALL", null, ["callee:00c58280:8"]]
- 00459514 bytes 5bfa1f94
+ 00459554 bytes 4bfb1f94
- 004594cc ["INT_ADD", "register:40f0:8", ["const:4594cc:8", "const:4:8"]]
- 004594cc ["CALL", null, ["callee:00c58260:8"]]
+ 0045950c ["INT_ADD", "register:40f0:8", ["const:45950c:8", "const:4:8"]]
+ 0045950c ["CALL", null, ["callee:00c58260:8"]]
- 004594cc bytes 65fa1f94
+ 0045950c bytes 55fb1f94
- 00459504 ["INT_ADD", "register:40f0:8", ["const:459504:8", "const:4:8"]]
- 00459504 ["CALL", null, ["callee:00c58270:8"]]
+ 00459544 ["INT_ADD", "register:40f0:8", ["const:459544:8", "const:4:8"]]
+ 00459544 ["CALL", null, ["callee:00c58270:8"]]
- 00459504 bytes 5bfa1f94
+ 00459544 bytes 4bfb1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0495667e2ec81ad32b422c96c11ef9e"></a>

### [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) → [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) FUN_00459d74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 207件 [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`0045b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md) [`0045c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md) [`0045c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c8c8.md) · 呼出先 3件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 207件 [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0045b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md) [`0045c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md) [`0045c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md) · 呼出先 3件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00459d94",
      "incomplete_value": true,
      "site": "00459d98",
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
      "definition_site": "00459d54",
      "incomplete_value": true,
      "site": "00459d58",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459d9c",
      "incomplete_value": true,
      "site": "00459da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459d5c",
      "incomplete_value": true,
      "site": "00459d64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:840:8"
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
      "definition_site": "00459da0",
      "incomplete_value": true,
      "site": "00459da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459d60",
      "incomplete_value": true,
      "site": "00459d64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:848:8"
              ]
            ]
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
      "00459d90",
      "READ",
      [
        "storage",
        "00c9a838",
        null,
        "pointer"
      ]
    ],
    [
      "00459d98",
      "DATA",
      [
        "storage",
        "00c633f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459d9c",
      "READ",
      [
        "storage",
        "00c9a840",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00459d90",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00459d98",
      "DATA",
      [
        "storage",
        "00c637f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459d9c",
      "READ",
      [
        "storage",
        "00c9ac40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d64) · [`00459d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d40) · [`00459d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md#insn-00459d50)
- 新版 [`00459da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459da4) · [`00459d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459d80) · [`00459d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459d90)

~~~diff
- 00459d64 ["INT_ADD", "register:40f0:8", ["const:459d64:8", "const:4:8"]]
- 00459d64 ["CALL", null, ["callee:00c57f10:8"]]
+ 00459da4 ["INT_ADD", "register:40f0:8", ["const:459da4:8", "const:4:8"]]
+ 00459da4 ["CALL", null, ["callee:00c57f10:8"]]
- 00459d64 bytes 6bf71f94
+ 00459da4 bytes 5bf81f94
- 00459d40 ["INT_ADD", "register:40f0:8", ["const:459d40:8", "const:4:8"]]
- 00459d40 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00459d80 ["INT_ADD", "register:40f0:8", ["const:459d80:8", "const:4:8"]]
+ 00459d80 ["CALL", null, ["callee:00c57ef0:8"]]
- 00459d40 bytes 6cf71f94
+ 00459d80 bytes 5cf81f94
- 00459d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:838:8"]]
- 00459d50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00459d90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c38:8"]]
+ 00459d90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00459d50 bytes 081d44f9
+ 00459d90 bytes 081d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1aacec900e5b44715202f3c34ac1bbe"></a>

### [`00459d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d8c.md) → [`00459dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459dcc.md) FUN_00459dcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459dd8",
      "incomplete_value": false,
      "site": "00459de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459d98",
      "incomplete_value": false,
      "site": "00459da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00459de4",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459de4",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d8c.md#insn-00459d98)
- 新版 [`00459dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459dcc.md#insn-00459dd8)

~~~diff
- 00459d98 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00459d98 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00459d98 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00459d98 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00459dd8 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00459dd8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00459dd8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00459dd8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00459d98 bytes 4a811091
+ 00459dd8 bytes 4a812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d925484b97da256fa3570e3a44864b82"></a>

### [`00459dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md) → [`00459e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md) FUN_00459e10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459e28",
      "incomplete_value": false,
      "site": "00459e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459de8",
      "incomplete_value": false,
      "site": "00459df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00459e34",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459e34",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md#insn-00459de8) · [`00459e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459dd0.md#insn-00459e18)
- 新版 [`00459e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md#insn-00459e28) · [`00459e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md#insn-00459e58)

~~~diff
- 00459de8 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00459de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00459de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00459de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459e28 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00459e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00459de8 bytes 08811091
+ 00459e28 bytes 08812091
- 00459e18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459e18 ["INT_ADD", "register:40f0:8", ["const:459e18:8", "const:4:8"]]
- 00459e18 ["CALLIND", null, ["register:0:8"]]
+ 00459e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459e58 ["INT_ADD", "register:40f0:8", ["const:459e58:8", "const:4:8"]]
+ 00459e58 ["CALLIND", null, ["register:0:8"]]
- 00459e18 bytes 00013fd6
+ 00459e58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e21dd4e902472fb21a975ec68832a05"></a>

### [`00459e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md) → [`00459e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md) FUN_00459e6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00459e98",
      "incomplete_value": false,
      "site": "00459e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459e58",
      "incomplete_value": false,
      "site": "00459e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00459e98",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459e98",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e40) · [`00459e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e50) · [`00459e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459e2c.md#insn-00459e74)
- 新版 [`00459e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459e80) · [`00459e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459e90) · [`00459eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459eb4)

~~~diff
- 00459e40 ["INT_ADD", "register:40f0:8", ["const:459e40:8", "const:4:8"]]
- 00459e40 ["CALL", null, ["callee:00c57e90:8"]]
+ 00459e80 ["INT_ADD", "register:40f0:8", ["const:459e80:8", "const:4:8"]]
+ 00459e80 ["CALL", null, ["callee:00c57e90:8"]]
- 00459e40 bytes 14f71f94
+ 00459e80 bytes 04f81f94
- 00459e50 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00459e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00459e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00459e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459e90 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00459e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00459e50 bytes 08811091
+ 00459e90 bytes 08812091
- 00459e74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459e74 ["INT_ADD", "register:40f0:8", ["const:459e74:8", "const:4:8"]]
- 00459e74 ["CALLIND", null, ["register:0:8"]]
+ 00459eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459eb4 ["INT_ADD", "register:40f0:8", ["const:459eb4:8", "const:4:8"]]
+ 00459eb4 ["CALLIND", null, ["register:0:8"]]
- 00459e74 bytes 00013fd6
+ 00459eb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d0aa9f0675967473edc5ea445002f0a"></a>

### [`00459eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md) → [`00459ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md) FUN_00459ef4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459f10",
      "incomplete_value": false,
      "site": "00459f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459ed0",
      "incomplete_value": false,
      "site": "00459ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      "00459f10",
      "DATA",
      [
        "storage",
        "00c63420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459f10",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md#insn-00459ecc) · [`00459ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459eb4.md#insn-00459ef0)
- 新版 [`00459f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md#insn-00459f0c) · [`00459f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md#insn-00459f30)

~~~diff
- 00459ecc ["COPY", "tmp:0:8", ["const:420:8"]]
- 00459ecc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00459ecc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00459ecc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459f0c ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00459f0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459f0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459f0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00459ecc bytes 29811091
+ 00459f0c bytes 29812091
- 00459ef0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00459ef0 ["INT_ADD", "register:40f0:8", ["const:459ef0:8", "const:4:8"]]
- 00459ef0 ["CALLIND", null, ["register:0:8"]]
+ 00459f30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00459f30 ["INT_ADD", "register:40f0:8", ["const:459f30:8", "const:4:8"]]
+ 00459f30 ["CALLIND", null, ["register:0:8"]]
- 00459ef0 bytes 20013fd6
+ 00459f30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0fbdd932b94879760bfc8cc0c86254d"></a>

### [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) → [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) FUN_00459ff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a114",
      "incomplete_value": true,
      "site": "0045a114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a0d4",
      "incomplete_value": true,
      "site": "0045a0d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e4f:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0045a174",
      "incomplete_value": true,
      "site": "0045a174",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a134",
      "incomplete_value": true,
      "site": "0045a134",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a164",
      "incomplete_value": true,
      "site": "0045a174",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a124",
      "incomplete_value": true,
      "site": "0045a134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a104",
      "READ",
      [
        "storage",
        "002b5e4f",
        null,
        "string"
      ]
    ],
    [
      "0045a158",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a164",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045a104",
      "READ",
      [
        "storage",
        "002b5e8f",
        null,
        "string"
      ]
    ],
    [
      "0045a158",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a164",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a114) · [`0045a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a134) · [`0045a174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md#insn-0045a174)
- 新版 [`0045a154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a154) · [`0045a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a174) · [`0045a1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a1b4)

~~~diff
- 0045a114 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0045a114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a154 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 0045a154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a114 bytes 08811a91
+ 0045a154 bytes 08812a91
- 0045a134 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a134 ["INT_ADD", "register:40f0:8", ["const:45a134:8", "const:4:8"]]
- 0045a134 ["CALLIND", null, ["register:0:8"]]
+ 0045a174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a174 ["INT_ADD", "register:40f0:8", ["const:45a174:8", "const:4:8"]]
+ 0045a174 ["CALLIND", null, ["register:0:8"]]
- 0045a134 bytes 00013fd6
+ 0045a174 bytes 00013fd6
- 0045a174 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a174 ["INT_ADD", "register:40f0:8", ["const:45a174:8", "const:4:8"]]
- 0045a174 ["CALLIND", null, ["register:0:8"]]
+ 0045a1b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a1b4 ["INT_ADD", "register:40f0:8", ["const:45a1b4:8", "const:4:8"]]
+ 0045a1b4 ["CALLIND", null, ["register:0:8"]]
- 0045a174 bytes 00013fd6
+ 0045a1b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936b49faad2239cd44fc5d4610c2847a"></a>

### [`0045a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a520.md) → [`0045a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md) FUN_0045a560

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0045a578",
      "incomplete_value": true,
      "site": "0045a57c",
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
      "definition_site": "0045a538",
      "incomplete_value": true,
      "site": "0045a53c",
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
      "0045a574",
      "READ",
      [
        "storage",
        "00c9a800",
        null,
        "pointer"
      ]
    ],
    [
      "0045a57c",
      "DATA",
      [
        "storage",
        "00c634a0",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0045a574",
      "READ",
      [
        "storage",
        "00c9ac00",
        null,
        "pointer"
      ]
    ],
    [
      "0045a57c",
      "DATA",
      [
        "storage",
        "00c638a0",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a520.md#insn-0045a534) · [`0045a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a520.md#insn-0045a540)
- 新版 [`0045a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md#insn-0045a574) · [`0045a580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md#insn-0045a580)

~~~diff
- 0045a534 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:800:8"]]
- 0045a534 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045a574 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c00:8"]]
+ 0045a574 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045a534 bytes 080144f9
+ 0045a574 bytes 080146f9
- 0045a540 ["INT_ADD", "register:40f0:8", ["const:45a540:8", "const:4:8"]]
- 0045a540 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0045a580 ["INT_ADD", "register:40f0:8", ["const:45a580:8", "const:4:8"]]
+ 0045a580 ["CALL", null, ["callee:00c57ea0:8"]]
- 0045a540 bytes 58f51f94
+ 0045a580 bytes 48f61f94
~~~


<a id="compare-d6d0712a37bf669293f836c9bab4daee"></a>

### [`0045a560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md) → [`0045a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md) FUN_0045a5a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045a554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a554.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`0045a594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a594.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a644",
      "incomplete_value": true,
      "site": "0045a648",
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
      "definition_site": "0045a604",
      "incomplete_value": true,
      "site": "0045a608",
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
      "definition_site": "0045a620",
      "incomplete_value": true,
      "site": "0045a628",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a5e0",
      "incomplete_value": true,
      "site": "0045a5e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:858:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a61c",
      "incomplete_value": false,
      "site": "0045a628",
      "value": [
        "leaf",
        "const:45a6c8:8"
      ]
    },
    "old": {
      "definition_site": "0045a5dc",
      "incomplete_value": false,
      "site": "0045a5e8",
      "value": [
        "leaf",
        "const:45a688:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a61c",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "0045a620",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "0045a620",
      "PARAM",
      [
        "storage",
        "00c928b0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0045a61c",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "0045a620",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045a620",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5c8) · [`0045a5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5e8) · [`0045a5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a560.md#insn-0045a5a0)
- 新版 [`0045a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a608) · [`0045a628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a628) · [`0045a5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a5e0)

~~~diff
- 0045a5c8 ["INT_ADD", "register:40f0:8", ["const:45a5c8:8", "const:4:8"]]
- 0045a5c8 ["CALL", null, ["callee:00c58320:8"]]
+ 0045a608 ["INT_ADD", "register:40f0:8", ["const:45a608:8", "const:4:8"]]
+ 0045a608 ["CALL", null, ["callee:00c58320:8"]]
- 0045a5c8 bytes 56f61f94
+ 0045a608 bytes 46f71f94
- 0045a5e8 ["INT_ADD", "register:40f0:8", ["const:45a5e8:8", "const:4:8"]]
- 0045a5e8 ["CALL", null, ["callee:00c58330:8"]]
+ 0045a628 ["INT_ADD", "register:40f0:8", ["const:45a628:8", "const:4:8"]]
+ 0045a628 ["CALL", null, ["callee:00c58330:8"]]
- 0045a5e8 bytes 52f61f94
+ 0045a628 bytes 42f71f94
- 0045a5a0 ["INT_ADD", "register:40f0:8", ["const:45a5a0:8", "const:4:8"]]
- 0045a5a0 ["CALL", null, ["callee:00c582f0:8"]]
+ 0045a5e0 ["INT_ADD", "register:40f0:8", ["const:45a5e0:8", "const:4:8"]]
+ 0045a5e0 ["CALL", null, ["callee:00c582f0:8"]]
- 0045a5a0 bytes 54f61f94
+ 0045a5e0 bytes 44f71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

