# v16.0.0 → v16.0.1 · 最優先の変更候補 (90)

[一覧の目次](README.md)

<a id="compare-161c132f991ce895d2dbe2d40dd57000"></a>

### [`00c3c918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md) → [`00c3cd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md) FUN_00c3cd40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c3cda4",
      "incomplete_value": false,
      "site": "00c3cda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c97c",
      "incomplete_value": false,
      "site": "00c3c97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "00c3cda4",
      "DATA",
      [
        "storage",
        "00c99290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3cda4",
      "DATA",
      [
        "storage",
        "00c99690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3c94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md#insn-00c3c94c) · [`00c3c970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md#insn-00c3c970) · [`00c3c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md#insn-00c3c9b4)
- 新版 [`00c3cd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cd74) · [`00c3cd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cd98) · [`00c3cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cddc)

~~~diff
- 00c3c94c ["INT_ADD", "register:40f0:8", ["const:c3c94c:8", "const:4:8"]]
- 00c3c94c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3cd74 ["INT_ADD", "register:40f0:8", ["const:c3cd74:8", "const:4:8"]]
+ 00c3cd74 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3c94c bytes b5740094
+ 00c3cd74 bytes ab740094
- 00c3c970 ["COPY", "tmp:0:8", ["const:290:8"]]
- 00c3c970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3c970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3c970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3cd98 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00c3cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3c970 bytes 08410a91
+ 00c3cd98 bytes 08411a91
- 00c3c9b4 ["INT_ADD", "register:40f0:8", ["const:c3c9b4:8", "const:4:8"]]
- 00c3c9b4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c3cddc ["INT_ADD", "register:40f0:8", ["const:c3cddc:8", "const:4:8"]]
+ 00c3cddc ["CALL", null, ["callee:00c58020:8"]]
- 00c3c9b4 bytes 9b6c0094
+ 00c3cddc bytes 916c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1f5c584819c228d0fc56097a01125ec"></a>

### [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) → [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) FUN_00c3cde0

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 10件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3cefc",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cad4",
      "incomplete_value": false,
      "site": "00c3caec",
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
            "const:e15:8"
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
      "definition_site": "00c3cf04",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:896:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cadc",
      "incomplete_value": false,
      "site": "00c3caec",
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
            "const:856:8"
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
      "definition_site": "00c3cf0c",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cae4",
      "incomplete_value": false,
      "site": "00c3caec",
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
            "const:30e:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3cefc",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ],
    [
      "00c3cf04",
      "PARAM",
      [
        "storage",
        "002b2856",
        null,
        "string"
      ]
    ],
    [
      "00c3cf0c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3cefc",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c3cf04",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c3cf0c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3caec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md#insn-00c3caec) · [`00c3cb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md#insn-00c3cb0c) · [`00c3ca24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md#insn-00c3ca24)
- 新版 [`00c3cf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3cf14) · [`00c3cf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3cf34) · [`00c3ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3ce4c)

~~~diff
- 00c3caec ["INT_ADD", "register:40f0:8", ["const:c3caec:8", "const:4:8"]]
- 00c3caec ["CALL", null, ["callee:00c3800c:8"]]
+ 00c3cf14 ["INT_ADD", "register:40f0:8", ["const:c3cf14:8", "const:4:8"]]
+ 00c3cf14 ["CALL", null, ["callee:00c3800c:8"]]
- 00c3caec bytes 3eecff97
+ 00c3cf14 bytes 3eecff97
- 00c3cb0c ["INT_ADD", "register:40f0:8", ["const:c3cb0c:8", "const:4:8"]]
- 00c3cb0c ["CALL", null, ["callee:00c3800c:8"]]
+ 00c3cf34 ["INT_ADD", "register:40f0:8", ["const:c3cf34:8", "const:4:8"]]
+ 00c3cf34 ["CALL", null, ["callee:00c3800c:8"]]
- 00c3cb0c bytes 36ecff97
+ 00c3cf34 bytes 36ecff97
- 00c3ca24 ["INT_ADD", "register:40f0:8", ["const:c3ca24:8", "const:4:8"]]
- 00c3ca24 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3ce4c ["INT_ADD", "register:40f0:8", ["const:c3ce4c:8", "const:4:8"]]
+ 00c3ce4c ["CALL", null, ["callee:00c5a020:8"]]
- 00c3ca24 bytes 7f740094
+ 00c3ce4c bytes 75740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f520330a158d915d6d0f49985f3b8f4c"></a>

### [`00c3cb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cb14.md) → [`00c3cf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md) FUN_00c3cf3c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c3cfc4",
      "incomplete_value": false,
      "site": "00c3cfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cb9c",
      "incomplete_value": false,
      "site": "00c3cb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00c3cfc4",
      "DATA",
      [
        "storage",
        "00c99370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3cfc4",
      "DATA",
      [
        "storage",
        "00c99770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cb14.md#insn-00c3cb6c) · [`00c3cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cb14.md#insn-00c3cb90) · [`00c3cc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cb14.md#insn-00c3cc04)
- 新版 [`00c3cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3cf94) · [`00c3cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3cfb8) · [`00c3d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3d02c)

~~~diff
- 00c3cb6c ["INT_ADD", "register:40f0:8", ["const:c3cb6c:8", "const:4:8"]]
- 00c3cb6c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3cf94 ["INT_ADD", "register:40f0:8", ["const:c3cf94:8", "const:4:8"]]
+ 00c3cf94 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3cb6c bytes 2d740094
+ 00c3cf94 bytes 23740094
- 00c3cb90 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00c3cb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3cfb8 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00c3cfb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3cfb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3cfb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cb90 bytes 08c10d91
+ 00c3cfb8 bytes 08c11d91
- 00c3cc04 ["INT_ADD", "register:40f0:8", ["const:c3cc04:8", "const:4:8"]]
- 00c3cc04 ["CALL", null, ["callee:00c58020:8"]]
+ 00c3d02c ["INT_ADD", "register:40f0:8", ["const:c3d02c:8", "const:4:8"]]
+ 00c3d02c ["CALL", null, ["callee:00c58020:8"]]
- 00c3cc04 bytes 076c0094
+ 00c3d02c bytes fd6b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a76445d11d93ccad6d1412f3100dd7cb"></a>

### [`00c3cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cde8.md) → [`00c3d210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md) FUN_00c3d210

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d274",
      "incomplete_value": false,
      "site": "00c3d274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ce4c",
      "incomplete_value": false,
      "site": "00c3ce4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d298",
      "incomplete_value": false,
      "site": "00c3d298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:13d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ce70",
      "incomplete_value": false,
      "site": "00c3ce70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:fd:8"
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
      "00c3d274",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d298",
      "DATA",
      [
        "storage",
        "002bb0fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d274",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d298",
      "DATA",
      [
        "storage",
        "002bb13d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ce1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cde8.md#insn-00c3ce1c) · [`00c3ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cde8.md#insn-00c3ce40) · [`00c3ce68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cde8.md#insn-00c3ce68)
- 新版 [`00c3d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d244) · [`00c3d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d268) · [`00c3d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d290)

~~~diff
- 00c3ce1c ["INT_ADD", "register:40f0:8", ["const:c3ce1c:8", "const:4:8"]]
- 00c3ce1c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d244 ["INT_ADD", "register:40f0:8", ["const:c3d244:8", "const:4:8"]]
+ 00c3d244 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3ce1c bytes 81730094
+ 00c3d244 bytes 77730094
- 00c3ce40 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3ce40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d268 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ce40 bytes 08410591
+ 00c3d268 bytes 08411591
- 00c3ce68 ["COPY", "tmp:0:8", ["const:fd:8"]]
- 00c3ce68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d290 ["COPY", "tmp:0:8", ["const:13d:8"]]
+ 00c3d290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ce68 bytes 08f50391
+ 00c3d290 bytes 08f50491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaebb0f028babff7ceb3ce49fa511428"></a>

### [`00c3ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3ce98.md) → [`00c3d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md) FUN_00c3d2c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d324",
      "incomplete_value": false,
      "site": "00c3d324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cefc",
      "incomplete_value": false,
      "site": "00c3cefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d348",
      "incomplete_value": false,
      "site": "00c3d348",
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
            "const:8d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cf20",
      "incomplete_value": false,
      "site": "00c3cf20",
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
            "const:891:8"
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
      "00c3d324",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d348",
      "DATA",
      [
        "storage",
        "002b1891",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d324",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d348",
      "DATA",
      [
        "storage",
        "002b18d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3ce98.md#insn-00c3cecc) · [`00c3cef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3ce98.md#insn-00c3cef0) · [`00c3cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3ce98.md#insn-00c3cf18)
- 新版 [`00c3d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d2f4) · [`00c3d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d318) · [`00c3d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d340)

~~~diff
- 00c3cecc ["INT_ADD", "register:40f0:8", ["const:c3cecc:8", "const:4:8"]]
- 00c3cecc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d2f4 ["INT_ADD", "register:40f0:8", ["const:c3d2f4:8", "const:4:8"]]
+ 00c3d2f4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3cecc bytes 55730094
+ 00c3d2f4 bytes 4b730094
- 00c3cef0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3cef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d318 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cef0 bytes 08410591
+ 00c3d318 bytes 08411591
- 00c3cf18 ["COPY", "tmp:0:8", ["const:891:8"]]
- 00c3cf18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cf18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cf18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d340 ["COPY", "tmp:0:8", ["const:8d1:8"]]
+ 00c3d340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cf18 bytes 08452291
+ 00c3d340 bytes 08452391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04d5cabb47adb8c5878d728fd8969268"></a>

### [`00c3cf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md) → [`00c3d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md) FUN_00c3d370

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d3d4",
      "incomplete_value": false,
      "site": "00c3d3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cfac",
      "incomplete_value": false,
      "site": "00c3cfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d3f8",
      "incomplete_value": false,
      "site": "00c3d3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:e6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cfd0",
      "incomplete_value": false,
      "site": "00c3cfd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:d9e:8"
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
      "00c3d3d4",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d3f8",
      "DATA",
      [
        "storage",
        "0029fd9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d3d4",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d3f8",
      "DATA",
      [
        "storage",
        "0029fe6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md#insn-00c3cf7c) · [`00c3cfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md#insn-00c3cfa0) · [`00c3cfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md#insn-00c3cfc8)
- 新版 [`00c3d3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3a4) · [`00c3d3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3c8) · [`00c3d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3f0)

~~~diff
- 00c3cf7c ["INT_ADD", "register:40f0:8", ["const:c3cf7c:8", "const:4:8"]]
- 00c3cf7c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d3a4 ["INT_ADD", "register:40f0:8", ["const:c3d3a4:8", "const:4:8"]]
+ 00c3d3a4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3cf7c bytes 29730094
+ 00c3d3a4 bytes 1f730094
- 00c3cfa0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3cfa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3c8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cfa0 bytes 08410591
+ 00c3d3c8 bytes 08411591
- 00c3cfc8 ["COPY", "tmp:0:8", ["const:d9e:8"]]
- 00c3cfc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3f0 ["COPY", "tmp:0:8", ["const:e6b:8"]]
+ 00c3d3f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cfc8 bytes 08793691
+ 00c3d3f0 bytes 08ad3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a3d9009944974c7dc191ce9636f1d41"></a>

### [`00c3cff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md) → [`00c3d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md) FUN_00c3d420

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d484",
      "incomplete_value": false,
      "site": "00c3d484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d05c",
      "incomplete_value": false,
      "site": "00c3d05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d4a8",
      "incomplete_value": false,
      "site": "00c3d4a8",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d080",
      "incomplete_value": false,
      "site": "00c3d080",
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
            "const:848:8"
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
      "00c3d484",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d4a8",
      "DATA",
      [
        "storage",
        "002b2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d484",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d4a8",
      "DATA",
      [
        "storage",
        "002b2888",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d02c) · [`00c3d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d050) · [`00c3d078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d078)
- 新版 [`00c3d454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d454) · [`00c3d478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d478) · [`00c3d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d4a0)

~~~diff
- 00c3d02c ["INT_ADD", "register:40f0:8", ["const:c3d02c:8", "const:4:8"]]
- 00c3d02c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d454 ["INT_ADD", "register:40f0:8", ["const:c3d454:8", "const:4:8"]]
+ 00c3d454 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d02c bytes fd720094
+ 00c3d454 bytes f3720094
- 00c3d050 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d478 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d050 bytes 08410591
+ 00c3d478 bytes 08411591
- 00c3d078 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00c3d078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d4a0 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00c3d4a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d4a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d4a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d078 bytes 08212191
+ 00c3d4a0 bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5366377a35e04ef6691bee7872c90a"></a>

### [`00c3d0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d0a8.md) → [`00c3d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md) FUN_00c3d4d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d534",
      "incomplete_value": false,
      "site": "00c3d534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d10c",
      "incomplete_value": false,
      "site": "00c3d10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d558",
      "incomplete_value": false,
      "site": "00c3d558",
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
            "const:9ac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d130",
      "incomplete_value": false,
      "site": "00c3d130",
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
            "const:8df:8"
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
      "00c3d534",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d558",
      "DATA",
      [
        "storage",
        "002a98df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d534",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d558",
      "DATA",
      [
        "storage",
        "002a99ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d0a8.md#insn-00c3d0dc) · [`00c3d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d0a8.md#insn-00c3d100) · [`00c3d128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d0a8.md#insn-00c3d128)
- 新版 [`00c3d504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d504) · [`00c3d528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d528) · [`00c3d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d550)

~~~diff
- 00c3d0dc ["INT_ADD", "register:40f0:8", ["const:c3d0dc:8", "const:4:8"]]
- 00c3d0dc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d504 ["INT_ADD", "register:40f0:8", ["const:c3d504:8", "const:4:8"]]
+ 00c3d504 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d0dc bytes d1720094
+ 00c3d504 bytes c7720094
- 00c3d100 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d528 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d100 bytes 08410591
+ 00c3d528 bytes 08411591
- 00c3d128 ["COPY", "tmp:0:8", ["const:8df:8"]]
- 00c3d128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d550 ["COPY", "tmp:0:8", ["const:9ac:8"]]
+ 00c3d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d128 bytes 087d2391
+ 00c3d550 bytes 08b12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f994eea4cb9417a3f32a943d6d4814b5"></a>

### [`00c3d308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d308.md) → [`00c3d730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md) FUN_00c3d730

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d794",
      "incomplete_value": false,
      "site": "00c3d794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d36c",
      "incomplete_value": false,
      "site": "00c3d36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d7b8",
      "incomplete_value": false,
      "site": "00c3d7b8",
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
            "const:e75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d390",
      "incomplete_value": false,
      "site": "00c3d390",
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
            "const:e35:8"
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
      "00c3d794",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d7b8",
      "DATA",
      [
        "storage",
        "002b9e35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d794",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d7b8",
      "DATA",
      [
        "storage",
        "002b9e75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d308.md#insn-00c3d33c) · [`00c3d360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d308.md#insn-00c3d360) · [`00c3d388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d308.md#insn-00c3d388)
- 新版 [`00c3d764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d764) · [`00c3d788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d788) · [`00c3d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d7b0)

~~~diff
- 00c3d33c ["INT_ADD", "register:40f0:8", ["const:c3d33c:8", "const:4:8"]]
- 00c3d33c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d764 ["INT_ADD", "register:40f0:8", ["const:c3d764:8", "const:4:8"]]
+ 00c3d764 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d33c bytes 39720094
+ 00c3d764 bytes 2f720094
- 00c3d360 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d788 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d360 bytes 08410591
+ 00c3d788 bytes 08411591
- 00c3d388 ["COPY", "tmp:0:8", ["const:e35:8"]]
- 00c3d388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d7b0 ["COPY", "tmp:0:8", ["const:e75:8"]]
+ 00c3d7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d388 bytes 08d53891
+ 00c3d7b0 bytes 08d53991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec25d7da5ae7e703a1419f550a2e03ab"></a>

### [`00c3d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md) → [`00c3d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md) FUN_00c3d7e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d848",
      "incomplete_value": false,
      "site": "00c3d848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d420",
      "incomplete_value": false,
      "site": "00c3d420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
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
      "00c3d848",
      "DATA",
      [
        "storage",
        "00c971d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3d848",
      "DATA",
      [
        "storage",
        "00c975d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d3f0) · [`00c3d414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d414) · [`00c3d45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d45c)
- 新版 [`00c3d818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d818) · [`00c3d83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d83c) · [`00c3d884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d884)

~~~diff
- 00c3d3f0 ["INT_ADD", "register:40f0:8", ["const:c3d3f0:8", "const:4:8"]]
- 00c3d3f0 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d818 ["INT_ADD", "register:40f0:8", ["const:c3d818:8", "const:4:8"]]
+ 00c3d818 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d3f0 bytes 0c720094
+ 00c3d818 bytes 02720094
- 00c3d414 ["COPY", "tmp:0:8", ["const:1d0:8"]]
- 00c3d414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d83c ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00c3d83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d414 bytes 08410791
+ 00c3d83c bytes 08411791
- 00c3d45c ["INT_ADD", "register:40f0:8", ["const:c3d45c:8", "const:4:8"]]
- 00c3d45c ["CALL", null, ["callee:00c58020:8"]]
+ 00c3d884 ["INT_ADD", "register:40f0:8", ["const:c3d884:8", "const:4:8"]]
+ 00c3d884 ["CALL", null, ["callee:00c58020:8"]]
- 00c3d45c bytes f1690094
+ 00c3d884 bytes e7690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6573221a54081077e65503a84ec68f78"></a>

### [`00c3d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md) → [`00c3d888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md) FUN_00c3d888

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d8ec",
      "incomplete_value": false,
      "site": "00c3d8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d4c4",
      "incomplete_value": false,
      "site": "00c3d4c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d910",
      "incomplete_value": false,
      "site": "00c3d910",
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
            "const:8e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d4e8",
      "incomplete_value": false,
      "site": "00c3d4e8",
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
            "const:8a5:8"
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
      "00c3d8ec",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d910",
      "DATA",
      [
        "storage",
        "002b08a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d8ec",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d910",
      "DATA",
      [
        "storage",
        "002b08e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md#insn-00c3d494) · [`00c3d4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md#insn-00c3d4b8) · [`00c3d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md#insn-00c3d4e0)
- 新版 [`00c3d8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d8bc) · [`00c3d8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d8e0) · [`00c3d908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d908)

~~~diff
- 00c3d494 ["INT_ADD", "register:40f0:8", ["const:c3d494:8", "const:4:8"]]
- 00c3d494 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d8bc ["INT_ADD", "register:40f0:8", ["const:c3d8bc:8", "const:4:8"]]
+ 00c3d8bc ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d494 bytes e3710094
+ 00c3d8bc bytes d9710094
- 00c3d4b8 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d4b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8e0 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d4b8 bytes 08410591
+ 00c3d8e0 bytes 08411591
- 00c3d4e0 ["COPY", "tmp:0:8", ["const:8a5:8"]]
- 00c3d4e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d908 ["COPY", "tmp:0:8", ["const:8e5:8"]]
+ 00c3d908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d4e0 bytes 08952291
+ 00c3d908 bytes 08952391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61d3eb01501f3f214460206fcf64742d"></a>

### [`00c3d510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d510.md) → [`00c3d938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md) FUN_00c3d938

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d99c",
      "incomplete_value": false,
      "site": "00c3d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d574",
      "incomplete_value": false,
      "site": "00c3d574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3d9c0",
      "incomplete_value": false,
      "site": "00c3d9c0",
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
            "const:e14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d598",
      "incomplete_value": false,
      "site": "00c3d598",
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
            "const:dd4:8"
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
      "00c3d99c",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d9c0",
      "DATA",
      [
        "storage",
        "002c0dd4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d99c",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d9c0",
      "DATA",
      [
        "storage",
        "002c0e14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d510.md#insn-00c3d544) · [`00c3d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d510.md#insn-00c3d568) · [`00c3d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d510.md#insn-00c3d590)
- 新版 [`00c3d96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d96c) · [`00c3d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d990) · [`00c3d9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d9b8)

~~~diff
- 00c3d544 ["INT_ADD", "register:40f0:8", ["const:c3d544:8", "const:4:8"]]
- 00c3d544 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3d96c ["INT_ADD", "register:40f0:8", ["const:c3d96c:8", "const:4:8"]]
+ 00c3d96c ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d544 bytes b7710094
+ 00c3d96c bytes ad710094
- 00c3d568 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d990 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d568 bytes 08410591
+ 00c3d990 bytes 08411591
- 00c3d590 ["COPY", "tmp:0:8", ["const:dd4:8"]]
- 00c3d590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9b8 ["COPY", "tmp:0:8", ["const:e14:8"]]
+ 00c3d9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d590 bytes 08513791
+ 00c3d9b8 bytes 08513891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae56d087900a57c288da14ce9568ada8"></a>

### [`00c3d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d5c0.md) → [`00c3d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md) FUN_00c3d9e8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3da4c",
      "incomplete_value": false,
      "site": "00c3da4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d624",
      "incomplete_value": false,
      "site": "00c3d624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3da70",
      "incomplete_value": false,
      "site": "00c3da70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:99b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d648",
      "incomplete_value": false,
      "site": "00c3d648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:8ce:8"
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
      "00c3da4c",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3da70",
      "DATA",
      [
        "storage",
        "002a88ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3da4c",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3da70",
      "DATA",
      [
        "storage",
        "002a899b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d5c0.md#insn-00c3d5f4) · [`00c3d618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d5c0.md#insn-00c3d618) · [`00c3d638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d5c0.md#insn-00c3d638)
- 新版 [`00c3da1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da1c) · [`00c3da40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da40) · [`00c3da60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da60)

~~~diff
- 00c3d5f4 ["INT_ADD", "register:40f0:8", ["const:c3d5f4:8", "const:4:8"]]
- 00c3d5f4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3da1c ["INT_ADD", "register:40f0:8", ["const:c3da1c:8", "const:4:8"]]
+ 00c3da1c ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d5f4 bytes 8b710094
+ 00c3da1c bytes 81710094
- 00c3d618 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3da40 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3da40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d618 bytes 08410591
+ 00c3da40 bytes 08411591
- 00c3d638 ["COPY", "tmp:0:8", ["const:8ce:8"]]
- 00c3d638 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00c3d638 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00c3d638 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00c3da60 ["COPY", "tmp:0:8", ["const:99b:8"]]
+ 00c3da60 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00c3da60 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00c3da60 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00c3d638 bytes 6b392391
+ 00c3da60 bytes 6b6d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963b6848707f74655a8348138bd27866"></a>

### [`00c3d66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md) → [`00c3da94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md) FUN_00c3da94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3daf8",
      "incomplete_value": false,
      "site": "00c3daf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d6d0",
      "incomplete_value": false,
      "site": "00c3d6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "definition_site": "00c3db1c",
      "incomplete_value": false,
      "site": "00c3db1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:fa6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d6f4",
      "incomplete_value": false,
      "site": "00c3d6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:f66:8"
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
      "00c3daf8",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3db1c",
      "DATA",
      [
        "storage",
        "002c1f66",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3daf8",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3db1c",
      "DATA",
      [
        "storage",
        "002c1fa6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6a0) · [`00c3d6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6c4) · [`00c3d6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6ec)
- 新版 [`00c3dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3dac8) · [`00c3daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3daec) · [`00c3db14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3db14)

~~~diff
- 00c3d6a0 ["INT_ADD", "register:40f0:8", ["const:c3d6a0:8", "const:4:8"]]
- 00c3d6a0 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3dac8 ["INT_ADD", "register:40f0:8", ["const:c3dac8:8", "const:4:8"]]
+ 00c3dac8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3d6a0 bytes 60710094
+ 00c3dac8 bytes 56710094
- 00c3d6c4 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3d6c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d6c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d6c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3daec ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3daec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3daec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3daec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d6c4 bytes 08410591
+ 00c3daec bytes 08411591
- 00c3d6ec ["COPY", "tmp:0:8", ["const:f66:8"]]
- 00c3d6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3db14 ["COPY", "tmp:0:8", ["const:fa6:8"]]
+ 00c3db14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3db14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3db14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d6ec bytes 08993d91
+ 00c3db14 bytes 08993e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5cd9aae116d605cee9b2c3e1896f092"></a>

### [`00c3da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md) → [`00c3de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md) FUN_00c3de30

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3de98",
      "incomplete_value": true,
      "site": "00c3dea4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:15c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da70",
      "incomplete_value": true,
      "site": "00c3da7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:11c:8"
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
      "definition_site": "00c3de9c",
      "incomplete_value": true,
      "site": "00c3dea8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c3da74",
      "incomplete_value": true,
      "site": "00c3da80",
      "value": [
        "LOAD",
        "8",
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
      "00c3de98",
      "READ",
      [
        "storage",
        "002bb11c",
        null,
        "string"
      ]
    ],
    [
      "00c3de9c",
      "READ",
      [
        "storage",
        "002bb12c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3de98",
      "READ",
      [
        "storage",
        "002bb15c",
        null,
        "string"
      ]
    ],
    [
      "00c3de9c",
      "READ",
      [
        "storage",
        "002bb16c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3da50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md#insn-00c3da50) · [`00c3da68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md#insn-00c3da68) · [`00c3daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3da08.md#insn-00c3daa0)
- 新版 [`00c3de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3de78) · [`00c3de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3de90) · [`00c3dec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3dec8)

~~~diff
- 00c3da50 ["INT_ADD", "register:40f0:8", ["const:c3da50:8", "const:4:8"]]
- 00c3da50 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3de78 ["INT_ADD", "register:40f0:8", ["const:c3de78:8", "const:4:8"]]
+ 00c3de78 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3da50 bytes 94700094
+ 00c3de78 bytes 8a700094
- 00c3da68 ["COPY", "tmp:0:8", ["const:11c:8"]]
- 00c3da68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c3da68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c3da68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c3de90 ["COPY", "tmp:0:8", ["const:15c:8"]]
+ 00c3de90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3de90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3de90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c3da68 bytes 4a710491
+ 00c3de90 bytes 4a710591
- 00c3daa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3daa0 ["INT_ADD", "register:40f0:8", ["const:c3daa0:8", "const:4:8"]]
- 00c3daa0 ["CALLIND", null, ["register:0:8"]]
+ 00c3dec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3dec8 ["INT_ADD", "register:40f0:8", ["const:c3dec8:8", "const:4:8"]]
+ 00c3dec8 ["CALLIND", null, ["register:0:8"]]
- 00c3daa0 bytes 00013fd6
+ 00c3dec8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-998d77552423af5278bf75e230a35209"></a>

### [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) → [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) FUN_00c3dfb0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 7件 [`00c3db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e0d0",
      "incomplete_value": false,
      "site": "00c3e0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3dca8",
      "incomplete_value": false,
      "site": "00c3dca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c3e0d0",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e0dc",
      "DATA",
      [
        "storage",
        "002af724",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e0d0",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e0dc",
      "DATA",
      [
        "storage",
        "002af764",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3dc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dc78) · [`00c3dc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dc9c) · [`00c3dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dd00)
- 新版 [`00c3e0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e0a0) · [`00c3e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e0c4) · [`00c3e128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e128)

~~~diff
- 00c3dc78 ["INT_ADD", "register:40f0:8", ["const:c3dc78:8", "const:4:8"]]
- 00c3dc78 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3e0a0 ["INT_ADD", "register:40f0:8", ["const:c3e0a0:8", "const:4:8"]]
+ 00c3e0a0 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3dc78 bytes ea6f0094
+ 00c3e0a0 bytes e06f0094
- 00c3dc9c ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3dc9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3dc9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3dc9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e0c4 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3dc9c bytes 08010991
+ 00c3e0c4 bytes 08011991
- 00c3dd00 ["INT_ADD", "register:40f0:8", ["const:c3dd00:8", "const:4:8"]]
- 00c3dd00 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3e128 ["INT_ADD", "register:40f0:8", ["const:c3e128:8", "const:4:8"]]
+ 00c3e128 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3dd00 bytes c86f0094
+ 00c3e128 bytes be6f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-286a1583c03f6258136fc5cb82ee3d96"></a>

### [`00c3ddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md) → [`00c3e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md) FUN_00c3e1dc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c3e240",
      "incomplete_value": false,
      "site": "00c3e240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3de18",
      "incomplete_value": false,
      "site": "00c3de18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c3e240",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e240",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3dde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md#insn-00c3dde8) · [`00c3de0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md#insn-00c3de0c) · [`00c3de50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md#insn-00c3de50)
- 新版 [`00c3e210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e210) · [`00c3e234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e234) · [`00c3e278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e278)

~~~diff
- 00c3dde8 ["INT_ADD", "register:40f0:8", ["const:c3dde8:8", "const:4:8"]]
- 00c3dde8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3e210 ["INT_ADD", "register:40f0:8", ["const:c3e210:8", "const:4:8"]]
+ 00c3e210 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3dde8 bytes 8e6f0094
+ 00c3e210 bytes 846f0094
- 00c3de0c ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3de0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3de0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3de0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e234 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3de0c bytes 08010991
+ 00c3e234 bytes 08011991
- 00c3de50 ["INT_ADD", "register:40f0:8", ["const:c3de50:8", "const:4:8"]]
- 00c3de50 ["CALL", null, ["callee:00c58020:8"]]
+ 00c3e278 ["INT_ADD", "register:40f0:8", ["const:c3e278:8", "const:4:8"]]
+ 00c3e278 ["CALL", null, ["callee:00c58020:8"]]
- 00c3de50 bytes 74670094
+ 00c3e278 bytes 6a670094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-329541e8cfdb96db06811f56caea6188"></a>

### [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) → [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) FUN_00c3e454

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 4件 [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 4件 [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e558",
      "incomplete_value": false,
      "site": "00c3e564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e130",
      "incomplete_value": false,
      "site": "00c3e13c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d44:8"
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
      "00c3e53c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e564",
      "DATA",
      [
        "storage",
        "002b8d44",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3e53c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e564",
      "DATA",
      [
        "storage",
        "002b8d84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md#insn-00c3e084) · [`00c3e0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md#insn-00c3e0d4) · [`00c3e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md#insn-00c3e108)
- 新版 [`00c3e4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e4ac) · [`00c3e4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e4fc) · [`00c3e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e530)

~~~diff
- 00c3e084 ["INT_ADD", "register:40f0:8", ["const:c3e084:8", "const:4:8"]]
- 00c3e084 ["CALL", null, ["callee:00c3f034:8"]]
+ 00c3e4ac ["INT_ADD", "register:40f0:8", ["const:c3e4ac:8", "const:4:8"]]
+ 00c3e4ac ["CALL", null, ["callee:00c3f034:8"]]
- 00c3e084 bytes e2020094
+ 00c3e4ac bytes e2020094
- 00c3e0d4 ["INT_ADD", "register:40f0:8", ["const:c3e0d4:8", "const:4:8"]]
- 00c3e0d4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3e4fc ["INT_ADD", "register:40f0:8", ["const:c3e4fc:8", "const:4:8"]]
+ 00c3e4fc ["CALL", null, ["callee:00c5a020:8"]]
- 00c3e0d4 bytes d36e0094
+ 00c3e4fc bytes c96e0094
- 00c3e108 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3e108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c3e108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c3e108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c3e530 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3e530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3e530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c3e108 bytes 29010991
+ 00c3e530 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b217d6082f8c6d46ca76b53ee07b51"></a>

### [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) → [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) FUN_00c3e5c4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) · 呼出先 8件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 8件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ea44",
      "incomplete_value": false,
      "site": "00c3ea44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e61c",
      "incomplete_value": false,
      "site": "00c3e61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      "00c3e7d8",
      "DATA",
      [
        "storage",
        "00c99060",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ea44",
      "DATA",
      [
        "storage",
        "00c990d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e7d8",
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ea44",
      "DATA",
      [
        "storage",
        "00c994d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md#insn-00c3e210) · [`00c3e21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md#insn-00c3e21c) · [`00c3e224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md#insn-00c3e224)
- 新版 [`00c3e638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e638) · [`00c3e644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e644) · [`00c3e64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e64c)

~~~diff
- 00c3e210 ["INT_ADD", "register:40f0:8", ["const:c3e210:8", "const:4:8"]]
- 00c3e210 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3e638 ["INT_ADD", "register:40f0:8", ["const:c3e638:8", "const:4:8"]]
+ 00c3e638 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3e210 bytes a46e0094
+ 00c3e638 bytes 9a6e0094
- 00c3e21c ["INT_ADD", "register:40f0:8", ["const:c3e21c:8", "const:4:8"]]
- 00c3e21c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3e644 ["INT_ADD", "register:40f0:8", ["const:c3e644:8", "const:4:8"]]
+ 00c3e644 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3e21c bytes c9720094
+ 00c3e644 bytes bf720094
- 00c3e224 ["INT_ADD", "register:40f0:8", ["const:c3e224:8", "const:4:8"]]
- 00c3e224 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3e64c ["INT_ADD", "register:40f0:8", ["const:c3e64c:8", "const:4:8"]]
+ 00c3e64c ["CALL", null, ["callee:00c5a020:8"]]
- 00c3e224 bytes 7f6e0094
+ 00c3e64c bytes 756e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445cb455ba77969b8430eab74a5288aa"></a>

### [`00c3e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md) → [`00c3ea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) FUN_00c3ea94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eafc",
      "incomplete_value": false,
      "site": "00c3eafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e6d4",
      "incomplete_value": false,
      "site": "00c3e6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
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
      "00c3eafc",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3eafc",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e6a4) · [`00c3e6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e6c8) · [`00c3e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e710)
- 新版 [`00c3eacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eacc) · [`00c3eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eaf0) · [`00c3eb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eb38)

~~~diff
- 00c3e6a4 ["INT_ADD", "register:40f0:8", ["const:c3e6a4:8", "const:4:8"]]
- 00c3e6a4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3eacc ["INT_ADD", "register:40f0:8", ["const:c3eacc:8", "const:4:8"]]
+ 00c3eacc ["CALL", null, ["callee:00c5a020:8"]]
- 00c3e6a4 bytes 5f6d0094
+ 00c3eacc bytes 556d0094
- 00c3e6c8 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00c3e6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3eaf0 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00c3eaf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eaf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eaf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e6c8 bytes 08010591
+ 00c3eaf0 bytes 08011591
- 00c3e710 ["INT_ADD", "register:40f0:8", ["const:c3e710:8", "const:4:8"]]
- 00c3e710 ["CALL", null, ["callee:00c58020:8"]]
+ 00c3eb38 ["INT_ADD", "register:40f0:8", ["const:c3eb38:8", "const:4:8"]]
+ 00c3eb38 ["CALL", null, ["callee:00c58020:8"]]
- 00c3e710 bytes 44650094
+ 00c3eb38 bytes 3a650094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de7106325757febb494e8b982dbfa549"></a>

### [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) → [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) FUN_00c3eb3c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 7件 [`00c3f548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md) [`00c3f620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 4件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 7件 [`00c3f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md) [`00c3fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eda8",
      "incomplete_value": false,
      "site": "00c3eda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e980",
      "incomplete_value": false,
      "site": "00c3e980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "00c3ec90",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eda8",
      "DATA",
      [
        "storage",
        "00c97320",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ee88",
      "PARAM",
      [
        "storage",
        "002a1ccc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3ec90",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eda8",
      "DATA",
      [
        "storage",
        "00c97720",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ee88",
      "PARAM",
      [
        "storage",
        "002a1d99",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md#insn-00c3e838) · [`00c3e85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md#insn-00c3e85c) · [`00c3e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md#insn-00c3e948)
- 新版 [`00c3ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ec60) · [`00c3ec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ec84) · [`00c3ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ed70)

~~~diff
- 00c3e838 ["INT_ADD", "register:40f0:8", ["const:c3e838:8", "const:4:8"]]
- 00c3e838 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3ec60 ["INT_ADD", "register:40f0:8", ["const:c3ec60:8", "const:4:8"]]
+ 00c3ec60 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3e838 bytes fa6c0094
+ 00c3ec60 bytes f06c0094
- 00c3e85c ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3e85c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e85c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e85c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ec84 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3ec84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ec84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ec84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e85c bytes 08010991
+ 00c3ec84 bytes 08011991
- 00c3e948 ["INT_ADD", "register:40f0:8", ["const:c3e948:8", "const:4:8"]]
- 00c3e948 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3ed70 ["INT_ADD", "register:40f0:8", ["const:c3ed70:8", "const:4:8"]]
+ 00c3ed70 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3e948 bytes b66c0094
+ 00c3ed70 bytes ac6c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-776d527bf80767da357440e7a94ac16f"></a>

### [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) → [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) FUN_00c3ef00

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 3件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 3件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 3件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3efdc",
      "incomplete_value": false,
      "site": "00c3efdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ebb4",
      "incomplete_value": false,
      "site": "00c3ebb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "definition_site": "00c3effc",
      "incomplete_value": false,
      "site": "00c3effc",
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
            "const:58c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ebd4",
      "incomplete_value": false,
      "site": "00c3ebd4",
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
            "const:54c:8"
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
      "00c3efdc",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3effc",
      "DATA",
      [
        "storage",
        "002ae54c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3efdc",
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3effc",
      "DATA",
      [
        "storage",
        "002ae58c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md#insn-00c3eb38) · [`00c3eb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md#insn-00c3eb80) · [`00c3eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md#insn-00c3eba4)
- 新版 [`00c3ef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3ef60) · [`00c3efa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3efa8) · [`00c3efcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3efcc)

~~~diff
- 00c3eb38 ["INT_ADD", "register:40f0:8", ["const:c3eb38:8", "const:4:8"]]
- 00c3eb38 ["CALL", null, ["callee:00c3fd7c:8"]]
+ 00c3ef60 ["INT_ADD", "register:40f0:8", ["const:c3ef60:8", "const:4:8"]]
+ 00c3ef60 ["CALL", null, ["callee:00c3fd7c:8"]]
- 00c3eb38 bytes 87030094
+ 00c3ef60 bytes 87030094
- 00c3eb80 ["INT_ADD", "register:40f0:8", ["const:c3eb80:8", "const:4:8"]]
- 00c3eb80 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3efa8 ["INT_ADD", "register:40f0:8", ["const:c3efa8:8", "const:4:8"]]
+ 00c3efa8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3eb80 bytes 286c0094
+ 00c3efa8 bytes 1e6c0094
- 00c3eba4 ["COPY", "register:4050:8", ["const:c97000:8"]]
+ 00c3efcc ["COPY", "register:4050:8", ["const:c98000:8"]]
- 00c3eba4 bytes ca0200b0
+ 00c3efcc bytes ca0200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f49c5b962e2ee8e03399c18af46a411"></a>

### [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) → [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) FUN_00c3f034

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 6件 [`00c4be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4be00.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)
- 新版 呼出元 3件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 6件 [`00c4c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c228.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f258",
      "incomplete_value": false,
      "site": "00c3f25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ee30",
      "incomplete_value": false,
      "site": "00c3ee34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00c3f25c",
      "DATA",
      [
        "storage",
        "00c98c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f25c",
      "DATA",
      [
        "storage",
        "00c99070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3edd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md#insn-00c3edd8) · [`00c3ee2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md#insn-00c3ee2c) · [`00c3ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md#insn-00c3ee30)
- 新版 [`00c3f200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f200) · [`00c3f254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f254) · [`00c3f258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f258)

~~~diff
- 00c3edd8 ["INT_ADD", "register:40f0:8", ["const:c3edd8:8", "const:4:8"]]
- 00c3edd8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3f200 ["INT_ADD", "register:40f0:8", ["const:c3f200:8", "const:4:8"]]
+ 00c3f200 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3edd8 bytes 926b0094
+ 00c3f200 bytes 886b0094
- 00c3ee2c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3f254 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c3ee2c bytes c80200d0
+ 00c3f254 bytes c80200d0
- 00c3ee30 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00c3ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f258 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00c3f258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ee30 bytes 08c13191
+ 00c3f258 bytes 08c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bff119433f84faac8566d1fc38dca55f"></a>

### [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) → [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) FUN_00c3f310

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) · 呼出先 13件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md)
- 新版 呼出元 2件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) · 呼出先 13件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f558",
      "incomplete_value": false,
      "site": "00c3f558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f130",
      "incomplete_value": false,
      "site": "00c3f130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "definition_site": "00c3f7c0",
      "incomplete_value": false,
      "site": "00c3f7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f398",
      "incomplete_value": false,
      "site": "00c3f398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3f49c",
      "DATA",
      [
        "storage",
        "00c98cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f558",
      "DATA",
      [
        "storage",
        "00c98ea0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f648",
      "DATA",
      [
        "storage",
        "00c98f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f49c",
      "DATA",
      [
        "storage",
        "00c990f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f558",
      "DATA",
      [
        "storage",
        "00c992a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f648",
      "DATA",
      [
        "storage",
        "00c99380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ef1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md#insn-00c3ef1c) · [`00c3efa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md#insn-00c3efa0) · [`00c3efc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md#insn-00c3efc0)
- 新版 [`00c3f344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f344) · [`00c3f3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f3c8) · [`00c3f3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f3e8)

~~~diff
- 00c3ef1c ["INT_ADD", "register:40f0:8", ["const:c3ef1c:8", "const:4:8"]]
- 00c3ef1c ["CALL", null, ["callee:00c3db44:8"]]
+ 00c3f344 ["INT_ADD", "register:40f0:8", ["const:c3f344:8", "const:4:8"]]
+ 00c3f344 ["CALL", null, ["callee:00c3db44:8"]]
- 00c3ef1c bytes 00faff97
+ 00c3f344 bytes 00faff97
- 00c3efa0 ["INT_ADD", "register:40f0:8", ["const:c3efa0:8", "const:4:8"]]
- 00c3efa0 ["CALL", null, ["callee:00c3dfb0:8"]]
+ 00c3f3c8 ["INT_ADD", "register:40f0:8", ["const:c3f3c8:8", "const:4:8"]]
+ 00c3f3c8 ["CALL", null, ["callee:00c3dfb0:8"]]
- 00c3efa0 bytes fafaff97
+ 00c3f3c8 bytes fafaff97
- 00c3efc0 ["INT_ADD", "register:40f0:8", ["const:c3efc0:8", "const:4:8"]]
- 00c3efc0 ["CALL", null, ["callee:00c46520:8"]]
+ 00c3f3e8 ["INT_ADD", "register:40f0:8", ["const:c3f3e8:8", "const:4:8"]]
+ 00c3f3e8 ["CALL", null, ["callee:00c46520:8"]]
- 00c3efc0 bytes 4e1c0094
+ 00c3f3e8 bytes 4e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-585ff57b4bc65cfb690e356ad68f8a8e"></a>

### [`00c3f4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md) → [`00c3f8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md) FUN_00c3f8d0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c3f934",
      "incomplete_value": false,
      "site": "00c3f934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f50c",
      "incomplete_value": false,
      "site": "00c3f50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c3f934",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f934",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f4dc) · [`00c3f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f500) · [`00c3f544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f544)
- 新版 [`00c3f904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f904) · [`00c3f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f928) · [`00c3f96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f96c)

~~~diff
- 00c3f4dc ["INT_ADD", "register:40f0:8", ["const:c3f4dc:8", "const:4:8"]]
- 00c3f4dc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3f904 ["INT_ADD", "register:40f0:8", ["const:c3f904:8", "const:4:8"]]
+ 00c3f904 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3f4dc bytes d1690094
+ 00c3f904 bytes c7690094
- 00c3f500 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3f500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f928 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3f928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3f500 bytes 08010991
+ 00c3f928 bytes 08011991
- 00c3f544 ["INT_ADD", "register:40f0:8", ["const:c3f544:8", "const:4:8"]]
- 00c3f544 ["CALL", null, ["callee:00c58020:8"]]
+ 00c3f96c ["INT_ADD", "register:40f0:8", ["const:c3f96c:8", "const:4:8"]]
+ 00c3f96c ["CALL", null, ["callee:00c58020:8"]]
- 00c3f544 bytes b7610094
+ 00c3f96c bytes ad610094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d354a9a3f6cf99a866a5fd167345ac18"></a>

### [`00c3f620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md) → [`00c3fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) FUN_00c3fa48

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fab4",
      "incomplete_value": false,
      "site": "00c3fab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f68c",
      "incomplete_value": false,
      "site": "00c3f68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c3fab4",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3fab4",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md#insn-00c3f654) · [`00c3f67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md#insn-00c3f67c) · [`00c3f684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md#insn-00c3f684)
- 新版 [`00c3fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3fa7c) · [`00c3faa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3faa4) · [`00c3faac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3faac)

~~~diff
- 00c3f654 ["INT_ADD", "register:40f0:8", ["const:c3f654:8", "const:4:8"]]
- 00c3f654 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3fa7c ["INT_ADD", "register:40f0:8", ["const:c3fa7c:8", "const:4:8"]]
+ 00c3fa7c ["CALL", null, ["callee:00c5a020:8"]]
- 00c3f654 bytes 73690094
+ 00c3fa7c bytes 69690094
- 00c3f67c ["INT_ADD", "register:40f0:8", ["const:c3f67c:8", "const:4:8"]]
- 00c3f67c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c3faa4 ["INT_ADD", "register:40f0:8", ["const:c3faa4:8", "const:4:8"]]
+ 00c3faa4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c3f67c bytes 59610094
+ 00c3faa4 bytes 4f610094
- 00c3f684 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c3f684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c3f684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c3f684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c3faac ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3faac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3faac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3faac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c3f684 bytes 29010991
+ 00c3faac bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9b18c7b87c0bfb697d6f05697a8edd7"></a>

### [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) → [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) FUN_00c3fd7c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 14件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) · 呼出先 42件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md)
- 新版 呼出元 14件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) · 呼出先 42件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40510",
      "incomplete_value": false,
      "site": "00c40510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c400e8",
      "incomplete_value": false,
      "site": "00c400e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40950",
      "incomplete_value": false,
      "site": "00c40950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40528",
      "incomplete_value": false,
      "site": "00c40528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40ffc",
      "incomplete_value": false,
      "site": "00c40ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40bd4",
      "incomplete_value": false,
      "site": "00c40bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 164,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3fe50",
      "READ",
      [
        "storage",
        "00c97560",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fe60",
      "READ",
      [
        "storage",
        "00c97561",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fe8c",
      "READ",
      [
        "storage",
        "00c97570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3fe50",
      "READ",
      [
        "storage",
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fe60",
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fe8c",
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3fe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md#insn-00c3fe0c) · [`00c3fe6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md#insn-00c3fe6c) · [`00c40410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md#insn-00c40410)
- 新版 [`00c40234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40234) · [`00c40294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40294) · [`00c40838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40838)

~~~diff
- 00c3fe0c ["INT_ADD", "register:40f0:8", ["const:c3fe0c:8", "const:4:8"]]
- 00c3fe0c ["CALL", null, ["callee:00c3a118:8"]]
+ 00c40234 ["INT_ADD", "register:40f0:8", ["const:c40234:8", "const:4:8"]]
+ 00c40234 ["CALL", null, ["callee:00c3a118:8"]]
- 00c3fe0c bytes b9e7ff97
+ 00c40234 bytes b9e7ff97
- 00c3fe6c ["INT_ADD", "register:40f0:8", ["const:c3fe6c:8", "const:4:8"]]
- 00c3fe6c ["CALL", null, ["callee:00c3a118:8"]]
+ 00c40294 ["INT_ADD", "register:40f0:8", ["const:c40294:8", "const:4:8"]]
+ 00c40294 ["CALL", null, ["callee:00c3a118:8"]]
- 00c3fe6c bytes a1e7ff97
+ 00c40294 bytes a1e7ff97
- 00c40410 ["INT_ADD", "register:40f0:8", ["const:c40410:8", "const:4:8"]]
- 00c40410 ["CALL", null, ["callee:00c3a118:8"]]
+ 00c40838 ["INT_ADD", "register:40f0:8", ["const:c40838:8", "const:4:8"]]
+ 00c40838 ["CALL", null, ["callee:00c3a118:8"]]
- 00c40410 bytes 38e6ff97
+ 00c40838 bytes 38e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8470205337ee51b35f14320ef84a3834"></a>

### [`00c40ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40ce4.md) → [`00c4110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md) FUN_00c4110c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4117c",
      "incomplete_value": false,
      "site": "00c4117c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40d54",
      "incomplete_value": false,
      "site": "00c40d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:850:8"
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
      "00c4117c",
      "DATA",
      [
        "storage",
        "00c97850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4117c",
      "DATA",
      [
        "storage",
        "00c97c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c40d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40ce4.md#insn-00c40d24) · [`00c40d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40ce4.md#insn-00c40d48) · [`00c40da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40ce4.md#insn-00c40da0)
- 新版 [`00c4114c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c4114c) · [`00c41170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c41170) · [`00c411c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c411c8)

~~~diff
- 00c40d24 ["INT_ADD", "register:40f0:8", ["const:c40d24:8", "const:4:8"]]
- 00c40d24 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4114c ["INT_ADD", "register:40f0:8", ["const:c4114c:8", "const:4:8"]]
+ 00c4114c ["CALL", null, ["callee:00c5a020:8"]]
- 00c40d24 bytes bf630094
+ 00c4114c bytes b5630094
- 00c40d48 ["COPY", "tmp:0:8", ["const:850:8"]]
- 00c40d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c40d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c40d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41170 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00c41170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c40d48 bytes 08412191
+ 00c41170 bytes 08413191
- 00c40da0 ["INT_ADD", "register:40f0:8", ["const:c40da0:8", "const:4:8"]]
- 00c40da0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c411c8 ["INT_ADD", "register:40f0:8", ["const:c411c8:8", "const:4:8"]]
+ 00c411c8 ["CALL", null, ["callee:00c58020:8"]]
- 00c40da0 bytes a05b0094
+ 00c411c8 bytes 965b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92e2f89f5648f065512ca1d8ca06ab72"></a>

### [`00c40da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md) → [`00c411cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md) FUN_00c411cc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4123c",
      "incomplete_value": false,
      "site": "00c4123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40e14",
      "incomplete_value": false,
      "site": "00c40e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00c4123c",
      "DATA",
      [
        "storage",
        "00c978c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4123c",
      "DATA",
      [
        "storage",
        "00c97cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c40de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md#insn-00c40de4) · [`00c40e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md#insn-00c40e08) · [`00c40e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md#insn-00c40e5c)
- 新版 [`00c4120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c4120c) · [`00c41230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c41230) · [`00c41284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c41284)

~~~diff
- 00c40de4 ["INT_ADD", "register:40f0:8", ["const:c40de4:8", "const:4:8"]]
- 00c40de4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4120c ["INT_ADD", "register:40f0:8", ["const:c4120c:8", "const:4:8"]]
+ 00c4120c ["CALL", null, ["callee:00c5a020:8"]]
- 00c40de4 bytes 8f630094
+ 00c4120c bytes 85630094
- 00c40e08 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00c40e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c40e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c40e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41230 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00c41230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c40e08 bytes 08012391
+ 00c41230 bytes 08013391
- 00c40e5c ["INT_ADD", "register:40f0:8", ["const:c40e5c:8", "const:4:8"]]
- 00c40e5c ["CALL", null, ["callee:00c58020:8"]]
+ 00c41284 ["INT_ADD", "register:40f0:8", ["const:c41284:8", "const:4:8"]]
+ 00c41284 ["CALL", null, ["callee:00c58020:8"]]
- 00c40e5c bytes 715b0094
+ 00c41284 bytes 675b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8a9291ee83013ed6f824565f847ef9"></a>

### [`00c40e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md) → [`00c41288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md) FUN_00c41288

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c412fc",
      "incomplete_value": false,
      "site": "00c412fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40ed4",
      "incomplete_value": false,
      "site": "00c40ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00c412fc",
      "DATA",
      [
        "storage",
        "00c97930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c412fc",
      "DATA",
      [
        "storage",
        "00c97d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c40ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40ea4) · [`00c40ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40ec8) · [`00c40f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40f28)
- 新版 [`00c412cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c412cc) · [`00c412f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c412f0) · [`00c41350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c41350)

~~~diff
- 00c40ea4 ["INT_ADD", "register:40f0:8", ["const:c40ea4:8", "const:4:8"]]
- 00c40ea4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c412cc ["INT_ADD", "register:40f0:8", ["const:c412cc:8", "const:4:8"]]
+ 00c412cc ["CALL", null, ["callee:00c5a020:8"]]
- 00c40ea4 bytes 5f630094
+ 00c412cc bytes 55630094
- 00c40ec8 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00c40ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c40ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c40ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c412f0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00c412f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c412f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c412f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c40ec8 bytes 08c12491
+ 00c412f0 bytes 08c13491
- 00c40f28 ["INT_ADD", "register:40f0:8", ["const:c40f28:8", "const:4:8"]]
- 00c40f28 ["CALL", null, ["callee:00c58020:8"]]
+ 00c41350 ["INT_ADD", "register:40f0:8", ["const:c41350:8", "const:4:8"]]
+ 00c41350 ["CALL", null, ["callee:00c58020:8"]]
- 00c40f28 bytes 3e5b0094
+ 00c41350 bytes 345b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df731fa0673055d73efaa378487748e"></a>

### [`00c40f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md) → [`00c41354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md) FUN_00c41354

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c413d4",
      "incomplete_value": false,
      "site": "00c413d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40fac",
      "incomplete_value": false,
      "site": "00c40fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00c413d4",
      "DATA",
      [
        "storage",
        "00c979a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c413d4",
      "DATA",
      [
        "storage",
        "00c97da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c40f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c40f7c) · [`00c40fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c40fa0) · [`00c41014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c41014)
- 新版 [`00c413a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c413a4) · [`00c413c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c413c8) · [`00c4143c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c4143c)

~~~diff
- 00c40f7c ["INT_ADD", "register:40f0:8", ["const:c40f7c:8", "const:4:8"]]
- 00c40f7c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c413a4 ["INT_ADD", "register:40f0:8", ["const:c413a4:8", "const:4:8"]]
+ 00c413a4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c40f7c bytes 29630094
+ 00c413a4 bytes 1f630094
- 00c40fa0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00c40fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c40fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c40fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c413c8 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c413c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c413c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c413c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c40fa0 bytes 08812691
+ 00c413c8 bytes 08813691
- 00c41014 ["INT_ADD", "register:40f0:8", ["const:c41014:8", "const:4:8"]]
- 00c41014 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4143c ["INT_ADD", "register:40f0:8", ["const:c4143c:8", "const:4:8"]]
+ 00c4143c ["CALL", null, ["callee:00c58020:8"]]
- 00c41014 bytes 035b0094
+ 00c4143c bytes f95a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057069d7016ddebe73b5af9bd59413d8"></a>

### [`00c41018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md) → [`00c41440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md) FUN_00c41440

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c414b0",
      "incomplete_value": false,
      "site": "00c414b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41088",
      "incomplete_value": false,
      "site": "00c41088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00c414b0",
      "DATA",
      [
        "storage",
        "00c97a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c414b0",
      "DATA",
      [
        "storage",
        "00c97e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md#insn-00c41058) · [`00c4107c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md#insn-00c4107c) · [`00c410d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md#insn-00c410d4)
- 新版 [`00c41480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c41480) · [`00c414a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c414a4) · [`00c414fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c414fc)

~~~diff
- 00c41058 ["INT_ADD", "register:40f0:8", ["const:c41058:8", "const:4:8"]]
- 00c41058 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c41480 ["INT_ADD", "register:40f0:8", ["const:c41480:8", "const:4:8"]]
+ 00c41480 ["CALL", null, ["callee:00c5a020:8"]]
- 00c41058 bytes f2620094
+ 00c41480 bytes e8620094
- 00c4107c ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00c4107c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4107c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4107c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c414a4 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00c414a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c414a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c414a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4107c bytes 08012a91
+ 00c414a4 bytes 08013a91
- 00c410d4 ["INT_ADD", "register:40f0:8", ["const:c410d4:8", "const:4:8"]]
- 00c410d4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c414fc ["INT_ADD", "register:40f0:8", ["const:c414fc:8", "const:4:8"]]
+ 00c414fc ["CALL", null, ["callee:00c58020:8"]]
- 00c410d4 bytes d35a0094
+ 00c414fc bytes c95a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e649939337e4407382bd28c11d3f8edc"></a>

### [`00c410d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c410d8.md) → [`00c41500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md) FUN_00c41500

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41570",
      "incomplete_value": false,
      "site": "00c41570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41148",
      "incomplete_value": false,
      "site": "00c41148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "00c41570",
      "DATA",
      [
        "storage",
        "00c97af0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41570",
      "DATA",
      [
        "storage",
        "00c97ef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c410d8.md#insn-00c41118) · [`00c4113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c410d8.md#insn-00c4113c) · [`00c41194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c410d8.md#insn-00c41194)
- 新版 [`00c41540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c41540) · [`00c41564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c41564) · [`00c415bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c415bc)

~~~diff
- 00c41118 ["INT_ADD", "register:40f0:8", ["const:c41118:8", "const:4:8"]]
- 00c41118 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c41540 ["INT_ADD", "register:40f0:8", ["const:c41540:8", "const:4:8"]]
+ 00c41540 ["CALL", null, ["callee:00c5a020:8"]]
- 00c41118 bytes c2620094
+ 00c41540 bytes b8620094
- 00c4113c ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00c4113c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4113c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4113c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41564 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00c41564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4113c bytes 08c12b91
+ 00c41564 bytes 08c13b91
- 00c41194 ["INT_ADD", "register:40f0:8", ["const:c41194:8", "const:4:8"]]
- 00c41194 ["CALL", null, ["callee:00c58020:8"]]
+ 00c415bc ["INT_ADD", "register:40f0:8", ["const:c415bc:8", "const:4:8"]]
+ 00c415bc ["CALL", null, ["callee:00c58020:8"]]
- 00c41194 bytes a35a0094
+ 00c415bc bytes 995a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30feeb0103929cee9d5dcd688191640d"></a>

### [`00c41198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41198.md) → [`00c415c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md) FUN_00c415c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c41634",
      "incomplete_value": false,
      "site": "00c41634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4120c",
      "incomplete_value": false,
      "site": "00c4120c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00c41634",
      "DATA",
      [
        "storage",
        "00c97b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41634",
      "DATA",
      [
        "storage",
        "00c97f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c411dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41198.md#insn-00c411dc) · [`00c41200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41198.md#insn-00c41200) · [`00c4125c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41198.md#insn-00c4125c)
- 新版 [`00c41604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41604) · [`00c41628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41628) · [`00c41684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41684)

~~~diff
- 00c411dc ["INT_ADD", "register:40f0:8", ["const:c411dc:8", "const:4:8"]]
- 00c411dc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c41604 ["INT_ADD", "register:40f0:8", ["const:c41604:8", "const:4:8"]]
+ 00c41604 ["CALL", null, ["callee:00c5a020:8"]]
- 00c411dc bytes 91620094
+ 00c41604 bytes 87620094
- 00c41200 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00c41200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41628 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00c41628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41200 bytes 08812d91
+ 00c41628 bytes 08813d91
- 00c4125c ["INT_ADD", "register:40f0:8", ["const:c4125c:8", "const:4:8"]]
- 00c4125c ["CALL", null, ["callee:00c58020:8"]]
+ 00c41684 ["INT_ADD", "register:40f0:8", ["const:c41684:8", "const:4:8"]]
+ 00c41684 ["CALL", null, ["callee:00c58020:8"]]
- 00c4125c bytes 715a0094
+ 00c41684 bytes 675a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d642922e94592f698c97c4fe68414c"></a>

### [`00c41260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41260.md) → [`00c41688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md) FUN_00c41688

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c416fc",
      "incomplete_value": false,
      "site": "00c416fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c412d4",
      "incomplete_value": false,
      "site": "00c412d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "00c416fc",
      "DATA",
      [
        "storage",
        "00c97bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c416fc",
      "DATA",
      [
        "storage",
        "00c97fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c412a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41260.md#insn-00c412a4) · [`00c412c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41260.md#insn-00c412c8) · [`00c41324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41260.md#insn-00c41324)
- 新版 [`00c416cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c416cc) · [`00c416f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c416f0) · [`00c4174c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c4174c)

~~~diff
- 00c412a4 ["INT_ADD", "register:40f0:8", ["const:c412a4:8", "const:4:8"]]
- 00c412a4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c416cc ["INT_ADD", "register:40f0:8", ["const:c416cc:8", "const:4:8"]]
+ 00c416cc ["CALL", null, ["callee:00c5a020:8"]]
- 00c412a4 bytes 5f620094
+ 00c416cc bytes 55620094
- 00c412c8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 00c412c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c412c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c412c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c416f0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00c416f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c416f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c416f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c412c8 bytes 08412f91
+ 00c416f0 bytes 08413f91
- 00c41324 ["INT_ADD", "register:40f0:8", ["const:c41324:8", "const:4:8"]]
- 00c41324 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4174c ["INT_ADD", "register:40f0:8", ["const:c4174c:8", "const:4:8"]]
+ 00c4174c ["CALL", null, ["callee:00c58020:8"]]
- 00c41324 bytes 3f5a0094
+ 00c4174c bytes 355a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2195c8e7a9c0deb62d8ea852e56fa523"></a>

### [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) → [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) FUN_00c41750

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 12件 [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md) [`00c45f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md)
- 新版 呼出元 2件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 12件 [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c46238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) [`00c4632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41a94",
      "incomplete_value": false,
      "site": "00c41a94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4166c",
      "incomplete_value": false,
      "site": "00c4166c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "definition_site": "00c41db0",
      "incomplete_value": false,
      "site": "00c41db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41988",
      "incomplete_value": false,
      "site": "00c41988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4202c",
      "incomplete_value": false,
      "site": "00c4202c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41c04",
      "incomplete_value": false,
      "site": "00c41c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c417b0",
      "DATA",
      [
        "storage",
        "00312a9c",
        "switchD_00c41390::switchdataD_00312a9c",
        "ushort"
      ]
    ],
    [
      "00c418e8",
      "PARAM",
      [
        "storage",
        "002ad1ad",
        null,
        "string"
      ]
    ],
    [
      "00c41900",
      "PARAM",
      [
        "storage",
        "002ac488",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c417b0",
      "DATA",
      [
        "storage",
        "00312adc",
        "switchD_00c417b8::switchdataD_00312adc",
        "ushort"
      ]
    ],
    [
      "00c418e8",
      "PARAM",
      [
        "storage",
        "002ad1ed",
        null,
        "string"
      ]
    ],
    [
      "00c41900",
      "PARAM",
      [
        "storage",
        "002ac4c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md#insn-00c41874) · [`00c4137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md#insn-00c4137c) · [`00c41384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md#insn-00c41384)
- 新版 [`00c41c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md#insn-00c41c9c) · [`00c417a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md#insn-00c417a4)

~~~diff
- 00c41874 ["INT_ADD", "register:40f0:8", ["const:c41874:8", "const:4:8"]]
- 00c41874 ["CALL", null, ["callee:00c3a118:8"]]
+ 00c41c9c ["INT_ADD", "register:40f0:8", ["const:c41c9c:8", "const:4:8"]]
+ 00c41c9c ["CALL", null, ["callee:00c3a118:8"]]
- 00c41874 bytes 1fe1ff97
+ 00c41c9c bytes 1fe1ff97
- 00c4137c ["COPY", "tmp:0:8", ["const:a9c:8"]]
- 00c4137c ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
- 00c4137c ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
- 00c4137c ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
+ 00c417a4 ["COPY", "tmp:0:8", ["const:adc:8"]]
+ 00c417a4 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
+ 00c417a4 ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
+ 00c417a4 ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
- 00c4137c bytes ce712a91
+ 00c417a4 bytes ce712b91
- 00c41384 ["COPY", "register:4078:8", ["const:c41394:8"]]
- 00c41384 bytes 8f000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a232833c15fc157de0bd66f38679e5"></a>

### [`00c41ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md) → [`00c420d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) FUN_00c420d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 3件 [`00c49134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 3件 [`00c4955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c422fc",
      "incomplete_value": false,
      "site": "00c422fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41ed4",
      "incomplete_value": false,
      "site": "00c41ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "definition_site": "00c42324",
      "incomplete_value": false,
      "site": "00c42324",
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
            "const:e5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41efc",
      "incomplete_value": false,
      "site": "00c41efc",
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
            "const:e1b:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c423d4",
      "incomplete_value": false,
      "site": "00c423d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41fac",
      "incomplete_value": false,
      "site": "00c41fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00c422fc",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42324",
      "DATA",
      [
        "storage",
        "002c0e1b",
        null,
        null
      ]
    ],
    [
      "00c423d4",
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c422fc",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42324",
      "DATA",
      [
        "storage",
        "002c0e5b",
        null,
        null
      ]
    ],
    [
      "00c423d4",
      "DATA",
      [
        "storage",
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md#insn-00c41ea4) · [`00c41ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md#insn-00c41ec8) · [`00c41eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md#insn-00c41eec)
- 新版 [`00c422cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c422cc) · [`00c422f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c422f0) · [`00c42314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c42314)

~~~diff
- 00c41ea4 ["INT_ADD", "register:40f0:8", ["const:c41ea4:8", "const:4:8"]]
- 00c41ea4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c422cc ["INT_ADD", "register:40f0:8", ["const:c422cc:8", "const:4:8"]]
+ 00c422cc ["CALL", null, ["callee:00c5a020:8"]]
- 00c41ea4 bytes 5f5f0094
+ 00c422cc bytes 555f0094
- 00c41ec8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c41ec8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c41ec8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c41ec8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c422f0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c422f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c422f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c422f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c41ec8 bytes 4a010991
+ 00c422f0 bytes 4a011991
- 00c41eec ["COPY", "tmp:0:8", ["const:e1b:8"]]
- 00c41eec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c41eec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c41eec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c42314 ["COPY", "tmp:0:8", ["const:e5b:8"]]
+ 00c42314 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c42314 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c42314 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c41eec bytes 4a6d3891
+ 00c42314 bytes 4a6d3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76d5216aa0ab71e5d0f78f9d790832a6"></a>

### [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) → [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) FUN_00c4248c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) · 呼出先 5件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) · 呼出先 5件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42554",
      "incomplete_value": false,
      "site": "00c42554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4212c",
      "incomplete_value": false,
      "site": "00c4212c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "00c42554",
      "DATA",
      [
        "storage",
        "00c98500",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42604",
      "DATA",
      [
        "storage",
        "00c98500",
        null,
        "undefined *"
      ]
    ],
    [
      "00c426b4",
      "DATA",
      [
        "storage",
        "00c98570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42554",
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42604",
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      "00c426b4",
      "DATA",
      [
        "storage",
        "00c98970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c420c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md#insn-00c420c4) · [`00c420d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md#insn-00c420d4) · [`00c420fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md#insn-00c420fc)
- 新版 [`00c424ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c424ec) · [`00c424fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c424fc) · [`00c42524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c42524)

~~~diff
- 00c420c4 ["INT_ADD", "register:40f0:8", ["const:c420c4:8", "const:4:8"]]
- 00c420c4 ["CALL", null, ["callee:00c3dfb0:8"]]
+ 00c424ec ["INT_ADD", "register:40f0:8", ["const:c424ec:8", "const:4:8"]]
+ 00c424ec ["CALL", null, ["callee:00c3dfb0:8"]]
- 00c420c4 bytes b1eeff97
+ 00c424ec bytes b1eeff97
- 00c420d4 ["INT_ADD", "register:40f0:8", ["const:c420d4:8", "const:4:8"]]
- 00c420d4 ["CALL", null, ["local:b0:8"]]
+ 00c424fc ["INT_ADD", "register:40f0:8", ["const:c424fc:8", "const:4:8"]]
+ 00c424fc ["CALL", null, ["local:b0:8"]]
- 00c420d4 bytes e4ffff97
+ 00c424fc bytes e4ffff97
- 00c420fc ["INT_ADD", "register:40f0:8", ["const:c420fc:8", "const:4:8"]]
- 00c420fc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c42524 ["INT_ADD", "register:40f0:8", ["const:c42524:8", "const:4:8"]]
+ 00c42524 ["CALL", null, ["callee:00c5a020:8"]]
- 00c420fc bytes c95e0094
+ 00c42524 bytes bf5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b89b8f658de8b43917f47f15e40dd5d4"></a>

### [`00c422cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c422cc.md) → [`00c426f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md) FUN_00c426f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42758",
      "incomplete_value": true,
      "site": "00c42758",
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
      "definition_site": "00c42330",
      "incomplete_value": true,
      "site": "00c42330",
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
      "00c42758",
      "DATA",
      [
        "storage",
        "00c985e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42758",
      "DATA",
      [
        "storage",
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c422cc.md#insn-00c42300) · [`00c42324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c422cc.md#insn-00c42324) · [`00c4236c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c422cc.md#insn-00c4236c)
- 新版 [`00c42728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c42728) · [`00c4274c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c4274c) · [`00c42794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c42794)

~~~diff
- 00c42300 ["INT_ADD", "register:40f0:8", ["const:c42300:8", "const:4:8"]]
- 00c42300 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c42728 ["INT_ADD", "register:40f0:8", ["const:c42728:8", "const:4:8"]]
+ 00c42728 ["CALL", null, ["callee:00c5a020:8"]]
- 00c42300 bytes 485e0094
+ 00c42728 bytes 3e5e0094
- 00c42324 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00c42324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c42324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c42324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4274c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00c4274c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4274c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4274c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c42324 bytes 08811791
+ 00c4274c bytes 08812791
- 00c4236c ["INT_ADD", "register:40f0:8", ["const:c4236c:8", "const:4:8"]]
- 00c4236c ["CALL", null, ["callee:00c58020:8"]]
+ 00c42794 ["INT_ADD", "register:40f0:8", ["const:c42794:8", "const:4:8"]]
+ 00c42794 ["CALL", null, ["callee:00c58020:8"]]
- 00c4236c bytes 2d560094
+ 00c42794 bytes 23560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6055d82ff1831aab590d48b22d71e93"></a>

### [`00c42370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42370.md) → [`00c42798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md) FUN_00c42798

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c428b4",
      "incomplete_value": false,
      "site": "00c428b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4248c",
      "incomplete_value": false,
      "site": "00c4248c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "00c428b4",
      "DATA",
      [
        "storage",
        "00c98650",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c428b4",
      "DATA",
      [
        "storage",
        "00c98a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42370.md#insn-00c4238c) · [`00c4239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42370.md#insn-00c4239c) · [`00c42458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42370.md#insn-00c42458)
- 新版 [`00c427b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c427b4) · [`00c427c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c427c4) · [`00c42880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c42880)

~~~diff
- 00c4238c ["INT_ADD", "register:40f0:8", ["const:c4238c:8", "const:4:8"]]
- 00c4238c ["CALL", null, ["callee:00c3accc:8"]]
+ 00c427b4 ["INT_ADD", "register:40f0:8", ["const:c427b4:8", "const:4:8"]]
+ 00c427b4 ["CALL", null, ["callee:00c3accc:8"]]
- 00c4238c bytes 46e1ff97
+ 00c427b4 bytes 46e1ff97
- 00c4239c ["INT_ADD", "register:40f0:8", ["const:c4239c:8", "const:4:8"]]
- 00c4239c ["CALL", null, ["callee:00c3fd7c:8"]]
+ 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
+ 00c427c4 ["CALL", null, ["callee:00c3fd7c:8"]]
- 00c4239c bytes 6ef5ff97
+ 00c427c4 bytes 6ef5ff97
- 00c42458 ["INT_ADD", "register:40f0:8", ["const:c42458:8", "const:4:8"]]
- 00c42458 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c42880 ["INT_ADD", "register:40f0:8", ["const:c42880:8", "const:4:8"]]
+ 00c42880 ["CALL", null, ["callee:00c5a020:8"]]
- 00c42458 bytes f25d0094
+ 00c42880 bytes e85d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19e78cbacdb91d9aa383e833ed8a9494"></a>

### [`00c424d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c424d8.md) → [`00c42900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md) FUN_00c42900

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c42968",
      "incomplete_value": false,
      "site": "00c42968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42540",
      "incomplete_value": false,
      "site": "00c42540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42994",
      "incomplete_value": false,
      "site": "00c42994",
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
            "const:e8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4256c",
      "incomplete_value": false,
      "site": "00c4256c",
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
            "const:e4a:8"
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
      "00c42968",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42994",
      "DATA",
      [
        "storage",
        "002b7e4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c42968",
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42994",
      "DATA",
      [
        "storage",
        "002b7e8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c424d8.md#insn-00c42510) · [`00c42530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c424d8.md#insn-00c42530) · [`00c42534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c424d8.md#insn-00c42534)
- 新版 [`00c42938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c42938) · [`00c42958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c42958) · [`00c4295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c4295c)

~~~diff
- 00c42510 ["INT_ADD", "register:40f0:8", ["const:c42510:8", "const:4:8"]]
- 00c42510 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c42938 ["INT_ADD", "register:40f0:8", ["const:c42938:8", "const:4:8"]]
+ 00c42938 ["CALL", null, ["callee:00c5a020:8"]]
- 00c42510 bytes c45d0094
+ 00c42938 bytes ba5d0094
- 00c42530 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c42958 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c42530 bytes a80200b0
+ 00c42958 bytes a80200d0
- 00c42534 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c42534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c42534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c42534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4295c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00c4295c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4295c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4295c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c42534 bytes 08013191
+ 00c4295c bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745258c8c1d7490a7cb8240b34d30e5e"></a>

### [`00c42598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md) → [`00c429c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md) FUN_00c429c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 9件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 9件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42e50",
      "incomplete_value": false,
      "site": "00c42e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42a28",
      "incomplete_value": false,
      "site": "00c42a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c42cac",
      "DATA",
      [
        "storage",
        "00c986c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42d40",
      "DATA",
      [
        "storage",
        "00c98730",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42d40",
      "DATA",
      [
        "storage",
        "00c987a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42cac",
      "DATA",
      [
        "storage",
        "00c98ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42d40",
      "DATA",
      [
        "storage",
        "00c98b30",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42d40",
      "DATA",
      [
        "storage",
        "00c98ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md#insn-00c42634) · [`00c4267c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md#insn-00c4267c) · [`00c426ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md#insn-00c426ac)
- 新版 [`00c42a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42a5c) · [`00c42aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42aa4) · [`00c42ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42ad4)

~~~diff
- 00c42634 ["INT_ADD", "register:40f0:8", ["const:c42634:8", "const:4:8"]]
- 00c42634 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c42a5c ["INT_ADD", "register:40f0:8", ["const:c42a5c:8", "const:4:8"]]
+ 00c42a5c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c42634 bytes 9b5d0094
+ 00c42a5c bytes 915d0094
- 00c4267c ["INT_ADD", "register:40f0:8", ["const:c4267c:8", "const:4:8"]]
- 00c4267c ["CALL", null, ["callee:00c3accc:8"]]
+ 00c42aa4 ["INT_ADD", "register:40f0:8", ["const:c42aa4:8", "const:4:8"]]
+ 00c42aa4 ["CALL", null, ["callee:00c3accc:8"]]
- 00c4267c bytes 8ae0ff97
+ 00c42aa4 bytes 8ae0ff97
- 00c426ac ["INT_ADD", "register:40f0:8", ["const:c426ac:8", "const:4:8"]]
- 00c426ac ["CALL", null, ["callee:00c5a020:8"]]
+ 00c42ad4 ["INT_ADD", "register:40f0:8", ["const:c42ad4:8", "const:4:8"]]
+ 00c42ad4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c426ac bytes 5d5d0094
+ 00c42ad4 bytes 535d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864fb295d9850302cd79ca16e605af68"></a>

### [`00c42a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42a68.md) → [`00c42e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md) FUN_00c42e90

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 8件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 8件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43174",
      "incomplete_value": true,
      "site": "00c43174",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42d4c",
      "incomplete_value": true,
      "site": "00c42d4c",
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
            "const:880:8"
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
      "00c42f9c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43174",
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42f9c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43174",
      "DATA",
      [
        "storage",
        "00c98c80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42a68.md#insn-00c42a90) · [`00c42aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42a68.md#insn-00c42aa0) · [`00c42b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42a68.md#insn-00c42b38)
- 新版 [`00c42eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42eb8) · [`00c42ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42ec8) · [`00c42f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42f60)

~~~diff
- 00c42a90 ["INT_ADD", "register:40f0:8", ["const:c42a90:8", "const:4:8"]]
- 00c42a90 ["CALL", null, ["callee:00c3accc:8"]]
+ 00c42eb8 ["INT_ADD", "register:40f0:8", ["const:c42eb8:8", "const:4:8"]]
+ 00c42eb8 ["CALL", null, ["callee:00c3accc:8"]]
- 00c42a90 bytes 85dfff97
+ 00c42eb8 bytes 85dfff97
- 00c42aa0 ["INT_ADD", "register:40f0:8", ["const:c42aa0:8", "const:4:8"]]
- 00c42aa0 ["CALL", null, ["callee:00c3fd7c:8"]]
+ 00c42ec8 ["INT_ADD", "register:40f0:8", ["const:c42ec8:8", "const:4:8"]]
+ 00c42ec8 ["CALL", null, ["callee:00c3fd7c:8"]]
- 00c42aa0 bytes adf3ff97
+ 00c42ec8 bytes adf3ff97
- 00c42b38 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c42b38 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 00c42b38 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 00c42b38 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 00c42f60 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c42f60 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 00c42f60 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 00c42f60 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 00c42b38 bytes 9c030991
+ 00c42f60 bytes 9c031991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf6c9c766c7072d9ea89de07bdc5ad8"></a>

### [`00c42fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42fb0.md) → [`00c433d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md) FUN_00c433d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4343c",
      "incomplete_value": false,
      "site": "00c4343c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43014",
      "incomplete_value": false,
      "site": "00c43014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "00c4343c",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4343c",
      "DATA",
      [
        "storage",
        "00c98d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42fb0.md#insn-00c42fe4) · [`00c43008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42fb0.md#insn-00c43008) · [`00c43048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42fb0.md#insn-00c43048)
- 新版 [`00c4340c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c4340c) · [`00c43430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c43430) · [`00c43470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c43470)

~~~diff
- 00c42fe4 ["INT_ADD", "register:40f0:8", ["const:c42fe4:8", "const:4:8"]]
- 00c42fe4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4340c ["INT_ADD", "register:40f0:8", ["const:c4340c:8", "const:4:8"]]
+ 00c4340c ["CALL", null, ["callee:00c5a020:8"]]
- 00c42fe4 bytes 0f5b0094
+ 00c4340c bytes 055b0094
- 00c43008 ["COPY", "tmp:0:8", ["const:960:8"]]
- 00c43008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c43430 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c43430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43008 bytes 08812591
+ 00c43430 bytes 08813591
- 00c43048 ["INT_ADD", "register:40f0:8", ["const:c43048:8", "const:4:8"]]
- 00c43048 ["CALL", null, ["callee:00c58020:8"]]
+ 00c43470 ["INT_ADD", "register:40f0:8", ["const:c43470:8", "const:4:8"]]
+ 00c43470 ["CALL", null, ["callee:00c58020:8"]]
- 00c43048 bytes f6520094
+ 00c43470 bytes ec520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5716435df9df45bb60c7d2534afc0c72"></a>

### [`00c4304c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c4304c.md) → [`00c43474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md) FUN_00c43474

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c434dc",
      "incomplete_value": false,
      "site": "00c434dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c430b4",
      "incomplete_value": false,
      "site": "00c430b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "00c434dc",
      "DATA",
      [
        "storage",
        "00c985e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c434dc",
      "DATA",
      [
        "storage",
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c4304c.md#insn-00c43084) · [`00c430a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c4304c.md#insn-00c430a8) · [`00c430f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c4304c.md#insn-00c430f4)
- 新版 [`00c434ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c434ac) · [`00c434d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c434d0) · [`00c4351c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c4351c)

~~~diff
- 00c43084 ["INT_ADD", "register:40f0:8", ["const:c43084:8", "const:4:8"]]
- 00c43084 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c434ac ["INT_ADD", "register:40f0:8", ["const:c434ac:8", "const:4:8"]]
+ 00c434ac ["CALL", null, ["callee:00c5a020:8"]]
- 00c43084 bytes e75a0094
+ 00c434ac bytes dd5a0094
- 00c430a8 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00c430a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c430a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c430a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c434d0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00c434d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c434d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c434d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c430a8 bytes 08811791
+ 00c434d0 bytes 08812791
- 00c430f4 ["INT_ADD", "register:40f0:8", ["const:c430f4:8", "const:4:8"]]
- 00c430f4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4351c ["INT_ADD", "register:40f0:8", ["const:c4351c:8", "const:4:8"]]
+ 00c4351c ["CALL", null, ["callee:00c58020:8"]]
- 00c430f4 bytes cb520094
+ 00c4351c bytes c1520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4e9b4ebc35c2e3d6d15ef0a8841638"></a>

### [`00c431a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md) → [`00c435cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md) FUN_00c435cc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43630",
      "incomplete_value": true,
      "site": "00c43630",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43208",
      "incomplete_value": true,
      "site": "00c43208",
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
            "const:9d0:8"
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
      "00c43630",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43630",
      "DATA",
      [
        "storage",
        "00c98dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c431d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c431d8) · [`00c431fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c431fc) · [`00c43240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c43240)
- 新版 [`00c43600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43600) · [`00c43624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43624) · [`00c43668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43668)

~~~diff
- 00c431d8 ["INT_ADD", "register:40f0:8", ["const:c431d8:8", "const:4:8"]]
- 00c431d8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c43600 ["INT_ADD", "register:40f0:8", ["const:c43600:8", "const:4:8"]]
+ 00c43600 ["CALL", null, ["callee:00c5a020:8"]]
- 00c431d8 bytes 925a0094
+ 00c43600 bytes 885a0094
- 00c431fc ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00c431fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c431fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c431fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c43624 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00c43624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c431fc bytes 08412791
+ 00c43624 bytes 08413791
- 00c43240 ["INT_ADD", "register:40f0:8", ["const:c43240:8", "const:4:8"]]
- 00c43240 ["CALL", null, ["callee:00c58020:8"]]
+ 00c43668 ["INT_ADD", "register:40f0:8", ["const:c43668:8", "const:4:8"]]
+ 00c43668 ["CALL", null, ["callee:00c58020:8"]]
- 00c43240 bytes 78520094
+ 00c43668 bytes 6e520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86eba8b99a903daa1d9e69153735734d"></a>

### [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) → [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) FUN_00c4366c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 7件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 7件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.34% / 新版 97.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43740",
      "incomplete_value": false,
      "site": "00c43740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43318",
      "incomplete_value": false,
      "site": "00c43318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "definition_site": "00c43a40",
      "incomplete_value": false,
      "site": "00c43a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43618",
      "incomplete_value": false,
      "site": "00c43618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43b10",
      "incomplete_value": false,
      "site": "00c43b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c436e8",
      "incomplete_value": false,
      "site": "00c436e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c43740",
      "DATA",
      [
        "storage",
        "00c98c00",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43874",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ],
    [
      "00c438b8",
      "DATA",
      [
        "storage",
        "00c98a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43740",
      "DATA",
      [
        "storage",
        "00c99000",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43874",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c438b8",
      "DATA",
      [
        "storage",
        "00c98e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c432bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md#insn-00c432bc) · [`00c432e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md#insn-00c432e4) · [`00c43308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md#insn-00c43308)
- 新版 [`00c436e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c436e4) · [`00c4370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c4370c) · [`00c43730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c43730)

~~~diff
- 00c432bc ["INT_ADD", "register:40f0:8", ["const:c432bc:8", "const:4:8"]]
- 00c432bc ["CALL", null, ["callee:00c4b7ac:8"]]
+ 00c436e4 ["INT_ADD", "register:40f0:8", ["const:c436e4:8", "const:4:8"]]
+ 00c436e4 ["CALL", null, ["callee:00c4b7ac:8"]]
- 00c432bc bytes 32200094
+ 00c436e4 bytes 32200094
- 00c432e4 ["INT_ADD", "register:40f0:8", ["const:c432e4:8", "const:4:8"]]
- 00c432e4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4370c ["INT_ADD", "register:40f0:8", ["const:c4370c:8", "const:4:8"]]
+ 00c4370c ["CALL", null, ["callee:00c5a020:8"]]
- 00c432e4 bytes 4f5a0094
+ 00c4370c bytes 455a0094
- 00c43308 ["COPY", "register:4050:8", ["const:c98000:8"]]
+ 00c43730 ["COPY", "register:4050:8", ["const:c99000:8"]]
- 00c43308 bytes aa0200b0
+ 00c43730 bytes aa0200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4dbd28f3ca3d9ec91f2d00767a94d5"></a>

### [`00c438b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c438b8.md) → [`00c43ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md) FUN_00c43ce0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43d54",
      "incomplete_value": false,
      "site": "00c43d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4392c",
      "incomplete_value": false,
      "site": "00c4392c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "00c43d54",
      "DATA",
      [
        "storage",
        "00c97770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43d54",
      "DATA",
      [
        "storage",
        "00c97b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c438fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c438b8.md#insn-00c438fc) · [`00c43920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c438b8.md#insn-00c43920) · [`00c43980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c438b8.md#insn-00c43980)
- 新版 [`00c43d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43d24) · [`00c43d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43d48) · [`00c43da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43da8)

~~~diff
- 00c438fc ["INT_ADD", "register:40f0:8", ["const:c438fc:8", "const:4:8"]]
- 00c438fc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c43d24 ["INT_ADD", "register:40f0:8", ["const:c43d24:8", "const:4:8"]]
+ 00c43d24 ["CALL", null, ["callee:00c5a020:8"]]
- 00c438fc bytes c9580094
+ 00c43d24 bytes bf580094
- 00c43920 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00c43920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c43d48 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00c43d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43920 bytes 08c11d91
+ 00c43d48 bytes 08c12d91
- 00c43980 ["INT_ADD", "register:40f0:8", ["const:c43980:8", "const:4:8"]]
- 00c43980 ["CALL", null, ["callee:00c58020:8"]]
+ 00c43da8 ["INT_ADD", "register:40f0:8", ["const:c43da8:8", "const:4:8"]]
+ 00c43da8 ["CALL", null, ["callee:00c58020:8"]]
- 00c43980 bytes a8500094
+ 00c43da8 bytes 9e500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ffa7c923deff180ce193059db2262bc"></a>

### [`00c43e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43e98.md) → [`00c442c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md) FUN_00c442c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44330",
      "incomplete_value": false,
      "site": "00c44330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43f08",
      "incomplete_value": false,
      "site": "00c43f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "00c44330",
      "DATA",
      [
        "storage",
        "00c977e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c44330",
      "DATA",
      [
        "storage",
        "00c97be0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43e98.md#insn-00c43ed8) · [`00c43efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43e98.md#insn-00c43efc) · [`00c43f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43e98.md#insn-00c43f54)
- 新版 [`00c44300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c44300) · [`00c44324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c44324) · [`00c4437c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c4437c)

~~~diff
- 00c43ed8 ["INT_ADD", "register:40f0:8", ["const:c43ed8:8", "const:4:8"]]
- 00c43ed8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c44300 ["INT_ADD", "register:40f0:8", ["const:c44300:8", "const:4:8"]]
+ 00c44300 ["CALL", null, ["callee:00c5a020:8"]]
- 00c43ed8 bytes 52570094
+ 00c44300 bytes 48570094
- 00c43efc ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00c43efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c44324 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00c44324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43efc bytes 08811f91
+ 00c44324 bytes 08812f91
- 00c43f54 ["INT_ADD", "register:40f0:8", ["const:c43f54:8", "const:4:8"]]
- 00c43f54 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4437c ["INT_ADD", "register:40f0:8", ["const:c4437c:8", "const:4:8"]]
+ 00c4437c ["CALL", null, ["callee:00c58020:8"]]
- 00c43f54 bytes 334f0094
+ 00c4437c bytes 294f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f0456e8970b846b59b40f1e73741650"></a>

### [`00c45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md) → [`00c46238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) FUN_00c46238

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 3件 [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c462e0",
      "incomplete_value": false,
      "site": "00c462e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c45eb8",
      "incomplete_value": false,
      "site": "00c45eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "00c462e0",
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c462e0",
      "DATA",
      [
        "storage",
        "00c980b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c45e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45e38) · [`00c45e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45e80) · [`00c45eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45eb0)
- 新版 [`00c46260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c46260) · [`00c462a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c462a8) · [`00c462d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c462d8)

~~~diff
- 00c45e38 ["INT_ADD", "register:40f0:8", ["const:c45e38:8", "const:4:8"]]
- 00c45e38 ["CALL", null, ["callee:00c3ab8c:8"]]
+ 00c46260 ["INT_ADD", "register:40f0:8", ["const:c46260:8", "const:4:8"]]
+ 00c46260 ["CALL", null, ["callee:00c3ab8c:8"]]
- 00c45e38 bytes 4bd2ff97
+ 00c46260 bytes 4bd2ff97
- 00c45e80 ["INT_ADD", "register:40f0:8", ["const:c45e80:8", "const:4:8"]]
- 00c45e80 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c462a8 ["INT_ADD", "register:40f0:8", ["const:c462a8:8", "const:4:8"]]
+ 00c462a8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c45e80 bytes 684f0094
+ 00c462a8 bytes 5e4f0094
- 00c45eb0 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c462d8 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c45eb0 bytes 890200d0
+ 00c462d8 bytes 890200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac38bc96901abe3dedad1ea8ca3d86e"></a>

### [`00c45f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md) → [`00c4632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md) FUN_00c4632c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4639c",
      "incomplete_value": false,
      "site": "00c463a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c45f74",
      "incomplete_value": false,
      "site": "00c45f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00c463a8",
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c463a8",
      "DATA",
      [
        "storage",
        "00c98120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c45f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f38) · [`00c45f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f70) · [`00c45f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f74)
- 新版 [`00c46360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c46360) · [`00c46398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c46398) · [`00c4639c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c4639c)

~~~diff
- 00c45f38 ["INT_ADD", "register:40f0:8", ["const:c45f38:8", "const:4:8"]]
- 00c45f38 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c46360 ["INT_ADD", "register:40f0:8", ["const:c46360:8", "const:4:8"]]
+ 00c46360 ["CALL", null, ["callee:00c5a020:8"]]
- 00c45f38 bytes 3a4f0094
+ 00c46360 bytes 304f0094
- 00c45f70 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c46398 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c45f70 bytes 880200d0
+ 00c46398 bytes 880200d0
- 00c45f74 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00c45f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c45f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c45f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4639c ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00c4639c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4639c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4639c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c45f74 bytes 08813491
+ 00c4639c bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c1d897b7cc8127c9bd34f885ed86cb"></a>

### [`00c45fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md) → [`00c463d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md) FUN_00c463d4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46010",
      "incomplete_value": false,
      "site": "00c46010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00c46438",
      "DATA",
      [
        "storage",
        "00c97ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46438",
      "DATA",
      [
        "storage",
        "00c982e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c45fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c45fe0) · [`00c46000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c46000) · [`00c46004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c46004)
- 新版 [`00c46408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c46408) · [`00c46428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c46428) · [`00c4642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c4642c)

~~~diff
- 00c45fe0 ["INT_ADD", "register:40f0:8", ["const:c45fe0:8", "const:4:8"]]
- 00c45fe0 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c46408 ["INT_ADD", "register:40f0:8", ["const:c46408:8", "const:4:8"]]
+ 00c46408 ["CALL", null, ["callee:00c5a020:8"]]
- 00c45fe0 bytes 104f0094
+ 00c46408 bytes 064f0094
- 00c46000 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c46428 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c46000 bytes 880200b0
+ 00c46428 bytes 880200d0
- 00c46004 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00c46004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4642c ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00c4642c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4642c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4642c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46004 bytes 08813b91
+ 00c4642c bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e23d83f1a758415b58829bd36f5b69"></a>

### [`00c4604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md) → [`00c46474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md) FUN_00c46474

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c464e0",
      "incomplete_value": false,
      "site": "00c464e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c460b8",
      "incomplete_value": false,
      "site": "00c460b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c464e0",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c464e0",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c46080) · [`00c460a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c460a8) · [`00c460b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c460b0)
- 新版 [`00c464a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464a8) · [`00c464d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464d0) · [`00c464d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464d8)

~~~diff
- 00c46080 ["INT_ADD", "register:40f0:8", ["const:c46080:8", "const:4:8"]]
- 00c46080 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c464a8 ["INT_ADD", "register:40f0:8", ["const:c464a8:8", "const:4:8"]]
+ 00c464a8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c46080 bytes e84e0094
+ 00c464a8 bytes de4e0094
- 00c460a8 ["INT_ADD", "register:40f0:8", ["const:c460a8:8", "const:4:8"]]
- 00c460a8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c464d0 ["INT_ADD", "register:40f0:8", ["const:c464d0:8", "const:4:8"]]
+ 00c464d0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c460a8 bytes ce460094
+ 00c464d0 bytes c4460094
- 00c460b0 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c460b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c460b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c460b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c464d8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c464d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c464d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c464d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c460b0 bytes 29010991
+ 00c464d8 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793212faaaacafc9b451c301dfc2c7aa"></a>

### [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) → [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) FUN_00c46520

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 14件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md)
- 新版 呼出元 2件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 14件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46640",
      "incomplete_value": false,
      "site": "00c46640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46218",
      "incomplete_value": false,
      "site": "00c46218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "definition_site": "00c46668",
      "incomplete_value": false,
      "site": "00c46668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46240",
      "incomplete_value": false,
      "site": "00c46240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "definition_site": "00c467f4",
      "incomplete_value": false,
      "site": "00c467f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c463cc",
      "incomplete_value": false,
      "site": "00c463cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "00c46640",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46668",
      "DATA",
      [
        "storage",
        "002b8d48",
        null,
        "string"
      ]
    ],
    [
      "00c467f4",
      "DATA",
      [
        "storage",
        "00c97f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46640",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46668",
      "DATA",
      [
        "storage",
        "002b8d88",
        null,
        "string"
      ]
    ],
    [
      "00c467f4",
      "DATA",
      [
        "storage",
        "00c98350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c467f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md#insn-00c467f4) · [`00c4680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md#insn-00c4680c) · [`00c46830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md#insn-00c46830)
- 新版 [`00c46c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46c1c) · [`00c46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46c34) · [`00c46c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46c58)

~~~diff
- 00c467f4 ["COPY", "tmp:0:8", ["const:e15:8"]]
- 00c467f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c467f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c467f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c46c1c ["COPY", "tmp:0:8", ["const:ee2:8"]]
+ 00c46c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c46c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c46c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c467f4 bytes 00543891
+ 00c46c1c bytes 00883b91
- 00c4680c ["INT_ADD", "register:40f0:8", ["const:c4680c:8", "const:4:8"]]
- 00c4680c ["CALL", null, ["callee:00c3800c:8"]]
+ 00c46c34 ["INT_ADD", "register:40f0:8", ["const:c46c34:8", "const:4:8"]]
+ 00c46c34 ["CALL", null, ["callee:00c3800c:8"]]
- 00c4680c bytes f6c4ff97
+ 00c46c34 bytes f6c4ff97
- 00c46830 ["INT_ADD", "register:40f0:8", ["const:c46830:8", "const:4:8"]]
- 00c46830 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c46c58 ["INT_ADD", "register:40f0:8", ["const:c46c58:8", "const:4:8"]]
+ 00c46c58 ["CALL", null, ["callee:00c3800c:8"]]
- 00c46830 bytes edc4ff97
+ 00c46c58 bytes edc4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35f10d1ade68491bc5cc5b5f27023b7"></a>

### [`00c46878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md) → [`00c46ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md) FUN_00c46ca0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c46d04",
      "incomplete_value": false,
      "site": "00c46d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c468dc",
      "incomplete_value": false,
      "site": "00c468dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
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
      "00c46d04",
      "DATA",
      [
        "storage",
        "00c982d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46d04",
      "DATA",
      [
        "storage",
        "00c986d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c468ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c468ac) · [`00c468d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c468d0) · [`00c46914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c46914)
- 新版 [`00c46cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46cd4) · [`00c46cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46cf8) · [`00c46d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46d3c)

~~~diff
- 00c468ac ["INT_ADD", "register:40f0:8", ["const:c468ac:8", "const:4:8"]]
- 00c468ac ["CALL", null, ["callee:00c5a020:8"]]
+ 00c46cd4 ["INT_ADD", "register:40f0:8", ["const:c46cd4:8", "const:4:8"]]
+ 00c46cd4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c468ac bytes dd4c0094
+ 00c46cd4 bytes d34c0094
- 00c468d0 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00c468d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c468d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c468d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46cf8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00c46cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c468d0 bytes 08410b91
+ 00c46cf8 bytes 08411b91
- 00c46914 ["INT_ADD", "register:40f0:8", ["const:c46914:8", "const:4:8"]]
- 00c46914 ["CALL", null, ["callee:00c58020:8"]]
+ 00c46d3c ["INT_ADD", "register:40f0:8", ["const:c46d3c:8", "const:4:8"]]
+ 00c46d3c ["CALL", null, ["callee:00c58020:8"]]
- 00c46914 bytes c3440094
+ 00c46d3c bytes b9440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba08a8d8924cea1e648f2088255ab690"></a>

### [`00c46918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md) → [`00c46d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md) FUN_00c46d40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46da8",
      "incomplete_value": false,
      "site": "00c46da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46980",
      "incomplete_value": false,
      "site": "00c46980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "00c46da8",
      "DATA",
      [
        "storage",
        "00c98340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46da8",
      "DATA",
      [
        "storage",
        "00c98740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c46950) · [`00c46974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c46974) · [`00c469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c469c0)
- 新版 [`00c46d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46d78) · [`00c46d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46d9c) · [`00c46de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46de8)

~~~diff
- 00c46950 ["INT_ADD", "register:40f0:8", ["const:c46950:8", "const:4:8"]]
- 00c46950 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c46d78 ["INT_ADD", "register:40f0:8", ["const:c46d78:8", "const:4:8"]]
+ 00c46d78 ["CALL", null, ["callee:00c5a020:8"]]
- 00c46950 bytes b44c0094
+ 00c46d78 bytes aa4c0094
- 00c46974 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00c46974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46d9c ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00c46d9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46d9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46d9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46974 bytes 08010d91
+ 00c46d9c bytes 08011d91
- 00c469c0 ["INT_ADD", "register:40f0:8", ["const:c469c0:8", "const:4:8"]]
- 00c469c0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c46de8 ["INT_ADD", "register:40f0:8", ["const:c46de8:8", "const:4:8"]]
+ 00c46de8 ["CALL", null, ["callee:00c58020:8"]]
- 00c469c0 bytes 98440094
+ 00c46de8 bytes 8e440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df8346806df88d4ca82044857aa802ee"></a>

### [`00c46d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md) → [`00c47190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md) FUN_00c47190

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c472b4",
      "incomplete_value": false,
      "site": "00c472cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46e8c",
      "incomplete_value": false,
      "site": "00c46ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "00c472b4",
      "PARAM",
      [
        "storage",
        "002b8d40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c472b4",
      "PARAM",
      [
        "storage",
        "002b8d80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46ea4) · [`00c46e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46e8c) · [`00c46ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46ed8)
- 新版 [`00c472cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c472cc) · [`00c472b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c472b4) · [`00c47300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c47300)

~~~diff
- 00c46ea4 ["INT_ADD", "register:40f0:8", ["const:c46ea4:8", "const:4:8"]]
- 00c46ea4 ["CALL", null, ["callee:00c5e100:8"]]
+ 00c472cc ["INT_ADD", "register:40f0:8", ["const:c472cc:8", "const:4:8"]]
+ 00c472cc ["CALL", null, ["callee:00c5e100:8"]]
- 00c46ea4 bytes 975b0094
+ 00c472cc bytes 8d5b0094
- 00c46e8c ["COPY", "tmp:0:8", ["const:d40:8"]]
- 00c46e8c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c46e8c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c46e8c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c472b4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00c472b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c472b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c472b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c46e8c bytes 42003591
+ 00c472b4 bytes 42003691
- 00c46ed8 ["INT_ADD", "register:40f0:8", ["const:c46ed8:8", "const:4:8"]]
- 00c46ed8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c47300 ["INT_ADD", "register:40f0:8", ["const:c47300:8", "const:4:8"]]
+ 00c47300 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c46ed8 bytes 724b0094
+ 00c47300 bytes 684b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb87ce39a9ead023e36823453f6d31ee"></a>

### [`00c46f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md) → [`00c4734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md) FUN_00c4734c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47488",
      "incomplete_value": false,
      "site": "00c47498",
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
            "const:51d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47060",
      "incomplete_value": false,
      "site": "00c47070",
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
            "const:4dd:8"
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
      "00c47488",
      "PARAM",
      [
        "storage",
        "002ac4dd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47488",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c47070) · [`00c47060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c47060) · [`00c470a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c470a4)
- 新版 [`00c47498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c47498) · [`00c47488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c47488) · [`00c474cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c474cc)

~~~diff
- 00c47070 ["INT_ADD", "register:40f0:8", ["const:c47070:8", "const:4:8"]]
- 00c47070 ["CALL", null, ["callee:00c5e100:8"]]
+ 00c47498 ["INT_ADD", "register:40f0:8", ["const:c47498:8", "const:4:8"]]
+ 00c47498 ["CALL", null, ["callee:00c5e100:8"]]
- 00c47070 bytes 245b0094
+ 00c47498 bytes 1a5b0094
- 00c47060 ["COPY", "tmp:0:8", ["const:4dd:8"]]
- 00c47060 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47060 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47060 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47488 ["COPY", "tmp:0:8", ["const:51d:8"]]
+ 00c47488 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47488 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47488 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47060 bytes 42741391
+ 00c47488 bytes 42741491
- 00c470a4 ["INT_ADD", "register:40f0:8", ["const:c470a4:8", "const:4:8"]]
- 00c470a4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c474cc ["INT_ADD", "register:40f0:8", ["const:c474cc:8", "const:4:8"]]
+ 00c474cc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c470a4 bytes ff4a0094
+ 00c474cc bytes f54a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d818e6cb5882fd15a77ce0c14fa41392"></a>

### [`00c470f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md) → [`00c47518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md) FUN_00c47518

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4768c",
      "incomplete_value": false,
      "site": "00c476a0",
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
            "const:e4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47264",
      "incomplete_value": false,
      "site": "00c47278",
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
            "const:e0e:8"
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
      "00c4768c",
      "PARAM",
      [
        "storage",
        "002b9e0e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4768c",
      "PARAM",
      [
        "storage",
        "002b9e4e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c47278) · [`00c47264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c47264) · [`00c472ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c472ac)
- 新版 [`00c476a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c476a0) · [`00c4768c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c4768c) · [`00c476d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c476d4)

~~~diff
- 00c47278 ["INT_ADD", "register:40f0:8", ["const:c47278:8", "const:4:8"]]
- 00c47278 ["CALL", null, ["callee:00c5e100:8"]]
+ 00c476a0 ["INT_ADD", "register:40f0:8", ["const:c476a0:8", "const:4:8"]]
+ 00c476a0 ["CALL", null, ["callee:00c5e100:8"]]
- 00c47278 bytes a25a0094
+ 00c476a0 bytes 985a0094
- 00c47264 ["COPY", "tmp:0:8", ["const:e0e:8"]]
- 00c47264 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47264 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47264 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c4768c ["COPY", "tmp:0:8", ["const:e4e:8"]]
+ 00c4768c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c4768c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c4768c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47264 bytes 42383891
+ 00c4768c bytes 42383991
- 00c472ac ["INT_ADD", "register:40f0:8", ["const:c472ac:8", "const:4:8"]]
- 00c472ac ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c476d4 ["INT_ADD", "register:40f0:8", ["const:c476d4:8", "const:4:8"]]
+ 00c476d4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c472ac bytes 7d4a0094
+ 00c476d4 bytes 734a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f359ad797969920233850e4253c7be94"></a>

### [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) → [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) FUN_00c47834

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) · 呼出先 14件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md)
- 新版 呼出元 3件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 14件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47950",
      "incomplete_value": false,
      "site": "00c47950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47528",
      "incomplete_value": false,
      "site": "00c47528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "definition_site": "00c47a28",
      "incomplete_value": false,
      "site": "00c47a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47600",
      "incomplete_value": false,
      "site": "00c47600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47ae8",
      "incomplete_value": false,
      "site": "00c47ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c476c0",
      "incomplete_value": false,
      "site": "00c476c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c47950",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47a28",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47ae8",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47950",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47a28",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47ae8",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md#insn-00c47d38) · [`00c474a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md#insn-00c474a8) · [`00c474bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md#insn-00c474bc)
- 新版 [`00c48160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c48160) · [`00c478d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c478d0) · [`00c478e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c478e4)

~~~diff
- 00c47d38 ["INT_ADD", "register:40f0:8", ["const:c47d38:8", "const:4:8"]]
- 00c47d38 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c48160 ["INT_ADD", "register:40f0:8", ["const:c48160:8", "const:4:8"]]
+ 00c48160 ["CALL", null, ["callee:00c3800c:8"]]
- 00c47d38 bytes abbfff97
+ 00c48160 bytes abbfff97
- 00c474a8 ["INT_ADD", "register:40f0:8", ["const:c474a8:8", "const:4:8"]]
- 00c474a8 ["CALL", null, ["local:b0:8"]]
+ 00c478d0 ["INT_ADD", "register:40f0:8", ["const:c478d0:8", "const:4:8"]]
+ 00c478d0 ["CALL", null, ["local:b0:8"]]
- 00c474a8 bytes d9ffff97
+ 00c478d0 bytes d9ffff97
- 00c474bc ["INT_ADD", "register:40f0:8", ["const:c474bc:8", "const:4:8"]]
- 00c474bc ["CALL", null, ["callee:00c4844c:8"]]
+ 00c478e4 ["INT_ADD", "register:40f0:8", ["const:c478e4:8", "const:4:8"]]
+ 00c478e4 ["CALL", null, ["callee:00c4844c:8"]]
- 00c474bc bytes da020094
+ 00c478e4 bytes da020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc0ec871bdd8b6c36d588e7338304d0"></a>

### [`00c47d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47d78.md) → [`00c481a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md) FUN_00c481a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4821c",
      "incomplete_value": false,
      "site": "00c4821c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47df4",
      "incomplete_value": false,
      "site": "00c47df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "00c4821c",
      "DATA",
      [
        "storage",
        "00c98260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4821c",
      "DATA",
      [
        "storage",
        "00c98660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47d78.md#insn-00c47dc4) · [`00c47de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47d78.md#insn-00c47de8) · [`00c47e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47d78.md#insn-00c47e54)
- 新版 [`00c481ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c481ec) · [`00c48210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c48210) · [`00c4827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c4827c)

~~~diff
- 00c47dc4 ["INT_ADD", "register:40f0:8", ["const:c47dc4:8", "const:4:8"]]
- 00c47dc4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c481ec ["INT_ADD", "register:40f0:8", ["const:c481ec:8", "const:4:8"]]
+ 00c481ec ["CALL", null, ["callee:00c5a020:8"]]
- 00c47dc4 bytes 97470094
+ 00c481ec bytes 8d470094
- 00c47de8 ["COPY", "tmp:0:8", ["const:260:8"]]
- 00c47de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c47de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c47de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c48210 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00c48210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c48210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c48210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c47de8 bytes 08810991
+ 00c48210 bytes 08811991
- 00c47e54 ["INT_ADD", "register:40f0:8", ["const:c47e54:8", "const:4:8"]]
- 00c47e54 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4827c ["INT_ADD", "register:40f0:8", ["const:c4827c:8", "const:4:8"]]
+ 00c4827c ["CALL", null, ["callee:00c58020:8"]]
- 00c47e54 bytes 733f0094
+ 00c4827c bytes 693f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9ea09dcd0e53098b4fad61f4db01e1"></a>

### [`00c47e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md) → [`00c48280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md) FUN_00c48280

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c482dc",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47eb4",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:e15:8"
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
      "definition_site": "00c482e4",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:896:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47ebc",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:856:8"
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
      "definition_site": "00c482ec",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47ec4",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:30e:8"
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
      "00c482dc",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ],
    [
      "00c482e4",
      "PARAM",
      [
        "storage",
        "002b2856",
        null,
        "string"
      ]
    ],
    [
      "00c482ec",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c482dc",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c482e4",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c482ec",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47ecc) · [`00c47eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47eb4) · [`00c47ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47ebc)
- 新版 [`00c482f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482f4) · [`00c482dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482dc) · [`00c482e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482e4)

~~~diff
- 00c47ecc ["INT_ADD", "register:40f0:8", ["const:c47ecc:8", "const:4:8"]]
- 00c47ecc ["CALL", null, ["callee:00c3800c:8"]]
+ 00c482f4 ["INT_ADD", "register:40f0:8", ["const:c482f4:8", "const:4:8"]]
+ 00c482f4 ["CALL", null, ["callee:00c3800c:8"]]
- 00c47ecc bytes 46bfff97
+ 00c482f4 bytes 46bfff97
- 00c47eb4 ["COPY", "tmp:0:8", ["const:e15:8"]]
- 00c47eb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c47eb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c47eb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c482dc ["COPY", "tmp:0:8", ["const:ee2:8"]]
+ 00c482dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c482dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c482dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c47eb4 bytes 00543891
+ 00c482dc bytes 00883b91
- 00c47ebc ["COPY", "tmp:0:8", ["const:856:8"]]
- 00c47ebc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c47ebc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c47ebc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c482e4 ["COPY", "tmp:0:8", ["const:896:8"]]
+ 00c482e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c482e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c482e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c47ebc bytes 21582191
+ 00c482e4 bytes 21582291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1b723d635de5ed9d0d42a05bca622f6"></a>

### [`00c48024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md) → [`00c4844c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md) FUN_00c4844c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c484b0",
      "incomplete_value": false,
      "site": "00c484b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48088",
      "incomplete_value": false,
      "site": "00c48088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "00c484b0",
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c484b0",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c48058) · [`00c4807c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c4807c) · [`00c480c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c480c0)
- 新版 [`00c48480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c48480) · [`00c484a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c484a4) · [`00c484e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c484e8)

~~~diff
- 00c48058 ["INT_ADD", "register:40f0:8", ["const:c48058:8", "const:4:8"]]
- 00c48058 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c48480 ["INT_ADD", "register:40f0:8", ["const:c48480:8", "const:4:8"]]
+ 00c48480 ["CALL", null, ["callee:00c5a020:8"]]
- 00c48058 bytes f2460094
+ 00c48480 bytes e8460094
- 00c4807c ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00c4807c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4807c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4807c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c484a4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c484a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c484a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c484a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4807c bytes 08c10791
+ 00c484a4 bytes 08c11791
- 00c480c0 ["INT_ADD", "register:40f0:8", ["const:c480c0:8", "const:4:8"]]
- 00c480c0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c484e8 ["INT_ADD", "register:40f0:8", ["const:c484e8:8", "const:4:8"]]
+ 00c484e8 ["CALL", null, ["callee:00c58020:8"]]
- 00c480c0 bytes d83e0094
+ 00c484e8 bytes ce3e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4192b398af78f1542d0a1ff6da84430"></a>

### [`00c482f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md) → [`00c48720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md) FUN_00c48720

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48778",
      "incomplete_value": true,
      "site": "00c48784",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48350",
      "incomplete_value": true,
      "site": "00c4835c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd1:8"
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
      "00c48778",
      "READ",
      [
        "storage",
        "002a1cd1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48778",
      "READ",
      [
        "storage",
        "002a1d9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c48334) · [`00c48348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c48348) · [`00c4837c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c4837c)
- 新版 [`00c4875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c4875c) · [`00c48770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c48770) · [`00c487a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c487a4)

~~~diff
- 00c48334 ["INT_ADD", "register:40f0:8", ["const:c48334:8", "const:4:8"]]
- 00c48334 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4875c ["INT_ADD", "register:40f0:8", ["const:c4875c:8", "const:4:8"]]
+ 00c4875c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48334 bytes 5b460094
+ 00c4875c bytes 51460094
- 00c48348 ["COPY", "tmp:0:8", ["const:cd1:8"]]
- 00c48348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c48348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c48348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c48770 ["COPY", "tmp:0:8", ["const:d9e:8"]]
+ 00c48770 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48770 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48770 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c48348 bytes 29453391
+ 00c48770 bytes 29793691
- 00c4837c ["INT_ADD", "register:40f0:8", ["const:c4837c:8", "const:4:8"]]
- 00c4837c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c487a4 ["INT_ADD", "register:40f0:8", ["const:c487a4:8", "const:4:8"]]
+ 00c487a4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4837c bytes 714a0094
+ 00c487a4 bytes 674a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15a060219703ca5ad7f9cf93fc41284"></a>

### [`00c48648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md) → [`00c48a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md) FUN_00c48a70

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48ad8",
      "incomplete_value": true,
      "site": "00c48ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c486b0",
      "incomplete_value": true,
      "site": "00c486bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
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
      "definition_site": "00c48b44",
      "incomplete_value": true,
      "site": "00c48b50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:943:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4871c",
      "incomplete_value": true,
      "site": "00c48728",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:903:8"
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
      "00c48ad8",
      "READ",
      [
        "storage",
        "002bfb10",
        null,
        "string"
      ]
    ],
    [
      "00c48b44",
      "READ",
      [
        "storage",
        "002b0903",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48ad8",
      "READ",
      [
        "storage",
        "002bfb50",
        null,
        "string"
      ]
    ],
    [
      "00c48b44",
      "READ",
      [
        "storage",
        "002b0943",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md#insn-00c48694) · [`00c486a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md#insn-00c486a8) · [`00c486d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md#insn-00c486d4)
- 新版 [`00c48abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48abc) · [`00c48ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48ad0) · [`00c48afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48afc)

~~~diff
- 00c48694 ["INT_ADD", "register:40f0:8", ["const:c48694:8", "const:4:8"]]
- 00c48694 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48abc ["INT_ADD", "register:40f0:8", ["const:c48abc:8", "const:4:8"]]
+ 00c48abc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c48694 bytes 83450094
+ 00c48abc bytes 79450094
- 00c486a8 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00c486a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c486a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c486a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c48ad0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00c48ad0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48ad0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48ad0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c486a8 bytes 29412c91
+ 00c48ad0 bytes 29412d91
- 00c486d4 ["INT_ADD", "register:40f0:8", ["const:c486d4:8", "const:4:8"]]
- 00c486d4 ["CALL", null, ["callee:00c45144:8"]]
+ 00c48afc ["INT_ADD", "register:40f0:8", ["const:c48afc:8", "const:4:8"]]
+ 00c48afc ["CALL", null, ["callee:00c45144:8"]]
- 00c486d4 bytes 92f1ff97
+ 00c48afc bytes 92f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6998999bcb7e09480c79bdf59350802a"></a>

### [`00c48764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md) → [`00c48b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md) FUN_00c48b8c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48c2c",
      "incomplete_value": true,
      "site": "00c48c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48804",
      "incomplete_value": true,
      "site": "00c48814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
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
      "00c48c2c",
      "READ",
      [
        "storage",
        "002c0e10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48c2c",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c48790) · [`00c487b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c487b4) · [`00c487e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c487e8)
- 新版 [`00c48bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48bb8) · [`00c48bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48bdc) · [`00c48c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48c10)

~~~diff
- 00c48790 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48790 ["INT_ADD", "register:40f0:8", ["const:c48790:8", "const:4:8"]]
- 00c48790 ["CALLIND", null, ["register:0:8"]]
+ 00c48bb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48bb8 ["INT_ADD", "register:40f0:8", ["const:c48bb8:8", "const:4:8"]]
+ 00c48bb8 ["CALLIND", null, ["register:0:8"]]
- 00c48790 bytes 00013fd6
+ 00c48bb8 bytes 00013fd6
- 00c487b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c487b4 ["INT_ADD", "register:40f0:8", ["const:c487b4:8", "const:4:8"]]
- 00c487b4 ["CALLIND", null, ["register:0:8"]]
+ 00c48bdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48bdc ["INT_ADD", "register:40f0:8", ["const:c48bdc:8", "const:4:8"]]
+ 00c48bdc ["CALLIND", null, ["register:0:8"]]
- 00c487b4 bytes 00013fd6
+ 00c48bdc bytes 00013fd6
- 00c487e8 ["INT_ADD", "register:40f0:8", ["const:c487e8:8", "const:4:8"]]
- 00c487e8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c48c10 ["INT_ADD", "register:40f0:8", ["const:c48c10:8", "const:4:8"]]
+ 00c48c10 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c487e8 bytes 2e450094
+ 00c48c10 bytes 24450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a964868bd6bb56e8f4cdcd8c635c9b"></a>

### [`00c49134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md) → [`00c4955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) FUN_00c4955c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c420d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c495c0",
      "incomplete_value": false,
      "site": "00c495c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c49198",
      "incomplete_value": false,
      "site": "00c49198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00c495c0",
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c495c0",
      "DATA",
      [
        "storage",
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c49168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md#insn-00c49168) · [`00c4918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md#insn-00c4918c) · [`00c491d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md#insn-00c491d0)
- 新版 [`00c49590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c49590) · [`00c495b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c495b4) · [`00c495f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c495f8)

~~~diff
- 00c49168 ["INT_ADD", "register:40f0:8", ["const:c49168:8", "const:4:8"]]
- 00c49168 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c49590 ["INT_ADD", "register:40f0:8", ["const:c49590:8", "const:4:8"]]
+ 00c49590 ["CALL", null, ["callee:00c5a020:8"]]
- 00c49168 bytes ae420094
+ 00c49590 bytes a4420094
- 00c4918c ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00c4918c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4918c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4918c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c495b4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00c495b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c495b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c495b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4918c bytes 08c10e91
+ 00c495b4 bytes 08c11e91
- 00c491d0 ["INT_ADD", "register:40f0:8", ["const:c491d0:8", "const:4:8"]]
- 00c491d0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c495f8 ["INT_ADD", "register:40f0:8", ["const:c495f8:8", "const:4:8"]]
+ 00c495f8 ["CALL", null, ["callee:00c58020:8"]]
- 00c491d0 bytes 943a0094
+ 00c495f8 bytes 8a3a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb6ab2710e7d25bdc946497628cab4d2"></a>

### [`00c492c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md) → [`00c496f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md) FUN_00c496f0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c498d0",
      "incomplete_value": false,
      "site": "00c498d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c494a8",
      "incomplete_value": false,
      "site": "00c494ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "definition_site": "00c49c08",
      "incomplete_value": false,
      "site": "00c49c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c497e0",
      "incomplete_value": false,
      "site": "00c497e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "00c498d4",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      "00c49c0c",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c498d4",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ],
    [
      "00c49c0c",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md#insn-00c4931c) · [`00c49398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md#insn-00c49398) · [`00c493c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md#insn-00c493c8)
- 新版 [`00c49744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c49744) · [`00c497c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c497c0) · [`00c497f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c497f0)

~~~diff
- 00c4931c ["INT_ADD", "register:40f0:8", ["const:c4931c:8", "const:4:8"]]
- 00c4931c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c49744 ["INT_ADD", "register:40f0:8", ["const:c49744:8", "const:4:8"]]
+ 00c49744 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4931c bytes 61420094
+ 00c49744 bytes 57420094
- 00c49398 ["INT_ADD", "register:40f0:8", ["const:c49398:8", "const:4:8"]]
- 00c49398 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c497c0 ["INT_ADD", "register:40f0:8", ["const:c497c0:8", "const:4:8"]]
+ 00c497c0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c49398 bytes 42420094
+ 00c497c0 bytes 38420094
- 00c493c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c493c8 ["INT_ADD", "register:40f0:8", ["const:c493c8:8", "const:4:8"]]
- 00c493c8 ["CALLIND", null, ["register:0:8"]]
+ 00c497f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c497f0 ["INT_ADD", "register:40f0:8", ["const:c497f0:8", "const:4:8"]]
+ 00c497f0 ["CALLIND", null, ["register:0:8"]]
- 00c493c8 bytes 00013fd6
+ 00c497f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1ae2f0b4bb1928a943926382f576c4"></a>

### [`00c4a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a3f0.md) → [`00c4a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md) FUN_00c4a818

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a9d8",
      "incomplete_value": true,
      "site": "00c4a9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4a5b0",
      "incomplete_value": true,
      "site": "00c4a5bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b0:8"
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
      "00c4a9d8",
      "READ",
      [
        "storage",
        "002b18b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4a9d8",
      "READ",
      [
        "storage",
        "002b18f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4a438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a3f0.md#insn-00c4a438) · [`00c4a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a3f0.md#insn-00c4a4a4) · [`00c4a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a3f0.md#insn-00c4a4d8)
- 新版 [`00c4a860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a860) · [`00c4a8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a8cc) · [`00c4a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a900)

~~~diff
- 00c4a438 ["INT_ADD", "register:40f0:8", ["const:c4a438:8", "const:4:8"]]
- 00c4a438 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a860 ["INT_ADD", "register:40f0:8", ["const:c4a860:8", "const:4:8"]]
+ 00c4a860 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a438 bytes 1a3e0094
+ 00c4a860 bytes 103e0094
- 00c4a4a4 ["INT_ADD", "register:40f0:8", ["const:c4a4a4:8", "const:4:8"]]
- 00c4a4a4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4a8cc ["INT_ADD", "register:40f0:8", ["const:c4a8cc:8", "const:4:8"]]
+ 00c4a8cc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a4a4 bytes ff3d0094
+ 00c4a8cc bytes f53d0094
- 00c4a4d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a4d8 ["INT_ADD", "register:40f0:8", ["const:c4a4d8:8", "const:4:8"]]
- 00c4a4d8 ["CALLIND", null, ["register:0:8"]]
+ 00c4a900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a900 ["INT_ADD", "register:40f0:8", ["const:c4a900:8", "const:4:8"]]
+ 00c4a900 ["CALLIND", null, ["register:0:8"]]
- 00c4a4d8 bytes 00013fd6
+ 00c4a900 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1864f6700b9d0687618a57f02dfa6775"></a>

### [`00c4a6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md) → [`00c4ab04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md) FUN_00c4ab04

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ab68",
      "incomplete_value": true,
      "site": "00c4ab78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:302:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4a740",
      "incomplete_value": true,
      "site": "00c4a750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c2:8"
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
      "00c4ab68",
      "READ",
      [
        "storage",
        "002bc2c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ab68",
      "READ",
      [
        "storage",
        "002bc302",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a720) · [`00c4a738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a738) · [`00c4a770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a770)
- 新版 [`00c4ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab48) · [`00c4ab60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab60) · [`00c4ab98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab98)

~~~diff
- 00c4a720 ["INT_ADD", "register:40f0:8", ["const:c4a720:8", "const:4:8"]]
- 00c4a720 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ab48 ["INT_ADD", "register:40f0:8", ["const:c4ab48:8", "const:4:8"]]
+ 00c4ab48 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a720 bytes 603d0094
+ 00c4ab48 bytes 563d0094
- 00c4a738 ["COPY", "tmp:0:8", ["const:2c2:8"]]
- 00c4a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4ab60 ["COPY", "tmp:0:8", ["const:302:8"]]
+ 00c4ab60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ab60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ab60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4a738 bytes 4a090b91
+ 00c4ab60 bytes 4a090c91
- 00c4a770 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a770 ["INT_ADD", "register:40f0:8", ["const:c4a770:8", "const:4:8"]]
- 00c4a770 ["CALLIND", null, ["register:0:8"]]
+ 00c4ab98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ab98 ["INT_ADD", "register:40f0:8", ["const:c4ab98:8", "const:4:8"]]
+ 00c4ab98 ["CALLIND", null, ["register:0:8"]]
- 00c4a770 bytes 00013fd6
+ 00c4ab98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-749e9d940baf5b82e4660f0a19ca0180"></a>

### [`00c4a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md) → [`00c4ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md) FUN_00c4ac28

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ac8c",
      "incomplete_value": true,
      "site": "00c4ac9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4a864",
      "incomplete_value": true,
      "site": "00c4a874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
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
      "00c4ac8c",
      "READ",
      [
        "storage",
        "002c0e10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ac8c",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4a844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a844) · [`00c4a85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a85c) · [`00c4a894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a894)
- 新版 [`00c4ac6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4ac6c) · [`00c4ac84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4ac84) · [`00c4acbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4acbc)

~~~diff
- 00c4a844 ["INT_ADD", "register:40f0:8", ["const:c4a844:8", "const:4:8"]]
- 00c4a844 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ac6c ["INT_ADD", "register:40f0:8", ["const:c4ac6c:8", "const:4:8"]]
+ 00c4ac6c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4a844 bytes 173d0094
+ 00c4ac6c bytes 0d3d0094
- 00c4a85c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00c4a85c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4a85c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4a85c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4ac84 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00c4ac84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ac84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ac84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4a85c bytes 4a413891
+ 00c4ac84 bytes 4a413991
- 00c4a894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a894 ["INT_ADD", "register:40f0:8", ["const:c4a894:8", "const:4:8"]]
- 00c4a894 ["CALLIND", null, ["register:0:8"]]
+ 00c4acbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4acbc ["INT_ADD", "register:40f0:8", ["const:c4acbc:8", "const:4:8"]]
+ 00c4acbc ["CALLIND", null, ["register:0:8"]]
- 00c4a894 bytes 00013fd6
+ 00c4acbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09f1dc32541568f0ddac73e8d4a7cd81"></a>

### [`00c4ac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md) → [`00c4b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md) FUN_00c4b0a4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b1c4",
      "incomplete_value": true,
      "site": "00c4b1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ad9c",
      "incomplete_value": true,
      "site": "00c4ada8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e64:8"
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
      "00c4b1c4",
      "READ",
      [
        "storage",
        "002b7e64",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4b1c4",
      "READ",
      [
        "storage",
        "002b7ea4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4aca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md#insn-00c4aca8) · [`00c4accc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md#insn-00c4accc) · [`00c4acf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md#insn-00c4acf8)
- 新版 [`00c4b0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b0d0) · [`00c4b0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b0f4) · [`00c4b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b120)

~~~diff
- 00c4aca8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4aca8 ["INT_ADD", "register:40f0:8", ["const:c4aca8:8", "const:4:8"]]
- 00c4aca8 ["CALLIND", null, ["register:0:8"]]
+ 00c4b0d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b0d0 ["INT_ADD", "register:40f0:8", ["const:c4b0d0:8", "const:4:8"]]
+ 00c4b0d0 ["CALLIND", null, ["register:0:8"]]
- 00c4aca8 bytes 00013fd6
+ 00c4b0d0 bytes 00013fd6
- 00c4accc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4accc ["INT_ADD", "register:40f0:8", ["const:c4accc:8", "const:4:8"]]
- 00c4accc ["CALLIND", null, ["register:0:8"]]
+ 00c4b0f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b0f4 ["INT_ADD", "register:40f0:8", ["const:c4b0f4:8", "const:4:8"]]
+ 00c4b0f4 ["CALLIND", null, ["register:0:8"]]
- 00c4accc bytes 00013fd6
+ 00c4b0f4 bytes 00013fd6
- 00c4acf8 ["INT_ADD", "register:40f0:8", ["const:c4acf8:8", "const:4:8"]]
- 00c4acf8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4b120 ["INT_ADD", "register:40f0:8", ["const:c4b120:8", "const:4:8"]]
+ 00c4b120 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4acf8 bytes ea3b0094
+ 00c4b120 bytes e03b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a68483ec71ee3bdc0a303f559e2dab"></a>

### [`00c4af8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md) → [`00c4b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md) FUN_00c4b3b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b41c",
      "incomplete_value": true,
      "site": "00c4b428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4aff4",
      "incomplete_value": true,
      "site": "00c4b000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b4a8",
      "incomplete_value": false,
      "site": "00c4b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b080",
      "incomplete_value": false,
      "site": "00c4b084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "00c4b41c",
      "READ",
      [
        "storage",
        "002ac540",
        null,
        "string"
      ]
    ],
    [
      "00c4b4ac",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4b41c",
      "READ",
      [
        "storage",
        "002ac580",
        null,
        "string"
      ]
    ],
    [
      "00c4b4ac",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4afd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md#insn-00c4afd4) · [`00c4afec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md#insn-00c4afec) · [`00c4b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md#insn-00c4b040)
- 新版 [`00c4b3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b3fc) · [`00c4b414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b414) · [`00c4b468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b468)

~~~diff
- 00c4afd4 ["INT_ADD", "register:40f0:8", ["const:c4afd4:8", "const:4:8"]]
- 00c4afd4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4b3fc ["INT_ADD", "register:40f0:8", ["const:c4b3fc:8", "const:4:8"]]
+ 00c4b3fc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4afd4 bytes 333b0094
+ 00c4b3fc bytes 293b0094
- 00c4afec ["COPY", "tmp:0:8", ["const:540:8"]]
- 00c4afec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4afec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4afec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4b414 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00c4b414 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4b414 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4b414 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4afec bytes 4a011591
+ 00c4b414 bytes 4a011691
- 00c4b040 ["INT_ADD", "register:40f0:8", ["const:c4b040:8", "const:4:8"]]
- 00c4b040 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4b468 ["INT_ADD", "register:40f0:8", ["const:c4b468:8", "const:4:8"]]
+ 00c4b468 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4b040 bytes 183b0094
+ 00c4b468 bytes 0e3b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ffdf7c07481bb2d9a69ad9feff0b758"></a>

### [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) → [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) FUN_00c4b7ac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 6件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) [`00c4b734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 6件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b8ac",
      "incomplete_value": false,
      "site": "00c4b8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b484",
      "incomplete_value": false,
      "site": "00c4b484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
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
      "definition_site": "00c4b954",
      "incomplete_value": false,
      "site": "00c4b954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b52c",
      "incomplete_value": false,
      "site": "00c4b52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00c4ba14",
      "incomplete_value": false,
      "site": "00c4ba14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b5ec",
      "incomplete_value": false,
      "site": "00c4b5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
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
      "00c4b8ac",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4b954",
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ba14",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4b8ac",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4b954",
      "DATA",
      [
        "storage",
        "00c98eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ba14",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md#insn-00c4b3f0) · [`00c4b400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md#insn-00c4b400) · [`00c4b42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md#insn-00c4b42c)
- 新版 [`00c4b818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b818) · [`00c4b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b828) · [`00c4b854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b854)

~~~diff
- 00c4b3f0 ["INT_ADD", "register:40f0:8", ["const:c4b3f0:8", "const:4:8"]]
- 00c4b3f0 ["CALL", null, ["callee:00c4bb5c:8"]]
+ 00c4b818 ["INT_ADD", "register:40f0:8", ["const:c4b818:8", "const:4:8"]]
+ 00c4b818 ["CALL", null, ["callee:00c4bb5c:8"]]
- 00c4b3f0 bytes d1000094
+ 00c4b818 bytes d1000094
- 00c4b400 ["INT_ADD", "register:40f0:8", ["const:c4b400:8", "const:4:8"]]
- 00c4b400 ["CALL", null, ["callee:00c3dfb0:8"]]
+ 00c4b828 ["INT_ADD", "register:40f0:8", ["const:c4b828:8", "const:4:8"]]
+ 00c4b828 ["CALL", null, ["callee:00c3dfb0:8"]]
- 00c4b400 bytes e2c9ff97
+ 00c4b828 bytes e2c9ff97
- 00c4b42c ["INT_ADD", "register:40f0:8", ["const:c4b42c:8", "const:4:8"]]
- 00c4b42c ["CALL", null, ["callee:00c3e5c4:8"]]
+ 00c4b854 ["INT_ADD", "register:40f0:8", ["const:c4b854:8", "const:4:8"]]
+ 00c4b854 ["CALL", null, ["callee:00c3e5c4:8"]]
- 00c4b42c bytes 5ccbff97
+ 00c4b854 bytes 5ccbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccfa5e1649dd7dcc59cd42d5f02badb"></a>

### [`00c4b734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md) → [`00c4bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) FUN_00c4bb5c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) · 呼出先 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) · 呼出先 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.29% / 新版 97.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bca8",
      "incomplete_value": false,
      "site": "00c4bca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b880",
      "incomplete_value": false,
      "site": "00c4b880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00c4be94",
      "incomplete_value": false,
      "site": "00c4be94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ba6c",
      "incomplete_value": false,
      "site": "00c4ba6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c4bbb4",
      "READ",
      [
        "storage",
        "00c97560",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bbc4",
      "READ",
      [
        "storage",
        "00c97561",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bbf0",
      "READ",
      [
        "storage",
        "00c97570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c4bbb4",
      "READ",
      [
        "storage",
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bbc4",
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bbf0",
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md#insn-00c4b76c) · [`00c4b818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md#insn-00c4b818) · [`00c4b84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md#insn-00c4b84c)
- 新版 [`00c4bb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bb94) · [`00c4bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bc40) · [`00c4bc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bc74)

~~~diff
- 00c4b76c ["COPY", "register:4060:8", ["const:c97380:8"]]
+ 00c4bb94 ["COPY", "register:4060:8", ["const:c97780:8"]]
- 00c4b76c bytes ace02510
+ 00c4bb94 bytes 6cdf2510
- 00c4b818 ["INT_ADD", "register:40f0:8", ["const:c4b818:8", "const:4:8"]]
- 00c4b818 ["CALL", null, ["callee:00c3accc:8"]]
+ 00c4bc40 ["INT_ADD", "register:40f0:8", ["const:c4bc40:8", "const:4:8"]]
+ 00c4bc40 ["CALL", null, ["callee:00c3accc:8"]]
- 00c4b818 bytes 23bcff97
+ 00c4bc40 bytes 23bcff97
- 00c4b84c ["INT_ADD", "register:40f0:8", ["const:c4b84c:8", "const:4:8"]]
- 00c4b84c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4bc74 ["INT_ADD", "register:40f0:8", ["const:c4bc74:8", "const:4:8"]]
+ 00c4bc74 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4b84c bytes f5380094
+ 00c4bc74 bytes eb380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da34a659b12e3b74eaeb9836b4a0251a"></a>

### [`00c4bb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md) → [`00c4bf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md) FUN_00c4bf78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

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
      "definition_site": "00c4bfdc",
      "incomplete_value": true,
      "site": "00c4bfec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:695:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bbb4",
      "incomplete_value": true,
      "site": "00c4bbc4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:655:8"
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
      "00c4bfdc",
      "READ",
      [
        "storage",
        "002bd655",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4bfdc",
      "READ",
      [
        "storage",
        "002bd695",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4bb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bb94) · [`00c4bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bbac) · [`00c4bbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bbe4)
- 新版 [`00c4bfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4bfbc) · [`00c4bfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4bfd4) · [`00c4c00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4c00c)

~~~diff
- 00c4bb94 ["INT_ADD", "register:40f0:8", ["const:c4bb94:8", "const:4:8"]]
- 00c4bb94 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4bfbc ["INT_ADD", "register:40f0:8", ["const:c4bfbc:8", "const:4:8"]]
+ 00c4bfbc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4bb94 bytes 43380094
+ 00c4bfbc bytes 39380094
- 00c4bbac ["COPY", "tmp:0:8", ["const:655:8"]]
- 00c4bbac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bbac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bbac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4bfd4 ["COPY", "tmp:0:8", ["const:695:8"]]
+ 00c4bfd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bfd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bfd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4bbac bytes 4a551991
+ 00c4bfd4 bytes 4a551a91
- 00c4bbe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4bbe4 ["INT_ADD", "register:40f0:8", ["const:c4bbe4:8", "const:4:8"]]
- 00c4bbe4 ["CALLIND", null, ["register:0:8"]]
+ 00c4c00c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c00c ["INT_ADD", "register:40f0:8", ["const:c4c00c:8", "const:4:8"]]
+ 00c4c00c ["CALLIND", null, ["register:0:8"]]
- 00c4bbe4 bytes 00013fd6
+ 00c4c00c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cacac4fe5439e85fbfd2c64a95d4dab"></a>

### [`00c4bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md) → [`00c4c05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md) FUN_00c4c05c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c0c0",
      "incomplete_value": true,
      "site": "00c4c0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:30d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bc98",
      "incomplete_value": true,
      "site": "00c4bca8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2cd:8"
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
      "00c4c0c0",
      "READ",
      [
        "storage",
        "002bc2cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c0c0",
      "READ",
      [
        "storage",
        "002bc30d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4bc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md#insn-00c4bc78) · [`00c4bc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md#insn-00c4bc90) · [`00c4bccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bc34.md#insn-00c4bccc)
- 新版 [`00c4c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0a0) · [`00c4c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0b8) · [`00c4c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0f4)

~~~diff
- 00c4bc78 ["INT_ADD", "register:40f0:8", ["const:c4bc78:8", "const:4:8"]]
- 00c4bc78 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c0a0 ["INT_ADD", "register:40f0:8", ["const:c4c0a0:8", "const:4:8"]]
+ 00c4c0a0 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4bc78 bytes 0a380094
+ 00c4c0a0 bytes 00380094
- 00c4bc90 ["COPY", "tmp:0:8", ["const:2cd:8"]]
- 00c4bc90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bc90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bc90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4c0b8 ["COPY", "tmp:0:8", ["const:30d:8"]]
+ 00c4c0b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c0b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c0b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4bc90 bytes 4a350b91
+ 00c4c0b8 bytes 4a350c91
- 00c4bccc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4bccc ["INT_ADD", "register:40f0:8", ["const:c4bccc:8", "const:4:8"]]
- 00c4bccc ["CALLIND", null, ["register:0:8"]]
+ 00c4c0f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c0f4 ["INT_ADD", "register:40f0:8", ["const:c4c0f4:8", "const:4:8"]]
+ 00c4c0f4 ["CALLIND", null, ["register:0:8"]]
- 00c4bccc bytes 00013fd6
+ 00c4c0f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e79a5f4f54b0b2ef7fced8700530a4eb"></a>

### [`00c4bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md) → [`00c4c338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md) FUN_00c4c338

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4c4cc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c0a4",
      "incomplete_value": false,
      "site": "00c4c0bc",
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
            "const:e15:8"
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
      "definition_site": "00c4c4d4",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:896:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c0ac",
      "incomplete_value": false,
      "site": "00c4c0bc",
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
            "const:856:8"
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
      "definition_site": "00c4c4dc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c0b4",
      "incomplete_value": false,
      "site": "00c4c0bc",
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
            "const:30e:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002bd65f",
        null,
        "string"
      ]
    ],
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002b8d58",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002bd69f",
        null,
        "string"
      ]
    ],
    [
      "00c4c43c",
      "READ",
      [
        "storage",
        "002b8d98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md#insn-00c4c0bc) · [`00c4bf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md#insn-00c4bf58) · [`00c4bfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md#insn-00c4bfac)
- 新版 [`00c4c4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c4e4) · [`00c4c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c380) · [`00c4c3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c3d4)

~~~diff
- 00c4c0bc ["INT_ADD", "register:40f0:8", ["const:c4c0bc:8", "const:4:8"]]
- 00c4c0bc ["CALL", null, ["callee:00c3800c:8"]]
+ 00c4c4e4 ["INT_ADD", "register:40f0:8", ["const:c4c4e4:8", "const:4:8"]]
+ 00c4c4e4 ["CALL", null, ["callee:00c3800c:8"]]
- 00c4c0bc bytes caaeff97
+ 00c4c4e4 bytes caaeff97
- 00c4bf58 ["INT_ADD", "register:40f0:8", ["const:c4bf58:8", "const:4:8"]]
- 00c4bf58 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c380 ["INT_ADD", "register:40f0:8", ["const:c4c380:8", "const:4:8"]]
+ 00c4c380 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4bf58 bytes 52370094
+ 00c4c380 bytes 48370094
- 00c4bfac ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00c4bfac ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4bfac ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4bfac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c3d4 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00c4c3d4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c3d4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c3d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c4bfac bytes b58e3b91
+ 00c4c3d4 bytes b58e3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8c1cea075481de8cb50892fff6009a9"></a>

### [`00c4c0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c0c8.md) → [`00c4c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md) FUN_00c4c4f0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 83.64% / 新版 83.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4c5b0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c188",
      "incomplete_value": false,
      "site": "00c4c1a0",
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
            "const:e15:8"
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
      "definition_site": "00c4c5b8",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:896:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c190",
      "incomplete_value": false,
      "site": "00c4c1a0",
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
            "const:856:8"
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
      "definition_site": "00c4c5c0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c198",
      "incomplete_value": false,
      "site": "00c4c1a0",
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
            "const:30e:8"
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
      "00c4c510",
      "DATA",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "00c4c540",
      "DATA",
      [
        "storage",
        "002b7e70",
        null,
        "string"
      ]
    ],
    [
      "00c4c578",
      "READ",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c510",
      "DATA",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      "00c4c540",
      "DATA",
      [
        "storage",
        "002b7eb0",
        null,
        "string"
      ]
    ],
    [
      "00c4c578",
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c0c8.md#insn-00c4c1a0) · [`00c4c0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c0c8.md#insn-00c4c0e8) · [`00c4c108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c0c8.md#insn-00c4c108)
- 新版 [`00c4c5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c5c8) · [`00c4c510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c510) · [`00c4c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c530)

~~~diff
- 00c4c1a0 ["INT_ADD", "register:40f0:8", ["const:c4c1a0:8", "const:4:8"]]
- 00c4c1a0 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c4c5c8 ["INT_ADD", "register:40f0:8", ["const:c4c5c8:8", "const:4:8"]]
+ 00c4c5c8 ["CALL", null, ["callee:00c3800c:8"]]
- 00c4c1a0 bytes 91aeff97
+ 00c4c5c8 bytes 91aeff97
- 00c4c0e8 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00c4c0e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c0e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c0e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c4c510 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00c4c510 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4c510 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4c510 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c4c0e8 bytes 008c3b91
+ 00c4c510 bytes 008c3c91
- 00c4c108 ["COPY", "tmp:0:8", ["const:65f:8"]]
- 00c4c108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4c530 ["COPY", "tmp:0:8", ["const:69f:8"]]
+ 00c4c530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4c530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4c530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4c108 bytes 087d1991
+ 00c4c530 bytes 087d1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e571d9bf659ba49a56832cd024fe6921"></a>

### [`00c4c1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md) → [`00c4c5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md) FUN_00c4c5d4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.01% / 新版 93.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c714",
      "incomplete_value": true,
      "site": "00c4c71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c2ec",
      "incomplete_value": true,
      "site": "00c4c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a70:8"
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
      "definition_site": "00c4c718",
      "incomplete_value": true,
      "site": "00c4c720",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c4c2f0",
      "incomplete_value": true,
      "site": "00c4c2f8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c780",
      "incomplete_value": true,
      "site": "00c4c788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:196:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c358",
      "incomplete_value": true,
      "site": "00c4c360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:156:8"
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
      "00c4c714",
      "READ",
      [
        "storage",
        "002b4a70",
        null,
        "string"
      ]
    ],
    [
      "00c4c718",
      "READ",
      [
        "storage",
        "002b4a7d",
        null,
        "string"
      ]
    ],
    [
      "00c4c780",
      "READ",
      [
        "storage",
        "002bb156",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c714",
      "READ",
      [
        "storage",
        "002b4ab0",
        null,
        "string"
      ]
    ],
    [
      "00c4c718",
      "READ",
      [
        "storage",
        "002b4abd",
        null,
        "string"
      ]
    ],
    [
      "00c4c780",
      "READ",
      [
        "storage",
        "002bb196",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md#insn-00c4c1f4) · [`00c4c238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md#insn-00c4c238) · [`00c4c270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md#insn-00c4c270)
- 新版 [`00c4c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c61c) · [`00c4c660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c660) · [`00c4c698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c698)

~~~diff
- 00c4c1f4 ["INT_ADD", "register:40f0:8", ["const:c4c1f4:8", "const:4:8"]]
- 00c4c1f4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c61c ["INT_ADD", "register:40f0:8", ["const:c4c61c:8", "const:4:8"]]
+ 00c4c61c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c1f4 bytes ab360094
+ 00c4c61c bytes a1360094
- 00c4c238 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c238 ["INT_ADD", "register:40f0:8", ["const:c4c238:8", "const:4:8"]]
- 00c4c238 ["CALLIND", null, ["register:0:8"]]
+ 00c4c660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c660 ["INT_ADD", "register:40f0:8", ["const:c4c660:8", "const:4:8"]]
+ 00c4c660 ["CALLIND", null, ["register:0:8"]]
- 00c4c238 bytes 00013fd6
+ 00c4c660 bytes 00013fd6
- 00c4c270 ["INT_ADD", "register:40f0:8", ["const:c4c270:8", "const:4:8"]]
- 00c4c270 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4c698 ["INT_ADD", "register:40f0:8", ["const:c4c698:8", "const:4:8"]]
+ 00c4c698 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4c270 bytes 8c360094
+ 00c4c698 bytes 82360094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34fe7051c1533d57fb1c667ef7e5efca"></a>

### [`00c4c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md) → [`00c4c810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md) FUN_00c4c810

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c4c830",
      "incomplete_value": true,
      "site": "00c4c834",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c408",
      "incomplete_value": true,
      "site": "00c4c40c",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
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
      "00c4c820",
      "DATA",
      [
        "storage",
        "00313d18",
        null,
        null
      ]
    ],
    [
      "00c4c82c",
      "DATA",
      [
        "storage",
        "00313d48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4c820",
      "DATA",
      [
        "storage",
        "00313d58",
        null,
        null
      ]
    ],
    [
      "00c4c82c",
      "DATA",
      [
        "storage",
        "00313d88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md#insn-00c4c3f4) · [`00c4c3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md#insn-00c4c3fc) · [`00c4c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md#insn-00c4c400)
- 新版 [`00c4c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md#insn-00c4c81c) · [`00c4c828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md#insn-00c4c828)

~~~diff
- 00c4c3f4 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00c4c3f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c3f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c3f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4c81c ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00c4c81c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c81c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c81c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c3f4 bytes 29613491
+ 00c4c81c bytes 29613591
- 00c4c3fc ["COPY", "register:4048:8", ["const:313000:8"]]
- 00c4c3fc bytes 29b6fff0
- 00c4c400 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00c4c400 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c400 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c400 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4c828 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00c4c828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c400 bytes 29213591
+ 00c4c828 bytes 29213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753b0c748e3ce21284c8857e0e78cc20"></a>

### [`00c4c6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6dc.md) → [`00c4cb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md) FUN_00c4cb04

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cb74",
      "incomplete_value": false,
      "site": "00c4cb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c74c",
      "incomplete_value": false,
      "site": "00c4c74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00c4cb74",
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4cb74",
      "DATA",
      [
        "storage",
        "00c99230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6dc.md#insn-00c4c71c) · [`00c4c744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6dc.md#insn-00c4c744) · [`00c4c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6dc.md#insn-00c4c748)
- 新版 [`00c4cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cb44) · [`00c4cb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cb6c) · [`00c4cb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cb70)

~~~diff
- 00c4c71c ["INT_ADD", "register:40f0:8", ["const:c4c71c:8", "const:4:8"]]
- 00c4c71c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4cb44 ["INT_ADD", "register:40f0:8", ["const:c4cb44:8", "const:4:8"]]
+ 00c4cb44 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4c71c bytes 41350094
+ 00c4cb44 bytes 37350094
- 00c4c744 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c4cb6c ["COPY", "register:4048:8", ["const:c99000:8"]]
- 00c4c744 bytes 69020090
+ 00c4cb6c bytes 690200b0
- 00c4c748 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00c4c748 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c748 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c748 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4cb70 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00c4cb70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4cb70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4cb70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c748 bytes 29c13891
+ 00c4cb70 bytes 29c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6207623b2dcd664d23dd321fe96d0e2"></a>

### [`00c4c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md) → [`00c4cdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md) FUN_00c4cdec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ce84",
      "incomplete_value": true,
      "site": "00c4ce94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:294:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ca5c",
      "incomplete_value": true,
      "site": "00c4ca6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b8:8"
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
      "00c4ce84",
      "READ",
      [
        "storage",
        "002a51b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ce84",
      "READ",
      [
        "storage",
        "002a5294",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md#insn-00c4c9f0) · [`00c4ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md#insn-00c4ca14) · [`00c4ca40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md#insn-00c4ca40)
- 新版 [`00c4ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce18) · [`00c4ce3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce3c) · [`00c4ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce68)

~~~diff
- 00c4c9f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c9f0 ["INT_ADD", "register:40f0:8", ["const:c4c9f0:8", "const:4:8"]]
- 00c4c9f0 ["CALLIND", null, ["register:0:8"]]
+ 00c4ce18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ce18 ["INT_ADD", "register:40f0:8", ["const:c4ce18:8", "const:4:8"]]
+ 00c4ce18 ["CALLIND", null, ["register:0:8"]]
- 00c4c9f0 bytes 00013fd6
+ 00c4ce18 bytes 00013fd6
- 00c4ca14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ca14 ["INT_ADD", "register:40f0:8", ["const:c4ca14:8", "const:4:8"]]
- 00c4ca14 ["CALLIND", null, ["register:0:8"]]
+ 00c4ce3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ce3c ["INT_ADD", "register:40f0:8", ["const:c4ce3c:8", "const:4:8"]]
+ 00c4ce3c ["CALLIND", null, ["register:0:8"]]
- 00c4ca14 bytes 00013fd6
+ 00c4ce3c bytes 00013fd6
- 00c4ca40 ["INT_ADD", "register:40f0:8", ["const:c4ca40:8", "const:4:8"]]
- 00c4ca40 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4ce68 ["INT_ADD", "register:40f0:8", ["const:c4ce68:8", "const:4:8"]]
+ 00c4ce68 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4ca40 bytes 98340094
+ 00c4ce68 bytes 8e340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e936df071718430186503bafbeda5ae9"></a>

### [`00c4ccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ccc8.md) → [`00c4d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md) FUN_00c4d0f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d15c",
      "incomplete_value": false,
      "site": "00c4d15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4cd34",
      "incomplete_value": false,
      "site": "00c4cd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c4d15c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4d15c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ccfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ccc8.md#insn-00c4ccfc) · [`00c4cd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ccc8.md#insn-00c4cd24) · [`00c4cd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ccc8.md#insn-00c4cd2c)
- 新版 [`00c4d124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d124) · [`00c4d14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d14c) · [`00c4d154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d154)

~~~diff
- 00c4ccfc ["INT_ADD", "register:40f0:8", ["const:c4ccfc:8", "const:4:8"]]
- 00c4ccfc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4d124 ["INT_ADD", "register:40f0:8", ["const:c4d124:8", "const:4:8"]]
+ 00c4d124 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4ccfc bytes c9330094
+ 00c4d124 bytes bf330094
- 00c4cd24 ["INT_ADD", "register:40f0:8", ["const:c4cd24:8", "const:4:8"]]
- 00c4cd24 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c4d14c ["INT_ADD", "register:40f0:8", ["const:c4d14c:8", "const:4:8"]]
+ 00c4d14c ["CALL", null, ["callee:00c57fe0:8"]]
- 00c4cd24 bytes af2b0094
+ 00c4d14c bytes a52b0094
- 00c4cd2c ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c4cd2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cd2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cd2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4d154 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4d154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4cd2c bytes 29010991
+ 00c4d154 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b595ede6df0d7f0b26bbd355749defa3"></a>

### [`00c4cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md) → [`00c4d19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md) FUN_00c4d19c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d204",
      "incomplete_value": false,
      "site": "00c4d204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4cddc",
      "incomplete_value": false,
      "site": "00c4cddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
      "00c4d204",
      "DATA",
      [
        "storage",
        "00c98ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4d204",
      "DATA",
      [
        "storage",
        "00c993f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4cdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md#insn-00c4cdac) · [`00c4cdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md#insn-00c4cdcc) · [`00c4cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4cd74.md#insn-00c4cdd0)
- 新版 [`00c4d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d1d4) · [`00c4d1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d1f4) · [`00c4d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d1f8)

~~~diff
- 00c4cdac ["INT_ADD", "register:40f0:8", ["const:c4cdac:8", "const:4:8"]]
- 00c4cdac ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4d1d4 ["INT_ADD", "register:40f0:8", ["const:c4d1d4:8", "const:4:8"]]
+ 00c4d1d4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4cdac bytes 9d330094
+ 00c4d1d4 bytes 93330094
- 00c4cdcc ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4d1f4 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4cdcc bytes 68020090
+ 00c4d1f4 bytes 68020090
- 00c4cdd0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00c4cdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4cdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4cdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4d1f8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00c4d1f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d1f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d1f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4cdd0 bytes 08c13f91
+ 00c4d1f8 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3cbe49ae3998ea82e1a5cf5934de52"></a>

### [`00c4d3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md) → [`00c4d7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md) FUN_00c4d7cc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d830",
      "incomplete_value": true,
      "site": "00c4d844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e7c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d408",
      "incomplete_value": true,
      "site": "00c4d41c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:daf:8"
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
      "00c4d830",
      "READ",
      [
        "storage",
        "002a3daf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d830",
      "READ",
      [
        "storage",
        "002a3e7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d3e8) · [`00c4d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d400) · [`00c4d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d430)
- 新版 [`00c4d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d810) · [`00c4d828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d828) · [`00c4d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d858)

~~~diff
- 00c4d3e8 ["INT_ADD", "register:40f0:8", ["const:c4d3e8:8", "const:4:8"]]
- 00c4d3e8 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4d810 ["INT_ADD", "register:40f0:8", ["const:c4d810:8", "const:4:8"]]
+ 00c4d810 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d3e8 bytes 2e320094
+ 00c4d810 bytes 24320094
- 00c4d400 ["COPY", "tmp:0:8", ["const:daf:8"]]
- 00c4d400 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d400 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d400 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4d828 ["COPY", "tmp:0:8", ["const:e7c:8"]]
+ 00c4d828 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d828 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d828 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4d400 bytes 4abd3691
+ 00c4d828 bytes 4af13991
- 00c4d430 ["INT_ADD", "register:40f0:8", ["const:c4d430:8", "const:4:8"]]
- 00c4d430 ["CALL", null, ["callee:00c45144:8"]]
+ 00c4d858 ["INT_ADD", "register:40f0:8", ["const:c4d858:8", "const:4:8"]]
+ 00c4d858 ["CALL", null, ["callee:00c45144:8"]]
- 00c4d430 bytes 3bdeff97
+ 00c4d858 bytes 3bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed0140a1f1fbbdbdb98d2639bf18829"></a>

### [`00c4d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d6a0.md) → [`00c4dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md) FUN_00c4dac8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4dc60",
      "incomplete_value": true,
      "site": "00c4dc6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:6ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d838",
      "incomplete_value": true,
      "site": "00c4d844",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:66d:8"
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
      "definition_site": "00c4dcc8",
      "incomplete_value": true,
      "site": "00c4dcd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d8a0",
      "incomplete_value": true,
      "site": "00c4d8ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4de28",
      "incomplete_value": true,
      "site": "00c4de38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4da00",
      "incomplete_value": true,
      "site": "00c4da10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4dc60",
      "READ",
      [
        "storage",
        "002bd66d",
        null,
        "string"
      ]
    ],
    [
      "00c4dcc8",
      "READ",
      [
        "storage",
        "002beac3",
        null,
        "string"
      ]
    ],
    [
      "00c4de28",
      "READ",
      [
        "storage",
        "002c0e10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4dc60",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c4dcc8",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ],
    [
      "00c4de28",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d6a0.md#insn-00c4d6f0) · [`00c4d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d6a0.md#insn-00c4d718) · [`00c4d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d6a0.md#insn-00c4d750)
- 新版 [`00c4db18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db18) · [`00c4db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db40) · [`00c4db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db78)

~~~diff
- 00c4d6f0 ["INT_ADD", "register:40f0:8", ["const:c4d6f0:8", "const:4:8"]]
- 00c4d6f0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4db18 ["INT_ADD", "register:40f0:8", ["const:c4db18:8", "const:4:8"]]
+ 00c4db18 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d6f0 bytes 6c310094
+ 00c4db18 bytes 62310094
- 00c4d718 ["INT_ADD", "register:40f0:8", ["const:c4d718:8", "const:4:8"]]
- 00c4d718 ["CALL", null, ["callee:00c45144:8"]]
+ 00c4db40 ["INT_ADD", "register:40f0:8", ["const:c4db40:8", "const:4:8"]]
+ 00c4db40 ["CALL", null, ["callee:00c45144:8"]]
- 00c4d718 bytes 81ddff97
+ 00c4db40 bytes 81ddff97
- 00c4d750 ["INT_ADD", "register:40f0:8", ["const:c4d750:8", "const:4:8"]]
- 00c4d750 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4db78 ["INT_ADD", "register:40f0:8", ["const:c4db78:8", "const:4:8"]]
+ 00c4db78 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4d750 bytes 54310094
+ 00c4db78 bytes 4a310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d72e16a0d8c423d1964af8021ffce028"></a>

### [`00c4dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc18.md) → [`00c4e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md) FUN_00c4e040

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 8件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 8件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.24% / 新版 97.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e238",
      "incomplete_value": false,
      "site": "00c4e238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4de10",
      "incomplete_value": false,
      "site": "00c4de10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "definition_site": "00c4e25c",
      "incomplete_value": false,
      "site": "00c4e25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:9ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4de34",
      "incomplete_value": false,
      "site": "00c4de34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:922:8"
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
      "definition_site": "00c4e2e8",
      "incomplete_value": false,
      "site": "00c4e2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dec0",
      "incomplete_value": false,
      "site": "00c4dec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "00c4e238",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e25c",
      "DATA",
      [
        "storage",
        "002a8922",
        null,
        "string"
      ]
    ],
    [
      "00c4e2e8",
      "DATA",
      [
        "storage",
        "00c99450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e238",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e25c",
      "DATA",
      [
        "storage",
        "002a89ef",
        null,
        "string"
      ]
    ],
    [
      "00c4e2e8",
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4dd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc18.md#insn-00c4dd1c) · [`00c4dd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc18.md#insn-00c4dd64) · [`00c4dd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc18.md#insn-00c4dd94)
- 新版 [`00c4e144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e144) · [`00c4e18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e18c) · [`00c4e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e1bc)

~~~diff
- 00c4dd1c ["INT_ADD", "register:40f0:8", ["const:c4dd1c:8", "const:4:8"]]
- 00c4dd1c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4e144 ["INT_ADD", "register:40f0:8", ["const:c4e144:8", "const:4:8"]]
+ 00c4e144 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4dd1c bytes e12f0094
+ 00c4e144 bytes d72f0094
- 00c4dd64 ["INT_ADD", "register:40f0:8", ["const:c4dd64:8", "const:4:8"]]
- 00c4dd64 ["CALL", null, ["callee:00c3accc:8"]]
+ 00c4e18c ["INT_ADD", "register:40f0:8", ["const:c4e18c:8", "const:4:8"]]
+ 00c4e18c ["CALL", null, ["callee:00c3accc:8"]]
- 00c4dd64 bytes d0b2ff97
+ 00c4e18c bytes d0b2ff97
- 00c4dd94 ["INT_ADD", "register:40f0:8", ["const:c4dd94:8", "const:4:8"]]
- 00c4dd94 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4e1bc ["INT_ADD", "register:40f0:8", ["const:c4e1bc:8", "const:4:8"]]
+ 00c4e1bc ["CALL", null, ["callee:00c5a020:8"]]
- 00c4dd94 bytes a32f0094
+ 00c4e1bc bytes 992f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8707702e47b7c9497b13221ae2ea7613"></a>

### [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) → [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) FUN_00c4e5e8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) · 呼出先 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e7e0",
      "incomplete_value": false,
      "site": "00c4e7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e3b8",
      "incomplete_value": false,
      "site": "00c4e3b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00c4e868",
      "incomplete_value": false,
      "site": "00c4e868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e440",
      "incomplete_value": false,
      "site": "00c4e440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e978",
      "incomplete_value": false,
      "site": "00c4e978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e550",
      "incomplete_value": false,
      "site": "00c4e550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "00c4e7e0",
      "DATA",
      [
        "storage",
        "00c99680",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e868",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e978",
      "DATA",
      [
        "storage",
        "00c995a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e7e0",
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e868",
      "DATA",
      [
        "storage",
        "00c99a10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e978",
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md#insn-00c4e2dc) · [`00c4e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md#insn-00c4e358) · [`00c4e380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md#insn-00c4e380)
- 新版 [`00c4e704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e704) · [`00c4e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e780) · [`00c4e7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e7a8)

~~~diff
- 00c4e2dc ["INT_ADD", "register:40f0:8", ["const:c4e2dc:8", "const:4:8"]]
- 00c4e2dc ["CALL", null, ["callee:00c3e5c4:8"]]
+ 00c4e704 ["INT_ADD", "register:40f0:8", ["const:c4e704:8", "const:4:8"]]
+ 00c4e704 ["CALL", null, ["callee:00c3e5c4:8"]]
- 00c4e2dc bytes b0bfff97
+ 00c4e704 bytes b0bfff97
- 00c4e358 ["INT_ADD", "register:40f0:8", ["const:c4e358:8", "const:4:8"]]
- 00c4e358 ["CALL", null, ["callee:00c3accc:8"]]
+ 00c4e780 ["INT_ADD", "register:40f0:8", ["const:c4e780:8", "const:4:8"]]
+ 00c4e780 ["CALL", null, ["callee:00c3accc:8"]]
- 00c4e358 bytes 53b1ff97
+ 00c4e780 bytes 53b1ff97
- 00c4e380 ["INT_ADD", "register:40f0:8", ["const:c4e380:8", "const:4:8"]]
- 00c4e380 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4e7a8 ["INT_ADD", "register:40f0:8", ["const:c4e7a8:8", "const:4:8"]]
+ 00c4e7a8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e380 bytes 282e0094
+ 00c4e7a8 bytes 1e2e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c83c58382a16ca4676b4207ac8f40ff8"></a>

### [`00c4e598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e598.md) → [`00c4e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md) FUN_00c4e9c0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ea2c",
      "incomplete_value": false,
      "site": "00c4ea2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e604",
      "incomplete_value": false,
      "site": "00c4e604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c4ea2c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ea2c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e598.md#insn-00c4e5cc) · [`00c4e5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e598.md#insn-00c4e5f4) · [`00c4e5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e598.md#insn-00c4e5fc)
- 新版 [`00c4e9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4e9f4) · [`00c4ea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4ea1c) · [`00c4ea24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4ea24)

~~~diff
- 00c4e5cc ["INT_ADD", "register:40f0:8", ["const:c4e5cc:8", "const:4:8"]]
- 00c4e5cc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4e9f4 ["INT_ADD", "register:40f0:8", ["const:c4e9f4:8", "const:4:8"]]
+ 00c4e9f4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e5cc bytes 952d0094
+ 00c4e9f4 bytes 8b2d0094
- 00c4e5f4 ["INT_ADD", "register:40f0:8", ["const:c4e5f4:8", "const:4:8"]]
- 00c4e5f4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c4ea1c ["INT_ADD", "register:40f0:8", ["const:c4ea1c:8", "const:4:8"]]
+ 00c4ea1c ["CALL", null, ["callee:00c57fe0:8"]]
- 00c4e5f4 bytes 7b250094
+ 00c4ea1c bytes 71250094
- 00c4e5fc ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c4e5fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e5fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e5fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4ea24 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4ea24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ea24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ea24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4e5fc bytes 29010991
+ 00c4ea24 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09cfc74418363adcc8c9d42416bd1bdd"></a>

### [`00c4e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md) → [`00c4ea6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md) FUN_00c4ea6c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ead8",
      "incomplete_value": false,
      "site": "00c4ead8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e6b0",
      "incomplete_value": false,
      "site": "00c4e6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c4ead8",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ead8",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md#insn-00c4e678) · [`00c4e6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md#insn-00c4e6a0) · [`00c4e6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md#insn-00c4e6a8)
- 新版 [`00c4eaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4eaa0) · [`00c4eac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4eac8) · [`00c4ead0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4ead0)

~~~diff
- 00c4e678 ["INT_ADD", "register:40f0:8", ["const:c4e678:8", "const:4:8"]]
- 00c4e678 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4eaa0 ["INT_ADD", "register:40f0:8", ["const:c4eaa0:8", "const:4:8"]]
+ 00c4eaa0 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e678 bytes 6a2d0094
+ 00c4eaa0 bytes 602d0094
- 00c4e6a0 ["INT_ADD", "register:40f0:8", ["const:c4e6a0:8", "const:4:8"]]
- 00c4e6a0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c4eac8 ["INT_ADD", "register:40f0:8", ["const:c4eac8:8", "const:4:8"]]
+ 00c4eac8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c4e6a0 bytes 50250094
+ 00c4eac8 bytes 46250094
- 00c4e6a8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c4e6a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e6a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e6a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4ead0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4ead0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ead0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ead0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4e6a8 bytes 29010991
+ 00c4ead0 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9705a56c8a16301434642f78b626412e"></a>

### [`00c4e6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md) → [`00c4eb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md) FUN_00c4eb18

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eb84",
      "incomplete_value": false,
      "site": "00c4eb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e75c",
      "incomplete_value": false,
      "site": "00c4e75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "00c4eb84",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4eb84",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e724) · [`00c4e74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e74c) · [`00c4e754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e754)
- 新版 [`00c4eb4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb4c) · [`00c4eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb74) · [`00c4eb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb7c)

~~~diff
- 00c4e724 ["INT_ADD", "register:40f0:8", ["const:c4e724:8", "const:4:8"]]
- 00c4e724 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4eb4c ["INT_ADD", "register:40f0:8", ["const:c4eb4c:8", "const:4:8"]]
+ 00c4eb4c ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e724 bytes 3f2d0094
+ 00c4eb4c bytes 352d0094
- 00c4e74c ["INT_ADD", "register:40f0:8", ["const:c4e74c:8", "const:4:8"]]
- 00c4e74c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c4eb74 ["INT_ADD", "register:40f0:8", ["const:c4eb74:8", "const:4:8"]]
+ 00c4eb74 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c4e74c bytes 25250094
+ 00c4eb74 bytes 1b250094
- 00c4e754 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c4e754 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e754 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4e754 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb7c ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4eb7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4e754 bytes 29010991
+ 00c4eb7c bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8edd140144ba4d0ee877f33b3af0fb3"></a>

### [`00c4e79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md) → [`00c4ebc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md) FUN_00c4ebc4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ec2c",
      "incomplete_value": false,
      "site": "00c4ec2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e804",
      "incomplete_value": false,
      "site": "00c4e804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "00c4ec2c",
      "DATA",
      [
        "storage",
        "00c996f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ec2c",
      "DATA",
      [
        "storage",
        "00c99af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md#insn-00c4e7d4) · [`00c4e7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md#insn-00c4e7f8) · [`00c4e844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md#insn-00c4e844)
- 新版 [`00c4ebfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ebfc) · [`00c4ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ec20) · [`00c4ec6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ec6c)

~~~diff
- 00c4e7d4 ["INT_ADD", "register:40f0:8", ["const:c4e7d4:8", "const:4:8"]]
- 00c4e7d4 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4ebfc ["INT_ADD", "register:40f0:8", ["const:c4ebfc:8", "const:4:8"]]
+ 00c4ebfc ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e7d4 bytes 132d0094
+ 00c4ebfc bytes 092d0094
- 00c4e7f8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 00c4e7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ec20 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00c4ec20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ec20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ec20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4e7f8 bytes 08c11b91
+ 00c4ec20 bytes 08c12b91
- 00c4e844 ["INT_ADD", "register:40f0:8", ["const:c4e844:8", "const:4:8"]]
- 00c4e844 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4ec6c ["INT_ADD", "register:40f0:8", ["const:c4ec6c:8", "const:4:8"]]
+ 00c4ec6c ["CALL", null, ["callee:00c58020:8"]]
- 00c4e844 bytes f7240094
+ 00c4ec6c bytes ed240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a5727d013dcb2b26fa29141487060e"></a>

### [`00c4e848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e848.md) → [`00c4ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md) FUN_00c4ec70

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4ecd4",
      "incomplete_value": false,
      "site": "00c4ecd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e8ac",
      "incomplete_value": false,
      "site": "00c4e8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "00c4ecd4",
      "DATA",
      [
        "storage",
        "00c99760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ecd4",
      "DATA",
      [
        "storage",
        "00c99b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e848.md#insn-00c4e87c) · [`00c4e8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e848.md#insn-00c4e8a0) · [`00c4e8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e848.md#insn-00c4e8e4)
- 新版 [`00c4eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4eca4) · [`00c4ecc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4ecc8) · [`00c4ed0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4ed0c)

~~~diff
- 00c4e87c ["INT_ADD", "register:40f0:8", ["const:c4e87c:8", "const:4:8"]]
- 00c4e87c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4eca4 ["INT_ADD", "register:40f0:8", ["const:c4eca4:8", "const:4:8"]]
+ 00c4eca4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e87c bytes e92c0094
+ 00c4eca4 bytes df2c0094
- 00c4e8a0 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00c4e8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecc8 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00c4ecc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4e8a0 bytes 08811d91
+ 00c4ecc8 bytes 08812d91
- 00c4e8e4 ["INT_ADD", "register:40f0:8", ["const:c4e8e4:8", "const:4:8"]]
- 00c4e8e4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4ed0c ["INT_ADD", "register:40f0:8", ["const:c4ed0c:8", "const:4:8"]]
+ 00c4ed0c ["CALL", null, ["callee:00c58020:8"]]
- 00c4e8e4 bytes cf240094
+ 00c4ed0c bytes c5240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1d5b64f3119ff880b7d7d226542115a"></a>

### [`00c4e8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e8e8.md) → [`00c4ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md) FUN_00c4ed10

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ed78",
      "incomplete_value": false,
      "site": "00c4ed78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e950",
      "incomplete_value": false,
      "site": "00c4e950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "00c4ed78",
      "DATA",
      [
        "storage",
        "00c997d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ed78",
      "DATA",
      [
        "storage",
        "00c99bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e8e8.md#insn-00c4e920) · [`00c4e944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e8e8.md#insn-00c4e944) · [`00c4e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e8e8.md#insn-00c4e990)
- 新版 [`00c4ed48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4ed48) · [`00c4ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4ed6c) · [`00c4edb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4edb8)

~~~diff
- 00c4e920 ["INT_ADD", "register:40f0:8", ["const:c4e920:8", "const:4:8"]]
- 00c4e920 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4ed48 ["INT_ADD", "register:40f0:8", ["const:c4ed48:8", "const:4:8"]]
+ 00c4ed48 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e920 bytes c02c0094
+ 00c4ed48 bytes b62c0094
- 00c4e944 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 00c4e944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed6c ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 00c4ed6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4e944 bytes 08411f91
+ 00c4ed6c bytes 08412f91
- 00c4e990 ["INT_ADD", "register:40f0:8", ["const:c4e990:8", "const:4:8"]]
- 00c4e990 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4edb8 ["INT_ADD", "register:40f0:8", ["const:c4edb8:8", "const:4:8"]]
+ 00c4edb8 ["CALL", null, ["callee:00c58020:8"]]
- 00c4e990 bytes a4240094
+ 00c4edb8 bytes 9a240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d35d6b63849869fadc9290343302a777"></a>

### [`00c4e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md) → [`00c4edbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md) FUN_00c4edbc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ee24",
      "incomplete_value": false,
      "site": "00c4ee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e9fc",
      "incomplete_value": false,
      "site": "00c4e9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "00c4ee24",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ee24",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md#insn-00c4e9cc) · [`00c4e9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md#insn-00c4e9f0) · [`00c4ea3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md#insn-00c4ea3c)
- 新版 [`00c4edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4edf4) · [`00c4ee18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4ee18) · [`00c4ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4ee64)

~~~diff
- 00c4e9cc ["INT_ADD", "register:40f0:8", ["const:c4e9cc:8", "const:4:8"]]
- 00c4e9cc ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4edf4 ["INT_ADD", "register:40f0:8", ["const:c4edf4:8", "const:4:8"]]
+ 00c4edf4 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4e9cc bytes 952c0094
+ 00c4edf4 bytes 8b2c0094
- 00c4e9f0 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00c4e9f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e9f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4e9f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee18 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c4ee18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4e9f0 bytes 08012191
+ 00c4ee18 bytes 08013191
- 00c4ea3c ["INT_ADD", "register:40f0:8", ["const:c4ea3c:8", "const:4:8"]]
- 00c4ea3c ["CALL", null, ["callee:00c58020:8"]]
+ 00c4ee64 ["INT_ADD", "register:40f0:8", ["const:c4ee64:8", "const:4:8"]]
+ 00c4ee64 ["CALL", null, ["callee:00c58020:8"]]
- 00c4ea3c bytes 79240094
+ 00c4ee64 bytes 6f240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a8a33372641111b51bf27fe48c38ff"></a>

### [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) → [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) FUN_00c4ee68

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 6件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c50408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md) [`00c504a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 6件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c50830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md) [`00c508d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ef64",
      "incomplete_value": false,
      "site": "00c4ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eb3c",
      "incomplete_value": false,
      "site": "00c4eb3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "definition_site": "00c4f040",
      "incomplete_value": false,
      "site": "00c4f040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ec18",
      "incomplete_value": false,
      "site": "00c4ec18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ecb4",
      "incomplete_value": false,
      "site": "00c4ecb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "00c4ef64",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f040",
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f0dc",
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ef64",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f040",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f0dc",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4eb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md#insn-00c4eb04) · [`00c4eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md#insn-00c4eb38) · [`00c4eba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md#insn-00c4eba8)
- 新版 [`00c4ef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4ef2c) · [`00c4ef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4ef60) · [`00c4efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4efd0)

~~~diff
- 00c4eb04 ["INT_ADD", "register:40f0:8", ["const:c4eb04:8", "const:4:8"]]
- 00c4eb04 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4ef2c ["INT_ADD", "register:40f0:8", ["const:c4ef2c:8", "const:4:8"]]
+ 00c4ef2c ["CALL", null, ["callee:00c5a020:8"]]
- 00c4eb04 bytes 472c0094
+ 00c4ef2c bytes 3d2c0094
- 00c4eb38 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00c4eb38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eb38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eb38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ef60 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4ef60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ef60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ef60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4eb38 bytes 08010991
+ 00c4ef60 bytes 08011991
- 00c4eba8 ["INT_ADD", "register:40f0:8", ["const:c4eba8:8", "const:4:8"]]
- 00c4eba8 ["CALL", null, ["callee:00c50830:8"]]
+ 00c4efd0 ["INT_ADD", "register:40f0:8", ["const:c4efd0:8", "const:4:8"]]
+ 00c4efd0 ["CALL", null, ["callee:00c50830:8"]]
- 00c4eba8 bytes 18060094
+ 00c4efd0 bytes 18060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-491e2cfd4b1fe9fca823573613449432"></a>

### [`00c4ecfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ecfc.md) → [`00c4f124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md) FUN_00c4f124

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f230",
      "incomplete_value": false,
      "site": "00c4f230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ee08",
      "incomplete_value": false,
      "site": "00c4ee08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "00c4f230",
      "DATA",
      [
        "storage",
        "00c99a70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f250",
      "DATA",
      [
        "storage",
        "002b360c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4f230",
      "DATA",
      [
        "storage",
        "00c99e70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f250",
      "DATA",
      [
        "storage",
        "002b364c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ecfc.md#insn-00c4ed74) · [`00c4ed84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ecfc.md#insn-00c4ed84) · [`00c4ed94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ecfc.md#insn-00c4ed94)
- 新版 [`00c4f19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f19c) · [`00c4f1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f1ac) · [`00c4f1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f1bc)

~~~diff
- 00c4ed74 ["COPY", "tmp:0:8", ["const:60c:8"]]
- 00c4ed74 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed74 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed74 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f19c ["COPY", "tmp:0:8", ["const:64c:8"]]
+ 00c4f19c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f19c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f19c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4ed74 bytes 73321891
+ 00c4f19c bytes 73321991
- 00c4ed84 ["COPY", "tmp:0:8", ["const:bde:8"]]
- 00c4ed84 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed84 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed84 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1ac ["COPY", "tmp:0:8", ["const:c1e:8"]]
+ 00c4f1ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4ed84 bytes 737a2f91
+ 00c4f1ac bytes 737a3091
- 00c4ed94 ["COPY", "tmp:0:8", ["const:77a:8"]]
- 00c4ed94 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed94 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4ed94 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1bc ["COPY", "tmp:0:8", ["const:847:8"]]
+ 00c4f1bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f1bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4ed94 bytes 73ea1d91
+ 00c4f1bc bytes 731e2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10e381b62ce706a4f7afd0b3d89eabd4"></a>

### [`00c4ee4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md) → [`00c4f274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md) FUN_00c4f274

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f2dc",
      "incomplete_value": false,
      "site": "00c4f2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eeb4",
      "incomplete_value": false,
      "site": "00c4eeb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00c4f2dc",
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f2dc",
      "DATA",
      [
        "storage",
        "00c99ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md#insn-00c4ee80) · [`00c4eeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md#insn-00c4eeac) · [`00c4eef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md#insn-00c4eef4)
- 新版 [`00c4f2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f2a8) · [`00c4f2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f2d4) · [`00c4f31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f31c)

~~~diff
- 00c4ee80 ["INT_ADD", "register:40f0:8", ["const:c4ee80:8", "const:4:8"]]
- 00c4ee80 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4f2a8 ["INT_ADD", "register:40f0:8", ["const:c4f2a8:8", "const:4:8"]]
+ 00c4f2a8 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4ee80 bytes 682b0094
+ 00c4f2a8 bytes 5e2b0094
- 00c4eeac ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00c4eeac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eeac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eeac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f2d4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00c4f2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4eeac bytes 08812b91
+ 00c4f2d4 bytes 08813b91
- 00c4eef4 ["INT_ADD", "register:40f0:8", ["const:c4eef4:8", "const:4:8"]]
- 00c4eef4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4f31c ["INT_ADD", "register:40f0:8", ["const:c4f31c:8", "const:4:8"]]
+ 00c4f31c ["CALL", null, ["callee:00c58020:8"]]
- 00c4eef4 bytes 4b230094
+ 00c4f31c bytes 41230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab12c4f982ba3a7b845b83fba0e1cc4e"></a>

### [`00c4eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4eef8.md) → [`00c4f320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md) FUN_00c4f320

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4f394",
      "incomplete_value": false,
      "site": "00c4f394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ef6c",
      "incomplete_value": false,
      "site": "00c4ef6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "00c4f394",
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f394",
      "DATA",
      [
        "storage",
        "00c99f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ef30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4eef8.md#insn-00c4ef30) · [`00c4ef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4eef8.md#insn-00c4ef5c) · [`00c4efb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4eef8.md#insn-00c4efb0)
- 新版 [`00c4f358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f358) · [`00c4f384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f384) · [`00c4f3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f3d8)

~~~diff
- 00c4ef30 ["INT_ADD", "register:40f0:8", ["const:c4ef30:8", "const:4:8"]]
- 00c4ef30 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4f358 ["INT_ADD", "register:40f0:8", ["const:c4f358:8", "const:4:8"]]
+ 00c4f358 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4ef30 bytes 3c2b0094
+ 00c4f358 bytes 322b0094
- 00c4ef5c ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00c4ef5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ef5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ef5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4f384 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00c4f384 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4f384 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4f384 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4ef5c bytes 4a412d91
+ 00c4f384 bytes 4a413d91
- 00c4efb0 ["INT_ADD", "register:40f0:8", ["const:c4efb0:8", "const:4:8"]]
- 00c4efb0 ["CALL", null, ["callee:00c58020:8"]]
+ 00c4f3d8 ["INT_ADD", "register:40f0:8", ["const:c4f3d8:8", "const:4:8"]]
+ 00c4f3d8 ["CALL", null, ["callee:00c58020:8"]]
- 00c4efb0 bytes 1c230094
+ 00c4f3d8 bytes 12230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

