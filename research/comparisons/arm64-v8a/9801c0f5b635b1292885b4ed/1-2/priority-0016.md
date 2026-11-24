# v16.0.0 → v16.0.1 · 最優先の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-70c0f7c61fb18ddbe9a19ad268537fcc"></a>

### [`00560304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md) → [`00560344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560344.md) FUN_00560344

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md) [`00c59410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md) [`00c59810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59810.md)

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
      "definition_site": "00560368",
      "incomplete_value": true,
      "site": "00560370",
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
      "definition_site": "00560328",
      "incomplete_value": true,
      "site": "00560330",
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
      "definition_site": "0056037c",
      "incomplete_value": true,
      "site": "0056037c",
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
      "definition_site": "0056033c",
      "incomplete_value": true,
      "site": "0056033c",
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
      "definition_site": "0056037c",
      "incomplete_value": true,
      "site": "0056037c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056033c",
      "incomplete_value": true,
      "site": "0056033c",
      "value": [
        "LOAD",
        "8",
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
      "00560360",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "00560368",
      "READ",
      [
        "storage",
        "00c92e70",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0056036c",
      "READ",
      [
        "storage",
        "00c92e88",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00560360",
      "READ",
      [
        "storage",
        "00c9b288",
        null,
        "pointer"
      ]
    ],
    [
      "00560368",
      "READ",
      [
        "storage",
        "00c93270",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0056036c",
      "READ",
      [
        "storage",
        "00c93288",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560314) · [`00560320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560320) · [`00560324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560324)
- 新版 [`00560354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560344.md#insn-00560354) · [`00560360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560344.md#insn-00560360)

~~~diff
- 00560314 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
+ 00560354 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
- 00560314 bytes d53900d0
+ 00560354 bytes d53900f0
- 00560320 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e88:8"]]
- 00560320 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00560360 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:288:8"]]
+ 00560360 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00560320 bytes b54647f9
+ 00560360 bytes b54641f9
- 00560324 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00560324 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b75d9e61c5c7c352a6ca4a9760b1d0"></a>

### [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) → [`005603c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md) FUN_005603c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`0055f618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

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
      "definition_site": "005603d0",
      "incomplete_value": false,
      "site": "005603d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560390",
      "incomplete_value": false,
      "site": "00560398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "005603d0",
      "PARAM",
      [
        "storage",
        "00ca5870",
        null,
        null
      ]
    ],
    [
      "005603f8",
      "DATA",
      [
        "storage",
        "00c6ae20",
        null,
        "undefined *"
      ]
    ],
    [
      "00560404",
      "DATA",
      [
        "storage",
        "00c6ad98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005603d0",
      "PARAM",
      [
        "storage",
        "00ca5c70",
        null,
        null
      ]
    ],
    [
      "005603f8",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ],
    [
      "00560404",
      "DATA",
      [
        "storage",
        "00c6b198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-00560398) · [`00560390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-00560390) · [`005603a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-005603a4)
- 新版 [`005603d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md#insn-005603d8) · [`005603d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md#insn-005603d0) · [`005603e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md#insn-005603e4)

~~~diff
- 00560398 ["INT_ADD", "register:40f0:8", ["const:560398:8", "const:4:8"]]
- 00560398 ["CALL", null, ["callee:00c583b0:8"]]
+ 005603d8 ["INT_ADD", "register:40f0:8", ["const:5603d8:8", "const:4:8"]]
+ 005603d8 ["CALL", null, ["callee:00c583b0:8"]]
- 00560398 bytes 06df1b94
+ 005603d8 bytes f6df1b94
- 00560390 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00560390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00560390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00560390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005603d0 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 005603d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005603d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005603d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00560390 bytes 00c02191
+ 005603d0 bytes 00c03191
- 005603a4 ["INT_ADD", "register:40f0:8", ["const:5603a4:8", "const:4:8"]]
- 005603a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 005603e4 ["INT_ADD", "register:40f0:8", ["const:5603e4:8", "const:4:8"]]
+ 005603e4 ["CALL", null, ["callee:00c57e90:8"]]
- 005603a4 bytes bbdd1b94
+ 005603e4 bytes abde1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5461b16e943f06b7c1a690918b674799"></a>

### [`00560704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560704.md) → [`00560744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560744.md) FUN_00560744

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
      "definition_site": "00560748",
      "incomplete_value": false,
      "site": "0056074c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560708",
      "incomplete_value": false,
      "site": "0056070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "0056074c",
      "DATA",
      [
        "storage",
        "00c6ae20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056074c",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560704.md#insn-00560704) · [`00560708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560704.md#insn-00560708)
- 新版 [`00560744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560744.md#insn-00560744) · [`00560748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560744.md#insn-00560748)

~~~diff
- 00560704 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560744 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560704 bytes 483800d0
+ 00560744 bytes 483800f0
- 00560708 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00560708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560748 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00560748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560708 bytes 08813891
+ 00560748 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbeeee32bd75f811656957ca4ef21b0c"></a>

### [`00560714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560714.md) → [`00560754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560754.md) FUN_00560754

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
      "definition_site": "00560764",
      "incomplete_value": false,
      "site": "0056076c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560724",
      "incomplete_value": false,
      "site": "0056072c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "0056076c",
      "DATA",
      [
        "storage",
        "00c6ae20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056076c",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560714.md#insn-00560720) · [`00560724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560714.md#insn-00560724) · [`00560730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560714.md#insn-00560730)
- 新版 [`00560760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560754.md#insn-00560760) · [`00560764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560754.md#insn-00560764) · [`00560770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560754.md#insn-00560770)

~~~diff
- 00560720 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560760 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560720 bytes 483800d0
+ 00560760 bytes 483800f0
- 00560724 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00560724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560764 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00560764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560724 bytes 08813891
+ 00560764 bytes 08810891
- 00560730 ["INT_ADD", "register:40f0:8", ["const:560730:8", "const:4:8"]]
- 00560730 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00560770 ["INT_ADD", "register:40f0:8", ["const:560770:8", "const:4:8"]]
+ 00560770 ["CALL", null, ["callee:00c57ea0:8"]]
- 00560730 bytes dcdc1b94
+ 00560770 bytes ccdd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-452e538ae299d9f8e517f881c2dc1fee"></a>

### [`0056074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md) → [`0056078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md) _INIT_26

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bfa930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa930.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bfad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md)

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
      "definition_site": "005607c8",
      "incomplete_value": true,
      "site": "005607c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560788",
      "incomplete_value": true,
      "site": "00560788",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ddd:8"
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
      "definition_site": "005607d4",
      "incomplete_value": false,
      "site": "005607dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560794",
      "incomplete_value": false,
      "site": "0056079c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "definition_site": "005607fc",
      "incomplete_value": true,
      "site": "00560808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005607bc",
      "incomplete_value": true,
      "site": "005607c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "005607ac",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "005607d4",
      "PARAM",
      [
        "storage",
        "00ca5870",
        null,
        null
      ]
    ],
    [
      "005607f8",
      "PARAM",
      [
        "storage",
        "00ca5870",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005607ac",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "005607d4",
      "PARAM",
      [
        "storage",
        "00ca5c70",
        null,
        null
      ]
    ],
    [
      "005607f8",
      "PARAM",
      [
        "storage",
        "00ca5c70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056079c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-0056079c) · [`005607c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-005607c8) · [`00560764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-00560764)
- 新版 [`005607dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md#insn-005607dc) · [`00560808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md#insn-00560808) · [`005607a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056078c.md#insn-005607a4)

~~~diff
- 0056079c ["INT_ADD", "register:40f0:8", ["const:56079c:8", "const:4:8"]]
- 0056079c ["CALL", null, ["callee:00c583a0:8"]]
+ 005607dc ["INT_ADD", "register:40f0:8", ["const:5607dc:8", "const:4:8"]]
+ 005607dc ["CALL", null, ["callee:00c583a0:8"]]
- 0056079c bytes 01de1b94
+ 005607dc bytes f1de1b94
- 005607c8 ["INT_ADD", "register:40f0:8", ["const:5607c8:8", "const:4:8"]]
- 005607c8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00560808 ["INT_ADD", "register:40f0:8", ["const:560808:8", "const:4:8"]]
+ 00560808 ["CALL", null, ["callee:00c57e30:8"]]
- 005607c8 bytes 9adc1b94
+ 00560808 bytes 8add1b94
- 00560764 ["COPY", "tmp:0:8", ["const:ddd:8"]]
- 00560764 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00560764 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00560764 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005607a4 ["COPY", "tmp:0:8", ["const:e1d:8"]]
+ 005607a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005607a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005607a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00560764 bytes 4a753791
+ 005607a4 bytes 4a753891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a0c1ded0fab654227b7627a993bd39"></a>

### [`0056081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md) → [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) FUN_0056085c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) [`009308a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009308a4.md) [`009313c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009313c0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 12件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) [`00930a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930a40.md) [`0093155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093155c.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00560878",
      "incomplete_value": false,
      "site": "00560880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560838",
      "incomplete_value": false,
      "site": "00560840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00560890",
      "incomplete_value": false,
      "site": "00560890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560850",
      "incomplete_value": false,
      "site": "00560850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
      "00560880",
      "DATA",
      [
        "storage",
        "00c6aed0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560890",
      "DATA",
      [
        "storage",
        "00c6af20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560880",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560890",
      "DATA",
      [
        "storage",
        "00c6b320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560830) · [`00560834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560834) · [`00560838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560838)
- 新版 [`00560870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560870) · [`00560874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560874) · [`00560878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md#insn-00560878)

~~~diff
- 00560830 ["INT_ADD", "register:40f0:8", ["const:560830:8", "const:4:8"]]
- 00560830 ["CALL", null, ["callee:00c57e90:8"]]
+ 00560870 ["INT_ADD", "register:40f0:8", ["const:560870:8", "const:4:8"]]
+ 00560870 ["CALL", null, ["callee:00c57e90:8"]]
- 00560830 bytes 98dc1b94
+ 00560870 bytes 88dd1b94
- 00560834 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560874 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560834 bytes 483800d0
+ 00560874 bytes 483800f0
- 00560838 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00560838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560878 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00560878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560838 bytes 08413b91
+ 00560878 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19dbe9a4489b829991836326726bfad8"></a>

### [`00560864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md) → [`005608a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md) FUN_005608a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`00560e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`00560e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560e48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0056093c",
      "incomplete_value": false,
      "site": "0056093c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005608fc",
      "incomplete_value": false,
      "site": "005608fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
      "0056093c",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ],
    [
      "005609bc",
      "READ",
      [
        "storage",
        "00c6af98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056093c",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ],
    [
      "005609bc",
      "READ",
      [
        "storage",
        "00c6b398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-00560894) · [`005608b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-005608b4) · [`005608d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-005608d8)
- 新版 [`005608d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-005608d4) · [`005608f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-005608f4) · [`00560918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005608a4.md#insn-00560918)

~~~diff
- 00560894 ["INT_ADD", "register:40f0:8", ["const:560894:8", "const:4:8"]]
- 00560894 ["CALL", null, ["callee:00550a14:8"]]
+ 005608d4 ["INT_ADD", "register:40f0:8", ["const:5608d4:8", "const:4:8"]]
+ 005608d4 ["CALL", null, ["callee:00550a14:8"]]
- 00560894 bytes 50c0ff97
+ 005608d4 bytes 50c0ff97
- 005608b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005608b4 ["INT_ADD", "register:40f0:8", ["const:5608b4:8", "const:4:8"]]
- 005608b4 ["CALLIND", null, ["register:0:8"]]
+ 005608f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005608f4 ["INT_ADD", "register:40f0:8", ["const:5608f4:8", "const:4:8"]]
+ 005608f4 ["CALLIND", null, ["register:0:8"]]
- 005608b4 bytes 00013fd6
+ 005608f4 bytes 00013fd6
- 005608d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005608d8 ["INT_ADD", "register:40f0:8", ["const:5608d8:8", "const:4:8"]]
- 005608d8 ["CALLIND", null, ["register:0:8"]]
+ 00560918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560918 ["INT_ADD", "register:40f0:8", ["const:560918:8", "const:4:8"]]
+ 00560918 ["CALLIND", null, ["register:0:8"]]
- 005608d8 bytes 00013fd6
+ 00560918 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f212fee2e27226b9db18974133049fa"></a>

### [`00560b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md) → [`00560b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md) FUN_00560b68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00560b80",
      "incomplete_value": false,
      "site": "00560b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560b40",
      "incomplete_value": false,
      "site": "00560b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "00560b84",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560b84",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b3c) · [`00560b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b40) · [`00560b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b50)
- 新版 [`00560b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md#insn-00560b7c) · [`00560b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md#insn-00560b80) · [`00560b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b68.md#insn-00560b90)

~~~diff
- 00560b3c ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00560b7c ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00560b3c bytes 493800d0
+ 00560b7c bytes 493800f0
- 00560b40 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00560b40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560b40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560b40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560b80 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00560b80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560b40 bytes 29c13991
+ 00560b80 bytes 29c10991
- 00560b50 ["INT_ADD", "register:40f0:8", ["const:560b50:8", "const:4:8"]]
- 00560b50 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00560b90 ["INT_ADD", "register:40f0:8", ["const:560b90:8", "const:4:8"]]
+ 00560b90 ["CALL", null, ["callee:00c57eb0:8"]]
- 00560b50 bytes d8db1b94
+ 00560b90 bytes c8dc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6869feeb8fddc8a6bed1589a133ec725"></a>

### [`00560b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md) → [`00560bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md) FUN_00560bb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00560bd0",
      "incomplete_value": false,
      "site": "00560bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560b90",
      "incomplete_value": false,
      "site": "00560b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "00560bd4",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560bd4",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560b8c) · [`00560b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560b90) · [`00560ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560ba0)
- 新版 [`00560bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560bcc) · [`00560bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560bd0) · [`00560be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560bb8.md#insn-00560be0)

~~~diff
- 00560b8c ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00560bcc ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00560b8c bytes 493800d0
+ 00560bcc bytes 493800f0
- 00560b90 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00560b90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560b90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560b90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560bd0 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00560bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560b90 bytes 29c13991
+ 00560bd0 bytes 29c10991
- 00560ba0 ["INT_ADD", "register:40f0:8", ["const:560ba0:8", "const:4:8"]]
- 00560ba0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00560be0 ["INT_ADD", "register:40f0:8", ["const:560be0:8", "const:4:8"]]
+ 00560be0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00560ba0 bytes c4db1b94
+ 00560be0 bytes b4dc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e282f5d37c0e5fd3c3d6ab88f1646ed"></a>

### [`00560bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bcc.md) → [`00560c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c0c.md) FUN_00560c0c

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
      "definition_site": "00560c10",
      "incomplete_value": false,
      "site": "00560c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560bd0",
      "incomplete_value": false,
      "site": "00560bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
      "00560c14",
      "DATA",
      [
        "storage",
        "00c6aed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c14",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bcc.md#insn-00560bcc) · [`00560bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bcc.md#insn-00560bd0)
- 新版 [`00560c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c0c.md#insn-00560c0c) · [`00560c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c0c.md#insn-00560c10)

~~~diff
- 00560bcc ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560c0c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560bcc bytes 483800d0
+ 00560c0c bytes 483800f0
- 00560bd0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00560bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560c10 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00560c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560bd0 bytes 08413b91
+ 00560c10 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fd93aa2b078349d0a53e8f0db4169d8"></a>

### [`00560bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bdc.md) → [`00560c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md) FUN_00560c1c

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
      "definition_site": "00560c2c",
      "incomplete_value": false,
      "site": "00560c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560bec",
      "incomplete_value": false,
      "site": "00560bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
      "00560c34",
      "DATA",
      [
        "storage",
        "00c6aed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c34",
      "DATA",
      [
        "storage",
        "00c6b2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bdc.md#insn-00560be8) · [`00560bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bdc.md#insn-00560bec) · [`00560bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560bdc.md#insn-00560bf8)
- 新版 [`00560c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md#insn-00560c28) · [`00560c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md#insn-00560c2c) · [`00560c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560c1c.md#insn-00560c38)

~~~diff
- 00560be8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560c28 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560be8 bytes 483800d0
+ 00560c28 bytes 483800f0
- 00560bec ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00560bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560c2c ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00560c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560bec bytes 08413b91
+ 00560c2c bytes 08410b91
- 00560bf8 ["INT_ADD", "register:40f0:8", ["const:560bf8:8", "const:4:8"]]
- 00560bf8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00560c38 ["INT_ADD", "register:40f0:8", ["const:560c38:8", "const:4:8"]]
+ 00560c38 ["CALL", null, ["callee:00c57ea0:8"]]
- 00560bf8 bytes aadb1b94
+ 00560c38 bytes 9adc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a1fded499427ceaa32c56c6c2d3a095"></a>

### [`00560c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md) → [`00560cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md) FUN_00560cb8

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
      "definition_site": "00560cd0",
      "incomplete_value": false,
      "site": "00560cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560c90",
      "incomplete_value": false,
      "site": "00560c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
      "00560cdc",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560cdc",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560c8c) · [`00560c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560c90) · [`00560cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560cc0)
- 新版 [`00560ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md#insn-00560ccc) · [`00560cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md#insn-00560cd0) · [`00560d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560cb8.md#insn-00560d00)

~~~diff
- 00560c8c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560ccc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560c8c bytes 483800d0
+ 00560ccc bytes 483800f0
- 00560c90 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 00560c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560cd0 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00560cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560c90 bytes 08c13d91
+ 00560cd0 bytes 08c10d91
- 00560cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560cc0 ["INT_ADD", "register:40f0:8", ["const:560cc0:8", "const:4:8"]]
- 00560cc0 ["CALLIND", null, ["register:0:8"]]
+ 00560d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560d00 ["INT_ADD", "register:40f0:8", ["const:560d00:8", "const:4:8"]]
+ 00560d00 ["CALLIND", null, ["register:0:8"]]
- 00560cc0 bytes 00013fd6
+ 00560d00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952b997652f7e384fb94f8dab337e134"></a>

### [`00560cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md) → [`00560d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md) FUN_00560d14

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
      "definition_site": "00560d40",
      "incomplete_value": false,
      "site": "00560d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560d00",
      "incomplete_value": false,
      "site": "00560d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
      "00560d40",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560d40",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560ce8) · [`00560cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560cf4) · [`00560cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560cf8)
- 新版 [`00560d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d28) · [`00560d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d34) · [`00560d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d14.md#insn-00560d38)

~~~diff
- 00560ce8 ["INT_ADD", "register:40f0:8", ["const:560ce8:8", "const:4:8"]]
- 00560ce8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00560d28 ["INT_ADD", "register:40f0:8", ["const:560d28:8", "const:4:8"]]
+ 00560d28 ["CALL", null, ["callee:00c57e90:8"]]
- 00560ce8 bytes 6adb1b94
+ 00560d28 bytes 5adc1b94
- 00560cf4 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560d34 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560cf4 bytes 483800d0
+ 00560d34 bytes 483800f0
- 00560cf8 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 00560cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560d38 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00560d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560cf8 bytes 08c13d91
+ 00560d38 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-357b28d725f1f55266ca5c2864322250"></a>

### [`00560d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md) → [`00560d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md) FUN_00560d9c

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560db8",
      "incomplete_value": true,
      "site": "00560db8",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560d78",
      "incomplete_value": true,
      "site": "00560d78",
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
            "const:f70:8"
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
      "00560db8",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560db8",
      "DATA",
      [
        "storage",
        "00c6b370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d70) · [`00560d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d74) · [`00560d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d98)
- 新版 [`00560db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md#insn-00560db0) · [`00560db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md#insn-00560db4) · [`00560dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560d9c.md#insn-00560dd8)

~~~diff
- 00560d70 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00560db0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00560d70 bytes 493800d0
+ 00560db0 bytes 493800f0
- 00560d74 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 00560d74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560d74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560d74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560db4 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00560db4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560db4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560db4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560d74 bytes 29c13d91
+ 00560db4 bytes 29c10d91
- 00560d98 ["COPY", "register:0:8", ["register:4048:8"]]
- 00560d98 ["INT_ADD", "register:40f0:8", ["const:560d98:8", "const:4:8"]]
- 00560d98 ["CALLIND", null, ["register:0:8"]]
+ 00560dd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00560dd8 ["INT_ADD", "register:40f0:8", ["const:560dd8:8", "const:4:8"]]
+ 00560dd8 ["CALLIND", null, ["register:0:8"]]
- 00560d98 bytes 20013fd6
+ 00560dd8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496b366ade36c7092b417b390e0b0021"></a>

### [`00560ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md) → [`00560ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md) FUN_00560ee0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "00560ef8",
      "incomplete_value": false,
      "site": "00560ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560eb8",
      "incomplete_value": false,
      "site": "00560eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
      "definition_site": "00560f04",
      "incomplete_value": false,
      "site": "00560f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560ec4",
      "incomplete_value": false,
      "site": "00560ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "00560ef8",
      "DATA",
      [
        "storage",
        "00c6aff0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560f04",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560ef8",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560f04",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md#insn-00560eac) · [`00560eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md#insn-00560eb0) · [`00560ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md#insn-00560ebc)
- 新版 [`00560eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md#insn-00560eec) · [`00560ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560ee0.md#insn-00560ef0)

~~~diff
- 00560eac ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560eec ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560eac bytes 483800d0
+ 00560eec bytes 483800f0
- 00560eb0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00560eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560ef0 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00560ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560eb0 bytes 08c13f91
+ 00560ef0 bytes 08c10f91
- 00560ebc ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00560ebc bytes 483800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-680a6d9347ea1a7ff3437f325fd7949f"></a>

### [`00560f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f54.md) → [`00560f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560f94.md) FUN_00560f94

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
      "definition_site": "00560f98",
      "incomplete_value": false,
      "site": "00560f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f58",
      "incomplete_value": false,
      "site": "00560f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
      "00560f9c",
      "DATA",
      [
        "storage",
        "00c6aff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560f9c",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f54.md#insn-00560f54) · [`00560f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f54.md#insn-00560f58)
- 新版 [`00560f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560f94.md#insn-00560f94) · [`00560f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560f94.md#insn-00560f98)

~~~diff
- 00560f54 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560f94 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560f54 bytes 483800d0
+ 00560f94 bytes 483800f0
- 00560f58 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00560f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560f98 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00560f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560f58 bytes 08c13f91
+ 00560f98 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed38c819fdfd90f23926e4968f22c23"></a>

### [`00560f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f64.md) → [`00560fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md) FUN_00560fa4

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
      "definition_site": "00560fb4",
      "incomplete_value": false,
      "site": "00560fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f74",
      "incomplete_value": false,
      "site": "00560f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
      "00560fbc",
      "DATA",
      [
        "storage",
        "00c6aff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560fbc",
      "DATA",
      [
        "storage",
        "00c6b3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f64.md#insn-00560f70) · [`00560f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f64.md#insn-00560f74) · [`00560f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560f64.md#insn-00560f80)
- 新版 [`00560fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md#insn-00560fb0) · [`00560fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md#insn-00560fb4) · [`00560fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fa4.md#insn-00560fc0)

~~~diff
- 00560f70 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00560fb0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560f70 bytes 483800d0
+ 00560fb0 bytes 483800f0
- 00560f74 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00560f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560fb4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00560fb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560fb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560fb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560f74 bytes 08c13f91
+ 00560fb4 bytes 08c10f91
- 00560f80 ["INT_ADD", "register:40f0:8", ["const:560f80:8", "const:4:8"]]
- 00560f80 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00560fc0 ["INT_ADD", "register:40f0:8", ["const:560fc0:8", "const:4:8"]]
+ 00560fc0 ["CALL", null, ["callee:00c57ea0:8"]]
- 00560f80 bytes c8da1b94
+ 00560fc0 bytes b8db1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b28091cee3b1ad5b13f2c4d5df63cf3"></a>

### [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) → [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md) FUN_005610b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 14件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 14件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0056110c",
      "incomplete_value": false,
      "site": "00561118",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005610cc",
      "incomplete_value": false,
      "site": "005610d8",
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
            "const:3ec:8"
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
      "definition_site": "0056139c",
      "incomplete_value": false,
      "site": "005613a4",
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
            "const:d45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056135c",
      "incomplete_value": false,
      "site": "00561364",
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
            "const:d05:8"
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
      "definition_site": "0056143c",
      "incomplete_value": false,
      "site": "00561440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:1c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005613fc",
      "incomplete_value": false,
      "site": "00561400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:189:8"
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
      "0056110c",
      "PARAM",
      [
        "storage",
        "002b73ec",
        null,
        "string"
      ]
    ],
    [
      "005611d4",
      "PARAM",
      [
        "storage",
        "002bb482",
        null,
        "string"
      ]
    ],
    [
      "005611f0",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056110c",
      "PARAM",
      [
        "storage",
        "002b742c",
        null,
        "string"
      ]
    ],
    [
      "005611d4",
      "PARAM",
      [
        "storage",
        "002bb4c2",
        null,
        "string"
      ]
    ],
    [
      "005611f0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005610d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-005610d8) · [`00561364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-00561364) · [`00561400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-00561400)
- 新版 [`00561118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-00561118) · [`005613a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-005613a4) · [`00561440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md#insn-00561440)

~~~diff
- 005610d8 ["INT_ADD", "register:40f0:8", ["const:5610d8:8", "const:4:8"]]
- 005610d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00561118 ["INT_ADD", "register:40f0:8", ["const:561118:8", "const:4:8"]]
+ 00561118 ["CALL", null, ["callee:00c57f60:8"]]
- 005610d8 bytes a2da1b94
+ 00561118 bytes 92db1b94
- 00561364 ["INT_ADD", "register:40f0:8", ["const:561364:8", "const:4:8"]]
- 00561364 ["CALL", null, ["callee:00c580b0:8"]]
+ 005613a4 ["INT_ADD", "register:40f0:8", ["const:5613a4:8", "const:4:8"]]
+ 005613a4 ["CALL", null, ["callee:00c580b0:8"]]
- 00561364 bytes 53da1b94
+ 005613a4 bytes 43db1b94
- 00561400 ["INT_ADD", "register:40f0:8", ["const:561400:8", "const:4:8"]]
- 00561400 ["CALL", null, ["callee:00c580b0:8"]]
+ 00561440 ["INT_ADD", "register:40f0:8", ["const:561440:8", "const:4:8"]]
+ 00561440 ["CALL", null, ["callee:00c580b0:8"]]
- 00561400 bytes 2cda1b94
+ 00561440 bytes 1cdb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f4a75dfa73447e6c24bdd3ecc668d88"></a>

### [`00561868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md) → [`005618a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md) FUN_005618a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005618c4",
      "incomplete_value": false,
      "site": "005618cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561884",
      "incomplete_value": false,
      "site": "0056188c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "005618cc",
      "DATA",
      [
        "storage",
        "00c6b040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005618cc",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md#insn-0056187c) · [`00561884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md#insn-00561884)
- 新版 [`005618bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md#insn-005618bc) · [`005618c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md#insn-005618c4)

~~~diff
- 0056187c ["INT_ADD", "register:40f0:8", ["const:56187c:8", "const:4:8"]]
- 0056187c ["CALL", null, ["callee:00c57e90:8"]]
+ 005618bc ["INT_ADD", "register:40f0:8", ["const:5618bc:8", "const:4:8"]]
+ 005618bc ["CALL", null, ["callee:00c57e90:8"]]
- 0056187c bytes 85d81b94
+ 005618bc bytes 75d91b94
- 00561884 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00561884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005618c4 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 005618c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005618c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005618c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561884 bytes 08010191
+ 005618c4 bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c5c6055fa4844e349717592a1cf2b4"></a>

### [`005618ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md) → [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) FUN_005618ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 5件 [`00560420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560420.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 5件 [`00560460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

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
      "definition_site": "00561968",
      "incomplete_value": false,
      "site": "00561970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:f09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561928",
      "incomplete_value": false,
      "site": "00561930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:ec9:8"
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
      "0056194c",
      "PARAM",
      [
        "storage",
        "002a8a0c",
        null,
        null
      ]
    ],
    [
      "00561968",
      "PARAM",
      [
        "storage",
        "002b4ec9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056194c",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ],
    [
      "00561968",
      "PARAM",
      [
        "storage",
        "002b4f09",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-00561930) · [`0056190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-0056190c) · [`00561914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-00561914)
- 新版 [`00561970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-00561970) · [`0056194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-0056194c) · [`00561954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md#insn-00561954)

~~~diff
- 00561930 ["INT_ADD", "register:40f0:8", ["const:561930:8", "const:4:8"]]
- 00561930 ["CALL", null, ["callee:00c57f70:8"]]
+ 00561970 ["INT_ADD", "register:40f0:8", ["const:561970:8", "const:4:8"]]
+ 00561970 ["CALL", null, ["callee:00c57f70:8"]]
- 00561930 bytes 90d81b94
+ 00561970 bytes 80d91b94
- 0056190c ["COPY", "tmp:0:8", ["const:a0c:8"]]
- 0056190c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056190c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056190c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056194c ["COPY", "tmp:0:8", ["const:ad9:8"]]
+ 0056194c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056194c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056194c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056190c bytes 21302891
+ 0056194c bytes 21642b91
- 00561914 ["INT_ADD", "register:40f0:8", ["const:561914:8", "const:4:8"]]
- 00561914 ["CALL", null, ["callee:00c57f70:8"]]
+ 00561954 ["INT_ADD", "register:40f0:8", ["const:561954:8", "const:4:8"]]
+ 00561954 ["CALL", null, ["callee:00c57f70:8"]]
- 00561914 bytes 97d81b94
+ 00561954 bytes 87d91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e10cf7415f7e74507ff429c81ba96ed"></a>

### [`00561ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md) → [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) FUN_00561b24

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d60.md)
- 新版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561b70",
      "incomplete_value": true,
      "site": "00561b70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b30",
      "incomplete_value": true,
      "site": "00561b30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
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
      "definition_site": "00561b90",
      "incomplete_value": true,
      "site": "00561ba0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b50",
      "incomplete_value": true,
      "site": "00561b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:650:8"
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
      "definition_site": "00561b8c",
      "incomplete_value": true,
      "site": "00561ba4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b4c",
      "incomplete_value": true,
      "site": "00561b64",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e25:8"
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
      "00561b48",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "00561b8c",
      "READ",
      [
        "storage",
        "002bee25",
        null,
        "string"
      ]
    ],
    [
      "00561b8c",
      "READ",
      [
        "storage",
        "002bee35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561b48",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "00561b8c",
      "READ",
      [
        "storage",
        "002bee65",
        null,
        "string"
      ]
    ],
    [
      "00561b8c",
      "READ",
      [
        "storage",
        "002bee75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561b00) · [`00561b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561b3c) · [`00561b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561b44)
- 新版 [`00561b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b40) · [`00561b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b7c) · [`00561b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md#insn-00561b84)

~~~diff
- 00561b00 ["COPY", "tmp:0:8", ["const:8ce:8"]]
- 00561b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561b40 ["COPY", "tmp:0:8", ["const:90e:8"]]
+ 00561b40 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b40 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b40 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561b00 bytes 4a392391
+ 00561b40 bytes 4a392491
- 00561b3c ["INT_ADD", "register:40f0:8", ["const:561b3c:8", "const:4:8"]]
- 00561b3c ["CALL", null, ["callee:00c57e90:8"]]
+ 00561b7c ["INT_ADD", "register:40f0:8", ["const:561b7c:8", "const:4:8"]]
+ 00561b7c ["CALL", null, ["callee:00c57e90:8"]]
- 00561b3c bytes d5d71b94
+ 00561b7c bytes c5d81b94
- 00561b44 ["COPY", "tmp:0:8", ["const:e25:8"]]
- 00561b44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561b44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561b44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561b84 ["COPY", "tmp:0:8", ["const:e65:8"]]
+ 00561b84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561b44 bytes 4a953891
+ 00561b84 bytes 4a953991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fac06de5011ed9efc982b84c3db9c27e"></a>

### [`00561cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md) → [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) FUN_00561cec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00561d08",
      "incomplete_value": false,
      "site": "00561d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561cc8",
      "incomplete_value": false,
      "site": "00561cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "00561d10",
      "DATA",
      [
        "storage",
        "00c6b090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561d10",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md#insn-00561cc0) · [`00561cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md#insn-00561cc8)
- 新版 [`00561d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md#insn-00561d00) · [`00561d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md#insn-00561d08)

~~~diff
- 00561cc0 ["INT_ADD", "register:40f0:8", ["const:561cc0:8", "const:4:8"]]
- 00561cc0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00561d00 ["INT_ADD", "register:40f0:8", ["const:561d00:8", "const:4:8"]]
+ 00561d00 ["CALL", null, ["callee:00c57e90:8"]]
- 00561cc0 bytes 74d71b94
+ 00561d00 bytes 64d81b94
- 00561cc8 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00561cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561d08 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00561d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561cc8 bytes 08410291
+ 00561d08 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59001929f50cfc595744a08cb42d846c"></a>

### [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) → [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) FUN_00561d34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`0044fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00563710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md) [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 21件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`0043e578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e578.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) [`0044fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00563750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563750.md) [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00561df4",
      "incomplete_value": false,
      "site": "00561df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561db4",
      "incomplete_value": false,
      "site": "00561db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "definition_site": "00561d78",
      "incomplete_value": true,
      "site": "00561d78",
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
      "definition_site": "00561d38",
      "incomplete_value": true,
      "site": "00561d38",
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
      "00561d74",
      "READ",
      [
        "storage",
        "00ca58c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00561df4",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561e80",
      "READ",
      [
        "storage",
        "00c6b108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561d74",
      "READ",
      [
        "storage",
        "00ca5cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00561df4",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561e80",
      "READ",
      [
        "storage",
        "00c6b508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d34) · [`00561d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d60) · [`00561d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d8c)
- 新版 [`00561d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561d74) · [`00561da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561da0) · [`00561dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md#insn-00561dcc)

~~~diff
- 00561d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8c0:8"]]
- 00561d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00561d74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
+ 00561d74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00561d34 bytes 296144f9
+ 00561d74 bytes 296146f9
- 00561d60 ["INT_ADD", "register:40f0:8", ["const:561d60:8", "const:4:8"]]
- 00561d60 ["CALL", null, ["callee:0043bb20:8"]]
+ 00561da0 ["INT_ADD", "register:40f0:8", ["const:561da0:8", "const:4:8"]]
+ 00561da0 ["CALL", null, ["callee:0043bb20:8"]]
- 00561d60 bytes 6067fb97
+ 00561da0 bytes 6067fb97
- 00561d8c ["INT_ADD", "register:40f0:8", ["const:561d8c:8", "const:4:8"]]
- 00561d8c ["CALL", null, ["callee:0043bb20:8"]]
+ 00561dcc ["INT_ADD", "register:40f0:8", ["const:561dcc:8", "const:4:8"]]
+ 00561dcc ["CALL", null, ["callee:0043bb20:8"]]
- 00561d8c bytes 5567fb97
+ 00561dcc bytes 5567fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f14a4b624492f2d4574075173b37ba5"></a>

### [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) → [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) FUN_00561fd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`005647a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`005647e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005623e8",
      "incomplete_value": false,
      "site": "005623f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005623a8",
      "incomplete_value": false,
      "site": "005623b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:220:8"
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
      "005623f4",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005623f4",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-00561ffc) · [`0056200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-0056200c) · [`00562038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-00562038)
- 新版 [`0056203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-0056203c) · [`0056204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-0056204c) · [`00562078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md#insn-00562078)

~~~diff
- 00561ffc ["INT_ADD", "register:40f0:8", ["const:561ffc:8", "const:4:8"]]
- 00561ffc ["CALL", null, ["callee:005626f4:8"]]
+ 0056203c ["INT_ADD", "register:40f0:8", ["const:56203c:8", "const:4:8"]]
+ 0056203c ["CALL", null, ["callee:005626f4:8"]]
- 00561ffc bytes ae010094
+ 0056203c bytes ae010094
- 0056200c ["INT_ADD", "register:40f0:8", ["const:56200c:8", "const:4:8"]]
- 0056200c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0056204c ["INT_ADD", "register:40f0:8", ["const:56204c:8", "const:4:8"]]
+ 0056204c ["CALL", null, ["callee:00c57eb0:8"]]
- 0056200c bytes a9d61b94
+ 0056204c bytes 99d71b94
- 00562038 ["INT_ADD", "register:40f0:8", ["const:562038:8", "const:4:8"]]
- 00562038 ["CALL", null, ["callee:00c58430:8"]]
+ 00562078 ["INT_ADD", "register:40f0:8", ["const:562078:8", "const:4:8"]]
+ 00562078 ["CALL", null, ["callee:00c58430:8"]]
- 00562038 bytes fed71b94
+ 00562078 bytes eed81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09941f973ff90530fca41bf66f4bcfc1"></a>

### [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) → [`00562cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md) FUN_00562cdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00562d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562d90.md) [`00563098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563098.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00562ce8",
      "incomplete_value": false,
      "site": "00562cec",
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
      "definition_site": "00562ca8",
      "incomplete_value": false,
      "site": "00562cac",
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
      "00562ce8",
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
      "00562ce8",
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

- 旧版 [`00562cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md#insn-00562cac) · [`00562ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md#insn-00562ca8)
- 新版 [`00562cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md#insn-00562cec) · [`00562ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/00562cdc.md#insn-00562ce8)

~~~diff
- 00562cac ["INT_ADD", "register:40f0:8", ["const:562cac:8", "const:4:8"]]
- 00562cac ["CALL", null, ["callee:0043b778:8"]]
+ 00562cec ["INT_ADD", "register:40f0:8", ["const:562cec:8", "const:4:8"]]
+ 00562cec ["CALL", null, ["callee:0043b778:8"]]
- 00562cac bytes a362fb97
+ 00562cec bytes a362fb97
- 00562ca8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00562ca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00562ca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00562ca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00562ce8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00562ce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00562ce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00562ce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00562ca8 bytes 00303c91
+ 00562ce8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e593f90092058c4c7a86399578e07d9"></a>

### [`005633a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633a4.md) → [`005633e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633e4.md) FUN_005633e4

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
      "definition_site": "005633e8",
      "incomplete_value": false,
      "site": "005633ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005633a8",
      "incomplete_value": false,
      "site": "005633ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "005633ec",
      "DATA",
      [
        "storage",
        "00c6b040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005633ec",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005633a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633a4.md#insn-005633a8)
- 新版 [`005633e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633e4.md#insn-005633e8)

~~~diff
- 005633a8 ["COPY", "tmp:0:8", ["const:40:8"]]
- 005633a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005633a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005633a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005633e8 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 005633e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005633e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005633e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005633a8 bytes 08010191
+ 005633e8 bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c0b7520c918230e94356b91a6c62602"></a>

### [`005633b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633b4.md) → [`005633f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md) FUN_005633f4

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
      "definition_site": "00563404",
      "incomplete_value": false,
      "site": "0056340c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005633c4",
      "incomplete_value": false,
      "site": "005633cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "0056340c",
      "DATA",
      [
        "storage",
        "00c6b040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056340c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005633c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633b4.md#insn-005633c4) · [`005633d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005633b4.md#insn-005633d0)
- 新版 [`00563404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md#insn-00563404) · [`00563410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005633f4.md#insn-00563410)

~~~diff
- 005633c4 ["COPY", "tmp:0:8", ["const:40:8"]]
- 005633c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005633c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005633c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563404 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00563404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005633c4 bytes 08010191
+ 00563404 bytes 08011191
- 005633d0 ["INT_ADD", "register:40f0:8", ["const:5633d0:8", "const:4:8"]]
- 005633d0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00563410 ["INT_ADD", "register:40f0:8", ["const:563410:8", "const:4:8"]]
+ 00563410 ["CALL", null, ["callee:00c57ea0:8"]]
- 005633d0 bytes b4d11b94
+ 00563410 bytes a4d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03d5afe3aa144f8ced2d7d9cc844f5d"></a>

### [`00563454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563454.md) → [`00563494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563494.md) FUN_00563494

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
      "definition_site": "00563498",
      "incomplete_value": false,
      "site": "0056349c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563458",
      "incomplete_value": false,
      "site": "0056345c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "0056349c",
      "DATA",
      [
        "storage",
        "00c6b090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056349c",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563454.md#insn-00563458)
- 新版 [`00563498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563494.md#insn-00563498)

~~~diff
- 00563458 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00563458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563498 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00563498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563458 bytes 08410291
+ 00563498 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121bfdcd597dacd078a3394dc6dd46df"></a>

### [`00563464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563464.md) → [`005634a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md) FUN_005634a4

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
      "definition_site": "005634b4",
      "incomplete_value": false,
      "site": "005634bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563474",
      "incomplete_value": false,
      "site": "0056347c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "005634bc",
      "DATA",
      [
        "storage",
        "00c6b090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005634bc",
      "DATA",
      [
        "storage",
        "00c6b490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563464.md#insn-00563474) · [`00563480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563464.md#insn-00563480)
- 新版 [`005634b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md#insn-005634b4) · [`005634c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634a4.md#insn-005634c0)

~~~diff
- 00563474 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00563474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563474 bytes 08410291
+ 005634b4 bytes 08411291
- 00563480 ["INT_ADD", "register:40f0:8", ["const:563480:8", "const:4:8"]]
- 00563480 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005634c0 ["INT_ADD", "register:40f0:8", ["const:5634c0:8", "const:4:8"]]
+ 005634c0 ["CALL", null, ["callee:00c57ea0:8"]]
- 00563480 bytes 88d11b94
+ 005634c0 bytes 78d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48db268a101c59cd71bd582e72a12b1"></a>

### [`005634ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md) → [`005634ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md) FUN_005634ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00563504",
      "incomplete_value": false,
      "site": "00563508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005634c4",
      "incomplete_value": false,
      "site": "005634c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "00563508",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563508",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005634c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md#insn-005634c4) · [`005634d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md#insn-005634d4)
- 新版 [`00563504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md#insn-00563504) · [`00563514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/005634ec.md#insn-00563514)

~~~diff
- 005634c4 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 005634c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005634c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005634c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563504 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00563504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005634c4 bytes 29810391
+ 00563504 bytes 29811391
- 005634d4 ["INT_ADD", "register:40f0:8", ["const:5634d4:8", "const:4:8"]]
- 005634d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00563514 ["INT_ADD", "register:40f0:8", ["const:563514:8", "const:4:8"]]
+ 00563514 ["CALL", null, ["callee:00c57eb0:8"]]
- 005634d4 bytes 77d11b94
+ 00563514 bytes 67d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54aa2b0f4b91f132712c03922f97710c"></a>

### [`005634fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md) → [`0056353c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md) FUN_0056353c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00563554",
      "incomplete_value": false,
      "site": "00563558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563514",
      "incomplete_value": false,
      "site": "00563518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "00563558",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563558",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563514) · [`00563524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563524) · [`00563534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563534)
- 新版 [`00563554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563554) · [`00563564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563564) · [`00563574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056353c.md#insn-00563574)

~~~diff
- 00563514 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00563514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563554 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00563554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563514 bytes 29810391
+ 00563554 bytes 29811391
- 00563524 ["INT_ADD", "register:40f0:8", ["const:563524:8", "const:4:8"]]
- 00563524 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00563564 ["INT_ADD", "register:40f0:8", ["const:563564:8", "const:4:8"]]
+ 00563564 ["CALL", null, ["callee:00c57eb0:8"]]
- 00563524 bytes 63d11b94
+ 00563564 bytes 53d21b94
- 00563534 ["INT_ADD", "register:40f0:8", ["const:563534:8", "const:4:8"]]
- 00563534 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00563574 ["INT_ADD", "register:40f0:8", ["const:563574:8", "const:4:8"]]
+ 00563574 ["CALL", null, ["callee:00c57eb0:8"]]
- 00563534 bytes 5fd11b94
+ 00563574 bytes 4fd21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00c72f36d8b4e0246d4cacdfe623fb26"></a>

### [`00563548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md) → [`00563588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md) FUN_00563588

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005635bc",
      "incomplete_value": false,
      "site": "005635bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056357c",
      "incomplete_value": false,
      "site": "0056357c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "005635bc",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005635bc",
      "DATA",
      [
        "storage",
        "00c6b4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-00563560) · [`00563570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-00563570) · [`00563578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-00563578)
- 新版 [`005635a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md#insn-005635a0) · [`005635b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563588.md#insn-005635b0)

~~~diff
- 00563560 ["INT_ADD", "register:40f0:8", ["const:563560:8", "const:4:8"]]
- 00563560 ["CALL", null, ["callee:00c57e90:8"]]
+ 005635a0 ["INT_ADD", "register:40f0:8", ["const:5635a0:8", "const:4:8"]]
+ 005635a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00563560 bytes 4cd11b94
+ 005635a0 bytes 3cd21b94
- 00563570 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00563570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00563570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00563570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005635b0 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 005635b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005635b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005635b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00563570 bytes 4a810391
+ 005635b0 bytes 4a811391
- 00563578 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00563578 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8705c927933eb5c6e303161af48bd1"></a>

### [`00563750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md) → [`00563790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md) FUN_00563790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005637bc",
      "incomplete_value": true,
      "site": "005637bc",
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
      "definition_site": "0056377c",
      "incomplete_value": true,
      "site": "0056377c",
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
      "005637b4",
      "READ",
      [
        "storage",
        "00ca58c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005637b4",
      "READ",
      [
        "storage",
        "00ca5cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-00563774) · [`00563798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-00563798) · [`005637cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-005637cc)
- 新版 [`005637b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-005637b4) · [`005637d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-005637d8) · [`0056380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563790.md#insn-0056380c)

~~~diff
- 00563774 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8c0:8"]]
- 00563774 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005637b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
+ 005637b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00563774 bytes 086144f9
+ 005637b4 bytes 086146f9
- 00563798 ["COPY", "register:0:8", ["register:4048:8"]]
- 00563798 ["INT_ADD", "register:40f0:8", ["const:563798:8", "const:4:8"]]
- 00563798 ["CALLIND", null, ["register:0:8"]]
+ 005637d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005637d8 ["INT_ADD", "register:40f0:8", ["const:5637d8:8", "const:4:8"]]
+ 005637d8 ["CALLIND", null, ["register:0:8"]]
- 00563798 bytes 20013fd6
+ 005637d8 bytes 20013fd6
- 005637cc ["INT_ADD", "register:40f0:8", ["const:5637cc:8", "const:4:8"]]
- 005637cc ["CALL", null, ["callee:00459d74:8"]]
+ 0056380c ["INT_ADD", "register:40f0:8", ["const:56380c:8", "const:4:8"]]
+ 0056380c ["CALL", null, ["callee:00459d74:8"]]
- 005637cc bytes 5ad9fb97
+ 0056380c bytes 5ad9fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbed07cfa4a10066da979b57d7721a76"></a>

### [`005637fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005637fc.md) → [`0056383c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056383c.md) FUN_0056383c

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
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563800",
      "incomplete_value": false,
      "site": "00563804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "00563844",
      "DATA",
      [
        "storage",
        "00c6b160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563844",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005637fc.md#insn-00563800)
- 新版 [`00563840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056383c.md#insn-00563840)

~~~diff
- 00563800 ["COPY", "tmp:0:8", ["const:160:8"]]
- 00563800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563840 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 00563840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563800 bytes 08810591
+ 00563840 bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8ab2a5cd73dd5e64c548450005693aa"></a>

### [`0056380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056380c.md) → [`0056384c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md) FUN_0056384c

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
      "definition_site": "0056385c",
      "incomplete_value": false,
      "site": "00563864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056381c",
      "incomplete_value": false,
      "site": "00563824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "00563864",
      "DATA",
      [
        "storage",
        "00c6b160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563864",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056381c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056380c.md#insn-0056381c) · [`00563828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056380c.md#insn-00563828)
- 新版 [`0056385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md#insn-0056385c) · [`00563868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056384c.md#insn-00563868)

~~~diff
- 0056381c ["COPY", "tmp:0:8", ["const:160:8"]]
- 0056381c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056381c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056381c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056385c ["COPY", "tmp:0:8", ["const:560:8"]]
+ 0056385c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056385c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056385c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056381c bytes 08810591
+ 0056385c bytes 08811591
- 00563828 ["INT_ADD", "register:40f0:8", ["const:563828:8", "const:4:8"]]
- 00563828 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00563868 ["INT_ADD", "register:40f0:8", ["const:563868:8", "const:4:8"]]
+ 00563868 ["CALL", null, ["callee:00c57ea0:8"]]
- 00563828 bytes 9ed01b94
+ 00563868 bytes 8ed11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af3b0387652c153cf041e9845fa7faf"></a>

### [`0056383c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056383c.md) → [`0056387c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056387c.md) FUN_0056387c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)

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
      "definition_site": "0056388c",
      "incomplete_value": false,
      "site": "00563890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056384c",
      "incomplete_value": false,
      "site": "00563850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "00563890",
      "DATA",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563890",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056384c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056383c.md#insn-0056384c)
- 新版 [`0056388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056387c.md#insn-0056388c)

~~~diff
- 0056384c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0056384c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056384c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056384c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056388c ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 0056388c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056388c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056388c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056384c bytes 29c10691
+ 0056388c bytes 29c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf12a0424342f07f524b672ddab390de"></a>

### [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) → [`0056389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md) FUN_0056389c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005652d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005652d4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`00563ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00565314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565314.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`00563b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563b04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563888",
      "incomplete_value": false,
      "site": "005638a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "005638e4",
      "DATA",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00563994",
      "READ",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005638e4",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00563994",
      "READ",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-00563888) · [`005638c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-005638c8) · [`005638d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-005638d8)
- 新版 [`005638c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-005638c8) · [`00563908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-00563908) · [`00563918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/0056389c.md#insn-00563918)

~~~diff
- 00563888 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00563888 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00563888 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00563888 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005638c8 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 005638c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005638c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005638c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00563888 bytes 4ac10691
+ 005638c8 bytes 4ac11691
- 005638c8 ["INT_ADD", "register:40f0:8", ["const:5638c8:8", "const:4:8"]]
- 005638c8 ["CALL", null, ["callee:005626f4:8"]]
+ 00563908 ["INT_ADD", "register:40f0:8", ["const:563908:8", "const:4:8"]]
+ 00563908 ["CALL", null, ["callee:005626f4:8"]]
- 005638c8 bytes 7bfbff97
+ 00563908 bytes 7bfbff97
- 005638d8 ["INT_ADD", "register:40f0:8", ["const:5638d8:8", "const:4:8"]]
- 005638d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00563918 ["INT_ADD", "register:40f0:8", ["const:563918:8", "const:4:8"]]
+ 00563918 ["CALL", null, ["callee:00c57eb0:8"]]
- 005638d8 bytes 76d01b94
+ 00563918 bytes 66d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f1e610b3be1196c6d8a7b3fe198727b"></a>

### [`00564548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md) → [`00564588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md) FUN_00564588

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00563df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md) [`00864ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/00864ca0.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`0091a0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a0f8.md) [`00a42f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42f40.md) · 呼出先 9件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 5件 [`00563e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563e30.md) [`00864ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864ce0.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`0091a294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091a294.md) [`00a43138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43138.md) · 呼出先 9件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005645d0",
      "incomplete_value": true,
      "site": "005645e0",
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
      "definition_site": "00564590",
      "incomplete_value": true,
      "site": "005645a0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005645d8",
      "incomplete_value": true,
      "site": "005645e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00564598",
      "incomplete_value": true,
      "site": "005645a4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564638",
      "incomplete_value": true,
      "site": "0056463c",
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
      "definition_site": "005645f8",
      "incomplete_value": true,
      "site": "005645fc",
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
      "005645bc",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "005645d8",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "005645bc",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "005645d8",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005645e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-005645e4) · [`0056457c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-0056457c) · [`00564580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-00564580)
- 新版 [`00564624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-00564624) · [`005645bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-005645bc) · [`005645c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md#insn-005645c0)

~~~diff
- 005645e4 ["INT_ADD", "register:40f0:8", ["const:5645e4:8", "const:4:8"]]
- 005645e4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00564624 ["INT_ADD", "register:40f0:8", ["const:564624:8", "const:4:8"]]
+ 00564624 ["CALL", null, ["callee:00c581f0:8"]]
- 005645e4 bytes 03ce1b94
+ 00564624 bytes f3ce1b94
- 0056457c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:888:8"]]
- 0056457c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005645bc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
+ 005645bc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 0056457c bytes 5a4744f9
+ 005645bc bytes 5a4746f9
- 00564580 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:7b8:8"]]
- 00564580 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005645c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:bb8:8"]]
+ 005645c0 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00564580 bytes 39df43f9
+ 005645c0 bytes 39df45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0126ec97c0884e62e9a30d02c25ccf8d"></a>

### [`00564754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564754.md) → [`00564794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564794.md) FUN_00564794

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
      "definition_site": "00564798",
      "incomplete_value": false,
      "site": "0056479c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564758",
      "incomplete_value": false,
      "site": "0056475c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0056479c",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056479c",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564754.md#insn-00564758)
- 新版 [`00564798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564794.md#insn-00564798)

~~~diff
- 00564758 ["COPY", "tmp:0:8", ["const:220:8"]]
- 00564758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564798 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00564798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564758 bytes 08810891
+ 00564798 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16077f036f7c65519fe3dfc834350769"></a>

### [`00564764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564764.md) → [`005647a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md) FUN_005647a4

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
      "definition_site": "005647b4",
      "incomplete_value": false,
      "site": "005647bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564774",
      "incomplete_value": false,
      "site": "0056477c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:220:8"
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
      "005647bc",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005647bc",
      "DATA",
      [
        "storage",
        "00c6b620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564764.md#insn-00564774) · [`00564780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564764.md#insn-00564780)
- 新版 [`005647b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md#insn-005647b4) · [`005647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647a4.md#insn-005647c0)

~~~diff
- 00564774 ["COPY", "tmp:0:8", ["const:220:8"]]
- 00564774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005647b4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 005647b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005647b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005647b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564774 bytes 08810891
+ 005647b4 bytes 08811891
- 00564780 ["INT_ADD", "register:40f0:8", ["const:564780:8", "const:4:8"]]
- 00564780 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005647c0 ["INT_ADD", "register:40f0:8", ["const:5647c0:8", "const:4:8"]]
+ 005647c0 ["CALL", null, ["callee:00c57ea0:8"]]
- 00564780 bytes c8cc1b94
+ 005647c0 bytes b8cd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1afaf17c215317bbf6d5ff6663b3f9ea"></a>

### [`005647a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md) → [`005647e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md) FUN_005647e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "00564804",
      "incomplete_value": false,
      "site": "00564804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005647c4",
      "incomplete_value": false,
      "site": "005647c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00564804",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564804",
      "DATA",
      [
        "storage",
        "00c6b670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005647bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md#insn-005647bc) · [`005647c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md#insn-005647c0)
- 新版 [`005647fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md#insn-005647fc) · [`00564800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647e0.md#insn-00564800)

~~~diff
- 005647bc ["COPY", "tmp:0:8", ["const:270:8"]]
- 005647bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005647bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005647bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005647fc ["COPY", "tmp:0:8", ["const:670:8"]]
+ 005647fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005647fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005647fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005647bc bytes 08c10991
+ 005647fc bytes 08c11991
- 005647c0 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005647c0 bytes f40300aa
+ 00564800 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00564800 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a1bf8a9e055198d3aa6ab936f7ba0e"></a>

### [`00564d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md) → [`00564d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md) FUN_00564d4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00564dcc",
      "incomplete_value": false,
      "site": "00564dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:ccd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564d8c",
      "incomplete_value": false,
      "site": "00564d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:c8d:8"
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
      "definition_site": "00564fa4",
      "incomplete_value": false,
      "site": "00564fb0",
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
            "const:94a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564f64",
      "incomplete_value": false,
      "site": "00564f70",
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
            "const:86e:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00564dcc",
      "PARAM",
      [
        "storage",
        "002b2c8d",
        null,
        null
      ]
    ],
    [
      "00564f08",
      "PARAM",
      [
        "storage",
        "002a2000",
        null,
        null
      ]
    ],
    [
      "00564fa4",
      "PARAM",
      [
        "storage",
        "002a786e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00564dcc",
      "PARAM",
      [
        "storage",
        "002b2ccd",
        null,
        null
      ]
    ],
    [
      "00564f08",
      "PARAM",
      [
        "storage",
        "002a20cd",
        null,
        null
      ]
    ],
    [
      "00564fa4",
      "PARAM",
      [
        "storage",
        "002a794a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564d94) · [`00564f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564f30) · [`00564f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564f70)
- 新版 [`00564dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564dd4) · [`00564f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564f70) · [`00564fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564d4c.md#insn-00564fb0)

~~~diff
- 00564d94 ["INT_ADD", "register:40f0:8", ["const:564d94:8", "const:4:8"]]
- 00564d94 ["CALL", null, ["callee:00c57f70:8"]]
+ 00564dd4 ["INT_ADD", "register:40f0:8", ["const:564dd4:8", "const:4:8"]]
+ 00564dd4 ["CALL", null, ["callee:00c57f70:8"]]
- 00564d94 bytes 77cb1b94
+ 00564dd4 bytes 67cc1b94
- 00564f30 ["INT_ADD", "register:40f0:8", ["const:564f30:8", "const:4:8"]]
- 00564f30 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00564f70 ["INT_ADD", "register:40f0:8", ["const:564f70:8", "const:4:8"]]
+ 00564f70 ["CALL", null, ["callee:00c57eb0:8"]]
- 00564f30 bytes e0ca1b94
+ 00564f70 bytes d0cb1b94
- 00564f70 ["INT_ADD", "register:40f0:8", ["const:564f70:8", "const:4:8"]]
- 00564f70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00564fb0 ["INT_ADD", "register:40f0:8", ["const:564fb0:8", "const:4:8"]]
+ 00564fb0 ["CALL", null, ["callee:00c57f60:8"]]
- 00564f70 bytes fcca1b94
+ 00564fb0 bytes eccb1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e0c7a4099671495e1906457f0b3e65f"></a>

### [`005653a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md) → [`005653e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md) FUN_005653e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564794.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005647d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/005647d4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005653fc",
      "incomplete_value": false,
      "site": "00565400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005653bc",
      "incomplete_value": false,
      "site": "005653c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "00565400",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565400",
      "DATA",
      [
        "storage",
        "00c6b670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005653bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-005653bc) · [`005653d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-005653d0) · [`00565418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-00565418)
- 新版 [`005653fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-005653fc) · [`00565410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-00565410) · [`00565458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005653e4.md#insn-00565458)

~~~diff
- 005653bc ["COPY", "tmp:0:8", ["const:270:8"]]
- 005653bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005653bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005653bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005653fc ["COPY", "tmp:0:8", ["const:670:8"]]
+ 005653fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005653fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005653fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005653bc bytes 08c10991
+ 005653fc bytes 08c11991
- 005653d0 ["INT_ADD", "register:40f0:8", ["const:5653d0:8", "const:4:8"]]
- 005653d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00565410 ["INT_ADD", "register:40f0:8", ["const:565410:8", "const:4:8"]]
+ 00565410 ["CALL", null, ["callee:00c53d00:8"]]
- 005653d0 bytes 44b91b94
+ 00565410 bytes 3cba1b94
- 00565418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565418 ["INT_ADD", "register:40f0:8", ["const:565418:8", "const:4:8"]]
- 00565418 ["CALLIND", null, ["register:0:8"]]
+ 00565458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00565458 ["INT_ADD", "register:40f0:8", ["const:565458:8", "const:4:8"]]
+ 00565458 ["CALLIND", null, ["register:0:8"]]
- 00565418 bytes 00013fd6
+ 00565458 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1caf5928e258bc6d03cb2723ec8feacf"></a>

### [`0056547c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md) → [`005654bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md) _INIT_27

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00560fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fa4.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00560fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560fe4.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 52.00% / 新版 52.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 10件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005654e4",
      "incomplete_value": false,
      "site": "005654e4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:ca0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654a4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:8a0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565504",
      "incomplete_value": false,
      "site": "00565504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654c4",
      "incomplete_value": false,
      "site": "005654c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056550c",
      "incomplete_value": false,
      "site": "0056550c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:cd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654cc",
      "incomplete_value": false,
      "site": "005654cc",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:8d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005654d4",
      "PARAM",
      [
        "storage",
        "00ca58a0",
        null,
        null
      ]
    ],
    [
      "005654dc",
      "PARAM",
      [
        "storage",
        "00560fa4",
        null,
        null
      ]
    ],
    [
      "005654e0",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005654d4",
      "PARAM",
      [
        "storage",
        "00ca5ca0",
        null,
        null
      ]
    ],
    [
      "005654dc",
      "PARAM",
      [
        "storage",
        "00560fe4",
        null,
        null
      ]
    ],
    [
      "005654e0",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056548c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md#insn-0056548c) · [`005654a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md#insn-005654a8) · [`005654d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md#insn-005654d8)
- 新版 [`005654cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-005654cc) · [`005654e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-005654e8) · [`00565518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/005654bc.md#insn-00565518)

~~~diff
- 0056548c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0056548c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056548c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056548c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005654cc ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 005654cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005654cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005654cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056548c bytes 73422e91
+ 005654cc bytes 73423e91
- 005654a8 ["INT_ADD", "register:40f0:8", ["const:5654a8:8", "const:4:8"]]
- 005654a8 ["CALL", null, ["callee:00c57e30:8"]]
+ 005654e8 ["INT_ADD", "register:40f0:8", ["const:5654e8:8", "const:4:8"]]
+ 005654e8 ["CALL", null, ["callee:00c57e30:8"]]
- 005654a8 bytes 62c91b94
+ 005654e8 bytes 52ca1b94
- 005654d8 ["INT_ADD", "register:40f0:8", ["const:5654d8:8", "const:4:8"]]
- 005654d8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00565518 ["INT_ADD", "register:40f0:8", ["const:565518:8", "const:4:8"]]
+ 00565518 ["CALL", null, ["callee:00c57e30:8"]]
- 005654d8 bytes 56c91b94
+ 00565518 bytes 46ca1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3cd9802eecdeb742b749c32629b9006"></a>

### [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) → [`00565a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md) FUN_00565a58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md) [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) · 呼出先 9件 [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md)
- 新版 呼出元 5件 [`0056897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/0056897c.md) [`005692bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005692bc.md) [`005694e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/005694e0.md) [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) [`0056a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a914.md) · 呼出先 9件 [`0056ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ca60.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md) [`0056d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d06c.md) [`0056d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d7d4.md) [`0056d97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d97c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00565c3c",
      "incomplete_value": true,
      "site": "00565c3c",
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
      "definition_site": "00565bfc",
      "incomplete_value": true,
      "site": "00565bfc",
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
      "00565c2c",
      "DATA",
      [
        "storage",
        "002c216c",
        null,
        null
      ]
    ],
    [
      "00565c44",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "00566654",
      "DATA",
      [
        "storage",
        "002d14e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00565c2c",
      "DATA",
      [
        "storage",
        "002c21ac",
        null,
        null
      ]
    ],
    [
      "00565c44",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "00566654",
      "DATA",
      [
        "storage",
        "002d1528",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md#insn-00565a64) · [`00565b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md#insn-00565b74) · [`00565bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md#insn-00565bd4)
- 新版 [`00565aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565aa4) · [`00565bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565bb4) · [`00565c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565a58.md#insn-00565c14)

~~~diff
- 00565a64 ["INT_ADD", "register:40f0:8", ["const:565a64:8", "const:4:8"]]
- 00565a64 ["CALL", null, ["callee:0056ca60:8"]]
+ 00565aa4 ["INT_ADD", "register:40f0:8", ["const:565aa4:8", "const:4:8"]]
+ 00565aa4 ["CALL", null, ["callee:0056ca60:8"]]
- 00565a64 bytes ef1b0094
+ 00565aa4 bytes ef1b0094
- 00565b74 ["INT_ADD", "register:40f0:8", ["const:565b74:8", "const:4:8"]]
- 00565b74 ["CALL", null, ["callee:0056d06c:8"]]
+ 00565bb4 ["INT_ADD", "register:40f0:8", ["const:565bb4:8", "const:4:8"]]
+ 00565bb4 ["CALL", null, ["callee:0056d06c:8"]]
- 00565b74 bytes 2e1d0094
+ 00565bb4 bytes 2e1d0094
- 00565bd4 ["COPY", "tmp:0:8", ["const:170:8"]]
- 00565bd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565bd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565bd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00565c14 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00565c14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00565c14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00565c14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565bd4 bytes 29c10591
+ 00565c14 bytes 29c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e77c80f16d244b0d4d9e8e897bccf350"></a>

### [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) → [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) FUN_00566c00

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) · 呼出先 28件 [`005658dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005658dc.md) [`005688e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md) [`00569f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md) [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md)
- 新版 呼出元 1件 [`0056a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a174.md) · 呼出先 28件 [`0056591c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/0056591c.md) [`00568928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00568/00568928.md) [`00569f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569f74.md) [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`0056ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056ce4c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.73% / 新版 99.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567ab8",
      "incomplete_value": true,
      "site": "00567ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567a78",
      "incomplete_value": true,
      "site": "00567a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056706c",
      "value": [
        "leaf",
        "ram:56f6b0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056702c",
      "value": [
        "leaf",
        "ram:56f670:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567640",
      "value": [
        "leaf",
        "ram:56f774:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567600",
      "value": [
        "leaf",
        "ram:56f734:8"
      ]
    },
    "ordinal": 75,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00566d24",
      "READ",
      [
        "storage",
        "00ca39f4",
        null,
        "string"
      ]
    ],
    [
      "00566d2c",
      "READ",
      [
        "storage",
        "00ca39f8",
        null,
        "string"
      ]
    ],
    [
      "00566ed0",
      "READ",
      [
        "storage",
        "00ca39f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00566d24",
      "READ",
      [
        "storage",
        "00ca3df4",
        null,
        "string"
      ]
    ],
    [
      "00566d2c",
      "READ",
      [
        "storage",
        "00ca3df8",
        null,
        "string"
      ]
    ],
    [
      "00566ed0",
      "READ",
      [
        "storage",
        "00ca3df4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056702c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md#insn-0056702c) · [`00567600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md#insn-00567600) · [`00567d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md#insn-00567d24)
- 新版 [`0056706c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-0056706c) · [`00567640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-00567640) · [`00567d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md#insn-00567d64)

~~~diff
- 0056702c ["INT_ADD", "register:40f0:8", ["const:56702c:8", "const:4:8"]]
- 0056702c ["CALL", null, ["ram:56f670:8"]]
+ 0056706c ["INT_ADD", "register:40f0:8", ["const:56706c:8", "const:4:8"]]
+ 0056706c ["CALL", null, ["ram:56f6b0:8"]]
- 0056702c bytes 91210094
+ 0056706c bytes 91210094
- 00567600 ["INT_ADD", "register:40f0:8", ["const:567600:8", "const:4:8"]]
- 00567600 ["CALL", null, ["ram:56f734:8"]]
+ 00567640 ["INT_ADD", "register:40f0:8", ["const:567640:8", "const:4:8"]]
+ 00567640 ["CALL", null, ["ram:56f774:8"]]
- 00567600 bytes 4d200094
+ 00567640 bytes 4d200094
- 00567d24 ["INT_ADD", "register:40f0:8", ["const:567d24:8", "const:4:8"]]
- 00567d24 ["CALL", null, ["callee:00c5a040:8"]]
+ 00567d64 ["INT_ADD", "register:40f0:8", ["const:567d64:8", "const:4:8"]]
+ 00567d64 ["CALL", null, ["callee:00c5a040:8"]]
- 00567d24 bytes c7c71b94
+ 00567d64 bytes b7c81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8011ae9dd22ccc8a046d88ba67274869"></a>

### [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) → [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) FUN_0056ab68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) · 呼出先 11件 [`0056af2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md) [`0056af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md) [`0056b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md) [`00570df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570df8.md) [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md)
- 新版 呼出元 1件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) · 呼出先 11件 [`0056af6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056af6c.md) [`0056afdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056afdc.md) [`0056b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md) [`00570e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e38.md) [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.63% / 新版 82.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 12件, `call_target` 4件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056acb0",
      "incomplete_value": false,
      "site": "0056acbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ac70",
      "incomplete_value": false,
      "site": "0056ac7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "definition_site": "0056ad2c",
      "incomplete_value": false,
      "site": "0056ad2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056acec",
      "incomplete_value": false,
      "site": "0056acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056ade0",
      "incomplete_value": false,
      "site": "0056ade0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ada0",
      "incomplete_value": false,
      "site": "0056ada0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056ab98",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abb0",
      "PARAM",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abd4",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056ab98",
      "READ",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abb0",
      "PARAM",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056abd4",
      "READ",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ab8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md#insn-0056ab8c) · [`0056aba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md#insn-0056aba4) · [`0056abb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md#insn-0056abb8)
- 新版 [`0056abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abcc) · [`0056abe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abe4) · [`0056abf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md#insn-0056abf8)

~~~diff
- 0056ab8c ["INT_ADD", "register:40f0:8", ["const:56ab8c:8", "const:4:8"]]
- 0056ab8c ["CALL", null, ["callee:00c5a0b0:8"]]
+ 0056abcc ["INT_ADD", "register:40f0:8", ["const:56abcc:8", "const:4:8"]]
+ 0056abcc ["CALL", null, ["callee:00c5a0b0:8"]]
- 0056ab8c bytes 49bc1b94
+ 0056abcc bytes 39bd1b94
- 0056aba4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056aba4 ["INT_ADD", "register:40f0:8", ["const:56aba4:8", "const:4:8"]]
- 0056aba4 ["CALLIND", null, ["register:0:8"]]
+ 0056abe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056abe4 ["INT_ADD", "register:40f0:8", ["const:56abe4:8", "const:4:8"]]
+ 0056abe4 ["CALLIND", null, ["register:0:8"]]
- 0056aba4 bytes 00013fd6
+ 0056abe4 bytes 00013fd6
- 0056abb8 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0056abb8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0056abb8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0056abb8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0056abf8 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 0056abf8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0056abf8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0056abf8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0056abb8 bytes 42402591
+ 0056abf8 bytes 42403591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9900f3c2b611521da005c100256a8b"></a>

### [`0056b1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md) → [`0056b23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md) FUN_0056b23c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056b258",
      "incomplete_value": true,
      "site": "0056b25c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056b218",
      "incomplete_value": true,
      "site": "0056b21c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "0056b254",
      "READ",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b254",
      "READ",
      [
        "storage",
        "00ca5920",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b2a0",
      "READ",
      [
        "storage",
        "00ca5930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056b254",
      "READ",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b254",
      "READ",
      [
        "storage",
        "00ca5d20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b2a0",
      "READ",
      [
        "storage",
        "00ca5d30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md#insn-0056b25c) · [`0056b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md#insn-0056b210) · [`0056b244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md#insn-0056b244)
- 新版 [`0056b29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b29c) · [`0056b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b250) · [`0056b284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md#insn-0056b284)

~~~diff
- 0056b25c ["COPY", "tmp:0:8", ["const:930:8"]]
- 0056b25c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b25c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b25c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b29c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0056b29c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b29c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b29c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b25c bytes 08c12491
+ 0056b29c bytes 08c13491
- 0056b210 ["COPY", "tmp:0:8", ["const:918:8"]]
- 0056b210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b250 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0056b250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b210 bytes 08612491
+ 0056b250 bytes 08613491
- 0056b244 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b244 ["INT_ADD", "register:40f0:8", ["const:56b244:8", "const:4:8"]]
- 0056b244 ["CALLIND", null, ["register:0:8"]]
+ 0056b284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b284 ["INT_ADD", "register:40f0:8", ["const:56b284:8", "const:4:8"]]
+ 0056b284 ["CALLIND", null, ["register:0:8"]]
- 0056b244 bytes 00013fd6
+ 0056b284 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a18e46e58bdbfe0ded0c2d3225e49a2"></a>

### [`0056b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md) → [`0056b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md) FUN_0056b2f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 3件 [`0056b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b5d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cc0.md)
- 新版 呼出元 1件 [`0056ab68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056ab68.md) · 呼出先 3件 [`0056b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b614.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b330",
      "incomplete_value": false,
      "site": "0056b334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b2f0",
      "incomplete_value": false,
      "site": "0056b2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "definition_site": "0056b3ac",
      "incomplete_value": true,
      "site": "0056b3b4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:4cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b36c",
      "incomplete_value": true,
      "site": "0056b374",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:48c:8"
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
      "definition_site": "0056b3b8",
      "incomplete_value": true,
      "site": "0056b3d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b378",
      "incomplete_value": true,
      "site": "0056b390",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b334",
      "DATA",
      [
        "storage",
        "00c6b2f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b360",
      "READ",
      [
        "storage",
        "00ca5958",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b3ac",
      "READ",
      [
        "storage",
        "002d148c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056b334",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b360",
      "READ",
      [
        "storage",
        "00ca5d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b3ac",
      "READ",
      [
        "storage",
        "002d14cc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md#insn-0056b3a4) · [`0056b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md#insn-0056b3b4) · [`0056b3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md#insn-0056b3cc)
- 新版 [`0056b3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b3e4) · [`0056b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b3f4) · [`0056b40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b2f4.md#insn-0056b40c)

~~~diff
- 0056b3a4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0056b3e4 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0056b3a4 bytes 693900f0
+ 0056b3e4 bytes 89390090
- 0056b3b4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:eb0:8"]]
- 0056b3b4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056b3f4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2b0:8"]]
+ 0056b3f4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0056b3b4 bytes 4a5947f9
+ 0056b3f4 bytes 4a5941f9
- 0056b3cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb8:8"]]
- 0056b3cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056b40c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
+ 0056b40c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0056b3cc bytes 085d47f9
+ 0056b40c bytes 085d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5188ffcdb60318bd0f4f4fad9f94c0f"></a>

### [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) → [`0056b79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md) FUN_0056b79c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00570df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570df8.md) · 呼出先 8件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`00570e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e38.md) · 呼出先 8件 [`00565584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00565/00565584.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b7b4",
      "incomplete_value": false,
      "site": "0056b7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b774",
      "incomplete_value": false,
      "site": "0056b778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056b808",
      "incomplete_value": false,
      "site": "0056b808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b7c8",
      "incomplete_value": false,
      "site": "0056b7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "0056b7b8",
      "DATA",
      [
        "storage",
        "00c6b2f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b800",
      "READ",
      [
        "storage",
        "00ca5960",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b808",
      "WRITE",
      [
        "storage",
        "00ca5960",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056b7b8",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b800",
      "READ",
      [
        "storage",
        "00ca5d60",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b808",
      "WRITE",
      [
        "storage",
        "00ca5d60",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md#insn-0056b7b8) · [`0056b7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md#insn-0056b7c8) · [`0056b774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md#insn-0056b774)
- 新版 [`0056b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b7f8) · [`0056b808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b808) · [`0056b7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b79c.md#insn-0056b7b4)

~~~diff
- 0056b7b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b7b8 ["INT_ADD", "register:40f0:8", ["const:56b7b8:8", "const:4:8"]]
- 0056b7b8 ["CALLIND", null, ["register:0:8"]]
+ 0056b7f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b7f8 ["INT_ADD", "register:40f0:8", ["const:56b7f8:8", "const:4:8"]]
+ 0056b7f8 ["CALLIND", null, ["register:0:8"]]
- 0056b7b8 bytes 00013fd6
+ 0056b7f8 bytes 00013fd6
- 0056b7c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
- 0056b7c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0056b808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
+ 0056b808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0056b7c8 bytes 096109b9
+ 0056b808 bytes 09610db9
- 0056b774 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0056b774 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056b774 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056b774 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056b7b4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 0056b7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056b774 bytes 29c10b91
+ 0056b7b4 bytes 29c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5f246b85f874f316e2f268a204116a"></a>

### [`0056c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md) → [`0056c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md) FUN_0056c4fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0056c6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6fc.md) [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) · 呼出先 8件 [`0056bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md) [`00c533d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c533d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0056c73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c73c.md) [`0056c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c740.md) · 呼出先 8件 [`0056bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056bcf4.md) [`00c537f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c537f0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056c66c",
      "incomplete_value": false,
      "site": "0056c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c62c",
      "incomplete_value": false,
      "site": "0056c62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "definition_site": "0056c538",
      "incomplete_value": true,
      "site": "0056c53c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056c4f8",
      "incomplete_value": true,
      "site": "0056c4fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "LOAD"
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
      "definition_site": "0056c5a0",
      "incomplete_value": false,
      "site": "0056c5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c560",
      "incomplete_value": false,
      "site": "0056c56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "0056c534",
      "READ",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c534",
      "READ",
      [
        "storage",
        "00ca5920",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c5a0",
      "PARAM",
      [
        "storage",
        "00c6b478",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056c534",
      "READ",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c534",
      "READ",
      [
        "storage",
        "00ca5d20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c5a0",
      "PARAM",
      [
        "storage",
        "00c6b878",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md#insn-0056c56c) · [`0056c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md#insn-0056c4f0) · [`0056c540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md#insn-0056c540)
- 新版 [`0056c5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c5ac) · [`0056c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c530) · [`0056c580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056c4fc.md#insn-0056c580)

~~~diff
- 0056c56c ["INT_ADD", "register:40f0:8", ["const:56c56c:8", "const:4:8"]]
- 0056c56c ["CALL", null, ["callee:00c58610:8"]]
+ 0056c5ac ["INT_ADD", "register:40f0:8", ["const:56c5ac:8", "const:4:8"]]
+ 0056c5ac ["CALL", null, ["callee:00c58610:8"]]
- 0056c56c bytes 29af1b94
+ 0056c5ac bytes 19b01b94
- 0056c4f0 ["COPY", "tmp:0:8", ["const:918:8"]]
- 0056c4f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c4f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c530 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0056c530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c4f0 bytes 08612491
+ 0056c530 bytes 08613491
- 0056c540 ["INT_ADD", "register:40f0:8", ["const:56c540:8", "const:4:8"]]
- 0056c540 ["CALL", null, ["callee:00c537f0:8"]]
+ 0056c580 ["INT_ADD", "register:40f0:8", ["const:56c580:8", "const:4:8"]]
+ 0056c580 ["CALL", null, ["callee:00c537f0:8"]]
- 0056c540 bytes a49b1b94
+ 0056c580 bytes 9c9c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bfb0bcd34e43856621e7ad6df6cf808"></a>

### [`0056cf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056cf38.md) → [`0056cf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md) FUN_0056cf78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.05% / 新版 77.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0056cf94",
      "incomplete_value": true,
      "site": "0056cf98",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "definition_site": "0056cf54",
      "incomplete_value": true,
      "site": "0056cf58",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "0056cf94",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "0056cfc4",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "0056cfe8",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056cf94",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "0056cfc4",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ],
    [
      "0056cfe8",
      "DATA",
      [
        "storage",
        "002c30e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056cf38.md#insn-0056cf50) · [`0056cf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056cf38.md#insn-0056cf7c) · [`0056cfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056cf38.md#insn-0056cfa0)
- 新版 [`0056cf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cf90) · [`0056cfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cfbc) · [`0056cfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056c/0056cf78.md#insn-0056cfe0)

~~~diff
- 0056cf50 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0056cf50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056cf50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056cf50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056cf90 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0056cf90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cf90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cf90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056cf50 bytes 08810291
+ 0056cf90 bytes 08810391
- 0056cf7c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0056cf7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056cf7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056cf7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056cfbc ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0056cfbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cfbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cfbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056cf7c bytes 29810291
+ 0056cfbc bytes 29810391
- 0056cfa0 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 0056cfa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056cfa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056cfe0 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0056cfe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cfe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056cfe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056cfa0 bytes 29810291
+ 0056cfe0 bytes 29810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a83055b4d864fb5b9dee538c70817b12"></a>

### [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) → [`0056d438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md) FUN_0056d438

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) · 呼出先 5件 [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)
- 新版 呼出元 2件 [`00569334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00569/00569334.md) [`0056d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d2e0.md) · 呼出先 5件 [`0056a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056a010.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a050.md) [`00c5a070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a070.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056d67c",
      "incomplete_value": true,
      "site": "0056d680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056d63c",
      "incomplete_value": true,
      "site": "0056d640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd8:8"
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
      "0056d67c",
      "READ",
      [
        "storage",
        "002c3fd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056d67c",
      "READ",
      [
        "storage",
        "002c4018",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md#insn-0056d480) · [`0056d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md#insn-0056d4a0) · [`0056d4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md#insn-0056d4d8)
- 新版 [`0056d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d4c0) · [`0056d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d4e0) · [`0056d518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056d/0056d438.md#insn-0056d518)

~~~diff
- 0056d480 ["INT_ADD", "register:40f0:8", ["const:56d480:8", "const:4:8"]]
- 0056d480 ["CALL", null, ["callee:00c5a050:8"]]
+ 0056d4c0 ["INT_ADD", "register:40f0:8", ["const:56d4c0:8", "const:4:8"]]
+ 0056d4c0 ["CALL", null, ["callee:00c5a050:8"]]
- 0056d480 bytes f4b11b94
+ 0056d4c0 bytes e4b21b94
- 0056d4a0 ["INT_ADD", "register:40f0:8", ["const:56d4a0:8", "const:4:8"]]
- 0056d4a0 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d4e0 ["INT_ADD", "register:40f0:8", ["const:56d4e0:8", "const:4:8"]]
+ 0056d4e0 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d4a0 bytes f4b11b94
+ 0056d4e0 bytes e4b21b94
- 0056d4d8 ["INT_ADD", "register:40f0:8", ["const:56d4d8:8", "const:4:8"]]
- 0056d4d8 ["CALL", null, ["callee:00c5a070:8"]]
+ 0056d518 ["INT_ADD", "register:40f0:8", ["const:56d518:8", "const:4:8"]]
+ 0056d518 ["CALL", null, ["callee:00c5a070:8"]]
- 0056d4d8 bytes e6b11b94
+ 0056d518 bytes d6b21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e73c8880fb4a6c65217a902366cb36f"></a>

### [`0056fd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md) → [`0056fda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md) FUN_0056fda0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fe0.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d20.md)
- 新版 呼出元 1件 [`00566c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00566/00566c00.md) · 呼出先 3件 [`00c583e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583e0.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00570080",
      "incomplete_value": true,
      "site": "00570084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570040",
      "incomplete_value": true,
      "site": "00570044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:350:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00570088",
      "incomplete_value": true,
      "site": "0057008c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:170:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570048",
      "incomplete_value": true,
      "site": "0057004c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:130:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005702cc",
      "incomplete_value": true,
      "site": "005702d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057028c",
      "incomplete_value": true,
      "site": "00570290",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056ff80",
      "READ",
      [
        "storage",
        "002c43b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00570080",
      "READ",
      [
        "storage",
        "002c2350",
        null,
        null
      ]
    ],
    [
      "00570088",
      "READ",
      [
        "storage",
        "002c3130",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056ff80",
      "READ",
      [
        "storage",
        "002c43f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00570080",
      "READ",
      [
        "storage",
        "002c2390",
        null,
        null
      ]
    ],
    [
      "00570088",
      "READ",
      [
        "storage",
        "002c3170",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056fde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md#insn-0056fde4) · [`0056fe00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md#insn-0056fe00) · [`0056feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md#insn-0056feb0)
- 新版 [`0056fe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fe24) · [`0056fe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fe40) · [`0056fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056f/0056fda0.md#insn-0056fef0)

~~~diff
- 0056fde4 ["INT_ADD", "register:40f0:8", ["const:56fde4:8", "const:4:8"]]
- 0056fde4 ["CALL", null, ["callee:00c5a020:8"]]
+ 0056fe24 ["INT_ADD", "register:40f0:8", ["const:56fe24:8", "const:4:8"]]
+ 0056fe24 ["CALL", null, ["callee:00c5a020:8"]]
- 0056fde4 bytes 8fa71b94
+ 0056fe24 bytes 7fa81b94
- 0056fe00 ["INT_ADD", "register:40f0:8", ["const:56fe00:8", "const:4:8"]]
- 0056fe00 ["CALL", null, ["callee:00c5a020:8"]]
+ 0056fe40 ["INT_ADD", "register:40f0:8", ["const:56fe40:8", "const:4:8"]]
+ 0056fe40 ["CALL", null, ["callee:00c5a020:8"]]
- 0056fe00 bytes 88a71b94
+ 0056fe40 bytes 78a81b94
- 0056feb0 ["INT_ADD", "register:40f0:8", ["const:56feb0:8", "const:4:8"]]
- 0056feb0 ["CALL", null, ["callee:00c5a020:8"]]
+ 0056fef0 ["INT_ADD", "register:40f0:8", ["const:56fef0:8", "const:4:8"]]
+ 0056fef0 ["CALL", null, ["callee:00c5a020:8"]]
- 0056feb0 bytes 5ca71b94
+ 0056fef0 bytes 4ca81b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a7f927b2f2c55f61d6c6e5531daaac"></a>

### [`00570db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570db8.md) → [`00570df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570df8.md) FUN_00570df8

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
      "definition_site": "00570dfc",
      "incomplete_value": false,
      "site": "00570e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570dbc",
      "incomplete_value": false,
      "site": "00570dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00570e00",
      "DATA",
      [
        "storage",
        "00c6b438",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00570e00",
      "DATA",
      [
        "storage",
        "00c6b838",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570db8.md#insn-00570dbc)
- 新版 [`00570dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570df8.md#insn-00570dfc)

~~~diff
- 00570dbc ["COPY", "tmp:0:8", ["const:438:8"]]
- 00570dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570dfc ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00570dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570dbc bytes 08e11091
+ 00570dfc bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd069d37a2c00170a7d65b337b5ea000"></a>

### [`00570dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570dc8.md) → [`00570e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md) FUN_00570e08

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
      "definition_site": "00570e18",
      "incomplete_value": false,
      "site": "00570e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570dd8",
      "incomplete_value": false,
      "site": "00570de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00570e20",
      "DATA",
      [
        "storage",
        "00c6b438",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00570e20",
      "DATA",
      [
        "storage",
        "00c6b838",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570dc8.md#insn-00570dd8) · [`00570de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570dc8.md#insn-00570de4)
- 新版 [`00570e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md#insn-00570e18) · [`00570e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e08.md#insn-00570e24)

~~~diff
- 00570dd8 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00570dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570e18 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00570e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570dd8 bytes 08e11091
+ 00570e18 bytes 08e12091
- 00570de4 ["INT_ADD", "register:40f0:8", ["const:570de4:8", "const:4:8"]]
- 00570de4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00570e24 ["INT_ADD", "register:40f0:8", ["const:570e24:8", "const:4:8"]]
+ 00570e24 ["CALL", null, ["callee:00c57ea0:8"]]
- 00570de4 bytes 2f9b1b94
+ 00570e24 bytes 1f9c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af432339931638dc6f9821ee424a4ed9"></a>

### [`00570f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md) → [`00570fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md) FUN_00570fa0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00570e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570e44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00570fac",
      "incomplete_value": true,
      "site": "00570fb0",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570f6c",
      "incomplete_value": true,
      "site": "00570f70",
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
      "00570fac",
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
      "00570fac",
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

- 旧版 [`00570f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md#insn-00570f70) · [`00570f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md#insn-00570f6c)
- 新版 [`00570fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md#insn-00570fb0) · [`00570fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fa0.md#insn-00570fac)

~~~diff
- 00570f70 ["INT_ADD", "register:40f0:8", ["const:570f70:8", "const:4:8"]]
- 00570f70 ["CALL", null, ["callee:0043b778:8"]]
+ 00570fb0 ["INT_ADD", "register:40f0:8", ["const:570fb0:8", "const:4:8"]]
+ 00570fb0 ["CALL", null, ["callee:0043b778:8"]]
- 00570f70 bytes f229fb97
+ 00570fb0 bytes f229fb97
- 00570f6c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00570f6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00570f6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00570f6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00570fac ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00570fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00570fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00570fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00570f6c bytes 00303c91
+ 00570fac bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1612556c5cf2f7e2d8f2fece1e7798e7"></a>

### [`00570f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f74.md) → [`00570fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md) FUN_00570fb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00570fcc",
      "incomplete_value": false,
      "site": "00570fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570f8c",
      "incomplete_value": false,
      "site": "00570f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "00570fd0",
      "DATA",
      [
        "storage",
        "00c6b4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00570fd0",
      "DATA",
      [
        "storage",
        "00c6b8a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f74.md#insn-00570f8c) · [`00570fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f74.md#insn-00570fa0) · [`00570fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f74.md#insn-00570fb4)
- 新版 [`00570fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570fcc) · [`00570fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570fe0) · [`00570ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00570/00570fb4.md#insn-00570ff4)

~~~diff
- 00570f8c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00570f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570fcc ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00570fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570f8c bytes 08811291
+ 00570fcc bytes 08812291
- 00570fa0 ["INT_ADD", "register:40f0:8", ["const:570fa0:8", "const:4:8"]]
- 00570fa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00570fe0 ["INT_ADD", "register:40f0:8", ["const:570fe0:8", "const:4:8"]]
+ 00570fe0 ["CALL", null, ["callee:00c53d00:8"]]
- 00570fa0 bytes 508a1b94
+ 00570fe0 bytes 488b1b94
- 00570fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00570fb4 ["INT_ADD", "register:40f0:8", ["const:570fb4:8", "const:4:8"]]
- 00570fb4 ["CALLIND", null, ["register:0:8"]]
+ 00570ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00570ff4 ["INT_ADD", "register:40f0:8", ["const:570ff4:8", "const:4:8"]]
+ 00570ff4 ["CALLIND", null, ["register:0:8"]]
- 00570fb4 bytes 00013fd6
+ 00570ff4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c646c686ca2a69efc0d5d2f65372a9d"></a>

### [`00570fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570fd0.md) → [`00571010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md) FUN_00571010

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571028",
      "incomplete_value": false,
      "site": "0057102c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570fe8",
      "incomplete_value": false,
      "site": "00570fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "0057102c",
      "DATA",
      [
        "storage",
        "00c6b4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057102c",
      "DATA",
      [
        "storage",
        "00c6b8a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570fd0.md#insn-00570fe8) · [`00570ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570fd0.md#insn-00570ffc) · [`00571010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570fd0.md#insn-00571010)
- 新版 [`00571028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-00571028) · [`0057103c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-0057103c) · [`00571050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571010.md#insn-00571050)

~~~diff
- 00570fe8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00570fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571028 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00571028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570fe8 bytes 08811291
+ 00571028 bytes 08812291
- 00570ffc ["INT_ADD", "register:40f0:8", ["const:570ffc:8", "const:4:8"]]
- 00570ffc ["CALL", null, ["callee:00c53d00:8"]]
+ 0057103c ["INT_ADD", "register:40f0:8", ["const:57103c:8", "const:4:8"]]
+ 0057103c ["CALL", null, ["callee:00c53d00:8"]]
- 00570ffc bytes 398a1b94
+ 0057103c bytes 318b1b94
- 00571010 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571010 ["INT_ADD", "register:40f0:8", ["const:571010:8", "const:4:8"]]
- 00571010 ["CALLIND", null, ["register:0:8"]]
+ 00571050 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571050 ["INT_ADD", "register:40f0:8", ["const:571050:8", "const:4:8"]]
+ 00571050 ["CALLIND", null, ["register:0:8"]]
- 00571010 bytes 00013fd6
+ 00571050 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-157ace3357ccb3f1912393878343bd4e"></a>

### [`005710b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005710b4.md) → [`005710f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md) FUN_005710f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0057110c",
      "incomplete_value": false,
      "site": "00571110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005710cc",
      "incomplete_value": false,
      "site": "005710d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "00571110",
      "DATA",
      [
        "storage",
        "00c6b4f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571110",
      "DATA",
      [
        "storage",
        "00c6b8f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005710cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005710b4.md#insn-005710cc) · [`005710e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005710b4.md#insn-005710e0) · [`005710f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005710b4.md#insn-005710f4)
- 新版 [`0057110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-0057110c) · [`00571120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-00571120) · [`00571134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005710f4.md#insn-00571134)

~~~diff
- 005710cc ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 005710cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005710cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005710cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057110c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 0057110c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057110c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057110c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005710cc bytes 08c11391
+ 0057110c bytes 08c12391
- 005710e0 ["INT_ADD", "register:40f0:8", ["const:5710e0:8", "const:4:8"]]
- 005710e0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00571120 ["INT_ADD", "register:40f0:8", ["const:571120:8", "const:4:8"]]
+ 00571120 ["CALL", null, ["callee:00c53d00:8"]]
- 005710e0 bytes 008a1b94
+ 00571120 bytes f88a1b94
- 005710f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005710f4 ["INT_ADD", "register:40f0:8", ["const:5710f4:8", "const:4:8"]]
- 005710f4 ["CALLIND", null, ["register:0:8"]]
+ 00571134 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571134 ["INT_ADD", "register:40f0:8", ["const:571134:8", "const:4:8"]]
+ 00571134 ["CALLIND", null, ["register:0:8"]]
- 005710f4 bytes 00013fd6
+ 00571134 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331e2d529865e7bca5e0ba9b7ae47fec"></a>

### [`00571110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571110.md) → [`00571150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md) FUN_00571150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571168",
      "incomplete_value": false,
      "site": "0057116c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571128",
      "incomplete_value": false,
      "site": "0057112c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0057116c",
      "DATA",
      [
        "storage",
        "00c6b4f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057116c",
      "DATA",
      [
        "storage",
        "00c6b8f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571110.md#insn-00571128) · [`0057113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571110.md#insn-0057113c) · [`00571150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571110.md#insn-00571150)
- 新版 [`00571168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-00571168) · [`0057117c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-0057117c) · [`00571190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571150.md#insn-00571190)

~~~diff
- 00571128 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 00571128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571168 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00571168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571128 bytes 08c11391
+ 00571168 bytes 08c12391
- 0057113c ["INT_ADD", "register:40f0:8", ["const:57113c:8", "const:4:8"]]
- 0057113c ["CALL", null, ["callee:00c53d00:8"]]
+ 0057117c ["INT_ADD", "register:40f0:8", ["const:57117c:8", "const:4:8"]]
+ 0057117c ["CALL", null, ["callee:00c53d00:8"]]
- 0057113c bytes e9891b94
+ 0057117c bytes e18a1b94
- 00571150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00571150 ["INT_ADD", "register:40f0:8", ["const:571150:8", "const:4:8"]]
- 00571150 ["CALLIND", null, ["register:0:8"]]
+ 00571190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571190 ["INT_ADD", "register:40f0:8", ["const:571190:8", "const:4:8"]]
+ 00571190 ["CALLIND", null, ["register:0:8"]]
- 00571150 bytes 00013fd6
+ 00571190 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d7a09f38cd2ae7160b641a696cdf231"></a>

### [`005711f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005711f4.md) → [`00571234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571234.md) FUN_00571234

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
      "definition_site": "00571238",
      "incomplete_value": false,
      "site": "0057123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005711f8",
      "incomplete_value": false,
      "site": "005711fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "0057123c",
      "DATA",
      [
        "storage",
        "00c6b540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057123c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005711f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005711f4.md#insn-005711f8)
- 新版 [`00571238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571234.md#insn-00571238)

~~~diff
- 005711f8 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005711f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005711f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005711f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571238 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00571238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005711f8 bytes 08011591
+ 00571238 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c72a3d228ffb4979885a00708fa22f17"></a>

### [`00571204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571204.md) → [`00571244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md) FUN_00571244

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
      "definition_site": "00571254",
      "incomplete_value": false,
      "site": "0057125c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571214",
      "incomplete_value": false,
      "site": "0057121c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "0057125c",
      "DATA",
      [
        "storage",
        "00c6b540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057125c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571204.md#insn-00571214) · [`00571220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571204.md#insn-00571220)
- 新版 [`00571254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md#insn-00571254) · [`00571260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571244.md#insn-00571260)

~~~diff
- 00571214 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00571214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571254 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00571254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571214 bytes 08011591
+ 00571254 bytes 08012591
- 00571220 ["INT_ADD", "register:40f0:8", ["const:571220:8", "const:4:8"]]
- 00571220 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00571260 ["INT_ADD", "register:40f0:8", ["const:571260:8", "const:4:8"]]
+ 00571260 ["CALL", null, ["callee:00c57ea0:8"]]
- 00571220 bytes 209a1b94
+ 00571260 bytes 109b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c997dd18a30115612c8a20d8a517f4a2"></a>

### [`00571244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md) → [`00571284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md) _INIT_28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056a/0056aad0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712b0",
      "incomplete_value": false,
      "site": "005712b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571270",
      "incomplete_value": false,
      "site": "00571270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712b0",
      "incomplete_value": false,
      "site": "005712b0",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:d18:8"
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
      "definition_site": "00571270",
      "incomplete_value": false,
      "site": "00571270",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:918:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005712b4",
      "incomplete_value": false,
      "site": "005712b4",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:d18:8"
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
      "definition_site": "00571274",
      "incomplete_value": false,
      "site": "00571274",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:918:8"
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005712a4",
      "PARAM",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "005712a8",
      "PARAM",
      [
        "storage",
        "0056aa90",
        null,
        null
      ]
    ],
    [
      "005712ac",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005712a4",
      "PARAM",
      [
        "storage",
        "00ca5d18",
        null,
        "undefined8"
      ]
    ],
    [
      "005712a8",
      "PARAM",
      [
        "storage",
        "0056aad0",
        null,
        null
      ]
    ],
    [
      "005712ac",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md#insn-00571278) · [`00571254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md#insn-00571254) · [`0057125c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md#insn-0057125c)
- 新版 [`005712b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-005712b8) · [`00571294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-00571294) · [`0057129c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571284.md#insn-0057129c)

~~~diff
- 00571278 ["INT_ADD", "register:40f0:8", ["const:571278:8", "const:4:8"]]
- 00571278 ["CALL", null, ["callee:00c57e30:8"]]
+ 005712b8 ["INT_ADD", "register:40f0:8", ["const:5712b8:8", "const:4:8"]]
+ 005712b8 ["CALL", null, ["callee:00c57e30:8"]]
- 00571278 bytes ee991b94
+ 005712b8 bytes de9a1b94
- 00571254 ["COPY", "register:4098:8", ["const:56aa90:8"]]
+ 00571294 ["COPY", "register:4098:8", ["const:56aad0:8"]]
- 00571254 bytes f3c1fc10
+ 00571294 bytes f3c1fc10
- 0057125c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0057125c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0057125c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0057125c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0057129c ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0057129c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0057129c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0057129c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0057125c bytes 94422e91
+ 0057129c bytes 94423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d49d171e23c51bb659629c0847b8979"></a>

### [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) → [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) FUN_005712e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0057481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md)
- 新版 呼出元 3件 [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0057485c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571368",
      "incomplete_value": true,
      "site": "00571368",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:29d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571328",
      "incomplete_value": true,
      "site": "00571328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
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
      "definition_site": "005713d0",
      "incomplete_value": true,
      "site": "005713d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571390",
      "incomplete_value": true,
      "site": "00571390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c91:8"
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
      "definition_site": "0057149c",
      "incomplete_value": true,
      "site": "0057149c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057145c",
      "incomplete_value": true,
      "site": "0057145c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:daa:8"
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
      "00571358",
      "READ",
      [
        "storage",
        "002a31d0",
        null,
        "string"
      ]
    ],
    [
      "005713b8",
      "READ",
      [
        "storage",
        "002b2c91",
        null,
        "string"
      ]
    ],
    [
      "0057148c",
      "READ",
      [
        "storage",
        "002b1daa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00571358",
      "READ",
      [
        "storage",
        "002a329d",
        null,
        "string"
      ]
    ],
    [
      "005713b8",
      "READ",
      [
        "storage",
        "002b2cd1",
        null,
        "string"
      ]
    ],
    [
      "0057148c",
      "READ",
      [
        "storage",
        "002b1dea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005712e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md#insn-005712e8) · [`00571368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md#insn-00571368) · [`005713d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md#insn-005713d0)
- 新版 [`00571328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-00571328) · [`005713a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-005713a8) · [`00571410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md#insn-00571410)

~~~diff
- 005712e8 ["INT_ADD", "register:40f0:8", ["const:5712e8:8", "const:4:8"]]
- 005712e8 ["CALL", null, ["callee:00596f2c:8"]]
+ 00571328 ["INT_ADD", "register:40f0:8", ["const:571328:8", "const:4:8"]]
+ 00571328 ["CALL", null, ["callee:00596f2c:8"]]
- 005712e8 bytes 01970094
+ 00571328 bytes 01970094
- 00571368 ["INT_ADD", "register:40f0:8", ["const:571368:8", "const:4:8"]]
- 00571368 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005713a8 ["INT_ADD", "register:40f0:8", ["const:5713a8:8", "const:4:8"]]
+ 005713a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00571368 bytes d2991b94
+ 005713a8 bytes c29a1b94
- 005713d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005713d0 ["INT_ADD", "register:40f0:8", ["const:5713d0:8", "const:4:8"]]
- 005713d0 ["CALLIND", null, ["register:0:8"]]
+ 00571410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00571410 ["INT_ADD", "register:40f0:8", ["const:571410:8", "const:4:8"]]
+ 00571410 ["CALLIND", null, ["register:0:8"]]
- 005713d0 bytes 00013fd6
+ 00571410 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06434e19df5887fdd440644a4019685"></a>

### [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) → [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) FUN_00571af4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550950.md) · 呼出先 15件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00550990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550990.md) · 呼出先 15件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.03% / 新版 95.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571cac",
      "incomplete_value": true,
      "site": "00571cac",
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
      "definition_site": "00571c6c",
      "incomplete_value": true,
      "site": "00571c6c",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571cdc",
      "incomplete_value": true,
      "site": "00571cdc",
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
      "definition_site": "00571c9c",
      "incomplete_value": true,
      "site": "00571c9c",
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
      "00571b70",
      "READ",
      [
        "storage",
        "002bda3e",
        null,
        "string"
      ]
    ],
    [
      "00571b70",
      "READ",
      [
        "storage",
        "002bda4e",
        null,
        "string"
      ]
    ],
    [
      "00571b74",
      "READ",
      [
        "storage",
        "002c2530",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00571b70",
      "READ",
      [
        "storage",
        "002bda7e",
        null,
        "string"
      ]
    ],
    [
      "00571b70",
      "READ",
      [
        "storage",
        "002bda8e",
        null,
        "string"
      ]
    ],
    [
      "00571b74",
      "READ",
      [
        "storage",
        "002c2570",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md#insn-00571aec) · [`00571af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md#insn-00571af4) · [`00571b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md#insn-00571b20)
- 新版 [`00571b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b2c) · [`00571b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b34) · [`00571b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md#insn-00571b60)

~~~diff
- 00571aec ["INT_ADD", "register:40f0:8", ["const:571aec:8", "const:4:8"]]
- 00571aec ["CALL", null, ["callee:00588e6c:8"]]
+ 00571b2c ["INT_ADD", "register:40f0:8", ["const:571b2c:8", "const:4:8"]]
+ 00571b2c ["CALL", null, ["callee:00588e6c:8"]]
- 00571aec bytes d05c0094
+ 00571b2c bytes d05c0094
- 00571af4 ["INT_ADD", "register:40f0:8", ["const:571af4:8", "const:4:8"]]
- 00571af4 ["CALL", null, ["callee:0058915c:8"]]
+ 00571b34 ["INT_ADD", "register:40f0:8", ["const:571b34:8", "const:4:8"]]
+ 00571b34 ["CALL", null, ["callee:0058915c:8"]]
- 00571af4 bytes 8a5d0094
+ 00571b34 bytes 8a5d0094
- 00571b20 ["INT_ADD", "register:40f0:8", ["const:571b20:8", "const:4:8"]]
- 00571b20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00571b60 ["INT_ADD", "register:40f0:8", ["const:571b60:8", "const:4:8"]]
+ 00571b60 ["CALL", null, ["callee:00c57e90:8"]]
- 00571b20 bytes dc971b94
+ 00571b60 bytes cc981b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-790aa9d818c23345cf29448566b9d16a"></a>

### [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) → [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) FUN_00571e18

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550954.md) · 呼出先 15件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00550994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550994.md) · 呼出先 15件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571e94",
      "incomplete_value": true,
      "site": "00571ea0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571e54",
      "incomplete_value": true,
      "site": "00571e60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:320:8"
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
      "definition_site": "00571e90",
      "incomplete_value": true,
      "site": "00571ea4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:72d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571e50",
      "incomplete_value": true,
      "site": "00571e64",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571e90",
      "incomplete_value": true,
      "site": "00571ea4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00571e50",
      "incomplete_value": true,
      "site": "00571e64",
      "value": [
        "LOAD",
        "16",
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
      "00571e90",
      "READ",
      [
        "storage",
        "002bc6ed",
        null,
        "string"
      ]
    ],
    [
      "00571e90",
      "READ",
      [
        "storage",
        "002bc6fd",
        null,
        "string"
      ]
    ],
    [
      "00571e94",
      "READ",
      [
        "storage",
        "002c2320",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00571e90",
      "READ",
      [
        "storage",
        "002bc72d",
        null,
        "string"
      ]
    ],
    [
      "00571e90",
      "READ",
      [
        "storage",
        "002bc73d",
        null,
        "string"
      ]
    ],
    [
      "00571e94",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md#insn-00571ea4) · [`00571e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md#insn-00571e0c) · [`00571e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md#insn-00571e14)
- 新版 [`00571ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md#insn-00571ee4) · [`00571e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md#insn-00571e4c) · [`00571e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md#insn-00571e54)

~~~diff
- 00571ea4 ["INT_ADD", "register:40f0:8", ["const:571ea4:8", "const:4:8"]]
- 00571ea4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00571ee4 ["INT_ADD", "register:40f0:8", ["const:571ee4:8", "const:4:8"]]
+ 00571ee4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00571ea4 bytes 03971b94
+ 00571ee4 bytes f3971b94
- 00571e0c ["INT_ADD", "register:40f0:8", ["const:571e0c:8", "const:4:8"]]
- 00571e0c ["CALL", null, ["callee:00588e6c:8"]]
+ 00571e4c ["INT_ADD", "register:40f0:8", ["const:571e4c:8", "const:4:8"]]
+ 00571e4c ["CALL", null, ["callee:00588e6c:8"]]
- 00571e0c bytes 085c0094
+ 00571e4c bytes 085c0094
- 00571e14 ["INT_ADD", "register:40f0:8", ["const:571e14:8", "const:4:8"]]
- 00571e14 ["CALL", null, ["callee:0058915c:8"]]
+ 00571e54 ["INT_ADD", "register:40f0:8", ["const:571e54:8", "const:4:8"]]
+ 00571e54 ["CALL", null, ["callee:0058915c:8"]]
- 00571e14 bytes c25c0094
+ 00571e54 bytes c25c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c450e5a8592d247d292972b6f966be1"></a>

### [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) → [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) FUN_005720f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550958.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00550998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550998.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057215c",
      "incomplete_value": true,
      "site": "0057216c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057211c",
      "incomplete_value": true,
      "site": "0057212c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f:8"
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
      "definition_site": "00572170",
      "incomplete_value": true,
      "site": "00572170",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00572130",
      "incomplete_value": true,
      "site": "00572130",
      "value": [
        "LOAD",
        "8",
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
      "0057213c",
      "READ",
      [
        "storage",
        "002bfea3",
        null,
        "string"
      ]
    ],
    [
      "0057215c",
      "READ",
      [
        "storage",
        "002a201f",
        null,
        "string"
      ]
    ],
    [
      "00572164",
      "READ",
      [
        "storage",
        "002a202d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057213c",
      "READ",
      [
        "storage",
        "002bfee3",
        null,
        "string"
      ]
    ],
    [
      "0057215c",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ],
    [
      "00572164",
      "READ",
      [
        "storage",
        "002a20fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005720ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md#insn-005720ec) · [`0057216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md#insn-0057216c) · [`005720e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md#insn-005720e4)
- 新版 [`0057212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-0057212c) · [`005721ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-005721ac) · [`00572124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md#insn-00572124)

~~~diff
- 005720ec ["INT_ADD", "register:40f0:8", ["const:5720ec:8", "const:4:8"]]
- 005720ec ["CALL", null, ["callee:0058915c:8"]]
+ 0057212c ["INT_ADD", "register:40f0:8", ["const:57212c:8", "const:4:8"]]
+ 0057212c ["CALL", null, ["callee:0058915c:8"]]
- 005720ec bytes 0c5c0094
+ 0057212c bytes 0c5c0094
- 0057216c ["INT_ADD", "register:40f0:8", ["const:57216c:8", "const:4:8"]]
- 0057216c ["CALL", null, ["callee:00589144:8"]]
+ 005721ac ["INT_ADD", "register:40f0:8", ["const:5721ac:8", "const:4:8"]]
+ 005721ac ["CALL", null, ["callee:00589144:8"]]
- 0057216c bytes e65b0094
+ 005721ac bytes e65b0094
- 005720e4 ["INT_ADD", "register:40f0:8", ["const:5720e4:8", "const:4:8"]]
- 005720e4 ["CALL", null, ["callee:00588e6c:8"]]
+ 00572124 ["INT_ADD", "register:40f0:8", ["const:572124:8", "const:4:8"]]
+ 00572124 ["CALL", null, ["callee:00588e6c:8"]]
- 005720e4 bytes 525b0094
+ 00572124 bytes 525b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd0741b569b6dc77e0b64496c83c89e"></a>

### [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) → [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) FUN_005722ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055095c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055095c.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0055099c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/0055099c.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572304",
      "incomplete_value": true,
      "site": "00572304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005722c4",
      "incomplete_value": true,
      "site": "005722c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea3:8"
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
      "definition_site": "00572310",
      "incomplete_value": true,
      "site": "00572320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005722d0",
      "incomplete_value": true,
      "site": "005722e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f:8"
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
      "definition_site": "00572324",
      "incomplete_value": true,
      "site": "00572324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005722e4",
      "incomplete_value": true,
      "site": "005722e4",
      "value": [
        "LOAD",
        "8",
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
      "005722f0",
      "READ",
      [
        "storage",
        "002bfea3",
        null,
        "string"
      ]
    ],
    [
      "00572310",
      "READ",
      [
        "storage",
        "002a201f",
        null,
        "string"
      ]
    ],
    [
      "00572318",
      "READ",
      [
        "storage",
        "002a202d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005722f0",
      "READ",
      [
        "storage",
        "002bfee3",
        null,
        "string"
      ]
    ],
    [
      "00572310",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ],
    [
      "00572318",
      "READ",
      [
        "storage",
        "002a20fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005722a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md#insn-005722a0) · [`00572320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md#insn-00572320) · [`00572298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md#insn-00572298)
- 新版 [`005722e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-005722e0) · [`00572360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-00572360) · [`005722d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md#insn-005722d8)

~~~diff
- 005722a0 ["INT_ADD", "register:40f0:8", ["const:5722a0:8", "const:4:8"]]
- 005722a0 ["CALL", null, ["callee:0058915c:8"]]
+ 005722e0 ["INT_ADD", "register:40f0:8", ["const:5722e0:8", "const:4:8"]]
+ 005722e0 ["CALL", null, ["callee:0058915c:8"]]
- 005722a0 bytes 9f5b0094
+ 005722e0 bytes 9f5b0094
- 00572320 ["INT_ADD", "register:40f0:8", ["const:572320:8", "const:4:8"]]
- 00572320 ["CALL", null, ["callee:00589144:8"]]
+ 00572360 ["INT_ADD", "register:40f0:8", ["const:572360:8", "const:4:8"]]
+ 00572360 ["CALL", null, ["callee:00589144:8"]]
- 00572320 bytes 795b0094
+ 00572360 bytes 795b0094
- 00572298 ["INT_ADD", "register:40f0:8", ["const:572298:8", "const:4:8"]]
- 00572298 ["CALL", null, ["callee:00588e6c:8"]]
+ 005722d8 ["INT_ADD", "register:40f0:8", ["const:5722d8:8", "const:4:8"]]
+ 005722d8 ["CALL", null, ["callee:00588e6c:8"]]
- 00572298 bytes e55a0094
+ 005722d8 bytes e55a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994fed998e7137c447f834b44ef4fbdb"></a>

### [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) → [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) FUN_00572460

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00574d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md)
- 新版 呼出元 1件 [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00574d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574d88.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.44% / 新版 92.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005724dc",
      "incomplete_value": true,
      "site": "005724ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057249c",
      "incomplete_value": true,
      "site": "005724ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a:8"
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
      "definition_site": "005724f0",
      "incomplete_value": true,
      "site": "005724f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005724b0",
      "incomplete_value": true,
      "site": "005724b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005724e4",
      "incomplete_value": true,
      "site": "005724f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005724a4",
      "incomplete_value": true,
      "site": "005724b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "005724dc",
      "READ",
      [
        "storage",
        "002b904a",
        null,
        "string"
      ]
    ],
    [
      "005724e0",
      "READ",
      [
        "storage",
        "002b9059",
        null,
        "string"
      ]
    ],
    [
      "005724e4",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005724dc",
      "READ",
      [
        "storage",
        "002b908a",
        null,
        "string"
      ]
    ],
    [
      "005724e0",
      "READ",
      [
        "storage",
        "002b9099",
        null,
        "string"
      ]
    ],
    [
      "005724e4",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005724f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md#insn-005724f0) · [`00572518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md#insn-00572518) · [`00572594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md#insn-00572594)
- 新版 [`00572530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-00572530) · [`00572558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-00572558) · [`005725d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md#insn-005725d4)

~~~diff
- 005724f0 ["INT_ADD", "register:40f0:8", ["const:5724f0:8", "const:4:8"]]
- 005724f0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00572530 ["INT_ADD", "register:40f0:8", ["const:572530:8", "const:4:8"]]
+ 00572530 ["CALL", null, ["callee:00c57eb0:8"]]
- 005724f0 bytes 70951b94
+ 00572530 bytes 60961b94
- 00572518 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:db8:8"]]
- 00572518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 00572558 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1b8:8"]]
+ 00572558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00572518 bytes 54b90db9
+ 00572558 bytes 54b901b9
- 00572594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00572594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005725d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
+ 005725d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00572594 bytes 09d106f9
+ 005725d4 bytes 09d100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ffb307316a02cdf562a8cad1301d74b"></a>

### [`00572874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572874.md) → [`005728b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md) FUN_005728b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00550964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550964.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005509a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a4.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572900",
      "incomplete_value": true,
      "site": "00572900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005728c0",
      "incomplete_value": true,
      "site": "005728c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9c:8"
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
      "005728f0",
      "READ",
      [
        "storage",
        "002a9c9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005728f0",
      "READ",
      [
        "storage",
        "002a9d69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572874.md#insn-00572894) · [`0057289c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572874.md#insn-0057289c) · [`005728a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572874.md#insn-005728a8)
- 新版 [`005728d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728d4) · [`005728dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728dc) · [`005728e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005728b4.md#insn-005728e8)

~~~diff
- 00572894 ["INT_ADD", "register:40f0:8", ["const:572894:8", "const:4:8"]]
- 00572894 ["CALL", null, ["callee:00588e6c:8"]]
+ 005728d4 ["INT_ADD", "register:40f0:8", ["const:5728d4:8", "const:4:8"]]
+ 005728d4 ["CALL", null, ["callee:00588e6c:8"]]
- 00572894 bytes 66590094
+ 005728d4 bytes 66590094
- 0057289c ["INT_ADD", "register:40f0:8", ["const:57289c:8", "const:4:8"]]
- 0057289c ["CALL", null, ["callee:0058915c:8"]]
+ 005728dc ["INT_ADD", "register:40f0:8", ["const:5728dc:8", "const:4:8"]]
+ 005728dc ["CALL", null, ["callee:0058915c:8"]]
- 0057289c bytes 205a0094
+ 005728dc bytes 205a0094
- 005728a8 ["COPY", "tmp:0:8", ["const:c9c:8"]]
- 005728a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005728a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005728a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005728e8 ["COPY", "tmp:0:8", ["const:d69:8"]]
+ 005728e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005728e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005728e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005728a8 bytes 29713291
+ 005728e8 bytes 29a53591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfdb5ee4fbd0ff86a70d362e88f64361"></a>

### [`005729a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md) → [`005729e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md) FUN_005729e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550968.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005509a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a8.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572a20",
      "incomplete_value": true,
      "site": "00572a38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005729e0",
      "incomplete_value": true,
      "site": "005729f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ead:8"
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
      "definition_site": "00572a3c",
      "incomplete_value": true,
      "site": "00572a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c94:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005729fc",
      "incomplete_value": true,
      "site": "00572a08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c54:8"
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
      "definition_site": "00572a4c",
      "incomplete_value": true,
      "site": "00572a4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00572a0c",
      "incomplete_value": true,
      "site": "00572a0c",
      "value": [
        "LOAD",
        "8",
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
      "00572a20",
      "READ",
      [
        "storage",
        "002bfead",
        null,
        "string"
      ]
    ],
    [
      "00572a3c",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "00572a40",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572a20",
      "READ",
      [
        "storage",
        "002bfeed",
        null,
        "string"
      ]
    ],
    [
      "00572a3c",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "00572a40",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005729c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md#insn-005729c8) · [`00572a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md#insn-00572a4c) · [`005729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md#insn-005729d0)
- 新版 [`00572a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a08) · [`00572a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a8c) · [`00572a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md#insn-00572a10)

~~~diff
- 005729c8 ["INT_ADD", "register:40f0:8", ["const:5729c8:8", "const:4:8"]]
- 005729c8 ["CALL", null, ["callee:00588e6c:8"]]
+ 00572a08 ["INT_ADD", "register:40f0:8", ["const:572a08:8", "const:4:8"]]
+ 00572a08 ["CALL", null, ["callee:00588e6c:8"]]
- 005729c8 bytes 19590094
+ 00572a08 bytes 19590094
- 00572a4c ["INT_ADD", "register:40f0:8", ["const:572a4c:8", "const:4:8"]]
- 00572a4c ["CALL", null, ["callee:00589144:8"]]
+ 00572a8c ["INT_ADD", "register:40f0:8", ["const:572a8c:8", "const:4:8"]]
+ 00572a8c ["CALL", null, ["callee:00589144:8"]]
- 00572a4c bytes ae590094
+ 00572a8c bytes ae590094
- 005729d0 ["INT_ADD", "register:40f0:8", ["const:5729d0:8", "const:4:8"]]
- 005729d0 ["CALL", null, ["callee:0058915c:8"]]
+ 00572a10 ["INT_ADD", "register:40f0:8", ["const:572a10:8", "const:4:8"]]
+ 00572a10 ["CALL", null, ["callee:0058915c:8"]]
- 005729d0 bytes d3590094
+ 00572a10 bytes d3590094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7fd7b8ab5952897a9236a3cc8bb748"></a>

### [`00572b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md) → [`00572ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md) FUN_00572ba0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055096c.md) · 呼出先 2件 [`00574eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005509ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509ac.md) · 呼出先 2件 [`00574ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ef0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00572c08",
      "incomplete_value": false,
      "site": "00572c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572bc8",
      "incomplete_value": false,
      "site": "00572bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "00572c08",
      "PARAM",
      [
        "storage",
        "00ca5d70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572c08",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md#insn-00572bd4) · [`00572b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md#insn-00572b98) · [`00572bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md#insn-00572bc0)
- 新版 [`00572c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572c14) · [`00572bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572bd8) · [`00572c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572ba0.md#insn-00572c00)

~~~diff
- 00572bd4 ["INT_ADD", "register:40f0:8", ["const:572bd4:8", "const:4:8"]]
- 00572bd4 ["CALL", null, ["callee:00574ef0:8"]]
+ 00572c14 ["INT_ADD", "register:40f0:8", ["const:572c14:8", "const:4:8"]]
+ 00572c14 ["CALL", null, ["callee:00574ef0:8"]]
- 00572bd4 bytes b7080094
+ 00572c14 bytes b7080094
- 00572b98 ["COPY", "register:0:8", ["register:4048:8"]]
- 00572b98 ["INT_ADD", "register:40f0:8", ["const:572b98:8", "const:4:8"]]
- 00572b98 ["CALLIND", null, ["register:0:8"]]
+ 00572bd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00572bd8 ["INT_ADD", "register:40f0:8", ["const:572bd8:8", "const:4:8"]]
+ 00572bd8 ["CALLIND", null, ["register:0:8"]]
- 00572b98 bytes 20013fd6
+ 00572bd8 bytes 20013fd6
- 00572bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00572bc0 ["INT_ADD", "register:40f0:8", ["const:572bc0:8", "const:4:8"]]
- 00572bc0 ["CALLIND", null, ["register:0:8"]]
+ 00572c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572c00 ["INT_ADD", "register:40f0:8", ["const:572c00:8", "const:4:8"]]
+ 00572c00 ["CALLIND", null, ["register:0:8"]]
- 00572bc0 bytes 00013fd6
+ 00572c00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2dda8129ed74becf0e83bd6ca94eb7"></a>

### [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) → [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) Java_jp_co_ponos_battlecats_MyActivity_onIapList

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) [`00574438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md) [`005750e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) [`00574478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md) [`00575124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575124.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00572d3c",
      "incomplete_value": false,
      "site": "00572d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572cfc",
      "incomplete_value": false,
      "site": "00572cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00572de8",
      "incomplete_value": true,
      "site": "00572dec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572da8",
      "incomplete_value": true,
      "site": "00572dac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c0:8"
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
      "definition_site": "00572e78",
      "incomplete_value": true,
      "site": "00572e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:29d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572e38",
      "incomplete_value": true,
      "site": "00572e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
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
      "00572ca4",
      "READ",
      [
        "storage",
        "00ca5da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572d3c",
      "DATA",
      [
        "storage",
        "00c6b710",
        null,
        "pointer"
      ]
    ],
    [
      "00572de8",
      "READ",
      [
        "storage",
        "002c29c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572ca4",
      "READ",
      [
        "storage",
        "00ca61a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572d3c",
      "DATA",
      [
        "storage",
        "00c6bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00572de8",
      "READ",
      [
        "storage",
        "002c2a00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md#insn-00572fc0) · [`005730a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md#insn-005730a0) · [`005730e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md#insn-005730e8)
- 新版 [`00573000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-00573000) · [`005730e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-005730e0) · [`00573128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md#insn-00573128)

~~~diff
- 00572fc0 ["INT_ADD", "register:40f0:8", ["const:572fc0:8", "const:4:8"]]
- 00572fc0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00573000 ["INT_ADD", "register:40f0:8", ["const:573000:8", "const:4:8"]]
+ 00573000 ["CALL", null, ["callee:00c57eb0:8"]]
- 00572fc0 bytes bc921b94
+ 00573000 bytes ac931b94
- 005730a0 ["COPY", "tmp:0:8", ["const:ad2:8"]]
- 005730a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005730a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005730a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005730e0 ["COPY", "tmp:0:8", ["const:b12:8"]]
+ 005730e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005730e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005730e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005730a0 bytes 29492b91
+ 005730e0 bytes 29492c91
- 005730e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005730e8 ["INT_ADD", "register:40f0:8", ["const:5730e8:8", "const:4:8"]]
- 005730e8 ["CALLIND", null, ["register:0:8"]]
+ 00573128 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00573128 ["INT_ADD", "register:40f0:8", ["const:573128:8", "const:4:8"]]
+ 00573128 ["CALLIND", null, ["register:0:8"]]
- 005730e8 bytes 20013fd6
+ 00573128 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d476787f5fbda2eee3c3451ce12c3186"></a>

### [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) → [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) [`0058a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a798.md) [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) [`0058a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7d8.md) [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00573fbc",
      "incomplete_value": true,
      "site": "00573fbc",
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
      "definition_site": "00573f7c",
      "incomplete_value": true,
      "site": "00573f7c",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00573f7c"
      ],
      [
        "FALL_THROUGH",
        "00573fbc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00573fbc",
      "incomplete_value": true,
      "site": "00573fc0",
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
      "definition_site": "00573f7c",
      "incomplete_value": true,
      "site": "00573f80",
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
      "00573fb8",
      "READ",
      [
        "storage",
        "00ca5d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00573fb8",
      "READ",
      [
        "storage",
        "00ca6190",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md#insn-00573e80) · [`00573e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md#insn-00573e8c) · [`00573e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md#insn-00573e9c)
- 新版 [`00573ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573ec0) · [`00573ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573ecc) · [`00573edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md#insn-00573edc)

~~~diff
- 00573e80 ["INT_ADD", "register:40f0:8", ["const:573e80:8", "const:4:8"]]
- 00573e80 ["CALL", null, ["callee:0058a624:8"]]
+ 00573ec0 ["INT_ADD", "register:40f0:8", ["const:573ec0:8", "const:4:8"]]
+ 00573ec0 ["CALL", null, ["callee:0058a624:8"]]
- 00573e80 bytes d9590094
+ 00573ec0 bytes d9590094
- 00573e8c ["INT_ADD", "register:40f0:8", ["const:573e8c:8", "const:4:8"]]
- 00573e8c ["CALL", null, ["callee:0058a624:8"]]
+ 00573ecc ["INT_ADD", "register:40f0:8", ["const:573ecc:8", "const:4:8"]]
+ 00573ecc ["CALL", null, ["callee:0058a624:8"]]
- 00573e8c bytes d6590094
+ 00573ecc bytes d6590094
- 00573e9c ["INT_ADD", "register:40f0:8", ["const:573e9c:8", "const:4:8"]]
- 00573e9c ["CALL", null, ["callee:0058a7d8:8"]]
+ 00573edc ["INT_ADD", "register:40f0:8", ["const:573edc:8", "const:4:8"]]
+ 00573edc ["CALL", null, ["callee:0058a7d8:8"]]
- 00573e9c bytes 3f5a0094
+ 00573edc bytes 3f5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131bb2eb3b6ba73ff91827dfd44b1b95"></a>

### [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) → [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases2

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) [`0058a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a798.md) [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) [`0058a720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a720.md) [`0058a7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7d8.md) [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00574278",
      "incomplete_value": true,
      "site": "00574278",
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
      "definition_site": "00574238",
      "incomplete_value": true,
      "site": "00574238",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00574238"
      ],
      [
        "FALL_THROUGH",
        "00574278"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00574278",
      "incomplete_value": true,
      "site": "0057427c",
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
      "definition_site": "00574238",
      "incomplete_value": true,
      "site": "0057423c",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00574274",
      "READ",
      [
        "storage",
        "00ca5d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00574274",
      "READ",
      [
        "storage",
        "00ca6190",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005740e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md#insn-005740e8) · [`005740f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md#insn-005740f4) · [`0057410c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md#insn-0057410c)
- 新版 [`00574128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-00574128) · [`00574134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-00574134) · [`0057414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md#insn-0057414c)

~~~diff
- 005740e8 ["INT_ADD", "register:40f0:8", ["const:5740e8:8", "const:4:8"]]
- 005740e8 ["CALL", null, ["callee:0058a624:8"]]
+ 00574128 ["INT_ADD", "register:40f0:8", ["const:574128:8", "const:4:8"]]
+ 00574128 ["CALL", null, ["callee:0058a624:8"]]
- 005740e8 bytes 3f590094
+ 00574128 bytes 3f590094
- 005740f4 ["INT_ADD", "register:40f0:8", ["const:5740f4:8", "const:4:8"]]
- 005740f4 ["CALL", null, ["callee:0058a624:8"]]
+ 00574134 ["INT_ADD", "register:40f0:8", ["const:574134:8", "const:4:8"]]
+ 00574134 ["CALL", null, ["callee:0058a624:8"]]
- 005740f4 bytes 3c590094
+ 00574134 bytes 3c590094
- 0057410c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057410c ["INT_ADD", "register:40f0:8", ["const:57410c:8", "const:4:8"]]
- 0057410c ["CALLIND", null, ["register:0:8"]]
+ 0057414c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057414c ["INT_ADD", "register:40f0:8", ["const:57414c:8", "const:4:8"]]
+ 0057414c ["CALLIND", null, ["register:0:8"]]
- 0057410c bytes 00013fd6
+ 0057414c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b86fd2f73a94f86a0dfd21a90269720"></a>

### [`005743a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743a4.md) → [`005743e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743e4.md) FUN_005743e4

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
      "definition_site": "005743e8",
      "incomplete_value": false,
      "site": "005743ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005743a8",
      "incomplete_value": false,
      "site": "005743ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:590:8"
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
      "005743ec",
      "DATA",
      [
        "storage",
        "00c6b590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005743ec",
      "DATA",
      [
        "storage",
        "00c6b990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005743a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743a4.md#insn-005743a8)
- 新版 [`005743e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743e4.md#insn-005743e8)

~~~diff
- 005743a8 ["COPY", "tmp:0:8", ["const:590:8"]]
- 005743a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005743a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005743a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005743e8 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005743e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005743e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005743e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005743a8 bytes 08411691
+ 005743e8 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff5f6fc3c94ff7239ab9c367a75cf4b"></a>

### [`005743b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743b4.md) → [`005743f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md) FUN_005743f4

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
      "definition_site": "00574404",
      "incomplete_value": false,
      "site": "0057440c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005743c4",
      "incomplete_value": false,
      "site": "005743cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:590:8"
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
      "0057440c",
      "DATA",
      [
        "storage",
        "00c6b590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057440c",
      "DATA",
      [
        "storage",
        "00c6b990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005743c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743b4.md#insn-005743c4) · [`005743d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743b4.md#insn-005743d0)
- 新版 [`00574404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md#insn-00574404) · [`00574410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005743f4.md#insn-00574410)

~~~diff
- 005743c4 ["COPY", "tmp:0:8", ["const:590:8"]]
- 005743c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005743c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005743c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574404 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00574404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005743c4 bytes 08411691
+ 00574404 bytes 08412691
- 005743d0 ["INT_ADD", "register:40f0:8", ["const:5743d0:8", "const:4:8"]]
- 005743d0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00574410 ["INT_ADD", "register:40f0:8", ["const:574410:8", "const:4:8"]]
+ 00574410 ["CALL", null, ["callee:00c57ea0:8"]]
- 005743d0 bytes b48d1b94
+ 00574410 bytes a48e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9388cda08fa4bbb75c0b1d7c049e8c02"></a>

### [`00574438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md) → [`00574478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md) FUN_00574478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005744a8",
      "incomplete_value": true,
      "site": "005744a8",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574468",
      "incomplete_value": true,
      "site": "00574468",
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
            "const:5e0:8"
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
      "005744a8",
      "DATA",
      [
        "storage",
        "00c6b5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005744a8",
      "DATA",
      [
        "storage",
        "00c6b9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md#insn-00574458) · [`005744a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md#insn-005744a0) · [`005744cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md#insn-005744cc)
- 新版 [`00574498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-00574498) · [`005744e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-005744e0) · [`0057450c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574478.md#insn-0057450c)

~~~diff
- 00574458 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00574458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574498 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00574498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574458 bytes 08811791
+ 00574498 bytes 08812791
- 005744a0 ["INT_ADD", "register:40f0:8", ["const:5744a0:8", "const:4:8"]]
- 005744a0 ["CALL", null, ["callee:0043bb20:8"]]
+ 005744e0 ["INT_ADD", "register:40f0:8", ["const:5744e0:8", "const:4:8"]]
+ 005744e0 ["CALL", null, ["callee:0043bb20:8"]]
- 005744a0 bytes 901dfb97
+ 005744e0 bytes 901dfb97
- 005744cc ["INT_ADD", "register:40f0:8", ["const:5744cc:8", "const:4:8"]]
- 005744cc ["CALL", null, ["callee:0043bb20:8"]]
+ 0057450c ["INT_ADD", "register:40f0:8", ["const:57450c:8", "const:4:8"]]
+ 0057450c ["CALL", null, ["callee:0043bb20:8"]]
- 005744cc bytes 851dfb97
+ 0057450c bytes 851dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c3b47b895c8aa55c35742629990455"></a>

### [`005746e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md) → [`00574728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md) FUN_00574728

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005743e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00574424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574424.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574740",
      "incomplete_value": false,
      "site": "00574744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574700",
      "incomplete_value": false,
      "site": "00574704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "00574744",
      "DATA",
      [
        "storage",
        "00c6b5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574744",
      "DATA",
      [
        "storage",
        "00c6b9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md#insn-00574700) · [`0057473c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md#insn-0057473c) · [`0057474c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md#insn-0057474c)
- 新版 [`00574740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-00574740) · [`0057477c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-0057477c) · [`0057478c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574728.md#insn-0057478c)

~~~diff
- 00574700 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00574700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00574700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00574700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00574740 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00574740 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00574740 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00574740 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00574700 bytes 29811791
+ 00574740 bytes 29812791
- 0057473c ["INT_ADD", "register:40f0:8", ["const:57473c:8", "const:4:8"]]
- 0057473c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057477c ["INT_ADD", "register:40f0:8", ["const:57477c:8", "const:4:8"]]
+ 0057477c ["CALL", null, ["callee:00c57eb0:8"]]
- 0057473c bytes dd8c1b94
+ 0057477c bytes cd8d1b94
- 0057474c ["INT_ADD", "register:40f0:8", ["const:57474c:8", "const:4:8"]]
- 0057474c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057478c ["INT_ADD", "register:40f0:8", ["const:57478c:8", "const:4:8"]]
+ 0057478c ["CALL", null, ["callee:00c57eb0:8"]]
- 0057474c bytes d98c1b94
+ 0057478c bytes c98d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbc53092240fca32ae083bf40954330"></a>

### [`00574788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574788.md) → [`005747c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747c8.md) FUN_005747c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005747cc",
      "incomplete_value": true,
      "site": "005747d0",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057478c",
      "incomplete_value": true,
      "site": "00574790",
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
            "const:648:8"
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
      "005747d0",
      "DATA",
      [
        "storage",
        "00c6b648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005747d0",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057478c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574788.md#insn-0057478c)
- 新版 [`005747cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747c8.md#insn-005747cc)

~~~diff
- 0057478c ["COPY", "tmp:0:8", ["const:648:8"]]
- 0057478c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057478c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057478c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005747cc ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 005747cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005747cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005747cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057478c bytes 08211991
+ 005747cc bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb600cbaab50b32aa7eb910492e8fd9"></a>

### [`00574798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574798.md) → [`005747d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md) FUN_005747d8

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
      "definition_site": "005747e8",
      "incomplete_value": false,
      "site": "005747f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005747a8",
      "incomplete_value": false,
      "site": "005747b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "005747f0",
      "DATA",
      [
        "storage",
        "00c6b648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005747f0",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005747a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574798.md#insn-005747a8) · [`005747b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574798.md#insn-005747b4)
- 新版 [`005747e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md#insn-005747e8) · [`005747f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005747d8.md#insn-005747f4)

~~~diff
- 005747a8 ["COPY", "tmp:0:8", ["const:648:8"]]
- 005747a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005747a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005747a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005747e8 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 005747e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005747e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005747e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005747a8 bytes 08211991
+ 005747e8 bytes 08212991
- 005747b4 ["INT_ADD", "register:40f0:8", ["const:5747b4:8", "const:4:8"]]
- 005747b4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005747f4 ["INT_ADD", "register:40f0:8", ["const:5747f4:8", "const:4:8"]]
+ 005747f4 ["CALL", null, ["callee:00c57ea0:8"]]
- 005747b4 bytes bb8c1b94
+ 005747f4 bytes ab8d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4fe70b184e7d8be44e96c750285729b"></a>

### [`0057481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md) → [`0057485c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md) FUN_0057485c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "00574880",
      "incomplete_value": false,
      "site": "00574880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574840",
      "incomplete_value": false,
      "site": "00574840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00574880",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574880",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md#insn-00574838) · [`0057483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md#insn-0057483c)
- 新版 [`00574878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md#insn-00574878) · [`0057487c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/0057485c.md#insn-0057487c)

~~~diff
- 00574838 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00574838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574878 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00574878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574838 bytes 08611a91
+ 00574878 bytes 08612a91
- 0057483c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0057483c bytes f50300aa
+ 0057487c ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 0057487c bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cac06ddb20c2fb33fc52cfa1c00e3e"></a>

### [`00574a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md) → [`00574acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md) FUN_00574acc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005747c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00574808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574808.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574ae4",
      "incomplete_value": false,
      "site": "00574ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574aa4",
      "incomplete_value": false,
      "site": "00574aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00574ae8",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574ae8",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md#insn-00574ae8) · [`00574aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md#insn-00574aa4) · [`00574ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md#insn-00574ab8)
- 新版 [`00574b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574b28) · [`00574ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574ae4) · [`00574af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574acc.md#insn-00574af8)

~~~diff
- 00574ae8 ["INT_ADD", "register:40f0:8", ["const:574ae8:8", "const:4:8"]]
- 00574ae8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00574b28 ["INT_ADD", "register:40f0:8", ["const:574b28:8", "const:4:8"]]
+ 00574b28 ["CALL", null, ["callee:00c53d00:8"]]
- 00574ae8 bytes 7e7b1b94
+ 00574b28 bytes 767c1b94
- 00574aa4 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00574aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574ae4 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00574ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574aa4 bytes 08611a91
+ 00574ae4 bytes 08612a91
- 00574ab8 ["INT_ADD", "register:40f0:8", ["const:574ab8:8", "const:4:8"]]
- 00574ab8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00574af8 ["INT_ADD", "register:40f0:8", ["const:574af8:8", "const:4:8"]]
+ 00574af8 ["CALL", null, ["callee:00c53d00:8"]]
- 00574ab8 bytes 8a7b1b94
+ 00574af8 bytes 827c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d30aacd945402d4ab1fe163b5f60222"></a>

### [`00574b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md) → [`00574ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md) FUN_00574ba4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) · 呼出先 2件 [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00573b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573b60.md) · 呼出先 2件 [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574bcc",
      "incomplete_value": false,
      "site": "00574bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574b8c",
      "incomplete_value": false,
      "site": "00574b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00574be0",
      "incomplete_value": false,
      "site": "00574be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574ba0",
      "incomplete_value": false,
      "site": "00574ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00574bd4",
      "DATA",
      [
        "storage",
        "00c6b648",
        null,
        "undefined *"
      ]
    ],
    [
      "00574be0",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574bd4",
      "DATA",
      [
        "storage",
        "00c6ba48",
        null,
        "undefined *"
      ]
    ],
    [
      "00574be0",
      "DATA",
      [
        "storage",
        "00c6ba98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md#insn-00574b84) · [`00574b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md#insn-00574b8c) · [`00574b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md#insn-00574b90)
- 新版 [`00574bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md#insn-00574bc4) · [`00574bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574ba4.md#insn-00574bcc)

~~~diff
- 00574b84 ["INT_ADD", "register:40f0:8", ["const:574b84:8", "const:4:8"]]
- 00574b84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00574bc4 ["INT_ADD", "register:40f0:8", ["const:574bc4:8", "const:4:8"]]
+ 00574bc4 ["CALL", null, ["callee:00c57e90:8"]]
- 00574b84 bytes c38b1b94
+ 00574bc4 bytes b38c1b94
- 00574b8c ["COPY", "tmp:0:8", ["const:648:8"]]
- 00574b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574bcc ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00574bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574b8c bytes 08211991
+ 00574bcc bytes 08212991
- 00574b90 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 00574b90 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d234989199abbbb3824ac37c71781d46"></a>

### [`00575304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md) → [`00575344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md) FUN_00575344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005751a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005751e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005751e8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00575350",
      "incomplete_value": false,
      "site": "00575354",
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
      "definition_site": "00575310",
      "incomplete_value": false,
      "site": "00575314",
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
      "00575350",
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
      "00575350",
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

- 旧版 [`00575314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md#insn-00575314) · [`00575310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md#insn-00575310)
- 新版 [`00575354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md#insn-00575354) · [`00575350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575344.md#insn-00575350)

~~~diff
- 00575314 ["INT_ADD", "register:40f0:8", ["const:575314:8", "const:4:8"]]
- 00575314 ["CALL", null, ["callee:0043b778:8"]]
+ 00575354 ["INT_ADD", "register:40f0:8", ["const:575354:8", "const:4:8"]]
+ 00575354 ["CALL", null, ["callee:0043b778:8"]]
- 00575314 bytes 0919fb97
+ 00575354 bytes 0919fb97
- 00575310 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00575310 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00575310 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00575310 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00575350 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00575350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00575350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00575350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00575310 bytes 00303c91
+ 00575350 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f872fde360e9c31a4b20a4cacd58be"></a>

### [`00575318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575318.md) → [`00575358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md) _INIT_29

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00571788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571788.md) [`005717b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005717c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717c8.md) [`005717f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005717f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00575380",
      "incomplete_value": false,
      "site": "00575380",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:170:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575340",
      "incomplete_value": false,
      "site": "00575340",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:d70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057539c",
      "incomplete_value": false,
      "site": "0057539c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
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
      "definition_site": "0057535c",
      "incomplete_value": false,
      "site": "0057535c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:da0:8"
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005753a0",
      "incomplete_value": false,
      "site": "005753a0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
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
      "definition_site": "00575360",
      "incomplete_value": false,
      "site": "00575360",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:da0:8"
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
      "00575370",
      "PARAM",
      [
        "storage",
        "00ca5d70",
        null,
        null
      ]
    ],
    [
      "00575378",
      "PARAM",
      [
        "storage",
        "00571788",
        null,
        null
      ]
    ],
    [
      "0057537c",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00575370",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        null
      ]
    ],
    [
      "00575378",
      "PARAM",
      [
        "storage",
        "005717c8",
        null,
        null
      ]
    ],
    [
      "0057537c",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575318.md#insn-00575328) · [`00575344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575318.md#insn-00575344) · [`0057532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575318.md#insn-0057532c)
- 新版 [`00575368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md#insn-00575368) · [`00575384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575358.md#insn-00575384)

~~~diff
- 00575328 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00575328 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00575328 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00575328 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00575368 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00575368 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00575368 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00575368 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00575328 bytes 73422e91
+ 00575368 bytes 73423e91
- 00575344 ["INT_ADD", "register:40f0:8", ["const:575344:8", "const:4:8"]]
- 00575344 ["CALL", null, ["callee:00c57e30:8"]]
+ 00575384 ["INT_ADD", "register:40f0:8", ["const:575384:8", "const:4:8"]]
+ 00575384 ["CALL", null, ["callee:00c57e30:8"]]
- 00575344 bytes bb891b94
+ 00575384 bytes ab8a1b94
- 0057532c ["COPY", "register:4008:8", ["const:ca5000:8"]]
- 0057532c bytes 81390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16598ab0a0272e9986692b200eee962"></a>

### [`005753d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753d8.md) → [`00575418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md) FUN_00575418

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057545c",
      "incomplete_value": true,
      "site": "00575474",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057541c",
      "incomplete_value": true,
      "site": "00575434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c5:8"
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
      "definition_site": "00575478",
      "incomplete_value": true,
      "site": "00575484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575438",
      "incomplete_value": true,
      "site": "00575444",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a1:8"
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
      "definition_site": "00575488",
      "incomplete_value": true,
      "site": "00575488",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00575448",
      "incomplete_value": true,
      "site": "00575448",
      "value": [
        "LOAD",
        "8",
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
      "0057545c",
      "READ",
      [
        "storage",
        "002a55c5",
        null,
        "string"
      ]
    ],
    [
      "00575478",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0057547c",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057545c",
      "READ",
      [
        "storage",
        "002a56a1",
        null,
        "string"
      ]
    ],
    [
      "00575478",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "0057547c",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753d8.md#insn-00575404) · [`00575488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753d8.md#insn-00575488) · [`005753fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753d8.md#insn-005753fc)
- 新版 [`00575444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-00575444) · [`005754c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-005754c8) · [`0057543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575418.md#insn-0057543c)

~~~diff
- 00575404 ["INT_ADD", "register:40f0:8", ["const:575404:8", "const:4:8"]]
- 00575404 ["CALL", null, ["callee:0058915c:8"]]
+ 00575444 ["INT_ADD", "register:40f0:8", ["const:575444:8", "const:4:8"]]
+ 00575444 ["CALL", null, ["callee:0058915c:8"]]
- 00575404 bytes 464f0094
+ 00575444 bytes 464f0094
- 00575488 ["INT_ADD", "register:40f0:8", ["const:575488:8", "const:4:8"]]
- 00575488 ["CALL", null, ["callee:00589144:8"]]
+ 005754c8 ["INT_ADD", "register:40f0:8", ["const:5754c8:8", "const:4:8"]]
+ 005754c8 ["CALL", null, ["callee:00589144:8"]]
- 00575488 bytes 1f4f0094
+ 005754c8 bytes 1f4f0094
- 005753fc ["INT_ADD", "register:40f0:8", ["const:5753fc:8", "const:4:8"]]
- 005753fc ["CALL", null, ["callee:00588e6c:8"]]
+ 0057543c ["INT_ADD", "register:40f0:8", ["const:57543c:8", "const:4:8"]]
+ 0057543c ["CALL", null, ["callee:00588e6c:8"]]
- 005753fc bytes 8c4e0094
+ 0057543c bytes 8c4e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88779b7ff02760a96c2e7d0b55e8e3f9"></a>

### [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) → [`00575588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md) FUN_00575588

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550974.md) · 呼出先 14件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00575d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md) [`00575f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)
- 新版 呼出元 1件 [`005509b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b4.md) · 呼出先 14件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00575d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575d8c.md) [`00575f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575f98.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.40% / 新版 82.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005755d8",
      "incomplete_value": true,
      "site": "005755e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:347:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575598",
      "incomplete_value": true,
      "site": "005755a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:27a:8"
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
      "definition_site": "005755f8",
      "incomplete_value": true,
      "site": "005755f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005755b8",
      "incomplete_value": true,
      "site": "005755b8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005755ec",
      "incomplete_value": true,
      "site": "00575600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005755ac",
      "incomplete_value": true,
      "site": "005755c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "005755d8",
      "READ",
      [
        "storage",
        "002a427a",
        null,
        "string"
      ]
    ],
    [
      "005755dc",
      "READ",
      [
        "storage",
        "002a4289",
        null,
        "string"
      ]
    ],
    [
      "005755ec",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005755d8",
      "READ",
      [
        "storage",
        "002a4347",
        null,
        "string"
      ]
    ],
    [
      "005755dc",
      "READ",
      [
        "storage",
        "002a4356",
        null,
        "string"
      ]
    ],
    [
      "005755ec",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md#insn-00575590) · [`00575600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md#insn-00575600)
- 新版 [`005755d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md#insn-005755d0) · [`005755d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md#insn-005755d4) · [`00575640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575588.md#insn-00575640)

~~~diff
- 00575590 ["COPY", "tmp:0:8", ["const:27a:8"]]
- 00575590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00575590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00575590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005755d0 ["COPY", "tmp:0:8", ["const:347:8"]]
+ 005755d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005755d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005755d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00575590 bytes 08e90991
+ 005755d0 bytes 081d0d91
+ 005755d4 ["COPY", "register:4048:8", ["const:2c2000:8"]]
+ 005755d4 bytes 69eaffb0
- 00575600 ["INT_ADD", "register:40f0:8", ["const:575600:8", "const:4:8"]]
- 00575600 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00575640 ["INT_ADD", "register:40f0:8", ["const:575640:8", "const:4:8"]]
+ 00575640 ["CALL", null, ["callee:00c57eb0:8"]]
- 00575600 bytes 2c891b94
+ 00575640 bytes 1c8a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68032c3b0132455396dfbc8e24441364"></a>

### [`00575790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md) → [`005757d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md) FUN_005757d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550978.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00576110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`005509b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b8.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00576150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576150.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575818",
      "incomplete_value": true,
      "site": "00575828",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005757d8",
      "incomplete_value": true,
      "site": "005757e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b7:8"
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
      "definition_site": "0057581c",
      "incomplete_value": true,
      "site": "00575840",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005757dc",
      "incomplete_value": true,
      "site": "00575800",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057582c",
      "incomplete_value": true,
      "site": "00575844",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005757ec",
      "incomplete_value": true,
      "site": "00575804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b10:8"
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
      "00575818",
      "READ",
      [
        "storage",
        "002bb4b7",
        null,
        "string"
      ]
    ],
    [
      "0057581c",
      "READ",
      [
        "storage",
        "002bb4c4",
        null,
        "string"
      ]
    ],
    [
      "0057582c",
      "READ",
      [
        "storage",
        "002c2b10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00575818",
      "READ",
      [
        "storage",
        "002bb4f7",
        null,
        "string"
      ]
    ],
    [
      "0057581c",
      "READ",
      [
        "storage",
        "002bb504",
        null,
        "string"
      ]
    ],
    [
      "0057582c",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md#insn-00575840) · [`005757b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md#insn-005757b4) · [`005757bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md#insn-005757bc)
- 新版 [`00575880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-00575880) · [`005757f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-005757f4) · [`005757fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005757d0.md#insn-005757fc)

~~~diff
- 00575840 ["INT_ADD", "register:40f0:8", ["const:575840:8", "const:4:8"]]
- 00575840 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00575880 ["INT_ADD", "register:40f0:8", ["const:575880:8", "const:4:8"]]
+ 00575880 ["CALL", null, ["callee:00c57eb0:8"]]
- 00575840 bytes 9c881b94
+ 00575880 bytes 8c891b94
- 005757b4 ["INT_ADD", "register:40f0:8", ["const:5757b4:8", "const:4:8"]]
- 005757b4 ["CALL", null, ["callee:00588e6c:8"]]
+ 005757f4 ["INT_ADD", "register:40f0:8", ["const:5757f4:8", "const:4:8"]]
+ 005757f4 ["CALL", null, ["callee:00588e6c:8"]]
- 005757b4 bytes 9e4d0094
+ 005757f4 bytes 9e4d0094
- 005757bc ["INT_ADD", "register:40f0:8", ["const:5757bc:8", "const:4:8"]]
- 005757bc ["CALL", null, ["callee:0058915c:8"]]
+ 005757fc ["INT_ADD", "register:40f0:8", ["const:5757fc:8", "const:4:8"]]
+ 005757fc ["CALL", null, ["callee:0058915c:8"]]
- 005757bc bytes 584e0094
+ 005757fc bytes 584e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe486ab7c578108194cf7f409be9ea52"></a>

### [`00575950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575950.md) → [`00575990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md) FUN_00575990

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005759f4",
      "incomplete_value": true,
      "site": "00575a0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:35f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005759b4",
      "incomplete_value": true,
      "site": "005759cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:292:8"
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
      "005759f4",
      "READ",
      [
        "storage",
        "002a4292",
        null,
        "string"
      ]
    ],
    [
      "00575a28",
      "READ",
      [
        "storage",
        "002bfef2",
        null,
        "string"
      ]
    ],
    [
      "00575a28",
      "READ",
      [
        "storage",
        "002bff02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005759f4",
      "READ",
      [
        "storage",
        "002a435f",
        null,
        "string"
      ]
    ],
    [
      "00575a28",
      "READ",
      [
        "storage",
        "002bff32",
        null,
        "string"
      ]
    ],
    [
      "00575a28",
      "READ",
      [
        "storage",
        "002bff42",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575950.md#insn-0057599c) · [`005759a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575950.md#insn-005759a4) · [`005759ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575950.md#insn-005759ac)
- 新版 [`005759dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759dc) · [`005759e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759e4) · [`005759ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/00575990.md#insn-005759ec)

~~~diff
- 0057599c ["INT_ADD", "register:40f0:8", ["const:57599c:8", "const:4:8"]]
- 0057599c ["CALL", null, ["callee:00588e6c:8"]]
+ 005759dc ["INT_ADD", "register:40f0:8", ["const:5759dc:8", "const:4:8"]]
+ 005759dc ["CALL", null, ["callee:00588e6c:8"]]
- 0057599c bytes 244d0094
+ 005759dc bytes 244d0094
- 005759a4 ["INT_ADD", "register:40f0:8", ["const:5759a4:8", "const:4:8"]]
- 005759a4 ["CALL", null, ["callee:0058915c:8"]]
+ 005759e4 ["INT_ADD", "register:40f0:8", ["const:5759e4:8", "const:4:8"]]
+ 005759e4 ["CALL", null, ["callee:0058915c:8"]]
- 005759a4 bytes de4d0094
+ 005759e4 bytes de4d0094
- 005759ac ["COPY", "tmp:0:8", ["const:292:8"]]
- 005759ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005759ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005759ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005759ec ["COPY", "tmp:0:8", ["const:35f:8"]]
+ 005759ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005759ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005759ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005759ac bytes 29490a91
+ 005759ec bytes 297d0d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1057285eb4ba51d01a0aa4f4be78996d"></a>

### [`00576314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576314.md) → [`00576354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md) _INIT_30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00575378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575378.md) [`005753a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753a8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005753b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005753b8.md) [`005753e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00575/005753e8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057637c",
      "incomplete_value": false,
      "site": "0057637c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057633c",
      "incomplete_value": false,
      "site": "0057633c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00576398",
      "incomplete_value": false,
      "site": "00576398",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:1f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576358",
      "incomplete_value": false,
      "site": "00576358",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576374",
      "incomplete_value": false,
      "site": "00576380",
      "value": [
        "leaf",
        "const:5753b8:8"
      ]
    },
    "old": {
      "definition_site": "00576334",
      "incomplete_value": false,
      "site": "00576340",
      "value": [
        "leaf",
        "const:575378:8"
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
      "0057636c",
      "PARAM",
      [
        "storage",
        "00ca5dc0",
        null,
        null
      ]
    ],
    [
      "00576374",
      "PARAM",
      [
        "storage",
        "00575378",
        null,
        null
      ]
    ],
    [
      "00576378",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057636c",
      "PARAM",
      [
        "storage",
        "00ca61c0",
        null,
        null
      ]
    ],
    [
      "00576374",
      "PARAM",
      [
        "storage",
        "005753b8",
        null,
        null
      ]
    ],
    [
      "00576378",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576314.md#insn-00576340) · [`00576324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576314.md#insn-00576324) · [`00576328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576314.md#insn-00576328)
- 新版 [`00576380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md#insn-00576380) · [`00576364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576354.md#insn-00576364)

~~~diff
- 00576340 ["INT_ADD", "register:40f0:8", ["const:576340:8", "const:4:8"]]
- 00576340 ["CALL", null, ["callee:00c57e30:8"]]
+ 00576380 ["INT_ADD", "register:40f0:8", ["const:576380:8", "const:4:8"]]
+ 00576380 ["CALL", null, ["callee:00c57e30:8"]]
- 00576340 bytes bc851b94
+ 00576380 bytes ac861b94
- 00576324 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00576324 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00576324 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00576324 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00576364 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00576364 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00576364 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00576364 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00576324 bytes 73422e91
+ 00576364 bytes 73423e91
- 00576328 ["COPY", "register:4008:8", ["const:ca5000:8"]]
- 00576328 bytes 613900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-443ac1deb9c156c3edd56ee81fd3efc2"></a>

### [`0057636c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057636c.md) → [`005763ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md) FUN_005763ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550988.md) · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`005509c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509c8.md) · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005763f0",
      "incomplete_value": false,
      "site": "00576408",
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
            "const:2a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763b0",
      "incomplete_value": false,
      "site": "005763c8",
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
            "const:1da:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005763f8",
      "incomplete_value": false,
      "site": "00576408",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763b8",
      "incomplete_value": false,
      "site": "005763c8",
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
            "const:1ea:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005763f0",
      "PARAM",
      [
        "storage",
        "002a31da",
        null,
        "string"
      ]
    ],
    [
      "005763f8",
      "PARAM",
      [
        "storage",
        "002a31ea",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005763f0",
      "PARAM",
      [
        "storage",
        "002a32a7",
        null,
        "string"
      ]
    ],
    [
      "005763f8",
      "PARAM",
      [
        "storage",
        "002a32b7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057636c.md#insn-00576388) · [`005763c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057636c.md#insn-005763c8) · [`0057637c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057636c.md#insn-0057637c)
- 新版 [`005763c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-005763c8) · [`00576408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-00576408) · [`005763bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005763ac.md#insn-005763bc)

~~~diff
- 00576388 ["INT_ADD", "register:40f0:8", ["const:576388:8", "const:4:8"]]
- 00576388 ["CALL", null, ["callee:00589850:8"]]
+ 005763c8 ["INT_ADD", "register:40f0:8", ["const:5763c8:8", "const:4:8"]]
+ 005763c8 ["CALL", null, ["callee:00589850:8"]]
- 00576388 bytes 224d0094
+ 005763c8 bytes 224d0094
- 005763c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005763c8 ["INT_ADD", "register:40f0:8", ["const:5763c8:8", "const:4:8"]]
- 005763c8 ["CALLIND", null, ["register:0:8"]]
+ 00576408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00576408 ["INT_ADD", "register:40f0:8", ["const:576408:8", "const:4:8"]]
+ 00576408 ["CALLIND", null, ["register:0:8"]]
- 005763c8 bytes 00013fd6
+ 00576408 bytes 00013fd6
- 0057637c ["INT_ADD", "register:40f0:8", ["const:57637c:8", "const:4:8"]]
- 0057637c ["CALL", null, ["callee:00588e6c:8"]]
+ 005763bc ["INT_ADD", "register:40f0:8", ["const:5763bc:8", "const:4:8"]]
+ 005763bc ["CALL", null, ["callee:00588e6c:8"]]
- 0057637c bytes ac4a0094
+ 005763bc bytes ac4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b04c726ad3391643ee2be67167703672"></a>

### [`00576400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md) → [`00576440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md) FUN_00576440

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`005509cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509cc.md) · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576490",
      "incomplete_value": false,
      "site": "005764a8",
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
            "const:d52:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576450",
      "incomplete_value": false,
      "site": "00576468",
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
            "const:d12:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576498",
      "incomplete_value": false,
      "site": "005764a8",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576458",
      "incomplete_value": false,
      "site": "00576468",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576490",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00576498",
      "PARAM",
      [
        "storage",
        "002ad870",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576490",
      "PARAM",
      [
        "storage",
        "002b0d52",
        null,
        "string"
      ]
    ],
    [
      "00576498",
      "PARAM",
      [
        "storage",
        "002ad8b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md#insn-00576428) · [`00576468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md#insn-00576468) · [`0057641c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md#insn-0057641c)
- 新版 [`00576468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-00576468) · [`005764a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-005764a8) · [`0057645c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md#insn-0057645c)

~~~diff
- 00576428 ["INT_ADD", "register:40f0:8", ["const:576428:8", "const:4:8"]]
- 00576428 ["CALL", null, ["callee:00589850:8"]]
+ 00576468 ["INT_ADD", "register:40f0:8", ["const:576468:8", "const:4:8"]]
+ 00576468 ["CALL", null, ["callee:00589850:8"]]
- 00576428 bytes fa4c0094
+ 00576468 bytes fa4c0094
- 00576468 ["COPY", "register:0:8", ["register:4040:8"]]
- 00576468 ["INT_ADD", "register:40f0:8", ["const:576468:8", "const:4:8"]]
- 00576468 ["CALLIND", null, ["register:0:8"]]
+ 005764a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005764a8 ["INT_ADD", "register:40f0:8", ["const:5764a8:8", "const:4:8"]]
+ 005764a8 ["CALLIND", null, ["register:0:8"]]
- 00576468 bytes 00013fd6
+ 005764a8 bytes 00013fd6
- 0057641c ["INT_ADD", "register:40f0:8", ["const:57641c:8", "const:4:8"]]
- 0057641c ["CALL", null, ["callee:00588e6c:8"]]
+ 0057645c ["INT_ADD", "register:40f0:8", ["const:57645c:8", "const:4:8"]]
+ 0057645c ["CALL", null, ["callee:00588e6c:8"]]
- 0057641c bytes 844a0094
+ 0057645c bytes 844a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab1fdd4803df0a3e454d755989b1d6c2"></a>

### [`005764c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005764c0.md) → [`00576500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md) FUN_00576500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509b8.md) · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`005509f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509f8.md) · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576544",
      "incomplete_value": false,
      "site": "0057655c",
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
            "const:42b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576504",
      "incomplete_value": false,
      "site": "0057651c",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057654c",
      "incomplete_value": false,
      "site": "0057655c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:a8f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057650c",
      "incomplete_value": false,
      "site": "0057651c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:a4f:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576544",
      "PARAM",
      [
        "storage",
        "002ba3eb",
        null,
        "string"
      ]
    ],
    [
      "0057654c",
      "PARAM",
      [
        "storage",
        "002aea4f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00576544",
      "PARAM",
      [
        "storage",
        "002ba42b",
        null,
        "string"
      ]
    ],
    [
      "0057654c",
      "PARAM",
      [
        "storage",
        "002aea8f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005764dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005764c0.md#insn-005764dc) · [`0057651c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005764c0.md#insn-0057651c) · [`005764d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005764c0.md#insn-005764d0)
- 新版 [`0057651c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-0057651c) · [`0057655c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-0057655c) · [`00576510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576500.md#insn-00576510)

~~~diff
- 005764dc ["INT_ADD", "register:40f0:8", ["const:5764dc:8", "const:4:8"]]
- 005764dc ["CALL", null, ["callee:00589850:8"]]
+ 0057651c ["INT_ADD", "register:40f0:8", ["const:57651c:8", "const:4:8"]]
+ 0057651c ["CALL", null, ["callee:00589850:8"]]
- 005764dc bytes cd4c0094
+ 0057651c bytes cd4c0094
- 0057651c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057651c ["INT_ADD", "register:40f0:8", ["const:57651c:8", "const:4:8"]]
- 0057651c ["CALLIND", null, ["register:0:8"]]
+ 0057655c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057655c ["INT_ADD", "register:40f0:8", ["const:57655c:8", "const:4:8"]]
+ 0057655c ["CALLIND", null, ["register:0:8"]]
- 0057651c bytes 00013fd6
+ 0057655c bytes 00013fd6
- 005764d0 ["INT_ADD", "register:40f0:8", ["const:5764d0:8", "const:4:8"]]
- 005764d0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00576510 ["INT_ADD", "register:40f0:8", ["const:576510:8", "const:4:8"]]
+ 00576510 ["CALL", null, ["callee:00588e6c:8"]]
- 005764d0 bytes 574a0094
+ 00576510 bytes 574a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d001512fdf530d67940f3c55b2386e19"></a>

### [`0057657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057657c.md) → [`005765bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md) FUN_005765bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005509fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509fc.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005765f8",
      "incomplete_value": true,
      "site": "00576610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005765b8",
      "incomplete_value": true,
      "site": "005765d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ecb:8"
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
      "005765f8",
      "READ",
      [
        "storage",
        "002b4ecb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005765f8",
      "READ",
      [
        "storage",
        "002b4f0b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057657c.md#insn-00576610) · [`00576598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057657c.md#insn-00576598) · [`005765a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057657c.md#insn-005765a0)
- 新版 [`00576650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-00576650) · [`005765d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-005765d8) · [`005765e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765bc.md#insn-005765e0)

~~~diff
- 00576610 ["INT_ADD", "register:40f0:8", ["const:576610:8", "const:4:8"]]
- 00576610 ["CALL", null, ["callee:00589144:8"]]
+ 00576650 ["INT_ADD", "register:40f0:8", ["const:576650:8", "const:4:8"]]
+ 00576650 ["CALL", null, ["callee:00589144:8"]]
- 00576610 bytes bd4a0094
+ 00576650 bytes bd4a0094
- 00576598 ["INT_ADD", "register:40f0:8", ["const:576598:8", "const:4:8"]]
- 00576598 ["CALL", null, ["callee:00588e6c:8"]]
+ 005765d8 ["INT_ADD", "register:40f0:8", ["const:5765d8:8", "const:4:8"]]
+ 005765d8 ["CALL", null, ["callee:00588e6c:8"]]
- 00576598 bytes 254a0094
+ 005765d8 bytes 254a0094
- 005765a0 ["INT_ADD", "register:40f0:8", ["const:5765a0:8", "const:4:8"]]
- 005765a0 ["CALL", null, ["callee:0058915c:8"]]
+ 005765e0 ["INT_ADD", "register:40f0:8", ["const:5765e0:8", "const:4:8"]]
+ 005765e0 ["CALL", null, ["callee:0058915c:8"]]
- 005765a0 bytes df4a0094
+ 005765e0 bytes df4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09178895b0ddba17050eaecdf0c11219"></a>

### [`005766c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md) → [`00576700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md) FUN_00576700

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005767e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md) · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`00576828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576828.md) · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

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
      "definition_site": "00576728",
      "incomplete_value": true,
      "site": "0057672c",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005766e8",
      "incomplete_value": true,
      "site": "005766ec",
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
            "const:760:8"
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
      "0057672c",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ],
    [
      "00576750",
      "READ",
      [
        "storage",
        "002a31ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057672c",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ],
    [
      "00576750",
      "READ",
      [
        "storage",
        "002a32bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005766e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md#insn-005766e8) · [`005766f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md#insn-005766f0) · [`005766f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md#insn-005766f8)
- 新版 [`00576728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576728) · [`00576730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576730) · [`00576738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576700.md#insn-00576738)

~~~diff
- 005766e8 ["COPY", "tmp:0:8", ["const:760:8"]]
- 005766e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005766e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005766e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576728 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00576728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005766e8 bytes 08811d91
+ 00576728 bytes 08812d91
- 005766f0 ["INT_ADD", "register:40f0:8", ["const:5766f0:8", "const:4:8"]]
- 005766f0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00576730 ["INT_ADD", "register:40f0:8", ["const:576730:8", "const:4:8"]]
+ 00576730 ["CALL", null, ["callee:00588e6c:8"]]
- 005766f0 bytes cf490094
+ 00576730 bytes cf490094
- 005766f8 ["INT_ADD", "register:40f0:8", ["const:5766f8:8", "const:4:8"]]
- 005766f8 ["CALL", null, ["callee:0058915c:8"]]
+ 00576738 ["INT_ADD", "register:40f0:8", ["const:576738:8", "const:4:8"]]
+ 00576738 ["CALL", null, ["callee:0058915c:8"]]
- 005766f8 bytes 894a0094
+ 00576738 bytes 894a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3dd7db54880a933641eb1d93d4cf1e"></a>

### [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) → [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) FUN_0057699c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)
- 新版 呼出元 3件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576a10",
      "incomplete_value": true,
      "site": "00576a10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:515:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005769d0",
      "incomplete_value": true,
      "site": "005769d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4d5:8"
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
      "definition_site": "00576a14",
      "incomplete_value": true,
      "site": "00576a14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005769d4",
      "incomplete_value": true,
      "site": "005769d4",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576a00",
      "READ",
      [
        "storage",
        "002bb4d5",
        null,
        "string"
      ]
    ],
    [
      "00576a08",
      "READ",
      [
        "storage",
        "002bb4db",
        null,
        "string"
      ]
    ],
    [
      "00576a78",
      "READ",
      [
        "storage",
        "002c127b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576a00",
      "READ",
      [
        "storage",
        "002bb515",
        null,
        "string"
      ]
    ],
    [
      "00576a08",
      "READ",
      [
        "storage",
        "002bb51b",
        null,
        "string"
      ]
    ],
    [
      "00576a78",
      "READ",
      [
        "storage",
        "002c12bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005769a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md#insn-005769a0) · [`005769b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md#insn-005769b0) · [`005769bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md#insn-005769bc)
- 新版 [`005769e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769e0) · [`005769f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769f0) · [`005769fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md#insn-005769fc)

~~~diff
- 005769a0 ["INT_ADD", "register:40f0:8", ["const:5769a0:8", "const:4:8"]]
- 005769a0 ["CALL", null, ["callee:00588e6c:8"]]
+ 005769e0 ["INT_ADD", "register:40f0:8", ["const:5769e0:8", "const:4:8"]]
+ 005769e0 ["CALL", null, ["callee:00588e6c:8"]]
- 005769a0 bytes 23490094
+ 005769e0 bytes 23490094
- 005769b0 ["INT_ADD", "register:40f0:8", ["const:5769b0:8", "const:4:8"]]
- 005769b0 ["CALL", null, ["callee:0058915c:8"]]
+ 005769f0 ["INT_ADD", "register:40f0:8", ["const:5769f0:8", "const:4:8"]]
+ 005769f0 ["CALL", null, ["callee:0058915c:8"]]
- 005769b0 bytes db490094
+ 005769f0 bytes db490094
- 005769bc ["COPY", "tmp:0:8", ["const:4d5:8"]]
- 005769bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005769bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005769bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005769fc ["COPY", "tmp:0:8", ["const:515:8"]]
+ 005769fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005769fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005769fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005769bc bytes 29551391
+ 005769fc bytes 29551491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed27312f261e9a76ec5f5a2fbf15ce1"></a>

### [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) → [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) FUN_00576f08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 2件 [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576f68",
      "incomplete_value": true,
      "site": "00576f7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576f28",
      "incomplete_value": true,
      "site": "00576f3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e7:8"
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
      "definition_site": "00576f80",
      "incomplete_value": true,
      "site": "00576f80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00576f40",
      "incomplete_value": true,
      "site": "00576f40",
      "value": [
        "LOAD",
        "8",
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
      "00576f4c",
      "READ",
      [
        "storage",
        "002a42a7",
        null,
        "string"
      ]
    ],
    [
      "00576f54",
      "READ",
      [
        "storage",
        "002a42ad",
        null,
        "string"
      ]
    ],
    [
      "00576f68",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576f4c",
      "READ",
      [
        "storage",
        "002a4374",
        null,
        "string"
      ]
    ],
    [
      "00576f54",
      "READ",
      [
        "storage",
        "002a437a",
        null,
        "string"
      ]
    ],
    [
      "00576f68",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md#insn-00576efc) · [`00576ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md#insn-00576ef4) · [`00576f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md#insn-00576f08)
- 新版 [`00576f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f3c) · [`00576f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f34) · [`00576f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md#insn-00576f48)

~~~diff
- 00576efc ["INT_ADD", "register:40f0:8", ["const:576efc:8", "const:4:8"]]
- 00576efc ["CALL", null, ["callee:0058915c:8"]]
+ 00576f3c ["INT_ADD", "register:40f0:8", ["const:576f3c:8", "const:4:8"]]
+ 00576f3c ["CALL", null, ["callee:0058915c:8"]]
- 00576efc bytes 88480094
+ 00576f3c bytes 88480094
- 00576ef4 ["INT_ADD", "register:40f0:8", ["const:576ef4:8", "const:4:8"]]
- 00576ef4 ["CALL", null, ["callee:00588e6c:8"]]
+ 00576f34 ["INT_ADD", "register:40f0:8", ["const:576f34:8", "const:4:8"]]
+ 00576f34 ["CALL", null, ["callee:00588e6c:8"]]
- 00576ef4 bytes ce470094
+ 00576f34 bytes ce470094
- 00576f08 ["COPY", "tmp:0:8", ["const:2a7:8"]]
- 00576f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00576f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00576f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00576f48 ["COPY", "tmp:0:8", ["const:374:8"]]
+ 00576f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00576f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00576f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00576f08 bytes 299d0a91
+ 00576f48 bytes 29d10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b6b176fb119c42ee2a7b333a13c7e8"></a>

### [`0057710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md) → [`0057714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md) FUN_0057714c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005771a8",
      "incomplete_value": true,
      "site": "005771a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:755:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577168",
      "incomplete_value": true,
      "site": "00577168",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:715:8"
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
      "definition_site": "005771b0",
      "incomplete_value": true,
      "site": "005771b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00577170",
      "incomplete_value": true,
      "site": "00577170",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00577190",
      "READ",
      [
        "storage",
        "002bc715",
        null,
        "string"
      ]
    ],
    [
      "00577198",
      "READ",
      [
        "storage",
        "002bc71a",
        null,
        "string"
      ]
    ],
    [
      "005771ac",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00577190",
      "READ",
      [
        "storage",
        "002bc755",
        null,
        "string"
      ]
    ],
    [
      "00577198",
      "READ",
      [
        "storage",
        "002bc75a",
        null,
        "string"
      ]
    ],
    [
      "005771ac",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md#insn-00577138) · [`00577140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md#insn-00577140) · [`0057714c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md#insn-0057714c)
- 新版 [`00577178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-00577178) · [`00577180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-00577180) · [`0057718c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md#insn-0057718c)

~~~diff
- 00577138 ["INT_ADD", "register:40f0:8", ["const:577138:8", "const:4:8"]]
- 00577138 ["CALL", null, ["callee:00588e6c:8"]]
+ 00577178 ["INT_ADD", "register:40f0:8", ["const:577178:8", "const:4:8"]]
+ 00577178 ["CALL", null, ["callee:00588e6c:8"]]
- 00577138 bytes 3d470094
+ 00577178 bytes 3d470094
- 00577140 ["INT_ADD", "register:40f0:8", ["const:577140:8", "const:4:8"]]
- 00577140 ["CALL", null, ["callee:0058915c:8"]]
+ 00577180 ["INT_ADD", "register:40f0:8", ["const:577180:8", "const:4:8"]]
+ 00577180 ["CALL", null, ["callee:0058915c:8"]]
- 00577140 bytes f7470094
+ 00577180 bytes f7470094
- 0057714c ["COPY", "tmp:0:8", ["const:715:8"]]
- 0057714c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057714c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057714c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057718c ["COPY", "tmp:0:8", ["const:755:8"]]
+ 0057718c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057718c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057718c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057714c bytes 29551c91
+ 0057718c bytes 29551d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

