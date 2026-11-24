# v16.0.0 → v16.0.1 · 最優先の変更候補 (38)

[一覧の目次](README.md)

<a id="compare-b01604d2f48fa6619971fba40c6c3825"></a>

### [`0079b38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b38c.md) → [`0079b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md) FUN_0079b3cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md) · 呼出先 14件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md) [`00795e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795e1c.md)
- 新版 呼出元 1件 [`0079b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b280.md) · 呼出先 14件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b428",
      "incomplete_value": false,
      "site": "0079b42c",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:820:8"
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
      "definition_site": "0079b3e8",
      "incomplete_value": false,
      "site": "0079b3ec",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b458",
      "incomplete_value": false,
      "site": "0079b45c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0079b418",
      "incomplete_value": false,
      "site": "0079b41c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b52c",
      "incomplete_value": false,
      "site": "0079b52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b4ec",
      "incomplete_value": false,
      "site": "0079b4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0079b42c",
      "DATA",
      [
        "storage",
        "00c6e430",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b45c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b52c",
      "DATA",
      [
        "storage",
        "00c79f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079b42c",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b45c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b52c",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b38c.md#insn-0079b3c0) · [`0079b3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b38c.md#insn-0079b3d8) · [`0079b3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b38c.md#insn-0079b3e0)
- 新版 [`0079b400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md#insn-0079b400) · [`0079b418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md#insn-0079b418) · [`0079b420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md#insn-0079b420)

~~~diff
- 0079b3c0 ["INT_ADD", "register:40f0:8", ["const:79b3c0:8", "const:4:8"]]
- 0079b3c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079b400 ["INT_ADD", "register:40f0:8", ["const:79b400:8", "const:4:8"]]
+ 0079b400 ["CALL", null, ["callee:00c57e90:8"]]
- 0079b3c0 bytes b4f11294
+ 0079b400 bytes a4f21294
- 0079b3d8 ["INT_ADD", "register:40f0:8", ["const:79b3d8:8", "const:4:8"]]
- 0079b3d8 ["CALL", null, ["callee:0059b908:8"]]
+ 0079b418 ["INT_ADD", "register:40f0:8", ["const:79b418:8", "const:4:8"]]
+ 0079b418 ["CALL", null, ["callee:0059b908:8"]]
- 0079b3d8 bytes 3c01f897
+ 0079b418 bytes 3c01f897
- 0079b3e0 ["COPY", "tmp:0:8", ["const:420:8"]]
- 0079b3e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079b3e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079b3e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079b420 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 0079b420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079b3e0 bytes 08811091
+ 0079b420 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfb64f83e19e9e51d67560dcd3e5368"></a>

### [`0079bc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bc7c.md) → [`0079bcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md) FUN_0079bcbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b984.md) · 呼出先 6件 [`0079bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md) [`0079dc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc48.md) [`0079dc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc4c.md) [`0079dccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dccc.md) [`0079dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dcd0.md)
- 新版 呼出元 1件 [`0079b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md) · 呼出先 6件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) [`0079dc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc88.md) [`0079dc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc8c.md) [`0079dd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dd0c.md) [`0079dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dd10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079bce4",
      "incomplete_value": true,
      "site": "0079bce4",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079bca4",
      "incomplete_value": true,
      "site": "0079bca4",
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
            "const:bf8:8"
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
      "definition_site": "0079bcf8",
      "incomplete_value": false,
      "site": "0079bcf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079bcb8",
      "incomplete_value": false,
      "site": "0079bcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0079bce4",
      "DATA",
      [
        "storage",
        "00c79bf8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bcf8",
      "DATA",
      [
        "storage",
        "00c79c88",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bd30",
      "READ",
      [
        "storage",
        "00c79ca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0079bce4",
      "DATA",
      [
        "storage",
        "00c79ff8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bcf8",
      "DATA",
      [
        "storage",
        "00c7a088",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bd30",
      "READ",
      [
        "storage",
        "00c7a0a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079bca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bc7c.md#insn-0079bca0) · [`0079bcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bc7c.md#insn-0079bcb0) · [`0079bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bc7c.md#insn-0079bcb4)
- 新版 [`0079bce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md#insn-0079bce0) · [`0079bcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md#insn-0079bcf0) · [`0079bcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md#insn-0079bcf4)

~~~diff
- 0079bca0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 0079bca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079bca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079bca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079bce0 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 0079bce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079bce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079bce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079bca0 bytes 08e12f91
+ 0079bce0 bytes 08e13f91
- 0079bcb0 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079bcf0 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079bcb0 bytes e82600d0
+ 0079bcf0 bytes e82600f0
- 0079bcb4 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0079bcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079bcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079bcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079bcf4 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0079bcf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079bcf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079bcf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079bcb4 bytes 08213291
+ 0079bcf4 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d834345fa215e2e2a286bd58286cec"></a>

### [`0079bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md) → [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) FUN_0079be08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079bc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bc7c.md) · 呼出先 15件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005a16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md) [`00795e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795e1c.md)
- 新版 呼出元 1件 [`0079bcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079bcbc.md) · 呼出先 15件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.43% / 新版 98.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079bf18",
      "incomplete_value": false,
      "site": "0079bf18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079bed8",
      "incomplete_value": false,
      "site": "0079bed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079c098",
      "incomplete_value": false,
      "site": "0079c098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079c058",
      "incomplete_value": false,
      "site": "0079c058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "0079bf18",
      "DATA",
      [
        "storage",
        "00c79d08",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bfcc",
      "READ",
      [
        "storage",
        "00c79d30",
        null,
        "undefined *"
      ]
    ],
    [
      "0079c098",
      "DATA",
      [
        "storage",
        "00c79d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079bf18",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ],
    [
      "0079bfcc",
      "READ",
      [
        "storage",
        "00c7a130",
        null,
        "undefined *"
      ]
    ],
    [
      "0079c098",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md#insn-0079be00) · [`0079be10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md#insn-0079be10) · [`0079be24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md#insn-0079be24)
- 新版 [`0079be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md#insn-0079be40) · [`0079be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md#insn-0079be50) · [`0079be64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md#insn-0079be64)

~~~diff
- 0079be00 ["INT_ADD", "register:40f0:8", ["const:79be00:8", "const:4:8"]]
- 0079be00 ["CALL", null, ["callee:0079c86c:8"]]
+ 0079be40 ["INT_ADD", "register:40f0:8", ["const:79be40:8", "const:4:8"]]
+ 0079be40 ["CALL", null, ["callee:0079c86c:8"]]
- 0079be00 bytes 8b020094
+ 0079be40 bytes 8b020094
- 0079be10 ["INT_ADD", "register:40f0:8", ["const:79be10:8", "const:4:8"]]
- 0079be10 ["CALL", null, ["callee:0079ddb4:8"]]
+ 0079be50 ["INT_ADD", "register:40f0:8", ["const:79be50:8", "const:4:8"]]
+ 0079be50 ["CALL", null, ["callee:0079ddb4:8"]]
- 0079be10 bytes d9070094
+ 0079be50 bytes d9070094
- 0079be24 ["INT_ADD", "register:40f0:8", ["const:79be24:8", "const:4:8"]]
- 0079be24 ["CALL", null, ["callee:005a1728:8"]]
+ 0079be64 ["INT_ADD", "register:40f0:8", ["const:79be64:8", "const:4:8"]]
+ 0079be64 ["CALL", null, ["callee:005a1728:8"]]
- 0079be24 bytes 3116f897
+ 0079be64 bytes 3116f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-398ac77c5a479f448cffa069795ba5dd"></a>

### [`0079ca00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079ca00.md) → [`0079ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079ca40.md) FUN_0079ca40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0079ca64",
      "incomplete_value": false,
      "site": "0079ca68",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0079ca24",
      "incomplete_value": false,
      "site": "0079ca28",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0079ca68",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ca68",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ca1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079ca00.md#insn-0079ca1c) · [`0079ca34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079ca00.md#insn-0079ca34) · [`0079ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079ca00.md#insn-0079ca44)
- 新版 [`0079ca5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079ca40.md#insn-0079ca5c) · [`0079ca74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079ca40.md#insn-0079ca74) · [`0079ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079ca40.md#insn-0079ca84)

~~~diff
- 0079ca1c ["COPY", "tmp:0:8", ["const:610:8"]]
- 0079ca1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079ca1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079ca1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079ca5c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0079ca5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ca5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ca5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079ca1c bytes 08411891
+ 0079ca5c bytes 08412891
- 0079ca34 ["INT_ADD", "register:40f0:8", ["const:79ca34:8", "const:4:8"]]
- 0079ca34 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0079ca74 ["INT_ADD", "register:40f0:8", ["const:79ca74:8", "const:4:8"]]
+ 0079ca74 ["CALL", null, ["callee:00c57eb0:8"]]
- 0079ca34 bytes 1fec1294
+ 0079ca74 bytes 0fed1294
- 0079ca44 ["INT_ADD", "register:40f0:8", ["const:79ca44:8", "const:4:8"]]
- 0079ca44 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0079ca84 ["INT_ADD", "register:40f0:8", ["const:79ca84:8", "const:4:8"]]
+ 0079ca84 ["CALL", null, ["callee:00c57eb0:8"]]
- 0079ca44 bytes 1bec1294
+ 0079ca84 bytes 0bed1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52562f7bd2d9440e9ffcf74d8154644d"></a>

### [`0079cae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cae8.md) → [`0079cb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cb28.md) FUN_0079cb28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0079cb4c",
      "incomplete_value": false,
      "site": "0079cb50",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0079cb0c",
      "incomplete_value": false,
      "site": "0079cb10",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "0079cb50",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079cb50",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079cb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cae8.md#insn-0079cb04) · [`0079cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cae8.md#insn-0079cb1c) · [`0079cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cae8.md#insn-0079cb2c)
- 新版 [`0079cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cb28.md#insn-0079cb44) · [`0079cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cb28.md#insn-0079cb5c) · [`0079cb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cb28.md#insn-0079cb6c)

~~~diff
- 0079cb04 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0079cb04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079cb04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079cb04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079cb44 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0079cb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079cb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079cb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079cb04 bytes 08411891
+ 0079cb44 bytes 08412891
- 0079cb1c ["INT_ADD", "register:40f0:8", ["const:79cb1c:8", "const:4:8"]]
- 0079cb1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0079cb5c ["INT_ADD", "register:40f0:8", ["const:79cb5c:8", "const:4:8"]]
+ 0079cb5c ["CALL", null, ["callee:00c57eb0:8"]]
- 0079cb1c bytes e5eb1294
+ 0079cb5c bytes d5ec1294
- 0079cb2c ["INT_ADD", "register:40f0:8", ["const:79cb2c:8", "const:4:8"]]
- 0079cb2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0079cb6c ["INT_ADD", "register:40f0:8", ["const:79cb6c:8", "const:4:8"]]
+ 0079cb6c ["CALL", null, ["callee:00c57eb0:8"]]
- 0079cb2c bytes e1eb1294
+ 0079cb6c bytes d1ec1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53f0fd4be3fb5859ba1521569c2e9264"></a>

### [`0079d384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d384.md) → [`0079d3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3c4.md) FUN_0079d3c4

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
      "definition_site": "0079d3d8",
      "incomplete_value": false,
      "site": "0079d3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d398",
      "incomplete_value": false,
      "site": "0079d39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0079d3dc",
      "DATA",
      [
        "storage",
        "00c798e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d3dc",
      "DATA",
      [
        "storage",
        "00c79ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d384.md#insn-0079d390) · [`0079d398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d384.md#insn-0079d398)
- 新版 [`0079d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3c4.md#insn-0079d3d0) · [`0079d3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3c4.md#insn-0079d3d8)

~~~diff
- 0079d390 ["INT_ADD", "register:40f0:8", ["const:79d390:8", "const:4:8"]]
- 0079d390 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079d3d0 ["INT_ADD", "register:40f0:8", ["const:79d3d0:8", "const:4:8"]]
+ 0079d3d0 ["CALL", null, ["callee:00c57e90:8"]]
- 0079d390 bytes c0e91294
+ 0079d3d0 bytes b0ea1294
- 0079d398 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0079d398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d3d8 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0079d3d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d3d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d3d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d398 bytes 08a12391
+ 0079d3d8 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9602d3ec3e3e317942f6a89c4c019b29"></a>

### [`0079d3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3a8.md) → [`0079d3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3e8.md) FUN_0079d3e8

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
      "definition_site": "0079d3ec",
      "incomplete_value": false,
      "site": "0079d3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d3ac",
      "incomplete_value": false,
      "site": "0079d3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0079d3f0",
      "DATA",
      [
        "storage",
        "00c798e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d3f0",
      "DATA",
      [
        "storage",
        "00c79ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3a8.md#insn-0079d3ac)
- 新版 [`0079d3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3e8.md#insn-0079d3ec)

~~~diff
- 0079d3ac ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0079d3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d3ec ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0079d3ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d3ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d3ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d3ac bytes 08a12391
+ 0079d3ec bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa16c26479912ca1f0f936efdc7bb47a"></a>

### [`0079d3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3c0.md) → [`0079d400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d400.md) FUN_0079d400

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
      "site": "0079d424",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079d3e4",
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
      "0079d424",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0079d424",
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

- 旧版 [`0079d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3c0.md#insn-0079d3e4) · [`0079d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3c0.md#insn-0079d3f0)
- 新版 [`0079d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d400.md#insn-0079d424) · [`0079d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d400.md#insn-0079d430)

~~~diff
- 0079d3e4 ["INT_ADD", "register:40f0:8", ["const:79d3e4:8", "const:4:8"]]
- 0079d3e4 ["CALL", null, ["ram:47acb4:8"]]
+ 0079d424 ["INT_ADD", "register:40f0:8", ["const:79d424:8", "const:4:8"]]
+ 0079d424 ["CALL", null, ["ram:47acf4:8"]]
- 0079d3e4 bytes 3476f397
+ 0079d424 bytes 3476f397
- 0079d3f0 ["INT_ADD", "register:40f0:8", ["const:79d3f0:8", "const:4:8"]]
- 0079d3f0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0079d430 ["INT_ADD", "register:40f0:8", ["const:79d430:8", "const:4:8"]]
+ 0079d430 ["CALL", null, ["callee:0047cdd4:8"]]
- 0079d3f0 bytes 697ef397
+ 0079d430 bytes 697ef397
~~~


<a id="compare-8e346a5fc495c82b0588274eff11fdcd"></a>

### [`0079d578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d578.md) → [`0079d5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5b8.md) FUN_0079d5b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d430.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0079d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d470.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0079d5c4",
      "incomplete_value": false,
      "site": "0079d5c8",
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
      "definition_site": "0079d584",
      "incomplete_value": false,
      "site": "0079d588",
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
      "0079d5c4",
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
      "0079d5c4",
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

- 旧版 [`0079d588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d578.md#insn-0079d588) · [`0079d584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d578.md#insn-0079d584)
- 新版 [`0079d5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5b8.md#insn-0079d5c8) · [`0079d5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5b8.md#insn-0079d5c4)

~~~diff
- 0079d588 ["INT_ADD", "register:40f0:8", ["const:79d588:8", "const:4:8"]]
- 0079d588 ["CALL", null, ["callee:0043b778:8"]]
+ 0079d5c8 ["INT_ADD", "register:40f0:8", ["const:79d5c8:8", "const:4:8"]]
+ 0079d5c8 ["CALL", null, ["callee:0043b778:8"]]
- 0079d588 bytes 6c78f297
+ 0079d5c8 bytes 6c78f297
- 0079d584 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0079d584 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0079d584 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0079d584 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0079d5c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0079d5c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0079d5c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0079d5c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0079d584 bytes 00303c91
+ 0079d5c4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88d8eb6358c219b09591bdd952a7b460"></a>

### [`0079d7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d7d4.md) → [`0079d814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d814.md) FUN_0079d814

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
      "definition_site": "0079d838",
      "incomplete_value": false,
      "site": "0079d838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d7f8",
      "incomplete_value": false,
      "site": "0079d7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "0079d838",
      "DATA",
      [
        "storage",
        "00c79968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d838",
      "DATA",
      [
        "storage",
        "00c79d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d7d4.md#insn-0079d7e8) · [`0079d7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d7d4.md#insn-0079d7f4)
- 新版 [`0079d828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d814.md#insn-0079d828) · [`0079d834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d814.md#insn-0079d834)

~~~diff
- 0079d7e8 ["INT_ADD", "register:40f0:8", ["const:79d7e8:8", "const:4:8"]]
- 0079d7e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079d828 ["INT_ADD", "register:40f0:8", ["const:79d828:8", "const:4:8"]]
+ 0079d828 ["CALL", null, ["callee:00c57e90:8"]]
- 0079d7e8 bytes aae81294
+ 0079d828 bytes 9ae91294
- 0079d7f4 ["COPY", "tmp:0:8", ["const:968:8"]]
- 0079d7f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d7f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d7f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d834 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0079d834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d7f4 bytes 08a12591
+ 0079d834 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d18bbbde197730bb70db31819b33b08"></a>

### [`0079d808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d808.md) → [`0079d848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d848.md) FUN_0079d848

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
      "definition_site": "0079d854",
      "incomplete_value": false,
      "site": "0079d854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d814",
      "incomplete_value": false,
      "site": "0079d814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "0079d854",
      "DATA",
      [
        "storage",
        "00c79968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d854",
      "DATA",
      [
        "storage",
        "00c79d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d808.md#insn-0079d810)
- 新版 [`0079d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d848.md#insn-0079d850)

~~~diff
- 0079d810 ["COPY", "tmp:0:8", ["const:968:8"]]
- 0079d810 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079d810 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079d810 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079d850 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0079d850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079d810 bytes 29a12591
+ 0079d850 bytes 29a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ac44da9e956368fdf87ee9c9c3a9a8"></a>

### [`0079d85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d85c.md) → [`0079d89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d89c.md) FUN_0079d89c

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
      "definition_site": "0079d8c0",
      "incomplete_value": false,
      "site": "0079d8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d880",
      "incomplete_value": false,
      "site": "0079d880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "0079d8c0",
      "DATA",
      [
        "storage",
        "00c799e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d8c0",
      "DATA",
      [
        "storage",
        "00c79de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d85c.md#insn-0079d870) · [`0079d87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d85c.md#insn-0079d87c)
- 新版 [`0079d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d89c.md#insn-0079d8b0) · [`0079d8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d89c.md#insn-0079d8bc)

~~~diff
- 0079d870 ["INT_ADD", "register:40f0:8", ["const:79d870:8", "const:4:8"]]
- 0079d870 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079d8b0 ["INT_ADD", "register:40f0:8", ["const:79d8b0:8", "const:4:8"]]
+ 0079d8b0 ["CALL", null, ["callee:00c57e90:8"]]
- 0079d870 bytes 88e81294
+ 0079d8b0 bytes 78e91294
- 0079d87c ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0079d87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d8bc ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0079d8bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d8bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d8bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d87c bytes 08a12791
+ 0079d8bc bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2847e2b032dceca5f3c159096bad3799"></a>

### [`0079d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d890.md) → [`0079d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8d0.md) FUN_0079d8d0

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
      "definition_site": "0079d8dc",
      "incomplete_value": false,
      "site": "0079d8dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d89c",
      "incomplete_value": false,
      "site": "0079d89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0079d8dc",
      "DATA",
      [
        "storage",
        "00c799e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d8dc",
      "DATA",
      [
        "storage",
        "00c79de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d890.md#insn-0079d898)
- 新版 [`0079d8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8d0.md#insn-0079d8d8)

~~~diff
- 0079d898 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0079d898 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079d898 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079d898 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079d8d8 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0079d8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079d898 bytes 29a12791
+ 0079d8d8 bytes 29a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97a73b77a3e96273125d0a3519c80e9"></a>

### [`0079d954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d954.md) → [`0079d994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md) FUN_0079d994

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
      "definition_site": "0079d9b8",
      "incomplete_value": false,
      "site": "0079d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d978",
      "incomplete_value": false,
      "site": "0079d978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "0079d9b8",
      "DATA",
      [
        "storage",
        "00c79a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d9b8",
      "DATA",
      [
        "storage",
        "00c79e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d954.md#insn-0079d968) · [`0079d974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d954.md#insn-0079d974)
- 新版 [`0079d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md#insn-0079d9a8) · [`0079d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md#insn-0079d9b4)

~~~diff
- 0079d968 ["INT_ADD", "register:40f0:8", ["const:79d968:8", "const:4:8"]]
- 0079d968 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079d9a8 ["INT_ADD", "register:40f0:8", ["const:79d9a8:8", "const:4:8"]]
+ 0079d9a8 ["CALL", null, ["callee:00c57e90:8"]]
- 0079d968 bytes 4ae81294
+ 0079d9a8 bytes 3ae91294
- 0079d974 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0079d974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d9b4 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0079d9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d974 bytes 08a12991
+ 0079d9b4 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84957c6670693228b160f2510b62173a"></a>

### [`0079d988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d988.md) → [`0079d9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9c8.md) FUN_0079d9c8

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
      "definition_site": "0079d9d4",
      "incomplete_value": false,
      "site": "0079d9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d994",
      "incomplete_value": false,
      "site": "0079d994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0079d9d4",
      "DATA",
      [
        "storage",
        "00c79a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d9d4",
      "DATA",
      [
        "storage",
        "00c79e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d988.md#insn-0079d990)
- 新版 [`0079d9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9c8.md#insn-0079d9d0)

~~~diff
- 0079d990 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0079d990 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079d990 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079d990 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079d9d0 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0079d9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079d9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079d990 bytes 29a12991
+ 0079d9d0 bytes 29a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7291213cec5eb15adf74d4bdd60cf764"></a>

### [`0079d9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d9a4.md) → [`0079d9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md) FUN_0079d9e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) [`0079b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) [`0079b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b280.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "site": "0079da0c",
      "value": [
        "leaf",
        "ram:768e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079d9cc",
      "value": [
        "leaf",
        "ram:768e50:8"
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
      "0079da0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ]
  ],
  "added": [
    [
      "0079da0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d9a4.md#insn-0079d9cc) · [`0079d9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d9a4.md#insn-0079d9c4) · [`0079da50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d9a4.md#insn-0079da50)
- 新版 [`0079da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da0c) · [`0079da04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da04) · [`0079da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da90)

~~~diff
- 0079d9cc ["INT_ADD", "register:40f0:8", ["const:79d9cc:8", "const:4:8"]]
- 0079d9cc ["CALL", null, ["ram:768e50:8"]]
+ 0079da0c ["INT_ADD", "register:40f0:8", ["const:79da0c:8", "const:4:8"]]
+ 0079da0c ["CALL", null, ["ram:768e90:8"]]
- 0079d9cc bytes 212dff97
+ 0079da0c bytes 212dff97
- 0079d9c4 ["INT_ADD", "register:40f0:8", ["const:79d9c4:8", "const:4:8"]]
- 0079d9c4 ["CALL", null, ["callee:008514f8:8"]]
+ 0079da04 ["INT_ADD", "register:40f0:8", ["const:79da04:8", "const:4:8"]]
+ 0079da04 ["CALL", null, ["callee:008514f8:8"]]
- 0079d9c4 bytes bdce0294
+ 0079da04 bytes bdce0294
- 0079da50 ["INT_ADD", "register:40f0:8", ["const:79da50:8", "const:4:8"]]
- 0079da50 ["CALL", null, ["callee:00459d74:8"]]
+ 0079da90 ["INT_ADD", "register:40f0:8", ["const:79da90:8", "const:4:8"]]
+ 0079da90 ["CALL", null, ["callee:00459d74:8"]]
- 0079da50 bytes b9f0f297
+ 0079da90 bytes b9f0f297
~~~


<a id="compare-c5549b01edf8782a56196b84e0e4ccb4"></a>

### [`0079da84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da84.md) → [`0079dac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md) FUN_0079dac4

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
      "definition_site": "0079dae8",
      "incomplete_value": false,
      "site": "0079dae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079daa8",
      "incomplete_value": false,
      "site": "0079daa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "0079dae8",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dae8",
      "DATA",
      [
        "storage",
        "00c79ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079da98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da84.md#insn-0079da98) · [`0079daa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079da84.md#insn-0079daa4)
- 新版 [`0079dad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md#insn-0079dad8) · [`0079dae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md#insn-0079dae4)

~~~diff
- 0079da98 ["INT_ADD", "register:40f0:8", ["const:79da98:8", "const:4:8"]]
- 0079da98 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079dad8 ["INT_ADD", "register:40f0:8", ["const:79dad8:8", "const:4:8"]]
+ 0079dad8 ["CALL", null, ["callee:00c57e90:8"]]
- 0079da98 bytes fee71294
+ 0079dad8 bytes eee81294
- 0079daa4 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0079daa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079daa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079daa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dae4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0079dae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079daa4 bytes 08a12b91
+ 0079dae4 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c10c326d123fe301926874b1aafb6459"></a>

### [`0079dab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dab8.md) → [`0079daf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079daf8.md) FUN_0079daf8

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
      "definition_site": "0079db04",
      "incomplete_value": false,
      "site": "0079db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dac4",
      "incomplete_value": false,
      "site": "0079dac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0079db04",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079db04",
      "DATA",
      [
        "storage",
        "00c79ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dab8.md#insn-0079dac0)
- 新版 [`0079db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079daf8.md#insn-0079db00)

~~~diff
- 0079dac0 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0079dac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079db00 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0079db00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dac0 bytes 29a12b91
+ 0079db00 bytes 29a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f40dd4550ee6deabae09d435dbf50f"></a>

### [`0079db08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db08.md) → [`0079db48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md) FUN_0079db48

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
      "definition_site": "0079db6c",
      "incomplete_value": false,
      "site": "0079db6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db2c",
      "incomplete_value": false,
      "site": "0079db2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "0079db6c",
      "DATA",
      [
        "storage",
        "00c79b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079db6c",
      "DATA",
      [
        "storage",
        "00c79f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db08.md#insn-0079db1c) · [`0079db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db08.md#insn-0079db28)
- 新版 [`0079db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md#insn-0079db5c) · [`0079db68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md#insn-0079db68)

~~~diff
- 0079db1c ["INT_ADD", "register:40f0:8", ["const:79db1c:8", "const:4:8"]]
- 0079db1c ["CALL", null, ["callee:00c57e90:8"]]
+ 0079db5c ["INT_ADD", "register:40f0:8", ["const:79db5c:8", "const:4:8"]]
+ 0079db5c ["CALL", null, ["callee:00c57e90:8"]]
- 0079db1c bytes dde71294
+ 0079db5c bytes cde81294
- 0079db28 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 0079db28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079db28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079db28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079db68 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 0079db68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079db68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079db68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079db28 bytes 08e12d91
+ 0079db68 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e504d3608732b9c443d0740a036596c"></a>

### [`0079db3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db3c.md) → [`0079db7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db7c.md) FUN_0079db7c

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
      "definition_site": "0079db88",
      "incomplete_value": false,
      "site": "0079db88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db48",
      "incomplete_value": false,
      "site": "0079db48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "0079db88",
      "DATA",
      [
        "storage",
        "00c79b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079db88",
      "DATA",
      [
        "storage",
        "00c79f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db3c.md#insn-0079db44)
- 新版 [`0079db84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db7c.md#insn-0079db84)

~~~diff
- 0079db44 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 0079db44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079db44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079db44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079db84 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 0079db84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079db44 bytes 29e12d91
+ 0079db84 bytes 29e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aacd7fa42a5e1ee30aa8abcf9d29918d"></a>

### [`0079dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc00.md) → [`0079dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md) FUN_0079dc40

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
      "definition_site": "0079dc64",
      "incomplete_value": false,
      "site": "0079dc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dc24",
      "incomplete_value": false,
      "site": "0079dc24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "0079dc64",
      "DATA",
      [
        "storage",
        "00c79bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dc64",
      "DATA",
      [
        "storage",
        "00c79ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc00.md#insn-0079dc14) · [`0079dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc00.md#insn-0079dc20)
- 新版 [`0079dc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md#insn-0079dc54) · [`0079dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md#insn-0079dc60)

~~~diff
- 0079dc14 ["INT_ADD", "register:40f0:8", ["const:79dc14:8", "const:4:8"]]
- 0079dc14 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079dc54 ["INT_ADD", "register:40f0:8", ["const:79dc54:8", "const:4:8"]]
+ 0079dc54 ["CALL", null, ["callee:00c57e90:8"]]
- 0079dc14 bytes 9fe71294
+ 0079dc54 bytes 8fe81294
- 0079dc20 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 0079dc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dc60 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 0079dc60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dc60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dc60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dc20 bytes 08e12f91
+ 0079dc60 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a372443f332af01f74af312c365d67"></a>

### [`0079dc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc34.md) → [`0079dc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc74.md) FUN_0079dc74

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
      "definition_site": "0079dc80",
      "incomplete_value": false,
      "site": "0079dc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dc40",
      "incomplete_value": false,
      "site": "0079dc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "0079dc80",
      "DATA",
      [
        "storage",
        "00c79bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dc80",
      "DATA",
      [
        "storage",
        "00c79ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc34.md#insn-0079dc3c)
- 新版 [`0079dc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc74.md#insn-0079dc7c)

~~~diff
- 0079dc3c ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 0079dc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dc7c ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 0079dc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dc3c bytes 29e12f91
+ 0079dc7c bytes 29e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c3ba82bb10029d47def1a6240ed3763"></a>

### [`0079dc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc84.md) → [`0079dcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md) FUN_0079dcc4

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
      "definition_site": "0079dce8",
      "incomplete_value": false,
      "site": "0079dce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dca8",
      "incomplete_value": false,
      "site": "0079dca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0079dce8",
      "DATA",
      [
        "storage",
        "00c79c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dce8",
      "DATA",
      [
        "storage",
        "00c7a088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc84.md#insn-0079dc98) · [`0079dca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc84.md#insn-0079dca0) · [`0079dca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dc84.md#insn-0079dca4)
- 新版 [`0079dcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md#insn-0079dcd8) · [`0079dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md#insn-0079dce0) · [`0079dce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md#insn-0079dce4)

~~~diff
- 0079dc98 ["INT_ADD", "register:40f0:8", ["const:79dc98:8", "const:4:8"]]
- 0079dc98 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079dcd8 ["INT_ADD", "register:40f0:8", ["const:79dcd8:8", "const:4:8"]]
+ 0079dcd8 ["CALL", null, ["callee:00c57e90:8"]]
- 0079dc98 bytes 7ee71294
+ 0079dcd8 bytes 6ee81294
- 0079dca0 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079dce0 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079dca0 bytes e8260090
+ 0079dce0 bytes e82600b0
- 0079dca4 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0079dca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dce4 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0079dce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dca4 bytes 08213291
+ 0079dce4 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bc887a34612c3f19ed7ea8d3bcf8be3"></a>

### [`0079dcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dcb8.md) → [`0079dcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcf8.md) FUN_0079dcf8

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
      "definition_site": "0079dd04",
      "incomplete_value": false,
      "site": "0079dd04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dcc4",
      "incomplete_value": false,
      "site": "0079dcc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0079dd04",
      "DATA",
      [
        "storage",
        "00c79c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dd04",
      "DATA",
      [
        "storage",
        "00c7a088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dcb8.md#insn-0079dcbc) · [`0079dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dcb8.md#insn-0079dcc0)
- 新版 [`0079dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcf8.md#insn-0079dcfc) · [`0079dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcf8.md#insn-0079dd00)

~~~diff
- 0079dcbc ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079dcfc ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079dcbc bytes e9260090
+ 0079dcfc bytes e92600b0
- 0079dcc0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0079dcc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dcc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dcc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dd00 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 0079dd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dcc0 bytes 29213291
+ 0079dd00 bytes 29210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32be378dc8224829f22043024064bda3"></a>

### [`0079dd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dd74.md) → [`0079ddb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md) FUN_0079ddb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079bdc8.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0079ddec",
      "incomplete_value": false,
      "site": "0079ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ddac",
      "incomplete_value": false,
      "site": "0079ddb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "0079ddf4",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079deac",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ddf4",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079deac",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ddf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dd74.md#insn-0079ddf4) · [`0079dda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dd74.md#insn-0079dda4) · [`0079ddac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dd74.md#insn-0079ddac)
- 新版 [`0079de34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079de34) · [`0079dde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079dde4) · [`0079ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079ddec)

~~~diff
- 0079ddf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ddf4 ["INT_ADD", "register:40f0:8", ["const:79ddf4:8", "const:4:8"]]
- 0079ddf4 ["CALLIND", null, ["register:0:8"]]
+ 0079de34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079de34 ["INT_ADD", "register:40f0:8", ["const:79de34:8", "const:4:8"]]
+ 0079de34 ["CALLIND", null, ["register:0:8"]]
- 0079ddf4 bytes 00013fd6
+ 0079de34 bytes 00013fd6
- 0079dda4 ["INT_ADD", "register:40f0:8", ["const:79dda4:8", "const:4:8"]]
- 0079dda4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079dde4 ["INT_ADD", "register:40f0:8", ["const:79dde4:8", "const:4:8"]]
+ 0079dde4 ["CALL", null, ["callee:00c57e90:8"]]
- 0079dda4 bytes 3be71294
+ 0079dde4 bytes 2be81294
- 0079ddac ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 0079ddac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079ddac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079ddac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079ddec ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0079ddec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ddec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ddec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079ddac bytes 08010791
+ 0079ddec bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2b1856fc6ef1d758490537af5ce911"></a>

### [`0079deec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079deec.md) → [`0079df2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md) FUN_0079df2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0079df44",
      "incomplete_value": false,
      "site": "0079df54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079df04",
      "incomplete_value": false,
      "site": "0079df14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "0079df54",
      "DATA",
      [
        "storage",
        "00c79d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079df54",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079deec.md#insn-0079df00) · [`0079df04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079deec.md#insn-0079df04) · [`0079df38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079deec.md#insn-0079df38)
- 新版 [`0079df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md#insn-0079df40) · [`0079df44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md#insn-0079df44) · [`0079df78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md#insn-0079df78)

~~~diff
- 0079df00 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079df40 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079df00 bytes e8260090
+ 0079df40 bytes e82600b0
- 0079df04 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 0079df04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079df04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079df04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079df44 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0079df44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079df04 bytes 08213491
+ 0079df44 bytes 08210491
- 0079df38 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079df38 ["INT_ADD", "register:40f0:8", ["const:79df38:8", "const:4:8"]]
- 0079df38 ["CALLIND", null, ["register:0:8"]]
+ 0079df78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079df78 ["INT_ADD", "register:40f0:8", ["const:79df78:8", "const:4:8"]]
+ 0079df78 ["CALLIND", null, ["register:0:8"]]
- 0079df38 bytes 00013fd6
+ 0079df78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb498f95e6c06d246df9fd9d1d94eb6e"></a>

### [`0079e008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e008.md) → [`0079e048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md) FUN_0079e048

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079e078",
      "incomplete_value": false,
      "site": "0079e078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e038",
      "incomplete_value": false,
      "site": "0079e038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "0079e078",
      "DATA",
      [
        "storage",
        "00c79d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e078",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e008.md#insn-0079e020) · [`0079e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e008.md#insn-0079e02c) · [`0079e030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e008.md#insn-0079e030)
- 新版 [`0079e060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e060) · [`0079e06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e06c) · [`0079e070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e070)

~~~diff
- 0079e020 ["INT_ADD", "register:40f0:8", ["const:79e020:8", "const:4:8"]]
- 0079e020 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079e060 ["INT_ADD", "register:40f0:8", ["const:79e060:8", "const:4:8"]]
+ 0079e060 ["CALL", null, ["callee:00c57e90:8"]]
- 0079e020 bytes 9ce61294
+ 0079e060 bytes 8ce71294
- 0079e02c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079e06c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079e02c bytes c82600f0
+ 0079e06c bytes e8260090
- 0079e030 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 0079e030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e070 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0079e070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e030 bytes 08213491
+ 0079e070 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f97b2ea30e51b2974483114b57f52d8a"></a>

### [`0079e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e110.md) → [`0079e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md) FUN_0079e150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079e178",
      "incomplete_value": false,
      "site": "0079e178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e138",
      "incomplete_value": false,
      "site": "0079e138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "0079e178",
      "DATA",
      [
        "storage",
        "00c79d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e178",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e110.md#insn-0079e12c) · [`0079e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e110.md#insn-0079e130) · [`0079e134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e110.md#insn-0079e134)
- 新版 [`0079e16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md#insn-0079e16c) · [`0079e170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md#insn-0079e170)

~~~diff
- 0079e12c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079e16c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079e12c bytes c82600f0
+ 0079e16c bytes e8260090
- 0079e130 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 0079e130 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e130 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e130 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e170 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0079e170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e130 bytes 08213491
+ 0079e170 bytes 08210491
- 0079e134 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0079e134 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6516e85805ef25a13f674eea0ce699bf"></a>

### [`0079e4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e4b4.md) → [`0079e4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4f4.md) FUN_0079e4f4

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
      "definition_site": "0079e500",
      "incomplete_value": false,
      "site": "0079e50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e4c0",
      "incomplete_value": false,
      "site": "0079e4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "0079e50c",
      "DATA",
      [
        "storage",
        "00c79d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e50c",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e4b4.md#insn-0079e4bc) · [`0079e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e4b4.md#insn-0079e4c0)
- 新版 [`0079e4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4f4.md#insn-0079e4fc) · [`0079e500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4f4.md#insn-0079e500)

~~~diff
- 0079e4bc ["COPY", "register:4050:8", ["const:c79000:8"]]
+ 0079e4fc ["COPY", "register:4050:8", ["const:c7a000:8"]]
- 0079e4bc bytes ca2600f0
+ 0079e4fc bytes ea260090
- 0079e4c0 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0079e4c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079e4c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079e4c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079e500 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0079e500 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e500 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e500 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079e4c0 bytes 4a213691
+ 0079e500 bytes 4a210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3f0d9adbbd7a797cd3d4243ddce0ccd"></a>

### [`0079e554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e554.md) → [`0079e594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md) FUN_0079e594

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
      "definition_site": "0079e5c0",
      "incomplete_value": false,
      "site": "0079e5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e580",
      "incomplete_value": false,
      "site": "0079e580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "0079e5c0",
      "DATA",
      [
        "storage",
        "00c79d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e5c0",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e554.md#insn-0079e568) · [`0079e574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e554.md#insn-0079e574) · [`0079e578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e554.md#insn-0079e578)
- 新版 [`0079e5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5a8) · [`0079e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5b4) · [`0079e5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5b8)

~~~diff
- 0079e568 ["INT_ADD", "register:40f0:8", ["const:79e568:8", "const:4:8"]]
- 0079e568 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079e5a8 ["INT_ADD", "register:40f0:8", ["const:79e5a8:8", "const:4:8"]]
+ 0079e5a8 ["CALL", null, ["callee:00c57e90:8"]]
- 0079e568 bytes 4ae51294
+ 0079e5a8 bytes 3ae61294
- 0079e574 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079e5b4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079e574 bytes c82600f0
+ 0079e5b4 bytes e8260090
- 0079e578 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0079e578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e5b8 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0079e5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e578 bytes 08213691
+ 0079e5b8 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4c02897a6e74730b5a366971f00284"></a>

### [`0079e5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e5dc.md) → [`0079e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md) FUN_0079e61c

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
      "definition_site": "0079e638",
      "incomplete_value": false,
      "site": "0079e638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e5f8",
      "incomplete_value": false,
      "site": "0079e5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "0079e638",
      "DATA",
      [
        "storage",
        "00c79d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e638",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e5dc.md#insn-0079e5f0) · [`0079e5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e5dc.md#insn-0079e5f4) · [`0079e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e5dc.md#insn-0079e618)
- 新版 [`0079e630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md#insn-0079e630) · [`0079e634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md#insn-0079e634) · [`0079e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md#insn-0079e658)

~~~diff
- 0079e5f0 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079e630 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079e5f0 bytes c92600f0
+ 0079e630 bytes e9260090
- 0079e5f4 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0079e5f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079e5f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079e5f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079e634 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0079e634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079e5f4 bytes 29213691
+ 0079e634 bytes 29210691
- 0079e618 ["COPY", "register:0:8", ["register:4048:8"]]
- 0079e618 ["INT_ADD", "register:40f0:8", ["const:79e618:8", "const:4:8"]]
- 0079e618 ["CALLIND", null, ["register:0:8"]]
+ 0079e658 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079e658 ["INT_ADD", "register:40f0:8", ["const:79e658:8", "const:4:8"]]
+ 0079e658 ["CALLIND", null, ["register:0:8"]]
- 0079e618 bytes 20013fd6
+ 0079e658 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-102533333d9a770d5693a6929fc40a15"></a>

### [`0079e720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e720.md) → [`0079e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md) FUN_0079e760

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0079e798",
      "incomplete_value": false,
      "site": "0079e7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e758",
      "incomplete_value": false,
      "site": "0079e760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "0079e7a0",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079e858",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e7a0",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079e858",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e720.md#insn-0079e7a0) · [`0079e750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e720.md#insn-0079e750) · [`0079e758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e720.md#insn-0079e758)
- 新版 [`0079e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e7e0) · [`0079e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e790) · [`0079e798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e798)

~~~diff
- 0079e7a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e7a0 ["INT_ADD", "register:40f0:8", ["const:79e7a0:8", "const:4:8"]]
- 0079e7a0 ["CALLIND", null, ["register:0:8"]]
+ 0079e7e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e7e0 ["INT_ADD", "register:40f0:8", ["const:79e7e0:8", "const:4:8"]]
+ 0079e7e0 ["CALLIND", null, ["register:0:8"]]
- 0079e7a0 bytes 00013fd6
+ 0079e7e0 bytes 00013fd6
- 0079e750 ["INT_ADD", "register:40f0:8", ["const:79e750:8", "const:4:8"]]
- 0079e750 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079e790 ["INT_ADD", "register:40f0:8", ["const:79e790:8", "const:4:8"]]
+ 0079e790 ["CALL", null, ["callee:00c57e90:8"]]
- 0079e750 bytes d0e41294
+ 0079e790 bytes c0e51294
- 0079e758 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 0079e758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e798 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0079e798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e758 bytes 08010791
+ 0079e798 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3aaa3f786bd6fdc838480b9025f0161"></a>

### [`0079e898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e898.md) → [`0079e8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md) FUN_0079e8d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0079e8f0",
      "incomplete_value": false,
      "site": "0079e900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e8b0",
      "incomplete_value": false,
      "site": "0079e8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "0079e900",
      "DATA",
      [
        "storage",
        "00c79e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e900",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e898.md#insn-0079e8ac) · [`0079e8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e898.md#insn-0079e8b0) · [`0079e8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e898.md#insn-0079e8e4)
- 新版 [`0079e8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md#insn-0079e8ec) · [`0079e8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md#insn-0079e8f0) · [`0079e924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md#insn-0079e924)

~~~diff
- 0079e8ac ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079e8ec ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079e8ac bytes c82600f0
+ 0079e8ec bytes e8260090
- 0079e8b0 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 0079e8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e8f0 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0079e8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e8b0 bytes 08213891
+ 0079e8f0 bytes 08210891
- 0079e8e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e8e4 ["INT_ADD", "register:40f0:8", ["const:79e8e4:8", "const:4:8"]]
- 0079e8e4 ["CALLIND", null, ["register:0:8"]]
+ 0079e924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e924 ["INT_ADD", "register:40f0:8", ["const:79e924:8", "const:4:8"]]
+ 0079e924 ["CALLIND", null, ["register:0:8"]]
- 0079e8e4 bytes 00013fd6
+ 0079e924 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17b3c72b25321c12614e4f02ecac6b0"></a>

### [`0079e928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e928.md) → [`0079e968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md) FUN_0079e968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0079e980",
      "incomplete_value": false,
      "site": "0079e990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e940",
      "incomplete_value": false,
      "site": "0079e950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "0079e990",
      "DATA",
      [
        "storage",
        "00c79e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e990",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e928.md#insn-0079e93c) · [`0079e940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e928.md#insn-0079e940) · [`0079e974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079e928.md#insn-0079e974)
- 新版 [`0079e97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e97c) · [`0079e980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e980) · [`0079e9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e9b4)

~~~diff
- 0079e93c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079e97c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079e93c bytes c82600f0
+ 0079e97c bytes e8260090
- 0079e940 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 0079e940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e980 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0079e980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e940 bytes 08213891
+ 0079e980 bytes 08210891
- 0079e974 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e974 ["INT_ADD", "register:40f0:8", ["const:79e974:8", "const:4:8"]]
- 0079e974 ["CALLIND", null, ["register:0:8"]]
+ 0079e9b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e9b4 ["INT_ADD", "register:40f0:8", ["const:79e9b4:8", "const:4:8"]]
+ 0079e9b4 ["CALLIND", null, ["register:0:8"]]
- 0079e974 bytes 00013fd6
+ 0079e9b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-721fb67e0dd00f52846ccc4f0a1c11c2"></a>

### [`0079eabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eabc.md) → [`0079eafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md) FUN_0079eafc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079eb24",
      "incomplete_value": false,
      "site": "0079eb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079eae4",
      "incomplete_value": false,
      "site": "0079eae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "0079eb24",
      "DATA",
      [
        "storage",
        "00c79e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079eb24",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eabc.md#insn-0079ead8) · [`0079eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eabc.md#insn-0079eadc) · [`0079eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eabc.md#insn-0079eae0)
- 新版 [`0079eb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md#insn-0079eb18) · [`0079eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md#insn-0079eb1c)

~~~diff
- 0079ead8 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079eb18 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079ead8 bytes c82600f0
+ 0079eb18 bytes e8260090
- 0079eadc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 0079eadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079eadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079eadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079eb1c ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0079eb1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eb1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eb1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079eadc bytes 08213891
+ 0079eb1c bytes 08210891
- 0079eae0 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0079eae0 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254fa3dd703fe6dbe149ff343e98c8aa"></a>

### [`0079ee48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee48.md) → [`0079ee88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee88.md) FUN_0079ee88

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
      "definition_site": "0079ee94",
      "incomplete_value": false,
      "site": "0079eea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ee54",
      "incomplete_value": false,
      "site": "0079ee60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0079eea0",
      "DATA",
      [
        "storage",
        "00c79e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079eea0",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ee50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee48.md#insn-0079ee50) · [`0079ee54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee48.md#insn-0079ee54)
- 新版 [`0079ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee88.md#insn-0079ee90) · [`0079ee94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee88.md#insn-0079ee94)

~~~diff
- 0079ee50 ["COPY", "register:4050:8", ["const:c79000:8"]]
+ 0079ee90 ["COPY", "register:4050:8", ["const:c7a000:8"]]
- 0079ee50 bytes ca2600f0
+ 0079ee90 bytes ea260090
- 0079ee54 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0079ee54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079ee54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079ee54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079ee94 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0079ee94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079ee94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079ee94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079ee54 bytes 4a213a91
+ 0079ee94 bytes 4a210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae7c8c5161498da157c21ae2e47b605"></a>

### [`0079ee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee8c.md) → [`0079eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md) FUN_0079eecc

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
      "definition_site": "0079eee4",
      "incomplete_value": false,
      "site": "0079eef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079eea4",
      "incomplete_value": false,
      "site": "0079eeb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0079eef0",
      "DATA",
      [
        "storage",
        "00c79e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079eef0",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079eea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee8c.md#insn-0079eea0) · [`0079eea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee8c.md#insn-0079eea4) · [`0079eed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ee8c.md#insn-0079eed4)
- 新版 [`0079eee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md#insn-0079eee0) · [`0079eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md#insn-0079eee4) · [`0079ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md#insn-0079ef14)

~~~diff
- 0079eea0 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079eee0 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079eea0 bytes c82600f0
+ 0079eee0 bytes e8260090
- 0079eea4 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0079eea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079eea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079eea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079eee4 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0079eee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079eea4 bytes 08213a91
+ 0079eee4 bytes 08210a91
- 0079eed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079eed4 ["INT_ADD", "register:40f0:8", ["const:79eed4:8", "const:4:8"]]
- 0079eed4 ["CALLIND", null, ["register:0:8"]]
+ 0079ef14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ef14 ["INT_ADD", "register:40f0:8", ["const:79ef14:8", "const:4:8"]]
+ 0079ef14 ["CALLIND", null, ["register:0:8"]]
- 0079eed4 bytes 00013fd6
+ 0079ef14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73cbee9faad595a18864e44233b25ad7"></a>

### [`0079eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eee8.md) → [`0079ef28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md) FUN_0079ef28

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
      "definition_site": "0079ef54",
      "incomplete_value": false,
      "site": "0079ef54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ef14",
      "incomplete_value": false,
      "site": "0079ef14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0079ef54",
      "DATA",
      [
        "storage",
        "00c79e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ef54",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079eefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eee8.md#insn-0079eefc) · [`0079ef08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eee8.md#insn-0079ef08) · [`0079ef0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079eee8.md#insn-0079ef0c)
- 新版 [`0079ef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef3c) · [`0079ef48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef48) · [`0079ef4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef4c)

~~~diff
- 0079eefc ["INT_ADD", "register:40f0:8", ["const:79eefc:8", "const:4:8"]]
- 0079eefc ["CALL", null, ["callee:00c57e90:8"]]
+ 0079ef3c ["INT_ADD", "register:40f0:8", ["const:79ef3c:8", "const:4:8"]]
+ 0079ef3c ["CALL", null, ["callee:00c57e90:8"]]
- 0079eefc bytes e5e21294
+ 0079ef3c bytes d5e31294
- 0079ef08 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079ef48 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079ef08 bytes c82600f0
+ 0079ef48 bytes e8260090
- 0079ef0c ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0079ef0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079ef0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079ef0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079ef4c ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0079ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079ef0c bytes 08213a91
+ 0079ef4c bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36d345c748ba4a26183954fda152b43b"></a>

### [`0079ef70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ef70.md) → [`0079efb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md) FUN_0079efb0

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
      "definition_site": "0079efcc",
      "incomplete_value": false,
      "site": "0079efcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ef8c",
      "incomplete_value": false,
      "site": "0079ef8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0079efcc",
      "DATA",
      [
        "storage",
        "00c79e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079efcc",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ef84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ef70.md#insn-0079ef84) · [`0079ef88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ef70.md#insn-0079ef88) · [`0079efac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079e/0079ef70.md#insn-0079efac)
- 新版 [`0079efc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md#insn-0079efc4) · [`0079efc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md#insn-0079efc8) · [`0079efec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md#insn-0079efec)

~~~diff
- 0079ef84 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079efc4 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079ef84 bytes c92600f0
+ 0079efc4 bytes e9260090
- 0079ef88 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0079ef88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079ef88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079ef88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079efc8 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 0079efc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079efc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079efc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079ef88 bytes 29213a91
+ 0079efc8 bytes 29210a91
- 0079efac ["COPY", "register:0:8", ["register:4048:8"]]
- 0079efac ["INT_ADD", "register:40f0:8", ["const:79efac:8", "const:4:8"]]
- 0079efac ["CALLIND", null, ["register:0:8"]]
+ 0079efec ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079efec ["INT_ADD", "register:40f0:8", ["const:79efec:8", "const:4:8"]]
+ 0079efec ["CALLIND", null, ["register:0:8"]]
- 0079efac bytes 20013fd6
+ 0079efec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-744e3927e05275961f4553581aa19d8b"></a>

### [`0079f22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f22c.md) → [`0079f26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md) FUN_0079f26c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079f284",
      "incomplete_value": true,
      "site": "0079f294",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f244",
      "incomplete_value": true,
      "site": "0079f254",
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
            "const:f08:8"
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
      "0079f294",
      "DATA",
      [
        "storage",
        "00c79f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f294",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f22c.md#insn-0079f240) · [`0079f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f22c.md#insn-0079f244) · [`0079f278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f22c.md#insn-0079f278)
- 新版 [`0079f280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md#insn-0079f280) · [`0079f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md#insn-0079f284) · [`0079f2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md#insn-0079f2b8)

~~~diff
- 0079f240 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079f280 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079f240 bytes c82600d0
+ 0079f280 bytes c82600f0
- 0079f244 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0079f244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f284 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0079f284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f244 bytes 08213c91
+ 0079f284 bytes 08210c91
- 0079f278 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f278 ["INT_ADD", "register:40f0:8", ["const:79f278:8", "const:4:8"]]
- 0079f278 ["CALLIND", null, ["register:0:8"]]
+ 0079f2b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f2b8 ["INT_ADD", "register:40f0:8", ["const:79f2b8:8", "const:4:8"]]
+ 0079f2b8 ["CALLIND", null, ["register:0:8"]]
- 0079f278 bytes 00013fd6
+ 0079f2b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d566ee957ae92d2450c697f483289fc"></a>

### [`0079f348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f348.md) → [`0079f388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md) FUN_0079f388

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079f3b8",
      "incomplete_value": false,
      "site": "0079f3b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f378",
      "incomplete_value": false,
      "site": "0079f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0079f3b8",
      "DATA",
      [
        "storage",
        "00c79f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f3b8",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f348.md#insn-0079f360) · [`0079f36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f348.md#insn-0079f36c) · [`0079f370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f348.md#insn-0079f370)
- 新版 [`0079f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f3a0) · [`0079f3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f3ac) · [`0079f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f3b0)

~~~diff
- 0079f360 ["INT_ADD", "register:40f0:8", ["const:79f360:8", "const:4:8"]]
- 0079f360 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079f3a0 ["INT_ADD", "register:40f0:8", ["const:79f3a0:8", "const:4:8"]]
+ 0079f3a0 ["CALL", null, ["callee:00c57e90:8"]]
- 0079f360 bytes cce11294
+ 0079f3a0 bytes bce21294
- 0079f36c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079f3ac ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079f36c bytes c82600d0
+ 0079f3ac bytes c82600f0
- 0079f370 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0079f370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f3b0 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0079f3b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f3b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f3b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f370 bytes 08213c91
+ 0079f3b0 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a68a3ba779d400eea470b7c6edce9396"></a>

### [`0079f450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f450.md) → [`0079f490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md) FUN_0079f490

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0079f4b8",
      "incomplete_value": false,
      "site": "0079f4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f478",
      "incomplete_value": false,
      "site": "0079f478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0079f4b8",
      "DATA",
      [
        "storage",
        "00c79f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f4b8",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f450.md#insn-0079f46c) · [`0079f470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f450.md#insn-0079f470) · [`0079f494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f450.md#insn-0079f494)
- 新版 [`0079f4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f4ac) · [`0079f4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f4b0) · [`0079f4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f4d4)

~~~diff
- 0079f46c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079f4ac ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079f46c bytes c82600d0
+ 0079f4ac bytes c82600f0
- 0079f470 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0079f470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f4b0 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0079f4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f470 bytes 08213c91
+ 0079f4b0 bytes 08210c91
- 0079f494 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f494 ["INT_ADD", "register:40f0:8", ["const:79f494:8", "const:4:8"]]
- 0079f494 ["CALLIND", null, ["register:0:8"]]
+ 0079f4d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f4d4 ["INT_ADD", "register:40f0:8", ["const:79f4d4:8", "const:4:8"]]
+ 0079f4d4 ["CALLIND", null, ["register:0:8"]]
- 0079f494 bytes 00013fd6
+ 0079f4d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-600c966674e03a1f45a8dd4db6a7bb5a"></a>

### [`0079f7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f7f4.md) → [`0079f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f834.md) FUN_0079f834

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
      "definition_site": "0079f840",
      "incomplete_value": false,
      "site": "0079f84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f800",
      "incomplete_value": false,
      "site": "0079f80c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0079f84c",
      "DATA",
      [
        "storage",
        "00c79f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f84c",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f7f4.md#insn-0079f7fc) · [`0079f800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f7f4.md#insn-0079f800)
- 新版 [`0079f83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f834.md#insn-0079f83c) · [`0079f840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f834.md#insn-0079f840)

~~~diff
- 0079f7fc ["COPY", "register:4050:8", ["const:c79000:8"]]
+ 0079f83c ["COPY", "register:4050:8", ["const:c7a000:8"]]
- 0079f7fc bytes ca2600d0
+ 0079f83c bytes ca2600f0
- 0079f800 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0079f800 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079f800 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079f800 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079f840 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0079f840 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079f840 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079f840 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079f800 bytes 4a213e91
+ 0079f840 bytes 4a210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a744cb15ac22be13a1d59ec6401a9d04"></a>

### [`0079f838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f838.md) → [`0079f878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md) FUN_0079f878

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
      "definition_site": "0079f890",
      "incomplete_value": false,
      "site": "0079f89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f850",
      "incomplete_value": false,
      "site": "0079f85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0079f89c",
      "DATA",
      [
        "storage",
        "00c79f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f89c",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f838.md#insn-0079f84c) · [`0079f850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f838.md#insn-0079f850) · [`0079f880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f838.md#insn-0079f880)
- 新版 [`0079f88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md#insn-0079f88c) · [`0079f890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md#insn-0079f890) · [`0079f8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md#insn-0079f8c0)

~~~diff
- 0079f84c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079f88c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079f84c bytes c82600d0
+ 0079f88c bytes c82600f0
- 0079f850 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0079f850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f890 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0079f890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f850 bytes 08213e91
+ 0079f890 bytes 08210e91
- 0079f880 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f880 ["INT_ADD", "register:40f0:8", ["const:79f880:8", "const:4:8"]]
- 0079f880 ["CALLIND", null, ["register:0:8"]]
+ 0079f8c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f8c0 ["INT_ADD", "register:40f0:8", ["const:79f8c0:8", "const:4:8"]]
+ 0079f8c0 ["CALLIND", null, ["register:0:8"]]
- 0079f880 bytes 00013fd6
+ 0079f8c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13b2a8e47626fd9ad72936299f73882d"></a>

### [`0079f894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f894.md) → [`0079f8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md) FUN_0079f8d4

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
      "definition_site": "0079f900",
      "incomplete_value": false,
      "site": "0079f900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f8c0",
      "incomplete_value": false,
      "site": "0079f8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0079f900",
      "DATA",
      [
        "storage",
        "00c79f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f900",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f894.md#insn-0079f8a8) · [`0079f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f894.md#insn-0079f8b4) · [`0079f8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f894.md#insn-0079f8b8)
- 新版 [`0079f8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f8e8) · [`0079f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f8f4) · [`0079f8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f8f8)

~~~diff
- 0079f8a8 ["INT_ADD", "register:40f0:8", ["const:79f8a8:8", "const:4:8"]]
- 0079f8a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079f8e8 ["INT_ADD", "register:40f0:8", ["const:79f8e8:8", "const:4:8"]]
+ 0079f8e8 ["CALL", null, ["callee:00c57e90:8"]]
- 0079f8a8 bytes 7ae01294
+ 0079f8e8 bytes 6ae11294
- 0079f8b4 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079f8f4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079f8b4 bytes c82600d0
+ 0079f8f4 bytes c82600f0
- 0079f8b8 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0079f8b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f8b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f8b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f8f8 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0079f8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f8b8 bytes 08213e91
+ 0079f8f8 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b962c689d3b97611e286b88c4fb0c552"></a>

### [`0079f91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f91c.md) → [`0079f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md) FUN_0079f95c

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
      "definition_site": "0079f978",
      "incomplete_value": false,
      "site": "0079f978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f938",
      "incomplete_value": false,
      "site": "0079f938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0079f978",
      "DATA",
      [
        "storage",
        "00c79f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f978",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f91c.md#insn-0079f930) · [`0079f934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f91c.md#insn-0079f934) · [`0079f958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079f91c.md#insn-0079f958)
- 新版 [`0079f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md#insn-0079f970) · [`0079f974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md#insn-0079f974) · [`0079f998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md#insn-0079f998)

~~~diff
- 0079f930 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079f970 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079f930 bytes c92600d0
+ 0079f970 bytes c92600f0
- 0079f934 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0079f934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079f934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079f934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079f974 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0079f974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079f934 bytes 29213e91
+ 0079f974 bytes 29210e91
- 0079f958 ["COPY", "register:0:8", ["register:4048:8"]]
- 0079f958 ["INT_ADD", "register:40f0:8", ["const:79f958:8", "const:4:8"]]
- 0079f958 ["CALLIND", null, ["register:0:8"]]
+ 0079f998 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079f998 ["INT_ADD", "register:40f0:8", ["const:79f998:8", "const:4:8"]]
+ 0079f998 ["CALLIND", null, ["register:0:8"]]
- 0079f958 bytes 20013fd6
+ 0079f998 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c160ec6515434f59f2d782a0992f5d"></a>

### [`0079fa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fa60.md) → [`0079faa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md) _INIT_142

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079fadc",
      "incomplete_value": true,
      "site": "0079faf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0079fa9c",
      "incomplete_value": true,
      "site": "0079fab8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079fcd0",
      "incomplete_value": false,
      "site": "0079fcd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079fc90",
      "incomplete_value": false,
      "site": "0079fc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "0079fadc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0079fb00",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0079fb20",
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
      "0079fadc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0079fb00",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0079fb20",
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

- 旧版 [`0079faf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fa60.md#insn-0079faf8) · [`0079fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fa60.md#insn-0079fc94) · [`0079fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079f/0079fa60.md#insn-0079fa8c)
- 新版 [`0079fb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079fb38) · [`0079fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079fcd4) · [`0079facc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079facc)

~~~diff
- 0079faf8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0079faf8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079faf8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079faf8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079fb38 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0079fb38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079fb38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079fb38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079faf8 bytes 4a553a91
+ 0079fb38 bytes 4a893d91
- 0079fc94 ["INT_ADD", "register:40f0:8", ["const:79fc94:8", "const:4:8"]]
- 0079fc94 ["CALL", null, ["callee:00c57e30:8"]]
+ 0079fcd4 ["INT_ADD", "register:40f0:8", ["const:79fcd4:8", "const:4:8"]]
+ 0079fcd4 ["CALL", null, ["callee:00c57e30:8"]]
- 0079fc94 bytes 67df1294
+ 0079fcd4 bytes 57e01294
- 0079fa8c ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0079fa8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0079fa8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0079fa8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0079facc ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0079facc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0079facc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0079facc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0079fa8c bytes 73e22c91
+ 0079facc bytes 73e23c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea710a32bdf1301fca4c57865e1f771f"></a>

### [`007a1a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1a70.md) → [`007a1ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md) FUN_007a1ab0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007a1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1890.md) [`007a1c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1c04.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`007a18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md) [`007a1c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "007a1abc",
      "incomplete_value": false,
      "site": "007a1ac0",
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
      "definition_site": "007a1a7c",
      "incomplete_value": false,
      "site": "007a1a80",
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
      "007a1abc",
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
      "007a1abc",
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

- 旧版 [`007a1a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1a70.md#insn-007a1a80) · [`007a1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a1a70.md#insn-007a1a7c)
- 新版 [`007a1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md#insn-007a1ac0) · [`007a1abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md#insn-007a1abc)

~~~diff
- 007a1a80 ["INT_ADD", "register:40f0:8", ["const:7a1a80:8", "const:4:8"]]
- 007a1a80 ["CALL", null, ["callee:0043b778:8"]]
+ 007a1ac0 ["INT_ADD", "register:40f0:8", ["const:7a1ac0:8", "const:4:8"]]
+ 007a1ac0 ["CALL", null, ["callee:0043b778:8"]]
- 007a1a80 bytes 2e67f297
+ 007a1ac0 bytes 2e67f297
- 007a1a7c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 007a1a7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007a1a7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007a1a7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007a1abc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 007a1abc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007a1abc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007a1abc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007a1a7c bytes 00303c91
+ 007a1abc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5628a3ccbe33be19e167cb5d9aba0126"></a>

### [`007aa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa3a8.md) → [`007aa3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md) _INIT_143

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aa424",
      "incomplete_value": true,
      "site": "007aa440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aa3e4",
      "incomplete_value": true,
      "site": "007aa400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aa448",
      "incomplete_value": true,
      "site": "007aa464",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aa408",
      "incomplete_value": true,
      "site": "007aa424",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aa468",
      "incomplete_value": true,
      "site": "007aa484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aa428",
      "incomplete_value": true,
      "site": "007aa444",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007aa424",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007aa448",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007aa468",
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
      "007aa424",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007aa448",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007aa468",
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

- 旧版 [`007aa420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa3a8.md#insn-007aa420) · [`007aa440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa3a8.md#insn-007aa440) · [`007aa508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa3a8.md#insn-007aa508)
- 新版 [`007aa460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa460) · [`007aa480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa480) · [`007aa548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa548)

~~~diff
- 007aa420 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007aa420 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aa420 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aa420 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aa460 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007aa460 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aa460 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aa460 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aa420 bytes 4a093691
+ 007aa460 bytes 4a093791
- 007aa440 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007aa440 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aa440 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aa440 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aa480 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 007aa480 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aa480 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aa480 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aa440 bytes 4a553a91
+ 007aa480 bytes 4a893d91
- 007aa508 ["INT_ADD", "register:40f0:8", ["const:7aa508:8", "const:4:8"]]
- 007aa508 ["CALL", null, ["callee:0043b7f8:8"]]
+ 007aa548 ["INT_ADD", "register:40f0:8", ["const:7aa548:8", "const:4:8"]]
+ 007aa548 ["CALL", null, ["callee:0043b7f8:8"]]
- 007aa508 bytes ac44f297
+ 007aa548 bytes ac44f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cca610760c53a3888dfb30838f9800a"></a>

### [`007aa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md) → [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) FUN_007aa808

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007ad808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`007aa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md) [`00aadd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00aadf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf8c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007aa9a8",
      "incomplete_value": false,
      "site": "007aa9ac",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aa968",
      "incomplete_value": false,
      "site": "007aa96c",
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
            "const:f0:8"
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
      "007aa868",
      "READ",
      [
        "storage",
        "00ca7b80",
        null,
        "undefined1"
      ]
    ],
    [
      "007aa86c",
      "READ",
      [
        "storage",
        "00ca7b88",
        null,
        "undefined8"
      ]
    ],
    [
      "007aa86c",
      "READ",
      [
        "storage",
        "00ca7b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007aa868",
      "READ",
      [
        "storage",
        "00ca7f80",
        null,
        "undefined1"
      ]
    ],
    [
      "007aa86c",
      "READ",
      [
        "storage",
        "00ca7f88",
        null,
        "undefined8"
      ]
    ],
    [
      "007aa86c",
      "READ",
      [
        "storage",
        "00ca7f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aa92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md#insn-007aa92c) · [`007aa96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md#insn-007aa96c) · [`007aa80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md#insn-007aa80c)
- 新版 [`007aa96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa96c) · [`007aa9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa9ac) · [`007aa84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa84c)

~~~diff
- 007aa92c ["INT_ADD", "register:40f0:8", ["const:7aa92c:8", "const:4:8"]]
- 007aa92c ["CALL", null, ["callee:00c58050:8"]]
+ 007aa96c ["INT_ADD", "register:40f0:8", ["const:7aa96c:8", "const:4:8"]]
+ 007aa96c ["CALL", null, ["callee:00c58050:8"]]
- 007aa92c bytes c9b41294
+ 007aa96c bytes b9b51294
- 007aa96c ["INT_ADD", "register:40f0:8", ["const:7aa96c:8", "const:4:8"]]
- 007aa96c ["CALL", null, ["callee:00442930:8"]]
+ 007aa9ac ["INT_ADD", "register:40f0:8", ["const:7aa9ac:8", "const:4:8"]]
+ 007aa9ac ["CALL", null, ["callee:00442930:8"]]
- 007aa96c bytes e15ff297
+ 007aa9ac bytes e15ff297
- 007aa80c ["INT_ADD", "register:40f0:8", ["const:7aa80c:8", "const:4:8"]]
- 007aa80c ["CALL", null, ["callee:007aaa28:8"]]
+ 007aa84c ["INT_ADD", "register:40f0:8", ["const:7aa84c:8", "const:4:8"]]
+ 007aa84c ["CALL", null, ["callee:007aaa28:8"]]
- 007aa80c bytes 77000094
+ 007aa84c bytes 77000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8edc49379d5b3d0a706b5b23fd7363f3"></a>

### [`007aa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md) → [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) FUN_007aaa28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007aa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md) [`007aacc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 2件 [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007aaa5c",
      "incomplete_value": false,
      "site": "007aaa60",
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
      "definition_site": "007aaa1c",
      "incomplete_value": false,
      "site": "007aaa20",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aaba0",
      "incomplete_value": true,
      "site": "007aaba4",
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
      "definition_site": "007aab60",
      "incomplete_value": true,
      "site": "007aab64",
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
      "definition_site": "007aab9c",
      "incomplete_value": true,
      "site": "007aaba8",
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
      "definition_site": "007aab5c",
      "incomplete_value": true,
      "site": "007aab68",
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
      "007aaa60",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "007aaa68",
      "PARAM",
      [
        "storage",
        "00ca7bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "007aaaa0",
      "PARAM",
      [
        "storage",
        "00ca7ba0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007aaa60",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "007aaa68",
      "PARAM",
      [
        "storage",
        "00ca7fb8",
        null,
        "undefined1"
      ]
    ],
    [
      "007aaaa0",
      "PARAM",
      [
        "storage",
        "00ca7fa0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aaa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md#insn-007aaa30) · [`007aaa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md#insn-007aaa60) · [`007aaa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md#insn-007aaa6c)
- 新版 [`007aaa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaa70) · [`007aaaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaaa0) · [`007aaaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaaac)

~~~diff
- 007aaa30 ["INT_ADD", "register:40f0:8", ["const:7aaa30:8", "const:4:8"]]
- 007aaa30 ["CALL", null, ["callee:0048ce54:8"]]
+ 007aaa70 ["INT_ADD", "register:40f0:8", ["const:7aaa70:8", "const:4:8"]]
+ 007aaa70 ["CALL", null, ["callee:0048ce54:8"]]
- 007aaa30 bytes f988f397
+ 007aaa70 bytes f988f397
- 007aaa60 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 007aaa60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007aaa60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007aaa60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007aaaa0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 007aaaa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007aaaa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007aaaa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007aaa60 bytes 00802e91
+ 007aaaa0 bytes 00803e91
- 007aaa6c ["INT_ADD", "register:40f0:8", ["const:7aaa6c:8", "const:4:8"]]
- 007aaa6c ["CALL", null, ["callee:00492e08:8"]]
+ 007aaaac ["INT_ADD", "register:40f0:8", ["const:7aaaac:8", "const:4:8"]]
+ 007aaaac ["CALL", null, ["callee:00492e08:8"]]
- 007aaa6c bytes d7a0f397
+ 007aaaac bytes d7a0f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d8b29332ec6aaa513eac48ac2683cc"></a>

### [`007aacc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md) → [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) FUN_007aad04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007aefb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb8.md) · 呼出先 8件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`007aa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa9e8.md) [`00aadd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`007aeff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md) · 呼出先 8件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00aadf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007aae54",
      "incomplete_value": false,
      "site": "007aae58",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aae14",
      "incomplete_value": false,
      "site": "007aae18",
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
            "const:f0:8"
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
      "007aad74",
      "PARAM",
      [
        "storage",
        "002bb784",
        null,
        "string"
      ]
    ],
    [
      "007aad80",
      "PARAM",
      [
        "storage",
        "002ab8ee",
        null,
        "string"
      ]
    ],
    [
      "007aae54",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007aad74",
      "PARAM",
      [
        "storage",
        "002bb7c4",
        null,
        "string"
      ]
    ],
    [
      "007aad80",
      "PARAM",
      [
        "storage",
        "002ab92e",
        null,
        "string"
      ]
    ],
    [
      "007aae54",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aadd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md#insn-007aadd8) · [`007aae18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md#insn-007aae18) · [`007aad0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md#insn-007aad0c)
- 新版 [`007aae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aae18) · [`007aae58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aae58) · [`007aad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aad4c)

~~~diff
- 007aadd8 ["INT_ADD", "register:40f0:8", ["const:7aadd8:8", "const:4:8"]]
- 007aadd8 ["CALL", null, ["callee:00c58050:8"]]
+ 007aae18 ["INT_ADD", "register:40f0:8", ["const:7aae18:8", "const:4:8"]]
+ 007aae18 ["CALL", null, ["callee:00c58050:8"]]
- 007aadd8 bytes 9eb31294
+ 007aae18 bytes 8eb41294
- 007aae18 ["INT_ADD", "register:40f0:8", ["const:7aae18:8", "const:4:8"]]
- 007aae18 ["CALL", null, ["callee:00442930:8"]]
+ 007aae58 ["INT_ADD", "register:40f0:8", ["const:7aae58:8", "const:4:8"]]
+ 007aae58 ["CALL", null, ["callee:00442930:8"]]
- 007aae18 bytes b65ef297
+ 007aae58 bytes b65ef297
- 007aad0c ["INT_ADD", "register:40f0:8", ["const:7aad0c:8", "const:4:8"]]
- 007aad0c ["CALL", null, ["callee:007aaa28:8"]]
+ 007aad4c ["INT_ADD", "register:40f0:8", ["const:7aad4c:8", "const:4:8"]]
+ 007aad4c ["CALL", null, ["callee:007aaa28:8"]]
- 007aad0c bytes 37ffff97
+ 007aad4c bytes 37ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ed3b55ec8aef2fcf7c296eda40bfd6"></a>

### [`007aaeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aaeb4.md) → [`007aaef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md) _INIT_144

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 74.77% / 新版 74.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 11件, `store_value` 11件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aaf30",
      "incomplete_value": true,
      "site": "007aaf4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aaef0",
      "incomplete_value": true,
      "site": "007aaf0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aaf54",
      "incomplete_value": true,
      "site": "007aaf70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aaf14",
      "incomplete_value": true,
      "site": "007aaf30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aaf74",
      "incomplete_value": true,
      "site": "007aaf90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007aaf34",
      "incomplete_value": true,
      "site": "007aaf50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007aaf30",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007aaf54",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007aaf74",
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
      "007aaf30",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007aaf54",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007aaf74",
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

- 旧版 [`007aaf2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aaeb4.md#insn-007aaf2c) · [`007aaf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aaeb4.md#insn-007aaf4c) · [`007ab014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aaeb4.md#insn-007ab014)
- 新版 [`007aaf6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007aaf6c) · [`007aaf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007aaf8c) · [`007ab054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007ab054)

~~~diff
- 007aaf2c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007aaf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aaf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aaf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aaf6c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007aaf6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aaf6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aaf6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aaf2c bytes 4a093691
+ 007aaf6c bytes 4a093791
- 007aaf4c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007aaf4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aaf4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aaf4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aaf8c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 007aaf8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aaf8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aaf8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aaf4c bytes 4a553a91
+ 007aaf8c bytes 4a893d91
- 007ab014 ["INT_ADD", "register:40f0:8", ["const:7ab014:8", "const:4:8"]]
- 007ab014 ["CALL", null, ["callee:0043b7f8:8"]]
+ 007ab054 ["INT_ADD", "register:40f0:8", ["const:7ab054:8", "const:4:8"]]
+ 007ab054 ["CALL", null, ["callee:0043b7f8:8"]]
- 007ab014 bytes e941f297
+ 007ab054 bytes e941f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054a9cffc76da838591e37190e0854c0"></a>

### [`007ab3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md) → [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) FUN_007ab404

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00931028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931028.md) · 呼出先 6件 [`007ab714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md) [`007ae734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae734.md) [`007ae80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae80c.md) [`007ae810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae810.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009311c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009311c4.md) · 呼出先 6件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) [`007ae774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae774.md) [`007ae84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae84c.md) [`007ae850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae850.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab4e4",
      "incomplete_value": false,
      "site": "007ab4e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab4a4",
      "incomplete_value": false,
      "site": "007ab4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "definition_site": "007ab534",
      "incomplete_value": false,
      "site": "007ab534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab4f4",
      "incomplete_value": false,
      "site": "007ab4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "007ab4e8",
      "DATA",
      [
        "storage",
        "00c7a008",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab534",
      "DATA",
      [
        "storage",
        "00c7a098",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab570",
      "READ",
      [
        "storage",
        "00c7a0b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ab4e8",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab534",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab570",
      "READ",
      [
        "storage",
        "00c7a4b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md#insn-007ab534) · [`007ab41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md#insn-007ab41c) · [`007ab454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md#insn-007ab454)
- 新版 [`007ab574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab574) · [`007ab45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab45c) · [`007ab494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab494)

~~~diff
- 007ab534 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab534 ["INT_ADD", "register:40f0:8", ["const:7ab534:8", "const:4:8"]]
- 007ab534 ["CALLIND", null, ["register:0:8"]]
+ 007ab574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab574 ["INT_ADD", "register:40f0:8", ["const:7ab574:8", "const:4:8"]]
+ 007ab574 ["CALLIND", null, ["register:0:8"]]
- 007ab534 bytes 00013fd6
+ 007ab574 bytes 00013fd6
- 007ab41c ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab41c ["INT_ADD", "register:40f0:8", ["const:7ab41c:8", "const:4:8"]]
- 007ab41c ["CALLIND", null, ["register:0:8"]]
+ 007ab45c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab45c ["INT_ADD", "register:40f0:8", ["const:7ab45c:8", "const:4:8"]]
+ 007ab45c ["CALLIND", null, ["register:0:8"]]
- 007ab41c bytes 00013fd6
+ 007ab45c bytes 00013fd6
- 007ab454 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab454 ["INT_ADD", "register:40f0:8", ["const:7ab454:8", "const:4:8"]]
- 007ab454 ["CALLIND", null, ["register:0:8"]]
+ 007ab494 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab494 ["INT_ADD", "register:40f0:8", ["const:7ab494:8", "const:4:8"]]
+ 007ab494 ["CALLIND", null, ["register:0:8"]]
- 007ab454 bytes 00013fd6
+ 007ab494 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c96551b34af7ec7b845dd5e382c1b8e"></a>

### [`007ab714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md) → [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) FUN_007ab754

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab3c4.md) · 呼出先 14件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md) [`00795e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795e1c.md)
- 新版 呼出元 1件 [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) · 呼出先 14件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab7a8",
      "incomplete_value": false,
      "site": "007ab7ac",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:c88:8"
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
      "definition_site": "007ab768",
      "incomplete_value": false,
      "site": "007ab76c",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:888:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab7d8",
      "incomplete_value": false,
      "site": "007ab7dc",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "007ab798",
      "incomplete_value": false,
      "site": "007ab79c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab868",
      "incomplete_value": false,
      "site": "007ab868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab828",
      "incomplete_value": false,
      "site": "007ab828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007ab7ac",
      "DATA",
      [
        "storage",
        "00c6e898",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab7dc",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab868",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ab7ac",
      "DATA",
      [
        "storage",
        "00c6ec98",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab7dc",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab868",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md#insn-007ab740) · [`007ab758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md#insn-007ab758) · [`007ab760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md#insn-007ab760)
- 新版 [`007ab780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab780) · [`007ab798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab798) · [`007ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab7a0)

~~~diff
- 007ab740 ["INT_ADD", "register:40f0:8", ["const:7ab740:8", "const:4:8"]]
- 007ab740 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ab780 ["INT_ADD", "register:40f0:8", ["const:7ab780:8", "const:4:8"]]
+ 007ab780 ["CALL", null, ["callee:00c57e90:8"]]
- 007ab740 bytes d4b01294
+ 007ab780 bytes c4b11294
- 007ab758 ["INT_ADD", "register:40f0:8", ["const:7ab758:8", "const:4:8"]]
- 007ab758 ["CALL", null, ["callee:0059b908:8"]]
+ 007ab798 ["INT_ADD", "register:40f0:8", ["const:7ab798:8", "const:4:8"]]
+ 007ab798 ["CALL", null, ["callee:0059b908:8"]]
- 007ab758 bytes 5cc0f797
+ 007ab798 bytes 5cc0f797
- 007ab760 ["COPY", "tmp:0:8", ["const:888:8"]]
- 007ab760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ab760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ab760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ab7a0 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 007ab7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ab7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ab7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ab760 bytes 08212291
+ 007ab7a0 bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f3de347b747f146808a6a062f7e28a"></a>

### [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) → [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) FUN_007abc24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ae784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae784.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 1件 [`007ae7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae7c4.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007abc70",
      "incomplete_value": false,
      "site": "007abc80",
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
      "definition_site": "007abc30",
      "incomplete_value": false,
      "site": "007abc40",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007abcd0",
      "incomplete_value": true,
      "site": "007abcd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abc90",
      "incomplete_value": true,
      "site": "007abc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
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
      "definition_site": "007abd94",
      "incomplete_value": true,
      "site": "007abd94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abd54",
      "incomplete_value": true,
      "site": "007abd54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3cf:8"
              ]
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
      "007abc80",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "007abcbc",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ],
    [
      "007abd78",
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
      "007abc80",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "007abcbc",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "007abd78",
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

- 旧版 [`007abe18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md#insn-007abe18) · [`007abfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md#insn-007abfc8) · [`007abc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md#insn-007abc24)
- 新版 [`007abe58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007abe58) · [`007ac008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007ac008) · [`007abc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007abc64)

~~~diff
- 007abe18 ["INT_ADD", "register:40f0:8", ["const:7abe18:8", "const:4:8"]]
- 007abe18 ["CALL", null, ["callee:0045982c:8"]]
+ 007abe58 ["INT_ADD", "register:40f0:8", ["const:7abe58:8", "const:4:8"]]
+ 007abe58 ["CALL", null, ["callee:0045982c:8"]]
- 007abe18 bytes 75b6f297
+ 007abe58 bytes 75b6f297
- 007abfc8 ["INT_ADD", "register:40f0:8", ["const:7abfc8:8", "const:4:8"]]
- 007abfc8 ["CALL", null, ["callee:0045982c:8"]]
+ 007ac008 ["INT_ADD", "register:40f0:8", ["const:7ac008:8", "const:4:8"]]
+ 007ac008 ["CALL", null, ["callee:0045982c:8"]]
- 007abfc8 bytes 09b6f297
+ 007ac008 bytes 09b6f297
- 007abc24 ["INT_ADD", "register:40f0:8", ["const:7abc24:8", "const:4:8"]]
- 007abc24 ["CALL", null, ["callee:00c57e90:8"]]
+ 007abc64 ["INT_ADD", "register:40f0:8", ["const:7abc64:8", "const:4:8"]]
+ 007abc64 ["CALL", null, ["callee:00c57e90:8"]]
- 007abc24 bytes 9baf1294
+ 007abc64 bytes 8bb01294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22f2e4577dffdb8991ed2197871d28f"></a>

### [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) → [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) FUN_007ac3c0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md)
- 新版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac410",
      "incomplete_value": true,
      "site": "007ac410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac3d0",
      "incomplete_value": true,
      "site": "007ac3d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
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
      "definition_site": "007ac4f4",
      "incomplete_value": true,
      "site": "007ac4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac4b4",
      "incomplete_value": true,
      "site": "007ac4b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:412:8"
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
      "definition_site": "007ac4e8",
      "incomplete_value": true,
      "site": "007ac4f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ac4a8",
      "incomplete_value": true,
      "site": "007ac4b8",
      "value": [
        "LOAD",
        "8",
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
      "007ac3ec",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ],
    [
      "007ac43c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "007ac450",
      "READ",
      [
        "storage",
        "002c12ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ac3ec",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "007ac43c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ac450",
      "READ",
      [
        "storage",
        "002c12fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md#insn-007ac3fc) · [`007ac43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md#insn-007ac43c) · [`007ac5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md#insn-007ac5d8)
- 新版 [`007ac43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac43c) · [`007ac47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac47c) · [`007ac618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac618)

~~~diff
- 007ac3fc ["INT_ADD", "register:40f0:8", ["const:7ac3fc:8", "const:4:8"]]
- 007ac3fc ["CALL", null, ["ram:48ccb8:8"]]
+ 007ac43c ["INT_ADD", "register:40f0:8", ["const:7ac43c:8", "const:4:8"]]
+ 007ac43c ["CALL", null, ["ram:48ccf8:8"]]
- 007ac3fc bytes 2f82f397
+ 007ac43c bytes 2f82f397
- 007ac43c ["INT_ADD", "register:40f0:8", ["const:7ac43c:8", "const:4:8"]]
- 007ac43c ["CALL", null, ["callee:00493690:8"]]
+ 007ac47c ["INT_ADD", "register:40f0:8", ["const:7ac47c:8", "const:4:8"]]
+ 007ac47c ["CALL", null, ["callee:00493690:8"]]
- 007ac43c bytes 859cf397
+ 007ac47c bytes 859cf397
- 007ac5d8 ["INT_ADD", "register:40f0:8", ["const:7ac5d8:8", "const:4:8"]]
- 007ac5d8 ["CALL", null, ["ram:48ccb8:8"]]
+ 007ac618 ["INT_ADD", "register:40f0:8", ["const:7ac618:8", "const:4:8"]]
+ 007ac618 ["CALL", null, ["ram:48ccf8:8"]]
- 007ac5d8 bytes b881f397
+ 007ac618 bytes b881f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aa40c5c0bb351480a032f011f57c106"></a>

### [`007ac6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac6a0.md) → [`007ac6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md) FUN_007ac6e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) · 呼出先 6件 [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) [`007aebfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebfc.md) [`007aec00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec00.md) [`007aec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec80.md) [`007aec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec84.md)
- 新版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 6件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) [`007aec3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec3c.md) [`007aec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec40.md) [`007aecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc0.md) [`007aecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac708",
      "incomplete_value": false,
      "site": "007ac708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac6c8",
      "incomplete_value": false,
      "site": "007ac6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "definition_site": "007ac71c",
      "incomplete_value": false,
      "site": "007ac71c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac6dc",
      "incomplete_value": false,
      "site": "007ac6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "007ac708",
      "DATA",
      [
        "storage",
        "00c7a198",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac71c",
      "DATA",
      [
        "storage",
        "00c7a218",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac754",
      "READ",
      [
        "storage",
        "00c7a238",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ac708",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac71c",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac754",
      "READ",
      [
        "storage",
        "00c7a638",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac6a0.md#insn-007ac6c4) · [`007ac6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac6a0.md#insn-007ac6d8) · [`007ac6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac6a0.md#insn-007ac6ec)
- 新版 [`007ac704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac704) · [`007ac718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac718) · [`007ac72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac72c)

~~~diff
- 007ac6c4 ["COPY", "tmp:0:8", ["const:198:8"]]
- 007ac6c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ac6c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ac6c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ac704 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 007ac704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ac6c4 bytes 08610691
+ 007ac704 bytes 08611691
- 007ac6d8 ["COPY", "tmp:0:8", ["const:218:8"]]
- 007ac6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ac6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ac6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ac718 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 007ac718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ac6d8 bytes 08610891
+ 007ac718 bytes 08611891
- 007ac6ec ["INT_ADD", "register:40f0:8", ["const:7ac6ec:8", "const:4:8"]]
- 007ac6ec ["CALL", null, ["callee:007ad324:8"]]
+ 007ac72c ["INT_ADD", "register:40f0:8", ["const:7ac72c:8", "const:4:8"]]
+ 007ac72c ["CALL", null, ["callee:007ad324:8"]]
- 007ac6ec bytes fe020094
+ 007ac72c bytes fe020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a76d31fbc4cf7057e107cc4db310ae"></a>

### [`007ac7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac7ec.md) → [`007ac82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md) FUN_007ac82c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00597618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597618.md)
- 新版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00597658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597658.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac84c",
      "incomplete_value": true,
      "site": "007ac864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:85:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac80c",
      "incomplete_value": true,
      "site": "007ac824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:45:8"
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
      "definition_site": "007ac868",
      "incomplete_value": true,
      "site": "007ac868",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ac828",
      "incomplete_value": true,
      "site": "007ac828",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ac84c",
      "READ",
      [
        "storage",
        "002b4045",
        null,
        "string"
      ]
    ],
    [
      "007ac85c",
      "READ",
      [
        "storage",
        "002b4053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ac84c",
      "READ",
      [
        "storage",
        "002b4085",
        null,
        "string"
      ]
    ],
    [
      "007ac85c",
      "READ",
      [
        "storage",
        "002b4093",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac7ec.md#insn-007ac804) · [`007ac838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac7ec.md#insn-007ac838) · [`007ac860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac7ec.md#insn-007ac860)
- 新版 [`007ac844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac844) · [`007ac878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac878) · [`007ac8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac8a0)

~~~diff
- 007ac804 ["COPY", "tmp:0:8", ["const:45:8"]]
- 007ac804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ac804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ac804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ac844 ["COPY", "tmp:0:8", ["const:85:8"]]
+ 007ac844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ac844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ac844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ac804 bytes 29150191
+ 007ac844 bytes 29150291
- 007ac838 ["INT_ADD", "register:40f0:8", ["const:7ac838:8", "const:4:8"]]
- 007ac838 ["CALL", null, ["callee:0048ce54:8"]]
+ 007ac878 ["INT_ADD", "register:40f0:8", ["const:7ac878:8", "const:4:8"]]
+ 007ac878 ["CALL", null, ["callee:0048ce54:8"]]
- 007ac838 bytes 7781f397
+ 007ac878 bytes 7781f397
- 007ac860 ["INT_ADD", "register:40f0:8", ["const:7ac860:8", "const:4:8"]]
- 007ac860 ["CALL", null, ["callee:0043bb20:8"]]
+ 007ac8a0 ["INT_ADD", "register:40f0:8", ["const:7ac8a0:8", "const:4:8"]]
+ 007ac8a0 ["CALL", null, ["callee:0043bb20:8"]]
- 007ac860 bytes a03cf297
+ 007ac8a0 bytes a03cf297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4984cbd041ede0e0a700b053d4b5adb"></a>

### [`007aca8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) → [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) FUN_007acacc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) · 呼出先 17件 [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md)
- 新版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 17件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007acb18",
      "incomplete_value": false,
      "site": "007acb1c",
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
      "definition_site": "007acad8",
      "incomplete_value": false,
      "site": "007acadc",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007acb68",
      "incomplete_value": true,
      "site": "007acb7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:34e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007acb28",
      "incomplete_value": true,
      "site": "007acb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:30e:8"
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
      "definition_site": "007acb80",
      "incomplete_value": true,
      "site": "007acb80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007acb40",
      "incomplete_value": true,
      "site": "007acb40",
      "value": [
        "LOAD",
        "8",
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
      "007acb1c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "007acb68",
      "READ",
      [
        "storage",
        "002c030e",
        null,
        "string"
      ]
    ],
    [
      "007acb78",
      "READ",
      [
        "storage",
        "002c031c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007acb1c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "007acb68",
      "READ",
      [
        "storage",
        "002c034e",
        null,
        "string"
      ]
    ],
    [
      "007acb78",
      "READ",
      [
        "storage",
        "002c035c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007acb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md#insn-007acb7c) · [`007acdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md#insn-007acdb4) · [`007acac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md#insn-007acac0)
- 新版 [`007acbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acbbc) · [`007acdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acdf4) · [`007acb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acb00)

~~~diff
- 007acb7c ["INT_ADD", "register:40f0:8", ["const:7acb7c:8", "const:4:8"]]
- 007acb7c ["CALL", null, ["callee:00748fb8:8"]]
+ 007acbbc ["INT_ADD", "register:40f0:8", ["const:7acbbc:8", "const:4:8"]]
+ 007acbbc ["CALL", null, ["callee:00748fb8:8"]]
- 007acb7c bytes ff70fe97
+ 007acbbc bytes ff70fe97
- 007acdb4 ["INT_ADD", "register:40f0:8", ["const:7acdb4:8", "const:4:8"]]
- 007acdb4 ["CALL", null, ["callee:00c581f0:8"]]
+ 007acdf4 ["INT_ADD", "register:40f0:8", ["const:7acdf4:8", "const:4:8"]]
+ 007acdf4 ["CALL", null, ["callee:00c581f0:8"]]
- 007acdb4 bytes 0fac1294
+ 007acdf4 bytes ffac1294
- 007acac0 ["INT_ADD", "register:40f0:8", ["const:7acac0:8", "const:4:8"]]
- 007acac0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007acb00 ["INT_ADD", "register:40f0:8", ["const:7acb00:8", "const:4:8"]]
+ 007acb00 ["CALL", null, ["callee:00c57e90:8"]]
- 007acac0 bytes f4ab1294
+ 007acb00 bytes e4ac1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d4a704ebb1236a1f20f9881487e2354"></a>

### [`007ad0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad0c4.md) → [`007ad104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md) FUN_007ad104

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 10件 [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00b0e50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)
- 新版 呼出元 1件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 10件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00b0e934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad154",
      "incomplete_value": true,
      "site": "007ad158",
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
      "definition_site": "007ad114",
      "incomplete_value": true,
      "site": "007ad118",
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
      "definition_site": "007ad150",
      "incomplete_value": true,
      "site": "007ad15c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ad110",
      "incomplete_value": true,
      "site": "007ad11c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ad164",
      "incomplete_value": true,
      "site": "007ad164",
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
                "const:30:8"
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
      "definition_site": "007ad124",
      "incomplete_value": true,
      "site": "007ad124",
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
                "const:30:8"
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
      "007ad140",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "007ad144",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "007ad150",
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
      "007ad140",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "007ad144",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "007ad150",
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

- 旧版 [`007ad15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad0c4.md#insn-007ad15c) · [`007ad100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad0c4.md#insn-007ad100) · [`007ad104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad0c4.md#insn-007ad104)
- 新版 [`007ad19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad19c) · [`007ad140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad140) · [`007ad144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad144)

~~~diff
- 007ad15c ["INT_ADD", "register:40f0:8", ["const:7ad15c:8", "const:4:8"]]
- 007ad15c ["CALL", null, ["callee:00c581f0:8"]]
+ 007ad19c ["INT_ADD", "register:40f0:8", ["const:7ad19c:8", "const:4:8"]]
+ 007ad19c ["CALL", null, ["callee:00c581f0:8"]]
- 007ad15c bytes 25ab1294
+ 007ad19c bytes 15ac1294
- 007ad100 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:888:8"]]
- 007ad100 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ad140 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c88:8"]]
+ 007ad140 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 007ad100 bytes 184744f9
+ 007ad140 bytes 184746f9
- 007ad104 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:7b8:8"]]
- 007ad104 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ad144 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:bb8:8"]]
+ 007ad144 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 007ad104 bytes f7de43f9
+ 007ad144 bytes f7de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055e7e183185286a0fcdb02c36d0e850"></a>

### [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) → [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) FUN_007ad324

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ac6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac6a0.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005a597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a5/005a597c.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 1件 [`007ac6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a59bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.08% / 新版 97.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad3e0",
      "incomplete_value": false,
      "site": "007ad3e4",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "007ad3a0",
      "incomplete_value": false,
      "site": "007ad3a4",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad470",
      "incomplete_value": false,
      "site": "007ad470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad430",
      "incomplete_value": false,
      "site": "007ad430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad580",
      "incomplete_value": false,
      "site": "007ad580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad540",
      "incomplete_value": false,
      "site": "007ad540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "007ad3e4",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad470",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad4e4",
      "READ",
      [
        "storage",
        "00c7a5c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ad3e4",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad470",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad4e4",
      "READ",
      [
        "storage",
        "00c7a9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ad364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md#insn-007ad364) · [`007ad318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md#insn-007ad318) · [`007ad344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md#insn-007ad344)
- 新版 [`007ad3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad3a4) · [`007ad358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad358) · [`007ad384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad384)

~~~diff
- 007ad364 ["INT_ADD", "register:40f0:8", ["const:7ad364:8", "const:4:8"]]
- 007ad364 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ad3a4 ["INT_ADD", "register:40f0:8", ["const:7ad3a4:8", "const:4:8"]]
+ 007ad3a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ad364 bytes d3a91294
+ 007ad3a4 bytes c3aa1294
- 007ad318 ["INT_ADD", "register:40f0:8", ["const:7ad318:8", "const:4:8"]]
- 007ad318 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ad358 ["INT_ADD", "register:40f0:8", ["const:7ad358:8", "const:4:8"]]
+ 007ad358 ["CALL", null, ["callee:00c57e90:8"]]
- 007ad318 bytes dea91294
+ 007ad358 bytes ceaa1294
- 007ad344 ["INT_ADD", "register:40f0:8", ["const:7ad344:8", "const:4:8"]]
- 007ad344 ["CALL", null, ["callee:0043bb20:8"]]
+ 007ad384 ["INT_ADD", "register:40f0:8", ["const:7ad384:8", "const:4:8"]]
+ 007ad384 ["CALL", null, ["callee:0043bb20:8"]]
- 007ad344 bytes e739f297
+ 007ad384 bytes e739f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df18b1598c45f3ab58b29a5f8a32595"></a>

### [`007ad808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md) → [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) FUN_007ad848

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007aec04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec04.md) · 呼出先 10件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`007aa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aa7c8.md) [`007aecf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf0.md)
- 新版 呼出元 1件 [`007aec44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec44.md) · 呼出先 10件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) [`007aed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed30.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad8b4",
      "incomplete_value": false,
      "site": "007ad8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad874",
      "incomplete_value": false,
      "site": "007ad87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad890",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad850",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad8ac",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad86c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ad890",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "007ad8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "007ad8bc",
      "DATA",
      [
        "storage",
        "00c7a298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ad890",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "007ad8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ad8bc",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ad850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md#insn-007ad850) · [`007ad86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md#insn-007ad86c) · [`007ad844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad808.md#insn-007ad844)
- 新版 [`007ad890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad890) · [`007ad8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad8ac) · [`007ad884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad884)

~~~diff
- 007ad850 ["INT_ADD", "register:40f0:8", ["const:7ad850:8", "const:4:8"]]
- 007ad850 ["CALL", null, ["ram:764344:8"]]
+ 007ad890 ["INT_ADD", "register:40f0:8", ["const:7ad890:8", "const:4:8"]]
+ 007ad890 ["CALL", null, ["ram:764384:8"]]
- 007ad850 bytes bddafe97
+ 007ad890 bytes bddafe97
- 007ad86c ["INT_ADD", "register:40f0:8", ["const:7ad86c:8", "const:4:8"]]
- 007ad86c ["CALL", null, ["ram:48ccb8:8"]]
+ 007ad8ac ["INT_ADD", "register:40f0:8", ["const:7ad8ac:8", "const:4:8"]]
+ 007ad8ac ["CALL", null, ["ram:48ccf8:8"]]
- 007ad86c bytes 137df397
+ 007ad8ac bytes 137df397
- 007ad844 ["INT_ADD", "register:40f0:8", ["const:7ad844:8", "const:4:8"]]
- 007ad844 ["CALL", null, ["callee:00aa3e24:8"]]
+ 007ad884 ["INT_ADD", "register:40f0:8", ["const:7ad884:8", "const:4:8"]]
+ 007ad884 ["CALL", null, ["callee:00aa3e24:8"]]
- 007ad844 bytes f9d80b94
+ 007ad884 bytes 68d90b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-868287f723e37f81b813bbb7285cfd71"></a>

### [`007ad944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md) → [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) FUN_007ad984

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007aec88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec88.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md)
- 新版 呼出元 1件 [`007aecc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc8.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007adb58",
      "incomplete_value": false,
      "site": "007adb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007adb18",
      "incomplete_value": false,
      "site": "007adb20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007adae4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007adaa4",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ad9cc",
      "PARAM",
      [
        "storage",
        "002b9394",
        null,
        "string"
      ]
    ],
    [
      "007ad9f0",
      "PARAM",
      [
        "storage",
        "002b854a",
        null,
        "string"
      ]
    ],
    [
      "007ad9fc",
      "PARAM",
      [
        "storage",
        "002b7729",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ad9cc",
      "PARAM",
      [
        "storage",
        "002b93d4",
        null,
        "string"
      ]
    ],
    [
      "007ad9f0",
      "PARAM",
      [
        "storage",
        "002b858a",
        null,
        "string"
      ]
    ],
    [
      "007ad9fc",
      "PARAM",
      [
        "storage",
        "002b7769",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007adaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md#insn-007adaa4) · [`007ad98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md#insn-007ad98c) · [`007ad9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad944.md#insn-007ad9b0)
- 新版 [`007adae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007adae4) · [`007ad9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007ad9cc) · [`007ad9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007ad9f0)

~~~diff
- 007adaa4 ["INT_ADD", "register:40f0:8", ["const:7adaa4:8", "const:4:8"]]
- 007adaa4 ["CALL", null, ["ram:48ccb8:8"]]
+ 007adae4 ["INT_ADD", "register:40f0:8", ["const:7adae4:8", "const:4:8"]]
+ 007adae4 ["CALL", null, ["ram:48ccf8:8"]]
- 007adaa4 bytes 857cf397
+ 007adae4 bytes 857cf397
- 007ad98c ["COPY", "tmp:0:8", ["const:394:8"]]
- 007ad98c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ad98c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ad98c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ad9cc ["COPY", "tmp:0:8", ["const:3d4:8"]]
+ 007ad9cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ad9cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ad9cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ad98c bytes 21500e91
+ 007ad9cc bytes 21500f91
- 007ad9b0 ["COPY", "tmp:0:8", ["const:54a:8"]]
- 007ad9b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ad9b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ad9b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ad9f0 ["COPY", "tmp:0:8", ["const:58a:8"]]
+ 007ad9f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ad9f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ad9f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ad9b0 bytes 21281591
+ 007ad9f0 bytes 21281691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3091c2b1d08a36baa44b709a1b6f3c2"></a>

### [`007add18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md) → [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) FUN_007add58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0081d1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d1ac.md) · 呼出先 8件 [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) [`007aefb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb0.md) [`007aefb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb4.md) [`007af0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0bc.md) [`007af0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0c0.md)
- 新版 呼出元 1件 [`0081d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md) · 呼出先 8件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) [`007aeff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff0.md) [`007aeff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff4.md) [`007af0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0fc.md) [`007af100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af100.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007addc0",
      "incomplete_value": false,
      "site": "007addc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007add80",
      "incomplete_value": false,
      "site": "007add80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007addd4",
      "incomplete_value": false,
      "site": "007adddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007add94",
      "incomplete_value": false,
      "site": "007add9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "007add9c",
      "PARAM",
      [
        "storage",
        "002a03f8",
        null,
        "string"
      ]
    ],
    [
      "007adda8",
      "PARAM",
      [
        "storage",
        "002b8542",
        null,
        "string"
      ]
    ],
    [
      "007addc0",
      "DATA",
      [
        "storage",
        "00c7a398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007add9c",
      "PARAM",
      [
        "storage",
        "002a04c5",
        null,
        "string"
      ]
    ],
    [
      "007adda8",
      "PARAM",
      [
        "storage",
        "002b8582",
        null,
        "string"
      ]
    ],
    [
      "007addc0",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007add5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md#insn-007add5c) · [`007adddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md#insn-007adddc) · [`007add68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md#insn-007add68)
- 新版 [`007add9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007add9c) · [`007ade1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007ade1c) · [`007adda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007adda8)

~~~diff
- 007add5c ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 007add5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007add5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007add5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007add9c ["COPY", "tmp:0:8", ["const:4c5:8"]]
+ 007add9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007add9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007add9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007add5c bytes 21e00f91
+ 007add9c bytes 21141391
- 007adddc ["COPY", "register:0:8", ["register:4040:8"]]
- 007adddc ["INT_ADD", "register:40f0:8", ["const:7adddc:8", "const:4:8"]]
- 007adddc ["CALLIND", null, ["register:0:8"]]
+ 007ade1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ade1c ["INT_ADD", "register:40f0:8", ["const:7ade1c:8", "const:4:8"]]
+ 007ade1c ["CALLIND", null, ["register:0:8"]]
- 007adddc bytes 00013fd6
+ 007ade1c bytes 00013fd6
- 007add68 ["COPY", "tmp:0:8", ["const:542:8"]]
- 007add68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007add68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007add68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007adda8 ["COPY", "tmp:0:8", ["const:582:8"]]
+ 007adda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007adda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007adda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007add68 bytes 21081591
+ 007adda8 bytes 21081691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9653b011fdc3d6859095c4bbb7b0af5e"></a>

### [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) → [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) FUN_007adf1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007add18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007add18.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005a4fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4fd8.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 1件 [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a5018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae068",
      "incomplete_value": false,
      "site": "007ae068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae028",
      "incomplete_value": false,
      "site": "007ae028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae178",
      "incomplete_value": false,
      "site": "007ae178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae138",
      "incomplete_value": false,
      "site": "007ae138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "007adfdc",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae068",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae0dc",
      "READ",
      [
        "storage",
        "00c7a6c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007adfdc",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae068",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae0dc",
      "READ",
      [
        "storage",
        "00c7aac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007adf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md#insn-007adf10) · [`007adf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md#insn-007adf3c) · [`007adf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md#insn-007adf48)
- 新版 [`007adf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf50) · [`007adf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf7c) · [`007adf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf88)

~~~diff
- 007adf10 ["INT_ADD", "register:40f0:8", ["const:7adf10:8", "const:4:8"]]
- 007adf10 ["CALL", null, ["callee:00c57e90:8"]]
+ 007adf50 ["INT_ADD", "register:40f0:8", ["const:7adf50:8", "const:4:8"]]
+ 007adf50 ["CALL", null, ["callee:00c57e90:8"]]
- 007adf10 bytes e0a61294
+ 007adf50 bytes d0a71294
- 007adf3c ["INT_ADD", "register:40f0:8", ["const:7adf3c:8", "const:4:8"]]
- 007adf3c ["CALL", null, ["callee:0043bb20:8"]]
+ 007adf7c ["INT_ADD", "register:40f0:8", ["const:7adf7c:8", "const:4:8"]]
+ 007adf7c ["CALL", null, ["callee:0043bb20:8"]]
- 007adf3c bytes e936f297
+ 007adf7c bytes e936f297
- 007adf48 ["INT_ADD", "register:40f0:8", ["const:7adf48:8", "const:4:8"]]
- 007adf48 ["CALL", null, ["callee:005a5018:8"]]
+ 007adf88 ["INT_ADD", "register:40f0:8", ["const:7adf88:8", "const:4:8"]]
+ 007adf88 ["CALL", null, ["callee:005a5018:8"]]
- 007adf48 bytes 24dcf797
+ 007adf88 bytes 24dcf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9abf64f16b9fe60a8686235d35a479c"></a>

### [`007ae400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae400.md) → [`007ae440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md) FUN_007ae440

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007ae464",
      "incomplete_value": false,
      "site": "007ae468",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "007ae424",
      "incomplete_value": false,
      "site": "007ae428",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "007ae468",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae468",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae400.md#insn-007ae41c) · [`007ae434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae400.md#insn-007ae434) · [`007ae444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae400.md#insn-007ae444)
- 新版 [`007ae45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae45c) · [`007ae474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae474) · [`007ae484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae484)

~~~diff
- 007ae41c ["COPY", "tmp:0:8", ["const:610:8"]]
- 007ae41c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae41c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae41c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae45c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 007ae45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae41c bytes 08411891
+ 007ae45c bytes 08412891
- 007ae434 ["INT_ADD", "register:40f0:8", ["const:7ae434:8", "const:4:8"]]
- 007ae434 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae474 ["INT_ADD", "register:40f0:8", ["const:7ae474:8", "const:4:8"]]
+ 007ae474 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae434 bytes 9fa51294
+ 007ae474 bytes 8fa61294
- 007ae444 ["INT_ADD", "register:40f0:8", ["const:7ae444:8", "const:4:8"]]
- 007ae444 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae484 ["INT_ADD", "register:40f0:8", ["const:7ae484:8", "const:4:8"]]
+ 007ae484 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae444 bytes 9ba51294
+ 007ae484 bytes 8ba61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e9e56469be3ec8bd113a1f7531d2de0"></a>

### [`007ae464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae464.md) → [`007ae4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md) FUN_007ae4a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007ae4d8",
      "incomplete_value": false,
      "site": "007ae4dc",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "007ae498",
      "incomplete_value": false,
      "site": "007ae49c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "007ae4dc",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae4dc",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae464.md#insn-007ae488) · [`007ae490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae464.md#insn-007ae490) · [`007ae4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae464.md#insn-007ae4a8)
- 新版 [`007ae4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4c8) · [`007ae4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4d0) · [`007ae4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4e8)

~~~diff
- 007ae488 ["INT_ADD", "register:40f0:8", ["const:7ae488:8", "const:4:8"]]
- 007ae488 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae4c8 ["INT_ADD", "register:40f0:8", ["const:7ae4c8:8", "const:4:8"]]
+ 007ae4c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae488 bytes 8aa51294
+ 007ae4c8 bytes 7aa61294
- 007ae490 ["COPY", "tmp:0:8", ["const:610:8"]]
- 007ae490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae4d0 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 007ae4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae490 bytes 08411891
+ 007ae4d0 bytes 08412891
- 007ae4a8 ["INT_ADD", "register:40f0:8", ["const:7ae4a8:8", "const:4:8"]]
- 007ae4a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae4e8 ["INT_ADD", "register:40f0:8", ["const:7ae4e8:8", "const:4:8"]]
+ 007ae4e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae4a8 bytes 82a51294
+ 007ae4e8 bytes 72a61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6a9481debdf1fee64586a28f8244ec"></a>

### [`007ae4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae4d8.md) → [`007ae518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md) FUN_007ae518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007ae54c",
      "incomplete_value": false,
      "site": "007ae550",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "007ae50c",
      "incomplete_value": false,
      "site": "007ae510",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
      "007ae550",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae550",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae4d8.md#insn-007ae4fc) · [`007ae504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae4d8.md#insn-007ae504) · [`007ae51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae4d8.md#insn-007ae51c)
- 新版 [`007ae53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae53c) · [`007ae544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae544) · [`007ae55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae55c)

~~~diff
- 007ae4fc ["INT_ADD", "register:40f0:8", ["const:7ae4fc:8", "const:4:8"]]
- 007ae4fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae53c ["INT_ADD", "register:40f0:8", ["const:7ae53c:8", "const:4:8"]]
+ 007ae53c ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae4fc bytes 6da51294
+ 007ae53c bytes 5da61294
- 007ae504 ["COPY", "tmp:0:8", ["const:610:8"]]
- 007ae504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae544 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 007ae544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae504 bytes 08411891
+ 007ae544 bytes 08412891
- 007ae51c ["INT_ADD", "register:40f0:8", ["const:7ae51c:8", "const:4:8"]]
- 007ae51c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ae55c ["INT_ADD", "register:40f0:8", ["const:7ae55c:8", "const:4:8"]]
+ 007ae55c ["CALL", null, ["callee:00c57eb0:8"]]
- 007ae51c bytes 65a51294
+ 007ae55c bytes 55a61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af2ecbd9ea72985676e7a41552389b5"></a>

### [`007ae54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae54c.md) → [`007ae58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae58c.md) FUN_007ae58c

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
      "definition_site": "007ae598",
      "incomplete_value": false,
      "site": "007ae5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae558",
      "incomplete_value": false,
      "site": "007ae564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae5a4",
      "DATA",
      [
        "storage",
        "00c7a008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae5a4",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae54c.md#insn-007ae558)
- 新版 [`007ae598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae58c.md#insn-007ae598)

~~~diff
- 007ae558 ["COPY", "tmp:0:8", ["const:8:8"]]
- 007ae558 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ae558 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ae558 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ae598 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 007ae598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ae558 bytes 4a210091
+ 007ae598 bytes 4a211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-163d3e594fc7a7009083a20d0e15beda"></a>

### [`007ae590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae590.md) → [`007ae5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md) FUN_007ae5d0

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
      "definition_site": "007ae5e8",
      "incomplete_value": false,
      "site": "007ae5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae5a8",
      "incomplete_value": false,
      "site": "007ae5b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae5f4",
      "DATA",
      [
        "storage",
        "00c7a008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae5f4",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae590.md#insn-007ae5a8) · [`007ae5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae590.md#insn-007ae5d8)
- 新版 [`007ae5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md#insn-007ae5e8) · [`007ae618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md#insn-007ae618)

~~~diff
- 007ae5a8 ["COPY", "tmp:0:8", ["const:8:8"]]
- 007ae5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae5e8 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 007ae5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae5a8 bytes 08210091
+ 007ae5e8 bytes 08211091
- 007ae5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae5d8 ["INT_ADD", "register:40f0:8", ["const:7ae5d8:8", "const:4:8"]]
- 007ae5d8 ["CALLIND", null, ["register:0:8"]]
+ 007ae618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae618 ["INT_ADD", "register:40f0:8", ["const:7ae618:8", "const:4:8"]]
+ 007ae618 ["CALLIND", null, ["register:0:8"]]
- 007ae5d8 bytes 00013fd6
+ 007ae618 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55846b545887cab1df8cadbe44968645"></a>

### [`007ae5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae5ec.md) → [`007ae62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md) FUN_007ae62c

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
      "definition_site": "007ae654",
      "incomplete_value": false,
      "site": "007ae658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae614",
      "incomplete_value": false,
      "site": "007ae618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae658",
      "DATA",
      [
        "storage",
        "00c7a008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae658",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae5ec.md#insn-007ae600) · [`007ae614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae5ec.md#insn-007ae614) · [`007ae638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae5ec.md#insn-007ae638)
- 新版 [`007ae640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae640) · [`007ae654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae654) · [`007ae678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae678)

~~~diff
- 007ae600 ["INT_ADD", "register:40f0:8", ["const:7ae600:8", "const:4:8"]]
- 007ae600 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ae640 ["INT_ADD", "register:40f0:8", ["const:7ae640:8", "const:4:8"]]
+ 007ae640 ["CALL", null, ["callee:00c57e90:8"]]
- 007ae600 bytes 24a51294
+ 007ae640 bytes 14a61294
- 007ae614 ["COPY", "tmp:0:8", ["const:8:8"]]
- 007ae614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ae654 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 007ae654 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae654 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae654 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae614 bytes 29210091
+ 007ae654 bytes 29211091
- 007ae638 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae638 ["INT_ADD", "register:40f0:8", ["const:7ae638:8", "const:4:8"]]
- 007ae638 ["CALLIND", null, ["register:0:8"]]
+ 007ae678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae678 ["INT_ADD", "register:40f0:8", ["const:7ae678:8", "const:4:8"]]
+ 007ae678 ["CALLIND", null, ["register:0:8"]]
- 007ae638 bytes 00013fd6
+ 007ae678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882c4179716bf32ff8675c9149740f77"></a>

### [`007ae67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae67c.md) → [`007ae6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md) FUN_007ae6bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007ae6d8",
      "incomplete_value": false,
      "site": "007ae6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae698",
      "incomplete_value": false,
      "site": "007ae69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae6dc",
      "DATA",
      [
        "storage",
        "00c7a008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae6dc",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae67c.md#insn-007ae698) · [`007ae6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae67c.md#insn-007ae6c0)
- 新版 [`007ae6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md#insn-007ae6d8) · [`007ae700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md#insn-007ae700)

~~~diff
- 007ae698 ["COPY", "tmp:0:8", ["const:8:8"]]
- 007ae698 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ae698 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ae698 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ae6d8 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 007ae6d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae6d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae6d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ae698 bytes 4a210091
+ 007ae6d8 bytes 4a211091
- 007ae6c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 007ae6c0 ["INT_ADD", "register:40f0:8", ["const:7ae6c0:8", "const:4:8"]]
- 007ae6c0 ["CALLIND", null, ["register:0:8"]]
+ 007ae700 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007ae700 ["INT_ADD", "register:40f0:8", ["const:7ae700:8", "const:4:8"]]
+ 007ae700 ["CALLIND", null, ["register:0:8"]]
- 007ae6c0 bytes 20013fd6
+ 007ae700 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8cbb5225b831b94651e8f0d22cd081"></a>

### [`007ae7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae7c4.md) → [`007ae804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md) FUN_007ae804

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
      "definition_site": "007ae828",
      "incomplete_value": false,
      "site": "007ae828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae7e8",
      "incomplete_value": false,
      "site": "007ae7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "007ae828",
      "DATA",
      [
        "storage",
        "00c7a098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae828",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae7c4.md#insn-007ae7d8) · [`007ae7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae7c4.md#insn-007ae7e4)
- 新版 [`007ae818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md#insn-007ae818) · [`007ae824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md#insn-007ae824)

~~~diff
- 007ae7d8 ["INT_ADD", "register:40f0:8", ["const:7ae7d8:8", "const:4:8"]]
- 007ae7d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ae818 ["INT_ADD", "register:40f0:8", ["const:7ae818:8", "const:4:8"]]
+ 007ae818 ["CALL", null, ["callee:00c57e90:8"]]
- 007ae7d8 bytes aea41294
+ 007ae818 bytes 9ea51294
- 007ae7e4 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007ae7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae824 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007ae824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae7e4 bytes 08610291
+ 007ae824 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae2d6fe5b6da67a152090267297171e3"></a>

### [`007ae7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae7f8.md) → [`007ae838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae838.md) FUN_007ae838

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
      "definition_site": "007ae844",
      "incomplete_value": false,
      "site": "007ae844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae804",
      "incomplete_value": false,
      "site": "007ae804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae844",
      "DATA",
      [
        "storage",
        "00c7a098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae844",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae7f8.md#insn-007ae800)
- 新版 [`007ae840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae838.md#insn-007ae840)

~~~diff
- 007ae800 ["COPY", "tmp:0:8", ["const:98:8"]]
- 007ae800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ae840 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007ae840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae800 bytes 29610291
+ 007ae840 bytes 29611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92cf3754391f09ae5e3477218d963d2d"></a>

### [`007ae814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae814.md) → [`007ae854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md) FUN_007ae854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md) [`007ae950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae950.md) [`007ae954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae954.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`007ae990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae990.md) [`007ae994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae994.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "007ae870",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ae830",
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
      "007ae870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "007ae880",
      "DATA",
      [
        "storage",
        "00c7a118",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae8b8",
      "READ",
      [
        "storage",
        "00c7a138",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ae870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ae880",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae8b8",
      "READ",
      [
        "storage",
        "00c7a538",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae814.md#insn-007ae830) · [`007ae838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae814.md#insn-007ae838) · [`007ae850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae814.md#insn-007ae850)
- 新版 [`007ae870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae870) · [`007ae878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae878) · [`007ae890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae890)

~~~diff
- 007ae830 ["INT_ADD", "register:40f0:8", ["const:7ae830:8", "const:4:8"]]
- 007ae830 ["CALL", null, ["ram:48ccb8:8"]]
+ 007ae870 ["INT_ADD", "register:40f0:8", ["const:7ae870:8", "const:4:8"]]
+ 007ae870 ["CALL", null, ["ram:48ccf8:8"]]
- 007ae830 bytes 2279f397
+ 007ae870 bytes 2279f397
- 007ae838 ["COPY", "tmp:0:8", ["const:118:8"]]
- 007ae838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae878 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007ae878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae838 bytes 08610491
+ 007ae878 bytes 08611491
- 007ae850 ["INT_ADD", "register:40f0:8", ["const:7ae850:8", "const:4:8"]]
- 007ae850 ["CALL", null, ["callee:004938d4:8"]]
+ 007ae890 ["INT_ADD", "register:40f0:8", ["const:7ae890:8", "const:4:8"]]
+ 007ae890 ["CALL", null, ["callee:004938d4:8"]]
- 007ae850 bytes 1194f397
+ 007ae890 bytes 1194f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffb3f12d0c4c747eaf1ce57453144d4"></a>

### [`007ae91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae91c.md) → [`007ae95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md) FUN_007ae95c

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
      "definition_site": "007ae970",
      "incomplete_value": false,
      "site": "007ae974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae930",
      "incomplete_value": false,
      "site": "007ae934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "007ae974",
      "DATA",
      [
        "storage",
        "00c7a118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae974",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae91c.md#insn-007ae928) · [`007ae930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae91c.md#insn-007ae930)
- 新版 [`007ae968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md#insn-007ae968) · [`007ae970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md#insn-007ae970)

~~~diff
- 007ae928 ["INT_ADD", "register:40f0:8", ["const:7ae928:8", "const:4:8"]]
- 007ae928 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ae968 ["INT_ADD", "register:40f0:8", ["const:7ae968:8", "const:4:8"]]
+ 007ae968 ["CALL", null, ["callee:00c57e90:8"]]
- 007ae928 bytes 5aa41294
+ 007ae968 bytes 4aa51294
- 007ae930 ["COPY", "tmp:0:8", ["const:118:8"]]
- 007ae930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae970 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007ae970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae930 bytes 08610491
+ 007ae970 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d9c0025be6d2fe3c26123c5b0660cc"></a>

### [`007ae940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae940.md) → [`007ae980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae980.md) FUN_007ae980

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
      "definition_site": "007ae984",
      "incomplete_value": false,
      "site": "007ae988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae944",
      "incomplete_value": false,
      "site": "007ae948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "007ae988",
      "DATA",
      [
        "storage",
        "00c7a118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae988",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae940.md#insn-007ae944)
- 新版 [`007ae984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae980.md#insn-007ae984)

~~~diff
- 007ae944 ["COPY", "tmp:0:8", ["const:118:8"]]
- 007ae944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae984 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007ae984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae944 bytes 08610491
+ 007ae984 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e9240256d8eccce1326e7fe7a15b627"></a>

### [`007ae958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae958.md) → [`007ae998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md) FUN_007ae998

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.79% / 新版 95.79%

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
      "site": "007aea90",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aea50",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ae9b8",
      "READ",
      [
        "storage",
        "002b7729",
        null,
        "string"
      ]
    ],
    [
      "007ae9c4",
      "READ",
      [
        "storage",
        "002b772f",
        null,
        "string"
      ]
    ],
    [
      "007aea90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "007ae9b8",
      "READ",
      [
        "storage",
        "002b7769",
        null,
        "string"
      ]
    ],
    [
      "007ae9c4",
      "READ",
      [
        "storage",
        "002b776f",
        null,
        "string"
      ]
    ],
    [
      "007aea90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae958.md#insn-007aea50) · [`007ae970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae958.md#insn-007ae970) · [`007ae9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007ae958.md#insn-007ae9a0)
- 新版 [`007aea90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007aea90) · [`007ae9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007ae9b0) · [`007ae9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007ae9e0)

~~~diff
- 007aea50 ["INT_ADD", "register:40f0:8", ["const:7aea50:8", "const:4:8"]]
- 007aea50 ["CALL", null, ["ram:48ccb8:8"]]
+ 007aea90 ["INT_ADD", "register:40f0:8", ["const:7aea90:8", "const:4:8"]]
+ 007aea90 ["CALL", null, ["ram:48ccf8:8"]]
- 007aea50 bytes 9a78f397
+ 007aea90 bytes 9a78f397
- 007ae970 ["COPY", "tmp:0:8", ["const:729:8"]]
- 007ae970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ae9b0 ["COPY", "tmp:0:8", ["const:769:8"]]
+ 007ae9b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae9b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae9b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae970 bytes 29a51c91
+ 007ae9b0 bytes 29a51d91
- 007ae9a0 ["INT_ADD", "register:40f0:8", ["const:7ae9a0:8", "const:4:8"]]
- 007ae9a0 ["CALL", null, ["callee:0048ce54:8"]]
+ 007ae9e0 ["INT_ADD", "register:40f0:8", ["const:7ae9e0:8", "const:4:8"]]
+ 007ae9e0 ["CALL", null, ["callee:0048ce54:8"]]
- 007ae9a0 bytes 1d79f397
+ 007ae9e0 bytes 1d79f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10da7fad59bd3ab8c3aaa0a455d1e154"></a>

### [`007aebb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebb4.md) → [`007aebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md) FUN_007aebf4

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
      "definition_site": "007aec18",
      "incomplete_value": false,
      "site": "007aec18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aebd8",
      "incomplete_value": false,
      "site": "007aebd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "007aec18",
      "DATA",
      [
        "storage",
        "00c7a198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aec18",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebb4.md#insn-007aebc8) · [`007aebd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebb4.md#insn-007aebd4)
- 新版 [`007aec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md#insn-007aec08) · [`007aec14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md#insn-007aec14)

~~~diff
- 007aebc8 ["INT_ADD", "register:40f0:8", ["const:7aebc8:8", "const:4:8"]]
- 007aebc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007aec08 ["INT_ADD", "register:40f0:8", ["const:7aec08:8", "const:4:8"]]
+ 007aec08 ["CALL", null, ["callee:00c57e90:8"]]
- 007aebc8 bytes b2a31294
+ 007aec08 bytes a2a41294
- 007aebd4 ["COPY", "tmp:0:8", ["const:198:8"]]
- 007aebd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aebd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aebd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aec14 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 007aec14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aebd4 bytes 08610691
+ 007aec14 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd9dba53e30dd6b0c42522141e325f4"></a>

### [`007aebe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebe8.md) → [`007aec28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec28.md) FUN_007aec28

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
      "definition_site": "007aec34",
      "incomplete_value": false,
      "site": "007aec34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aebf4",
      "incomplete_value": false,
      "site": "007aebf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "007aec34",
      "DATA",
      [
        "storage",
        "00c7a198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aec34",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aebf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aebe8.md#insn-007aebf0)
- 新版 [`007aec30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec28.md#insn-007aec30)

~~~diff
- 007aebf0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 007aebf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aebf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aebf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aec30 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 007aec30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aec30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aec30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aebf0 bytes 29610691
+ 007aec30 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc5937ee191724087ad0be60ef0fcb73"></a>

### [`007aec38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec38.md) → [`007aec78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md) FUN_007aec78

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
      "definition_site": "007aec9c",
      "incomplete_value": false,
      "site": "007aec9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aec5c",
      "incomplete_value": false,
      "site": "007aec5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "007aec9c",
      "DATA",
      [
        "storage",
        "00c7a218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aec9c",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aec4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec38.md#insn-007aec4c) · [`007aec58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec38.md#insn-007aec58)
- 新版 [`007aec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md#insn-007aec8c) · [`007aec98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md#insn-007aec98)

~~~diff
- 007aec4c ["INT_ADD", "register:40f0:8", ["const:7aec4c:8", "const:4:8"]]
- 007aec4c ["CALL", null, ["callee:00c57e90:8"]]
+ 007aec8c ["INT_ADD", "register:40f0:8", ["const:7aec8c:8", "const:4:8"]]
+ 007aec8c ["CALL", null, ["callee:00c57e90:8"]]
- 007aec4c bytes 91a31294
+ 007aec8c bytes 81a41294
- 007aec58 ["COPY", "tmp:0:8", ["const:218:8"]]
- 007aec58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aec58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aec58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aec98 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 007aec98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aec58 bytes 08610891
+ 007aec98 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8919140341f3c68b851d12bc9918f38"></a>

### [`007aec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec6c.md) → [`007aecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecac.md) FUN_007aecac

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
      "definition_site": "007aecb8",
      "incomplete_value": false,
      "site": "007aecb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aec78",
      "incomplete_value": false,
      "site": "007aec78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007aecb8",
      "DATA",
      [
        "storage",
        "00c7a218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aecb8",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aec74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aec6c.md#insn-007aec74)
- 新版 [`007aecb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecac.md#insn-007aecb4)

~~~diff
- 007aec74 ["COPY", "tmp:0:8", ["const:218:8"]]
- 007aec74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aec74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aec74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aecb4 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 007aecb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aecb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aecb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aec74 bytes 29610891
+ 007aecb4 bytes 29611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d8542893d0fc996ba08bbc4dc53377f"></a>

### [`007aecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecbc.md) → [`007aecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md) FUN_007aecfc

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
      "definition_site": "007aed10",
      "incomplete_value": false,
      "site": "007aed14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aecd0",
      "incomplete_value": false,
      "site": "007aecd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "007aed14",
      "DATA",
      [
        "storage",
        "00c7a298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aed14",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecbc.md#insn-007aecc8) · [`007aecd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecbc.md#insn-007aecd0)
- 新版 [`007aed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md#insn-007aed08) · [`007aed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md#insn-007aed10)

~~~diff
- 007aecc8 ["INT_ADD", "register:40f0:8", ["const:7aecc8:8", "const:4:8"]]
- 007aecc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007aed08 ["INT_ADD", "register:40f0:8", ["const:7aed08:8", "const:4:8"]]
+ 007aed08 ["CALL", null, ["callee:00c57e90:8"]]
- 007aecc8 bytes 72a31294
+ 007aed08 bytes 62a41294
- 007aecd0 ["COPY", "tmp:0:8", ["const:298:8"]]
- 007aecd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aecd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aecd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aed10 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 007aed10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aecd0 bytes 08610a91
+ 007aed10 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d2a467b59efe8c4419f6161d5235fd"></a>

### [`007aece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aece0.md) → [`007aed20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed20.md) FUN_007aed20

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
      "definition_site": "007aed24",
      "incomplete_value": false,
      "site": "007aed28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aece4",
      "incomplete_value": false,
      "site": "007aece8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "007aed28",
      "DATA",
      [
        "storage",
        "00c7a298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aed28",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aece4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aece0.md#insn-007aece4)
- 新版 [`007aed24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed20.md#insn-007aed24)

~~~diff
- 007aece4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 007aece4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aece4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aece4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aed24 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 007aed24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aece4 bytes 08610a91
+ 007aed24 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a37bcab160442b15e21a3eaae19b298"></a>

### [`007aecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md) → [`007aed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md) FUN_007aed38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044c44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c44c.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "007aed54",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aed14",
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
      "007aed54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "007aed54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aed14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md#insn-007aed14) · [`007aed20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md#insn-007aed20) · [`007aed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md#insn-007aed2c)
- 新版 [`007aed54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed54) · [`007aed60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed60) · [`007aed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed6c)

~~~diff
- 007aed14 ["INT_ADD", "register:40f0:8", ["const:7aed14:8", "const:4:8"]]
- 007aed14 ["CALL", null, ["ram:48ccb8:8"]]
+ 007aed54 ["INT_ADD", "register:40f0:8", ["const:7aed54:8", "const:4:8"]]
+ 007aed54 ["CALL", null, ["ram:48ccf8:8"]]
- 007aed14 bytes e977f397
+ 007aed54 bytes e977f397
- 007aed20 ["INT_ADD", "register:40f0:8", ["const:7aed20:8", "const:4:8"]]
- 007aed20 ["CALL", null, ["callee:0044c48c:8"]]
+ 007aed60 ["INT_ADD", "register:40f0:8", ["const:7aed60:8", "const:4:8"]]
+ 007aed60 ["CALL", null, ["callee:0044c48c:8"]]
- 007aed20 bytes cb75f297
+ 007aed60 bytes cb75f297
- 007aed2c ["INT_ADD", "register:40f0:8", ["const:7aed2c:8", "const:4:8"]]
- 007aed2c ["CALL", null, ["callee:004928ac:8"]]
+ 007aed6c ["INT_ADD", "register:40f0:8", ["const:7aed6c:8", "const:4:8"]]
+ 007aed6c ["CALL", null, ["callee:004928ac:8"]]
- 007aed2c bytes d08ef397
+ 007aed6c bytes d08ef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d2aeee37b30f37f6c60dda0c10d677"></a>

### [`007aedd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aedd8.md) → [`007aee18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md) FUN_007aee18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007aee20",
      "incomplete_value": false,
      "site": "007aee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aede0",
      "incomplete_value": false,
      "site": "007aede4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "007aee24",
      "DATA",
      [
        "storage",
        "00c7a318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aee24",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aedd8.md#insn-007aede0) · [`007aee04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aedd8.md#insn-007aee04)
- 新版 [`007aee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md#insn-007aee20) · [`007aee44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md#insn-007aee44)

~~~diff
- 007aede0 ["COPY", "tmp:0:8", ["const:318:8"]]
- 007aede0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aede0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aede0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aee20 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 007aee20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aee20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aee20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aede0 bytes 29610c91
+ 007aee20 bytes 29611c91
- 007aee04 ["INT_ADD", "register:40f0:8", ["const:7aee04:8", "const:4:8"]]
- 007aee04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007aee44 ["INT_ADD", "register:40f0:8", ["const:7aee44:8", "const:4:8"]]
+ 007aee44 ["CALL", null, ["callee:00c57eb0:8"]]
- 007aee04 bytes 2ba31294
+ 007aee44 bytes 1ba41294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07691a165b75eb3088fe51764a51bc50"></a>

### [`007aee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee18.md) → [`007aee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md) FUN_007aee58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007aee84",
      "incomplete_value": false,
      "site": "007aee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aee44",
      "incomplete_value": false,
      "site": "007aee44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "007aee84",
      "DATA",
      [
        "storage",
        "00c7a318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aee84",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aee2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee18.md#insn-007aee2c) · [`007aee3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee18.md#insn-007aee3c) · [`007aee64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee18.md#insn-007aee64)
- 新版 [`007aee6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aee6c) · [`007aee7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aee7c) · [`007aeea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aeea4)

~~~diff
- 007aee2c ["INT_ADD", "register:40f0:8", ["const:7aee2c:8", "const:4:8"]]
- 007aee2c ["CALL", null, ["callee:00c57e90:8"]]
+ 007aee6c ["INT_ADD", "register:40f0:8", ["const:7aee6c:8", "const:4:8"]]
+ 007aee6c ["CALL", null, ["callee:00c57e90:8"]]
- 007aee2c bytes 19a31294
+ 007aee6c bytes 09a41294
- 007aee3c ["COPY", "tmp:0:8", ["const:318:8"]]
- 007aee3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aee3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aee3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aee7c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 007aee7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aee7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aee7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aee3c bytes 4a610c91
+ 007aee7c bytes 4a611c91
- 007aee64 ["INT_ADD", "register:40f0:8", ["const:7aee64:8", "const:4:8"]]
- 007aee64 ["CALL", null, ["callee:0043bb20:8"]]
+ 007aeea4 ["INT_ADD", "register:40f0:8", ["const:7aeea4:8", "const:4:8"]]
+ 007aeea4 ["CALL", null, ["callee:0043bb20:8"]]
- 007aee64 bytes 1f33f297
+ 007aeea4 bytes 1f33f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8982ed257522cdd5164374dfec560820"></a>

### [`007aee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee8c.md) → [`007aeecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeecc.md) FUN_007aeecc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007aeed4",
      "incomplete_value": false,
      "site": "007aeed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aee94",
      "incomplete_value": false,
      "site": "007aee94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "007aeed4",
      "DATA",
      [
        "storage",
        "00c7a318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aeed4",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aee90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee8c.md#insn-007aee90)
- 新版 [`007aeed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeecc.md#insn-007aeed0)

~~~diff
- 007aee90 ["COPY", "tmp:0:8", ["const:318:8"]]
- 007aee90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aee90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aee90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aeed0 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 007aeed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aeed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aeed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aee90 bytes 08610c91
+ 007aeed0 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39f036dfabb58f0f778908956ba05d0"></a>

### [`007aef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef10.md) → [`007aef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md) FUN_007aef50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "007aef60",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aef20",
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
      "007aef60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "007aef60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aef20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef10.md#insn-007aef20)
- 新版 [`007aef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md#insn-007aef60)

~~~diff
- 007aef20 ["INT_ADD", "register:40f0:8", ["const:7aef20:8", "const:4:8"]]
- 007aef20 ["CALL", null, ["ram:48ccb8:8"]]
+ 007aef60 ["INT_ADD", "register:40f0:8", ["const:7aef60:8", "const:4:8"]]
+ 007aef60 ["CALL", null, ["ram:48ccf8:8"]]
- 007aef20 bytes 6677f397
+ 007aef60 bytes 6677f397
~~~


<a id="compare-42326106296e0b46ae406e688b62821e"></a>

### [`007aef60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef60.md) → [`007aefa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md) FUN_007aefa0

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
      "definition_site": "007aefc0",
      "incomplete_value": false,
      "site": "007aefc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aef80",
      "incomplete_value": false,
      "site": "007aef84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "007aefc4",
      "DATA",
      [
        "storage",
        "00c7a398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aefc4",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aef74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef60.md#insn-007aef74) · [`007aef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef60.md#insn-007aef80)
- 新版 [`007aefb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md#insn-007aefb4) · [`007aefc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md#insn-007aefc0)

~~~diff
- 007aef74 ["INT_ADD", "register:40f0:8", ["const:7aef74:8", "const:4:8"]]
- 007aef74 ["CALL", null, ["callee:00c57e90:8"]]
+ 007aefb4 ["INT_ADD", "register:40f0:8", ["const:7aefb4:8", "const:4:8"]]
+ 007aefb4 ["CALL", null, ["callee:00c57e90:8"]]
- 007aef74 bytes c7a21294
+ 007aefb4 bytes b7a31294
- 007aef80 ["COPY", "tmp:0:8", ["const:398:8"]]
- 007aef80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aef80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aef80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aefc0 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 007aefc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aefc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aefc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aef80 bytes 08610e91
+ 007aefc0 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32191ca772db77a51f82767d61d21b8"></a>

### [`007aef98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef98.md) → [`007aefd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefd8.md) FUN_007aefd8

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
      "definition_site": "007aefdc",
      "incomplete_value": false,
      "site": "007aefe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aef9c",
      "incomplete_value": false,
      "site": "007aefa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "007aefe0",
      "DATA",
      [
        "storage",
        "00c7a398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aefe0",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aef98.md#insn-007aef9c)
- 新版 [`007aefdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefd8.md#insn-007aefdc)

~~~diff
- 007aef9c ["COPY", "tmp:0:8", ["const:398:8"]]
- 007aef9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aef9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aef9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aefdc ["COPY", "tmp:0:8", ["const:798:8"]]
+ 007aefdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aefdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aefdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aef9c bytes 08610e91
+ 007aefdc bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ade295e78ce79f4d82df0ba2b3ee81"></a>

### [`007aefb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb8.md) → [`007aeff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md) FUN_007aeff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`007aacc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007aa/007aacc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "007af02c",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aefec",
      "value": [
        "leaf",
        "ram:764344:8"
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
      "007af02c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ],
  "added": [
    [
      "007af02c",
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

- 旧版 [`007aefec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb8.md#insn-007aefec) · [`007aefe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb8.md#insn-007aefe4) · [`007aeff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aefb8.md#insn-007aeff8)
- 新版 [`007af02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af02c) · [`007af024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af024) · [`007af038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af038)

~~~diff
- 007aefec ["INT_ADD", "register:40f0:8", ["const:7aefec:8", "const:4:8"]]
- 007aefec ["CALL", null, ["ram:764344:8"]]
+ 007af02c ["INT_ADD", "register:40f0:8", ["const:7af02c:8", "const:4:8"]]
+ 007af02c ["CALL", null, ["ram:764384:8"]]
- 007aefec bytes d6d4fe97
+ 007af02c bytes d6d4fe97
- 007aefe4 ["INT_ADD", "register:40f0:8", ["const:7aefe4:8", "const:4:8"]]
- 007aefe4 ["CALL", null, ["callee:008514f8:8"]]
+ 007af024 ["INT_ADD", "register:40f0:8", ["const:7af024:8", "const:4:8"]]
+ 007af024 ["CALL", null, ["callee:008514f8:8"]]
- 007aefe4 bytes 35890294
+ 007af024 bytes 35890294
- 007aeff8 ["INT_ADD", "register:40f0:8", ["const:7aeff8:8", "const:4:8"]]
- 007aeff8 ["CALL", null, ["callee:007aad04:8"]]
+ 007af038 ["INT_ADD", "register:40f0:8", ["const:7af038:8", "const:4:8"]]
+ 007af038 ["CALL", null, ["callee:007aad04:8"]]
- 007aeff8 bytes 33efff97
+ 007af038 bytes 33efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-627246ce2e263eecfa513ce3bb8cb6d1"></a>

### [`007af088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af088.md) → [`007af0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md) FUN_007af0c8

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
      "definition_site": "007af0dc",
      "incomplete_value": false,
      "site": "007af0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af09c",
      "incomplete_value": false,
      "site": "007af0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "007af0e0",
      "DATA",
      [
        "storage",
        "00c7a418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af0e0",
      "DATA",
      [
        "storage",
        "00c7a818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af088.md#insn-007af094) · [`007af09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af088.md#insn-007af09c)
- 新版 [`007af0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md#insn-007af0d4) · [`007af0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md#insn-007af0dc)

~~~diff
- 007af094 ["INT_ADD", "register:40f0:8", ["const:7af094:8", "const:4:8"]]
- 007af094 ["CALL", null, ["callee:00c57e90:8"]]
+ 007af0d4 ["INT_ADD", "register:40f0:8", ["const:7af0d4:8", "const:4:8"]]
+ 007af0d4 ["CALL", null, ["callee:00c57e90:8"]]
- 007af094 bytes 7fa21294
+ 007af0d4 bytes 6fa31294
- 007af09c ["COPY", "tmp:0:8", ["const:418:8"]]
- 007af09c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af09c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af09c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af0dc ["COPY", "tmp:0:8", ["const:818:8"]]
+ 007af0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af09c bytes 08611091
+ 007af0dc bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5b7e3107099d4dd7748d78eb3a3c96"></a>

### [`007af0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0f0.md) → [`007af130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md) FUN_007af130

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ab714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007ab714.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "007af168",
      "incomplete_value": false,
      "site": "007af170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af128",
      "incomplete_value": false,
      "site": "007af130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "007af170",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af228",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af170",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af228",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0f0.md#insn-007af170) · [`007af120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0f0.md#insn-007af120) · [`007af128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af0f0.md#insn-007af128)
- 新版 [`007af1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af1b0) · [`007af160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af160) · [`007af168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af168)

~~~diff
- 007af170 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af170 ["INT_ADD", "register:40f0:8", ["const:7af170:8", "const:4:8"]]
- 007af170 ["CALLIND", null, ["register:0:8"]]
+ 007af1b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af1b0 ["INT_ADD", "register:40f0:8", ["const:7af1b0:8", "const:4:8"]]
+ 007af1b0 ["CALLIND", null, ["register:0:8"]]
- 007af170 bytes 00013fd6
+ 007af1b0 bytes 00013fd6
- 007af120 ["INT_ADD", "register:40f0:8", ["const:7af120:8", "const:4:8"]]
- 007af120 ["CALL", null, ["callee:00c57e90:8"]]
+ 007af160 ["INT_ADD", "register:40f0:8", ["const:7af160:8", "const:4:8"]]
+ 007af160 ["CALL", null, ["callee:00c57e90:8"]]
- 007af120 bytes 5ca21294
+ 007af160 bytes 4ca31294
- 007af128 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 007af128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af168 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 007af168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af128 bytes 08010791
+ 007af168 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99690022e8b5ccf7a7e4382cd3f5394b"></a>

### [`007af268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af268.md) → [`007af2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af2a8.md) FUN_007af2a8

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
      "definition_site": "007af2b4",
      "incomplete_value": false,
      "site": "007af2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af274",
      "incomplete_value": false,
      "site": "007af280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007af2c0",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af2c0",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af268.md#insn-007af274)
- 新版 [`007af2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af2a8.md#insn-007af2b4)

~~~diff
- 007af274 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007af274 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007af274 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007af274 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007af2b4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 007af2b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007af2b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007af2b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007af274 bytes 4a611291
+ 007af2b4 bytes 4a612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4b6a8b82fe0651db44d0b1d5391167"></a>

### [`007af308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af308.md) → [`007af348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md) FUN_007af348

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
      "definition_site": "007af374",
      "incomplete_value": false,
      "site": "007af374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af334",
      "incomplete_value": false,
      "site": "007af334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007af374",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af374",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af308.md#insn-007af31c) · [`007af32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af308.md#insn-007af32c) · [`007af350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af308.md#insn-007af350)
- 新版 [`007af35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af35c) · [`007af36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af36c) · [`007af390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af390)

~~~diff
- 007af31c ["INT_ADD", "register:40f0:8", ["const:7af31c:8", "const:4:8"]]
- 007af31c ["CALL", null, ["callee:00c57e90:8"]]
+ 007af35c ["INT_ADD", "register:40f0:8", ["const:7af35c:8", "const:4:8"]]
+ 007af35c ["CALL", null, ["callee:00c57e90:8"]]
- 007af31c bytes dda11294
+ 007af35c bytes cda21294
- 007af32c ["COPY", "tmp:0:8", ["const:498:8"]]
- 007af32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af36c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 007af36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af32c bytes 08611291
+ 007af36c bytes 08612291
- 007af350 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af350 ["INT_ADD", "register:40f0:8", ["const:7af350:8", "const:4:8"]]
- 007af350 ["CALLIND", null, ["register:0:8"]]
+ 007af390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af390 ["INT_ADD", "register:40f0:8", ["const:7af390:8", "const:4:8"]]
+ 007af390 ["CALLIND", null, ["register:0:8"]]
- 007af350 bytes 00013fd6
+ 007af390 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f2d300175afbc767bd3c9f362cab55"></a>

### [`007af390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af390.md) → [`007af3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md) FUN_007af3d0

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
      "definition_site": "007af3ec",
      "incomplete_value": false,
      "site": "007af3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af3ac",
      "incomplete_value": false,
      "site": "007af3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007af3ec",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af3ec",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af390.md#insn-007af3a8) · [`007af3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af390.md#insn-007af3cc)
- 新版 [`007af3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md#insn-007af3e8) · [`007af40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md#insn-007af40c)

~~~diff
- 007af3a8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007af3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007af3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007af3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007af3e8 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 007af3e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007af3e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007af3e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007af3a8 bytes 29611291
+ 007af3e8 bytes 29612291
- 007af3cc ["COPY", "register:0:8", ["register:4048:8"]]
- 007af3cc ["INT_ADD", "register:40f0:8", ["const:7af3cc:8", "const:4:8"]]
- 007af3cc ["CALLIND", null, ["register:0:8"]]
+ 007af40c ["COPY", "register:0:8", ["register:4048:8"]]
+ 007af40c ["INT_ADD", "register:40f0:8", ["const:7af40c:8", "const:4:8"]]
+ 007af40c ["CALLIND", null, ["register:0:8"]]
- 007af3cc bytes 20013fd6
+ 007af40c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9071e4b64e083d9c2e4ceece899f234a"></a>

### [`007af5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af5ec.md) → [`007af62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af62c.md) FUN_007af62c

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
      "definition_site": "007af638",
      "incomplete_value": false,
      "site": "007af644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af5f8",
      "incomplete_value": false,
      "site": "007af604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007af644",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af644",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af5ec.md#insn-007af5f8)
- 新版 [`007af638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af62c.md#insn-007af638)

~~~diff
- 007af5f8 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007af5f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007af5f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007af5f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007af638 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007af638 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007af638 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007af638 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007af5f8 bytes 4a611491
+ 007af638 bytes 4a612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f93a48c40ff335daac1e8721c78e97"></a>

### [`007af630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af630.md) → [`007af670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md) FUN_007af670

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
      "definition_site": "007af688",
      "incomplete_value": false,
      "site": "007af694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af648",
      "incomplete_value": false,
      "site": "007af654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "007af694",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af694",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af630.md#insn-007af648) · [`007af678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af630.md#insn-007af678)
- 新版 [`007af688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md#insn-007af688) · [`007af6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md#insn-007af6b8)

~~~diff
- 007af648 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007af648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af688 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007af688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af648 bytes 08611491
+ 007af688 bytes 08612491
- 007af678 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af678 ["INT_ADD", "register:40f0:8", ["const:7af678:8", "const:4:8"]]
- 007af678 ["CALLIND", null, ["register:0:8"]]
+ 007af6b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af6b8 ["INT_ADD", "register:40f0:8", ["const:7af6b8:8", "const:4:8"]]
+ 007af6b8 ["CALLIND", null, ["register:0:8"]]
- 007af678 bytes 00013fd6
+ 007af6b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

