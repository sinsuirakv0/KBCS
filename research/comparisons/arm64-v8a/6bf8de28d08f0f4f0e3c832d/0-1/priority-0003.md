# v16.0.0 → v16.0.1 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-61a869c57b02f3baa6f6fc2878c3055f"></a>

### [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) → [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) FUN_0045a6d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 20件 [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`0045effc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045effc.md) [`0045fa9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fa9c.md) [`00538300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/00538300.md) [`005385b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00538/005385b0.md) · 呼出先 5件 [`00bf9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9210.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f10.md) [`00c57f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f20.md)
- 新版 呼出元 20件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`0045f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md) [`0045fadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md) [`00538340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538340.md) [`005385f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/005385f0.md) · 呼出先 5件 [`00bf9638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9638.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58310.md) [`00c58320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58320.md)

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
      "definition_site": "0045a710",
      "incomplete_value": true,
      "site": "0045a718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045a6d0",
      "incomplete_value": true,
      "site": "0045a6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a714",
      "incomplete_value": true,
      "site": "0045a718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a6d4",
      "incomplete_value": true,
      "site": "0045a6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:868:8"
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
      "0045a710",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "0045a710",
      "PARAM",
      [
        "storage",
        "00c928b0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a714",
      "READ",
      [
        "storage",
        "00c9a868",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045a710",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045a710",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a714",
      "READ",
      [
        "storage",
        "00c9ac68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6d8) · [`0045a6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6a8) · [`0045a6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md#insn-0045a6b0)
- 新版 [`0045a718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a718) · [`0045a6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a6e8) · [`0045a6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a6f0)

~~~diff
- 0045a6d8 ["INT_ADD", "register:40f0:8", ["const:45a6d8:8", "const:4:8"]]
- 0045a6d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 0045a718 ["INT_ADD", "register:40f0:8", ["const:45a718:8", "const:4:8"]]
+ 0045a718 ["CALL", null, ["callee:00c57f10:8"]]
- 0045a6d8 bytes 0ef51f94
+ 0045a718 bytes fef51f94
- 0045a6a8 ["INT_ADD", "register:40f0:8", ["const:45a6a8:8", "const:4:8"]]
- 0045a6a8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0045a6e8 ["INT_ADD", "register:40f0:8", ["const:45a6e8:8", "const:4:8"]]
+ 0045a6e8 ["CALL", null, ["callee:00c57ef0:8"]]
- 0045a6a8 bytes 12f51f94
+ 0045a6e8 bytes 02f61f94
- 0045a6b0 ["INT_ADD", "register:40f0:8", ["const:45a6b0:8", "const:4:8"]]
- 0045a6b0 ["CALL", null, ["callee:00c58310:8"]]
+ 0045a6f0 ["INT_ADD", "register:40f0:8", ["const:45a6f0:8", "const:4:8"]]
+ 0045a6f0 ["CALL", null, ["callee:00c58310:8"]]
- 0045a6b0 bytes 18f61f94
+ 0045a6f0 bytes 08f71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d5ef72c0d74cb6542dc51b31490354"></a>

### [`0045a6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md) → [`0045a734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md) FUN_0045a734

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
      "definition_site": "0045a748",
      "incomplete_value": false,
      "site": "0045a74c",
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
      "definition_site": "0045a708",
      "incomplete_value": false,
      "site": "0045a70c",
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
      "0045a74c",
      "DATA",
      [
        "storage",
        "00c63500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a74c",
      "DATA",
      [
        "storage",
        "00c63900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md#insn-0045a700) · [`0045a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a6f4.md#insn-0045a708)
- 新版 [`0045a740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md#insn-0045a740) · [`0045a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md#insn-0045a748)

~~~diff
- 0045a700 ["INT_ADD", "register:40f0:8", ["const:45a700:8", "const:4:8"]]
- 0045a700 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045a740 ["INT_ADD", "register:40f0:8", ["const:45a740:8", "const:4:8"]]
+ 0045a740 ["CALL", null, ["callee:00c57e90:8"]]
- 0045a700 bytes e4f41f94
+ 0045a740 bytes d4f51f94
- 0045a708 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0045a708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a748 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0045a748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a708 bytes 08011491
+ 0045a748 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13a32a92be924f46e43ad38fb87910a3"></a>

### [`0045a718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a718.md) → [`0045a758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a758.md) FUN_0045a758

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
      "definition_site": "0045a75c",
      "incomplete_value": false,
      "site": "0045a760",
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
      "definition_site": "0045a71c",
      "incomplete_value": false,
      "site": "0045a720",
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
      "0045a760",
      "DATA",
      [
        "storage",
        "00c63500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a760",
      "DATA",
      [
        "storage",
        "00c63900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a718.md#insn-0045a71c)
- 新版 [`0045a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a758.md#insn-0045a75c)

~~~diff
- 0045a71c ["COPY", "tmp:0:8", ["const:500:8"]]
- 0045a71c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a71c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a71c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a75c ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0045a75c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a75c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a75c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a71c bytes 08011491
+ 0045a75c bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bffe8dca5caf2e3d12210c7ce6a333f8"></a>

### [`0045a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md) → [`0045a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md) FUN_0045a770

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

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
      "definition_site": "0045a89c",
      "incomplete_value": true,
      "site": "0045a89c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045a85c",
      "incomplete_value": true,
      "site": "0045a85c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045a890",
      "incomplete_value": true,
      "site": "0045a89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045a850",
      "incomplete_value": true,
      "site": "0045a85c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a90c",
      "incomplete_value": true,
      "site": "0045a90c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045a8cc",
      "incomplete_value": true,
      "site": "0045a8cc",
      "value": [
        "LOAD",
        "8",
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
      "0045a880",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a890",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a8ac",
      "READ",
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
      "0045a880",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a890",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a8ac",
      "READ",
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

- 旧版 [`0045a85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a85c) · [`0045a8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a8cc) · [`0045a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md#insn-0045a928)
- 新版 [`0045a89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a89c) · [`0045a90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a90c) · [`0045a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a968)

~~~diff
- 0045a85c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a85c ["INT_ADD", "register:40f0:8", ["const:45a85c:8", "const:4:8"]]
- 0045a85c ["CALLIND", null, ["register:0:8"]]
+ 0045a89c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a89c ["INT_ADD", "register:40f0:8", ["const:45a89c:8", "const:4:8"]]
+ 0045a89c ["CALLIND", null, ["register:0:8"]]
- 0045a85c bytes 00013fd6
+ 0045a89c bytes 00013fd6
- 0045a8cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a8cc ["INT_ADD", "register:40f0:8", ["const:45a8cc:8", "const:4:8"]]
- 0045a8cc ["CALLIND", null, ["register:0:8"]]
+ 0045a90c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a90c ["INT_ADD", "register:40f0:8", ["const:45a90c:8", "const:4:8"]]
+ 0045a90c ["CALLIND", null, ["register:0:8"]]
- 0045a8cc bytes 00013fd6
+ 0045a90c bytes 00013fd6
- 0045a928 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
- 0045a928 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045a968 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
+ 0045a968 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0045a928 bytes 004d43f9
+ 0045a968 bytes 004d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cba9f200f648acb8ab9d79daa54d7c7"></a>

### [`0045aa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa4c.md) → [`0045aa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa8c.md) FUN_0045aa8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00451d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d8c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md)

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
      "definition_site": "0045aa94",
      "incomplete_value": false,
      "site": "0045aa94",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aa54",
      "incomplete_value": false,
      "site": "0045aa54",
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
            "const:580:8"
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
      "0045aa94",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aa94",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa4c.md#insn-0045aa50)
- 新版 [`0045aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa8c.md#insn-0045aa90)

~~~diff
- 0045aa50 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0045aa50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aa90 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0045aa90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aa90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aa50 bytes 08011691
+ 0045aa90 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9c61b918a1b2587c825dca44549285"></a>

### [`0045aa5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md) → [`0045aa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md) FUN_0045aa9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00451d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451d8c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0045aab4",
      "incomplete_value": false,
      "site": "0045aab4",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aa74",
      "incomplete_value": false,
      "site": "0045aa74",
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
            "const:580:8"
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
      "0045aab4",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aab4",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md#insn-0045aa6c) · [`0045aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa5c.md#insn-0045aa78)
- 新版 [`0045aaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md#insn-0045aaac) · [`0045aab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md#insn-0045aab8)

~~~diff
- 0045aa6c ["COPY", "tmp:0:8", ["const:580:8"]]
- 0045aa6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0045aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aa6c bytes 08011691
+ 0045aaac bytes 08012691
- 0045aa78 ["INT_ADD", "register:40f0:8", ["const:45aa78:8", "const:4:8"]]
- 0045aa78 ["CALL", null, ["callee:00451dcc:8"]]
+ 0045aab8 ["INT_ADD", "register:40f0:8", ["const:45aab8:8", "const:4:8"]]
+ 0045aab8 ["CALL", null, ["callee:00451dcc:8"]]
- 0045aa78 bytes c5dcff97
+ 0045aab8 bytes c5dcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbbd42b56f48889da4b4b7731063cad"></a>

### [`0045aa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md) → [`0045aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md) FUN_0045aacc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b2b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0045aaf0",
      "incomplete_value": false,
      "site": "0045aaf0",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aab0",
      "incomplete_value": false,
      "site": "0045aab0",
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
            "const:580:8"
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
      "0045aaf0",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aaf0",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aaa0) · [`0045aaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aaac) · [`0045aab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aa8c.md#insn-0045aab8)
- 新版 [`0045aae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aae0) · [`0045aaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aaec) · [`0045aaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aaf8)

~~~diff
- 0045aaa0 ["INT_ADD", "register:40f0:8", ["const:45aaa0:8", "const:4:8"]]
- 0045aaa0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045aae0 ["INT_ADD", "register:40f0:8", ["const:45aae0:8", "const:4:8"]]
+ 0045aae0 ["CALL", null, ["callee:00c57e90:8"]]
- 0045aaa0 bytes fcf31f94
+ 0045aae0 bytes ecf41f94
- 0045aaac ["COPY", "tmp:0:8", ["const:580:8"]]
- 0045aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0045aaec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aaac bytes 08011691
+ 0045aaec bytes 08012691
- 0045aab8 ["INT_ADD", "register:40f0:8", ["const:45aab8:8", "const:4:8"]]
- 0045aab8 ["CALL", null, ["callee:0045b2f0:8"]]
+ 0045aaf8 ["INT_ADD", "register:40f0:8", ["const:45aaf8:8", "const:4:8"]]
+ 0045aaf8 ["CALL", null, ["callee:0045b2f0:8"]]
- 0045aab8 bytes fe010094
+ 0045aaf8 bytes fe010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0924f462c659f0d6424db75648a1283"></a>

### [`0045aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aae0.md) → [`0045ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab20.md) FUN_0045ab20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md)

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
      "definition_site": "0045ab2c",
      "incomplete_value": false,
      "site": "0045ab2c",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aaec",
      "incomplete_value": false,
      "site": "0045aaec",
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
            "const:580:8"
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
      "0045ab2c",
      "DATA",
      [
        "storage",
        "00c63580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ab2c",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045aae0.md#insn-0045aae8)
- 新版 [`0045ab28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab20.md#insn-0045ab28)

~~~diff
- 0045aae8 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0045aae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045aae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045aae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ab28 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0045ab28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ab28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ab28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045aae8 bytes 29011691
+ 0045ab28 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a04ef18f6aa993677117326d4d799a4"></a>

### [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) → [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) FUN_0045ab6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0045b86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b86c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8ac.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_value` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ae54",
      "incomplete_value": false,
      "site": "0045ae54",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ae14",
      "incomplete_value": false,
      "site": "0045ae14",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ac8c",
      "value": [
        "leaf",
        "ram:7690c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ac4c",
      "value": [
        "leaf",
        "ram:769084:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0045acb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045ac8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ],
    [
      "0045acec",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:0045acb4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "0045ac8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007690c4"
      ]
    ],
    [
      "0045acec",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045acf4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ac4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md#insn-0045ac4c) · [`0045acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md#insn-0045acb4) · [`0045acbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md#insn-0045acbc)
- 新版 [`0045ac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md#insn-0045ac8c) · [`0045acfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md#insn-0045acfc)

~~~diff
- 0045ac4c ["INT_ADD", "register:40f0:8", ["const:45ac4c:8", "const:4:8"]]
- 0045ac4c ["CALL", null, ["ram:769084:8"]]
+ 0045ac8c ["INT_ADD", "register:40f0:8", ["const:45ac8c:8", "const:4:8"]]
+ 0045ac8c ["CALL", null, ["ram:7690c4:8"]]
- 0045ac4c bytes 0e390c94
+ 0045ac8c bytes 0e390c94
- 0045acb4 ["INT_ADD", "register:40f0:8", ["const:45acb4:8", "const:4:8"]]
- 0045acb4 ["CALL", null, ["callee:008514f8:8"]]
- 0045acb4 bytes 01da0f94
- 0045acbc ["INT_ADD", "register:40f0:8", ["const:45acbc:8", "const:4:8"]]
- 0045acbc ["CALL", null, ["ram:764344:8"]]
+ 0045acfc ["INT_ADD", "register:40f0:8", ["const:45acfc:8", "const:4:8"]]
+ 0045acfc ["CALL", null, ["ram:764384:8"]]
- 0045acbc bytes a2250c94
+ 0045acfc bytes a2250c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fd449baee78cd6f79dfb305b60b73fe"></a>

### [`0045b620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md) → [`0045b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md) FUN_0045b660

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0045b678",
      "incomplete_value": false,
      "site": "0045b684",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b638",
      "incomplete_value": false,
      "site": "0045b644",
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
            "const:5f0:8"
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
      "0045b684",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b684",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b638) · [`0045b668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b668) · [`0045b698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b620.md#insn-0045b698)
- 新版 [`0045b678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b678) · [`0045b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b6a8) · [`0045b6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b6d8)

~~~diff
- 0045b638 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0045b638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b678 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045b678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b638 bytes 08c11791
+ 0045b678 bytes 08c12791
- 0045b668 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b668 ["INT_ADD", "register:40f0:8", ["const:45b668:8", "const:4:8"]]
- 0045b668 ["CALLIND", null, ["register:0:8"]]
+ 0045b6a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b6a8 ["INT_ADD", "register:40f0:8", ["const:45b6a8:8", "const:4:8"]]
+ 0045b6a8 ["CALLIND", null, ["register:0:8"]]
- 0045b668 bytes 00013fd6
+ 0045b6a8 bytes 00013fd6
- 0045b698 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b698 ["INT_ADD", "register:40f0:8", ["const:45b698:8", "const:4:8"]]
- 0045b698 ["CALLIND", null, ["register:0:8"]]
+ 0045b6d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b6d8 ["INT_ADD", "register:40f0:8", ["const:45b6d8:8", "const:4:8"]]
+ 0045b6d8 ["CALLIND", null, ["register:0:8"]]
- 0045b698 bytes 00013fd6
+ 0045b6d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c827fb4a20de6476df3e26b6541d20"></a>

### [`0045b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md) → [`0045b74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md) FUN_0045b74c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0045b764",
      "incomplete_value": false,
      "site": "0045b770",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b724",
      "incomplete_value": false,
      "site": "0045b730",
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
            "const:5f0:8"
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
      "0045b770",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b770",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b724) · [`0045b754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b754) · [`0045b784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b70c.md#insn-0045b784)
- 新版 [`0045b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b764) · [`0045b794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b794) · [`0045b7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b7c4)

~~~diff
- 0045b724 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0045b724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b764 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045b764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b724 bytes 08c11791
+ 0045b764 bytes 08c12791
- 0045b754 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b754 ["INT_ADD", "register:40f0:8", ["const:45b754:8", "const:4:8"]]
- 0045b754 ["CALLIND", null, ["register:0:8"]]
+ 0045b794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b794 ["INT_ADD", "register:40f0:8", ["const:45b794:8", "const:4:8"]]
+ 0045b794 ["CALLIND", null, ["register:0:8"]]
- 0045b754 bytes 00013fd6
+ 0045b794 bytes 00013fd6
- 0045b784 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b784 ["INT_ADD", "register:40f0:8", ["const:45b784:8", "const:4:8"]]
- 0045b784 ["CALLIND", null, ["register:0:8"]]
+ 0045b7c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b7c4 ["INT_ADD", "register:40f0:8", ["const:45b7c4:8", "const:4:8"]]
+ 0045b7c4 ["CALLIND", null, ["register:0:8"]]
- 0045b784 bytes 00013fd6
+ 0045b7c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0c110a2a920ce87c0ee8d27fe1ab3c"></a>

### [`0045b7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md) → [`0045b834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md) FUN_0045b834

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045babc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045babc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045bafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0045b858",
      "incomplete_value": false,
      "site": "0045b858",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b818",
      "incomplete_value": false,
      "site": "0045b818",
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
            "const:5f0:8"
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
      "0045b858",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b858",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b808) · [`0045b814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b814) · [`0045b820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b7f4.md#insn-0045b820)
- 新版 [`0045b848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b848) · [`0045b854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b854) · [`0045b860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b860)

~~~diff
- 0045b808 ["INT_ADD", "register:40f0:8", ["const:45b808:8", "const:4:8"]]
- 0045b808 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045b848 ["INT_ADD", "register:40f0:8", ["const:45b848:8", "const:4:8"]]
+ 0045b848 ["CALL", null, ["callee:00c57e90:8"]]
- 0045b808 bytes a2f01f94
+ 0045b848 bytes 92f11f94
- 0045b814 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0045b814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b854 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045b854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b814 bytes 08c11791
+ 0045b854 bytes 08c12791
- 0045b820 ["INT_ADD", "register:40f0:8", ["const:45b820:8", "const:4:8"]]
- 0045b820 ["CALL", null, ["callee:0045bafc:8"]]
+ 0045b860 ["INT_ADD", "register:40f0:8", ["const:45b860:8", "const:4:8"]]
+ 0045b860 ["CALL", null, ["callee:0045bafc:8"]]
- 0045b820 bytes a7000094
+ 0045b860 bytes a7000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee5b87e000e9d4dfa5984447081ad6b"></a>

### [`0045b848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b848.md) → [`0045b888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b888.md) FUN_0045b888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045babc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045babc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045bafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md)

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
      "definition_site": "0045b894",
      "incomplete_value": false,
      "site": "0045b894",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b854",
      "incomplete_value": false,
      "site": "0045b854",
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
            "const:5f0:8"
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
      "0045b894",
      "DATA",
      [
        "storage",
        "00c635f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b894",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b848.md#insn-0045b850)
- 新版 [`0045b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b888.md#insn-0045b890)

~~~diff
- 0045b850 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0045b850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045b850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045b850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045b890 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 0045b890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045b850 bytes 29c11791
+ 0045b890 bytes 29c12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc55069d01e25fc9dd93f3911d912f1"></a>

### [`0045b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md) → [`0045b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md) FUN_0045b8d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.17% / 新版 94.17%

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
      "site": "0045b910",
      "value": [
        "leaf",
        "ram:768e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b8d0",
      "value": [
        "leaf",
        "ram:768e50:8"
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
      "site": "0045b988",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b948",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045ba3c",
      "incomplete_value": false,
      "site": "0045ba40",
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
      "definition_site": "0045b9fc",
      "incomplete_value": false,
      "site": "0045ba00",
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
      "0045b910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ],
    [
      "0045b91c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ],
  "added": [
    [
      "0045b910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ],
    [
      "0045b91c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045b8d0) · [`0045b948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045b948) · [`0045b9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045b894.md#insn-0045b9c0)
- 新版 [`0045b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045b910) · [`0045b988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045b988) · [`0045ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045ba00)

~~~diff
- 0045b8d0 ["INT_ADD", "register:40f0:8", ["const:45b8d0:8", "const:4:8"]]
- 0045b8d0 ["CALL", null, ["ram:768e50:8"]]
+ 0045b910 ["INT_ADD", "register:40f0:8", ["const:45b910:8", "const:4:8"]]
+ 0045b910 ["CALL", null, ["ram:768e90:8"]]
- 0045b8d0 bytes 60350c94
+ 0045b910 bytes 60350c94
- 0045b948 ["INT_ADD", "register:40f0:8", ["const:45b948:8", "const:4:8"]]
- 0045b948 ["CALL", null, ["ram:764344:8"]]
+ 0045b988 ["INT_ADD", "register:40f0:8", ["const:45b988:8", "const:4:8"]]
+ 0045b988 ["CALL", null, ["ram:764384:8"]]
- 0045b948 bytes 7f220c94
+ 0045b988 bytes 7f220c94
- 0045b9c0 ["INT_ADD", "register:40f0:8", ["const:45b9c0:8", "const:4:8"]]
- 0045b9c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045ba00 ["INT_ADD", "register:40f0:8", ["const:45ba00:8", "const:4:8"]]
+ 0045ba00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0045b9c0 bytes 3cf01f94
+ 0045ba00 bytes 2cf11f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72e13a32180c546b678c80fd71611d4c"></a>

### [`0045bd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd4c.md) → [`0045bd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd8c.md) FUN_0045bd8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045bd90",
      "incomplete_value": false,
      "site": "0045bd94",
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
      "definition_site": "0045bd50",
      "incomplete_value": false,
      "site": "0045bd54",
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
      "0045bd94",
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
      "0045bd94",
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

- 旧版 [`0045bd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd4c.md#insn-0045bd50)
- 新版 [`0045bd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd8c.md#insn-0045bd90)

~~~diff
- 0045bd50 ["COPY", "tmp:0:8", ["const:690:8"]]
- 0045bd50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bd90 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045bd90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bd90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bd90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bd50 bytes 08411a91
+ 0045bd90 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ae1f8ce8de7ce02696c754f18a732f"></a>

### [`0045bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd5c.md) → [`0045bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md) FUN_0045bd9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045bdac",
      "incomplete_value": false,
      "site": "0045bdb4",
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
      "definition_site": "0045bd6c",
      "incomplete_value": false,
      "site": "0045bd74",
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
      "0045bdb4",
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
      "0045bdb4",
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

- 旧版 [`0045bd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd5c.md#insn-0045bd6c) · [`0045bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd5c.md#insn-0045bd78)
- 新版 [`0045bdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md#insn-0045bdac) · [`0045bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md#insn-0045bdb8)

~~~diff
- 0045bd6c ["COPY", "tmp:0:8", ["const:690:8"]]
- 0045bd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bdac ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045bdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bd6c bytes 08411a91
+ 0045bdac bytes 08412a91
- 0045bd78 ["INT_ADD", "register:40f0:8", ["const:45bd78:8", "const:4:8"]]
- 0045bd78 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0045bdb8 ["INT_ADD", "register:40f0:8", ["const:45bdb8:8", "const:4:8"]]
+ 0045bdb8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0045bd78 bytes 4aef1f94
+ 0045bdb8 bytes 3af01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45e67745e44660cc87fcf925e6b386e9"></a>

### [`0045bd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd9c.md) → [`0045bddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bddc.md) FUN_0045bddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md)

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
      "definition_site": "0045bdec",
      "incomplete_value": false,
      "site": "0045bdf0",
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
      "definition_site": "0045bdac",
      "incomplete_value": false,
      "site": "0045bdb0",
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
      "0045bdf0",
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
      "0045bdf0",
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

- 旧版 [`0045bdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bd9c.md#insn-0045bdac)
- 新版 [`0045bdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bddc.md#insn-0045bdec)

~~~diff
- 0045bdac ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0045bdac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bdac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bdac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045bdec ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0045bdec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bdec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bdec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bdac bytes 29811b91
+ 0045bdec bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d781d7259c5362345307930e2d35d27"></a>

### [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) → [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) FUN_0045bdf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) · 呼出先 2件 [`0045bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) · 呼出先 2件 [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0045be14",
      "incomplete_value": false,
      "site": "0045be14",
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
      "definition_site": "0045bdd4",
      "incomplete_value": false,
      "site": "0045bdd4",
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
      "0045be14",
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
      "0045be14",
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

- 旧版 [`0045bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md#insn-0045bdcc) · [`0045bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md#insn-0045bdd8)
- 新版 [`0045be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md#insn-0045be0c) · [`0045be18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md#insn-0045be18)

~~~diff
- 0045bdcc ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0045bdcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045be0c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0045be0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045be0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045be0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bdcc bytes 08811b91
+ 0045be0c bytes 08812b91
- 0045bdd8 ["INT_ADD", "register:40f0:8", ["const:45bdd8:8", "const:4:8"]]
- 0045bdd8 ["CALL", null, ["callee:0045be2c:8"]]
+ 0045be18 ["INT_ADD", "register:40f0:8", ["const:45be18:8", "const:4:8"]]
+ 0045be18 ["CALL", null, ["callee:0045be2c:8"]]
- 0045bdd8 bytes 05000094
+ 0045be18 bytes 05000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f0435fef97ef0b72e1cb0f229d5704"></a>

### [`0045be54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be54.md) → [`0045be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be94.md) FUN_0045be94

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
      "definition_site": "0045bea0",
      "incomplete_value": false,
      "site": "0045beac",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045be60",
      "incomplete_value": false,
      "site": "0045be6c",
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
            "const:740:8"
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
      "0045beac",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045beac",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be54.md#insn-0045be60)
- 新版 [`0045bea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be94.md#insn-0045bea0)

~~~diff
- 0045be60 ["COPY", "tmp:0:8", ["const:740:8"]]
- 0045be60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045be60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045be60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045bea0 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0045bea0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045bea0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045bea0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045be60 bytes 4a011d91
+ 0045bea0 bytes 4a012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc83239128a35d039d33837a7b5b373"></a>

### [`0045be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md) → [`0045bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md) FUN_0045bed8

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
      "definition_site": "0045bef0",
      "incomplete_value": false,
      "site": "0045befc",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045beb0",
      "incomplete_value": false,
      "site": "0045bebc",
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
            "const:740:8"
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
      "0045befc",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045befc",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045beb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md#insn-0045beb0) · [`0045bee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045be98.md#insn-0045bee0)
- 新版 [`0045bef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md#insn-0045bef0) · [`0045bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md#insn-0045bf20)

~~~diff
- 0045beb0 ["COPY", "tmp:0:8", ["const:740:8"]]
- 0045beb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045beb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045beb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bef0 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0045bef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045beb0 bytes 08011d91
+ 0045bef0 bytes 08012d91
- 0045bee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bee0 ["INT_ADD", "register:40f0:8", ["const:45bee0:8", "const:4:8"]]
- 0045bee0 ["CALLIND", null, ["register:0:8"]]
+ 0045bf20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bf20 ["INT_ADD", "register:40f0:8", ["const:45bf20:8", "const:4:8"]]
+ 0045bf20 ["CALLIND", null, ["register:0:8"]]
- 0045bee0 bytes 00013fd6
+ 0045bf20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adecd13c6500a369f4bbd6009557555"></a>

### [`0045bef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md) → [`0045bf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md) FUN_0045bf34

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
      "definition_site": "0045bf60",
      "incomplete_value": false,
      "site": "0045bf60",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bf20",
      "incomplete_value": false,
      "site": "0045bf20",
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
            "const:740:8"
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
      "0045bf60",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bf60",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf08) · [`0045bf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf18) · [`0045bf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bef4.md#insn-0045bf3c)
- 新版 [`0045bf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf48) · [`0045bf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf58) · [`0045bf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf7c)

~~~diff
- 0045bf08 ["INT_ADD", "register:40f0:8", ["const:45bf08:8", "const:4:8"]]
- 0045bf08 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045bf48 ["INT_ADD", "register:40f0:8", ["const:45bf48:8", "const:4:8"]]
+ 0045bf48 ["CALL", null, ["callee:00c57e90:8"]]
- 0045bf08 bytes e2ee1f94
+ 0045bf48 bytes d2ef1f94
- 0045bf18 ["COPY", "tmp:0:8", ["const:740:8"]]
- 0045bf18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bf58 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0045bf58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bf18 bytes 08011d91
+ 0045bf58 bytes 08012d91
- 0045bf3c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bf3c ["INT_ADD", "register:40f0:8", ["const:45bf3c:8", "const:4:8"]]
- 0045bf3c ["CALLIND", null, ["register:0:8"]]
+ 0045bf7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bf7c ["INT_ADD", "register:40f0:8", ["const:45bf7c:8", "const:4:8"]]
+ 0045bf7c ["CALLIND", null, ["register:0:8"]]
- 0045bf3c bytes 00013fd6
+ 0045bf7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0dc3ad0352e7328716d86bade684a8f"></a>

### [`0045bf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md) → [`0045bfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md) FUN_0045bfbc

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
      "definition_site": "0045bfd8",
      "incomplete_value": false,
      "site": "0045bfd8",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bf98",
      "incomplete_value": false,
      "site": "0045bf98",
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
            "const:740:8"
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
      "0045bfd8",
      "DATA",
      [
        "storage",
        "00c63740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bfd8",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md#insn-0045bf94) · [`0045bfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bf7c.md#insn-0045bfb8)
- 新版 [`0045bfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md#insn-0045bfd4) · [`0045bff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md#insn-0045bff8)

~~~diff
- 0045bf94 ["COPY", "tmp:0:8", ["const:740:8"]]
- 0045bf94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bf94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bf94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045bfd4 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 0045bfd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bfd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bfd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bf94 bytes 29011d91
+ 0045bfd4 bytes 29012d91
- 0045bfb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045bfb8 ["INT_ADD", "register:40f0:8", ["const:45bfb8:8", "const:4:8"]]
- 0045bfb8 ["CALLIND", null, ["register:0:8"]]
+ 0045bff8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045bff8 ["INT_ADD", "register:40f0:8", ["const:45bff8:8", "const:4:8"]]
+ 0045bff8 ["CALLIND", null, ["register:0:8"]]
- 0045bfb8 bytes 20013fd6
+ 0045bff8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca3e2b3e83a94a7894c127163c28dc7b"></a>

### [`0045c078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md) → [`0045c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md) FUN_0045c0b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c100",
      "incomplete_value": true,
      "site": "0045c100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045c0c0",
      "incomplete_value": true,
      "site": "0045c0c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c284",
      "incomplete_value": true,
      "site": "0045c298",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c244",
      "incomplete_value": true,
      "site": "0045c258",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d4e:8"
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
      "definition_site": "0045c364",
      "incomplete_value": true,
      "site": "0045c364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045c324",
      "incomplete_value": true,
      "site": "0045c324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0045c0dc",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0045c284",
      "READ",
      [
        "storage",
        "002a1d4e",
        null,
        "string"
      ]
    ],
    [
      "0045c350",
      "READ",
      [
        "storage",
        "0029fe60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045c0dc",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0045c284",
      "READ",
      [
        "storage",
        "002a1e1b",
        null,
        "string"
      ]
    ],
    [
      "0045c350",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c100) · [`0045c094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c094) · [`0045c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c078.md#insn-0045c0d0)
- 新版 [`0045c140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c140) · [`0045c0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c0d4) · [`0045c110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c110)

~~~diff
- 0045c100 ["INT_ADD", "register:40f0:8", ["const:45c100:8", "const:4:8"]]
- 0045c100 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045c140 ["INT_ADD", "register:40f0:8", ["const:45c140:8", "const:4:8"]]
+ 0045c140 ["CALL", null, ["callee:00c57eb0:8"]]
- 0045c100 bytes 6cee1f94
+ 0045c140 bytes 5cef1f94
- 0045c094 ["COPY", "tmp:0:8", ["const:165:8"]]
- 0045c094 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c094 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c094 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c0d4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0045c0d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c0d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c0d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c094 bytes 4a950591
+ 0045c0d4 bytes 4a950691
- 0045c0d0 ["INT_ADD", "register:40f0:8", ["const:45c0d0:8", "const:4:8"]]
- 0045c0d0 ["CALL", null, ["callee:0044108c:8"]]
+ 0045c110 ["INT_ADD", "register:40f0:8", ["const:45c110:8", "const:4:8"]]
+ 0045c110 ["CALL", null, ["callee:0044108c:8"]]
- 0045c0d0 bytes df93ff97
+ 0045c110 bytes df93ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73cc22d01b3e90f92e3466accf752ff"></a>

### [`0045c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6a4.md) → [`0045c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c6e4.md) FUN_0045c6e4

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
      "definition_site": "0045c6f0",
      "incomplete_value": false,
      "site": "0045c6fc",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c6b0",
      "incomplete_value": false,
      "site": "0045c6bc",
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
            "const:7d0:8"
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
      "0045c6fc",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c6fc",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6a4.md#insn-0045c6b0)
- 新版 [`0045c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c6e4.md#insn-0045c6f0)

~~~diff
- 0045c6b0 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0045c6b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c6b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c6b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c6f0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0045c6f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c6f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c6f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c6b0 bytes 4a411f91
+ 0045c6f0 bytes 4a412f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28acd4d1f0494cc79945ae8ae51b48c8"></a>

### [`0045c6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md) → [`0045c728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md) FUN_0045c728

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
      "definition_site": "0045c740",
      "incomplete_value": false,
      "site": "0045c74c",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c700",
      "incomplete_value": false,
      "site": "0045c70c",
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
            "const:7d0:8"
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
      "0045c74c",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c74c",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md#insn-0045c700) · [`0045c730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c6e8.md#insn-0045c730)
- 新版 [`0045c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md#insn-0045c740) · [`0045c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md#insn-0045c770)

~~~diff
- 0045c700 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0045c700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c740 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0045c740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c700 bytes 08411f91
+ 0045c740 bytes 08412f91
- 0045c730 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c730 ["INT_ADD", "register:40f0:8", ["const:45c730:8", "const:4:8"]]
- 0045c730 ["CALLIND", null, ["register:0:8"]]
+ 0045c770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c770 ["INT_ADD", "register:40f0:8", ["const:45c770:8", "const:4:8"]]
+ 0045c770 ["CALLIND", null, ["register:0:8"]]
- 0045c730 bytes 00013fd6
+ 0045c770 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b20fca57506857b310d64960c6ba694"></a>

### [`0045c744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md) → [`0045c784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md) FUN_0045c784

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
      "definition_site": "0045c7b0",
      "incomplete_value": false,
      "site": "0045c7b0",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c770",
      "incomplete_value": false,
      "site": "0045c770",
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
            "const:7d0:8"
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
      "0045c7b0",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c7b0",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c758) · [`0045c768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c768) · [`0045c78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c744.md#insn-0045c78c)
- 新版 [`0045c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c798) · [`0045c7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c7a8) · [`0045c7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c7cc)

~~~diff
- 0045c758 ["INT_ADD", "register:40f0:8", ["const:45c758:8", "const:4:8"]]
- 0045c758 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045c798 ["INT_ADD", "register:40f0:8", ["const:45c798:8", "const:4:8"]]
+ 0045c798 ["CALL", null, ["callee:00c57e90:8"]]
- 0045c758 bytes ceec1f94
+ 0045c798 bytes beed1f94
- 0045c768 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0045c768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c7a8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0045c7a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c7a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c7a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c768 bytes 08411f91
+ 0045c7a8 bytes 08412f91
- 0045c78c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c78c ["INT_ADD", "register:40f0:8", ["const:45c78c:8", "const:4:8"]]
- 0045c78c ["CALLIND", null, ["register:0:8"]]
+ 0045c7cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c7cc ["INT_ADD", "register:40f0:8", ["const:45c7cc:8", "const:4:8"]]
+ 0045c7cc ["CALLIND", null, ["register:0:8"]]
- 0045c78c bytes 00013fd6
+ 0045c7cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d35d00cdb401667f38c16764bfdd6cfc"></a>

### [`0045c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md) → [`0045c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md) FUN_0045c80c

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
      "definition_site": "0045c828",
      "incomplete_value": false,
      "site": "0045c828",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c7e8",
      "incomplete_value": false,
      "site": "0045c7e8",
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
            "const:7d0:8"
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
      "0045c828",
      "DATA",
      [
        "storage",
        "00c637d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c828",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md#insn-0045c7e4) · [`0045c808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c7cc.md#insn-0045c808)
- 新版 [`0045c824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md#insn-0045c824) · [`0045c848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md#insn-0045c848)

~~~diff
- 0045c7e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0045c7e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045c7e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045c7e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c824 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 0045c824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045c7e4 bytes 29411f91
+ 0045c824 bytes 29412f91
- 0045c808 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045c808 ["INT_ADD", "register:40f0:8", ["const:45c808:8", "const:4:8"]]
- 0045c808 ["CALLIND", null, ["register:0:8"]]
+ 0045c848 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045c848 ["INT_ADD", "register:40f0:8", ["const:45c848:8", "const:4:8"]]
+ 0045c848 ["CALLIND", null, ["register:0:8"]]
- 0045c808 bytes 20013fd6
+ 0045c848 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-635203887c25c4c171dfb4eeb464a6bd"></a>

### [`0045cd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md) → [`0045cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md) FUN_0045cd8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045ca58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ca58.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0045ca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0045cd98",
      "incomplete_value": false,
      "site": "0045cd9c",
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
      "definition_site": "0045cd58",
      "incomplete_value": false,
      "site": "0045cd5c",
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
      "0045cd98",
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
      "0045cd98",
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

- 旧版 [`0045cd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md#insn-0045cd5c) · [`0045cd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd4c.md#insn-0045cd58)
- 新版 [`0045cd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md#insn-0045cd9c) · [`0045cd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md#insn-0045cd98)

~~~diff
- 0045cd5c ["INT_ADD", "register:40f0:8", ["const:45cd5c:8", "const:4:8"]]
- 0045cd5c ["CALL", null, ["callee:0043b778:8"]]
+ 0045cd9c ["INT_ADD", "register:40f0:8", ["const:45cd9c:8", "const:4:8"]]
+ 0045cd9c ["CALL", null, ["callee:0043b778:8"]]
- 0045cd5c bytes 777aff97
+ 0045cd9c bytes 777aff97
- 0045cd58 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0045cd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045cd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045cd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045cd98 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0045cd98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cd98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cd98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045cd58 bytes 00303c91
+ 0045cd98 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a5ddd529f676c2031455d18f981526a"></a>

### [`0045cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd60.md) → [`0045cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cda0.md) FUN_0045cda0

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
      "definition_site": "0045cdac",
      "incomplete_value": false,
      "site": "0045cdb8",
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
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cd6c",
      "incomplete_value": false,
      "site": "0045cd78",
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
            "const:860:8"
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
      "0045cdb8",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cdb8",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cd60.md#insn-0045cd6c)
- 新版 [`0045cdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cda0.md#insn-0045cdac)

~~~diff
- 0045cd6c ["COPY", "tmp:0:8", ["const:860:8"]]
- 0045cd6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045cd6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045cd6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045cdac ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0045cdac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cdac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cdac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045cd6c bytes 4a812191
+ 0045cdac bytes 4a813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c8232068533b371007d2ad80b42909"></a>

### [`0045cda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md) → [`0045cde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md) FUN_0045cde4

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
      "definition_site": "0045cdfc",
      "incomplete_value": false,
      "site": "0045ce08",
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
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cdbc",
      "incomplete_value": false,
      "site": "0045cdc8",
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
            "const:860:8"
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
      "0045ce08",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ce08",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md#insn-0045cdbc) · [`0045cdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cda4.md#insn-0045cdec)
- 新版 [`0045cdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md#insn-0045cdfc) · [`0045ce2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md#insn-0045ce2c)

~~~diff
- 0045cdbc ["COPY", "tmp:0:8", ["const:860:8"]]
- 0045cdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045cdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045cdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045cdfc ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0045cdfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cdfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cdfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045cdbc bytes 08812191
+ 0045cdfc bytes 08813191
- 0045cdec ["COPY", "register:0:8", ["register:4040:8"]]
- 0045cdec ["INT_ADD", "register:40f0:8", ["const:45cdec:8", "const:4:8"]]
- 0045cdec ["CALLIND", null, ["register:0:8"]]
+ 0045ce2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ce2c ["INT_ADD", "register:40f0:8", ["const:45ce2c:8", "const:4:8"]]
+ 0045ce2c ["CALLIND", null, ["register:0:8"]]
- 0045cdec bytes 00013fd6
+ 0045ce2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50de53e9867ff44513814ec433676b54"></a>

### [`0045ce00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md) → [`0045ce40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md) FUN_0045ce40

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
      "definition_site": "0045ce6c",
      "incomplete_value": false,
      "site": "0045ce6c",
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
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ce2c",
      "incomplete_value": false,
      "site": "0045ce2c",
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
            "const:860:8"
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
      "0045ce6c",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ce6c",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce14) · [`0045ce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce24) · [`0045ce48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce00.md#insn-0045ce48)
- 新版 [`0045ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce54) · [`0045ce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce64) · [`0045ce88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce88)

~~~diff
- 0045ce14 ["INT_ADD", "register:40f0:8", ["const:45ce14:8", "const:4:8"]]
- 0045ce14 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045ce54 ["INT_ADD", "register:40f0:8", ["const:45ce54:8", "const:4:8"]]
+ 0045ce54 ["CALL", null, ["callee:00c57e90:8"]]
- 0045ce14 bytes 1feb1f94
+ 0045ce54 bytes 0fec1f94
- 0045ce24 ["COPY", "tmp:0:8", ["const:860:8"]]
- 0045ce24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ce64 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0045ce64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ce24 bytes 08812191
+ 0045ce64 bytes 08813191
- 0045ce48 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045ce48 ["INT_ADD", "register:40f0:8", ["const:45ce48:8", "const:4:8"]]
- 0045ce48 ["CALLIND", null, ["register:0:8"]]
+ 0045ce88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ce88 ["INT_ADD", "register:40f0:8", ["const:45ce88:8", "const:4:8"]]
+ 0045ce88 ["CALLIND", null, ["register:0:8"]]
- 0045ce48 bytes 00013fd6
+ 0045ce88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6796f67e63f43ee5b114b3828b2e46f"></a>

### [`0045ce88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md) → [`0045cec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md) FUN_0045cec8

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
      "definition_site": "0045cee4",
      "incomplete_value": false,
      "site": "0045cee4",
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
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cea4",
      "incomplete_value": false,
      "site": "0045cea4",
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
            "const:860:8"
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
      "0045cee4",
      "DATA",
      [
        "storage",
        "00c63860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cee4",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md#insn-0045cea0) · [`0045cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ce88.md#insn-0045cec4)
- 新版 [`0045cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md#insn-0045cee0) · [`0045cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md#insn-0045cf04)

~~~diff
- 0045cea0 ["COPY", "tmp:0:8", ["const:860:8"]]
- 0045cea0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045cea0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045cea0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045cee0 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 0045cee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045cea0 bytes 29812191
+ 0045cee0 bytes 29813191
- 0045cec4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045cec4 ["INT_ADD", "register:40f0:8", ["const:45cec4:8", "const:4:8"]]
- 0045cec4 ["CALLIND", null, ["register:0:8"]]
+ 0045cf04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045cf04 ["INT_ADD", "register:40f0:8", ["const:45cf04:8", "const:4:8"]]
+ 0045cf04 ["CALLIND", null, ["register:0:8"]]
- 0045cec4 bytes 20013fd6
+ 0045cf04 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a161622aa69a0d91606641537b570528"></a>

### [`0045cf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md) → [`0045cfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cfc4.md) FUN_0045cfc4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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
      "definition_site": "0045d018",
      "incomplete_value": true,
      "site": "0045d018",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045cfd8",
      "incomplete_value": true,
      "site": "0045cfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045d148",
      "incomplete_value": true,
      "site": "0045d15c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d108",
      "incomplete_value": true,
      "site": "0045d11c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d4e:8"
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
      "definition_site": "0045d31c",
      "incomplete_value": false,
      "site": "0045d31c",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d2dc",
      "incomplete_value": false,
      "site": "0045d2dc",
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
            "const:718:8"
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
      "0045cfe4",
      "PARAM",
      [
        "storage",
        "00ca46e0",
        null,
        null
      ]
    ],
    [
      "0045d004",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0045d148",
      "READ",
      [
        "storage",
        "002a1d4e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045cfe4",
      "PARAM",
      [
        "storage",
        "00ca4ae0",
        null,
        null
      ]
    ],
    [
      "0045d004",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0045d148",
      "READ",
      [
        "storage",
        "002a1e1b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045cfb4) · [`0045d018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045d018) · [`0045d2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045cf84.md#insn-0045d2dc)
- 新版 [`0045cff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cfc4.md#insn-0045cff4) · [`0045d058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cfc4.md#insn-0045d058) · [`0045d31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cfc4.md#insn-0045d31c)

~~~diff
- 0045cfb4 ["INT_ADD", "register:40f0:8", ["const:45cfb4:8", "const:4:8"]]
- 0045cfb4 ["CALL", null, ["callee:00c580e0:8"]]
+ 0045cff4 ["INT_ADD", "register:40f0:8", ["const:45cff4:8", "const:4:8"]]
+ 0045cff4 ["CALL", null, ["callee:00c580e0:8"]]
- 0045cfb4 bytes 4beb1f94
+ 0045cff4 bytes 3bec1f94
- 0045d018 ["INT_ADD", "register:40f0:8", ["const:45d018:8", "const:4:8"]]
- 0045d018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045d058 ["INT_ADD", "register:40f0:8", ["const:45d058:8", "const:4:8"]]
+ 0045d058 ["CALL", null, ["callee:00c57eb0:8"]]
- 0045d018 bytes a6ea1f94
+ 0045d058 bytes 96eb1f94
- 0045d2dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
- 0045d2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0045d31c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 0045d31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0045d2dc bytes 148d03f9
+ 0045d31c bytes 148d05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b11b46b336b9e8a53932f04033df9c"></a>

### [`0045d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d750.md) → [`0045d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d790.md) FUN_0045d790

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
      "definition_site": "0045d79c",
      "incomplete_value": false,
      "site": "0045d7a8",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d75c",
      "incomplete_value": false,
      "site": "0045d768",
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
            "const:8e0:8"
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
      "0045d7a8",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d7a8",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d750.md#insn-0045d75c)
- 新版 [`0045d79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d790.md#insn-0045d79c)

~~~diff
- 0045d75c ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0045d75c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045d75c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045d75c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045d79c ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 0045d79c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d79c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d79c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045d75c bytes 4a812391
+ 0045d79c bytes 4a813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ec0d70b1ea23fa4d3742bb09c5e583"></a>

### [`0045d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md) → [`0045d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md) FUN_0045d7d4

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
      "definition_site": "0045d7ec",
      "incomplete_value": false,
      "site": "0045d7f8",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d7ac",
      "incomplete_value": false,
      "site": "0045d7b8",
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
            "const:8e0:8"
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
      "0045d7f8",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d7f8",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md#insn-0045d7ac) · [`0045d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d794.md#insn-0045d7dc)
- 新版 [`0045d7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md#insn-0045d7ec) · [`0045d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md#insn-0045d81c)

~~~diff
- 0045d7ac ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0045d7ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d7ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d7ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ec ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 0045d7ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d7ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d7ac bytes 08812391
+ 0045d7ec bytes 08813391
- 0045d7dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d7dc ["INT_ADD", "register:40f0:8", ["const:45d7dc:8", "const:4:8"]]
- 0045d7dc ["CALLIND", null, ["register:0:8"]]
+ 0045d81c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d81c ["INT_ADD", "register:40f0:8", ["const:45d81c:8", "const:4:8"]]
+ 0045d81c ["CALLIND", null, ["register:0:8"]]
- 0045d7dc bytes 00013fd6
+ 0045d81c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e82110d21412fb3e44747619fcc8459"></a>

### [`0045d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md) → [`0045d830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md) FUN_0045d830

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
      "definition_site": "0045d85c",
      "incomplete_value": false,
      "site": "0045d85c",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d81c",
      "incomplete_value": false,
      "site": "0045d81c",
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
            "const:8e0:8"
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
      "0045d85c",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d85c",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d804) · [`0045d814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d814) · [`0045d838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d7f0.md#insn-0045d838)
- 新版 [`0045d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d844) · [`0045d854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d854) · [`0045d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d878)

~~~diff
- 0045d804 ["INT_ADD", "register:40f0:8", ["const:45d804:8", "const:4:8"]]
- 0045d804 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045d844 ["INT_ADD", "register:40f0:8", ["const:45d844:8", "const:4:8"]]
+ 0045d844 ["CALL", null, ["callee:00c57e90:8"]]
- 0045d804 bytes a3e81f94
+ 0045d844 bytes 93e91f94
- 0045d814 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0045d814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d854 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 0045d854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d814 bytes 08812391
+ 0045d854 bytes 08813391
- 0045d838 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d838 ["INT_ADD", "register:40f0:8", ["const:45d838:8", "const:4:8"]]
- 0045d838 ["CALLIND", null, ["register:0:8"]]
+ 0045d878 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d878 ["INT_ADD", "register:40f0:8", ["const:45d878:8", "const:4:8"]]
+ 0045d878 ["CALLIND", null, ["register:0:8"]]
- 0045d838 bytes 00013fd6
+ 0045d878 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b15764011b055b27ca9e04530f28a369"></a>

### [`0045d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md) → [`0045d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md) FUN_0045d8b8

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
      "definition_site": "0045d8d4",
      "incomplete_value": false,
      "site": "0045d8d4",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d894",
      "incomplete_value": false,
      "site": "0045d894",
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
            "const:8e0:8"
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
      "0045d8d4",
      "DATA",
      [
        "storage",
        "00c638e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d8d4",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md#insn-0045d890) · [`0045d8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d878.md#insn-0045d8b4)
- 新版 [`0045d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md#insn-0045d8d0) · [`0045d8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md#insn-0045d8f4)

~~~diff
- 0045d890 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0045d890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045d890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045d890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045d8d0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 0045d8d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d8d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d8d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045d890 bytes 29812391
+ 0045d8d0 bytes 29813391
- 0045d8b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045d8b4 ["INT_ADD", "register:40f0:8", ["const:45d8b4:8", "const:4:8"]]
- 0045d8b4 ["CALLIND", null, ["register:0:8"]]
+ 0045d8f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045d8f4 ["INT_ADD", "register:40f0:8", ["const:45d8f4:8", "const:4:8"]]
+ 0045d8f4 ["CALLIND", null, ["register:0:8"]]
- 0045d8b4 bytes 20013fd6
+ 0045d8f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dfebfa8e48f7de2a23a789104de4835"></a>

### [`0045d974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md) → [`0045d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md) FUN_0045d9b4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "0045dac8",
      "incomplete_value": false,
      "site": "0045dac8",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045da88",
      "incomplete_value": false,
      "site": "0045da88",
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
            "const:718:8"
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
      "definition_site": "0045dacc",
      "incomplete_value": false,
      "site": "0045dacc",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045da8c",
      "incomplete_value": false,
      "site": "0045da8c",
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
            "const:730:8"
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
      "definition_site": "0045da10",
      "incomplete_value": true,
      "site": "0045da10",
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
      "definition_site": "0045d9d0",
      "incomplete_value": true,
      "site": "0045d9d0",
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
      "0045da08",
      "READ",
      [
        "storage",
        "00ca4710",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da08",
      "READ",
      [
        "storage",
        "00ca4718",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da74",
      "READ",
      [
        "storage",
        "00ca4710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045da08",
      "READ",
      [
        "storage",
        "00ca4b10",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da08",
      "READ",
      [
        "storage",
        "00ca4b18",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da74",
      "READ",
      [
        "storage",
        "00ca4b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045da88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045da88) · [`0045da8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045da8c) · [`0045dac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md#insn-0045dac8)
- 新版 [`0045dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045dac8) · [`0045dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045dacc) · [`0045db08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045db08)

~~~diff
- 0045da88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
- 0045da88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045dac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 0045dac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045da88 bytes 138d03f9
+ 0045dac8 bytes 138d05f9
- 0045da8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0045da8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0045da8c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:730:8"]]
- 0045da8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0045dacc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0045dacc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0045dacc ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:b30:8"]]
+ 0045dacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0045da8c bytes 3fc11c39
+ 0045dacc bytes 3fc12c39
- 0045dac8 ["INT_ADD", "register:40f0:8", ["const:45dac8:8", "const:4:8"]]
- 0045dac8 ["CALL", null, ["callee:00459d74:8"]]
+ 0045db08 ["INT_ADD", "register:40f0:8", ["const:45db08:8", "const:4:8"]]
+ 0045db08 ["CALL", null, ["callee:00459d74:8"]]
- 0045dac8 bytes 9bf0ff97
+ 0045db08 bytes 9bf0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59f2566ac1e178d18812cc56163e110"></a>

### [`0045de2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md) → [`0045de6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md) FUN_0045de6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045db38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045db38.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0045db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0045de78",
      "incomplete_value": false,
      "site": "0045de7c",
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
      "definition_site": "0045de38",
      "incomplete_value": false,
      "site": "0045de3c",
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
      "0045de78",
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
      "0045de78",
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

- 旧版 [`0045de3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md#insn-0045de3c) · [`0045de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de2c.md#insn-0045de38)
- 新版 [`0045de7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md#insn-0045de7c) · [`0045de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md#insn-0045de78)

~~~diff
- 0045de3c ["INT_ADD", "register:40f0:8", ["const:45de3c:8", "const:4:8"]]
- 0045de3c ["CALL", null, ["callee:0043b778:8"]]
+ 0045de7c ["INT_ADD", "register:40f0:8", ["const:45de7c:8", "const:4:8"]]
+ 0045de7c ["CALL", null, ["callee:0043b778:8"]]
- 0045de3c bytes 3f76ff97
+ 0045de7c bytes 3f76ff97
- 0045de38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0045de38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045de38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045de38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045de78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0045de78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045de78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045de78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045de38 bytes 00303c91
+ 0045de78 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c111ace10fc3409430e1cc7a51c8d2b"></a>

### [`0045de44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md) → [`0045de84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md) FUN_0045de84

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
      "definition_site": "0045dea8",
      "incomplete_value": false,
      "site": "0045dea8",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045de68",
      "incomplete_value": false,
      "site": "0045de68",
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
            "const:970:8"
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
      "0045dea8",
      "DATA",
      [
        "storage",
        "00c63970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045dea8",
      "DATA",
      [
        "storage",
        "00c63d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045de58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md#insn-0045de58) · [`0045de64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de44.md#insn-0045de64)
- 新版 [`0045de98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md#insn-0045de98) · [`0045dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md#insn-0045dea4)

~~~diff
- 0045de58 ["INT_ADD", "register:40f0:8", ["const:45de58:8", "const:4:8"]]
- 0045de58 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045de98 ["INT_ADD", "register:40f0:8", ["const:45de98:8", "const:4:8"]]
+ 0045de98 ["CALL", null, ["callee:00c57e90:8"]]
- 0045de58 bytes 0ee71f94
+ 0045de98 bytes fee71f94
- 0045de64 ["COPY", "tmp:0:8", ["const:970:8"]]
- 0045de64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045de64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045de64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045dea4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0045dea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045de64 bytes 08c12591
+ 0045dea4 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-460705f8139ef7ad1421541bfdc9e667"></a>

### [`0045de78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de78.md) → [`0045deb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045deb8.md) FUN_0045deb8

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
      "definition_site": "0045dec4",
      "incomplete_value": false,
      "site": "0045dec4",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045de84",
      "incomplete_value": false,
      "site": "0045de84",
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
            "const:970:8"
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
      "0045dec4",
      "DATA",
      [
        "storage",
        "00c63970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045dec4",
      "DATA",
      [
        "storage",
        "00c63d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045de80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de78.md#insn-0045de80)
- 新版 [`0045dec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045deb8.md#insn-0045dec0)

~~~diff
- 0045de80 ["COPY", "tmp:0:8", ["const:970:8"]]
- 0045de80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045de80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045de80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045dec0 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0045dec0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045dec0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045dec0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045de80 bytes 29c12591
+ 0045dec0 bytes 29c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60ef002aae9e2988aa2109dda958417b"></a>

### [`0045de94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de94.md) → [`0045ded4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md) FUN_0045ded4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)

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
      "definition_site": "0045df28",
      "incomplete_value": true,
      "site": "0045df28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045dee8",
      "incomplete_value": true,
      "site": "0045dee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e2b4",
      "incomplete_value": false,
      "site": "0045e2b4",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e274",
      "incomplete_value": false,
      "site": "0045e274",
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
            "const:770:8"
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
      "definition_site": "0045e2b8",
      "incomplete_value": false,
      "site": "0045e2b8",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e278",
      "incomplete_value": false,
      "site": "0045e278",
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
            "const:788:8"
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
      "0045def4",
      "PARAM",
      [
        "storage",
        "00ca4734",
        null,
        null
      ]
    ],
    [
      "0045df14",
      "READ",
      [
        "storage",
        "002b7165",
        null,
        "string"
      ]
    ],
    [
      "0045e03c",
      "READ",
      [
        "storage",
        "00ca4768",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045def4",
      "PARAM",
      [
        "storage",
        "00ca4b34",
        null,
        null
      ]
    ],
    [
      "0045df14",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0045e03c",
      "READ",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045dec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de94.md#insn-0045dec4) · [`0045df28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de94.md#insn-0045df28) · [`0045e274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045de94.md#insn-0045e274)
- 新版 [`0045df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045df04) · [`0045df68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045df68) · [`0045e2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045e2b4)

~~~diff
- 0045dec4 ["INT_ADD", "register:40f0:8", ["const:45dec4:8", "const:4:8"]]
- 0045dec4 ["CALL", null, ["callee:00c580e0:8"]]
+ 0045df04 ["INT_ADD", "register:40f0:8", ["const:45df04:8", "const:4:8"]]
+ 0045df04 ["CALL", null, ["callee:00c580e0:8"]]
- 0045dec4 bytes 87e71f94
+ 0045df04 bytes 77e81f94
- 0045df28 ["INT_ADD", "register:40f0:8", ["const:45df28:8", "const:4:8"]]
- 0045df28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045df68 ["INT_ADD", "register:40f0:8", ["const:45df68:8", "const:4:8"]]
+ 0045df68 ["CALL", null, ["callee:00c57eb0:8"]]
- 0045df28 bytes e2e61f94
+ 0045df68 bytes d2e71f94
- 0045e274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
- 0045e274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045e2b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
+ 0045e2b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045e274 bytes 13b903f9
+ 0045e2b4 bytes 13b905f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19241ff753e951ed84cfffa9b4c25bf"></a>

### [`0045e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md) → [`0045e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md) FUN_0045e470

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
      "definition_site": "0045e494",
      "incomplete_value": false,
      "site": "0045e494",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e454",
      "incomplete_value": false,
      "site": "0045e454",
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
            "const:9f0:8"
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
      "0045e494",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e494",
      "DATA",
      [
        "storage",
        "00c63df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md#insn-0045e444) · [`0045e450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e430.md#insn-0045e450)
- 新版 [`0045e484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md#insn-0045e484) · [`0045e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md#insn-0045e490)

~~~diff
- 0045e444 ["INT_ADD", "register:40f0:8", ["const:45e444:8", "const:4:8"]]
- 0045e444 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045e484 ["INT_ADD", "register:40f0:8", ["const:45e484:8", "const:4:8"]]
+ 0045e484 ["CALL", null, ["callee:00c57e90:8"]]
- 0045e444 bytes 93e51f94
+ 0045e484 bytes 83e61f94
- 0045e450 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045e450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e490 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 0045e490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e450 bytes 08c12791
+ 0045e490 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73909f15ccd7a80111e66df171df3b7d"></a>

### [`0045e464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e464.md) → [`0045e4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4a4.md) FUN_0045e4a4

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
      "definition_site": "0045e4b0",
      "incomplete_value": false,
      "site": "0045e4b0",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e470",
      "incomplete_value": false,
      "site": "0045e470",
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
            "const:9f0:8"
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
      "0045e4b0",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e4b0",
      "DATA",
      [
        "storage",
        "00c63df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e464.md#insn-0045e46c)
- 新版 [`0045e4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4a4.md#insn-0045e4ac)

~~~diff
- 0045e46c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045e46c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045e46c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045e46c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ac ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 0045e4ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045e46c bytes 29c12791
+ 0045e4ac bytes 29c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10ab99a65f91a99e0f0584374f53cfdc"></a>

### [`0045e480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md) → [`0045e4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md) FUN_0045e4c0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00769084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768a28.md) [`007690c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007690c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 2件, `store_destination` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e5c8",
      "incomplete_value": false,
      "site": "0045e5c8",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e588",
      "incomplete_value": false,
      "site": "0045e588",
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
            "const:770:8"
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
      "definition_site": "0045e5cc",
      "incomplete_value": false,
      "site": "0045e5cc",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e58c",
      "incomplete_value": false,
      "site": "0045e58c",
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
            "const:788:8"
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
      "definition_site": "0045e528",
      "incomplete_value": true,
      "site": "0045e528",
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
      "definition_site": "0045e4e8",
      "incomplete_value": true,
      "site": "0045e4e8",
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
      "0045e4fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689e8"
      ]
    ],
    [
      "unmatched:0045e4c0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0045e504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ]
  ],
  "added": [
    [
      "0045e4fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768a28"
      ]
    ],
    [
      "0045e500",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0045e504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007690c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md#insn-0045e4bc) · [`0045e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md#insn-0045e4c0) · [`0045e4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e480.md#insn-0045e4c4)
- 新版 [`0045e4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md#insn-0045e4fc) · [`0045e504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md#insn-0045e504)

~~~diff
- 0045e4bc ["INT_ADD", "register:40f0:8", ["const:45e4bc:8", "const:4:8"]]
- 0045e4bc ["CALL", null, ["ram:7689e8:8"]]
+ 0045e4fc ["INT_ADD", "register:40f0:8", ["const:45e4fc:8", "const:4:8"]]
+ 0045e4fc ["CALL", null, ["ram:768a28:8"]]
- 0045e4bc bytes 4b290c94
+ 0045e4fc bytes 4b290c94
- 0045e4c0 ["INT_ADD", "register:40f0:8", ["const:45e4c0:8", "const:4:8"]]
- 0045e4c0 ["CALL", null, ["callee:008514f8:8"]]
- 0045e4c0 bytes fecb0f94
- 0045e4c4 ["INT_ADD", "register:40f0:8", ["const:45e4c4:8", "const:4:8"]]
- 0045e4c4 ["CALL", null, ["ram:769084:8"]]
+ 0045e504 ["INT_ADD", "register:40f0:8", ["const:45e504:8", "const:4:8"]]
+ 0045e504 ["CALL", null, ["ram:7690c4:8"]]
- 0045e4c4 bytes f02a0c94
+ 0045e504 bytes f02a0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b391d7f8814ec7245d86daa02f0113dd"></a>

### [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) → [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) FUN_0045e668

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0045f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0045ebe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045e714",
      "incomplete_value": true,
      "site": "0045e724",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e99:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e6d4",
      "incomplete_value": true,
      "site": "0045e6e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e59:8"
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
      "definition_site": "0045e78c",
      "incomplete_value": true,
      "site": "0045e78c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e74c",
      "incomplete_value": true,
      "site": "0045e74c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed9:8"
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
      "definition_site": "0045e828",
      "incomplete_value": true,
      "site": "0045e840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0045e7e8",
      "incomplete_value": true,
      "site": "0045e800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0045e714",
      "READ",
      [
        "storage",
        "002b5e59",
        null,
        "string"
      ]
    ],
    [
      "0045e778",
      "READ",
      [
        "storage",
        "002a0ed9",
        null,
        "string"
      ]
    ],
    [
      "0045e828",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045e714",
      "READ",
      [
        "storage",
        "002b5e99",
        null,
        "string"
      ]
    ],
    [
      "0045e778",
      "READ",
      [
        "storage",
        "002a0fa6",
        null,
        "string"
      ]
    ],
    [
      "0045e828",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e70c) · [`0045e844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e844) · [`0045e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md#insn-0045e89c)
- 新版 [`0045e74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md#insn-0045e74c) · [`0045e884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md#insn-0045e884)

~~~diff
- 0045e70c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045e70c ["INT_ADD", "register:40f0:8", ["const:45e70c:8", "const:4:8"]]
- 0045e70c ["CALLIND", null, ["register:0:8"]]
+ 0045e74c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045e74c ["INT_ADD", "register:40f0:8", ["const:45e74c:8", "const:4:8"]]
+ 0045e74c ["CALLIND", null, ["register:0:8"]]
- 0045e70c bytes 00013fd6
+ 0045e74c bytes 00013fd6
- 0045e844 ["COPY", "tmp:0:8", ["const:611:8"]]
- 0045e844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e884 ["COPY", "tmp:0:8", ["const:651:8"]]
+ 0045e884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e844 bytes 08451891
+ 0045e884 bytes 08451991
- 0045e89c ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0045e89c bytes 29f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2068034d00a145355aca0ce3e79aafd8"></a>

### [`0045eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md) → [`0045ebe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md) FUN_0045ebe4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.03% / 新版 82.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ec30",
      "incomplete_value": true,
      "site": "0045ec30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ebf0",
      "incomplete_value": true,
      "site": "0045ebf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9fd:8"
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
      "definition_site": "0045ec34",
      "incomplete_value": true,
      "site": "0045ec34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045ebf4",
      "incomplete_value": true,
      "site": "0045ebf4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045ec9c",
      "incomplete_value": true,
      "site": "0045ec9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ec5c",
      "incomplete_value": true,
      "site": "0045ec5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e6b:8"
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
      "0045ec20",
      "READ",
      [
        "storage",
        "002a89fd",
        null,
        "string"
      ]
    ],
    [
      "0045ec24",
      "READ",
      [
        "storage",
        "002a8a03",
        null,
        "string"
      ]
    ],
    [
      "0045ec88",
      "READ",
      [
        "storage",
        "002b5e6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045ec20",
      "READ",
      [
        "storage",
        "002a8aca",
        null,
        "string"
      ]
    ],
    [
      "0045ec24",
      "READ",
      [
        "storage",
        "002a8ad0",
        null,
        "string"
      ]
    ],
    [
      "0045ec88",
      "READ",
      [
        "storage",
        "002b5eab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md#insn-0045ec9c) · [`0045ebd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md#insn-0045ebd8) · [`0045ebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eba4.md#insn-0045ebdc)
- 新版 [`0045ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md#insn-0045ecdc) · [`0045ec18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md#insn-0045ec18)

~~~diff
- 0045ec9c ["INT_ADD", "register:40f0:8", ["const:45ec9c:8", "const:4:8"]]
- 0045ec9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045ecdc ["INT_ADD", "register:40f0:8", ["const:45ecdc:8", "const:4:8"]]
+ 0045ecdc ["CALL", null, ["callee:00c57eb0:8"]]
- 0045ec9c bytes 85e31f94
+ 0045ecdc bytes 75e41f94
- 0045ebd8 ["COPY", "tmp:0:8", ["const:9fd:8"]]
- 0045ebd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ebd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ebd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ec18 ["COPY", "tmp:0:8", ["const:aca:8"]]
+ 0045ec18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ec18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ec18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ebd8 bytes 29f52791
+ 0045ec18 bytes 29292b91
- 0045ebdc ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0045ebdc bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9089ab3a00a2ff3691425c09648c43e1"></a>

### [`0045eddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eddc.md) → [`0045ee1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee1c.md) FUN_0045ee1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045ee20",
      "incomplete_value": false,
      "site": "0045ee24",
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
      "definition_site": "0045ede0",
      "incomplete_value": false,
      "site": "0045ede4",
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
      "0045ee24",
      "DATA",
      [
        "storage",
        "00c63a70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045ee24",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eddc.md#insn-0045ede0)
- 新版 [`0045ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee1c.md#insn-0045ee20)

~~~diff
- 0045ede0 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0045ede0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ede0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ede0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ee20 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0045ee20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ede0 bytes 08c12991
+ 0045ee20 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ece7955e69a658e54f30f2a4c39beeba"></a>

### [`0045edec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045edec.md) → [`0045ee2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md) FUN_0045ee2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045ee3c",
      "incomplete_value": false,
      "site": "0045ee44",
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
      "definition_site": "0045edfc",
      "incomplete_value": false,
      "site": "0045ee04",
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
      "0045ee44",
      "DATA",
      [
        "storage",
        "00c63a70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045ee44",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045edfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045edec.md#insn-0045edfc) · [`0045ee08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045edec.md#insn-0045ee08)
- 新版 [`0045ee3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md#insn-0045ee3c) · [`0045ee48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md#insn-0045ee48)

~~~diff
- 0045edfc ["COPY", "tmp:0:8", ["const:a70:8"]]
- 0045edfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045edfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045edfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ee3c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0045ee3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045edfc bytes 08c12991
+ 0045ee3c bytes 08c13991
- 0045ee08 ["INT_ADD", "register:40f0:8", ["const:45ee08:8", "const:4:8"]]
- 0045ee08 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0045ee48 ["INT_ADD", "register:40f0:8", ["const:45ee48:8", "const:4:8"]]
+ 0045ee48 ["CALL", null, ["callee:00c57ea0:8"]]
- 0045ee08 bytes 26e31f94
+ 0045ee48 bytes 16e41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80670124835cc669f0788d74a45ab979"></a>

### [`0045ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee28.md) → [`0045ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md) FUN_0045ee68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "0045ee8c",
      "incomplete_value": true,
      "site": "0045ee8c",
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
      "definition_site": "0045ee4c",
      "incomplete_value": true,
      "site": "0045ee4c",
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
      "0045ee80",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "0045ee8c",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0045ee80",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0045ee8c",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee28.md#insn-0045ee40) · [`0045ee50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee28.md#insn-0045ee50) · [`0045ee58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee28.md#insn-0045ee58)
- 新版 [`0045ee80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee80) · [`0045ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee90) · [`0045ee98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee98)

~~~diff
- 0045ee40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 0045ee40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045ee80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 0045ee80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045ee40 bytes 082944f9
+ 0045ee80 bytes 082946f9
- 0045ee50 ["INT_ADD", "register:40f0:8", ["const:45ee50:8", "const:4:8"]]
- 0045ee50 ["CALL", null, ["callee:00c580d0:8"]]
+ 0045ee90 ["INT_ADD", "register:40f0:8", ["const:45ee90:8", "const:4:8"]]
+ 0045ee90 ["CALL", null, ["callee:00c580d0:8"]]
- 0045ee50 bytes a0e31f94
+ 0045ee90 bytes 90e41f94
- 0045ee58 ["INT_ADD", "register:40f0:8", ["const:45ee58:8", "const:4:8"]]
- 0045ee58 ["CALL", null, ["callee:00c57e60:8"]]
+ 0045ee98 ["INT_ADD", "register:40f0:8", ["const:45ee98:8", "const:4:8"]]
+ 0045ee98 ["CALL", null, ["callee:00c57e60:8"]]
- 0045ee58 bytes 02e31f94
+ 0045ee98 bytes f2e31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0758a68a0bf83d718f765f73b2e3950"></a>

### [`0045ee74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee74.md) → [`0045eeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md) FUN_0045eeb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "0045eed8",
      "incomplete_value": true,
      "site": "0045eed8",
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
      "definition_site": "0045ee98",
      "incomplete_value": true,
      "site": "0045ee98",
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
      "0045eecc",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "0045eed8",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0045eecc",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0045eed8",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee74.md#insn-0045ee8c) · [`0045ee9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee74.md#insn-0045ee9c) · [`0045eea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee74.md#insn-0045eea4)
- 新版 [`0045eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eecc) · [`0045eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eedc) · [`0045eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eee4)

~~~diff
- 0045ee8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 0045ee8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045eecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 0045eecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045ee8c bytes 082944f9
+ 0045eecc bytes 082946f9
- 0045ee9c ["INT_ADD", "register:40f0:8", ["const:45ee9c:8", "const:4:8"]]
- 0045ee9c ["CALL", null, ["callee:00c580d0:8"]]
+ 0045eedc ["INT_ADD", "register:40f0:8", ["const:45eedc:8", "const:4:8"]]
+ 0045eedc ["CALL", null, ["callee:00c580d0:8"]]
- 0045ee9c bytes 8de31f94
+ 0045eedc bytes 7de41f94
- 0045eea4 ["INT_ADD", "register:40f0:8", ["const:45eea4:8", "const:4:8"]]
- 0045eea4 ["CALL", null, ["callee:00c57e60:8"]]
+ 0045eee4 ["INT_ADD", "register:40f0:8", ["const:45eee4:8", "const:4:8"]]
+ 0045eee4 ["CALL", null, ["callee:00c57e60:8"]]
- 0045eea4 bytes efe21f94
+ 0045eee4 bytes dfe31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f983d6403cd604bb24a07289a19535dd"></a>

### [`0045eed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md) → [`0045ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md) FUN_0045ef14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045ee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045ee1c.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`0045ee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee5c.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

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
      "definition_site": "0045efb8",
      "incomplete_value": true,
      "site": "0045efbc",
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
      "definition_site": "0045ef78",
      "incomplete_value": true,
      "site": "0045ef7c",
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
      "definition_site": "0045ef94",
      "incomplete_value": true,
      "site": "0045ef9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045ef54",
      "incomplete_value": true,
      "site": "0045ef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0045ef90",
      "incomplete_value": false,
      "site": "0045ef9c",
      "value": [
        "leaf",
        "const:45a6c8:8"
      ]
    },
    "old": {
      "definition_site": "0045ef50",
      "incomplete_value": false,
      "site": "0045ef5c",
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
      "0045ef90",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "0045ef94",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "0045ef94",
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
      "0045ef90",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "0045ef94",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045ef94",
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

- 旧版 [`0045ef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef3c) · [`0045ef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef5c) · [`0045ef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045eed4.md#insn-0045ef14)
- 新版 [`0045ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef7c) · [`0045ef9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef9c) · [`0045ef54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef54)

~~~diff
- 0045ef3c ["INT_ADD", "register:40f0:8", ["const:45ef3c:8", "const:4:8"]]
- 0045ef3c ["CALL", null, ["callee:00c58320:8"]]
+ 0045ef7c ["INT_ADD", "register:40f0:8", ["const:45ef7c:8", "const:4:8"]]
+ 0045ef7c ["CALL", null, ["callee:00c58320:8"]]
- 0045ef3c bytes f9e31f94
+ 0045ef7c bytes e9e41f94
- 0045ef5c ["INT_ADD", "register:40f0:8", ["const:45ef5c:8", "const:4:8"]]
- 0045ef5c ["CALL", null, ["callee:00c58330:8"]]
+ 0045ef9c ["INT_ADD", "register:40f0:8", ["const:45ef9c:8", "const:4:8"]]
+ 0045ef9c ["CALL", null, ["callee:00c58330:8"]]
- 0045ef5c bytes f5e31f94
+ 0045ef9c bytes e5e41f94
- 0045ef14 ["INT_ADD", "register:40f0:8", ["const:45ef14:8", "const:4:8"]]
- 0045ef14 ["CALL", null, ["callee:00c582f0:8"]]
+ 0045ef54 ["INT_ADD", "register:40f0:8", ["const:45ef54:8", "const:4:8"]]
+ 0045ef54 ["CALL", null, ["callee:00c582f0:8"]]
- 0045ef14 bytes f7e31f94
+ 0045ef54 bytes e7e41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d3bf4cf69b7b8e4fd16fa489173b4a"></a>

### [`0045f0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f0f8.md) → [`0045f138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f138.md) FUN_0045f138

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
      "definition_site": "0045f144",
      "incomplete_value": false,
      "site": "0045f150",
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
    "old": {
      "definition_site": "0045f104",
      "incomplete_value": false,
      "site": "0045f110",
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
            "const:b18:8"
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
      "0045f150",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f150",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f0f8.md#insn-0045f104)
- 新版 [`0045f144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f138.md#insn-0045f144)

~~~diff
- 0045f104 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0045f104 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f104 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f104 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f144 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0045f144 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f144 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f144 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f104 bytes 4a612c91
+ 0045f144 bytes 4a613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96573b875f965cd4dba9d54b8340fc43"></a>

### [`0045f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md) → [`0045f17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md) FUN_0045f17c

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
      "definition_site": "0045f194",
      "incomplete_value": false,
      "site": "0045f1a0",
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
    "old": {
      "definition_site": "0045f154",
      "incomplete_value": false,
      "site": "0045f160",
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
            "const:b18:8"
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
      "0045f1a0",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f1a0",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md#insn-0045f154) · [`0045f184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f13c.md#insn-0045f184)
- 新版 [`0045f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md#insn-0045f194) · [`0045f1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md#insn-0045f1c4)

~~~diff
- 0045f154 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0045f154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f194 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0045f194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f154 bytes 08612c91
+ 0045f194 bytes 08613c91
- 0045f184 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f184 ["INT_ADD", "register:40f0:8", ["const:45f184:8", "const:4:8"]]
- 0045f184 ["CALLIND", null, ["register:0:8"]]
+ 0045f1c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f1c4 ["INT_ADD", "register:40f0:8", ["const:45f1c4:8", "const:4:8"]]
+ 0045f1c4 ["CALLIND", null, ["register:0:8"]]
- 0045f184 bytes 00013fd6
+ 0045f1c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5cbbd6dacaf4850fd7744c55958d74"></a>

### [`0045f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md) → [`0045f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md) FUN_0045f1d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0045f204",
      "incomplete_value": false,
      "site": "0045f204",
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
    "old": {
      "definition_site": "0045f1c4",
      "incomplete_value": false,
      "site": "0045f1c4",
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
            "const:b18:8"
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
      "0045f204",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f204",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1ac) · [`0045f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1bc) · [`0045f1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f198.md#insn-0045f1e0)
- 新版 [`0045f1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f1ec) · [`0045f1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f1fc) · [`0045f220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f220)

~~~diff
- 0045f1ac ["INT_ADD", "register:40f0:8", ["const:45f1ac:8", "const:4:8"]]
- 0045f1ac ["CALL", null, ["callee:00c57e90:8"]]
+ 0045f1ec ["INT_ADD", "register:40f0:8", ["const:45f1ec:8", "const:4:8"]]
+ 0045f1ec ["CALL", null, ["callee:00c57e90:8"]]
- 0045f1ac bytes 39e21f94
+ 0045f1ec bytes 29e31f94
- 0045f1bc ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0045f1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f1fc ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0045f1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f1bc bytes 08612c91
+ 0045f1fc bytes 08613c91
- 0045f1e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f1e0 ["INT_ADD", "register:40f0:8", ["const:45f1e0:8", "const:4:8"]]
- 0045f1e0 ["CALLIND", null, ["register:0:8"]]
+ 0045f220 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f220 ["INT_ADD", "register:40f0:8", ["const:45f220:8", "const:4:8"]]
+ 0045f220 ["CALLIND", null, ["register:0:8"]]
- 0045f1e0 bytes 00013fd6
+ 0045f220 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba06a94918f7a8bab06037f801482c8"></a>

### [`0045f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md) → [`0045f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md) FUN_0045f268

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0045f288",
      "incomplete_value": false,
      "site": "0045f288",
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
    "old": {
      "definition_site": "0045f248",
      "incomplete_value": false,
      "site": "0045f248",
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
            "const:b18:8"
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
      "0045f288",
      "DATA",
      [
        "storage",
        "00c63b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f288",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f288) · [`0045f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f244) · [`0045f264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f228.md#insn-0045f264)
- 新版 [`0045f2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f2c8) · [`0045f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f284) · [`0045f2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f2a4)

~~~diff
- 0045f288 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f288 ["INT_ADD", "register:40f0:8", ["const:45f288:8", "const:4:8"]]
- 0045f288 ["CALLIND", null, ["register:0:8"]]
+ 0045f2c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f2c8 ["INT_ADD", "register:40f0:8", ["const:45f2c8:8", "const:4:8"]]
+ 0045f2c8 ["CALLIND", null, ["register:0:8"]]
- 0045f288 bytes 00013fd6
+ 0045f2c8 bytes 00013fd6
- 0045f244 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0045f244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f284 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0045f284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f244 bytes 08612c91
+ 0045f284 bytes 08613c91
- 0045f264 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f264 ["INT_ADD", "register:40f0:8", ["const:45f264:8", "const:4:8"]]
- 0045f264 ["CALLIND", null, ["register:0:8"]]
+ 0045f2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f2a4 ["INT_ADD", "register:40f0:8", ["const:45f2a4:8", "const:4:8"]]
+ 0045f2a4 ["CALLIND", null, ["register:0:8"]]
- 0045f264 bytes 00013fd6
+ 0045f2a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2619564c74974c4011f581a63cf9955d"></a>

### [`0045f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md) → [`0045f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md) FUN_0045f368

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0045e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045e/0045e628.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "0045f414",
      "incomplete_value": true,
      "site": "0045f414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f3d4",
      "incomplete_value": true,
      "site": "0045f3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d63:8"
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
      "0045f400",
      "READ",
      [
        "storage",
        "002a1d63",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045f400",
      "READ",
      [
        "storage",
        "002a1e30",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f414) · [`0045f380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f380) · [`0045f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f328.md#insn-0045f3ac)
- 新版 [`0045f454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f454) · [`0045f3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f3c0) · [`0045f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f3ec)

~~~diff
- 0045f414 ["INT_ADD", "register:40f0:8", ["const:45f414:8", "const:4:8"]]
- 0045f414 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045f454 ["INT_ADD", "register:40f0:8", ["const:45f454:8", "const:4:8"]]
+ 0045f454 ["CALL", null, ["callee:00c57eb0:8"]]
- 0045f414 bytes a7e11f94
+ 0045f454 bytes 97e21f94
- 0045f380 ["INT_ADD", "register:40f0:8", ["const:45f380:8", "const:4:8"]]
- 0045f380 ["CALL", null, ["callee:0044108c:8"]]
+ 0045f3c0 ["INT_ADD", "register:40f0:8", ["const:45f3c0:8", "const:4:8"]]
+ 0045f3c0 ["CALL", null, ["callee:0044108c:8"]]
- 0045f380 bytes 3387ff97
+ 0045f3c0 bytes 3387ff97
- 0045f3ac ["INT_ADD", "register:40f0:8", ["const:45f3ac:8", "const:4:8"]]
- 0045f3ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 0045f3ec ["INT_ADD", "register:40f0:8", ["const:45f3ec:8", "const:4:8"]]
+ 0045f3ec ["CALL", null, ["callee:00c57eb0:8"]]
- 0045f3ac bytes c1e11f94
+ 0045f3ec bytes b1e21f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a682cbf1575df89ae5a46f83d16113e6"></a>

### [`0045f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f5ec.md) → [`0045f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f62c.md) FUN_0045f62c

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
      "definition_site": "0045f638",
      "incomplete_value": false,
      "site": "0045f644",
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
    "old": {
      "definition_site": "0045f5f8",
      "incomplete_value": false,
      "site": "0045f604",
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
            "const:b98:8"
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
      "0045f644",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f644",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f5ec.md#insn-0045f5f8)
- 新版 [`0045f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f62c.md#insn-0045f638)

~~~diff
- 0045f5f8 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0045f5f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f5f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f5f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f638 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0045f638 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f638 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f638 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f5f8 bytes 4a612e91
+ 0045f638 bytes 4a613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b98c7647d780f63605f7424a9d7d1bf"></a>

### [`0045f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md) → [`0045f670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md) FUN_0045f670

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
      "definition_site": "0045f688",
      "incomplete_value": false,
      "site": "0045f694",
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
    "old": {
      "definition_site": "0045f648",
      "incomplete_value": false,
      "site": "0045f654",
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
            "const:b98:8"
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
      "0045f694",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f694",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md#insn-0045f648) · [`0045f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f630.md#insn-0045f678)
- 新版 [`0045f688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md#insn-0045f688) · [`0045f6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md#insn-0045f6b8)

~~~diff
- 0045f648 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0045f648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f688 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0045f688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f648 bytes 08612e91
+ 0045f688 bytes 08613e91
- 0045f678 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f678 ["INT_ADD", "register:40f0:8", ["const:45f678:8", "const:4:8"]]
- 0045f678 ["CALLIND", null, ["register:0:8"]]
+ 0045f6b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f6b8 ["INT_ADD", "register:40f0:8", ["const:45f6b8:8", "const:4:8"]]
+ 0045f6b8 ["CALLIND", null, ["register:0:8"]]
- 0045f678 bytes 00013fd6
+ 0045f6b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4765a3fe5eb172253e59a5417a1cf3"></a>

### [`0045f68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md) → [`0045f6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md) FUN_0045f6cc

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
      "definition_site": "0045f6f8",
      "incomplete_value": false,
      "site": "0045f6f8",
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
    "old": {
      "definition_site": "0045f6b8",
      "incomplete_value": false,
      "site": "0045f6b8",
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
            "const:b98:8"
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
      "0045f6f8",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f6f8",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6a0) · [`0045f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6b0) · [`0045f6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f68c.md#insn-0045f6d4)
- 新版 [`0045f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f6e0) · [`0045f6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f6f0) · [`0045f714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f714)

~~~diff
- 0045f6a0 ["INT_ADD", "register:40f0:8", ["const:45f6a0:8", "const:4:8"]]
- 0045f6a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045f6e0 ["INT_ADD", "register:40f0:8", ["const:45f6e0:8", "const:4:8"]]
+ 0045f6e0 ["CALL", null, ["callee:00c57e90:8"]]
- 0045f6a0 bytes fce01f94
+ 0045f6e0 bytes ece11f94
- 0045f6b0 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0045f6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f6f0 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0045f6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f6b0 bytes 08612e91
+ 0045f6f0 bytes 08613e91
- 0045f6d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f6d4 ["INT_ADD", "register:40f0:8", ["const:45f6d4:8", "const:4:8"]]
- 0045f6d4 ["CALLIND", null, ["register:0:8"]]
+ 0045f714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f714 ["INT_ADD", "register:40f0:8", ["const:45f714:8", "const:4:8"]]
+ 0045f714 ["CALLIND", null, ["register:0:8"]]
- 0045f6d4 bytes 00013fd6
+ 0045f714 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdcc420269c1602c2e66c6af12d7550f"></a>

### [`0045f714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md) → [`0045f754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md) FUN_0045f754

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
      "definition_site": "0045f770",
      "incomplete_value": false,
      "site": "0045f770",
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
    "old": {
      "definition_site": "0045f730",
      "incomplete_value": false,
      "site": "0045f730",
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
            "const:b98:8"
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
      "0045f770",
      "DATA",
      [
        "storage",
        "00c63b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f770",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md#insn-0045f72c) · [`0045f750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f714.md#insn-0045f750)
- 新版 [`0045f76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md#insn-0045f76c) · [`0045f790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md#insn-0045f790)

~~~diff
- 0045f72c ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0045f72c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f72c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f72c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f76c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0045f76c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f76c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f76c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f72c bytes 29612e91
+ 0045f76c bytes 29613e91
- 0045f750 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045f750 ["INT_ADD", "register:40f0:8", ["const:45f750:8", "const:4:8"]]
- 0045f750 ["CALLIND", null, ["register:0:8"]]
+ 0045f790 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045f790 ["INT_ADD", "register:40f0:8", ["const:45f790:8", "const:4:8"]]
+ 0045f790 ["CALLIND", null, ["register:0:8"]]
- 0045f750 bytes 20013fd6
+ 0045f790 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce1cdd7008855b6844b082932884a9f"></a>

### [`0045f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md) → [`0045f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md) FUN_0045f900

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0045f914",
      "incomplete_value": false,
      "site": "0045f918",
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
      "definition_site": "0045f8d4",
      "incomplete_value": false,
      "site": "0045f8d8",
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
      "0045f918",
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
      "0045f918",
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

- 旧版 [`0045f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8d0) · [`0045f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8d4) · [`0045f8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f8c0.md#insn-0045f8e8)
- 新版 [`0045f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f910) · [`0045f914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f914) · [`0045f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f928)

~~~diff
- 0045f8d0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f910 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f8d0 bytes 28400090
+ 0045f910 bytes 284000b0
- 0045f8d4 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0045f8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f914 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0045f914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f8d4 bytes 08613091
+ 0045f914 bytes 08610091
- 0045f8e8 ["INT_ADD", "register:40f0:8", ["const:45f8e8:8", "const:4:8"]]
- 0045f8e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0045f928 ["INT_ADD", "register:40f0:8", ["const:45f928:8", "const:4:8"]]
+ 0045f928 ["CALL", null, ["callee:00c53d00:8"]]
- 0045f8e8 bytes fecf1f94
+ 0045f928 bytes f6d01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70159f9e7a495fa5fae5c2cba8f723c2"></a>

### [`0045f91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md) → [`0045f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md) FUN_0045f95c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0045f974",
      "incomplete_value": false,
      "site": "0045f978",
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
      "definition_site": "0045f934",
      "incomplete_value": false,
      "site": "0045f938",
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
      "0045f978",
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
      "0045f978",
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

- 旧版 [`0045f930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f930) · [`0045f934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f934) · [`0045f948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f91c.md#insn-0045f948)
- 新版 [`0045f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f970) · [`0045f974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f974) · [`0045f988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f988)

~~~diff
- 0045f930 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f970 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f930 bytes 28400090
+ 0045f970 bytes 284000b0
- 0045f934 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0045f934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f974 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0045f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f934 bytes 08613091
+ 0045f974 bytes 08610091
- 0045f948 ["INT_ADD", "register:40f0:8", ["const:45f948:8", "const:4:8"]]
- 0045f948 ["CALL", null, ["callee:00c53d00:8"]]
+ 0045f988 ["INT_ADD", "register:40f0:8", ["const:45f988:8", "const:4:8"]]
+ 0045f988 ["CALL", null, ["callee:00c53d00:8"]]
- 0045f948 bytes e6cf1f94
+ 0045f988 bytes ded01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a15698b6ca8152c327be99e5a9876cd"></a>

### [`0045f978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md) → [`0045f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md) FUN_0045f9b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0045f9dc",
      "incomplete_value": false,
      "site": "0045f9dc",
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
      "definition_site": "0045f99c",
      "incomplete_value": false,
      "site": "0045f99c",
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
      "0045f9dc",
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
      "0045f9dc",
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

- 旧版 [`0045f98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f98c) · [`0045f994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f994) · [`0045f998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f978.md#insn-0045f998)
- 新版 [`0045f9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9cc) · [`0045f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9d4) · [`0045f9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9d8)

~~~diff
- 0045f98c ["INT_ADD", "register:40f0:8", ["const:45f98c:8", "const:4:8"]]
- 0045f98c ["CALL", null, ["callee:00c57e90:8"]]
+ 0045f9cc ["INT_ADD", "register:40f0:8", ["const:45f9cc:8", "const:4:8"]]
+ 0045f9cc ["CALL", null, ["callee:00c57e90:8"]]
- 0045f98c bytes 41e01f94
+ 0045f9cc bytes 31e11f94
- 0045f994 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045f9d4 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045f994 bytes 29400090
+ 0045f9d4 bytes 294000b0
- 0045f998 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0045f998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d8 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0045f9d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f9d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f998 bytes 29613091
+ 0045f9d8 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3369464c6ce94c12d47b8ce69f42667"></a>

### [`0045f9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md) → [`0045fa08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md) FUN_0045fa08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0045fa14",
      "incomplete_value": false,
      "site": "0045fa14",
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
      "definition_site": "0045f9d4",
      "incomplete_value": false,
      "site": "0045f9d4",
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
      "0045fa14",
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
      "0045fa14",
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

- 旧版 [`0045f9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9cc) · [`0045f9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9d0) · [`0045f9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045f9c8.md#insn-0045f9f0)
- 新版 [`0045fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md#insn-0045fa0c) · [`0045fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md#insn-0045fa10) · [`0045fa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md#insn-0045fa30)

~~~diff
- 0045f9cc ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045fa0c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045f9cc bytes 29400090
+ 0045fa0c bytes 294000b0
- 0045f9d0 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0045f9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fa10 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0045fa10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f9d0 bytes 29613091
+ 0045fa10 bytes 29610091
- 0045f9f0 ["INT_ADD", "register:40f0:8", ["const:45f9f0:8", "const:4:8"]]
- 0045f9f0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0045fa30 ["INT_ADD", "register:40f0:8", ["const:45fa30:8", "const:4:8"]]
+ 0045fa30 ["CALL", null, ["callee:00c53cd0:8"]]
- 0045f9f0 bytes b0cf1f94
+ 0045fa30 bytes a8d01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56336e7c9cff6ebe0d04bd6e802a59f5"></a>

### [`0045fb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md) → [`0045fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fb9c.md) FUN_0045fb9c

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
      "definition_site": "0045fba8",
      "incomplete_value": false,
      "site": "0045fbb4",
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
    "old": {
      "definition_site": "0045fb68",
      "incomplete_value": false,
      "site": "0045fb74",
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
            "const:c98:8"
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
      "0045fbb4",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fbb4",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md#insn-0045fb64) · [`0045fb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fb5c.md#insn-0045fb68)
- 新版 [`0045fba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fb9c.md#insn-0045fba4) · [`0045fba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fb9c.md#insn-0045fba8)

~~~diff
- 0045fb64 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045fba4 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045fb64 bytes 2a400090
+ 0045fba4 bytes 2a4000b0
- 0045fb68 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0045fb68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fb68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fb68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fba8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0045fba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fb68 bytes 4a613291
+ 0045fba8 bytes 4a610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65d63465d28bf68bd4d6afa86121e86"></a>

### [`0045fba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md) → [`0045fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md) FUN_0045fbe0

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
      "definition_site": "0045fbf8",
      "incomplete_value": false,
      "site": "0045fc04",
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
    "old": {
      "definition_site": "0045fbb8",
      "incomplete_value": false,
      "site": "0045fbc4",
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
            "const:c98:8"
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
      "0045fc04",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fc04",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbb4) · [`0045fbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbb8) · [`0045fbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fba0.md#insn-0045fbe8)
- 新版 [`0045fbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md#insn-0045fbf4) · [`0045fbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md#insn-0045fbf8) · [`0045fc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md#insn-0045fc28)

~~~diff
- 0045fbb4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045fbf4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045fbb4 bytes 28400090
+ 0045fbf4 bytes 284000b0
- 0045fbb8 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0045fbb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fbb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fbb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fbf8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0045fbf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fbf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fbf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fbb8 bytes 08613291
+ 0045fbf8 bytes 08610291
- 0045fbe8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fbe8 ["INT_ADD", "register:40f0:8", ["const:45fbe8:8", "const:4:8"]]
- 0045fbe8 ["CALLIND", null, ["register:0:8"]]
+ 0045fc28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fc28 ["INT_ADD", "register:40f0:8", ["const:45fc28:8", "const:4:8"]]
+ 0045fc28 ["CALLIND", null, ["register:0:8"]]
- 0045fbe8 bytes 00013fd6
+ 0045fc28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9dcc10829ea8614c810b67d0e312c6"></a>

### [`0045fbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md) → [`0045fc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md) FUN_0045fc3c

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
      "definition_site": "0045fc68",
      "incomplete_value": false,
      "site": "0045fc68",
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
    "old": {
      "definition_site": "0045fc28",
      "incomplete_value": false,
      "site": "0045fc28",
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
            "const:c98:8"
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
      "0045fc68",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fc68",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc10) · [`0045fc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc1c) · [`0045fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fbfc.md#insn-0045fc20)
- 新版 [`0045fc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc50) · [`0045fc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc5c) · [`0045fc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc60)

~~~diff
- 0045fc10 ["INT_ADD", "register:40f0:8", ["const:45fc10:8", "const:4:8"]]
- 0045fc10 ["CALL", null, ["callee:00c57e90:8"]]
+ 0045fc50 ["INT_ADD", "register:40f0:8", ["const:45fc50:8", "const:4:8"]]
+ 0045fc50 ["CALL", null, ["callee:00c57e90:8"]]
- 0045fc10 bytes a0df1f94
+ 0045fc50 bytes 90e01f94
- 0045fc1c ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045fc5c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045fc1c bytes 28400090
+ 0045fc5c bytes 284000b0
- 0045fc20 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0045fc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fc60 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0045fc60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fc20 bytes 08613291
+ 0045fc60 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814b840e34ee676bf860344f151c6899"></a>

### [`0045fc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md) → [`0045fcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md) FUN_0045fcc4

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
      "definition_site": "0045fce0",
      "incomplete_value": false,
      "site": "0045fce0",
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
    "old": {
      "definition_site": "0045fca0",
      "incomplete_value": false,
      "site": "0045fca0",
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
            "const:c98:8"
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
      "0045fce0",
      "DATA",
      [
        "storage",
        "00c63c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fce0",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fc98) · [`0045fc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fc9c) · [`0045fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fc84.md#insn-0045fcc0)
- 新版 [`0045fcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md#insn-0045fcd8) · [`0045fcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md#insn-0045fcdc) · [`0045fd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md#insn-0045fd00)

~~~diff
- 0045fc98 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045fcd8 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045fc98 bytes 29400090
+ 0045fcd8 bytes 294000b0
- 0045fc9c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0045fc9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fc9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fc9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fcdc ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0045fcdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fcdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fcdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fc9c bytes 29613291
+ 0045fcdc bytes 29610291
- 0045fcc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045fcc0 ["INT_ADD", "register:40f0:8", ["const:45fcc0:8", "const:4:8"]]
- 0045fcc0 ["CALLIND", null, ["register:0:8"]]
+ 0045fd00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045fd00 ["INT_ADD", "register:40f0:8", ["const:45fd00:8", "const:4:8"]]
+ 0045fd00 ["CALLIND", null, ["register:0:8"]]
- 0045fcc0 bytes 20013fd6
+ 0045fd00 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a32d39e8c8e1d2841466fbd17a62004"></a>

### [`0045fdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md) → [`0045fe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe08.md) FUN_0045fe08

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
      "definition_site": "0045fe14",
      "incomplete_value": false,
      "site": "0045fe20",
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
    "old": {
      "definition_site": "0045fdd4",
      "incomplete_value": false,
      "site": "0045fde0",
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
            "const:d18:8"
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
      "0045fe20",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fe20",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md#insn-0045fdd0) · [`0045fdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fdc8.md#insn-0045fdd4)
- 新版 [`0045fe10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe08.md#insn-0045fe10) · [`0045fe14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe08.md#insn-0045fe14)

~~~diff
- 0045fdd0 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045fe10 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045fdd0 bytes 2a400090
+ 0045fe10 bytes 2a4000b0
- 0045fdd4 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0045fdd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fdd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fdd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fe14 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0045fe14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fe14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fe14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fdd4 bytes 4a613491
+ 0045fe14 bytes 4a610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c8c1a6575211b08c2f4afa536c76c3"></a>

### [`0045fe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md) → [`0045fe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md) FUN_0045fe4c

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
      "definition_site": "0045fe64",
      "incomplete_value": false,
      "site": "0045fe70",
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
    "old": {
      "definition_site": "0045fe24",
      "incomplete_value": false,
      "site": "0045fe30",
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
            "const:d18:8"
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
      "0045fe70",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fe70",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe20) · [`0045fe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe24) · [`0045fe54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe0c.md#insn-0045fe54)
- 新版 [`0045fe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md#insn-0045fe60) · [`0045fe64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md#insn-0045fe64) · [`0045fe94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md#insn-0045fe94)

~~~diff
- 0045fe20 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045fe60 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045fe20 bytes 28400090
+ 0045fe60 bytes 284000b0
- 0045fe24 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0045fe24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fe64 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0045fe64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fe64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fe24 bytes 08613491
+ 0045fe64 bytes 08610491
- 0045fe54 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fe54 ["INT_ADD", "register:40f0:8", ["const:45fe54:8", "const:4:8"]]
- 0045fe54 ["CALLIND", null, ["register:0:8"]]
+ 0045fe94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fe94 ["INT_ADD", "register:40f0:8", ["const:45fe94:8", "const:4:8"]]
+ 0045fe94 ["CALLIND", null, ["register:0:8"]]
- 0045fe54 bytes 00013fd6
+ 0045fe94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3701c1f8302f57473ea8b4f71d1eb51f"></a>

### [`0045fe68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md) → [`0045fea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md) FUN_0045fea8

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
      "definition_site": "0045fed4",
      "incomplete_value": false,
      "site": "0045fed4",
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
    "old": {
      "definition_site": "0045fe94",
      "incomplete_value": false,
      "site": "0045fe94",
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
            "const:d18:8"
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
      "0045fed4",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fed4",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe7c) · [`0045fe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe88) · [`0045fe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fe68.md#insn-0045fe8c)
- 新版 [`0045febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045febc) · [`0045fec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045fec8) · [`0045fecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045fecc)

~~~diff
- 0045fe7c ["INT_ADD", "register:40f0:8", ["const:45fe7c:8", "const:4:8"]]
- 0045fe7c ["CALL", null, ["callee:00c57e90:8"]]
+ 0045febc ["INT_ADD", "register:40f0:8", ["const:45febc:8", "const:4:8"]]
+ 0045febc ["CALL", null, ["callee:00c57e90:8"]]
- 0045fe7c bytes 05df1f94
+ 0045febc bytes f5df1f94
- 0045fe88 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045fec8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045fe88 bytes 28400090
+ 0045fec8 bytes 284000b0
- 0045fe8c ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0045fe8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fecc ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0045fecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fe8c bytes 08613491
+ 0045fecc bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4e1234ee2f158c517e6e9acae11a63"></a>

### [`0045fef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md) → [`0045ff30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md) FUN_0045ff30

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
      "definition_site": "0045ff4c",
      "incomplete_value": false,
      "site": "0045ff4c",
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
    "old": {
      "definition_site": "0045ff0c",
      "incomplete_value": false,
      "site": "0045ff0c",
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
            "const:d18:8"
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
      "0045ff4c",
      "DATA",
      [
        "storage",
        "00c63d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff4c",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ff04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff04) · [`0045ff08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff08) · [`0045ff2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045f/0045fef0.md#insn-0045ff2c)
- 新版 [`0045ff44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md#insn-0045ff44) · [`0045ff48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md#insn-0045ff48) · [`0045ff6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md#insn-0045ff6c)

~~~diff
- 0045ff04 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045ff44 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045ff04 bytes 29400090
+ 0045ff44 bytes 294000b0
- 0045ff08 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0045ff08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ff48 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0045ff48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ff08 bytes 29613491
+ 0045ff48 bytes 29610491
- 0045ff2c ["COPY", "register:0:8", ["register:4048:8"]]
- 0045ff2c ["INT_ADD", "register:40f0:8", ["const:45ff2c:8", "const:4:8"]]
- 0045ff2c ["CALLIND", null, ["register:0:8"]]
+ 0045ff6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045ff6c ["INT_ADD", "register:40f0:8", ["const:45ff6c:8", "const:4:8"]]
+ 0045ff6c ["CALLIND", null, ["register:0:8"]]
- 0045ff2c bytes 20013fd6
+ 0045ff6c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f8ac95c93a47b9ab1f7303c906dfefa"></a>

### [`00460090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md) → [`004600d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md) FUN_004600d0

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
      "definition_site": "004600e4",
      "incomplete_value": false,
      "site": "004600e8",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004600a4",
      "incomplete_value": false,
      "site": "004600a8",
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
            "const:d98:8"
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
      "004600e8",
      "DATA",
      [
        "storage",
        "00c63d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004600e8",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046009c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-0046009c) · [`004600a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-004600a0) · [`004600a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460090.md#insn-004600a4)
- 新版 [`004600dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md#insn-004600dc) · [`004600e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md#insn-004600e0) · [`004600e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md#insn-004600e4)

~~~diff
- 0046009c ["INT_ADD", "register:40f0:8", ["const:46009c:8", "const:4:8"]]
- 0046009c ["CALL", null, ["callee:00c57e90:8"]]
+ 004600dc ["INT_ADD", "register:40f0:8", ["const:4600dc:8", "const:4:8"]]
+ 004600dc ["CALL", null, ["callee:00c57e90:8"]]
- 0046009c bytes 7dde1f94
+ 004600dc bytes 6ddf1f94
- 004600a0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004600e0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004600a0 bytes 084000f0
+ 004600e0 bytes 28400090
- 004600a4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 004600a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004600a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004600a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004600e4 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 004600e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004600e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004600e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004600a4 bytes 08613691
+ 004600e4 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23edec80f374677a986be9d022c20957"></a>

### [`004600b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md) → [`004600f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600f4.md) FUN_004600f4

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
      "definition_site": "004600f8",
      "incomplete_value": false,
      "site": "004600fc",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004600b8",
      "incomplete_value": false,
      "site": "004600bc",
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
      "004600fc",
      "DATA",
      [
        "storage",
        "00c63d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004600fc",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004600b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md#insn-004600b4) · [`004600b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600b4.md#insn-004600b8)
- 新版 [`004600f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600f4.md#insn-004600f4) · [`004600f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600f4.md#insn-004600f8)

~~~diff
- 004600b4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004600f4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004600b4 bytes 084000f0
+ 004600f4 bytes 28400090
- 004600b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 004600b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004600b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004600b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004600f8 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 004600f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004600f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004600f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004600b8 bytes 08613691
+ 004600f8 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-717e12b93a5adfc4d6da5b8185b48d21"></a>

### [`004600cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md) → [`0046010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md) FUN_0046010c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

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
      "definition_site": "00460238",
      "incomplete_value": true,
      "site": "00460238",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004601f8",
      "incomplete_value": true,
      "site": "004601f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004602d4",
      "incomplete_value": true,
      "site": "004602d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00460294",
      "incomplete_value": true,
      "site": "00460294",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004602c4",
      "incomplete_value": true,
      "site": "004602d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00460284",
      "incomplete_value": true,
      "site": "00460294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00460228",
      "READ",
      [
        "storage",
        "002b5e4f",
        null,
        "string"
      ]
    ],
    [
      "00460270",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046027c",
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
      "00460228",
      "READ",
      [
        "storage",
        "002b5e8f",
        null,
        "string"
      ]
    ],
    [
      "00460270",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046027c",
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

- 旧版 [`00460294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-00460294) · [`00460310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-00460310) · [`004603bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md#insn-004603bc)
- 新版 [`004602d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-004602d4) · [`00460350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-00460350) · [`004603fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-004603fc)

~~~diff
- 00460294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460294 ["INT_ADD", "register:40f0:8", ["const:460294:8", "const:4:8"]]
- 00460294 ["CALLIND", null, ["register:0:8"]]
+ 004602d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004602d4 ["INT_ADD", "register:40f0:8", ["const:4602d4:8", "const:4:8"]]
+ 004602d4 ["CALLIND", null, ["register:0:8"]]
- 00460294 bytes 00013fd6
+ 004602d4 bytes 00013fd6
- 00460310 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460310 ["INT_ADD", "register:40f0:8", ["const:460310:8", "const:4:8"]]
- 00460310 ["CALLIND", null, ["register:0:8"]]
+ 00460350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460350 ["INT_ADD", "register:40f0:8", ["const:460350:8", "const:4:8"]]
+ 00460350 ["CALLIND", null, ["register:0:8"]]
- 00460310 bytes 00013fd6
+ 00460350 bytes 00013fd6
- 004603bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004603bc ["INT_ADD", "register:40f0:8", ["const:4603bc:8", "const:4:8"]]
- 004603bc ["CALLIND", null, ["register:0:8"]]
+ 004603fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004603fc ["INT_ADD", "register:40f0:8", ["const:4603fc:8", "const:4:8"]]
+ 004603fc ["CALLIND", null, ["register:0:8"]]
- 004603bc bytes 00013fd6
+ 004603fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1bc6d5e0f6e54d9383df3281cc92e1"></a>

### [`0046052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md) → [`0046056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046056c.md) FUN_0046056c

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
      "definition_site": "00460578",
      "incomplete_value": false,
      "site": "00460584",
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
      "definition_site": "00460538",
      "incomplete_value": false,
      "site": "00460544",
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
      "00460584",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460584",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md#insn-00460534) · [`00460538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/0046052c.md#insn-00460538)
- 新版 [`00460574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046056c.md#insn-00460574) · [`00460578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046056c.md#insn-00460578)

~~~diff
- 00460534 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 00460574 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00460534 bytes 0a4000f0
+ 00460574 bytes 2a400090
- 00460538 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00460538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00460538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00460538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00460578 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00460578 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00460578 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00460578 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00460538 bytes 4a613891
+ 00460578 bytes 4a610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e50d7934c9b052df1a3e4bc90afb5af"></a>

### [`00460570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md) → [`004605b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md) FUN_004605b0

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
      "definition_site": "004605c8",
      "incomplete_value": false,
      "site": "004605d4",
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
      "definition_site": "00460588",
      "incomplete_value": false,
      "site": "00460594",
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
      "004605d4",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004605d4",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-00460584) · [`00460588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-00460588) · [`004605b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460570.md#insn-004605b8)
- 新版 [`004605c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md#insn-004605c4) · [`004605c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md#insn-004605c8) · [`004605f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md#insn-004605f8)

~~~diff
- 00460584 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004605c4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00460584 bytes 084000f0
+ 004605c4 bytes 28400090
- 00460588 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00460588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004605c8 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 004605c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004605c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004605c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460588 bytes 08613891
+ 004605c8 bytes 08610891
- 004605b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004605b8 ["INT_ADD", "register:40f0:8", ["const:4605b8:8", "const:4:8"]]
- 004605b8 ["CALLIND", null, ["register:0:8"]]
+ 004605f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004605f8 ["INT_ADD", "register:40f0:8", ["const:4605f8:8", "const:4:8"]]
+ 004605f8 ["CALLIND", null, ["register:0:8"]]
- 004605b8 bytes 00013fd6
+ 004605f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ab121634c902a95450953002ec93084"></a>

### [`004605cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md) → [`0046060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md) FUN_0046060c

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
      "definition_site": "00460638",
      "incomplete_value": false,
      "site": "00460638",
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
      "definition_site": "004605f8",
      "incomplete_value": false,
      "site": "004605f8",
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
      "00460638",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460638",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004605e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605e0) · [`004605ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605ec) · [`004605f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004605cc.md#insn-004605f0)
- 新版 [`00460620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-00460620) · [`0046062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-0046062c) · [`00460630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-00460630)

~~~diff
- 004605e0 ["INT_ADD", "register:40f0:8", ["const:4605e0:8", "const:4:8"]]
- 004605e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00460620 ["INT_ADD", "register:40f0:8", ["const:460620:8", "const:4:8"]]
+ 00460620 ["CALL", null, ["callee:00c57e90:8"]]
- 004605e0 bytes 2cdd1f94
+ 00460620 bytes 1cde1f94
- 004605ec ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0046062c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004605ec bytes 084000f0
+ 0046062c bytes 28400090
- 004605f0 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 004605f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004605f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004605f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460630 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00460630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004605f0 bytes 08613891
+ 00460630 bytes 08610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8fea99f88cf3038521c77343fec1c74"></a>

### [`00460654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md) → [`00460694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md) FUN_00460694

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
      "definition_site": "004606b0",
      "incomplete_value": false,
      "site": "004606b0",
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
      "definition_site": "00460670",
      "incomplete_value": false,
      "site": "00460670",
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
      "004606b0",
      "DATA",
      [
        "storage",
        "00c63e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004606b0",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-00460668) · [`0046066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-0046066c) · [`00460690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460654.md#insn-00460690)
- 新版 [`004606a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md#insn-004606a8) · [`004606ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md#insn-004606ac) · [`004606d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md#insn-004606d0)

~~~diff
- 00460668 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 004606a8 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00460668 bytes 094000f0
+ 004606a8 bytes 29400090
- 0046066c ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0046066c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046066c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046066c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004606ac ["COPY", "tmp:0:8", ["const:218:8"]]
+ 004606ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004606ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004606ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046066c bytes 29613891
+ 004606ac bytes 29610891
- 00460690 ["COPY", "register:0:8", ["register:4048:8"]]
- 00460690 ["INT_ADD", "register:40f0:8", ["const:460690:8", "const:4:8"]]
- 00460690 ["CALLIND", null, ["register:0:8"]]
+ 004606d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004606d0 ["INT_ADD", "register:40f0:8", ["const:4606d0:8", "const:4:8"]]
+ 004606d0 ["CALLIND", null, ["register:0:8"]]
- 00460690 bytes 20013fd6
+ 004606d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11114f76d5c97b05073b47ad03fa8aee"></a>

### [`00460750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md) → [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) FUN_00460790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`00461690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461690.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md)

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
      "definition_site": "00460918",
      "incomplete_value": true,
      "site": "00460924",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:971:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004608d8",
      "incomplete_value": true,
      "site": "004608e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:931:8"
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
      "definition_site": "00460a84",
      "incomplete_value": true,
      "site": "00460a94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460a44",
      "incomplete_value": true,
      "site": "00460a54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:178:8"
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
      "definition_site": "00460a98",
      "incomplete_value": true,
      "site": "00460a98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00460a58",
      "incomplete_value": true,
      "site": "00460a58",
      "value": [
        "LOAD",
        "8",
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
      "00460918",
      "READ",
      [
        "storage",
        "002b2931",
        null,
        "string"
      ]
    ],
    [
      "00460a84",
      "READ",
      [
        "storage",
        "002b7178",
        null,
        "string"
      ]
    ],
    [
      "00460a8c",
      "READ",
      [
        "storage",
        "002b717d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00460918",
      "READ",
      [
        "storage",
        "002b2971",
        null,
        "string"
      ]
    ],
    [
      "00460a84",
      "READ",
      [
        "storage",
        "002b71b8",
        null,
        "string"
      ]
    ],
    [
      "00460a8c",
      "READ",
      [
        "storage",
        "002b71bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-00460b9c) · [`00460cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-00460cf0) · [`004607b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/00460750.md#insn-004607b8)
- 新版 [`00460bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-00460bdc) · [`00460d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-00460d30) · [`004607f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-004607f8)

~~~diff
- 00460b9c ["INT_ADD", "register:40f0:8", ["const:460b9c:8", "const:4:8"]]
- 00460b9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00460bdc ["INT_ADD", "register:40f0:8", ["const:460bdc:8", "const:4:8"]]
+ 00460bdc ["CALL", null, ["callee:00c57eb0:8"]]
- 00460b9c bytes c5db1f94
+ 00460bdc bytes b5dc1f94
- 00460cf0 ["INT_ADD", "register:40f0:8", ["const:460cf0:8", "const:4:8"]]
- 00460cf0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00460d30 ["INT_ADD", "register:40f0:8", ["const:460d30:8", "const:4:8"]]
+ 00460d30 ["CALL", null, ["callee:00c57eb0:8"]]
- 00460cf0 bytes 70db1f94
+ 00460d30 bytes 60dc1f94
- 004607b8 ["INT_ADD", "register:40f0:8", ["const:4607b8:8", "const:4:8"]]
- 004607b8 ["CALL", null, ["callee:0044108c:8"]]
+ 004607f8 ["INT_ADD", "register:40f0:8", ["const:4607f8:8", "const:4:8"]]
+ 004607f8 ["CALL", null, ["callee:0044108c:8"]]
- 004607b8 bytes 2582ff97
+ 004607f8 bytes 2582ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8deee0a538e05fdd2abc3fa5c649c88e"></a>

### [`00461620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md) → [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) FUN_00461660

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`00461d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461d88.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0046166c",
      "incomplete_value": false,
      "site": "00461670",
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
      "definition_site": "0046162c",
      "incomplete_value": false,
      "site": "00461630",
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
      "0046166c",
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
      "0046166c",
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

- 旧版 [`00461630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md#insn-00461630) · [`0046162c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461620.md#insn-0046162c)
- 新版 [`00461670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md#insn-00461670) · [`0046166c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md#insn-0046166c)

~~~diff
- 00461630 ["INT_ADD", "register:40f0:8", ["const:461630:8", "const:4:8"]]
- 00461630 ["CALL", null, ["callee:0043b778:8"]]
+ 00461670 ["INT_ADD", "register:40f0:8", ["const:461670:8", "const:4:8"]]
+ 00461670 ["CALL", null, ["callee:0043b778:8"]]
- 00461630 bytes 4268ff97
+ 00461670 bytes 4268ff97
- 0046162c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0046162c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046162c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046162c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046166c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0046166c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046166c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046166c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046162c bytes 00303c91
+ 0046166c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54e9d9c46361bf08fa21eb29ca7c11ef"></a>

### [`004619d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md) → [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) FUN_00461a18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) [`00461af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md) [`009bf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) [`00461b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md) [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00461a24",
      "incomplete_value": false,
      "site": "00461a28",
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
      "definition_site": "004619e4",
      "incomplete_value": false,
      "site": "004619e8",
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
      "00461a24",
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
      "00461a24",
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

- 旧版 [`004619e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md#insn-004619e8) · [`004619e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md#insn-004619e4)
- 新版 [`00461a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md#insn-00461a28) · [`00461a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md#insn-00461a24)

~~~diff
- 004619e8 ["INT_ADD", "register:40f0:8", ["const:4619e8:8", "const:4:8"]]
- 004619e8 ["CALL", null, ["callee:0043b778:8"]]
+ 00461a28 ["INT_ADD", "register:40f0:8", ["const:461a28:8", "const:4:8"]]
+ 00461a28 ["CALL", null, ["callee:0043b778:8"]]
- 004619e8 bytes 5467ff97
+ 00461a28 bytes 5467ff97
- 004619e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 004619e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004619e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004619e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00461a24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00461a24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00461a24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00461a24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004619e4 bytes 00303c91
+ 00461a24 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fff05983a17ea4bfc7b01dc1e6a390"></a>

### [`00461ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md) → [`00462030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462030.md) FUN_00462030

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
      "definition_site": "0046203c",
      "incomplete_value": false,
      "site": "00462048",
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
      "definition_site": "00461ffc",
      "incomplete_value": false,
      "site": "00462008",
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
      "00462048",
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
      "00462048",
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

- 旧版 [`00461ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md#insn-00461ff8) · [`00461ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461ff0.md#insn-00461ffc)
- 新版 [`00462038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462030.md#insn-00462038) · [`0046203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462030.md#insn-0046203c)

~~~diff
- 00461ff8 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 00462038 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00461ff8 bytes 0a4000d0
+ 00462038 bytes 0a4000d0
- 00461ffc ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00461ffc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00461ffc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00461ffc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046203c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0046203c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046203c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046203c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00461ffc bytes 4a613a91
+ 0046203c bytes 4a610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d5b2a620b8a7078e02c7a836723ee2"></a>

### [`00462034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md) → [`00462074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md) FUN_00462074

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
      "definition_site": "0046208c",
      "incomplete_value": false,
      "site": "00462098",
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
      "definition_site": "0046204c",
      "incomplete_value": false,
      "site": "00462058",
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
      "00462098",
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
      "00462098",
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

- 旧版 [`00462048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-00462048) · [`0046204c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-0046204c) · [`0046207c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462034.md#insn-0046207c)
- 新版 [`00462088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md#insn-00462088) · [`0046208c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md#insn-0046208c) · [`004620bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md#insn-004620bc)

~~~diff
- 00462048 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00462088 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00462048 bytes 084000b0
+ 00462088 bytes 084000d0
- 0046204c ["COPY", "tmp:0:8", ["const:e98:8"]]
- 0046204c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046204c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046204c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046208c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0046208c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046208c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046208c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046204c bytes 08613a91
+ 0046208c bytes 08610a91
- 0046207c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046207c ["INT_ADD", "register:40f0:8", ["const:46207c:8", "const:4:8"]]
- 0046207c ["CALLIND", null, ["register:0:8"]]
+ 004620bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004620bc ["INT_ADD", "register:40f0:8", ["const:4620bc:8", "const:4:8"]]
+ 004620bc ["CALLIND", null, ["register:0:8"]]
- 0046207c bytes 00013fd6
+ 004620bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dd3c970e64632db9fa31f9ad92a4967"></a>

### [`00462090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md) → [`004620d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md) FUN_004620d0

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
      "definition_site": "004620fc",
      "incomplete_value": false,
      "site": "004620fc",
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
      "definition_site": "004620bc",
      "incomplete_value": false,
      "site": "004620bc",
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
      "004620fc",
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
      "004620fc",
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

- 旧版 [`004620a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620a4) · [`004620b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620b0) · [`004620b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462090.md#insn-004620b4)
- 新版 [`004620e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-004620e4) · [`004620f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-004620f0) · [`004620f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-004620f4)

~~~diff
- 004620a4 ["INT_ADD", "register:40f0:8", ["const:4620a4:8", "const:4:8"]]
- 004620a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 004620e4 ["INT_ADD", "register:40f0:8", ["const:4620e4:8", "const:4:8"]]
+ 004620e4 ["CALL", null, ["callee:00c57e90:8"]]
- 004620a4 bytes 7bd61f94
+ 004620e4 bytes 6bd71f94
- 004620b0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004620f0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004620b0 bytes 084000b0
+ 004620f0 bytes 084000d0
- 004620b4 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 004620b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004620b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004620b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004620f4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 004620f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004620f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004620f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004620b4 bytes 08613a91
+ 004620f4 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ecf968142f68ff8a9592e47116cbb0"></a>

### [`00462118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md) → [`00462158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md) FUN_00462158

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
      "definition_site": "00462174",
      "incomplete_value": false,
      "site": "00462174",
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
      "definition_site": "00462134",
      "incomplete_value": false,
      "site": "00462134",
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
      "00462174",
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
      "00462174",
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

- 旧版 [`0046212c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-0046212c) · [`00462130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-00462130) · [`00462154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462118.md#insn-00462154)
- 新版 [`0046216c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md#insn-0046216c) · [`00462170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md#insn-00462170) · [`00462194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md#insn-00462194)

~~~diff
- 0046212c ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0046216c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0046212c bytes 094000b0
+ 0046216c bytes 094000d0
- 00462130 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00462130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462170 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00462170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462130 bytes 29613a91
+ 00462170 bytes 29610a91
- 00462154 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462154 ["INT_ADD", "register:40f0:8", ["const:462154:8", "const:4:8"]]
- 00462154 ["CALLIND", null, ["register:0:8"]]
+ 00462194 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462194 ["INT_ADD", "register:40f0:8", ["const:462194:8", "const:4:8"]]
+ 00462194 ["CALLIND", null, ["register:0:8"]]
- 00462154 bytes 20013fd6
+ 00462194 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ba7bd9521f4505ff0cbdaa00084d38"></a>

### [`00462380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md) → [`004623c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004623c0.md) FUN_004623c0

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
      "definition_site": "004623cc",
      "incomplete_value": false,
      "site": "004623d8",
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
      "definition_site": "0046238c",
      "incomplete_value": false,
      "site": "00462398",
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
      "004623d8",
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
      "004623d8",
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

- 旧版 [`00462388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md#insn-00462388) · [`0046238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462380.md#insn-0046238c)
- 新版 [`004623c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004623c0.md#insn-004623c8) · [`004623cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004623c0.md#insn-004623cc)

~~~diff
- 00462388 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 004623c8 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00462388 bytes 0a4000b0
+ 004623c8 bytes 0a4000d0
- 0046238c ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0046238c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046238c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046238c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004623cc ["COPY", "tmp:0:8", ["const:318:8"]]
+ 004623cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004623cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004623cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046238c bytes 4a613c91
+ 004623cc bytes 4a610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e2b7f5ec216a833f27266d657424000"></a>

### [`004623c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md) → [`00462404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md) FUN_00462404

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
      "definition_site": "0046241c",
      "incomplete_value": false,
      "site": "00462428",
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
      "definition_site": "004623dc",
      "incomplete_value": false,
      "site": "004623e8",
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
      "00462428",
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
      "00462428",
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

- 旧版 [`004623d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-004623d8) · [`004623dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-004623dc) · [`0046240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004623c4.md#insn-0046240c)
- 新版 [`00462418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md#insn-00462418) · [`0046241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md#insn-0046241c) · [`0046244c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md#insn-0046244c)

~~~diff
- 004623d8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00462418 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004623d8 bytes 084000b0
+ 00462418 bytes 084000d0
- 004623dc ["COPY", "tmp:0:8", ["const:f18:8"]]
- 004623dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004623dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004623dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046241c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0046241c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046241c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046241c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004623dc bytes 08613c91
+ 0046241c bytes 08610c91
- 0046240c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046240c ["INT_ADD", "register:40f0:8", ["const:46240c:8", "const:4:8"]]
- 0046240c ["CALLIND", null, ["register:0:8"]]
+ 0046244c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046244c ["INT_ADD", "register:40f0:8", ["const:46244c:8", "const:4:8"]]
+ 0046244c ["CALLIND", null, ["register:0:8"]]
- 0046240c bytes 00013fd6
+ 0046244c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bede671762522846d4026dde0e1be9c"></a>

### [`00462420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md) → [`00462460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md) FUN_00462460

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
      "definition_site": "0046248c",
      "incomplete_value": false,
      "site": "0046248c",
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
      "definition_site": "0046244c",
      "incomplete_value": false,
      "site": "0046244c",
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
      "0046248c",
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
      "0046248c",
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

- 旧版 [`00462434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462434) · [`00462440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462440) · [`00462444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462420.md#insn-00462444)
- 新版 [`00462474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-00462474) · [`00462480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-00462480) · [`00462484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-00462484)

~~~diff
- 00462434 ["INT_ADD", "register:40f0:8", ["const:462434:8", "const:4:8"]]
- 00462434 ["CALL", null, ["callee:00c57e90:8"]]
+ 00462474 ["INT_ADD", "register:40f0:8", ["const:462474:8", "const:4:8"]]
+ 00462474 ["CALL", null, ["callee:00c57e90:8"]]
- 00462434 bytes 97d51f94
+ 00462474 bytes 87d61f94
- 00462440 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00462480 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00462440 bytes 084000b0
+ 00462480 bytes 084000d0
- 00462444 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00462444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462484 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00462484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462444 bytes 08613c91
+ 00462484 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4dfd81d3bbd928e56c07f8c5e45946"></a>

### [`004624a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md) → [`004624e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md) FUN_004624e8

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
      "definition_site": "00462504",
      "incomplete_value": false,
      "site": "00462504",
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
      "definition_site": "004624c4",
      "incomplete_value": false,
      "site": "004624c4",
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
      "00462504",
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
      "00462504",
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

- 旧版 [`004624bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624bc) · [`004624c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624c0) · [`004624e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004624a8.md#insn-004624e4)
- 新版 [`004624fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md#insn-004624fc) · [`00462500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md#insn-00462500) · [`00462524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md#insn-00462524)

~~~diff
- 004624bc ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 004624fc ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004624bc bytes 094000b0
+ 004624fc bytes 094000d0
- 004624c0 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 004624c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004624c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004624c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462500 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00462500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004624c0 bytes 29613c91
+ 00462500 bytes 29610c91
- 004624e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004624e4 ["INT_ADD", "register:40f0:8", ["const:4624e4:8", "const:4:8"]]
- 004624e4 ["CALLIND", null, ["register:0:8"]]
+ 00462524 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462524 ["INT_ADD", "register:40f0:8", ["const:462524:8", "const:4:8"]]
+ 00462524 ["CALLIND", null, ["register:0:8"]]
- 004624e4 bytes 20013fd6
+ 00462524 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2f91e2afb6258c4fbd0f6d15dbfdd0b"></a>

### [`00462640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md) → [`00462680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462680.md) FUN_00462680

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
      "definition_site": "0046268c",
      "incomplete_value": false,
      "site": "00462698",
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
      "definition_site": "0046264c",
      "incomplete_value": false,
      "site": "00462658",
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
      "00462698",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462698",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md#insn-00462648) · [`0046264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462640.md#insn-0046264c)
- 新版 [`00462688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462680.md#insn-00462688) · [`0046268c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462680.md#insn-0046268c)

~~~diff
- 00462648 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 00462688 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 00462648 bytes 0a4000b0
+ 00462688 bytes 0a4000d0
- 0046264c ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0046264c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046264c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046264c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046268c ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0046268c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046268c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046268c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046264c bytes 4a613e91
+ 0046268c bytes 4a610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e125cafdd75dbaea773c6e7e15d5e63a"></a>

### [`00462684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md) → [`004626c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md) FUN_004626c4

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
      "definition_site": "004626dc",
      "incomplete_value": false,
      "site": "004626e8",
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
      "definition_site": "0046269c",
      "incomplete_value": false,
      "site": "004626a8",
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
      "004626e8",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004626e8",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-00462698) · [`0046269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-0046269c) · [`004626cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462684.md#insn-004626cc)
- 新版 [`004626d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md#insn-004626d8) · [`004626dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md#insn-004626dc) · [`0046270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md#insn-0046270c)

~~~diff
- 00462698 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004626d8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00462698 bytes 084000b0
+ 004626d8 bytes 084000d0
- 0046269c ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0046269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004626dc ["COPY", "tmp:0:8", ["const:398:8"]]
+ 004626dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004626dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004626dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046269c bytes 08613e91
+ 004626dc bytes 08610e91
- 004626cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004626cc ["INT_ADD", "register:40f0:8", ["const:4626cc:8", "const:4:8"]]
- 004626cc ["CALLIND", null, ["register:0:8"]]
+ 0046270c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046270c ["INT_ADD", "register:40f0:8", ["const:46270c:8", "const:4:8"]]
+ 0046270c ["CALLIND", null, ["register:0:8"]]
- 004626cc bytes 00013fd6
+ 0046270c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09bd29758a41eecd01a046bb3e8709df"></a>

### [`004626e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md) → [`00462720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md) FUN_00462720

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
      "definition_site": "0046274c",
      "incomplete_value": false,
      "site": "0046274c",
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
      "definition_site": "0046270c",
      "incomplete_value": false,
      "site": "0046270c",
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
      "0046274c",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046274c",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004626f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-004626f4) · [`00462700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-00462700) · [`00462704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004626e0.md#insn-00462704)
- 新版 [`00462734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462734) · [`00462740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462740) · [`00462744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462744)

~~~diff
- 004626f4 ["INT_ADD", "register:40f0:8", ["const:4626f4:8", "const:4:8"]]
- 004626f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00462734 ["INT_ADD", "register:40f0:8", ["const:462734:8", "const:4:8"]]
+ 00462734 ["CALL", null, ["callee:00c57e90:8"]]
- 004626f4 bytes e7d41f94
+ 00462734 bytes d7d51f94
- 00462700 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00462740 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00462700 bytes 084000b0
+ 00462740 bytes 084000d0
- 00462704 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00462704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462744 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00462744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462704 bytes 08613e91
+ 00462744 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac2747f3443489d89eec3dbf7bb5a8c2"></a>

### [`00462768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md) → [`004627a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md) FUN_004627a8

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
      "definition_site": "004627c4",
      "incomplete_value": false,
      "site": "004627c4",
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
      "definition_site": "00462784",
      "incomplete_value": false,
      "site": "00462784",
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
      "004627c4",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004627c4",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-0046277c) · [`00462780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-00462780) · [`004627a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462768.md#insn-004627a4)
- 新版 [`004627bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md#insn-004627bc) · [`004627c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md#insn-004627c0) · [`004627e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md#insn-004627e4)

~~~diff
- 0046277c ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 004627bc ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0046277c bytes 094000b0
+ 004627bc bytes 094000d0
- 00462780 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00462780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004627c0 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 004627c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004627c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004627c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462780 bytes 29613e91
+ 004627c0 bytes 29610e91
- 004627a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004627a4 ["INT_ADD", "register:40f0:8", ["const:4627a4:8", "const:4:8"]]
- 004627a4 ["CALLIND", null, ["register:0:8"]]
+ 004627e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004627e4 ["INT_ADD", "register:40f0:8", ["const:4627e4:8", "const:4:8"]]
+ 004627e4 ["CALLIND", null, ["register:0:8"]]
- 004627a4 bytes 20013fd6
+ 004627e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eebf8403e5b92afd38ce78172211b43c"></a>

### [`00462900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462900.md) → [`00462940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462940.md) FUN_00462940

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
      "definition_site": "0046294c",
      "incomplete_value": false,
      "site": "00462958",
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
      "definition_site": "0046290c",
      "incomplete_value": false,
      "site": "00462918",
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
      "00462958",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462958",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046290c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462900.md#insn-0046290c)
- 新版 [`0046294c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462940.md#insn-0046294c)

~~~diff
- 0046290c ["COPY", "tmp:0:8", ["const:18:8"]]
- 0046290c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046290c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046290c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046294c ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0046294c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046294c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046294c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046290c bytes 4a610091
+ 0046294c bytes 4a611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65203be7d5cb562bf9c0e33331c3c6fe"></a>

### [`00462944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md) → [`00462984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md) FUN_00462984

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
      "definition_site": "0046299c",
      "incomplete_value": false,
      "site": "004629a8",
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
      "definition_site": "0046295c",
      "incomplete_value": false,
      "site": "00462968",
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
      "004629a8",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004629a8",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md#insn-0046295c) · [`0046298c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462944.md#insn-0046298c)
- 新版 [`0046299c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md#insn-0046299c) · [`004629cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md#insn-004629cc)

~~~diff
- 0046295c ["COPY", "tmp:0:8", ["const:18:8"]]
- 0046295c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046295c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046295c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046299c ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0046299c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046299c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046299c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046295c bytes 08610091
+ 0046299c bytes 08611091
- 0046298c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046298c ["INT_ADD", "register:40f0:8", ["const:46298c:8", "const:4:8"]]
- 0046298c ["CALLIND", null, ["register:0:8"]]
+ 004629cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004629cc ["INT_ADD", "register:40f0:8", ["const:4629cc:8", "const:4:8"]]
+ 004629cc ["CALLIND", null, ["register:0:8"]]
- 0046298c bytes 00013fd6
+ 004629cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4793e73fc11f46e5921024056c2c13ab"></a>

### [`004629a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md) → [`004629e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md) FUN_004629e0

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
      "definition_site": "00462a0c",
      "incomplete_value": false,
      "site": "00462a0c",
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
      "definition_site": "004629cc",
      "incomplete_value": false,
      "site": "004629cc",
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
      "00462a0c",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462a0c",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004629b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629b4) · [`004629c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629c4) · [`004629e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/004629a0.md#insn-004629e8)
- 新版 [`004629f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-004629f4) · [`00462a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-00462a04) · [`00462a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-00462a28)

~~~diff
- 004629b4 ["INT_ADD", "register:40f0:8", ["const:4629b4:8", "const:4:8"]]
- 004629b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 004629f4 ["INT_ADD", "register:40f0:8", ["const:4629f4:8", "const:4:8"]]
+ 004629f4 ["CALL", null, ["callee:00c57e90:8"]]
- 004629b4 bytes 37d41f94
+ 004629f4 bytes 27d51f94
- 004629c4 ["COPY", "tmp:0:8", ["const:18:8"]]
- 004629c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004629c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004629c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462a04 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00462a04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004629c4 bytes 08610091
+ 00462a04 bytes 08611091
- 004629e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004629e8 ["INT_ADD", "register:40f0:8", ["const:4629e8:8", "const:4:8"]]
- 004629e8 ["CALLIND", null, ["register:0:8"]]
+ 00462a28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462a28 ["INT_ADD", "register:40f0:8", ["const:462a28:8", "const:4:8"]]
+ 00462a28 ["CALLIND", null, ["register:0:8"]]
- 004629e8 bytes 00013fd6
+ 00462a28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce9b9d4219e9423b53d86a6ae636fbf"></a>

### [`00462a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md) → [`00462a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md) FUN_00462a68

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
      "definition_site": "00462a84",
      "incomplete_value": false,
      "site": "00462a84",
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
      "definition_site": "00462a44",
      "incomplete_value": false,
      "site": "00462a44",
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
      "00462a84",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462a84",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md#insn-00462a40) · [`00462a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462a28.md#insn-00462a64)
- 新版 [`00462a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md#insn-00462a80) · [`00462aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md#insn-00462aa4)

~~~diff
- 00462a40 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00462a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462a80 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00462a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462a40 bytes 29610091
+ 00462a80 bytes 29611091
- 00462a64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462a64 ["INT_ADD", "register:40f0:8", ["const:462a64:8", "const:4:8"]]
- 00462a64 ["CALLIND", null, ["register:0:8"]]
+ 00462aa4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462aa4 ["INT_ADD", "register:40f0:8", ["const:462aa4:8", "const:4:8"]]
+ 00462aa4 ["CALLIND", null, ["register:0:8"]]
- 00462a64 bytes 20013fd6
+ 00462aa4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2360d53cfe334f7fdd0031976ea3b9a2"></a>

### [`00462d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462d7c.md) → [`00462dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462dbc.md) FUN_00462dbc

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
      "definition_site": "00462dc8",
      "incomplete_value": false,
      "site": "00462dd4",
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
      "definition_site": "00462d88",
      "incomplete_value": false,
      "site": "00462d94",
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
      "00462dd4",
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
      "00462dd4",
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

- 旧版 [`00462d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462d7c.md#insn-00462d88)
- 新版 [`00462dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462dbc.md#insn-00462dc8)

~~~diff
- 00462d88 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00462d88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00462d88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00462d88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00462dc8 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00462dc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00462dc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00462dc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00462d88 bytes 4a610291
+ 00462dc8 bytes 4a611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

