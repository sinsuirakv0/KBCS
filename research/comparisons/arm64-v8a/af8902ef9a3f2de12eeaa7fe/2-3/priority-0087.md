# v16.0.0 → v16.0.1 · 最優先の変更候補 (87)

[一覧の目次](README.md)

<a id="compare-e234eb7ea198a9e62a016131ca8a130a"></a>

### [`00bfe474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe474.md) → [`00bfe89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe89c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfe8c8",
      "incomplete_value": true,
      "site": "00bfe8c8",
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
      "definition_site": "00bfe4a0",
      "incomplete_value": true,
      "site": "00bfe4a0",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfe8c4",
      "incomplete_value": true,
      "site": "00bfe8cc",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfe49c",
      "incomplete_value": true,
      "site": "00bfe4a4",
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
            "const:18:8"
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
      "00bfe8b8",
      "READ",
      [
        "storage",
        "00c9b718",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8c8",
      "DATA",
      [
        "storage",
        "00c92a98",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8cc",
      "DATA",
      [
        "storage",
        "00c92a70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfe8b8",
      "READ",
      [
        "storage",
        "00c9bb18",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8c8",
      "DATA",
      [
        "storage",
        "00c92e98",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8cc",
      "DATA",
      [
        "storage",
        "00c92e70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfe490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe474.md#insn-00bfe490) · [`00bfe4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe474.md#insn-00bfe4ac)
- 新版 `00bfe8b8`（命令位置の公開資料なし） · `00bfe8d4`（命令位置の公開資料なし）

~~~diff
- 00bfe490 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:718:8"]]
- 00bfe490 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfe8b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 00bfe8b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfe490 bytes 088d43f9
+ 00bfe8b8 bytes 088d45f9
- 00bfe4ac ["INT_ADD", "register:40f0:8", ["const:bfe4ac:8", "const:4:8"]]
- 00bfe4ac ["CALL", null, ["callee:00c581e0:8"]]
+ 00bfe8d4 ["INT_ADD", "register:40f0:8", ["const:bfe8d4:8", "const:4:8"]]
+ 00bfe8d4 ["CALL", null, ["callee:00c581e0:8"]]
- 00bfe4ac bytes 4d660194
+ 00bfe8d4 bytes 43660194
~~~


<a id="compare-f935e25207e7e6e2175b6b2825b57704"></a>

### [`00bfe6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md) → [`00bfeafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfeafc.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfeb50",
      "incomplete_value": true,
      "site": "00bfeb54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfe728",
      "incomplete_value": true,
      "site": "00bfe72c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bfeb98",
      "incomplete_value": true,
      "site": "00bfeb9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfe770",
      "incomplete_value": true,
      "site": "00bfe774",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bfeb50",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfeb50",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfeb98",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfeb50",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bfeb50",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfeb98",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfe72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe72c) · [`00bfe774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe774) · [`00bfe700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe700)
- 新版 `00bfeb54`（命令位置の公開資料なし） · `00bfeb9c`（命令位置の公開資料なし） · `00bfeb28`（命令位置の公開資料なし）

~~~diff
- 00bfe72c ["INT_ADD", "register:40f0:8", ["const:bfe72c:8", "const:4:8"]]
- 00bfe72c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfeb54 ["INT_ADD", "register:40f0:8", ["const:bfeb54:8", "const:4:8"]]
+ 00bfeb54 ["CALL", null, ["callee:00c58280:8"]]
- 00bfe72c bytes d5650194
+ 00bfeb54 bytes cb650194
- 00bfe774 ["INT_ADD", "register:40f0:8", ["const:bfe774:8", "const:4:8"]]
- 00bfe774 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfeb9c ["INT_ADD", "register:40f0:8", ["const:bfeb9c:8", "const:4:8"]]
+ 00bfeb9c ["CALL", null, ["callee:00c58280:8"]]
- 00bfe774 bytes c3650194
+ 00bfeb9c bytes b9650194
- 00bfe700 ["INT_ADD", "register:40f0:8", ["const:bfe700:8", "const:4:8"]]
- 00bfe700 ["CALL", null, ["callee:00c58260:8"]]
+ 00bfeb28 ["INT_ADD", "register:40f0:8", ["const:bfeb28:8", "const:4:8"]]
+ 00bfeb28 ["CALL", null, ["callee:00c58260:8"]]
- 00bfe700 bytes d8650194
+ 00bfeb28 bytes ce650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c1f2b401889b49ff33d2006765bb627"></a>

### [`00bfe864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md) → [`00bfec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfec8c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfece0",
      "incomplete_value": true,
      "site": "00bfece4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfe8b8",
      "incomplete_value": true,
      "site": "00bfe8bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bfed28",
      "incomplete_value": true,
      "site": "00bfed2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfe900",
      "incomplete_value": true,
      "site": "00bfe904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bfece0",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfece0",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfed28",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfece0",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bfece0",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfed28",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfe8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe8bc) · [`00bfe904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe904) · [`00bfe890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe890)
- 新版 `00bfece4`（命令位置の公開資料なし） · `00bfed2c`（命令位置の公開資料なし） · `00bfecb8`（命令位置の公開資料なし）

~~~diff
- 00bfe8bc ["INT_ADD", "register:40f0:8", ["const:bfe8bc:8", "const:4:8"]]
- 00bfe8bc ["CALL", null, ["callee:00c58280:8"]]
+ 00bfece4 ["INT_ADD", "register:40f0:8", ["const:bfece4:8", "const:4:8"]]
+ 00bfece4 ["CALL", null, ["callee:00c58280:8"]]
- 00bfe8bc bytes 71650194
+ 00bfece4 bytes 67650194
- 00bfe904 ["INT_ADD", "register:40f0:8", ["const:bfe904:8", "const:4:8"]]
- 00bfe904 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfed2c ["INT_ADD", "register:40f0:8", ["const:bfed2c:8", "const:4:8"]]
+ 00bfed2c ["CALL", null, ["callee:00c58280:8"]]
- 00bfe904 bytes 5f650194
+ 00bfed2c bytes 55650194
- 00bfe890 ["INT_ADD", "register:40f0:8", ["const:bfe890:8", "const:4:8"]]
- 00bfe890 ["CALL", null, ["callee:00c58260:8"]]
+ 00bfecb8 ["INT_ADD", "register:40f0:8", ["const:bfecb8:8", "const:4:8"]]
+ 00bfecb8 ["CALL", null, ["callee:00c58260:8"]]
- 00bfe890 bytes 74650194
+ 00bfecb8 bytes 6a650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab285744fdac5262d77632ac5199790"></a>

### [`00bfe9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md) → [`00bfee1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfee1c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfee70",
      "incomplete_value": true,
      "site": "00bfee74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfea48",
      "incomplete_value": true,
      "site": "00bfea4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bfeeb8",
      "incomplete_value": true,
      "site": "00bfeebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfea90",
      "incomplete_value": true,
      "site": "00bfea94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bfee70",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfee70",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfeeb8",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfee70",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bfee70",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfeeb8",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfea4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md#insn-00bfea4c) · [`00bfea94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md#insn-00bfea94) · [`00bfea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md#insn-00bfea20)
- 新版 `00bfee74`（命令位置の公開資料なし） · `00bfeebc`（命令位置の公開資料なし） · `00bfee48`（命令位置の公開資料なし）

~~~diff
- 00bfea4c ["INT_ADD", "register:40f0:8", ["const:bfea4c:8", "const:4:8"]]
- 00bfea4c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfee74 ["INT_ADD", "register:40f0:8", ["const:bfee74:8", "const:4:8"]]
+ 00bfee74 ["CALL", null, ["callee:00c58280:8"]]
- 00bfea4c bytes 0d650194
+ 00bfee74 bytes 03650194
- 00bfea94 ["INT_ADD", "register:40f0:8", ["const:bfea94:8", "const:4:8"]]
- 00bfea94 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfeebc ["INT_ADD", "register:40f0:8", ["const:bfeebc:8", "const:4:8"]]
+ 00bfeebc ["CALL", null, ["callee:00c58280:8"]]
- 00bfea94 bytes fb640194
+ 00bfeebc bytes f1640194
- 00bfea20 ["INT_ADD", "register:40f0:8", ["const:bfea20:8", "const:4:8"]]
- 00bfea20 ["CALL", null, ["callee:00c58260:8"]]
+ 00bfee48 ["INT_ADD", "register:40f0:8", ["const:bfee48:8", "const:4:8"]]
+ 00bfee48 ["CALL", null, ["callee:00c58260:8"]]
- 00bfea20 bytes 10650194
+ 00bfee48 bytes 06650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6677facc252bb41b87db49a93b2c6b90"></a>

### [`00bfeb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md) → [`00bfefac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfefac.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bff004",
      "incomplete_value": true,
      "site": "00bff008",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfebdc",
      "incomplete_value": true,
      "site": "00bfebe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bff04c",
      "incomplete_value": true,
      "site": "00bff050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfec24",
      "incomplete_value": true,
      "site": "00bfec28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bff004",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bff004",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff04c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bff004",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bff004",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff04c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfebe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md#insn-00bfebe0) · [`00bfec28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md#insn-00bfec28) · [`00bfebb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md#insn-00bfebb4)
- 新版 `00bff008`（命令位置の公開資料なし） · `00bff050`（命令位置の公開資料なし） · `00bfefdc`（命令位置の公開資料なし）

~~~diff
- 00bfebe0 ["INT_ADD", "register:40f0:8", ["const:bfebe0:8", "const:4:8"]]
- 00bfebe0 ["CALL", null, ["callee:00c58280:8"]]
+ 00bff008 ["INT_ADD", "register:40f0:8", ["const:bff008:8", "const:4:8"]]
+ 00bff008 ["CALL", null, ["callee:00c58280:8"]]
- 00bfebe0 bytes a8640194
+ 00bff008 bytes 9e640194
- 00bfec28 ["INT_ADD", "register:40f0:8", ["const:bfec28:8", "const:4:8"]]
- 00bfec28 ["CALL", null, ["callee:00c58280:8"]]
+ 00bff050 ["INT_ADD", "register:40f0:8", ["const:bff050:8", "const:4:8"]]
+ 00bff050 ["CALL", null, ["callee:00c58280:8"]]
- 00bfec28 bytes 96640194
+ 00bff050 bytes 8c640194
- 00bfebb4 ["INT_ADD", "register:40f0:8", ["const:bfebb4:8", "const:4:8"]]
- 00bfebb4 ["CALL", null, ["callee:00c58260:8"]]
+ 00bfefdc ["INT_ADD", "register:40f0:8", ["const:bfefdc:8", "const:4:8"]]
+ 00bfefdc ["CALL", null, ["callee:00c58260:8"]]
- 00bfebb4 bytes ab640194
+ 00bfefdc bytes a1640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074a78d988a47189261e5799f7bdabf1"></a>

### [`00bfed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md) → [`00bff144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff144.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bff198",
      "incomplete_value": true,
      "site": "00bff19c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfed70",
      "incomplete_value": true,
      "site": "00bfed74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bff1e0",
      "incomplete_value": true,
      "site": "00bff1e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfedb8",
      "incomplete_value": true,
      "site": "00bfedbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bff198",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bff198",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff1e0",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bff198",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bff198",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff1e0",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md#insn-00bfed74) · [`00bfedbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md#insn-00bfedbc) · [`00bfed48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md#insn-00bfed48)
- 新版 `00bff19c`（命令位置の公開資料なし） · `00bff1e4`（命令位置の公開資料なし） · `00bff170`（命令位置の公開資料なし）

~~~diff
- 00bfed74 ["INT_ADD", "register:40f0:8", ["const:bfed74:8", "const:4:8"]]
- 00bfed74 ["CALL", null, ["callee:00c58280:8"]]
+ 00bff19c ["INT_ADD", "register:40f0:8", ["const:bff19c:8", "const:4:8"]]
+ 00bff19c ["CALL", null, ["callee:00c58280:8"]]
- 00bfed74 bytes 43640194
+ 00bff19c bytes 39640194
- 00bfedbc ["INT_ADD", "register:40f0:8", ["const:bfedbc:8", "const:4:8"]]
- 00bfedbc ["CALL", null, ["callee:00c58280:8"]]
+ 00bff1e4 ["INT_ADD", "register:40f0:8", ["const:bff1e4:8", "const:4:8"]]
+ 00bff1e4 ["CALL", null, ["callee:00c58280:8"]]
- 00bfedbc bytes 31640194
+ 00bff1e4 bytes 27640194
- 00bfed48 ["INT_ADD", "register:40f0:8", ["const:bfed48:8", "const:4:8"]]
- 00bfed48 ["CALL", null, ["callee:00c58260:8"]]
+ 00bff170 ["INT_ADD", "register:40f0:8", ["const:bff170:8", "const:4:8"]]
+ 00bff170 ["CALL", null, ["callee:00c58260:8"]]
- 00bfed48 bytes 46640194
+ 00bff170 bytes 3c640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7596fafbe0484297dbf13d53c28cfa9"></a>

### [`00bfeeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md) → [`00bff2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff2d4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bff328",
      "incomplete_value": true,
      "site": "00bff32c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfef00",
      "incomplete_value": true,
      "site": "00bfef04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
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
      "definition_site": "00bff370",
      "incomplete_value": true,
      "site": "00bff374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bfef48",
      "incomplete_value": true,
      "site": "00bfef4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bff328",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bff328",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff370",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bff328",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00bff328",
      "PARAM",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bff370",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfef04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfef04) · [`00bfef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfef4c) · [`00bfeed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfeed8)
- 新版 `00bff32c`（命令位置の公開資料なし） · `00bff374`（命令位置の公開資料なし） · `00bff300`（命令位置の公開資料なし）

~~~diff
- 00bfef04 ["INT_ADD", "register:40f0:8", ["const:bfef04:8", "const:4:8"]]
- 00bfef04 ["CALL", null, ["callee:00c58280:8"]]
+ 00bff32c ["INT_ADD", "register:40f0:8", ["const:bff32c:8", "const:4:8"]]
+ 00bff32c ["CALL", null, ["callee:00c58280:8"]]
- 00bfef04 bytes df630194
+ 00bff32c bytes d5630194
- 00bfef4c ["INT_ADD", "register:40f0:8", ["const:bfef4c:8", "const:4:8"]]
- 00bfef4c ["CALL", null, ["callee:00c58280:8"]]
+ 00bff374 ["INT_ADD", "register:40f0:8", ["const:bff374:8", "const:4:8"]]
+ 00bff374 ["CALL", null, ["callee:00c58280:8"]]
- 00bfef4c bytes cd630194
+ 00bff374 bytes c3630194
- 00bfeed8 ["INT_ADD", "register:40f0:8", ["const:bfeed8:8", "const:4:8"]]
- 00bfeed8 ["CALL", null, ["callee:00c58260:8"]]
+ 00bff300 ["INT_ADD", "register:40f0:8", ["const:bff300:8", "const:4:8"]]
+ 00bff300 ["CALL", null, ["callee:00c58260:8"]]
- 00bfeed8 bytes e2630194
+ 00bff300 bytes d8630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d54047330897c62ce26675221ceb97"></a>

### [`00bff3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md) → [`00bff7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff7e4.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bff810",
      "incomplete_value": true,
      "site": "00bff810",
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
      "definition_site": "00bff3e8",
      "incomplete_value": true,
      "site": "00bff3e8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bff814",
      "incomplete_value": true,
      "site": "00bff814",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bff3ec",
      "incomplete_value": true,
      "site": "00bff3ec",
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
            "const:18:8"
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
      "definition_site": "00bff834",
      "incomplete_value": true,
      "site": "00bff840",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bff40c",
      "incomplete_value": true,
      "site": "00bff418",
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
            "const:18:8"
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
      "00bff800",
      "READ",
      [
        "storage",
        "00c9b720",
        null,
        "pointer"
      ]
    ],
    [
      "00bff810",
      "DATA",
      [
        "storage",
        "00c92f58",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bff814",
      "DATA",
      [
        "storage",
        "00c92f30",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bff800",
      "READ",
      [
        "storage",
        "00c9bb20",
        null,
        "pointer"
      ]
    ],
    [
      "00bff810",
      "DATA",
      [
        "storage",
        "00c93358",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bff814",
      "DATA",
      [
        "storage",
        "00c93330",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bff3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff3d8) · [`00bff3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff3f4) · [`00bff400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff400)
- 新版 `00bff800`（命令位置の公開資料なし） · `00bff81c`（命令位置の公開資料なし） · `00bff828`（命令位置の公開資料なし）

~~~diff
- 00bff3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:720:8"]]
- 00bff3d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bff800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b20:8"]]
+ 00bff800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bff3d8 bytes 089143f9
+ 00bff800 bytes 089145f9
- 00bff3f4 ["INT_ADD", "register:40f0:8", ["const:bff3f4:8", "const:4:8"]]
- 00bff3f4 ["CALL", null, ["callee:00c581e0:8"]]
+ 00bff81c ["INT_ADD", "register:40f0:8", ["const:bff81c:8", "const:4:8"]]
+ 00bff81c ["CALL", null, ["callee:00c581e0:8"]]
- 00bff3f4 bytes 7b620194
+ 00bff81c bytes 71620194
- 00bff400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:728:8"]]
- 00bff400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bff828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b28:8"]]
+ 00bff828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bff400 bytes 089543f9
+ 00bff828 bytes 089545f9
~~~


<a id="compare-ecae819ea11027bc34a7e3b5e312c256"></a>

### [`00bff8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md) → [`00bffd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffd08.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfe0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 1件 [`00c5e3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3e0.md) · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bffd28",
      "incomplete_value": true,
      "site": "00bffd28",
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
      "definition_site": "00bff900",
      "incomplete_value": true,
      "site": "00bff900",
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
      "00bffd20",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "00bffd28",
      "DATA",
      [
        "storage",
        "00c92b78",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bffd20",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bffd28",
      "DATA",
      [
        "storage",
        "00c92f78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bff8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md#insn-00bff8f8) · [`00bff904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md#insn-00bff904)
- 新版 `00bffd20`（命令位置の公開資料なし） · `00bffd2c`（命令位置の公開資料なし）

~~~diff
- 00bff8f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:730:8"]]
- 00bff8f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bffd20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00bffd20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bff8f8 bytes 089943f9
+ 00bffd20 bytes 089945f9
- 00bff904 ["INT_ADD", "register:40f0:8", ["const:bff904:8", "const:4:8"]]
- 00bff904 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bffd2c ["INT_ADD", "register:40f0:8", ["const:bffd2c:8", "const:4:8"]]
+ 00bffd2c ["CALL", null, ["callee:00c5a7a0:8"]]
- 00bff904 bytes a76a0194
+ 00bffd2c bytes 9d6a0194
~~~


<a id="compare-faf079cbfa1188833325054dc78347b0"></a>

### [`00bff924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md) → [`00bffd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffd4c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bffd74",
      "incomplete_value": true,
      "site": "00bffd74",
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
      "definition_site": "00bff94c",
      "incomplete_value": true,
      "site": "00bff94c",
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
      "00bffd68",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "00bffd74",
      "DATA",
      [
        "storage",
        "00c92b78",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bffd68",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bffd74",
      "DATA",
      [
        "storage",
        "00c92f78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bff940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md#insn-00bff940) · [`00bff950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md#insn-00bff950)
- 新版 `00bffd68`（命令位置の公開資料なし） · `00bffd78`（命令位置の公開資料なし）

~~~diff
- 00bff940 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:730:8"]]
- 00bff940 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bffd68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00bffd68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bff940 bytes 089943f9
+ 00bffd68 bytes 089945f9
- 00bff950 ["INT_ADD", "register:40f0:8", ["const:bff950:8", "const:4:8"]]
- 00bff950 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bffd78 ["INT_ADD", "register:40f0:8", ["const:bffd78:8", "const:4:8"]]
+ 00bffd78 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bff950 bytes a06a0194
+ 00bffd78 bytes 966a0194
~~~


<a id="compare-a9fdc0a0dcaa16a39f2cdbe624349196"></a>

### [`00bffd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md) → [`00c001b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c001b0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c001dc",
      "incomplete_value": true,
      "site": "00c001dc",
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
      "definition_site": "00bffdb4",
      "incomplete_value": true,
      "site": "00bffdb4",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c001e0",
      "incomplete_value": true,
      "site": "00c001e0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bffdb8",
      "incomplete_value": true,
      "site": "00bffdb8",
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
            "const:18:8"
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
      "00c001cc",
      "READ",
      [
        "storage",
        "00c9b738",
        null,
        "pointer"
      ]
    ],
    [
      "00c001dc",
      "DATA",
      [
        "storage",
        "00c92c28",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00c001e0",
      "DATA",
      [
        "storage",
        "00c92c00",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c001cc",
      "READ",
      [
        "storage",
        "00c9bb38",
        null,
        "pointer"
      ]
    ],
    [
      "00c001dc",
      "DATA",
      [
        "storage",
        "00c93028",
        null,
        "pointer"
      ]
    ],
    [
      "00c001e0",
      "DATA",
      [
        "storage",
        "00c93000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bffda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md#insn-00bffda4) · [`00bffdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md#insn-00bffdc0)
- 新版 `00c001cc`（命令位置の公開資料なし） · `00c001e8`（命令位置の公開資料なし）

~~~diff
- 00bffda4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:738:8"]]
- 00bffda4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c001cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00c001cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bffda4 bytes 089d43f9
+ 00c001cc bytes 089d45f9
- 00bffdc0 ["INT_ADD", "register:40f0:8", ["const:bffdc0:8", "const:4:8"]]
- 00bffdc0 ["CALL", null, ["callee:00c581e0:8"]]
+ 00c001e8 ["INT_ADD", "register:40f0:8", ["const:c001e8:8", "const:4:8"]]
+ 00c001e8 ["CALL", null, ["callee:00c581e0:8"]]
- 00bffdc0 bytes 08600194
+ 00c001e8 bytes fe5f0194
~~~


<a id="compare-614bd4045480f7d9f2f5348c512599b0"></a>

### [`00bffef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md) → [`00c0031c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0031c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c003ac",
      "incomplete_value": true,
      "site": "00c003b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfff84",
      "incomplete_value": true,
      "site": "00bfff88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c003ac",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c003ac",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c003ac",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c003ac",
      "PARAM",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfff88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff88) · [`00bfff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff54) · [`00bfff78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff78)
- 新版 `00c003b0`（命令位置の公開資料なし） · `00c0037c`（命令位置の公開資料なし） · `00c003a0`（命令位置の公開資料なし）

~~~diff
- 00bfff88 ["INT_ADD", "register:40f0:8", ["const:bfff88:8", "const:4:8"]]
- 00bfff88 ["CALL", null, ["callee:00c58280:8"]]
+ 00c003b0 ["INT_ADD", "register:40f0:8", ["const:c003b0:8", "const:4:8"]]
+ 00c003b0 ["CALL", null, ["callee:00c58280:8"]]
- 00bfff88 bytes be5f0194
+ 00c003b0 bytes b45f0194
- 00bfff54 ["INT_ADD", "register:40f0:8", ["const:bfff54:8", "const:4:8"]]
- 00bfff54 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c0037c ["INT_ADD", "register:40f0:8", ["const:c0037c:8", "const:4:8"]]
+ 00c0037c ["CALL", null, ["callee:00c5e3f0:8"]]
- 00bfff54 bytes 27780194
+ 00c0037c bytes 1d780194
- 00bfff78 ["INT_ADD", "register:40f0:8", ["const:bfff78:8", "const:4:8"]]
- 00bfff78 ["CALL", null, ["callee:00c58270:8"]]
+ 00c003a0 ["INT_ADD", "register:40f0:8", ["const:c003a0:8", "const:4:8"]]
+ 00c003a0 ["CALL", null, ["callee:00c58270:8"]]
- 00bfff78 bytes be5f0194
+ 00c003a0 bytes b45f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a5a7d73d3623766a1004d6b93092f4"></a>

### [`00c003fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md) → [`00c00824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00824.md) FUN_00c00824

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c003f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003f4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c0081c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0081c.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00878",
      "incomplete_value": true,
      "site": "00c0087c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00450",
      "incomplete_value": true,
      "site": "00c00454",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c00878",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00878",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c00878",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c00878",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00454) · [`00c00428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00428) · [`00c00444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00444)
- 新版 `00c0087c`（命令位置の公開資料なし） · `00c00850`（命令位置の公開資料なし） · `00c0086c`（命令位置の公開資料なし）

~~~diff
- 00c00454 ["INT_ADD", "register:40f0:8", ["const:c00454:8", "const:4:8"]]
- 00c00454 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0087c ["INT_ADD", "register:40f0:8", ["const:c0087c:8", "const:4:8"]]
+ 00c0087c ["CALL", null, ["callee:00c58280:8"]]
- 00c00454 bytes 8b5e0194
+ 00c0087c bytes 815e0194
- 00c00428 ["INT_ADD", "register:40f0:8", ["const:c00428:8", "const:4:8"]]
- 00c00428 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00850 ["INT_ADD", "register:40f0:8", ["const:c00850:8", "const:4:8"]]
+ 00c00850 ["CALL", null, ["callee:00c5e420:8"]]
- 00c00428 bytes fe760194
+ 00c00850 bytes f4760194
- 00c00444 ["INT_ADD", "register:40f0:8", ["const:c00444:8", "const:4:8"]]
- 00c00444 ["CALL", null, ["callee:00c58270:8"]]
+ 00c0086c ["INT_ADD", "register:40f0:8", ["const:c0086c:8", "const:4:8"]]
+ 00c0086c ["CALL", null, ["callee:00c58270:8"]]
- 00c00444 bytes 8b5e0194
+ 00c0086c bytes 815e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a87b1e844f5cb2b886c64201c27575"></a>

### [`00c00534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md) → [`00c0095c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0095c.md) FUN_00c0095c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c0052c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00954.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c009b0",
      "incomplete_value": true,
      "site": "00c009b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00588",
      "incomplete_value": true,
      "site": "00c0058c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c009b0",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c009b0",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c009b0",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c009b0",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0058c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c0058c) · [`00c00560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c00560) · [`00c0057c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c0057c)
- 新版 `00c009b4`（命令位置の公開資料なし） · `00c00988`（命令位置の公開資料なし） · `00c009a4`（命令位置の公開資料なし）

~~~diff
- 00c0058c ["INT_ADD", "register:40f0:8", ["const:c0058c:8", "const:4:8"]]
- 00c0058c ["CALL", null, ["callee:00c58280:8"]]
+ 00c009b4 ["INT_ADD", "register:40f0:8", ["const:c009b4:8", "const:4:8"]]
+ 00c009b4 ["CALL", null, ["callee:00c58280:8"]]
- 00c0058c bytes 3d5e0194
+ 00c009b4 bytes 335e0194
- 00c00560 ["INT_ADD", "register:40f0:8", ["const:c00560:8", "const:4:8"]]
- 00c00560 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00988 ["INT_ADD", "register:40f0:8", ["const:c00988:8", "const:4:8"]]
+ 00c00988 ["CALL", null, ["callee:00c5e420:8"]]
- 00c00560 bytes b0760194
+ 00c00988 bytes a6760194
- 00c0057c ["INT_ADD", "register:40f0:8", ["const:c0057c:8", "const:4:8"]]
- 00c0057c ["CALL", null, ["callee:00c58270:8"]]
+ 00c009a4 ["INT_ADD", "register:40f0:8", ["const:c009a4:8", "const:4:8"]]
+ 00c009a4 ["CALL", null, ["callee:00c58270:8"]]
- 00c0057c bytes 3d5e0194
+ 00c009a4 bytes 335e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3b561f7e5f832539c195c83f5d71ca8"></a>

### [`00c006ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md) → [`00c00ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00ad4.md) FUN_00c00ad4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c006a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006a4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00acc.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00b28",
      "incomplete_value": true,
      "site": "00c00b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00700",
      "incomplete_value": true,
      "site": "00c00704",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c00b28",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00b28",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c00b28",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c00b28",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c00704) · [`00c006d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c006d8) · [`00c006f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c006f4)
- 新版 `00c00b2c`（命令位置の公開資料なし） · `00c00b00`（命令位置の公開資料なし） · `00c00b1c`（命令位置の公開資料なし）

~~~diff
- 00c00704 ["INT_ADD", "register:40f0:8", ["const:c00704:8", "const:4:8"]]
- 00c00704 ["CALL", null, ["callee:00c58280:8"]]
+ 00c00b2c ["INT_ADD", "register:40f0:8", ["const:c00b2c:8", "const:4:8"]]
+ 00c00b2c ["CALL", null, ["callee:00c58280:8"]]
- 00c00704 bytes df5d0194
+ 00c00b2c bytes d55d0194
- 00c006d8 ["INT_ADD", "register:40f0:8", ["const:c006d8:8", "const:4:8"]]
- 00c006d8 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00b00 ["INT_ADD", "register:40f0:8", ["const:c00b00:8", "const:4:8"]]
+ 00c00b00 ["CALL", null, ["callee:00c5e420:8"]]
- 00c006d8 bytes 52760194
+ 00c00b00 bytes 48760194
- 00c006f4 ["INT_ADD", "register:40f0:8", ["const:c006f4:8", "const:4:8"]]
- 00c006f4 ["CALL", null, ["callee:00c58270:8"]]
+ 00c00b1c ["INT_ADD", "register:40f0:8", ["const:c00b1c:8", "const:4:8"]]
+ 00c00b1c ["CALL", null, ["callee:00c58270:8"]]
- 00c006f4 bytes df5d0194
+ 00c00b1c bytes d55d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c874dd20b5b35cde25ec0d157a94b94c"></a>

### [`00c007e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md) → [`00c00c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00c0c.md) FUN_00c00c0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c007dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007dc.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00c04.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00c60",
      "incomplete_value": true,
      "site": "00c00c64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00838",
      "incomplete_value": true,
      "site": "00c0083c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c00c60",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00c60",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c00c60",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c00c60",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c0083c) · [`00c00810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c00810) · [`00c0082c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c0082c)
- 新版 `00c00c64`（命令位置の公開資料なし） · `00c00c38`（命令位置の公開資料なし） · `00c00c54`（命令位置の公開資料なし）

~~~diff
- 00c0083c ["INT_ADD", "register:40f0:8", ["const:c0083c:8", "const:4:8"]]
- 00c0083c ["CALL", null, ["callee:00c58280:8"]]
+ 00c00c64 ["INT_ADD", "register:40f0:8", ["const:c00c64:8", "const:4:8"]]
+ 00c00c64 ["CALL", null, ["callee:00c58280:8"]]
- 00c0083c bytes 915d0194
+ 00c00c64 bytes 875d0194
- 00c00810 ["INT_ADD", "register:40f0:8", ["const:c00810:8", "const:4:8"]]
- 00c00810 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00c38 ["INT_ADD", "register:40f0:8", ["const:c00c38:8", "const:4:8"]]
+ 00c00c38 ["CALL", null, ["callee:00c5e420:8"]]
- 00c00810 bytes 04760194
+ 00c00c38 bytes fa750194
- 00c0082c ["INT_ADD", "register:40f0:8", ["const:c0082c:8", "const:4:8"]]
- 00c0082c ["CALL", null, ["callee:00c58270:8"]]
+ 00c00c54 ["INT_ADD", "register:40f0:8", ["const:c00c54:8", "const:4:8"]]
+ 00c00c54 ["CALL", null, ["callee:00c58270:8"]]
- 00c0082c bytes 915d0194
+ 00c00c54 bytes 875d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62082a330e9b276c3c3bf94771e6777"></a>

### [`00c00960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md) → [`00c00d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00d88.md) FUN_00c00d88

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00958.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00d80.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00ddc",
      "incomplete_value": true,
      "site": "00c00de0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c009b4",
      "incomplete_value": true,
      "site": "00c009b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c00ddc",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00ddc",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c00ddc",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c00ddc",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c009b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c009b8) · [`00c0098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c0098c) · [`00c009a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c009a8)
- 新版 `00c00de0`（命令位置の公開資料なし） · `00c00db4`（命令位置の公開資料なし） · `00c00dd0`（命令位置の公開資料なし）

~~~diff
- 00c009b8 ["INT_ADD", "register:40f0:8", ["const:c009b8:8", "const:4:8"]]
- 00c009b8 ["CALL", null, ["callee:00c58280:8"]]
+ 00c00de0 ["INT_ADD", "register:40f0:8", ["const:c00de0:8", "const:4:8"]]
+ 00c00de0 ["CALL", null, ["callee:00c58280:8"]]
- 00c009b8 bytes 325d0194
+ 00c00de0 bytes 285d0194
- 00c0098c ["INT_ADD", "register:40f0:8", ["const:c0098c:8", "const:4:8"]]
- 00c0098c ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00db4 ["INT_ADD", "register:40f0:8", ["const:c00db4:8", "const:4:8"]]
+ 00c00db4 ["CALL", null, ["callee:00c5e420:8"]]
- 00c0098c bytes a5750194
+ 00c00db4 bytes 9b750194
- 00c009a8 ["INT_ADD", "register:40f0:8", ["const:c009a8:8", "const:4:8"]]
- 00c009a8 ["CALL", null, ["callee:00c58270:8"]]
+ 00c00dd0 ["INT_ADD", "register:40f0:8", ["const:c00dd0:8", "const:4:8"]]
+ 00c00dd0 ["CALL", null, ["callee:00c58270:8"]]
- 00c009a8 bytes 325d0194
+ 00c00dd0 bytes 285d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0837acbacbb95236cc9e3a41d0ac7b"></a>

### [`00c00a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md) → [`00c00ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00ec0.md) FUN_00c00ec0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a90.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00eb8.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00f14",
      "incomplete_value": true,
      "site": "00c00f18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00aec",
      "incomplete_value": true,
      "site": "00c00af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c00f14",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00f14",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c00f14",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c00f14",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00af0) · [`00c00ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00ac4) · [`00c00ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00ae0)
- 新版 `00c00f18`（命令位置の公開資料なし） · `00c00eec`（命令位置の公開資料なし） · `00c00f08`（命令位置の公開資料なし）

~~~diff
- 00c00af0 ["INT_ADD", "register:40f0:8", ["const:c00af0:8", "const:4:8"]]
- 00c00af0 ["CALL", null, ["callee:00c58280:8"]]
+ 00c00f18 ["INT_ADD", "register:40f0:8", ["const:c00f18:8", "const:4:8"]]
+ 00c00f18 ["CALL", null, ["callee:00c58280:8"]]
- 00c00af0 bytes e45c0194
+ 00c00f18 bytes da5c0194
- 00c00ac4 ["INT_ADD", "register:40f0:8", ["const:c00ac4:8", "const:4:8"]]
- 00c00ac4 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c00eec ["INT_ADD", "register:40f0:8", ["const:c00eec:8", "const:4:8"]]
+ 00c00eec ["CALL", null, ["callee:00c5e420:8"]]
- 00c00ac4 bytes 57750194
+ 00c00eec bytes 4d750194
- 00c00ae0 ["INT_ADD", "register:40f0:8", ["const:c00ae0:8", "const:4:8"]]
- 00c00ae0 ["CALL", null, ["callee:00c58270:8"]]
+ 00c00f08 ["INT_ADD", "register:40f0:8", ["const:c00f08:8", "const:4:8"]]
+ 00c00f08 ["CALL", null, ["callee:00c58270:8"]]
- 00c00ae0 bytes e45c0194
+ 00c00f08 bytes da5c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970840271635e207c70f8dd674ae4244"></a>

### [`00c00bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md) → [`00c00ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00ff8.md) FUN_00c00ff8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bc8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c00ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00ff0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0104c",
      "incomplete_value": true,
      "site": "00c01050",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00c24",
      "incomplete_value": true,
      "site": "00c00c28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c0104c",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c0104c",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0104c",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c0104c",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00c28) · [`00c00bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00bfc) · [`00c00c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00c18)
- 新版 `00c01050`（命令位置の公開資料なし） · `00c01024`（命令位置の公開資料なし） · `00c01040`（命令位置の公開資料なし）

~~~diff
- 00c00c28 ["INT_ADD", "register:40f0:8", ["const:c00c28:8", "const:4:8"]]
- 00c00c28 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01050 ["INT_ADD", "register:40f0:8", ["const:c01050:8", "const:4:8"]]
+ 00c01050 ["CALL", null, ["callee:00c58280:8"]]
- 00c00c28 bytes 965c0194
+ 00c01050 bytes 8c5c0194
- 00c00bfc ["INT_ADD", "register:40f0:8", ["const:c00bfc:8", "const:4:8"]]
- 00c00bfc ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01024 ["INT_ADD", "register:40f0:8", ["const:c01024:8", "const:4:8"]]
+ 00c01024 ["CALL", null, ["callee:00c5e420:8"]]
- 00c00bfc bytes 09750194
+ 00c01024 bytes ff740194
- 00c00c18 ["INT_ADD", "register:40f0:8", ["const:c00c18:8", "const:4:8"]]
- 00c00c18 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01040 ["INT_ADD", "register:40f0:8", ["const:c01040:8", "const:4:8"]]
+ 00c01040 ["CALL", null, ["callee:00c58270:8"]]
- 00c00c18 bytes 965c0194
+ 00c01040 bytes 8c5c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00cd3e59c3845f5b04c56244589c8b3f"></a>

### [`00c00d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md) → [`00c01130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01130.md) FUN_00c01130

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d00.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c01128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01128.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01184",
      "incomplete_value": true,
      "site": "00c01188",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00d5c",
      "incomplete_value": true,
      "site": "00c00d60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c01184",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c01184",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c01184",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c01184",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d60) · [`00c00d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d34) · [`00c00d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d50)
- 新版 `00c01188`（命令位置の公開資料なし） · `00c0115c`（命令位置の公開資料なし） · `00c01178`（命令位置の公開資料なし）

~~~diff
- 00c00d60 ["INT_ADD", "register:40f0:8", ["const:c00d60:8", "const:4:8"]]
- 00c00d60 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01188 ["INT_ADD", "register:40f0:8", ["const:c01188:8", "const:4:8"]]
+ 00c01188 ["CALL", null, ["callee:00c58280:8"]]
- 00c00d60 bytes 485c0194
+ 00c01188 bytes 3e5c0194
- 00c00d34 ["INT_ADD", "register:40f0:8", ["const:c00d34:8", "const:4:8"]]
- 00c00d34 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c0115c ["INT_ADD", "register:40f0:8", ["const:c0115c:8", "const:4:8"]]
+ 00c0115c ["CALL", null, ["callee:00c5e420:8"]]
- 00c00d34 bytes bb740194
+ 00c0115c bytes b1740194
- 00c00d50 ["INT_ADD", "register:40f0:8", ["const:c00d50:8", "const:4:8"]]
- 00c00d50 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01178 ["INT_ADD", "register:40f0:8", ["const:c01178:8", "const:4:8"]]
+ 00c01178 ["CALL", null, ["callee:00c58270:8"]]
- 00c00d50 bytes 485c0194
+ 00c01178 bytes 3e5c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ed362f2cc15248b76c68999fcb75118"></a>

### [`00c00e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md) → [`00c01268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01268.md) FUN_00c01268

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e38.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c01260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01260.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c012bc",
      "incomplete_value": true,
      "site": "00c012c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00e94",
      "incomplete_value": true,
      "site": "00c00e98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c012bc",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c012bc",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c012bc",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c012bc",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00e98) · [`00c00e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00e6c) · [`00c00e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00e88)
- 新版 `00c012c0`（命令位置の公開資料なし） · `00c01294`（命令位置の公開資料なし） · `00c012b0`（命令位置の公開資料なし）

~~~diff
- 00c00e98 ["INT_ADD", "register:40f0:8", ["const:c00e98:8", "const:4:8"]]
- 00c00e98 ["CALL", null, ["callee:00c58280:8"]]
+ 00c012c0 ["INT_ADD", "register:40f0:8", ["const:c012c0:8", "const:4:8"]]
+ 00c012c0 ["CALL", null, ["callee:00c58280:8"]]
- 00c00e98 bytes fa5b0194
+ 00c012c0 bytes f05b0194
- 00c00e6c ["INT_ADD", "register:40f0:8", ["const:c00e6c:8", "const:4:8"]]
- 00c00e6c ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01294 ["INT_ADD", "register:40f0:8", ["const:c01294:8", "const:4:8"]]
+ 00c01294 ["CALL", null, ["callee:00c5e420:8"]]
- 00c00e6c bytes 6d740194
+ 00c01294 bytes 63740194
- 00c00e88 ["INT_ADD", "register:40f0:8", ["const:c00e88:8", "const:4:8"]]
- 00c00e88 ["CALL", null, ["callee:00c58270:8"]]
+ 00c012b0 ["INT_ADD", "register:40f0:8", ["const:c012b0:8", "const:4:8"]]
+ 00c012b0 ["CALL", null, ["callee:00c58270:8"]]
- 00c00e88 bytes fa5b0194
+ 00c012b0 bytes f05b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46ca1f541fcca8a2abcfd5a9f5698fd0"></a>

### [`00c00f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md) → [`00c013a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c013a0.md) FUN_00c013a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c00f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f70.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c01398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01398.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c013f4",
      "incomplete_value": true,
      "site": "00c013f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c00fcc",
      "incomplete_value": true,
      "site": "00c00fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c013f4",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c013f4",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c013f4",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c013f4",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c00fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c00fd0) · [`00c00fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c00fa4) · [`00c00fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c00fc0)
- 新版 `00c013f8`（命令位置の公開資料なし） · `00c013cc`（命令位置の公開資料なし） · `00c013e8`（命令位置の公開資料なし）

~~~diff
- 00c00fd0 ["INT_ADD", "register:40f0:8", ["const:c00fd0:8", "const:4:8"]]
- 00c00fd0 ["CALL", null, ["callee:00c58280:8"]]
+ 00c013f8 ["INT_ADD", "register:40f0:8", ["const:c013f8:8", "const:4:8"]]
+ 00c013f8 ["CALL", null, ["callee:00c58280:8"]]
- 00c00fd0 bytes ac5b0194
+ 00c013f8 bytes a25b0194
- 00c00fa4 ["INT_ADD", "register:40f0:8", ["const:c00fa4:8", "const:4:8"]]
- 00c00fa4 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c013cc ["INT_ADD", "register:40f0:8", ["const:c013cc:8", "const:4:8"]]
+ 00c013cc ["CALL", null, ["callee:00c5e420:8"]]
- 00c00fa4 bytes 1f740194
+ 00c013cc bytes 15740194
- 00c00fc0 ["INT_ADD", "register:40f0:8", ["const:c00fc0:8", "const:4:8"]]
- 00c00fc0 ["CALL", null, ["callee:00c58270:8"]]
+ 00c013e8 ["INT_ADD", "register:40f0:8", ["const:c013e8:8", "const:4:8"]]
+ 00c013e8 ["CALL", null, ["callee:00c58270:8"]]
- 00c00fc0 bytes ac5b0194
+ 00c013e8 bytes a25b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aac1e3ebb509db42c6df762685d057b"></a>

### [`00c010b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md) → [`00c014d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c014d8.md) FUN_00c014d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c010a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010a8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c014d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c014d0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0152c",
      "incomplete_value": true,
      "site": "00c01530",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c01104",
      "incomplete_value": true,
      "site": "00c01108",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c0152c",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c0152c",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0152c",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c0152c",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c01108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md#insn-00c01108) · [`00c010dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md#insn-00c010dc) · [`00c010f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md#insn-00c010f8)
- 新版 `00c01530`（命令位置の公開資料なし） · `00c01504`（命令位置の公開資料なし） · `00c01520`（命令位置の公開資料なし）

~~~diff
- 00c01108 ["INT_ADD", "register:40f0:8", ["const:c01108:8", "const:4:8"]]
- 00c01108 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01530 ["INT_ADD", "register:40f0:8", ["const:c01530:8", "const:4:8"]]
+ 00c01530 ["CALL", null, ["callee:00c58280:8"]]
- 00c01108 bytes 5e5b0194
+ 00c01530 bytes 545b0194
- 00c010dc ["INT_ADD", "register:40f0:8", ["const:c010dc:8", "const:4:8"]]
- 00c010dc ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01504 ["INT_ADD", "register:40f0:8", ["const:c01504:8", "const:4:8"]]
+ 00c01504 ["CALL", null, ["callee:00c5e420:8"]]
- 00c010dc bytes d1730194
+ 00c01504 bytes c7730194
- 00c010f8 ["INT_ADD", "register:40f0:8", ["const:c010f8:8", "const:4:8"]]
- 00c010f8 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01520 ["INT_ADD", "register:40f0:8", ["const:c01520:8", "const:4:8"]]
+ 00c01520 ["CALL", null, ["callee:00c58270:8"]]
- 00c010f8 bytes 5e5b0194
+ 00c01520 bytes 545b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4212b239d74c0dd218854b8135e8523"></a>

### [`00c011e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md) → [`00c01610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01610.md) FUN_00c01610

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c011e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c01608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01608.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01664",
      "incomplete_value": true,
      "site": "00c01668",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0123c",
      "incomplete_value": true,
      "site": "00c01240",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c01664",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c01664",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c01664",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c01664",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c01240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01240) · [`00c01214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01214) · [`00c01230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01230)
- 新版 `00c01668`（命令位置の公開資料なし） · `00c0163c`（命令位置の公開資料なし） · `00c01658`（命令位置の公開資料なし）

~~~diff
- 00c01240 ["INT_ADD", "register:40f0:8", ["const:c01240:8", "const:4:8"]]
- 00c01240 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01668 ["INT_ADD", "register:40f0:8", ["const:c01668:8", "const:4:8"]]
+ 00c01668 ["CALL", null, ["callee:00c58280:8"]]
- 00c01240 bytes 105b0194
+ 00c01668 bytes 065b0194
- 00c01214 ["INT_ADD", "register:40f0:8", ["const:c01214:8", "const:4:8"]]
- 00c01214 ["CALL", null, ["callee:00c5e420:8"]]
+ 00c0163c ["INT_ADD", "register:40f0:8", ["const:c0163c:8", "const:4:8"]]
+ 00c0163c ["CALL", null, ["callee:00c5e420:8"]]
- 00c01214 bytes 83730194
+ 00c0163c bytes 79730194
- 00c01230 ["INT_ADD", "register:40f0:8", ["const:c01230:8", "const:4:8"]]
- 00c01230 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01658 ["INT_ADD", "register:40f0:8", ["const:c01658:8", "const:4:8"]]
+ 00c01658 ["CALL", null, ["callee:00c58270:8"]]
- 00c01230 bytes 105b0194
+ 00c01658 bytes 065b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b3bdf3940eae991518ee785652992d"></a>

### [`00c01320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md) → [`00c01748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01748.md) FUN_00c01748

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c01318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01318.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)
- 新版 呼出元 1件 [`00c01740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01740.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0179c",
      "incomplete_value": true,
      "site": "00c017a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c01374",
      "incomplete_value": true,
      "site": "00c01378",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
      "00c0179c",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c0179c",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0179c",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c0179c",
      "PARAM",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c01378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md#insn-00c01378) · [`00c0134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md#insn-00c0134c) · [`00c01368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md#insn-00c01368)
- 新版 `00c017a0`（命令位置の公開資料なし） · `00c01774`（命令位置の公開資料なし） · `00c01790`（命令位置の公開資料なし）

~~~diff
- 00c01378 ["INT_ADD", "register:40f0:8", ["const:c01378:8", "const:4:8"]]
- 00c01378 ["CALL", null, ["callee:00c58280:8"]]
+ 00c017a0 ["INT_ADD", "register:40f0:8", ["const:c017a0:8", "const:4:8"]]
+ 00c017a0 ["CALL", null, ["callee:00c58280:8"]]
- 00c01378 bytes c25a0194
+ 00c017a0 bytes b85a0194
- 00c0134c ["INT_ADD", "register:40f0:8", ["const:c0134c:8", "const:4:8"]]
- 00c0134c ["CALL", null, ["callee:00c5e420:8"]]
+ 00c01774 ["INT_ADD", "register:40f0:8", ["const:c01774:8", "const:4:8"]]
+ 00c01774 ["CALL", null, ["callee:00c5e420:8"]]
- 00c0134c bytes 35730194
+ 00c01774 bytes 2b730194
- 00c01368 ["INT_ADD", "register:40f0:8", ["const:c01368:8", "const:4:8"]]
- 00c01368 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01790 ["INT_ADD", "register:40f0:8", ["const:c01790:8", "const:4:8"]]
+ 00c01790 ["CALL", null, ["callee:00c58270:8"]]
- 00c01368 bytes c25a0194
+ 00c01790 bytes b85a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fc8f72421fc9a4f964ba621b0583a0"></a>

### [`00c015a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md) → [`00c019cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c019cc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01a0c",
      "incomplete_value": true,
      "site": "00c01a10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c015e4",
      "incomplete_value": true,
      "site": "00c015e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
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
      "00c01a0c",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c01a0c",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c01a0c",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c01a0c",
      "PARAM",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c015e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c015e8) · [`00c015d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c015d8) · [`00c015e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c015e4)
- 新版 `00c01a10`（命令位置の公開資料なし） · `00c01a00`（命令位置の公開資料なし） · `00c01a0c`（命令位置の公開資料なし）

~~~diff
- 00c015e8 ["INT_ADD", "register:40f0:8", ["const:c015e8:8", "const:4:8"]]
- 00c015e8 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01a10 ["INT_ADD", "register:40f0:8", ["const:c01a10:8", "const:4:8"]]
+ 00c01a10 ["CALL", null, ["callee:00c58280:8"]]
- 00c015e8 bytes 265a0194
+ 00c01a10 bytes 1c5a0194
- 00c015d8 ["INT_ADD", "register:40f0:8", ["const:c015d8:8", "const:4:8"]]
- 00c015d8 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01a00 ["INT_ADD", "register:40f0:8", ["const:c01a00:8", "const:4:8"]]
+ 00c01a00 ["CALL", null, ["callee:00c58270:8"]]
- 00c015d8 bytes 265a0194
+ 00c01a00 bytes 1c5a0194
- 00c015e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:740:8"]]
- 00c015e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c01a0c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b40:8"]]
+ 00c01a0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c015e4 bytes 21a043f9
+ 00c01a0c bytes 21a045f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375c275048658711c68f204bd5f3860a"></a>

### [`00c01818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md) → [`00c01c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01c40.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01c78",
      "incomplete_value": true,
      "site": "00c01c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c01850",
      "incomplete_value": true,
      "site": "00c01854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
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
      "00c01c78",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c01c78",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c01c78",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c01c78",
      "PARAM",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c01854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01854) · [`00c01844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01844) · [`00c01850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01850)
- 新版 `00c01c7c`（命令位置の公開資料なし） · `00c01c6c`（命令位置の公開資料なし） · `00c01c78`（命令位置の公開資料なし）

~~~diff
- 00c01854 ["INT_ADD", "register:40f0:8", ["const:c01854:8", "const:4:8"]]
- 00c01854 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01c7c ["INT_ADD", "register:40f0:8", ["const:c01c7c:8", "const:4:8"]]
+ 00c01c7c ["CALL", null, ["callee:00c58280:8"]]
- 00c01854 bytes 8b590194
+ 00c01c7c bytes 81590194
- 00c01844 ["INT_ADD", "register:40f0:8", ["const:c01844:8", "const:4:8"]]
- 00c01844 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01c6c ["INT_ADD", "register:40f0:8", ["const:c01c6c:8", "const:4:8"]]
+ 00c01c6c ["CALL", null, ["callee:00c58270:8"]]
- 00c01844 bytes 8b590194
+ 00c01c6c bytes 81590194
- 00c01850 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:740:8"]]
- 00c01850 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c01c78 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b40:8"]]
+ 00c01c78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c01850 bytes 21a043f9
+ 00c01c78 bytes 21a045f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d4dc7c2a1e2f7528ceace9c259e4cb"></a>

### [`00c01a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md) → [`00c01e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01e38.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e460.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01e78",
      "incomplete_value": true,
      "site": "00c01e7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c01a50",
      "incomplete_value": true,
      "site": "00c01a54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
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
      "00c01e78",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c01e78",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c01e78",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c01e78",
      "PARAM",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c01a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a54) · [`00c01a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a44) · [`00c01a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a50)
- 新版 `00c01e7c`（命令位置の公開資料なし） · `00c01e6c`（命令位置の公開資料なし） · `00c01e78`（命令位置の公開資料なし）

~~~diff
- 00c01a54 ["INT_ADD", "register:40f0:8", ["const:c01a54:8", "const:4:8"]]
- 00c01a54 ["CALL", null, ["callee:00c58280:8"]]
+ 00c01e7c ["INT_ADD", "register:40f0:8", ["const:c01e7c:8", "const:4:8"]]
+ 00c01e7c ["CALL", null, ["callee:00c58280:8"]]
- 00c01a54 bytes 0b590194
+ 00c01e7c bytes 01590194
- 00c01a44 ["INT_ADD", "register:40f0:8", ["const:c01a44:8", "const:4:8"]]
- 00c01a44 ["CALL", null, ["callee:00c58270:8"]]
+ 00c01e6c ["INT_ADD", "register:40f0:8", ["const:c01e6c:8", "const:4:8"]]
+ 00c01e6c ["CALL", null, ["callee:00c58270:8"]]
- 00c01a44 bytes 0b590194
+ 00c01e6c bytes 01590194
- 00c01a50 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:740:8"]]
- 00c01a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c01e78 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b40:8"]]
+ 00c01e78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c01a50 bytes 21a043f9
+ 00c01e78 bytes 21a045f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2c0faae476f19f2420d2084c3098c7"></a>

### [`00c028c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md) → [`00c02cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02cf0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c02d1c",
      "incomplete_value": true,
      "site": "00c02d1c",
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
      "definition_site": "00c028f4",
      "incomplete_value": true,
      "site": "00c028f4",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c02d18",
      "incomplete_value": true,
      "site": "00c02d20",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c028f0",
      "incomplete_value": true,
      "site": "00c028f8",
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
            "const:18:8"
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
      "00c02d0c",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ],
    [
      "00c02d1c",
      "DATA",
      [
        "storage",
        "00c92c88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00c02d20",
      "DATA",
      [
        "storage",
        "00c92c60",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c02d0c",
      "READ",
      [
        "storage",
        "00c9bb50",
        null,
        "pointer"
      ]
    ],
    [
      "00c02d1c",
      "DATA",
      [
        "storage",
        "00c93088",
        null,
        "pointer"
      ]
    ],
    [
      "00c02d20",
      "DATA",
      [
        "storage",
        "00c93060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c028e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md#insn-00c028e4) · [`00c02900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md#insn-00c02900)
- 新版 `00c02d0c`（命令位置の公開資料なし） · `00c02d28`（命令位置の公開資料なし）

~~~diff
- 00c028e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:750:8"]]
- 00c028e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c02d0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b50:8"]]
+ 00c02d0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c028e4 bytes 08a943f9
+ 00c02d0c bytes 08a945f9
- 00c02900 ["INT_ADD", "register:40f0:8", ["const:c02900:8", "const:4:8"]]
- 00c02900 ["CALL", null, ["callee:00c581e0:8"]]
+ 00c02d28 ["INT_ADD", "register:40f0:8", ["const:c02d28:8", "const:4:8"]]
+ 00c02d28 ["CALL", null, ["callee:00c581e0:8"]]
- 00c02900 bytes 38550194
+ 00c02d28 bytes 2e550194
~~~


<a id="compare-b27734898e61f25e7baab036d5d37cad"></a>

### [`00c02bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md) → [`00c02fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02fdc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03030",
      "incomplete_value": true,
      "site": "00c03034",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02c08",
      "incomplete_value": true,
      "site": "00c02c0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03078",
      "incomplete_value": true,
      "site": "00c0307c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02c50",
      "incomplete_value": true,
      "site": "00c02c54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03030",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03030",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03078",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03030",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03030",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03078",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c02c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02c0c) · [`00c02c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02c54) · [`00c02be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02be0)
- 新版 `00c03034`（命令位置の公開資料なし） · `00c0307c`（命令位置の公開資料なし） · `00c03008`（命令位置の公開資料なし）

~~~diff
- 00c02c0c ["INT_ADD", "register:40f0:8", ["const:c02c0c:8", "const:4:8"]]
- 00c02c0c ["CALL", null, ["callee:00c58280:8"]]
+ 00c03034 ["INT_ADD", "register:40f0:8", ["const:c03034:8", "const:4:8"]]
+ 00c03034 ["CALL", null, ["callee:00c58280:8"]]
- 00c02c0c bytes 9d540194
+ 00c03034 bytes 93540194
- 00c02c54 ["INT_ADD", "register:40f0:8", ["const:c02c54:8", "const:4:8"]]
- 00c02c54 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0307c ["INT_ADD", "register:40f0:8", ["const:c0307c:8", "const:4:8"]]
+ 00c0307c ["CALL", null, ["callee:00c58280:8"]]
- 00c02c54 bytes 8b540194
+ 00c0307c bytes 81540194
- 00c02be0 ["INT_ADD", "register:40f0:8", ["const:c02be0:8", "const:4:8"]]
- 00c02be0 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03008 ["INT_ADD", "register:40f0:8", ["const:c03008:8", "const:4:8"]]
+ 00c03008 ["CALL", null, ["callee:00c5e400:8"]]
- 00c02be0 bytes 086d0194
+ 00c03008 bytes fe6c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4b5125deb6786d8da0ee099ae5301e"></a>

### [`00c02d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md) → [`00c0316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c0316c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEs

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c031c8",
      "incomplete_value": true,
      "site": "00c031cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02da0",
      "incomplete_value": true,
      "site": "00c02da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03210",
      "incomplete_value": true,
      "site": "00c03214",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02de8",
      "incomplete_value": true,
      "site": "00c02dec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c031c8",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c031c8",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03210",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c031c8",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c031c8",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03210",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c02da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02da4) · [`00c02dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02dec) · [`00c02d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02d74)
- 新版 `00c031cc`（命令位置の公開資料なし） · `00c03214`（命令位置の公開資料なし） · `00c0319c`（命令位置の公開資料なし）

~~~diff
- 00c02da4 ["INT_ADD", "register:40f0:8", ["const:c02da4:8", "const:4:8"]]
- 00c02da4 ["CALL", null, ["callee:00c58280:8"]]
+ 00c031cc ["INT_ADD", "register:40f0:8", ["const:c031cc:8", "const:4:8"]]
+ 00c031cc ["CALL", null, ["callee:00c58280:8"]]
- 00c02da4 bytes 37540194
+ 00c031cc bytes 2d540194
- 00c02dec ["INT_ADD", "register:40f0:8", ["const:c02dec:8", "const:4:8"]]
- 00c02dec ["CALL", null, ["callee:00c58280:8"]]
+ 00c03214 ["INT_ADD", "register:40f0:8", ["const:c03214:8", "const:4:8"]]
+ 00c03214 ["CALL", null, ["callee:00c58280:8"]]
- 00c02dec bytes 25540194
+ 00c03214 bytes 1b540194
- 00c02d74 ["INT_ADD", "register:40f0:8", ["const:c02d74:8", "const:4:8"]]
- 00c02d74 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c0319c ["INT_ADD", "register:40f0:8", ["const:c0319c:8", "const:4:8"]]
+ 00c0319c ["CALL", null, ["callee:00c5e400:8"]]
- 00c02d74 bytes a36c0194
+ 00c0319c bytes 996c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-450f2e910f228f0dccdbcbd2823d1e88"></a>

### [`00c02efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md) → [`00c03324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c03324.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEt

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03378",
      "incomplete_value": true,
      "site": "00c0337c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02f50",
      "incomplete_value": true,
      "site": "00c02f54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c033c0",
      "incomplete_value": true,
      "site": "00c033c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c02f98",
      "incomplete_value": true,
      "site": "00c02f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03378",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03378",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c033c0",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03378",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03378",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c033c0",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c02f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f54) · [`00c02f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f9c) · [`00c02f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f28)
- 新版 `00c0337c`（命令位置の公開資料なし） · `00c033c4`（命令位置の公開資料なし） · `00c03350`（命令位置の公開資料なし）

~~~diff
- 00c02f54 ["INT_ADD", "register:40f0:8", ["const:c02f54:8", "const:4:8"]]
- 00c02f54 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0337c ["INT_ADD", "register:40f0:8", ["const:c0337c:8", "const:4:8"]]
+ 00c0337c ["CALL", null, ["callee:00c58280:8"]]
- 00c02f54 bytes cb530194
+ 00c0337c bytes c1530194
- 00c02f9c ["INT_ADD", "register:40f0:8", ["const:c02f9c:8", "const:4:8"]]
- 00c02f9c ["CALL", null, ["callee:00c58280:8"]]
+ 00c033c4 ["INT_ADD", "register:40f0:8", ["const:c033c4:8", "const:4:8"]]
+ 00c033c4 ["CALL", null, ["callee:00c58280:8"]]
- 00c02f9c bytes b9530194
+ 00c033c4 bytes af530194
- 00c02f28 ["INT_ADD", "register:40f0:8", ["const:c02f28:8", "const:4:8"]]
- 00c02f28 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03350 ["INT_ADD", "register:40f0:8", ["const:c03350:8", "const:4:8"]]
+ 00c03350 ["CALL", null, ["callee:00c5e400:8"]]
- 00c02f28 bytes 366c0194
+ 00c03350 bytes 2c6c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401bb7c1ae26783a55eb2ec43239a386"></a>

### [`00c0308c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md) → [`00c034b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c034b4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03510",
      "incomplete_value": true,
      "site": "00c03514",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c030e8",
      "incomplete_value": true,
      "site": "00c030ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03558",
      "incomplete_value": true,
      "site": "00c0355c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03130",
      "incomplete_value": true,
      "site": "00c03134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03510",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03510",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03558",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03510",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03510",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03558",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c030ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md#insn-00c030ec) · [`00c03134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md#insn-00c03134) · [`00c030bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md#insn-00c030bc)
- 新版 `00c03514`（命令位置の公開資料なし） · `00c0355c`（命令位置の公開資料なし） · `00c034e4`（命令位置の公開資料なし）

~~~diff
- 00c030ec ["INT_ADD", "register:40f0:8", ["const:c030ec:8", "const:4:8"]]
- 00c030ec ["CALL", null, ["callee:00c58280:8"]]
+ 00c03514 ["INT_ADD", "register:40f0:8", ["const:c03514:8", "const:4:8"]]
+ 00c03514 ["CALL", null, ["callee:00c58280:8"]]
- 00c030ec bytes 65530194
+ 00c03514 bytes 5b530194
- 00c03134 ["INT_ADD", "register:40f0:8", ["const:c03134:8", "const:4:8"]]
- 00c03134 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0355c ["INT_ADD", "register:40f0:8", ["const:c0355c:8", "const:4:8"]]
+ 00c0355c ["CALL", null, ["callee:00c58280:8"]]
- 00c03134 bytes 53530194
+ 00c0355c bytes 49530194
- 00c030bc ["INT_ADD", "register:40f0:8", ["const:c030bc:8", "const:4:8"]]
- 00c030bc ["CALL", null, ["callee:00c5e400:8"]]
+ 00c034e4 ["INT_ADD", "register:40f0:8", ["const:c034e4:8", "const:4:8"]]
+ 00c034e4 ["CALL", null, ["callee:00c5e400:8"]]
- 00c030bc bytes d16b0194
+ 00c034e4 bytes c76b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bebdb8d439910e8aee6bb0eca522fdaa"></a>

### [`00c03244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md) → [`00c0366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c0366c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c036c0",
      "incomplete_value": true,
      "site": "00c036c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03298",
      "incomplete_value": true,
      "site": "00c0329c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03708",
      "incomplete_value": true,
      "site": "00c0370c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c032e0",
      "incomplete_value": true,
      "site": "00c032e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c036c0",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c036c0",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03708",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c036c0",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c036c0",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03708",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md#insn-00c0329c) · [`00c032e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md#insn-00c032e4) · [`00c03270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md#insn-00c03270)
- 新版 `00c036c4`（命令位置の公開資料なし） · `00c0370c`（命令位置の公開資料なし） · `00c03698`（命令位置の公開資料なし）

~~~diff
- 00c0329c ["INT_ADD", "register:40f0:8", ["const:c0329c:8", "const:4:8"]]
- 00c0329c ["CALL", null, ["callee:00c58280:8"]]
+ 00c036c4 ["INT_ADD", "register:40f0:8", ["const:c036c4:8", "const:4:8"]]
+ 00c036c4 ["CALL", null, ["callee:00c58280:8"]]
- 00c0329c bytes f9520194
+ 00c036c4 bytes ef520194
- 00c032e4 ["INT_ADD", "register:40f0:8", ["const:c032e4:8", "const:4:8"]]
- 00c032e4 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0370c ["INT_ADD", "register:40f0:8", ["const:c0370c:8", "const:4:8"]]
+ 00c0370c ["CALL", null, ["callee:00c58280:8"]]
- 00c032e4 bytes e7520194
+ 00c0370c bytes dd520194
- 00c03270 ["INT_ADD", "register:40f0:8", ["const:c03270:8", "const:4:8"]]
- 00c03270 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03698 ["INT_ADD", "register:40f0:8", ["const:c03698:8", "const:4:8"]]
+ 00c03698 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03270 bytes 646b0194
+ 00c03698 bytes 5a6b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c76d6c838edd82d54fafddc4f542ef1"></a>

### [`00c033d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md) → [`00c037fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c037fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03850",
      "incomplete_value": true,
      "site": "00c03854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03428",
      "incomplete_value": true,
      "site": "00c0342c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03898",
      "incomplete_value": true,
      "site": "00c0389c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03470",
      "incomplete_value": true,
      "site": "00c03474",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03850",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03850",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03898",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03850",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03850",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03898",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0342c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md#insn-00c0342c) · [`00c03474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md#insn-00c03474) · [`00c03400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md#insn-00c03400)
- 新版 `00c03854`（命令位置の公開資料なし） · `00c0389c`（命令位置の公開資料なし） · `00c03828`（命令位置の公開資料なし）

~~~diff
- 00c0342c ["INT_ADD", "register:40f0:8", ["const:c0342c:8", "const:4:8"]]
- 00c0342c ["CALL", null, ["callee:00c58280:8"]]
+ 00c03854 ["INT_ADD", "register:40f0:8", ["const:c03854:8", "const:4:8"]]
+ 00c03854 ["CALL", null, ["callee:00c58280:8"]]
- 00c0342c bytes 95520194
+ 00c03854 bytes 8b520194
- 00c03474 ["INT_ADD", "register:40f0:8", ["const:c03474:8", "const:4:8"]]
- 00c03474 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0389c ["INT_ADD", "register:40f0:8", ["const:c0389c:8", "const:4:8"]]
+ 00c0389c ["CALL", null, ["callee:00c58280:8"]]
- 00c03474 bytes 83520194
+ 00c0389c bytes 79520194
- 00c03400 ["INT_ADD", "register:40f0:8", ["const:c03400:8", "const:4:8"]]
- 00c03400 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03828 ["INT_ADD", "register:40f0:8", ["const:c03828:8", "const:4:8"]]
+ 00c03828 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03400 bytes 006b0194
+ 00c03828 bytes f66a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bb06392959dcc483b7bd0f53a8ba5b6"></a>

### [`00c03564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md) → [`00c0398c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c0398c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c039e0",
      "incomplete_value": true,
      "site": "00c039e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c035b8",
      "incomplete_value": true,
      "site": "00c035bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03a28",
      "incomplete_value": true,
      "site": "00c03a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03600",
      "incomplete_value": true,
      "site": "00c03604",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c039e0",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c039e0",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03a28",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c039e0",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c039e0",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03a28",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c035bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md#insn-00c035bc) · [`00c03604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md#insn-00c03604) · [`00c03590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md#insn-00c03590)
- 新版 `00c039e4`（命令位置の公開資料なし） · `00c03a2c`（命令位置の公開資料なし） · `00c039b8`（命令位置の公開資料なし）

~~~diff
- 00c035bc ["INT_ADD", "register:40f0:8", ["const:c035bc:8", "const:4:8"]]
- 00c035bc ["CALL", null, ["callee:00c58280:8"]]
+ 00c039e4 ["INT_ADD", "register:40f0:8", ["const:c039e4:8", "const:4:8"]]
+ 00c039e4 ["CALL", null, ["callee:00c58280:8"]]
- 00c035bc bytes 31520194
+ 00c039e4 bytes 27520194
- 00c03604 ["INT_ADD", "register:40f0:8", ["const:c03604:8", "const:4:8"]]
- 00c03604 ["CALL", null, ["callee:00c58280:8"]]
+ 00c03a2c ["INT_ADD", "register:40f0:8", ["const:c03a2c:8", "const:4:8"]]
+ 00c03a2c ["CALL", null, ["callee:00c58280:8"]]
- 00c03604 bytes 1f520194
+ 00c03a2c bytes 15520194
- 00c03590 ["INT_ADD", "register:40f0:8", ["const:c03590:8", "const:4:8"]]
- 00c03590 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c039b8 ["INT_ADD", "register:40f0:8", ["const:c039b8:8", "const:4:8"]]
+ 00c039b8 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03590 bytes 9c6a0194
+ 00c039b8 bytes 926a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76df5515cab5a17504f18ec32d916e64"></a>

### [`00c036f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md) → [`00c03b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c03b1c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEx

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03b70",
      "incomplete_value": true,
      "site": "00c03b74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03748",
      "incomplete_value": true,
      "site": "00c0374c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03bb8",
      "incomplete_value": true,
      "site": "00c03bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03790",
      "incomplete_value": true,
      "site": "00c03794",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03b70",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03b70",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03bb8",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03b70",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03b70",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03bb8",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0374c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c0374c) · [`00c03794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c03794) · [`00c03720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c03720)
- 新版 `00c03b74`（命令位置の公開資料なし） · `00c03bbc`（命令位置の公開資料なし） · `00c03b48`（命令位置の公開資料なし）

~~~diff
- 00c0374c ["INT_ADD", "register:40f0:8", ["const:c0374c:8", "const:4:8"]]
- 00c0374c ["CALL", null, ["callee:00c58280:8"]]
+ 00c03b74 ["INT_ADD", "register:40f0:8", ["const:c03b74:8", "const:4:8"]]
+ 00c03b74 ["CALL", null, ["callee:00c58280:8"]]
- 00c0374c bytes cd510194
+ 00c03b74 bytes c3510194
- 00c03794 ["INT_ADD", "register:40f0:8", ["const:c03794:8", "const:4:8"]]
- 00c03794 ["CALL", null, ["callee:00c58280:8"]]
+ 00c03bbc ["INT_ADD", "register:40f0:8", ["const:c03bbc:8", "const:4:8"]]
+ 00c03bbc ["CALL", null, ["callee:00c58280:8"]]
- 00c03794 bytes bb510194
+ 00c03bbc bytes b1510194
- 00c03720 ["INT_ADD", "register:40f0:8", ["const:c03720:8", "const:4:8"]]
- 00c03720 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03b48 ["INT_ADD", "register:40f0:8", ["const:c03b48:8", "const:4:8"]]
+ 00c03b48 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03720 bytes 386a0194
+ 00c03b48 bytes 2e6a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62bf1d058a90df7a03b5a1506ba3b002"></a>

### [`00c03884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md) → [`00c03cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c03cac.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEy

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03d00",
      "incomplete_value": true,
      "site": "00c03d04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c038d8",
      "incomplete_value": true,
      "site": "00c038dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03d48",
      "incomplete_value": true,
      "site": "00c03d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03920",
      "incomplete_value": true,
      "site": "00c03924",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03d00",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03d00",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03d48",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03d00",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03d00",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03d48",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c038dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c038dc) · [`00c03924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c03924) · [`00c038b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c038b0)
- 新版 `00c03d04`（命令位置の公開資料なし） · `00c03d4c`（命令位置の公開資料なし） · `00c03cd8`（命令位置の公開資料なし）

~~~diff
- 00c038dc ["INT_ADD", "register:40f0:8", ["const:c038dc:8", "const:4:8"]]
- 00c038dc ["CALL", null, ["callee:00c58280:8"]]
+ 00c03d04 ["INT_ADD", "register:40f0:8", ["const:c03d04:8", "const:4:8"]]
+ 00c03d04 ["CALL", null, ["callee:00c58280:8"]]
- 00c038dc bytes 69510194
+ 00c03d04 bytes 5f510194
- 00c03924 ["INT_ADD", "register:40f0:8", ["const:c03924:8", "const:4:8"]]
- 00c03924 ["CALL", null, ["callee:00c58280:8"]]
+ 00c03d4c ["INT_ADD", "register:40f0:8", ["const:c03d4c:8", "const:4:8"]]
+ 00c03d4c ["CALL", null, ["callee:00c58280:8"]]
- 00c03924 bytes 57510194
+ 00c03d4c bytes 4d510194
- 00c038b0 ["INT_ADD", "register:40f0:8", ["const:c038b0:8", "const:4:8"]]
- 00c038b0 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03cd8 ["INT_ADD", "register:40f0:8", ["const:c03cd8:8", "const:4:8"]]
+ 00c03cd8 ["CALL", null, ["callee:00c5e400:8"]]
- 00c038b0 bytes d4690194
+ 00c03cd8 bytes ca690194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b3b42a054eafd1bbcc0e342690b6971"></a>

### [`00c03a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md) → [`00c03e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c03e3c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEf

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03e94",
      "incomplete_value": true,
      "site": "00c03e98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03a6c",
      "incomplete_value": true,
      "site": "00c03a70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c03edc",
      "incomplete_value": true,
      "site": "00c03ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03ab4",
      "incomplete_value": true,
      "site": "00c03ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c03e94",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03e94",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03edc",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c03e94",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c03e94",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03edc",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c03a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03a70) · [`00c03ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03ab8) · [`00c03a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03a44)
- 新版 `00c03e98`（命令位置の公開資料なし） · `00c03ee0`（命令位置の公開資料なし） · `00c03e6c`（命令位置の公開資料なし）

~~~diff
- 00c03a70 ["INT_ADD", "register:40f0:8", ["const:c03a70:8", "const:4:8"]]
- 00c03a70 ["CALL", null, ["callee:00c58280:8"]]
+ 00c03e98 ["INT_ADD", "register:40f0:8", ["const:c03e98:8", "const:4:8"]]
+ 00c03e98 ["CALL", null, ["callee:00c58280:8"]]
- 00c03a70 bytes 04510194
+ 00c03e98 bytes fa500194
- 00c03ab8 ["INT_ADD", "register:40f0:8", ["const:c03ab8:8", "const:4:8"]]
- 00c03ab8 ["CALL", null, ["callee:00c58280:8"]]
+ 00c03ee0 ["INT_ADD", "register:40f0:8", ["const:c03ee0:8", "const:4:8"]]
+ 00c03ee0 ["CALL", null, ["callee:00c58280:8"]]
- 00c03ab8 bytes f2500194
+ 00c03ee0 bytes e8500194
- 00c03a44 ["INT_ADD", "register:40f0:8", ["const:c03a44:8", "const:4:8"]]
- 00c03a44 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c03e6c ["INT_ADD", "register:40f0:8", ["const:c03e6c:8", "const:4:8"]]
+ 00c03e6c ["CALL", null, ["callee:00c5e400:8"]]
- 00c03a44 bytes 6f690194
+ 00c03e6c bytes 65690194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d6b3c40db3838d68cf103b3a4fd69a"></a>

### [`00c03bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md) → [`00c03fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c03/00c03fd4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEd

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0402c",
      "incomplete_value": true,
      "site": "00c04030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03c04",
      "incomplete_value": true,
      "site": "00c03c08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c04074",
      "incomplete_value": true,
      "site": "00c04078",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03c4c",
      "incomplete_value": true,
      "site": "00c03c50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c0402c",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c0402c",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04074",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c0402c",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c0402c",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04074",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c03c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03c08) · [`00c03c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03c50) · [`00c03bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03bdc)
- 新版 `00c04030`（命令位置の公開資料なし） · `00c04078`（命令位置の公開資料なし） · `00c04004`（命令位置の公開資料なし）

~~~diff
- 00c03c08 ["INT_ADD", "register:40f0:8", ["const:c03c08:8", "const:4:8"]]
- 00c03c08 ["CALL", null, ["callee:00c58280:8"]]
+ 00c04030 ["INT_ADD", "register:40f0:8", ["const:c04030:8", "const:4:8"]]
+ 00c04030 ["CALL", null, ["callee:00c58280:8"]]
- 00c03c08 bytes 9e500194
+ 00c04030 bytes 94500194
- 00c03c50 ["INT_ADD", "register:40f0:8", ["const:c03c50:8", "const:4:8"]]
- 00c03c50 ["CALL", null, ["callee:00c58280:8"]]
+ 00c04078 ["INT_ADD", "register:40f0:8", ["const:c04078:8", "const:4:8"]]
+ 00c04078 ["CALL", null, ["callee:00c58280:8"]]
- 00c03c50 bytes 8c500194
+ 00c04078 bytes 82500194
- 00c03bdc ["INT_ADD", "register:40f0:8", ["const:c03bdc:8", "const:4:8"]]
- 00c03bdc ["CALL", null, ["callee:00c5e400:8"]]
+ 00c04004 ["INT_ADD", "register:40f0:8", ["const:c04004:8", "const:4:8"]]
+ 00c04004 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03bdc bytes 09690194
+ 00c04004 bytes ff680194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ee925cd5f90b59d419b017846ed920"></a>

### [`00c03d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md) → [`00c0416c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c0416c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c041c0",
      "incomplete_value": true,
      "site": "00c041c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03d98",
      "incomplete_value": true,
      "site": "00c03d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c04208",
      "incomplete_value": true,
      "site": "00c0420c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03de0",
      "incomplete_value": true,
      "site": "00c03de4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c041c0",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c041c0",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04208",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c041c0",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c041c0",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04208",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c03d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03d9c) · [`00c03de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03de4) · [`00c03d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03d70)
- 新版 `00c041c4`（命令位置の公開資料なし） · `00c0420c`（命令位置の公開資料なし） · `00c04198`（命令位置の公開資料なし）

~~~diff
- 00c03d9c ["INT_ADD", "register:40f0:8", ["const:c03d9c:8", "const:4:8"]]
- 00c03d9c ["CALL", null, ["callee:00c58280:8"]]
+ 00c041c4 ["INT_ADD", "register:40f0:8", ["const:c041c4:8", "const:4:8"]]
+ 00c041c4 ["CALL", null, ["callee:00c58280:8"]]
- 00c03d9c bytes 39500194
+ 00c041c4 bytes 2f500194
- 00c03de4 ["INT_ADD", "register:40f0:8", ["const:c03de4:8", "const:4:8"]]
- 00c03de4 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0420c ["INT_ADD", "register:40f0:8", ["const:c0420c:8", "const:4:8"]]
+ 00c0420c ["CALL", null, ["callee:00c58280:8"]]
- 00c03de4 bytes 27500194
+ 00c0420c bytes 1d500194
- 00c03d70 ["INT_ADD", "register:40f0:8", ["const:c03d70:8", "const:4:8"]]
- 00c03d70 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c04198 ["INT_ADD", "register:40f0:8", ["const:c04198:8", "const:4:8"]]
+ 00c04198 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03d70 bytes a4680194
+ 00c04198 bytes 9a680194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cd36b39716e683dad0b40efc49fc192"></a>

### [`00c03ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md) → [`00c042fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c042fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPKv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c04350",
      "incomplete_value": true,
      "site": "00c04354",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03f28",
      "incomplete_value": true,
      "site": "00c03f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
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
      "definition_site": "00c04398",
      "incomplete_value": true,
      "site": "00c0439c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c03f70",
      "incomplete_value": true,
      "site": "00c03f74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "00c04350",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c04350",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04398",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c04350",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c04350",
      "PARAM",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c04398",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c03f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f2c) · [`00c03f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f74) · [`00c03f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f00)
- 新版 `00c04354`（命令位置の公開資料なし） · `00c0439c`（命令位置の公開資料なし） · `00c04328`（命令位置の公開資料なし）

~~~diff
- 00c03f2c ["INT_ADD", "register:40f0:8", ["const:c03f2c:8", "const:4:8"]]
- 00c03f2c ["CALL", null, ["callee:00c58280:8"]]
+ 00c04354 ["INT_ADD", "register:40f0:8", ["const:c04354:8", "const:4:8"]]
+ 00c04354 ["CALL", null, ["callee:00c58280:8"]]
- 00c03f2c bytes d54f0194
+ 00c04354 bytes cb4f0194
- 00c03f74 ["INT_ADD", "register:40f0:8", ["const:c03f74:8", "const:4:8"]]
- 00c03f74 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0439c ["INT_ADD", "register:40f0:8", ["const:c0439c:8", "const:4:8"]]
+ 00c0439c ["CALL", null, ["callee:00c58280:8"]]
- 00c03f74 bytes c34f0194
+ 00c0439c bytes b94f0194
- 00c03f00 ["INT_ADD", "register:40f0:8", ["const:c03f00:8", "const:4:8"]]
- 00c03f00 ["CALL", null, ["callee:00c5e400:8"]]
+ 00c04328 ["INT_ADD", "register:40f0:8", ["const:c04328:8", "const:4:8"]]
+ 00c04328 ["CALL", null, ["callee:00c5e400:8"]]
- 00c03f00 bytes 40680194
+ 00c04328 bytes 36680194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de1792bf6d0a52ae8bebcfdf6d88299"></a>

### [`00c04604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md) → [`00c04a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04a2c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC1EOS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c046b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c046b0.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c04ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ad8.md) [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c04a54",
      "incomplete_value": true,
      "site": "00c04a54",
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
      "definition_site": "00c0462c",
      "incomplete_value": true,
      "site": "00c0462c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c04a80",
      "incomplete_value": true,
      "site": "00c04a84",
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
      "definition_site": "00c04658",
      "incomplete_value": true,
      "site": "00c0465c",
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
      "00c04a4c",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c04a54",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c04a74",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c04a4c",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c04a54",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c04a74",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c04624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c04624) · [`00c04630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c04630) · [`00c0464c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c0464c)
- 新版 `00c04a4c`（命令位置の公開資料なし） · `00c04a58`（命令位置の公開資料なし） · `00c04a74`（命令位置の公開資料なし）

~~~diff
- 00c04624 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
- 00c04624 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c04a4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:848:8"]]
+ 00c04a4c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c04624 bytes b52642f9
+ 00c04a4c bytes b52644f9
- 00c04630 ["INT_ADD", "register:40f0:8", ["const:c04630:8", "const:4:8"]]
- 00c04630 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00c04a58 ["INT_ADD", "register:40f0:8", ["const:c04a58:8", "const:4:8"]]
+ 00c04a58 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00c04630 bytes 5c570194
+ 00c04a58 bytes 52570194
- 00c0464c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
- 00c0464c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c04a74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 00c04a74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c0464c bytes 08e143f9
+ 00c04a74 bytes 08e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6571b264b93e549e696db16543470041"></a>

### [`00c05264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md) → [`00c0568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0568c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) · 呼出先 6件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`00c58f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f00.md) · 呼出先 6件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.89% / 新版 86.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c056b0",
      "incomplete_value": true,
      "site": "00c056b0",
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
      "definition_site": "00c05288",
      "incomplete_value": true,
      "site": "00c05288",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c056d4",
      "incomplete_value": true,
      "site": "00c056d8",
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
      "definition_site": "00c052ac",
      "incomplete_value": true,
      "site": "00c052b0",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c056fc",
      "incomplete_value": true,
      "site": "00c05700",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c052d4",
      "incomplete_value": true,
      "site": "00c052d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
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
      "00c056a8",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c056b0",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c056c4",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c056a8",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c056b0",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c056c4",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c052d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c052d8) · [`00c05304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c05304) · [`00c05280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c05280)
- 新版 `00c05700`（命令位置の公開資料なし） · `00c0572c`（命令位置の公開資料なし） · `00c056a8`（命令位置の公開資料なし）

~~~diff
- 00c052d8 ["INT_ADD", "register:40f0:8", ["const:c052d8:8", "const:4:8"]]
- 00c052d8 ["CALL", null, ["callee:00c5d180:8"]]
+ 00c05700 ["INT_ADD", "register:40f0:8", ["const:c05700:8", "const:4:8"]]
+ 00c05700 ["CALL", null, ["callee:00c5d180:8"]]
- 00c052d8 bytes aa5e0194
+ 00c05700 bytes a05e0194
- 00c05304 ["INT_ADD", "register:40f0:8", ["const:c05304:8", "const:4:8"]]
- 00c05304 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0572c ["INT_ADD", "register:40f0:8", ["const:c0572c:8", "const:4:8"]]
+ 00c0572c ["CALL", null, ["callee:00c58280:8"]]
- 00c05304 bytes df4a0194
+ 00c0572c bytes d54a0194
- 00c05280 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
- 00c05280 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c056a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:848:8"]]
+ 00c056a8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05280 bytes b52642f9
+ 00c056a8 bytes b52644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b18ae3d936d2c897992fd28b94e9a5d"></a>

### [`00c05388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md) → [`00c057b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c057b0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1EOS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.06% / 新版 94.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c057d8",
      "incomplete_value": true,
      "site": "00c057d8",
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
      "definition_site": "00c053b0",
      "incomplete_value": true,
      "site": "00c053b0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0580c",
      "incomplete_value": true,
      "site": "00c05814",
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
      "definition_site": "00c053e4",
      "incomplete_value": true,
      "site": "00c053ec",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c057cc",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c057d8",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c05804",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c057cc",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c057d8",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c05804",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c053a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c053a4) · [`00c053b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c053b4) · [`00c053dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c053dc)
- 新版 `00c057cc`（命令位置の公開資料なし） · `00c057dc`（命令位置の公開資料なし） · `00c05804`（命令位置の公開資料なし）

~~~diff
- 00c053a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
- 00c053a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c057cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
+ 00c057cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c053a4 bytes 082542f9
+ 00c057cc bytes 082544f9
- 00c053b4 ["INT_ADD", "register:40f0:8", ["const:c053b4:8", "const:4:8"]]
- 00c053b4 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00c057dc ["INT_ADD", "register:40f0:8", ["const:c057dc:8", "const:4:8"]]
+ 00c057dc ["CALL", null, ["callee:00c5a7d0:8"]]
- 00c053b4 bytes 07540194
+ 00c057dc bytes fd530194
- 00c053dc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4f0:8"]]
- 00c053dc ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c05804 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8f0:8"]]
+ 00c05804 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00c053dc bytes 4a7942f9
+ 00c05804 bytes 4a7944f9
~~~


<a id="compare-f2f5cc9ac0103badaf262504affdacf8"></a>

### [`00c0551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md) → [`00c05944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05944.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b20.md) · 呼出先 5件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md)
- 新版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f20.md) · 呼出先 5件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

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
      "definition_site": "00c05968",
      "incomplete_value": true,
      "site": "00c0596c",
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
      "definition_site": "00c05540",
      "incomplete_value": true,
      "site": "00c05544",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c059d4",
      "incomplete_value": true,
      "site": "00c059d4",
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
      "definition_site": "00c055ac",
      "incomplete_value": true,
      "site": "00c055ac",
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
      "00c05960",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c0596c",
      "DATA",
      [
        "storage",
        "00c90b70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c0598c",
      "READ",
      [
        "storage",
        "00c90b88",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00c05960",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c0596c",
      "DATA",
      [
        "storage",
        "00c90f70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c0598c",
      "READ",
      [
        "storage",
        "00c90f88",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c05538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05538) · [`00c05550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05550) · [`00c05558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05558)
- 新版 `00c05960`（命令位置の公開資料なし） · `00c05978`（命令位置の公開資料なし） · `00c05980`（命令位置の公開資料なし）

~~~diff
- 00c05538 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
- 00c05538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c05960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
+ 00c05960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05538 bytes 087942f9
+ 00c05960 bytes 087944f9
- 00c05550 ["INT_ADD", "register:40f0:8", ["const:c05550:8", "const:4:8"]]
- 00c05550 ["CALL", null, ["callee:00c5d190:8"]]
+ 00c05978 ["INT_ADD", "register:40f0:8", ["const:c05978:8", "const:4:8"]]
+ 00c05978 ["CALL", null, ["callee:00c5d190:8"]]
- 00c05550 bytes 105e0194
+ 00c05978 bytes 065e0194
- 00c05558 ["INT_ADD", "register:40f0:8", ["const:c05558:8", "const:4:8"]]
- 00c05558 ["CALL", null, ["callee:00c5a000:8"]]
+ 00c05980 ["INT_ADD", "register:40f0:8", ["const:c05980:8", "const:4:8"]]
+ 00c05980 ["CALL", null, ["callee:00c5a000:8"]]
- 00c05558 bytes aa510194
+ 00c05980 bytes a0510194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a817f717fb71c8409bdae8a6fad952f7"></a>

### [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) → [`00c05dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) FUN_00c05dcc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00c04f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04f8c.md) [`00c0503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0503c.md) [`00c050f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md) [`00c051a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c051a8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c053b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md) [`00c05464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md) [`00c05520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md) [`00c055d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 74.03% / 新版 74.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e08",
      "incomplete_value": false,
      "site": "00c05e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:e8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c059e0",
      "incomplete_value": false,
      "site": "00c059e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:dbd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e18",
      "incomplete_value": false,
      "site": "00c05e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:93b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c059f0",
      "incomplete_value": false,
      "site": "00c059f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:86e:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e28",
      "incomplete_value": false,
      "site": "00c05e2c",
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
            "const:561:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05a00",
      "incomplete_value": false,
      "site": "00c05a04",
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
            "const:521:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c05dec",
      "DATA",
      [
        "storage",
        "002a746a",
        null,
        null
      ]
    ],
    [
      "00c05df4",
      "DATA",
      [
        "storage",
        "00310b10",
        "switchD_00c059d4::switchdataD_00310b10",
        "byte"
      ]
    ],
    [
      "00c05e08",
      "DATA",
      [
        "storage",
        "002a2dbd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c05dec",
      "DATA",
      [
        "storage",
        "002a7546",
        null,
        null
      ]
    ],
    [
      "00c05df4",
      "DATA",
      [
        "storage",
        "00310b50",
        "switchD_00c05dfc::switchdataD_00310b50",
        "byte"
      ]
    ],
    [
      "00c05e08",
      "DATA",
      [
        "storage",
        "002a2e8a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c059bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059bc) · [`00c059c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059c4) · [`00c059c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059c8)
- 新版 `00c05de4`（命令位置の公開資料なし） · `00c05dec`（命令位置の公開資料なし）

~~~diff
- 00c059bc ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00c059bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c059bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c059bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c05de4 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00c05de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c05de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c05de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c059bc bytes 29412c91
+ 00c05de4 bytes 29412d91
- 00c059c4 ["COPY", "tmp:0:8", ["const:46a:8"]]
- 00c059c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c059c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c059c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c05dec ["COPY", "tmp:0:8", ["const:546:8"]]
+ 00c05dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c05dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c05dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c059c4 bytes 00a81191
+ 00c05dec bytes 00181591
- 00c059c8 ["COPY", "register:4050:8", ["const:c059d8:8"]]
- 00c059c8 bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d3278f40e8995780a0bcbfd2669deab"></a>

### [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) → [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) FUN_00c05f58

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 71件 [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) [`00c0dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) · 呼出先 4件 [`00c37b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e080.md)
- 新版 呼出元 71件 [`00c0788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) [`00c0a534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) [`00c0ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) [`00c0d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) [`00c0e08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) · 呼出先 4件 [`00c37f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f6c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e480.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c05f84",
      "incomplete_value": true,
      "site": "00c05f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05b5c",
      "incomplete_value": true,
      "site": "00c05b64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:760:8"
              ]
            ]
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
      "definition_site": "00c05f88",
      "incomplete_value": true,
      "site": "00c05f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05b60",
      "incomplete_value": true,
      "site": "00c05b64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:768:8"
              ]
            ]
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
      "00c05f84",
      "READ",
      [
        "storage",
        "00c9b760",
        null,
        "pointer"
      ]
    ],
    [
      "00c05f84",
      "PARAM",
      [
        "storage",
        "00c96588",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c05f88",
      "READ",
      [
        "storage",
        "00c9b768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c05f84",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00c05f84",
      "PARAM",
      [
        "storage",
        "00c96988",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c05f88",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c05b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md#insn-00c05b64) · [`00c05b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md#insn-00c05b44) · [`00c05b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md#insn-00c05b4c)
- 新版 `00c05f8c`（命令位置の公開資料なし） · `00c05f6c`（命令位置の公開資料なし） · `00c05f74`（命令位置の公開資料なし）

~~~diff
- 00c05b64 ["INT_ADD", "register:40f0:8", ["const:c05b64:8", "const:4:8"]]
- 00c05b64 ["CALL", null, ["callee:00c57f10:8"]]
+ 00c05f8c ["INT_ADD", "register:40f0:8", ["const:c05f8c:8", "const:4:8"]]
+ 00c05f8c ["CALL", null, ["callee:00c57f10:8"]]
- 00c05b64 bytes eb470194
+ 00c05f8c bytes e1470194
- 00c05b44 ["INT_ADD", "register:40f0:8", ["const:c05b44:8", "const:4:8"]]
- 00c05b44 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00c05f6c ["INT_ADD", "register:40f0:8", ["const:c05f6c:8", "const:4:8"]]
+ 00c05f6c ["CALL", null, ["callee:00c57ef0:8"]]
- 00c05b44 bytes eb470194
+ 00c05f6c bytes e1470194
- 00c05b4c ["INT_ADD", "register:40f0:8", ["const:c05b4c:8", "const:4:8"]]
- 00c05b4c ["CALL", null, ["callee:00c5e480:8"]]
+ 00c05f74 ["INT_ADD", "register:40f0:8", ["const:c05f74:8", "const:4:8"]]
+ 00c05f74 ["CALL", null, ["callee:00c5e480:8"]]
- 00c05b4c bytes 4d610194
+ 00c05f74 bytes 43610194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c924055d836f0c81afe9bab165523f"></a>

### [`00c05bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md) → [`00c05ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ffc.md) FUN_00c05ffc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06030",
      "incomplete_value": true,
      "site": "00c06030",
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
      "definition_site": "00c05c08",
      "incomplete_value": true,
      "site": "00c05c08",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06028",
      "incomplete_value": true,
      "site": "00c06038",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c00",
      "incomplete_value": true,
      "site": "00c05c10",
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
            "const:18:8"
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
      "definition_site": "00c06034",
      "incomplete_value": true,
      "site": "00c0603c",
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
      "definition_site": "00c05c0c",
      "incomplete_value": true,
      "site": "00c05c14",
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
      "00c06018",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      "00c0601c",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c06030",
      "DATA",
      [
        "storage",
        "00c92e60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c06018",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00c0601c",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c06030",
      "DATA",
      [
        "storage",
        "00c93260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c05be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md#insn-00c05be4) · [`00c05bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md#insn-00c05bf0) · [`00c05bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md#insn-00c05bf4)
- 新版 `00c0600c`（命令位置の公開資料なし） · `00c06018`（命令位置の公開資料なし） · `00c0601c`（命令位置の公開資料なし）

~~~diff
- 00c05be4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c0600c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00c05be4 bytes a80400b0
+ 00c0600c bytes a80400b0
- 00c05bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c05bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 00c06018 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05bf0 bytes 084947f9
+ 00c06018 bytes 084941f9
- 00c05bf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00c05bf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c0601c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00c0601c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05bf4 bytes 29e143f9
+ 00c0601c bytes 29e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d8abb975634bf683910ce5793198269"></a>

### [`00c05c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md) → [`00c06080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06080.md) FUN_00c06080

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c060a0",
      "incomplete_value": true,
      "site": "00c060b4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c78",
      "incomplete_value": true,
      "site": "00c05c8c",
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
            "const:18:8"
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
      "definition_site": "00c060c0",
      "incomplete_value": true,
      "site": "00c060c0",
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
      "definition_site": "00c05c98",
      "incomplete_value": true,
      "site": "00c05c98",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c060c4",
      "incomplete_value": true,
      "site": "00c060c8",
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
      "definition_site": "00c05c9c",
      "incomplete_value": true,
      "site": "00c05ca0",
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
      "00c06094",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      "00c060b0",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c060b4",
      "DATA",
      [
        "storage",
        "00c92e38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c06094",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00c060b0",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c060b4",
      "DATA",
      [
        "storage",
        "00c93238",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c05c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md#insn-00c05c68) · [`00c05c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md#insn-00c05c6c) · [`00c05c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md#insn-00c05c88)
- 新版 `00c06090`（命令位置の公開資料なし） · `00c06094`（命令位置の公開資料なし） · `00c060b0`（命令位置の公開資料なし）

~~~diff
- 00c05c68 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c06090 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00c05c68 bytes a80400b0
+ 00c06090 bytes a80400b0
- 00c05c6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c05c6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 00c06094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05c6c bytes 084947f9
+ 00c06094 bytes 084941f9
- 00c05c88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00c05c88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c060b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00c060b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05c88 bytes 29e143f9
+ 00c060b0 bytes 29e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58426f74fd1ec071be95d7f1b79fe45"></a>

### [`00c05cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md) → [`00c06104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06104.md) FUN_00c06104

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06124",
      "incomplete_value": true,
      "site": "00c06138",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05cfc",
      "incomplete_value": true,
      "site": "00c05d10",
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
            "const:18:8"
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
      "definition_site": "00c06144",
      "incomplete_value": true,
      "site": "00c06144",
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
      "definition_site": "00c05d1c",
      "incomplete_value": true,
      "site": "00c05d1c",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06148",
      "incomplete_value": true,
      "site": "00c0614c",
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
      "definition_site": "00c05d20",
      "incomplete_value": true,
      "site": "00c05d24",
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
      "00c06118",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      "00c06134",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c06138",
      "DATA",
      [
        "storage",
        "00c92e38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c06118",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00c06134",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c06138",
      "DATA",
      [
        "storage",
        "00c93238",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c05cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md#insn-00c05cec) · [`00c05cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md#insn-00c05cf0) · [`00c05d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md#insn-00c05d0c)
- 新版 `00c06114`（命令位置の公開資料なし） · `00c06118`（命令位置の公開資料なし） · `00c06134`（命令位置の公開資料なし）

~~~diff
- 00c05cec ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c06114 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00c05cec bytes a80400b0
+ 00c06114 bytes a80400b0
- 00c05cf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c05cf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06118 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 00c06118 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05cf0 bytes 084947f9
+ 00c06118 bytes 084941f9
- 00c05d0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00c05d0c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06134 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00c06134 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c05d0c bytes 29e143f9
+ 00c06134 bytes 29e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b764b1ae4a642084397b68c29fd884d9"></a>

### [`00c061b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md) → [`00c065dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c065dc.md) FUN_00c065dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 4件 [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06604",
      "incomplete_value": false,
      "site": "00c06610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c061dc",
      "incomplete_value": false,
      "site": "00c061e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "definition_site": "00c06624",
      "incomplete_value": true,
      "site": "00c06628",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c061fc",
      "incomplete_value": true,
      "site": "00c06200",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
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
      "00c06610",
      "DATA",
      [
        "storage",
        "00c930f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c06624",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06624",
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c06610",
      "DATA",
      [
        "storage",
        "00c934f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c06624",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06624",
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c06200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md#insn-00c06200) · [`00c061d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md#insn-00c061d4) · [`00c061dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md#insn-00c061dc)
- 新版 `00c06628`（命令位置の公開資料なし） · `00c065fc`（命令位置の公開資料なし） · `00c06604`（命令位置の公開資料なし）

~~~diff
- 00c06200 ["INT_ADD", "register:40f0:8", ["const:c06200:8", "const:4:8"]]
- 00c06200 ["CALL", null, ["callee:00c58280:8"]]
+ 00c06628 ["INT_ADD", "register:40f0:8", ["const:c06628:8", "const:4:8"]]
+ 00c06628 ["CALL", null, ["callee:00c58280:8"]]
- 00c06200 bytes 20470194
+ 00c06628 bytes 16470194
- 00c061d4 ["INT_ADD", "register:40f0:8", ["const:c061d4:8", "const:4:8"]]
- 00c061d4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00c065fc ["INT_ADD", "register:40f0:8", ["const:c065fc:8", "const:4:8"]]
+ 00c065fc ["CALL", null, ["callee:00c581f0:8"]]
- 00c061d4 bytes 07470194
+ 00c065fc bytes fd460194
- 00c061dc ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00c061dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c061dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c061dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c06604 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00c06604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c06604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c06604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c061dc bytes 08e10391
+ 00c06604 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526e4443be242bf05fcd83f485f1e4a7"></a>

### [`00c0625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md) → [`00c06684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06684.md) FUN_00c06684

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06004.md) · 呼出先 4件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfe0.md)
- 新版 呼出元 1件 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 4件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3e0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c066ac",
      "incomplete_value": false,
      "site": "00c066b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06284",
      "incomplete_value": false,
      "site": "00c06290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "definition_site": "00c066cc",
      "incomplete_value": true,
      "site": "00c066d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c062a4",
      "incomplete_value": true,
      "site": "00c062a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7a8:8"
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
      "00c066b8",
      "DATA",
      [
        "storage",
        "00c93228",
        null,
        "undefined *"
      ]
    ],
    [
      "00c066cc",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c066cc",
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c066b8",
      "DATA",
      [
        "storage",
        "00c93628",
        null,
        "undefined *"
      ]
    ],
    [
      "00c066cc",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00c066cc",
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c062a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md#insn-00c062a8) · [`00c0627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md#insn-00c0627c) · [`00c06284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md#insn-00c06284)
- 新版 `00c066d0`（命令位置の公開資料なし） · `00c066a4`（命令位置の公開資料なし） · `00c066ac`（命令位置の公開資料なし）

~~~diff
- 00c062a8 ["INT_ADD", "register:40f0:8", ["const:c062a8:8", "const:4:8"]]
- 00c062a8 ["CALL", null, ["callee:00c58280:8"]]
+ 00c066d0 ["INT_ADD", "register:40f0:8", ["const:c066d0:8", "const:4:8"]]
+ 00c066d0 ["CALL", null, ["callee:00c58280:8"]]
- 00c062a8 bytes f6460194
+ 00c066d0 bytes ec460194
- 00c0627c ["INT_ADD", "register:40f0:8", ["const:c0627c:8", "const:4:8"]]
- 00c0627c ["CALL", null, ["callee:00c5e3e0:8"]]
+ 00c066a4 ["INT_ADD", "register:40f0:8", ["const:c066a4:8", "const:4:8"]]
+ 00c066a4 ["CALL", null, ["callee:00c5e3e0:8"]]
- 00c0627c bytes 595f0194
+ 00c066a4 bytes 4f5f0194
- 00c06284 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00c06284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c06284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c06284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c066ac ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00c066ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c066ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c066ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c06284 bytes 08a10891
+ 00c066ac bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-295ac492d6aefbc97833c73f643e0fb8"></a>

### [`00c06350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md) → [`00c06778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06778.md) _ZNSt6__ndk18ios_base4InitC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md) · 呼出先 5件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06304.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c5e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4f0.md) · 呼出先 5件 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) [`00c0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c0672c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c067ac",
      "incomplete_value": false,
      "site": "00c067b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06384",
      "incomplete_value": false,
      "site": "00c06388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c067b8",
      "value": [
        "leaf",
        "ram:c06190:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c06390",
      "value": [
        "leaf",
        "ram:c05d68:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c067c0",
      "incomplete_value": false,
      "site": "00c067d4",
      "value": [
        "leaf",
        "const:c0672c:8"
      ]
    },
    "old": {
      "definition_site": "00c06398",
      "incomplete_value": false,
      "site": "00c063ac",
      "value": [
        "leaf",
        "const:c06304:8"
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
      "00c06790",
      "READ",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c067ac",
      "PARAM",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c067b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c05d68"
      ]
    ]
  ],
  "added": [
    [
      "00c06790",
      "READ",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ],
    [
      "00c067ac",
      "PARAM",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ],
    [
      "00c067b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c06190"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c06388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c06388) · [`00c06390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c06390) · [`00c063ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c063ac)
- 新版 `00c067b0`（命令位置の公開資料なし） · `00c067b8`（命令位置の公開資料なし） · `00c067d4`（命令位置の公開資料なし）

~~~diff
- 00c06388 ["INT_ADD", "register:40f0:8", ["const:c06388:8", "const:4:8"]]
- 00c06388 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c067b0 ["INT_ADD", "register:40f0:8", ["const:c067b0:8", "const:4:8"]]
+ 00c067b0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c06388 bytes b2450194
+ 00c067b0 bytes a8450194
- 00c06390 ["INT_ADD", "register:40f0:8", ["const:c06390:8", "const:4:8"]]
- 00c06390 ["CALL", null, ["ram:c05d68:8"]]
+ 00c067b8 ["INT_ADD", "register:40f0:8", ["const:c067b8:8", "const:4:8"]]
+ 00c067b8 ["CALL", null, ["ram:c06190:8"]]
- 00c06390 bytes 76feff97
+ 00c067b8 bytes 76feff97
- 00c063ac ["INT_ADD", "register:40f0:8", ["const:c063ac:8", "const:4:8"]]
- 00c063ac ["CALL", null, ["callee:00c57e30:8"]]
+ 00c067d4 ["INT_ADD", "register:40f0:8", ["const:c067d4:8", "const:4:8"]]
+ 00c067d4 ["CALL", null, ["callee:00c57e30:8"]]
- 00c063ac bytes a1450194
+ 00c067d4 bytes 97450194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41dd5ea041a3c87bd25b2077c9d875c0"></a>

### [`00c06414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md) → [`00c0683c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c0683c.md) FUN_00c0683c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 2件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

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
      "definition_site": "00c06858",
      "incomplete_value": true,
      "site": "00c06860",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06430",
      "incomplete_value": true,
      "site": "00c06438",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
              ]
            ]
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
      "definition_site": "00c068b4",
      "incomplete_value": false,
      "site": "00c068b8",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0648c",
      "incomplete_value": false,
      "site": "00c06490",
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
            "const:cf7:8"
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
      "00c06858",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06858",
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c068b4",
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c06858",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06858",
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c068b4",
      "PARAM",
      [
        "storage",
        "002b5d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c06438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md#insn-00c06438) · [`00c06490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md#insn-00c06490) · [`00c06430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md#insn-00c06430)
- 新版 `00c06860`（命令位置の公開資料なし） · `00c068b8`（命令位置の公開資料なし） · `00c06858`（命令位置の公開資料なし）

~~~diff
- 00c06438 ["INT_ADD", "register:40f0:8", ["const:c06438:8", "const:4:8"]]
- 00c06438 ["CALL", null, ["callee:00c58280:8"]]
+ 00c06860 ["INT_ADD", "register:40f0:8", ["const:c06860:8", "const:4:8"]]
+ 00c06860 ["CALL", null, ["callee:00c58280:8"]]
- 00c06438 bytes 92460194
+ 00c06860 bytes 88460194
- 00c06490 ["INT_ADD", "register:40f0:8", ["const:c06490:8", "const:4:8"]]
- 00c06490 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c068b8 ["INT_ADD", "register:40f0:8", ["const:c068b8:8", "const:4:8"]]
+ 00c068b8 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c06490 bytes c85d0194
+ 00c068b8 bytes be5d0194
- 00c06430 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 00c06430 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06858 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8b8:8"]]
+ 00c06858 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c06430 bytes 215c42f9
+ 00c06858 bytes 215c44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c953b99b80810f38675ae4ef055bbf18"></a>

### [`00c067a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md) → [`00c06bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06bd0.md) FUN_00c06bd0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06bfc",
      "incomplete_value": true,
      "site": "00c06c00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c067d4",
      "incomplete_value": true,
      "site": "00c067d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
              ]
            ]
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
      "00c06bfc",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06bfc",
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c06bfc",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06bfc",
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c067d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067d8) · [`00c067c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067c8) · [`00c067d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067d4)
- 新版 `00c06c00`（命令位置の公開資料なし） · `00c06bf0`（命令位置の公開資料なし） · `00c06bfc`（命令位置の公開資料なし）

~~~diff
- 00c067d8 ["INT_ADD", "register:40f0:8", ["const:c067d8:8", "const:4:8"]]
- 00c067d8 ["CALL", null, ["callee:00c58280:8"]]
+ 00c06c00 ["INT_ADD", "register:40f0:8", ["const:c06c00:8", "const:4:8"]]
+ 00c06c00 ["CALL", null, ["callee:00c58280:8"]]
- 00c067d8 bytes aa450194
+ 00c06c00 bytes a0450194
- 00c067c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c067c8 ["INT_ADD", "register:40f0:8", ["const:c067c8:8", "const:4:8"]]
- 00c067c8 ["CALLIND", null, ["register:0:8"]]
+ 00c06bf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06bf0 ["INT_ADD", "register:40f0:8", ["const:c06bf0:8", "const:4:8"]]
+ 00c06bf0 ["CALLIND", null, ["register:0:8"]]
- 00c067c8 bytes 00013fd6
+ 00c06bf0 bytes 00013fd6
- 00c067d4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 00c067d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06bfc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8b8:8"]]
+ 00c06bfc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c067d4 bytes 215c42f9
+ 00c06bfc bytes 215c44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86bf0a3a8bd54d43dfc2e55ed90efc54"></a>

### [`00c06aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md) → [`00c06ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ed0.md) FUN_00c06ed0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c06190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 2件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

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
      "definition_site": "00c06eec",
      "incomplete_value": true,
      "site": "00c06ef4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06ac4",
      "incomplete_value": true,
      "site": "00c06acc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7a8:8"
              ]
            ]
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
      "definition_site": "00c06f48",
      "incomplete_value": false,
      "site": "00c06f4c",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06b20",
      "incomplete_value": false,
      "site": "00c06b24",
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
            "const:cf7:8"
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
      "00c06eec",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06eec",
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c06f48",
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c06eec",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06eec",
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c06f48",
      "PARAM",
      [
        "storage",
        "002b5d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c06acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md#insn-00c06acc) · [`00c06b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md#insn-00c06b24) · [`00c06ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md#insn-00c06ac4)
- 新版 `00c06ef4`（命令位置の公開資料なし） · `00c06f4c`（命令位置の公開資料なし） · `00c06eec`（命令位置の公開資料なし）

~~~diff
- 00c06acc ["INT_ADD", "register:40f0:8", ["const:c06acc:8", "const:4:8"]]
- 00c06acc ["CALL", null, ["callee:00c58280:8"]]
+ 00c06ef4 ["INT_ADD", "register:40f0:8", ["const:c06ef4:8", "const:4:8"]]
+ 00c06ef4 ["CALL", null, ["callee:00c58280:8"]]
- 00c06acc bytes ed440194
+ 00c06ef4 bytes e3440194
- 00c06b24 ["INT_ADD", "register:40f0:8", ["const:c06b24:8", "const:4:8"]]
- 00c06b24 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c06f4c ["INT_ADD", "register:40f0:8", ["const:c06f4c:8", "const:4:8"]]
+ 00c06f4c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c06b24 bytes 235c0194
+ 00c06f4c bytes 195c0194
- 00c06ac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7a8:8"]]
- 00c06ac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c06eec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ba8:8"]]
+ 00c06eec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c06ac4 bytes 21d443f9
+ 00c06eec bytes 21d445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04012b051093dfbec8cab06df85d7d0b"></a>

### [`00c06e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md) → [`00c0725c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0725c.md) FUN_00c0725c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c07288",
      "incomplete_value": true,
      "site": "00c0728c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06e60",
      "incomplete_value": true,
      "site": "00c06e64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7a8:8"
              ]
            ]
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
      "00c07288",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c07288",
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c07288",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00c07288",
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c06e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e64) · [`00c06e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e54) · [`00c06e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e60)
- 新版 `00c0728c`（命令位置の公開資料なし） · `00c0727c`（命令位置の公開資料なし） · `00c07288`（命令位置の公開資料なし）

~~~diff
- 00c06e64 ["INT_ADD", "register:40f0:8", ["const:c06e64:8", "const:4:8"]]
- 00c06e64 ["CALL", null, ["callee:00c58280:8"]]
+ 00c0728c ["INT_ADD", "register:40f0:8", ["const:c0728c:8", "const:4:8"]]
+ 00c0728c ["CALL", null, ["callee:00c58280:8"]]
- 00c06e64 bytes 07440194
+ 00c0728c bytes fd430194
- 00c06e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06e54 ["INT_ADD", "register:40f0:8", ["const:c06e54:8", "const:4:8"]]
- 00c06e54 ["CALLIND", null, ["register:0:8"]]
+ 00c0727c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0727c ["INT_ADD", "register:40f0:8", ["const:c0727c:8", "const:4:8"]]
+ 00c0727c ["CALLIND", null, ["register:0:8"]]
- 00c06e54 bytes 00013fd6
+ 00c0727c bytes 00013fd6
- 00c06e60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7a8:8"]]
- 00c06e60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c07288 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ba8:8"]]
+ 00c07288 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c06e60 bytes 21d443f9
+ 00c07288 bytes 21d445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b62eff56193d9a06df8771109ade637"></a>

### [`00c070fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md) → [`00c07524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07524.md) _INIT_2

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c063e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c063e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5e0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c06808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06808.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0753c",
      "incomplete_value": false,
      "site": "00c07540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c07114",
      "incomplete_value": false,
      "site": "00c07118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "00c0753c",
      "PARAM",
      [
        "storage",
        "011274c0",
        null,
        null
      ]
    ],
    [
      "00c0754c",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ],
    [
      "00c07550",
      "READ",
      [
        "storage",
        "00c9b7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c0753c",
      "PARAM",
      [
        "storage",
        "011278c0",
        null,
        null
      ]
    ],
    [
      "00c0754c",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ],
    [
      "00c07550",
      "READ",
      [
        "storage",
        "00c9bbb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c07118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md#insn-00c07118) · [`00c07110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md#insn-00c07110) · [`00c07124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md#insn-00c07124)
- 新版 `00c07540`（命令位置の公開資料なし） · `00c07538`（命令位置の公開資料なし） · `00c0754c`（命令位置の公開資料なし）

~~~diff
- 00c07118 ["INT_ADD", "register:40f0:8", ["const:c07118:8", "const:4:8"]]
- 00c07118 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c07540 ["INT_ADD", "register:40f0:8", ["const:c07540:8", "const:4:8"]]
+ 00c07540 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c07118 bytes f65b0194
+ 00c07540 bytes ec5b0194
- 00c07110 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00c07110 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c07110 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c07110 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c07538 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00c07538 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c07538 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c07538 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c07110 bytes 73021391
+ 00c07538 bytes 73022391
- 00c07124 ["COPY", "register:4010:8", ["const:c62b90:8"]]
+ 00c0754c ["COPY", "register:4010:8", ["const:c62f90:8"]]
- 00c07124 bytes 62d32d10
+ 00c0754c bytes 22d22d10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268574e2c7798df91bac824981891120"></a>

### [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) → [`00c0788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c07910",
      "incomplete_value": true,
      "site": "00c07910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c074e8",
      "incomplete_value": true,
      "site": "00c074e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c07988",
      "incomplete_value": true,
      "site": "00c07988",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c07560",
      "incomplete_value": true,
      "site": "00c07560",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c07918",
      "incomplete_value": true,
      "site": "00c0791c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c074f0",
      "incomplete_value": true,
      "site": "00c074f4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c07908",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c07910",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c07914",
      "READ",
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
      "00c07908",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c07910",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c07914",
      "READ",
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

- 旧版 [`00c0751c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md#insn-00c0751c) · [`00c07594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md#insn-00c07594) · [`00c074ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md#insn-00c074ac)
- 新版 `00c07944`（命令位置の公開資料なし） · `00c079bc`（命令位置の公開資料なし） · `00c078d4`（命令位置の公開資料なし）

~~~diff
- 00c0751c ["INT_ADD", "register:40f0:8", ["const:c0751c:8", "const:4:8"]]
- 00c0751c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c07944 ["INT_ADD", "register:40f0:8", ["const:c07944:8", "const:4:8"]]
+ 00c07944 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0751c bytes 71590194
+ 00c07944 bytes 67590194
- 00c07594 ["INT_ADD", "register:40f0:8", ["const:c07594:8", "const:4:8"]]
- 00c07594 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c079bc ["INT_ADD", "register:40f0:8", ["const:c079bc:8", "const:4:8"]]
+ 00c079bc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c07594 bytes 53590194
+ 00c079bc bytes 49590194
- 00c074ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00c074ac ["INT_ADD", "register:40f0:8", ["const:c074ac:8", "const:4:8"]]
- 00c074ac ["CALLIND", null, ["register:0:8"]]
+ 00c078d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c078d4 ["INT_ADD", "register:40f0:8", ["const:c078d4:8", "const:4:8"]]
+ 00c078d4 ["CALLIND", null, ["register:0:8"]]
- 00c074ac bytes 00013fd6
+ 00c078d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-523dfdc841763258a463b810129676b2"></a>

### [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) → [`00c0a534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0a580",
      "incomplete_value": true,
      "site": "00c0a580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c0a158",
      "incomplete_value": true,
      "site": "00c0a158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0a9fc",
      "incomplete_value": true,
      "site": "00c0a9fc",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a5d4",
      "incomplete_value": true,
      "site": "00c0a5d4",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0a588",
      "incomplete_value": true,
      "site": "00c0a58c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0a160",
      "incomplete_value": true,
      "site": "00c0a164",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c0a578",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a580",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a584",
      "READ",
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
      "00c0a578",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a580",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a584",
      "READ",
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

- 旧版 [`00c0a18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md#insn-00c0a18c) · [`00c0a1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md#insn-00c0a1cc) · [`00c0a4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md#insn-00c0a4d4)
- 新版 `00c0a5b4`（命令位置の公開資料なし） · `00c0a5f4`（命令位置の公開資料なし） · `00c0a8fc`（命令位置の公開資料なし）

~~~diff
- 00c0a18c ["INT_ADD", "register:40f0:8", ["const:c0a18c:8", "const:4:8"]]
- 00c0a18c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0a5b4 ["INT_ADD", "register:40f0:8", ["const:c0a5b4:8", "const:4:8"]]
+ 00c0a5b4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0a18c bytes 554e0194
+ 00c0a5b4 bytes 4b4e0194
- 00c0a1cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0a1cc ["INT_ADD", "register:40f0:8", ["const:c0a1cc:8", "const:4:8"]]
- 00c0a1cc ["CALLIND", null, ["register:0:8"]]
+ 00c0a5f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0a5f4 ["INT_ADD", "register:40f0:8", ["const:c0a5f4:8", "const:4:8"]]
+ 00c0a5f4 ["CALLIND", null, ["register:0:8"]]
- 00c0a1cc bytes 00013fd6
+ 00c0a5f4 bytes 00013fd6
- 00c0a4d4 ["INT_ADD", "register:40f0:8", ["const:c0a4d4:8", "const:4:8"]]
- 00c0a4d4 ["CALL", null, ["callee:00c0ac28:8"]]
+ 00c0a8fc ["INT_ADD", "register:40f0:8", ["const:c0a8fc:8", "const:4:8"]]
+ 00c0a8fc ["CALL", null, ["callee:00c0ac28:8"]]
- 00c0a4d4 bytes cb000094
+ 00c0a8fc bytes cb000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a762632cce91dee999dd08bd4a58dc8b"></a>

### [`00c0a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md) → [`00c0acdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0acdc.md) _ZNSt6__ndk16__clocEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0ad38",
      "incomplete_value": true,
      "site": "00c0ad38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a910",
      "incomplete_value": true,
      "site": "00c0a910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0ad18",
      "incomplete_value": false,
      "site": "00c0ad1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a8f0",
      "incomplete_value": false,
      "site": "00c0a8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c0ad28",
      "incomplete_value": false,
      "site": "00c0ad34",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a900",
      "incomplete_value": false,
      "site": "00c0a90c",
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
            "const:13c:8"
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
      "00c0acf8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ad00",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ad18",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0acf8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ad00",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ad18",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0a8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a8f4) · [`00c0a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a90c) · [`00c0a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a910)
- 新版 `00c0ad1c`（命令位置の公開資料なし） · `00c0ad34`（命令位置の公開資料なし） · `00c0ad38`（命令位置の公開資料なし）

~~~diff
- 00c0a8f4 ["INT_ADD", "register:40f0:8", ["const:c0a8f4:8", "const:4:8"]]
- 00c0a8f4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0ad1c ["INT_ADD", "register:40f0:8", ["const:c0ad1c:8", "const:4:8"]]
+ 00c0ad1c ["CALL", null, ["callee:00c57e50:8"]]
- 00c0a8f4 bytes 57340194
+ 00c0ad1c bytes 4d340194
- 00c0a90c ["INT_ADD", "register:40f0:8", ["const:c0a90c:8", "const:4:8"]]
- 00c0a90c ["CALL", null, ["callee:00c5d220:8"]]
+ 00c0ad34 ["INT_ADD", "register:40f0:8", ["const:c0ad34:8", "const:4:8"]]
+ 00c0ad34 ["CALL", null, ["callee:00c5d220:8"]]
- 00c0a90c bytes 45490194
+ 00c0ad34 bytes 3b490194
- 00c0a910 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00c0a910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c0ad38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00c0ad38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c0a910 bytes 604e04f9
+ 00c0ad38 bytes 604e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ccefd413138d12d77c725394a2225a3"></a>

### [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) → [`00c0ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ade8",
      "incomplete_value": true,
      "site": "00c0ade8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a9c0",
      "incomplete_value": true,
      "site": "00c0a9c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c0ae60",
      "incomplete_value": true,
      "site": "00c0ae60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c0aa38",
      "incomplete_value": true,
      "site": "00c0aa38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0adf0",
      "incomplete_value": true,
      "site": "00c0adf4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0a9c8",
      "incomplete_value": true,
      "site": "00c0a9cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0ade0",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ade8",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0adec",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0ade0",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ade8",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0adec",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0a9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md#insn-00c0a9f4) · [`00c0aa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md#insn-00c0aa6c) · [`00c0a984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md#insn-00c0a984)
- 新版 `00c0ae1c`（命令位置の公開資料なし） · `00c0ae94`（命令位置の公開資料なし） · `00c0adac`（命令位置の公開資料なし）

~~~diff
- 00c0a9f4 ["INT_ADD", "register:40f0:8", ["const:c0a9f4:8", "const:4:8"]]
- 00c0a9f4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0ae1c ["INT_ADD", "register:40f0:8", ["const:c0ae1c:8", "const:4:8"]]
+ 00c0ae1c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0a9f4 bytes 3b4c0194
+ 00c0ae1c bytes 314c0194
- 00c0aa6c ["INT_ADD", "register:40f0:8", ["const:c0aa6c:8", "const:4:8"]]
- 00c0aa6c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0ae94 ["INT_ADD", "register:40f0:8", ["const:c0ae94:8", "const:4:8"]]
+ 00c0ae94 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0aa6c bytes 1d4c0194
+ 00c0ae94 bytes 134c0194
- 00c0a984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0a984 ["INT_ADD", "register:40f0:8", ["const:c0a984:8", "const:4:8"]]
- 00c0a984 ["CALLIND", null, ["register:0:8"]]
+ 00c0adac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0adac ["INT_ADD", "register:40f0:8", ["const:c0adac:8", "const:4:8"]]
+ 00c0adac ["CALLIND", null, ["register:0:8"]]
- 00c0a984 bytes 00013fd6
+ 00c0adac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bed4733c19fd4180d471d3c20aa4276"></a>

### [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) → [`00c0d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0d9f4",
      "incomplete_value": true,
      "site": "00c0d9f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0d5cc",
      "incomplete_value": true,
      "site": "00c0d5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c0de64",
      "incomplete_value": true,
      "site": "00c0de64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0da3c",
      "incomplete_value": true,
      "site": "00c0da3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0d9fc",
      "incomplete_value": true,
      "site": "00c0da00",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0d5d4",
      "incomplete_value": true,
      "site": "00c0d5d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c0d9ec",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0d9f4",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0d9f8",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0d9ec",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c0d9f4",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0d9f8",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0d5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md#insn-00c0d5f8) · [`00c0d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md#insn-00c0d600) · [`00c0d640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md#insn-00c0d640)
- 新版 `00c0da20`（命令位置の公開資料なし） · `00c0da28`（命令位置の公開資料なし） · `00c0da68`（命令位置の公開資料なし）

~~~diff
- 00c0d5f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
- 00c0d5f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c0da20 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
+ 00c0da20 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c0d5f8 bytes 00a043f9
+ 00c0da20 bytes 00a045f9
- 00c0d600 ["INT_ADD", "register:40f0:8", ["const:c0d600:8", "const:4:8"]]
- 00c0d600 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0da28 ["INT_ADD", "register:40f0:8", ["const:c0da28:8", "const:4:8"]]
+ 00c0da28 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0d600 bytes 38410194
+ 00c0da28 bytes 2e410194
- 00c0d640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0d640 ["INT_ADD", "register:40f0:8", ["const:c0d640:8", "const:4:8"]]
- 00c0d640 ["CALLIND", null, ["register:0:8"]]
+ 00c0da68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0da68 ["INT_ADD", "register:40f0:8", ["const:c0da68:8", "const:4:8"]]
+ 00c0da68 ["CALLIND", null, ["register:0:8"]]
- 00c0d640 bytes 00013fd6
+ 00c0da68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b384931f7aba8cbec85cc9c4dac327cd"></a>

### [`00c0dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) → [`00c0e08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_prepERNS_8ios_baseEPcRcS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e550.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e144",
      "incomplete_value": true,
      "site": "00c0e14c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0dd1c",
      "incomplete_value": true,
      "site": "00c0dd24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0e0f8",
      "incomplete_value": true,
      "site": "00c0e100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c0dcd0",
      "incomplete_value": true,
      "site": "00c0dcd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0e0f4",
      "incomplete_value": false,
      "site": "00c0e100",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c0dccc",
      "incomplete_value": false,
      "site": "00c0dcd8",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      "00c0e0c4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e0cc",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e0d0",
      "READ",
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
      "00c0e0c4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e0cc",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e0d0",
      "READ",
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

- 旧版 [`00c0dcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md#insn-00c0dcd8) · [`00c0dd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md#insn-00c0dd58) · [`00c0dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md#insn-00c0dc94)
- 新版 `00c0e100`（命令位置の公開資料なし） · `00c0e180`（命令位置の公開資料なし） · `00c0e0bc`（命令位置の公開資料なし）

~~~diff
- 00c0dcd8 ["INT_ADD", "register:40f0:8", ["const:c0dcd8:8", "const:4:8"]]
- 00c0dcd8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0e100 ["INT_ADD", "register:40f0:8", ["const:c0e100:8", "const:4:8"]]
+ 00c0e100 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0dcd8 bytes 823f0194
+ 00c0e100 bytes 783f0194
- 00c0dd58 ["INT_ADD", "register:40f0:8", ["const:c0dd58:8", "const:4:8"]]
- 00c0dd58 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0e180 ["INT_ADD", "register:40f0:8", ["const:c0e180:8", "const:4:8"]]
+ 00c0e180 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0dd58 bytes 623f0194
+ 00c0e180 bytes 583f0194
- 00c0dc94 ["INT_ADD", "register:40f0:8", ["const:c0dc94:8", "const:4:8"]]
- 00c0dc94 ["CALL", null, ["callee:00c58270:8"]]
+ 00c0e0bc ["INT_ADD", "register:40f0:8", ["const:c0e0bc:8", "const:4:8"]]
+ 00c0e0bc ["CALL", null, ["callee:00c58270:8"]]
- 00c0dc94 bytes 77280194
+ 00c0e0bc bytes 6d280194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba51f9f48d97d772c641d05d01902d7"></a>

### [`00c0e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md) → [`00c0e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e4a0.md) _ZNSt6__ndk19__num_getIcE17__stage2_int_prepERNS_8ios_baseEPcRc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e554",
      "incomplete_value": true,
      "site": "00c0e55c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e12c",
      "incomplete_value": true,
      "site": "00c0e134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
      "definition_site": "00c0e544",
      "incomplete_value": true,
      "site": "00c0e54c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e11c",
      "incomplete_value": true,
      "site": "00c0e124",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0e548",
      "incomplete_value": true,
      "site": "00c0e54c",
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
            "const:1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e120",
      "incomplete_value": true,
      "site": "00c0e124",
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
            "const:1a:8"
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
      "00c0e4d4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e4dc",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e4e0",
      "READ",
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
      "00c0e4d4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e4dc",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e4e0",
      "READ",
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

- 旧版 [`00c0e124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md#insn-00c0e124) · [`00c0e168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md#insn-00c0e168) · [`00c0e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md#insn-00c0e0a4)
- 新版 `00c0e54c`（命令位置の公開資料なし） · `00c0e590`（命令位置の公開資料なし） · `00c0e4cc`（命令位置の公開資料なし）

~~~diff
- 00c0e124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0e124 ["INT_ADD", "register:40f0:8", ["const:c0e124:8", "const:4:8"]]
- 00c0e124 ["CALLIND", null, ["register:0:8"]]
+ 00c0e54c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0e54c ["INT_ADD", "register:40f0:8", ["const:c0e54c:8", "const:4:8"]]
+ 00c0e54c ["CALLIND", null, ["register:0:8"]]
- 00c0e124 bytes 00013fd6
+ 00c0e54c bytes 00013fd6
- 00c0e168 ["INT_ADD", "register:40f0:8", ["const:c0e168:8", "const:4:8"]]
- 00c0e168 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0e590 ["INT_ADD", "register:40f0:8", ["const:c0e590:8", "const:4:8"]]
+ 00c0e590 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e168 bytes 5e3e0194
+ 00c0e590 bytes 543e0194
- 00c0e0a4 ["INT_ADD", "register:40f0:8", ["const:c0e0a4:8", "const:4:8"]]
- 00c0e0a4 ["CALL", null, ["callee:00c58270:8"]]
+ 00c0e4cc ["INT_ADD", "register:40f0:8", ["const:c0e4cc:8", "const:4:8"]]
+ 00c0e4cc ["CALL", null, ["callee:00c58270:8"]]
- 00c0e0a4 bytes 73270194
+ 00c0e4cc bytes 69270194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f562c99693bb0751dd457563d77fbbf7"></a>

### [`00c0e1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md) → [`00c0e620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e620.md) _ZNSt6__ndk19__num_getIwE19__stage2_float_prepERNS_8ios_baseEPwRwS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5b0.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e658",
      "incomplete_value": true,
      "site": "00c0e660",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e230",
      "incomplete_value": true,
      "site": "00c0e238",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c0e6d8",
      "incomplete_value": true,
      "site": "00c0e6e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c0e2b0",
      "incomplete_value": true,
      "site": "00c0e2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0e668",
      "incomplete_value": true,
      "site": "00c0e66c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0e240",
      "incomplete_value": true,
      "site": "00c0e244",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c0e658",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e660",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e664",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0e658",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e660",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e664",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md#insn-00c0e26c) · [`00c0e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md#insn-00c0e2a8) · [`00c0e2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md#insn-00c0e2ec)
- 新版 `00c0e694`（命令位置の公開資料なし） · `00c0e6d0`（命令位置の公開資料なし） · `00c0e714`（命令位置の公開資料なし）

~~~diff
- 00c0e26c ["INT_ADD", "register:40f0:8", ["const:c0e26c:8", "const:4:8"]]
- 00c0e26c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0e694 ["INT_ADD", "register:40f0:8", ["const:c0e694:8", "const:4:8"]]
+ 00c0e694 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e26c bytes 1d3e0194
+ 00c0e694 bytes 133e0194
- 00c0e2a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0e2a8 ["INT_ADD", "register:40f0:8", ["const:c0e2a8:8", "const:4:8"]]
- 00c0e2a8 ["CALLIND", null, ["register:0:8"]]
+ 00c0e6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0e6d0 ["INT_ADD", "register:40f0:8", ["const:c0e6d0:8", "const:4:8"]]
+ 00c0e6d0 ["CALLIND", null, ["register:0:8"]]
- 00c0e2a8 bytes 00013fd6
+ 00c0e6d0 bytes 00013fd6
- 00c0e2ec ["INT_ADD", "register:40f0:8", ["const:c0e2ec:8", "const:4:8"]]
- 00c0e2ec ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0e714 ["INT_ADD", "register:40f0:8", ["const:c0e714:8", "const:4:8"]]
+ 00c0e714 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e2ec bytes fd3d0194
+ 00c0e714 bytes f33d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2290994eb2144b10b31ba8d6a47443ae"></a>

### [`00c0e5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md) → [`00c0ea20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ea20.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ea54",
      "incomplete_value": true,
      "site": "00c0ea5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e62c",
      "incomplete_value": true,
      "site": "00c0e634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c0ead4",
      "incomplete_value": true,
      "site": "00c0eadc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c0e6ac",
      "incomplete_value": true,
      "site": "00c0e6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0ea64",
      "incomplete_value": true,
      "site": "00c0ea68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0e63c",
      "incomplete_value": true,
      "site": "00c0e640",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c0ea54",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ea5c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ea60",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0ea54",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ea5c",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ea60",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md#insn-00c0e668) · [`00c0e6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md#insn-00c0e6a4) · [`00c0e6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md#insn-00c0e6e8)
- 新版 `00c0ea90`（命令位置の公開資料なし） · `00c0eacc`（命令位置の公開資料なし） · `00c0eb10`（命令位置の公開資料なし）

~~~diff
- 00c0e668 ["INT_ADD", "register:40f0:8", ["const:c0e668:8", "const:4:8"]]
- 00c0e668 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0ea90 ["INT_ADD", "register:40f0:8", ["const:c0ea90:8", "const:4:8"]]
+ 00c0ea90 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e668 bytes 1e3d0194
+ 00c0ea90 bytes 143d0194
- 00c0e6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0e6a4 ["INT_ADD", "register:40f0:8", ["const:c0e6a4:8", "const:4:8"]]
- 00c0e6a4 ["CALLIND", null, ["register:0:8"]]
+ 00c0eacc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0eacc ["INT_ADD", "register:40f0:8", ["const:c0eacc:8", "const:4:8"]]
+ 00c0eacc ["CALLIND", null, ["register:0:8"]]
- 00c0e6a4 bytes 00013fd6
+ 00c0eacc bytes 00013fd6
- 00c0e6e8 ["INT_ADD", "register:40f0:8", ["const:c0e6e8:8", "const:4:8"]]
- 00c0e6e8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0eb10 ["INT_ADD", "register:40f0:8", ["const:c0eb10:8", "const:4:8"]]
+ 00c0eb10 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e6e8 bytes fe3c0194
+ 00c0eb10 bytes f43c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-070797b78539ee518e1cbb26120d591a"></a>

### [`00c0e778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md) → [`00c0eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0eba0.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ec08",
      "incomplete_value": true,
      "site": "00c0ec08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e7e0",
      "incomplete_value": true,
      "site": "00c0e7e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0ec10",
      "incomplete_value": true,
      "site": "00c0ec14",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0e7e8",
      "incomplete_value": true,
      "site": "00c0e7ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0ec34",
      "incomplete_value": true,
      "site": "00c0ec3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e80c",
      "incomplete_value": true,
      "site": "00c0e814",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
              ]
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
      "00c0ec00",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ec08",
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ec0c",
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0ec00",
      "READ",
      [
        "storage",
        "00c9bbb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ec08",
      "DATA",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ec0c",
      "READ",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0e814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md#insn-00c0e814) · [`00c0e7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md#insn-00c0e7d0) · [`00c0e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md#insn-00c0e7d8)
- 新版 `00c0ec3c`（命令位置の公開資料なし） · `00c0ebf8`（命令位置の公開資料なし） · `00c0ec00`（命令位置の公開資料なし）

~~~diff
- 00c0e814 ["INT_ADD", "register:40f0:8", ["const:c0e814:8", "const:4:8"]]
- 00c0e814 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c0ec3c ["INT_ADD", "register:40f0:8", ["const:c0ec3c:8", "const:4:8"]]
+ 00c0ec3c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0e814 bytes b33c0194
+ 00c0ec3c bytes a93c0194
- 00c0e7d0 ["INT_ADD", "register:40f0:8", ["const:c0e7d0:8", "const:4:8"]]
- 00c0e7d0 ["CALL", null, ["callee:00c58270:8"]]
+ 00c0ebf8 ["INT_ADD", "register:40f0:8", ["const:c0ebf8:8", "const:4:8"]]
+ 00c0ebf8 ["CALL", null, ["callee:00c58270:8"]]
- 00c0e7d0 bytes a8250194
+ 00c0ebf8 bytes 9e250194
- 00c0e7d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
- 00c0e7d8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c0ec00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
+ 00c0ec00 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c0e7d8 bytes d6de43f9
+ 00c0ec00 bytes d6de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20c6272bd454c5f4cc75bae57ad6d2bc"></a>

### [`00c0e958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md) → [`00c0ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed80.md) FUN_00c0ed80

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c0e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e948.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed70.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0ef7c",
      "incomplete_value": true,
      "site": "00c0ef7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eb54",
      "incomplete_value": true,
      "site": "00c0eb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0ee60",
      "incomplete_value": true,
      "site": "00c0ee78",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ea38",
      "incomplete_value": true,
      "site": "00c0ea50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0ef5c",
      "incomplete_value": false,
      "site": "00c0ef60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eb34",
      "incomplete_value": false,
      "site": "00c0eb38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c0ee54",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ee60",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ef5c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0ee54",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ee60",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ef5c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0ea50) · [`00c0eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0eb38) · [`00c0eb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0eb50)
- 新版 `00c0ee78`（命令位置の公開資料なし） · `00c0ef60`（命令位置の公開資料なし） · `00c0ef78`（命令位置の公開資料なし）

~~~diff
- 00c0ea50 ["INT_ADD", "register:40f0:8", ["const:c0ea50:8", "const:4:8"]]
- 00c0ea50 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0ee78 ["INT_ADD", "register:40f0:8", ["const:c0ee78:8", "const:4:8"]]
+ 00c0ee78 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0ea50 bytes cb040094
+ 00c0ee78 bytes cb040094
- 00c0eb38 ["INT_ADD", "register:40f0:8", ["const:c0eb38:8", "const:4:8"]]
- 00c0eb38 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0ef60 ["INT_ADD", "register:40f0:8", ["const:c0ef60:8", "const:4:8"]]
+ 00c0ef60 ["CALL", null, ["callee:00c57e50:8"]]
- 00c0eb38 bytes c6230194
+ 00c0ef60 bytes bc230194
- 00c0eb50 ["INT_ADD", "register:40f0:8", ["const:c0eb50:8", "const:4:8"]]
- 00c0eb50 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c0ef78 ["INT_ADD", "register:40f0:8", ["const:c0ef78:8", "const:4:8"]]
+ 00c0ef78 ["CALL", null, ["callee:00c5d220:8"]]
- 00c0eb50 bytes b4380194
+ 00c0ef78 bytes aa380194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584d5f43acf44525721d75865ca8458a"></a>

### [`00c0eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md) → [`00c0efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efcc.md) FUN_00c0efcc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c0eb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eb94.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0efbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efbc.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f1c8",
      "incomplete_value": true,
      "site": "00c0f1c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eda0",
      "incomplete_value": true,
      "site": "00c0eda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0f0ac",
      "incomplete_value": true,
      "site": "00c0f0c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ec84",
      "incomplete_value": true,
      "site": "00c0ec9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f1a8",
      "incomplete_value": false,
      "site": "00c0f1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ed80",
      "incomplete_value": false,
      "site": "00c0ed84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c0f0a0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f0ac",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f1a8",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0f0a0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f0ac",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f1a8",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md#insn-00c0ec9c) · [`00c0ed84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md#insn-00c0ed84) · [`00c0ed9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md#insn-00c0ed9c)
- 新版 `00c0f0c4`（命令位置の公開資料なし） · `00c0f1ac`（命令位置の公開資料なし） · `00c0f1c4`（命令位置の公開資料なし）

~~~diff
- 00c0ec9c ["INT_ADD", "register:40f0:8", ["const:c0ec9c:8", "const:4:8"]]
- 00c0ec9c ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0f0c4 ["INT_ADD", "register:40f0:8", ["const:c0f0c4:8", "const:4:8"]]
+ 00c0f0c4 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0ec9c bytes 38040094
+ 00c0f0c4 bytes 38040094
- 00c0ed84 ["INT_ADD", "register:40f0:8", ["const:c0ed84:8", "const:4:8"]]
- 00c0ed84 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0f1ac ["INT_ADD", "register:40f0:8", ["const:c0f1ac:8", "const:4:8"]]
+ 00c0f1ac ["CALL", null, ["callee:00c57e50:8"]]
- 00c0ed84 bytes 33230194
+ 00c0f1ac bytes 29230194
- 00c0ed9c ["INT_ADD", "register:40f0:8", ["const:c0ed9c:8", "const:4:8"]]
- 00c0ed9c ["CALL", null, ["callee:00c5d220:8"]]
+ 00c0f1c4 ["INT_ADD", "register:40f0:8", ["const:c0f1c4:8", "const:4:8"]]
+ 00c0f1c4 ["CALL", null, ["callee:00c5d220:8"]]
- 00c0ed9c bytes 21380194
+ 00c0f1c4 bytes 17380194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b37ee64e52ed44d577acaed49053948"></a>

### [`00c0edf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md) → [`00c0f218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f218.md) FUN_00c0f218

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c0ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0ede0.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0f208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f208.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f3f8",
      "incomplete_value": true,
      "site": "00c0f3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0efd0",
      "incomplete_value": true,
      "site": "00c0efd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0f2dc",
      "incomplete_value": true,
      "site": "00c0f2f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eeb4",
      "incomplete_value": true,
      "site": "00c0eecc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f3d8",
      "incomplete_value": false,
      "site": "00c0f3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0efb0",
      "incomplete_value": false,
      "site": "00c0efb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c0f2d0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f2dc",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f3d8",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0f2d0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f2dc",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f3d8",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0eecc) · [`00c0efb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0efb4) · [`00c0efcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0efcc)
- 新版 `00c0f2f4`（命令位置の公開資料なし） · `00c0f3dc`（命令位置の公開資料なし） · `00c0f3f4`（命令位置の公開資料なし）

~~~diff
- 00c0eecc ["INT_ADD", "register:40f0:8", ["const:c0eecc:8", "const:4:8"]]
- 00c0eecc ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0f2f4 ["INT_ADD", "register:40f0:8", ["const:c0f2f4:8", "const:4:8"]]
+ 00c0f2f4 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0eecc bytes ac030094
+ 00c0f2f4 bytes ac030094
- 00c0efb4 ["INT_ADD", "register:40f0:8", ["const:c0efb4:8", "const:4:8"]]
- 00c0efb4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0f3dc ["INT_ADD", "register:40f0:8", ["const:c0f3dc:8", "const:4:8"]]
+ 00c0f3dc ["CALL", null, ["callee:00c57e50:8"]]
- 00c0efb4 bytes a7220194
+ 00c0f3dc bytes 9d220194
- 00c0efcc ["INT_ADD", "register:40f0:8", ["const:c0efcc:8", "const:4:8"]]
- 00c0efcc ["CALL", null, ["callee:00c5d220:8"]]
+ 00c0f3f4 ["INT_ADD", "register:40f0:8", ["const:c0f3f4:8", "const:4:8"]]
+ 00c0f3f4 ["CALL", null, ["callee:00c5d220:8"]]
- 00c0efcc bytes 95370194
+ 00c0f3f4 bytes 8b370194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba300583fabf4fe36e6bf8b31e4be84"></a>

### [`00c0f020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md) → [`00c0f448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f448.md) FUN_00c0f448

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c0f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f010.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f438.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f628",
      "incomplete_value": true,
      "site": "00c0f628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f200",
      "incomplete_value": true,
      "site": "00c0f200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0f50c",
      "incomplete_value": true,
      "site": "00c0f524",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f0e4",
      "incomplete_value": true,
      "site": "00c0f0fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f608",
      "incomplete_value": false,
      "site": "00c0f60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f1e0",
      "incomplete_value": false,
      "site": "00c0f1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c0f500",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f50c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f608",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0f500",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f50c",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f608",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0f0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md#insn-00c0f0fc) · [`00c0f1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md#insn-00c0f1e4) · [`00c0f1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md#insn-00c0f1fc)
- 新版 `00c0f524`（命令位置の公開資料なし） · `00c0f60c`（命令位置の公開資料なし） · `00c0f624`（命令位置の公開資料なし）

~~~diff
- 00c0f0fc ["INT_ADD", "register:40f0:8", ["const:c0f0fc:8", "const:4:8"]]
- 00c0f0fc ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0f524 ["INT_ADD", "register:40f0:8", ["const:c0f524:8", "const:4:8"]]
+ 00c0f524 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0f0fc bytes 20030094
+ 00c0f524 bytes 20030094
- 00c0f1e4 ["INT_ADD", "register:40f0:8", ["const:c0f1e4:8", "const:4:8"]]
- 00c0f1e4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0f60c ["INT_ADD", "register:40f0:8", ["const:c0f60c:8", "const:4:8"]]
+ 00c0f60c ["CALL", null, ["callee:00c57e50:8"]]
- 00c0f1e4 bytes 1b220194
+ 00c0f60c bytes 11220194
- 00c0f1fc ["INT_ADD", "register:40f0:8", ["const:c0f1fc:8", "const:4:8"]]
- 00c0f1fc ["CALL", null, ["callee:00c5d220:8"]]
+ 00c0f624 ["INT_ADD", "register:40f0:8", ["const:c0f624:8", "const:4:8"]]
+ 00c0f624 ["CALL", null, ["callee:00c5d220:8"]]
- 00c0f1fc bytes 09370194
+ 00c0f624 bytes ff360194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c571cc3879384c15b2102c2fcdbef9e4"></a>

### [`00c0f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) → [`00c0f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f678.md) FUN_00c0f678

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f240.md) · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c0f668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f668.md) · 呼出先 12件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.09% / 新版 91.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f9bc",
      "incomplete_value": false,
      "site": "00c0f9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f594",
      "incomplete_value": false,
      "site": "00c0f594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0f9fc",
      "incomplete_value": false,
      "site": "00c0f9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f5d4",
      "incomplete_value": false,
      "site": "00c0f5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0fa34",
      "incomplete_value": true,
      "site": "00c0fa34",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f60c",
      "incomplete_value": true,
      "site": "00c0f60c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0f778",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f784",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f7c8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0f778",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f784",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f7c8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md#insn-00c0f3c4) · [`00c0f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md#insn-00c0f3fc) · [`00c0f574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md#insn-00c0f574)
- 新版 `00c0f7ec`（命令位置の公開資料なし） · `00c0f824`（命令位置の公開資料なし） · `00c0f99c`（命令位置の公開資料なし）

~~~diff
- 00c0f3c4 ["INT_ADD", "register:40f0:8", ["const:c0f3c4:8", "const:4:8"]]
- 00c0f3c4 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0f7ec ["INT_ADD", "register:40f0:8", ["const:c0f7ec:8", "const:4:8"]]
+ 00c0f7ec ["CALL", null, ["callee:00c101a4:8"]]
- 00c0f3c4 bytes 6e020094
+ 00c0f7ec bytes 6e020094
- 00c0f3fc ["INT_ADD", "register:40f0:8", ["const:c0f3fc:8", "const:4:8"]]
- 00c0f3fc ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c0f824 ["INT_ADD", "register:40f0:8", ["const:c0f824:8", "const:4:8"]]
+ 00c0f824 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c0f3fc bytes 6f300094
+ 00c0f824 bytes 6f300094
- 00c0f574 ["INT_ADD", "register:40f0:8", ["const:c0f574:8", "const:4:8"]]
- 00c0f574 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c0f99c ["INT_ADD", "register:40f0:8", ["const:c0f99c:8", "const:4:8"]]
+ 00c0f99c ["CALL", null, ["callee:00c57e50:8"]]
- 00c0f574 bytes 37210194
+ 00c0f99c bytes 2d210194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8f0d6d149319c7c034bf76a6fa8db9"></a>

### [`00c0f6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md) → [`00c0fb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0fb08.md) FUN_00c0fb08

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0f6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6d0.md) · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c0faf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0faf8.md) · 呼出先 12件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.02% / 新版 91.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0fe44",
      "incomplete_value": false,
      "site": "00c0fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa1c",
      "incomplete_value": false,
      "site": "00c0fa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0fe84",
      "incomplete_value": false,
      "site": "00c0fe84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa5c",
      "incomplete_value": false,
      "site": "00c0fa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0febc",
      "incomplete_value": true,
      "site": "00c0febc",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa94",
      "incomplete_value": true,
      "site": "00c0fa94",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0fc04",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0fc0c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0fc54",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0fc04",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0fc0c",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0fc54",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md#insn-00c0f7f8) · [`00c0f850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md#insn-00c0f850) · [`00c0f888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md#insn-00c0f888)
- 新版 `00c0fc20`（命令位置の公開資料なし） · `00c0fc78`（命令位置の公開資料なし） · `00c0fcb0`（命令位置の公開資料なし）

~~~diff
- 00c0f7f8 ["INT_ADD", "register:40f0:8", ["const:c0f7f8:8", "const:4:8"]]
- 00c0f7f8 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0fc20 ["INT_ADD", "register:40f0:8", ["const:c0fc20:8", "const:4:8"]]
+ 00c0fc20 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0f7f8 bytes 61010094
+ 00c0fc20 bytes 61010094
- 00c0f850 ["INT_ADD", "register:40f0:8", ["const:c0f850:8", "const:4:8"]]
- 00c0f850 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c0fc78 ["INT_ADD", "register:40f0:8", ["const:c0fc78:8", "const:4:8"]]
+ 00c0fc78 ["CALL", null, ["callee:00c101a4:8"]]
- 00c0f850 bytes 4b010094
+ 00c0fc78 bytes 4b010094
- 00c0f888 ["INT_ADD", "register:40f0:8", ["const:c0f888:8", "const:4:8"]]
- 00c0f888 ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c0fcb0 ["INT_ADD", "register:40f0:8", ["const:c0fcb0:8", "const:4:8"]]
+ 00c0fcb0 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c0f888 bytes 4c2f0094
+ 00c0fcb0 bytes 4c2f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95d605a527f487f8fa3db88393f082a6"></a>

### [`00c0fb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md) → [`00c0ff80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0ff80.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPKv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c10074",
      "incomplete_value": true,
      "site": "00c10074",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c0fc4c",
      "incomplete_value": true,
      "site": "00c0fc4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10164",
      "incomplete_value": true,
      "site": "00c10164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fd3c",
      "incomplete_value": true,
      "site": "00c0fd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c1007c",
      "incomplete_value": true,
      "site": "00c10080",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0fc54",
      "incomplete_value": true,
      "site": "00c0fc58",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00c0ffac",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ffc4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ffcc",
      "PARAM",
      [
        "storage",
        "002a621f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c0ffac",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ffc4",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ffcc",
      "PARAM",
      [
        "storage",
        "002a62fb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fc7c) · [`00c0fd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fd20) · [`00c0fd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fd3c)
- 新版 `00c100a4`（命令位置の公開資料なし） · `00c10148`（命令位置の公開資料なし） · `00c10164`（命令位置の公開資料なし）

~~~diff
- 00c0fc7c ["INT_ADD", "register:40f0:8", ["const:c0fc7c:8", "const:4:8"]]
- 00c0fc7c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c100a4 ["INT_ADD", "register:40f0:8", ["const:c100a4:8", "const:4:8"]]
+ 00c100a4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0fc7c bytes 99370194
+ 00c100a4 bytes 8f370194
- 00c0fd20 ["INT_ADD", "register:40f0:8", ["const:c0fd20:8", "const:4:8"]]
- 00c0fd20 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c10148 ["INT_ADD", "register:40f0:8", ["const:c10148:8", "const:4:8"]]
+ 00c10148 ["CALL", null, ["callee:00c57e50:8"]]
- 00c0fd20 bytes 4c1f0194
+ 00c10148 bytes 421f0194
- 00c0fd3c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
- 00c0fd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c10164 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
+ 00c10164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c0fd3c bytes e04e04f9
+ 00c10164 bytes e04e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f4e9ebf07849897b25ed09d2cf4a14"></a>

### [`00c0feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md) → [`00c102d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c102d4.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1033c",
      "incomplete_value": true,
      "site": "00c1033c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c0ff14",
      "incomplete_value": true,
      "site": "00c0ff14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c10344",
      "incomplete_value": true,
      "site": "00c10348",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c0ff1c",
      "incomplete_value": true,
      "site": "00c0ff20",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c10368",
      "incomplete_value": true,
      "site": "00c10370",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c0ff40",
      "incomplete_value": true,
      "site": "00c0ff48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "00c10334",
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1033c",
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c10340",
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c10334",
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1033c",
      "DATA",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c10340",
      "READ",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0ff48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c0ff48) · [`00c0ff04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c0ff04) · [`00c0ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c0ff0c)
- 新版 `00c10370`（命令位置の公開資料なし） · `00c1032c`（命令位置の公開資料なし） · `00c10334`（命令位置の公開資料なし）

~~~diff
- 00c0ff48 ["INT_ADD", "register:40f0:8", ["const:c0ff48:8", "const:4:8"]]
- 00c0ff48 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c10370 ["INT_ADD", "register:40f0:8", ["const:c10370:8", "const:4:8"]]
+ 00c10370 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c0ff48 bytes e6360194
+ 00c10370 bytes dc360194
- 00c0ff04 ["INT_ADD", "register:40f0:8", ["const:c0ff04:8", "const:4:8"]]
- 00c0ff04 ["CALL", null, ["callee:00c58270:8"]]
+ 00c1032c ["INT_ADD", "register:40f0:8", ["const:c1032c:8", "const:4:8"]]
+ 00c1032c ["CALL", null, ["callee:00c58270:8"]]
- 00c0ff04 bytes db1f0194
+ 00c1032c bytes d11f0194
- 00c0ff0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7c8:8"]]
- 00c0ff0c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c10334 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bc8:8"]]
+ 00c10334 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c0ff0c bytes d6e643f9
+ 00c10334 bytes d6e645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d50938efc6840037b50931c33bc0f6"></a>

### [`00c1008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md) → [`00c104b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c104b4.md) FUN_00c104b4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c1007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1007c.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c104a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c104a4.md) · 呼出先 8件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c106b0",
      "incomplete_value": true,
      "site": "00c106b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10288",
      "incomplete_value": true,
      "site": "00c10288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10594",
      "incomplete_value": true,
      "site": "00c105ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1016c",
      "incomplete_value": true,
      "site": "00c10184",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10690",
      "incomplete_value": false,
      "site": "00c10694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10268",
      "incomplete_value": false,
      "site": "00c1026c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c10588",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10594",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10690",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c10588",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10594",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10690",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md#insn-00c10184) · [`00c1026c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md#insn-00c1026c) · [`00c10284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md#insn-00c10284)
- 新版 `00c105ac`（命令位置の公開資料なし） · `00c10694`（命令位置の公開資料なし） · `00c106ac`（命令位置の公開資料なし）

~~~diff
- 00c10184 ["INT_ADD", "register:40f0:8", ["const:c10184:8", "const:4:8"]]
- 00c10184 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c105ac ["INT_ADD", "register:40f0:8", ["const:c105ac:8", "const:4:8"]]
+ 00c105ac ["CALL", null, ["callee:00c101a4:8"]]
- 00c10184 bytes fefeff97
+ 00c105ac bytes fefeff97
- 00c1026c ["INT_ADD", "register:40f0:8", ["const:c1026c:8", "const:4:8"]]
- 00c1026c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c10694 ["INT_ADD", "register:40f0:8", ["const:c10694:8", "const:4:8"]]
+ 00c10694 ["CALL", null, ["callee:00c57e50:8"]]
- 00c1026c bytes f91d0194
+ 00c10694 bytes ef1d0194
- 00c10284 ["INT_ADD", "register:40f0:8", ["const:c10284:8", "const:4:8"]]
- 00c10284 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c106ac ["INT_ADD", "register:40f0:8", ["const:c106ac:8", "const:4:8"]]
+ 00c106ac ["CALL", null, ["callee:00c5d220:8"]]
- 00c10284 bytes e7320194
+ 00c106ac bytes dd320194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e4aebedb9ee5d13c65e897cbd61810"></a>

### [`00c102d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md) → [`00c10700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10700.md) FUN_00c10700

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c102c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102c8.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c106f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c106f0.md) · 呼出先 8件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c108fc",
      "incomplete_value": true,
      "site": "00c108fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c104d4",
      "incomplete_value": true,
      "site": "00c104d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c107e0",
      "incomplete_value": true,
      "site": "00c107f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c103b8",
      "incomplete_value": true,
      "site": "00c103d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c108dc",
      "incomplete_value": false,
      "site": "00c108e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c104b4",
      "incomplete_value": false,
      "site": "00c104b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c107d4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c107e0",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c108dc",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c107d4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c107e0",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c108dc",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c103d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c103d0) · [`00c104b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c104b8) · [`00c104d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c104d0)
- 新版 `00c107f8`（命令位置の公開資料なし） · `00c108e0`（命令位置の公開資料なし） · `00c108f8`（命令位置の公開資料なし）

~~~diff
- 00c103d0 ["INT_ADD", "register:40f0:8", ["const:c103d0:8", "const:4:8"]]
- 00c103d0 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c107f8 ["INT_ADD", "register:40f0:8", ["const:c107f8:8", "const:4:8"]]
+ 00c107f8 ["CALL", null, ["callee:00c101a4:8"]]
- 00c103d0 bytes 6bfeff97
+ 00c107f8 bytes 6bfeff97
- 00c104b8 ["INT_ADD", "register:40f0:8", ["const:c104b8:8", "const:4:8"]]
- 00c104b8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c108e0 ["INT_ADD", "register:40f0:8", ["const:c108e0:8", "const:4:8"]]
+ 00c108e0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c104b8 bytes 661d0194
+ 00c108e0 bytes 5c1d0194
- 00c104d0 ["INT_ADD", "register:40f0:8", ["const:c104d0:8", "const:4:8"]]
- 00c104d0 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c108f8 ["INT_ADD", "register:40f0:8", ["const:c108f8:8", "const:4:8"]]
+ 00c108f8 ["CALL", null, ["callee:00c5d220:8"]]
- 00c104d0 bytes 54320194
+ 00c108f8 bytes 4a320194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5731daadc0930cb08468fefed18305"></a>

### [`00c10524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md) → [`00c1094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c1094c.md) FUN_00c1094c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c10514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10514.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c1093c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c1093c.md) · 呼出先 8件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10b2c",
      "incomplete_value": true,
      "site": "00c10b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10704",
      "incomplete_value": true,
      "site": "00c10704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c10b0c",
      "incomplete_value": false,
      "site": "00c10b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c106e4",
      "incomplete_value": false,
      "site": "00c106e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10b1c",
      "incomplete_value": false,
      "site": "00c10b28",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c106f4",
      "incomplete_value": false,
      "site": "00c10700",
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
            "const:13c:8"
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
      "00c10a04",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10a10",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10b0c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c10a04",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10a10",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10b0c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c106e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c106e8) · [`00c10700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c10700) · [`00c10704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c10704)
- 新版 `00c10b10`（命令位置の公開資料なし） · `00c10b28`（命令位置の公開資料なし） · `00c10b2c`（命令位置の公開資料なし）

~~~diff
- 00c106e8 ["INT_ADD", "register:40f0:8", ["const:c106e8:8", "const:4:8"]]
- 00c106e8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c10b10 ["INT_ADD", "register:40f0:8", ["const:c10b10:8", "const:4:8"]]
+ 00c10b10 ["CALL", null, ["callee:00c57e50:8"]]
- 00c106e8 bytes da1c0194
+ 00c10b10 bytes d01c0194
- 00c10700 ["INT_ADD", "register:40f0:8", ["const:c10700:8", "const:4:8"]]
- 00c10700 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c10b28 ["INT_ADD", "register:40f0:8", ["const:c10b28:8", "const:4:8"]]
+ 00c10b28 ["CALL", null, ["callee:00c5d220:8"]]
- 00c10700 bytes c8310194
+ 00c10b28 bytes be310194
- 00c10704 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
- 00c10704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c10b2c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
+ 00c10b2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c10704 bytes e04e04f9
+ 00c10b2c bytes e04e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-252e07bdf1a092a74d86b2a7a44c3d38"></a>

### [`00c10754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md) → [`00c10b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10b7c.md) FUN_00c10b7c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c10744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10744.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c10b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10b6c.md) · 呼出先 8件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10d5c",
      "incomplete_value": true,
      "site": "00c10d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10934",
      "incomplete_value": true,
      "site": "00c10934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c10c40",
      "incomplete_value": true,
      "site": "00c10c58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10818",
      "incomplete_value": true,
      "site": "00c10830",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10d3c",
      "incomplete_value": false,
      "site": "00c10d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10914",
      "incomplete_value": false,
      "site": "00c10918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "00c10c34",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10c40",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10d3c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c10c34",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10c40",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10d3c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md#insn-00c10830) · [`00c10918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md#insn-00c10918) · [`00c10930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md#insn-00c10930)
- 新版 `00c10c58`（命令位置の公開資料なし） · `00c10d40`（命令位置の公開資料なし） · `00c10d58`（命令位置の公開資料なし）

~~~diff
- 00c10830 ["INT_ADD", "register:40f0:8", ["const:c10830:8", "const:4:8"]]
- 00c10830 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c10c58 ["INT_ADD", "register:40f0:8", ["const:c10c58:8", "const:4:8"]]
+ 00c10c58 ["CALL", null, ["callee:00c101a4:8"]]
- 00c10830 bytes 53fdff97
+ 00c10c58 bytes 53fdff97
- 00c10918 ["INT_ADD", "register:40f0:8", ["const:c10918:8", "const:4:8"]]
- 00c10918 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c10d40 ["INT_ADD", "register:40f0:8", ["const:c10d40:8", "const:4:8"]]
+ 00c10d40 ["CALL", null, ["callee:00c57e50:8"]]
- 00c10918 bytes 4e1c0194
+ 00c10d40 bytes 441c0194
- 00c10930 ["INT_ADD", "register:40f0:8", ["const:c10930:8", "const:4:8"]]
- 00c10930 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c10d58 ["INT_ADD", "register:40f0:8", ["const:c10d58:8", "const:4:8"]]
+ 00c10d58 ["CALL", null, ["callee:00c5d220:8"]]
- 00c10930 bytes 3c310194
+ 00c10d58 bytes 32310194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0468c14dc935024273b160eafbe602"></a>

### [`00c10984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) → [`00c10dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10dac.md) FUN_00c10dac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10974.md) · 呼出先 12件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c10d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10d9c.md) · 呼出先 12件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c110f0",
      "incomplete_value": false,
      "site": "00c110f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10cc8",
      "incomplete_value": false,
      "site": "00c10cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11130",
      "incomplete_value": true,
      "site": "00c11130",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10d08",
      "incomplete_value": true,
      "site": "00c10d08",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11168",
      "incomplete_value": true,
      "site": "00c11168",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10d40",
      "incomplete_value": true,
      "site": "00c10d40",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c10eac",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10eb8",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10efc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c10eac",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10eb8",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10efc",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md#insn-00c10aa0) · [`00c10af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md#insn-00c10af8) · [`00c10b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md#insn-00c10b30)
- 新版 `00c10ec8`（命令位置の公開資料なし） · `00c10f20`（命令位置の公開資料なし） · `00c10f58`（命令位置の公開資料なし）

~~~diff
- 00c10aa0 ["INT_ADD", "register:40f0:8", ["const:c10aa0:8", "const:4:8"]]
- 00c10aa0 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c10ec8 ["INT_ADD", "register:40f0:8", ["const:c10ec8:8", "const:4:8"]]
+ 00c10ec8 ["CALL", null, ["callee:00c101a4:8"]]
- 00c10aa0 bytes b7fcff97
+ 00c10ec8 bytes b7fcff97
- 00c10af8 ["INT_ADD", "register:40f0:8", ["const:c10af8:8", "const:4:8"]]
- 00c10af8 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c10f20 ["INT_ADD", "register:40f0:8", ["const:c10f20:8", "const:4:8"]]
+ 00c10f20 ["CALL", null, ["callee:00c101a4:8"]]
- 00c10af8 bytes a1fcff97
+ 00c10f20 bytes a1fcff97
- 00c10b30 ["INT_ADD", "register:40f0:8", ["const:c10b30:8", "const:4:8"]]
- 00c10b30 ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c10f58 ["INT_ADD", "register:40f0:8", ["const:c10f58:8", "const:4:8"]]
+ 00c10f58 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c10b30 bytes a22a0094
+ 00c10f58 bytes a22a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9238e8959521c5b583ef4b42b3febe"></a>

### [`00c10e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md) → [`00c1123c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1123c.md) FUN_00c1123c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e04.md) · 呼出先 12件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c1122c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1122c.md) · 呼出先 12件 [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11578",
      "incomplete_value": false,
      "site": "00c11578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11150",
      "incomplete_value": false,
      "site": "00c11150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c115b8",
      "incomplete_value": false,
      "site": "00c115b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11190",
      "incomplete_value": false,
      "site": "00c11190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c115f0",
      "incomplete_value": true,
      "site": "00c115f0",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c111c8",
      "incomplete_value": true,
      "site": "00c111c8",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c11338",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11340",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11388",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11338",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11340",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11388",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md#insn-00c10f2c) · [`00c10fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md#insn-00c10fbc) · [`00c10fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md#insn-00c10fe8)
- 新版 `00c11354`（命令位置の公開資料なし） · `00c113e4`（命令位置の公開資料なし） · `00c11410`（命令位置の公開資料なし）

~~~diff
- 00c10f2c ["INT_ADD", "register:40f0:8", ["const:c10f2c:8", "const:4:8"]]
- 00c10f2c ["CALL", null, ["callee:00c101a4:8"]]
+ 00c11354 ["INT_ADD", "register:40f0:8", ["const:c11354:8", "const:4:8"]]
+ 00c11354 ["CALL", null, ["callee:00c101a4:8"]]
- 00c10f2c bytes 94fbff97
+ 00c11354 bytes 94fbff97
- 00c10fbc ["INT_ADD", "register:40f0:8", ["const:c10fbc:8", "const:4:8"]]
- 00c10fbc ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c113e4 ["INT_ADD", "register:40f0:8", ["const:c113e4:8", "const:4:8"]]
+ 00c113e4 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c10fbc bytes 7f290094
+ 00c113e4 bytes 7f290094
- 00c10fe8 ["INT_ADD", "register:40f0:8", ["const:c10fe8:8", "const:4:8"]]
- 00c10fe8 ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c11410 ["INT_ADD", "register:40f0:8", ["const:c11410:8", "const:4:8"]]
+ 00c11410 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c10fe8 bytes 74290094
+ 00c11410 bytes 74290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb177eb75e2bd082ff88af1db897012b"></a>

### [`00c1128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md) → [`00c116b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c116b4.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPKv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c101a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c118a4",
      "incomplete_value": true,
      "site": "00c118a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1147c",
      "incomplete_value": true,
      "site": "00c1147c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c116fc",
      "incomplete_value": true,
      "site": "00c11718",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c112d4",
      "incomplete_value": true,
      "site": "00c112f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c11704",
      "incomplete_value": false,
      "site": "00c11718",
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
            "const:2fb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c112dc",
      "incomplete_value": false,
      "site": "00c112f0",
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
            "const:21f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c116e4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c116fc",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11704",
      "PARAM",
      [
        "storage",
        "002a621f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c116e4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c116fc",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11704",
      "PARAM",
      [
        "storage",
        "002a62fb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c112f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md#insn-00c112f0) · [`00c113b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md#insn-00c113b8) · [`00c11478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md#insn-00c11478)
- 新版 `00c11718`（命令位置の公開資料なし） · `00c117e0`（命令位置の公開資料なし） · `00c118a0`（命令位置の公開資料なし）

~~~diff
- 00c112f0 ["INT_ADD", "register:40f0:8", ["const:c112f0:8", "const:4:8"]]
- 00c112f0 ["CALL", null, ["callee:00c101a4:8"]]
+ 00c11718 ["INT_ADD", "register:40f0:8", ["const:c11718:8", "const:4:8"]]
+ 00c11718 ["CALL", null, ["callee:00c101a4:8"]]
- 00c112f0 bytes a3faff97
+ 00c11718 bytes a3faff97
- 00c113b8 ["INT_ADD", "register:40f0:8", ["const:c113b8:8", "const:4:8"]]
- 00c113b8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c117e0 ["INT_ADD", "register:40f0:8", ["const:c117e0:8", "const:4:8"]]
+ 00c117e0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c113b8 bytes ca310194
+ 00c117e0 bytes c0310194
- 00c11478 ["INT_ADD", "register:40f0:8", ["const:c11478:8", "const:4:8"]]
- 00c11478 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c118a0 ["INT_ADD", "register:40f0:8", ["const:c118a0:8", "const:4:8"]]
+ 00c118a0 ["CALL", null, ["callee:00c5d220:8"]]
- 00c11478 bytes 6a2e0194
+ 00c118a0 bytes 602e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a7b74208d3a63517df2b3a27116d042"></a>

### [`00c116bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md) → [`00c11ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c11ae4.md) _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1d0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5d0.md) · 呼出先 4件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11b2c",
      "incomplete_value": true,
      "site": "00c11b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c11704",
      "incomplete_value": true,
      "site": "00c11704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11b94",
      "incomplete_value": true,
      "site": "00c11b94",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1176c",
      "incomplete_value": true,
      "site": "00c1176c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c11b38",
      "incomplete_value": true,
      "site": "00c11b3c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c11710",
      "incomplete_value": true,
      "site": "00c11714",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c11b14",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c11b2c",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11b34",
      "READ",
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
      "00c11b14",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c11b2c",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11b34",
      "READ",
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

- 旧版 [`00c1173c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md#insn-00c1173c) · [`00c117a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md#insn-00c117a0) · [`00c116ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md#insn-00c116ec)
- 新版 `00c11b64`（命令位置の公開資料なし） · `00c11bc8`（命令位置の公開資料なし） · `00c11b14`（命令位置の公開資料なし）

~~~diff
- 00c1173c ["INT_ADD", "register:40f0:8", ["const:c1173c:8", "const:4:8"]]
- 00c1173c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c11b64 ["INT_ADD", "register:40f0:8", ["const:c11b64:8", "const:4:8"]]
+ 00c11b64 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1173c bytes e9300194
+ 00c11b64 bytes df300194
- 00c117a0 ["INT_ADD", "register:40f0:8", ["const:c117a0:8", "const:4:8"]]
- 00c117a0 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c11bc8 ["INT_ADD", "register:40f0:8", ["const:c11bc8:8", "const:4:8"]]
+ 00c11bc8 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c117a0 bytes d0300194
+ 00c11bc8 bytes c6300194
- 00c116ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:830:8"]]
- 00c116ec ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c11b14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c30:8"]]
+ 00c11b14 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c116ec bytes b51a44f9
+ 00c11b14 bytes b51a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea99589807acd19c3fb1e2a19408a89"></a>

### [`00c11ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md) → [`00c11ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c11ed8.md) _ZNSt6__ndk19__num_putIcE23__widen_and_group_floatEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1e0.md) · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5e5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5e0.md) · 呼出先 7件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11f20",
      "incomplete_value": true,
      "site": "00c11f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c11af8",
      "incomplete_value": true,
      "site": "00c11af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11f88",
      "incomplete_value": true,
      "site": "00c11f88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11b60",
      "incomplete_value": true,
      "site": "00c11b60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1212c",
      "incomplete_value": true,
      "site": "00c1212c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11d04",
      "incomplete_value": true,
      "site": "00c11d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c11f08",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c11f20",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11f28",
      "READ",
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
      "00c11f08",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c11f20",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11f28",
      "READ",
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

- 旧版 [`00c11b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md#insn-00c11b30) · [`00c11b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md#insn-00c11b94) · [`00c11d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md#insn-00c11d04)
- 新版 `00c11f58`（命令位置の公開資料なし） · `00c11fbc`（命令位置の公開資料なし） · `00c1212c`（命令位置の公開資料なし）

~~~diff
- 00c11b30 ["INT_ADD", "register:40f0:8", ["const:c11b30:8", "const:4:8"]]
- 00c11b30 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c11f58 ["INT_ADD", "register:40f0:8", ["const:c11f58:8", "const:4:8"]]
+ 00c11f58 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c11b30 bytes ec2f0194
+ 00c11f58 bytes e22f0194
- 00c11b94 ["INT_ADD", "register:40f0:8", ["const:c11b94:8", "const:4:8"]]
- 00c11b94 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c11fbc ["INT_ADD", "register:40f0:8", ["const:c11fbc:8", "const:4:8"]]
+ 00c11fbc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c11b94 bytes d32f0194
+ 00c11fbc bytes c92f0194
- 00c11d04 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
- 00c11d04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c1212c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
+ 00c1212c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c11d04 bytes e04e04f9
+ 00c1212c bytes e04e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16cbc1e4e491c5e05e394cea4ad00ccd"></a>

### [`00c120a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md) → [`00c124d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c12/00c124d0.md) _ZNSt6__ndk19__num_putIwE21__widen_and_group_intEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1f0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5f0.md) · 呼出先 4件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12518",
      "incomplete_value": true,
      "site": "00c12518",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c120f0",
      "incomplete_value": true,
      "site": "00c120f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c12580",
      "incomplete_value": true,
      "site": "00c12580",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c12158",
      "incomplete_value": true,
      "site": "00c12158",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c12524",
      "incomplete_value": true,
      "site": "00c12528",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c120fc",
      "incomplete_value": true,
      "site": "00c12100",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c12500",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c12518",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12520",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c12500",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c12518",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12520",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c12128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md#insn-00c12128) · [`00c1218c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md#insn-00c1218c) · [`00c120d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md#insn-00c120d8)
- 新版 `00c12550`（命令位置の公開資料なし） · `00c125b4`（命令位置の公開資料なし） · `00c12500`（命令位置の公開資料なし）

~~~diff
- 00c12128 ["INT_ADD", "register:40f0:8", ["const:c12128:8", "const:4:8"]]
- 00c12128 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c12550 ["INT_ADD", "register:40f0:8", ["const:c12550:8", "const:4:8"]]
+ 00c12550 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c12128 bytes 6e2e0194
+ 00c12550 bytes 642e0194
- 00c1218c ["INT_ADD", "register:40f0:8", ["const:c1218c:8", "const:4:8"]]
- 00c1218c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c125b4 ["INT_ADD", "register:40f0:8", ["const:c125b4:8", "const:4:8"]]
+ 00c125b4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1218c bytes 552e0194
+ 00c125b4 bytes 4b2e0194
- 00c120d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:740:8"]]
- 00c120d8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c12500 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b40:8"]]
+ 00c12500 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c120d8 bytes d6a243f9
+ 00c12500 bytes d6a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3095d545f0229260e9a4200f0065c724"></a>

### [`00c124a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md) → [`00c128cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c12/00c128cc.md) _ZNSt6__ndk19__num_putIwE23__widen_and_group_floatEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e200.md) · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5e600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e600.md) · 呼出先 7件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.71% / 新版 96.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12914",
      "incomplete_value": true,
      "site": "00c12914",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c124ec",
      "incomplete_value": true,
      "site": "00c124ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c12b18",
      "incomplete_value": true,
      "site": "00c12b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c126f0",
      "incomplete_value": true,
      "site": "00c126f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12b98",
      "incomplete_value": false,
      "site": "00c12b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c12770",
      "incomplete_value": false,
      "site": "00c12770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c128fc",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c12914",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1291c",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c128fc",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c12914",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1291c",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c12588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md#insn-00c12588) · [`00c126f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md#insn-00c126f0) · [`00c12770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md#insn-00c12770)
- 新版 `00c129b0`（命令位置の公開資料なし） · `00c12b18`（命令位置の公開資料なし） · `00c12b98`（命令位置の公開資料なし）

~~~diff
- 00c12588 ["INT_ADD", "register:40f0:8", ["const:c12588:8", "const:4:8"]]
- 00c12588 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c129b0 ["INT_ADD", "register:40f0:8", ["const:c129b0:8", "const:4:8"]]
+ 00c129b0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c12588 bytes 562d0194
+ 00c129b0 bytes 4c2d0194
- 00c126f0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
- 00c126f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c12b18 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
+ 00c12b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c126f0 bytes e04e04f9
+ 00c12b18 bytes e04e06f9
- 00c12770 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c12770 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c12b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c12b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c12770 bytes 004d04f9
+ 00c12b98 bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb3f15f52b46124ce20e517dceb936c"></a>

### [`00c13050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md) → [`00c13478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13478.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c134b8",
      "incomplete_value": true,
      "site": "00c134c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c13090",
      "incomplete_value": true,
      "site": "00c13098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c134c8",
      "incomplete_value": true,
      "site": "00c134cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c130a0",
      "incomplete_value": true,
      "site": "00c130a4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c134e8",
      "incomplete_value": true,
      "site": "00c134f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c130c0",
      "incomplete_value": true,
      "site": "00c130c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c134b8",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c134c0",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c134c4",
      "READ",
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
      "00c134b8",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c134c0",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c134c4",
      "READ",
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

- 旧版 [`00c130c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md#insn-00c130c8) · [`00c13088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md#insn-00c13088) · [`00c13090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md#insn-00c13090)
- 新版 `00c134f0`（命令位置の公開資料なし） · `00c134b0`（命令位置の公開資料なし） · `00c134b8`（命令位置の公開資料なし）

~~~diff
- 00c130c8 ["INT_ADD", "register:40f0:8", ["const:c130c8:8", "const:4:8"]]
- 00c130c8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c134f0 ["INT_ADD", "register:40f0:8", ["const:c134f0:8", "const:4:8"]]
+ 00c134f0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c130c8 bytes 862a0194
+ 00c134f0 bytes 7c2a0194
- 00c13088 ["INT_ADD", "register:40f0:8", ["const:c13088:8", "const:4:8"]]
- 00c13088 ["CALL", null, ["callee:00c58270:8"]]
+ 00c134b0 ["INT_ADD", "register:40f0:8", ["const:c134b0:8", "const:4:8"]]
+ 00c134b0 ["CALL", null, ["callee:00c58270:8"]]
- 00c13088 bytes 7a130194
+ 00c134b0 bytes 70130194
- 00c13090 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
- 00c13090 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c134b8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
+ 00c134b8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c13090 bytes 181b44f9
+ 00c134b8 bytes 181b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3115232f6514e3e13e833013ee3161a2"></a>

### [`00c13264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md) → [`00c1368c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c1368c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c136cc",
      "incomplete_value": true,
      "site": "00c136d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c132a4",
      "incomplete_value": true,
      "site": "00c132ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c136dc",
      "incomplete_value": true,
      "site": "00c136e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c132b4",
      "incomplete_value": true,
      "site": "00c132b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c136fc",
      "incomplete_value": true,
      "site": "00c13704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c132d4",
      "incomplete_value": true,
      "site": "00c132dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c136cc",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c136d4",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c136d8",
      "READ",
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
      "00c136cc",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c136d4",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c136d8",
      "READ",
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

- 旧版 [`00c132dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md#insn-00c132dc) · [`00c1329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md#insn-00c1329c) · [`00c132a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md#insn-00c132a4)
- 新版 `00c13704`（命令位置の公開資料なし） · `00c136c4`（命令位置の公開資料なし） · `00c136cc`（命令位置の公開資料なし）

~~~diff
- 00c132dc ["INT_ADD", "register:40f0:8", ["const:c132dc:8", "const:4:8"]]
- 00c132dc ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c13704 ["INT_ADD", "register:40f0:8", ["const:c13704:8", "const:4:8"]]
+ 00c13704 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c132dc bytes 012a0194
+ 00c13704 bytes f7290194
- 00c1329c ["INT_ADD", "register:40f0:8", ["const:c1329c:8", "const:4:8"]]
- 00c1329c ["CALL", null, ["callee:00c58270:8"]]
+ 00c136c4 ["INT_ADD", "register:40f0:8", ["const:c136c4:8", "const:4:8"]]
+ 00c136c4 ["CALL", null, ["callee:00c58270:8"]]
- 00c1329c bytes f5120194
+ 00c136c4 bytes eb120194
- 00c132a4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
- 00c132a4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c136cc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
+ 00c136cc ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c132a4 bytes 181b44f9
+ 00c136cc bytes 181b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49c5ad0dfe9c29bdba0c61289d3f0d0f"></a>

### [`00c13468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md) → [`00c13890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13890.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c138cc",
      "incomplete_value": true,
      "site": "00c138d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c134a4",
      "incomplete_value": true,
      "site": "00c134ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c13900",
      "incomplete_value": true,
      "site": "00c13908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c134d8",
      "incomplete_value": true,
      "site": "00c134e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c138fc",
      "incomplete_value": false,
      "site": "00c13908",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c134d4",
      "incomplete_value": false,
      "site": "00c134e0",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      "00c138cc",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c138d4",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c138d8",
      "READ",
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
      "00c138cc",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c138d4",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c138d8",
      "READ",
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

- 旧版 [`00c134e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md#insn-00c134e0) · [`00c1349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md#insn-00c1349c) · [`00c134a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md#insn-00c134a4)
- 新版 `00c13908`（命令位置の公開資料なし） · `00c138c4`（命令位置の公開資料なし） · `00c138cc`（命令位置の公開資料なし）

~~~diff
- 00c134e0 ["INT_ADD", "register:40f0:8", ["const:c134e0:8", "const:4:8"]]
- 00c134e0 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c13908 ["INT_ADD", "register:40f0:8", ["const:c13908:8", "const:4:8"]]
+ 00c13908 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c134e0 bytes 80290194
+ 00c13908 bytes 76290194
- 00c1349c ["INT_ADD", "register:40f0:8", ["const:c1349c:8", "const:4:8"]]
- 00c1349c ["CALL", null, ["callee:00c58270:8"]]
+ 00c138c4 ["INT_ADD", "register:40f0:8", ["const:c138c4:8", "const:4:8"]]
+ 00c138c4 ["CALL", null, ["callee:00c58270:8"]]
- 00c1349c bytes 75120194
+ 00c138c4 bytes 6b120194
- 00c134a4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
- 00c134a4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c138cc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
+ 00c138cc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c134a4 bytes f71a44f9
+ 00c138cc bytes f71a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd7c8765c1b7025624107d3e7e7cd92"></a>

### [`00c135ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md) → [`00c13a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13a14.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c148ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.57% / 新版 97.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c13a6c",
      "incomplete_value": true,
      "site": "00c13a6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
      "definition_site": "00c13644",
      "incomplete_value": true,
      "site": "00c13644",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c13c60",
      "incomplete_value": true,
      "site": "00c13c74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:ebf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13838",
      "incomplete_value": true,
      "site": "00c1384c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:e7f:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c13a74",
      "incomplete_value": true,
      "site": "00c13a78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1364c",
      "incomplete_value": true,
      "site": "00c13650",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c13a64",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c13a6c",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c13a70",
      "READ",
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
      "00c13a64",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c13a6c",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c13a70",
      "READ",
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

- 旧版 [`00c13678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md#insn-00c13678) · [`00c13634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md#insn-00c13634) · [`00c1363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md#insn-00c1363c)
- 新版 `00c13aa0`（命令位置の公開資料なし） · `00c13a5c`（命令位置の公開資料なし） · `00c13a64`（命令位置の公開資料なし）

~~~diff
- 00c13678 ["INT_ADD", "register:40f0:8", ["const:c13678:8", "const:4:8"]]
- 00c13678 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c13aa0 ["INT_ADD", "register:40f0:8", ["const:c13aa0:8", "const:4:8"]]
+ 00c13aa0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c13678 bytes 1a290194
+ 00c13aa0 bytes 10290194
- 00c13634 ["INT_ADD", "register:40f0:8", ["const:c13634:8", "const:4:8"]]
- 00c13634 ["CALL", null, ["callee:00c58270:8"]]
+ 00c13a5c ["INT_ADD", "register:40f0:8", ["const:c13a5c:8", "const:4:8"]]
+ 00c13a5c ["CALL", null, ["callee:00c58270:8"]]
- 00c13634 bytes 0f120194
+ 00c13a5c bytes 05120194
- 00c1363c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:830:8"]]
- 00c1363c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c13a64 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c30:8"]]
+ 00c13a64 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1363c bytes 5a1b44f9
+ 00c13a64 bytes 5a1b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-511574f1ce38bdf01a511bcb3a65e58d"></a>

### [`00c147c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md) → [`00c14bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14bf0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKwSC_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e630.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.68% / 新版 99.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c14c78",
      "incomplete_value": true,
      "site": "00c14c80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14850",
      "incomplete_value": true,
      "site": "00c14858",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c14c74",
      "incomplete_value": false,
      "site": "00c14c80",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c1484c",
      "incomplete_value": false,
      "site": "00c14858",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      "00c14c44",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c14c4c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14c50",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c14c44",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c14c4c",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14c50",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c14858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md#insn-00c14858) · [`00c14814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md#insn-00c14814) · [`00c1481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md#insn-00c1481c)
- 新版 `00c14c80`（命令位置の公開資料なし） · `00c14c3c`（命令位置の公開資料なし） · `00c14c44`（命令位置の公開資料なし）

~~~diff
- 00c14858 ["INT_ADD", "register:40f0:8", ["const:c14858:8", "const:4:8"]]
- 00c14858 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c14c80 ["INT_ADD", "register:40f0:8", ["const:c14c80:8", "const:4:8"]]
+ 00c14c80 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c14858 bytes a2240194
+ 00c14c80 bytes 98240194
- 00c14814 ["INT_ADD", "register:40f0:8", ["const:c14814:8", "const:4:8"]]
- 00c14814 ["CALL", null, ["callee:00c58270:8"]]
+ 00c14c3c ["INT_ADD", "register:40f0:8", ["const:c14c3c:8", "const:4:8"]]
+ 00c14c3c ["CALL", null, ["callee:00c58270:8"]]
- 00c14814 bytes 970d0194
+ 00c14c3c bytes 8d0d0194
- 00c1481c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:740:8"]]
- 00c1481c ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c14c44 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:b40:8"]]
+ 00c14c44 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1481c bytes 9ca343f9
+ 00c14c44 bytes 9ca345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42344520152435310bfd5f565c0db417"></a>

### [`00c14cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md) → [`00c150f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c150f0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e630.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1510c",
      "incomplete_value": true,
      "site": "00c15118",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2e1000:8"
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
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2e1000:8"
              ],
              [
                "leaf",
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1510c",
      "incomplete_value": true,
      "site": "00c15118",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
      "value": [
        "LOAD",
        "16",
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
      "00c1510c",
      "READ",
      [
        "storage",
        "002e1938",
        null,
        null
      ]
    ],
    [
      "00c1510c",
      "READ",
      [
        "storage",
        "002e1948",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1510c",
      "READ",
      [
        "storage",
        "002e1978",
        null,
        null
      ]
    ],
    [
      "00c1510c",
      "READ",
      [
        "storage",
        "002e1988",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c14cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md#insn-00c14cdc) · [`00c14cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md#insn-00c14cf4)
- 新版 `00c15104`（命令位置の公開資料なし） · `00c1511c`（命令位置の公開資料なし）

~~~diff
- 00c14cdc ["COPY", "tmp:0:8", ["const:938:8"]]
- 00c14cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c14cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c14cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c15104 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00c15104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c15104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c15104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c14cdc bytes 08e12491
+ 00c15104 bytes 08e12591
- 00c14cf4 ["INT_ADD", "register:40f0:8", ["const:c14cf4:8", "const:4:8"]]
- 00c14cf4 ["CALL", null, ["callee:00c5e630:8"]]
+ 00c1511c ["INT_ADD", "register:40f0:8", ["const:c1511c:8", "const:4:8"]]
+ 00c1511c ["CALL", null, ["callee:00c5e630:8"]]
- 00c14cf4 bytes 4f250194
+ 00c1511c bytes 45250194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06287fe0bb49cf2c86ffe0657e8a60d4"></a>

### [`00c14d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md) → [`00c151c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c151c0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15200",
      "incomplete_value": true,
      "site": "00c15208",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14dd8",
      "incomplete_value": true,
      "site": "00c14de0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15210",
      "incomplete_value": true,
      "site": "00c15214",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c14de8",
      "incomplete_value": true,
      "site": "00c14dec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c15230",
      "incomplete_value": true,
      "site": "00c15238",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14e08",
      "incomplete_value": true,
      "site": "00c14e10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
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
      "00c15200",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c15208",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1520c",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c15200",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c15208",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1520c",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c14e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md#insn-00c14e10) · [`00c14dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md#insn-00c14dd0) · [`00c14dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md#insn-00c14dd8)
- 新版 `00c15238`（命令位置の公開資料なし） · `00c151f8`（命令位置の公開資料なし） · `00c15200`（命令位置の公開資料なし）

~~~diff
- 00c14e10 ["INT_ADD", "register:40f0:8", ["const:c14e10:8", "const:4:8"]]
- 00c14e10 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c15238 ["INT_ADD", "register:40f0:8", ["const:c15238:8", "const:4:8"]]
+ 00c15238 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c14e10 bytes 34230194
+ 00c15238 bytes 2a230194
- 00c14dd0 ["INT_ADD", "register:40f0:8", ["const:c14dd0:8", "const:4:8"]]
- 00c14dd0 ["CALL", null, ["callee:00c58270:8"]]
+ 00c151f8 ["INT_ADD", "register:40f0:8", ["const:c151f8:8", "const:4:8"]]
+ 00c151f8 ["CALL", null, ["callee:00c58270:8"]]
- 00c14dd0 bytes 280c0194
+ 00c151f8 bytes 1e0c0194
- 00c14dd8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
- 00c14dd8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c15200 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
+ 00c15200 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c14dd8 bytes 18a343f9
+ 00c15200 bytes 18a345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822fca58f5750329772eeb321fae2ccd"></a>

### [`00c14fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md) → [`00c153d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c153d4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15414",
      "incomplete_value": true,
      "site": "00c1541c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14fec",
      "incomplete_value": true,
      "site": "00c14ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15424",
      "incomplete_value": true,
      "site": "00c15428",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c14ffc",
      "incomplete_value": true,
      "site": "00c15000",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c15444",
      "incomplete_value": true,
      "site": "00c1544c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1501c",
      "incomplete_value": true,
      "site": "00c15024",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
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
      "00c15414",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1541c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15420",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c15414",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1541c",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15420",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c15024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md#insn-00c15024) · [`00c14fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md#insn-00c14fe4) · [`00c14fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md#insn-00c14fec)
- 新版 `00c1544c`（命令位置の公開資料なし） · `00c1540c`（命令位置の公開資料なし） · `00c15414`（命令位置の公開資料なし）

~~~diff
- 00c15024 ["INT_ADD", "register:40f0:8", ["const:c15024:8", "const:4:8"]]
- 00c15024 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1544c ["INT_ADD", "register:40f0:8", ["const:c1544c:8", "const:4:8"]]
+ 00c1544c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c15024 bytes af220194
+ 00c1544c bytes a5220194
- 00c14fe4 ["INT_ADD", "register:40f0:8", ["const:c14fe4:8", "const:4:8"]]
- 00c14fe4 ["CALL", null, ["callee:00c58270:8"]]
+ 00c1540c ["INT_ADD", "register:40f0:8", ["const:c1540c:8", "const:4:8"]]
+ 00c1540c ["CALL", null, ["callee:00c58270:8"]]
- 00c14fe4 bytes a30b0194
+ 00c1540c bytes 990b0194
- 00c14fec ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
- 00c14fec ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c15414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
+ 00c15414 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c14fec bytes 18a343f9
+ 00c15414 bytes 18a345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebcea6b59ce42b46f03bf5bb0f5dd1f9"></a>

### [`00c151b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md) → [`00c155d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c155d8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15614",
      "incomplete_value": true,
      "site": "00c1561c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c151ec",
      "incomplete_value": true,
      "site": "00c151f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15624",
      "incomplete_value": true,
      "site": "00c15628",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c151fc",
      "incomplete_value": true,
      "site": "00c15200",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c15648",
      "incomplete_value": true,
      "site": "00c15650",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c15220",
      "incomplete_value": true,
      "site": "00c15228",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
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
      "00c15614",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1561c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15620",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c15614",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1561c",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15620",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c15228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md#insn-00c15228) · [`00c151e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md#insn-00c151e4) · [`00c151ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md#insn-00c151ec)
- 新版 `00c15650`（命令位置の公開資料なし） · `00c1560c`（命令位置の公開資料なし） · `00c15614`（命令位置の公開資料なし）

~~~diff
- 00c15228 ["INT_ADD", "register:40f0:8", ["const:c15228:8", "const:4:8"]]
- 00c15228 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c15650 ["INT_ADD", "register:40f0:8", ["const:c15650:8", "const:4:8"]]
+ 00c15650 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c15228 bytes 2e220194
+ 00c15650 bytes 24220194
- 00c151e4 ["INT_ADD", "register:40f0:8", ["const:c151e4:8", "const:4:8"]]
- 00c151e4 ["CALL", null, ["callee:00c58270:8"]]
+ 00c1560c ["INT_ADD", "register:40f0:8", ["const:c1560c:8", "const:4:8"]]
+ 00c1560c ["CALL", null, ["callee:00c58270:8"]]
- 00c151e4 bytes 230b0194
+ 00c1560c bytes 190b0194
- 00c151ec ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:740:8"]]
- 00c151ec ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c15614 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b40:8"]]
+ 00c15614 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c151ec bytes f7a243f9
+ 00c15614 bytes f7a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2088cfc82a1fbf70c2e18b9f416a137e"></a>

### [`00c15334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md) → [`00c1575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c1575c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c165f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c157b4",
      "incomplete_value": true,
      "site": "00c157b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1538c",
      "incomplete_value": true,
      "site": "00c1538c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
      "definition_site": "00c159a4",
      "incomplete_value": true,
      "site": "00c159b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:ecc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1557c",
      "incomplete_value": true,
      "site": "00c15590",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:e8c:8"
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
      "definition_site": "00c159a4",
      "incomplete_value": true,
      "site": "00c159b8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c1557c",
      "incomplete_value": true,
      "site": "00c15590",
      "value": [
        "LOAD",
        "16",
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
      "00c157ac",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c157b4",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c157b8",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c157ac",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c157b4",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c157b8",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md#insn-00c153c0) · [`00c1537c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md#insn-00c1537c) · [`00c15384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md#insn-00c15384)
- 新版 `00c157e8`（命令位置の公開資料なし） · `00c157a4`（命令位置の公開資料なし） · `00c157ac`（命令位置の公開資料なし）

~~~diff
- 00c153c0 ["INT_ADD", "register:40f0:8", ["const:c153c0:8", "const:4:8"]]
- 00c153c0 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c157e8 ["INT_ADD", "register:40f0:8", ["const:c157e8:8", "const:4:8"]]
+ 00c157e8 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c153c0 bytes c8210194
+ 00c157e8 bytes be210194
- 00c1537c ["INT_ADD", "register:40f0:8", ["const:c1537c:8", "const:4:8"]]
- 00c1537c ["CALL", null, ["callee:00c58270:8"]]
+ 00c157a4 ["INT_ADD", "register:40f0:8", ["const:c157a4:8", "const:4:8"]]
+ 00c157a4 ["CALL", null, ["callee:00c58270:8"]]
- 00c1537c bytes bd0a0194
+ 00c157a4 bytes b30a0194
- 00c15384 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:740:8"]]
- 00c15384 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c157ac ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:b40:8"]]
+ 00c157ac ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c15384 bytes 5aa343f9
+ 00c157ac bytes 5aa345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb4b973eb02f1dc6fc8c869fdd38e92"></a>

### [`00c16524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md) → [`00c1694c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c1694c.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE3putES4_RNS_8ios_baseEcPK2tmPKcSC_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a380.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a780.md) · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.39% / 新版 99.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1699c",
      "incomplete_value": true,
      "site": "00c169a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c16574",
      "incomplete_value": true,
      "site": "00c1657c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c169ac",
      "incomplete_value": true,
      "site": "00c169b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c16584",
      "incomplete_value": true,
      "site": "00c16588",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c169cc",
      "incomplete_value": true,
      "site": "00c169d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c165a4",
      "incomplete_value": true,
      "site": "00c165ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c1699c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c169a4",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c169a8",
      "READ",
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
      "00c1699c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c169a4",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c169a8",
      "READ",
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

- 旧版 [`00c165ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md#insn-00c165ac) · [`00c1656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md#insn-00c1656c) · [`00c16574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md#insn-00c16574)
- 新版 `00c169d4`（命令位置の公開資料なし） · `00c16994`（命令位置の公開資料なし） · `00c1699c`（命令位置の公開資料なし）

~~~diff
- 00c165ac ["INT_ADD", "register:40f0:8", ["const:c165ac:8", "const:4:8"]]
- 00c165ac ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c169d4 ["INT_ADD", "register:40f0:8", ["const:c169d4:8", "const:4:8"]]
+ 00c169d4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c165ac bytes 4d1d0194
+ 00c169d4 bytes 431d0194
- 00c1656c ["INT_ADD", "register:40f0:8", ["const:c1656c:8", "const:4:8"]]
- 00c1656c ["CALL", null, ["callee:00c58270:8"]]
+ 00c16994 ["INT_ADD", "register:40f0:8", ["const:c16994:8", "const:4:8"]]
+ 00c16994 ["CALL", null, ["callee:00c58270:8"]]
- 00c1656c bytes 41060194
+ 00c16994 bytes 37060194
- 00c16574 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:830:8"]]
- 00c16574 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1699c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c30:8"]]
+ 00c1699c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c16574 bytes 7b1b44f9
+ 00c1699c bytes 7b1b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f4143b22a63713e2064220f1572813"></a>

### [`00c16904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md) → [`00c16d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16d2c.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE3putES4_RNS_8ios_baseEwPK2tmPKwSC_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16d7c",
      "incomplete_value": true,
      "site": "00c16d84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16954",
      "incomplete_value": true,
      "site": "00c1695c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c16d8c",
      "incomplete_value": true,
      "site": "00c16d90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c16964",
      "incomplete_value": true,
      "site": "00c16968",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c16dac",
      "incomplete_value": true,
      "site": "00c16db4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16984",
      "incomplete_value": true,
      "site": "00c1698c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
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
      "00c16d7c",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c16d84",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c16d88",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c16d7c",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c16d84",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c16d88",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md#insn-00c1698c) · [`00c1694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md#insn-00c1694c) · [`00c16954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md#insn-00c16954)
- 新版 `00c16db4`（命令位置の公開資料なし） · `00c16d74`（命令位置の公開資料なし） · `00c16d7c`（命令位置の公開資料なし）

~~~diff
- 00c1698c ["INT_ADD", "register:40f0:8", ["const:c1698c:8", "const:4:8"]]
- 00c1698c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c16db4 ["INT_ADD", "register:40f0:8", ["const:c16db4:8", "const:4:8"]]
+ 00c16db4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1698c bytes 551c0194
+ 00c16db4 bytes 4b1c0194
- 00c1694c ["INT_ADD", "register:40f0:8", ["const:c1694c:8", "const:4:8"]]
- 00c1694c ["CALL", null, ["callee:00c58270:8"]]
+ 00c16d74 ["INT_ADD", "register:40f0:8", ["const:c16d74:8", "const:4:8"]]
+ 00c16d74 ["CALL", null, ["callee:00c58270:8"]]
- 00c1694c bytes 49050194
+ 00c16d74 bytes 3f050194
- 00c16954 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:740:8"]]
- 00c16954 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c16d7c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:b40:8"]]
+ 00c16d7c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c16954 bytes 7ba343f9
+ 00c16d7c bytes 7ba345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

