# v16.0.0 → v16.0.1 · 最優先の変更候補 (91)

[一覧の目次](README.md)

<a id="compare-cfb8936d52349ef9ef676c67195b080b"></a>

### [`00c4efb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4efb4.md) → [`00c4f3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f3dc.md) FUN_00c4f3dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4f440",
      "incomplete_value": false,
      "site": "00c4f440",
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
      "definition_site": "00c4f018",
      "incomplete_value": false,
      "site": "00c4f018",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f460",
      "incomplete_value": false,
      "site": "00c4f460",
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
            "const:56b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f038",
      "incomplete_value": false,
      "site": "00c4f038",
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
            "const:48f:8"
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
      "00c4f440",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f460",
      "DATA",
      [
        "storage",
        "002a748f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4f440",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f460",
      "DATA",
      [
        "storage",
        "002a756b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4efe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4efb4.md#insn-00c4efe8) · [`00c4f00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4efb4.md#insn-00c4f00c) · [`00c4f030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4efb4.md#insn-00c4f030)
- 新版 `00c4f410`（命令位置の公開資料なし） · `00c4f434`（命令位置の公開資料なし） · `00c4f458`（命令位置の公開資料なし）

~~~diff
- 00c4efe8 ["INT_ADD", "register:40f0:8", ["const:c4efe8:8", "const:4:8"]]
- 00c4efe8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4f410 ["INT_ADD", "register:40f0:8", ["const:c4f410:8", "const:4:8"]]
+ 00c4f410 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4efe8 bytes 0e2b0094
+ 00c4f410 bytes 042b0094
- 00c4f00c ["COPY", "tmp:0:8", ["const:840:8"]]
- 00c4f00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f434 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c4f434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f00c bytes 08012191
+ 00c4f434 bytes 08013191
- 00c4f030 ["COPY", "tmp:0:8", ["const:48f:8"]]
- 00c4f030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4f458 ["COPY", "tmp:0:8", ["const:56b:8"]]
+ 00c4f458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4f030 bytes 293d1291
+ 00c4f458 bytes 29ad1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d2ce85bd80aa6b6a8b34524e80eb249"></a>

### [`00c4f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f064.md) → [`00c4f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f48c.md) FUN_00c4f48c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c4f4f0",
      "incomplete_value": false,
      "site": "00c4f4f0",
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
      "definition_site": "00c4f0c8",
      "incomplete_value": false,
      "site": "00c4f0c8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f510",
      "incomplete_value": false,
      "site": "00c4f510",
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
            "const:f06:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f0e8",
      "incomplete_value": false,
      "site": "00c4f0e8",
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
            "const:e39:8"
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
      "00c4f4f0",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f510",
      "DATA",
      [
        "storage",
        "002a0e39",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4f4f0",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f510",
      "DATA",
      [
        "storage",
        "002a0f06",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f064.md#insn-00c4f098) · [`00c4f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f064.md#insn-00c4f0bc) · [`00c4f0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f064.md#insn-00c4f0e0)
- 新版 `00c4f4c0`（命令位置の公開資料なし） · `00c4f4e4`（命令位置の公開資料なし） · `00c4f508`（命令位置の公開資料なし）

~~~diff
- 00c4f098 ["INT_ADD", "register:40f0:8", ["const:c4f098:8", "const:4:8"]]
- 00c4f098 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c4f4c0 ["INT_ADD", "register:40f0:8", ["const:c4f4c0:8", "const:4:8"]]
+ 00c4f4c0 ["CALL", null, ["callee:00c5a020:8"]]
- 00c4f098 bytes e22a0094
+ 00c4f4c0 bytes d82a0094
- 00c4f0bc ["COPY", "tmp:0:8", ["const:840:8"]]
- 00c4f0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4e4 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c4f4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f0bc bytes 08012191
+ 00c4f4e4 bytes 08013191
- 00c4f0e0 ["COPY", "tmp:0:8", ["const:e39:8"]]
- 00c4f0e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f0e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f0e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4f508 ["COPY", "tmp:0:8", ["const:f06:8"]]
+ 00c4f508 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f508 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f508 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4f0e0 bytes 29e53891
+ 00c4f508 bytes 29193c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09824647353c1280e8f8211f5a1fc301"></a>

### [`00c4f578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f578.md) → [`00c4f9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f9a0.md) FUN_00c4f9a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fb30",
      "incomplete_value": true,
      "site": "00c4fb3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c4f708",
      "incomplete_value": true,
      "site": "00c4f714",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fb98",
      "incomplete_value": true,
      "site": "00c4fba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c4f770",
      "incomplete_value": true,
      "site": "00c4f77c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c4fb30",
      "READ",
      [
        "storage",
        "002bd66d",
        null,
        "string"
      ]
    ],
    [
      "00c4fb98",
      "READ",
      [
        "storage",
        "002beac3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4fb30",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c4fb98",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f578.md#insn-00c4f5c4) · [`00c4f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f578.md#insn-00c4f5ec) · [`00c4f624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f578.md#insn-00c4f624)
- 新版 `00c4f9ec`（命令位置の公開資料なし） · `00c4fa14`（命令位置の公開資料なし） · `00c4fa4c`（命令位置の公開資料なし）

~~~diff
- 00c4f5c4 ["INT_ADD", "register:40f0:8", ["const:c4f5c4:8", "const:4:8"]]
- 00c4f5c4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4f9ec ["INT_ADD", "register:40f0:8", ["const:c4f9ec:8", "const:4:8"]]
+ 00c4f9ec ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f5c4 bytes b7290094
+ 00c4f9ec bytes ad290094
- 00c4f5ec ["INT_ADD", "register:40f0:8", ["const:c4f5ec:8", "const:4:8"]]
- 00c4f5ec ["CALL", null, ["callee:00c45144:8"]]
+ 00c4fa14 ["INT_ADD", "register:40f0:8", ["const:c4fa14:8", "const:4:8"]]
+ 00c4fa14 ["CALL", null, ["callee:00c45144:8"]]
- 00c4f5ec bytes ccd5ff97
+ 00c4fa14 bytes ccd5ff97
- 00c4f624 ["INT_ADD", "register:40f0:8", ["const:c4f624:8", "const:4:8"]]
- 00c4f624 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c4fa4c ["INT_ADD", "register:40f0:8", ["const:c4fa4c:8", "const:4:8"]]
+ 00c4fa4c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4f624 bytes 9f290094
+ 00c4fa4c bytes 95290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d68143f2c8fc507b32a634713d67acc5"></a>

### [`00c4fc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fc8c.md) → [`00c500b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c500b4.md) FUN_00c500b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5018c",
      "incomplete_value": true,
      "site": "00c50198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c4fd64",
      "incomplete_value": true,
      "site": "00c4fd70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c501f4",
      "incomplete_value": true,
      "site": "00c50200",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c4fdcc",
      "incomplete_value": true,
      "site": "00c4fdd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c5018c",
      "READ",
      [
        "storage",
        "002bd66d",
        null,
        "string"
      ]
    ],
    [
      "00c501f4",
      "READ",
      [
        "storage",
        "002beac3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c5018c",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c501f4",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4fcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fc8c.md#insn-00c4fcb0) · [`00c4fce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fc8c.md#insn-00c4fce4) · [`00c4fd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fc8c.md#insn-00c4fd48)
- 新版 `00c500d8`（命令位置の公開資料なし） · `00c5010c`（命令位置の公開資料なし） · `00c50170`（命令位置の公開資料なし）

~~~diff
- 00c4fcb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4fcb0 ["INT_ADD", "register:40f0:8", ["const:c4fcb0:8", "const:4:8"]]
- 00c4fcb0 ["CALLIND", null, ["register:0:8"]]
+ 00c500d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c500d8 ["INT_ADD", "register:40f0:8", ["const:c500d8:8", "const:4:8"]]
+ 00c500d8 ["CALLIND", null, ["register:0:8"]]
- 00c4fcb0 bytes 00013fd6
+ 00c500d8 bytes 00013fd6
- 00c4fce4 ["INT_ADD", "register:40f0:8", ["const:c4fce4:8", "const:4:8"]]
- 00c4fce4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c5010c ["INT_ADD", "register:40f0:8", ["const:c5010c:8", "const:4:8"]]
+ 00c5010c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4fce4 bytes ef270094
+ 00c5010c bytes e5270094
- 00c4fd48 ["INT_ADD", "register:40f0:8", ["const:c4fd48:8", "const:4:8"]]
- 00c4fd48 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50170 ["INT_ADD", "register:40f0:8", ["const:c50170:8", "const:4:8"]]
+ 00c50170 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c4fd48 bytes d6270094
+ 00c50170 bytes cc270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b04e32ef68f364aae7414b3217e4ec84"></a>

### [`00c50074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50074.md) → [`00c5049c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5049c.md) FUN_00c5049c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50504",
      "incomplete_value": true,
      "site": "00c50510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c500dc",
      "incomplete_value": true,
      "site": "00c500e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "00c50504",
      "READ",
      [
        "storage",
        "002a7498",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50504",
      "READ",
      [
        "storage",
        "002a7574",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c500c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50074.md#insn-00c500c0) · [`00c500d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50074.md#insn-00c500d4) · [`00c50120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50074.md#insn-00c50120)
- 新版 `00c504e8`（命令位置の公開資料なし） · `00c504fc`（命令位置の公開資料なし） · `00c50548`（命令位置の公開資料なし）

~~~diff
- 00c500c0 ["INT_ADD", "register:40f0:8", ["const:c500c0:8", "const:4:8"]]
- 00c500c0 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c504e8 ["INT_ADD", "register:40f0:8", ["const:c504e8:8", "const:4:8"]]
+ 00c504e8 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c500c0 bytes f8260094
+ 00c504e8 bytes ee260094
- 00c500d4 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00c500d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c500d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c500d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c504fc ["COPY", "tmp:0:8", ["const:574:8"]]
+ 00c504fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c504fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c504fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c500d4 bytes 29611291
+ 00c504fc bytes 29d11591
- 00c50120 ["INT_ADD", "register:40f0:8", ["const:c50120:8", "const:4:8"]]
- 00c50120 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50548 ["INT_ADD", "register:40f0:8", ["const:c50548:8", "const:4:8"]]
+ 00c50548 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50120 bytes e0260094
+ 00c50548 bytes d6260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328c655953a3f8ed99207b03e5d0fde6"></a>

### [`00c50408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md) → [`00c50830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md) FUN_00c50830

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c50894",
      "incomplete_value": false,
      "site": "00c50894",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5046c",
      "incomplete_value": false,
      "site": "00c5046c",
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
            "const:8b0:8"
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
      "00c50894",
      "DATA",
      [
        "storage",
        "00c998b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50894",
      "DATA",
      [
        "storage",
        "00c99cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5043c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md#insn-00c5043c) · [`00c50460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md#insn-00c50460) · [`00c504a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md#insn-00c504a4)
- 新版 `00c50864`（命令位置の公開資料なし） · `00c50888`（命令位置の公開資料なし） · `00c508cc`（命令位置の公開資料なし）

~~~diff
- 00c5043c ["INT_ADD", "register:40f0:8", ["const:c5043c:8", "const:4:8"]]
- 00c5043c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c50864 ["INT_ADD", "register:40f0:8", ["const:c50864:8", "const:4:8"]]
+ 00c50864 ["CALL", null, ["callee:00c5a020:8"]]
- 00c5043c bytes f9250094
+ 00c50864 bytes ef250094
- 00c50460 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 00c50460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50888 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00c50888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50460 bytes 08c12291
+ 00c50888 bytes 08c13291
- 00c504a4 ["INT_ADD", "register:40f0:8", ["const:c504a4:8", "const:4:8"]]
- 00c504a4 ["CALL", null, ["callee:00c58020:8"]]
+ 00c508cc ["INT_ADD", "register:40f0:8", ["const:c508cc:8", "const:4:8"]]
+ 00c508cc ["CALL", null, ["callee:00c58020:8"]]
- 00c504a4 bytes df1d0094
+ 00c508cc bytes d51d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78a9d10b6a70a914c9b9ebd9f2f9375"></a>

### [`00c504a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md) → [`00c508d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md) FUN_00c508d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

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
      "definition_site": "00c50938",
      "incomplete_value": false,
      "site": "00c50938",
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
      "definition_site": "00c50510",
      "incomplete_value": false,
      "site": "00c50510",
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
      "00c50938",
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
      "00c50938",
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

- 旧版 [`00c504e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c504e0) · [`00c50504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c50504) · [`00c5054c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c5054c)
- 新版 `00c50908`（命令位置の公開資料なし） · `00c5092c`（命令位置の公開資料なし） · `00c50974`（命令位置の公開資料なし）

~~~diff
- 00c504e0 ["INT_ADD", "register:40f0:8", ["const:c504e0:8", "const:4:8"]]
- 00c504e0 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c50908 ["INT_ADD", "register:40f0:8", ["const:c50908:8", "const:4:8"]]
+ 00c50908 ["CALL", null, ["callee:00c5a020:8"]]
- 00c504e0 bytes d0250094
+ 00c50908 bytes c6250094
- 00c50504 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00c50504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c5092c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00c5092c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c5092c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c5092c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50504 bytes 08812491
+ 00c5092c bytes 08813491
- 00c5054c ["INT_ADD", "register:40f0:8", ["const:c5054c:8", "const:4:8"]]
- 00c5054c ["CALL", null, ["callee:00c58020:8"]]
+ 00c50974 ["INT_ADD", "register:40f0:8", ["const:c50974:8", "const:4:8"]]
+ 00c50974 ["CALL", null, ["callee:00c58020:8"]]
- 00c5054c bytes b51d0094
+ 00c50974 bytes ab1d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-000ca5bb9e345c8898bbd71887e2ae80"></a>

### [`00c50550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md) → [`00c50978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50978.md) FUN_00c50978

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c509dc",
      "incomplete_value": true,
      "site": "00c509e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c505b4",
      "incomplete_value": true,
      "site": "00c505c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
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
      "definition_site": "00c509ec",
      "incomplete_value": true,
      "site": "00c509ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c505c4",
      "incomplete_value": true,
      "site": "00c505c4",
      "value": [
        "LOAD",
        "8",
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
      "00c509dc",
      "READ",
      [
        "storage",
        "002bfb28",
        null,
        "string"
      ]
    ],
    [
      "00c509e0",
      "READ",
      [
        "storage",
        "002bfb2d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c509dc",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "00c509e0",
      "READ",
      [
        "storage",
        "002bfb6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md#insn-00c50594) · [`00c505ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md#insn-00c505ac) · [`00c505e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md#insn-00c505e4)
- 新版 `00c509bc`（命令位置の公開資料なし） · `00c509d4`（命令位置の公開資料なし） · `00c50a0c`（命令位置の公開資料なし）

~~~diff
- 00c50594 ["INT_ADD", "register:40f0:8", ["const:c50594:8", "const:4:8"]]
- 00c50594 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c509bc ["INT_ADD", "register:40f0:8", ["const:c509bc:8", "const:4:8"]]
+ 00c509bc ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50594 bytes c3250094
+ 00c509bc bytes b9250094
- 00c505ac ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00c505ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c505ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c505ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c509d4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00c509d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c509d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c509d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c505ac bytes 4aa12c91
+ 00c509d4 bytes 4aa12d91
- 00c505e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c505e4 ["INT_ADD", "register:40f0:8", ["const:c505e4:8", "const:4:8"]]
- 00c505e4 ["CALLIND", null, ["register:0:8"]]
+ 00c50a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50a0c ["INT_ADD", "register:40f0:8", ["const:c50a0c:8", "const:4:8"]]
+ 00c50a0c ["CALLIND", null, ["register:0:8"]]
- 00c505e4 bytes 00013fd6
+ 00c50a0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df2fe2dfcf1be644a09aecec197716dd"></a>

### [`00c507d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c507d4.md) → [`00c50bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50bfc.md) FUN_00c50bfc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50c64",
      "incomplete_value": false,
      "site": "00c50c64",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5083c",
      "incomplete_value": false,
      "site": "00c5083c",
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
            "const:990:8"
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
      "00c50c64",
      "DATA",
      [
        "storage",
        "00c99990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50c64",
      "DATA",
      [
        "storage",
        "00c99d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c507d4.md#insn-00c5080c) · [`00c50830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c507d4.md#insn-00c50830) · [`00c50874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c507d4.md#insn-00c50874)
- 新版 `00c50c34`（命令位置の公開資料なし） · `00c50c58`（命令位置の公開資料なし） · `00c50c9c`（命令位置の公開資料なし）

~~~diff
- 00c5080c ["INT_ADD", "register:40f0:8", ["const:c5080c:8", "const:4:8"]]
- 00c5080c ["CALL", null, ["callee:00c5a020:8"]]
+ 00c50c34 ["INT_ADD", "register:40f0:8", ["const:c50c34:8", "const:4:8"]]
+ 00c50c34 ["CALL", null, ["callee:00c5a020:8"]]
- 00c5080c bytes 05250094
+ 00c50c34 bytes fb240094
- 00c50830 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00c50830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50c58 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00c50c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50830 bytes 08412691
+ 00c50c58 bytes 08413691
- 00c50874 ["INT_ADD", "register:40f0:8", ["const:c50874:8", "const:4:8"]]
- 00c50874 ["CALL", null, ["callee:00c58020:8"]]
+ 00c50c9c ["INT_ADD", "register:40f0:8", ["const:c50c9c:8", "const:4:8"]]
+ 00c50c9c ["CALL", null, ["callee:00c58020:8"]]
- 00c50874 bytes eb1c0094
+ 00c50c9c bytes e11c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08fedbc033a442177668815cd61743e"></a>

### [`00c508a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c508a4.md) → [`00c50ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ccc.md) FUN_00c50ccc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c50e48",
      "incomplete_value": false,
      "site": "00c50e60",
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
      "definition_site": "00c50a20",
      "incomplete_value": false,
      "site": "00c50a38",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c50e50",
      "incomplete_value": false,
      "site": "00c50e60",
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
            "const:58a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50a28",
      "incomplete_value": false,
      "site": "00c50a38",
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
            "const:54a:8"
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
      "definition_site": "00c50e58",
      "incomplete_value": false,
      "site": "00c50e60",
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
      "definition_site": "00c50a30",
      "incomplete_value": false,
      "site": "00c50a38",
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
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c50e48",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ],
    [
      "00c50e50",
      "PARAM",
      [
        "storage",
        "002ac54a",
        null,
        "string"
      ]
    ],
    [
      "00c50e58",
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
      "00c50e48",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c50e50",
      "PARAM",
      [
        "storage",
        "002ac58a",
        null,
        "string"
      ]
    ],
    [
      "00c50e58",
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

- 旧版 [`00c50a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c508a4.md#insn-00c50a38) · [`00c50900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c508a4.md#insn-00c50900) · [`00c50948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c508a4.md#insn-00c50948)
- 新版 `00c50e60`（命令位置の公開資料なし） · `00c50d28`（命令位置の公開資料なし） · `00c50d70`（命令位置の公開資料なし）

~~~diff
- 00c50a38 ["INT_ADD", "register:40f0:8", ["const:c50a38:8", "const:4:8"]]
- 00c50a38 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c50e60 ["INT_ADD", "register:40f0:8", ["const:c50e60:8", "const:4:8"]]
+ 00c50e60 ["CALL", null, ["callee:00c3800c:8"]]
- 00c50a38 bytes 6b9cff97
+ 00c50e60 bytes 6b9cff97
- 00c50900 ["INT_ADD", "register:40f0:8", ["const:c50900:8", "const:4:8"]]
- 00c50900 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50d28 ["INT_ADD", "register:40f0:8", ["const:c50d28:8", "const:4:8"]]
+ 00c50d28 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50900 bytes e8240094
+ 00c50d28 bytes de240094
- 00c50948 ["INT_ADD", "register:40f0:8", ["const:c50948:8", "const:4:8"]]
- 00c50948 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c50d70 ["INT_ADD", "register:40f0:8", ["const:c50d70:8", "const:4:8"]]
+ 00c50d70 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c50948 bytes d6240094
+ 00c50d70 bytes cc240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-878fb635b3f0ca0287bcb18460006f48"></a>

### [`00c50a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md) → [`00c50e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50e78.md) FUN_00c50e78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50ee4",
      "incomplete_value": false,
      "site": "00c50ee4",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50abc",
      "incomplete_value": false,
      "site": "00c50abc",
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
            "const:a00:8"
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
      "00c50ee4",
      "DATA",
      [
        "storage",
        "00c99a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50ee4",
      "DATA",
      [
        "storage",
        "00c99e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50a88) · [`00c50ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50ab4) · [`00c50b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50b00)
- 新版 `00c50eb0`（命令位置の公開資料なし） · `00c50edc`（命令位置の公開資料なし） · `00c50f28`（命令位置の公開資料なし）

~~~diff
- 00c50a88 ["INT_ADD", "register:40f0:8", ["const:c50a88:8", "const:4:8"]]
- 00c50a88 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c50eb0 ["INT_ADD", "register:40f0:8", ["const:c50eb0:8", "const:4:8"]]
+ 00c50eb0 ["CALL", null, ["callee:00c5a020:8"]]
- 00c50a88 bytes 66240094
+ 00c50eb0 bytes 5c240094
- 00c50ab4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00c50ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50edc ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00c50edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50ab4 bytes 08012891
+ 00c50edc bytes 08013891
- 00c50b00 ["INT_ADD", "register:40f0:8", ["const:c50b00:8", "const:4:8"]]
- 00c50b00 ["CALL", null, ["callee:00c58020:8"]]
+ 00c50f28 ["INT_ADD", "register:40f0:8", ["const:c50f28:8", "const:4:8"]]
+ 00c50f28 ["CALL", null, ["callee:00c58020:8"]]
- 00c50b00 bytes 481c0094
+ 00c50f28 bytes 3e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04eb23244f702c64c96b78e5583c552"></a>

### [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) → [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) FUN_00c51b74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c51414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md) [`00c51624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md) · 呼出先 6件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)
- 新版 呼出元 2件 [`00c5183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md) [`00c51a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md) · 呼出先 6件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51cdc",
      "incomplete_value": false,
      "site": "00c51cf4",
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
      "definition_site": "00c518b4",
      "incomplete_value": false,
      "site": "00c518cc",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51ce4",
      "incomplete_value": false,
      "site": "00c51cf4",
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
      "definition_site": "00c518bc",
      "incomplete_value": false,
      "site": "00c518cc",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51cec",
      "incomplete_value": false,
      "site": "00c51cf4",
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
            "const:9b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c518c4",
      "incomplete_value": false,
      "site": "00c518cc",
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
            "const:8e4:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51cdc",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ],
    [
      "00c51ce4",
      "PARAM",
      [
        "storage",
        "002b2856",
        null,
        "string"
      ]
    ],
    [
      "00c51cec",
      "PARAM",
      [
        "storage",
        "002a88e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c51cdc",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c51ce4",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c51cec",
      "PARAM",
      [
        "storage",
        "002a89b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c518cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md#insn-00c518cc) · [`00c517a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md#insn-00c517a4) · [`00c517e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md#insn-00c517e4)
- 新版 `00c51cf4`（命令位置の公開資料なし） · `00c51bcc`（命令位置の公開資料なし） · `00c51c0c`（命令位置の公開資料なし）

~~~diff
- 00c518cc ["INT_ADD", "register:40f0:8", ["const:c518cc:8", "const:4:8"]]
- 00c518cc ["CALL", null, ["callee:00c3800c:8"]]
+ 00c51cf4 ["INT_ADD", "register:40f0:8", ["const:c51cf4:8", "const:4:8"]]
+ 00c51cf4 ["CALL", null, ["callee:00c3800c:8"]]
- 00c518cc bytes c698ff97
+ 00c51cf4 bytes c698ff97
- 00c517a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c517a4 ["INT_ADD", "register:40f0:8", ["const:c517a4:8", "const:4:8"]]
- 00c517a4 ["CALLIND", null, ["register:0:8"]]
+ 00c51bcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51bcc ["INT_ADD", "register:40f0:8", ["const:c51bcc:8", "const:4:8"]]
+ 00c51bcc ["CALLIND", null, ["register:0:8"]]
- 00c517a4 bytes 00013fd6
+ 00c51bcc bytes 00013fd6
- 00c517e4 ["INT_ADD", "register:40f0:8", ["const:c517e4:8", "const:4:8"]]
- 00c517e4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c51c0c ["INT_ADD", "register:40f0:8", ["const:c51c0c:8", "const:4:8"]]
+ 00c51c0c ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c517e4 bytes 2f210094
+ 00c51c0c bytes 25210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf0842d2b986d7f27c5ef4342cb589e6"></a>

### [`00c51b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b3c.md) → [`00c51f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f64.md) __cxa_free_exception

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b20.md) · 呼出先 1件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md)
- 新版 呼出元 1件 [`00c57f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f20.md) · 呼出先 1件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00c51f74",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51b4c",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "00c51f74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ],
  "added": [
    [
      "00c51f74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b3c.md#insn-00c51b4c)
- 新版 `00c51f74`（命令位置の公開資料なし）

~~~diff
- 00c51b4c ["INT_ADD", "register:40f0:8", ["const:c51b4c:8", "const:4:8"]]
- 00c51b4c ["CALL", null, ["ram:c523f0:8"]]
+ 00c51f74 ["INT_ADD", "register:40f0:8", ["const:c51f74:8", "const:4:8"]]
+ 00c51f74 ["CALL", null, ["ram:c52818:8"]]
- 00c51b4c bytes 29020094
+ 00c51f74 bytes 29020094
~~~


<a id="compare-3d74f92a9c52f5922597386bea30d28c"></a>

### [`00c51bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md) → [`00c51ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md) FUN_00c51ff8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c51b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b60.md) · 呼出先 4件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c51f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f88.md) · 呼出先 4件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

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
      "site": "00c5203c",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51c14",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "00c5203c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ],
  "added": [
    [
      "00c5203c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md#insn-00c51c14) · [`00c51bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md#insn-00c51bf4) · [`00c51c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md#insn-00c51c0c)
- 新版 `00c5203c`（命令位置の公開資料なし） · `00c5201c`（命令位置の公開資料なし） · `00c52034`（命令位置の公開資料なし）

~~~diff
- 00c51c14 ["INT_ADD", "register:40f0:8", ["const:c51c14:8", "const:4:8"]]
- 00c51c14 ["CALL", null, ["ram:c523f0:8"]]
+ 00c5203c ["INT_ADD", "register:40f0:8", ["const:c5203c:8", "const:4:8"]]
+ 00c5203c ["CALL", null, ["ram:c52818:8"]]
- 00c51c14 bytes f7010094
+ 00c5203c bytes f7010094
- 00c51bf4 ["INT_ADD", "register:40f0:8", ["const:c51bf4:8", "const:4:8"]]
- 00c51bf4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00c5201c ["INT_ADD", "register:40f0:8", ["const:c5201c:8", "const:4:8"]]
+ 00c5201c ["CALL", null, ["callee:00c53d00:8"]]
- 00c51bf4 bytes 3b070094
+ 00c5201c bytes 39070094
- 00c51c0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51c0c ["INT_ADD", "register:40f0:8", ["const:c51c0c:8", "const:4:8"]]
- 00c51c0c ["CALLIND", null, ["register:0:8"]]
+ 00c52034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52034 ["INT_ADD", "register:40f0:8", ["const:c52034:8", "const:4:8"]]
+ 00c52034 ["CALLIND", null, ["register:0:8"]]
- 00c51c0c bytes 00013fd6
+ 00c52034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9324ea06141b81c78e19edf95d5e04"></a>

### [`00c51d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51d08.md) → [`00c52130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md) __cxa_end_catch

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ed0.md) · 呼出先 4件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c53d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d1c.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 1件 [`00c582d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582d0.md) · 呼出先 4件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5413c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c5413c.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

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
      "site": "00c521a0",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51d78",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "site": "00c521d0",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51da8",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "00c521a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ],
    [
      "00c521d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ],
  "added": [
    [
      "00c521a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ],
    [
      "00c521d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51d08.md#insn-00c51d78) · [`00c51da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51d08.md#insn-00c51da8) · [`00c51d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51d08.md#insn-00c51d18)
- 新版 `00c521a0`（命令位置の公開資料なし） · `00c521d0`（命令位置の公開資料なし） · `00c52140`（命令位置の公開資料なし）

~~~diff
- 00c51d78 ["INT_ADD", "register:40f0:8", ["const:c51d78:8", "const:4:8"]]
- 00c51d78 ["CALL", null, ["ram:c523f0:8"]]
+ 00c521a0 ["INT_ADD", "register:40f0:8", ["const:c521a0:8", "const:4:8"]]
+ 00c521a0 ["CALL", null, ["ram:c52818:8"]]
- 00c51d78 bytes 9e010094
+ 00c521a0 bytes 9e010094
- 00c51da8 ["INT_ADD", "register:40f0:8", ["const:c51da8:8", "const:4:8"]]
- 00c51da8 ["CALL", null, ["ram:c523f0:8"]]
+ 00c521d0 ["INT_ADD", "register:40f0:8", ["const:c521d0:8", "const:4:8"]]
+ 00c521d0 ["CALL", null, ["ram:c52818:8"]]
- 00c51da8 bytes 92010094
+ 00c521d0 bytes 92010094
- 00c51d18 ["INT_ADD", "register:40f0:8", ["const:c51d18:8", "const:4:8"]]
- 00c51d18 ["CALL", null, ["callee:00c5eda0:8"]]
+ 00c52140 ["INT_ADD", "register:40f0:8", ["const:c52140:8", "const:4:8"]]
+ 00c52140 ["CALL", null, ["callee:00c5eda0:8"]]
- 00c51d18 bytes 22330094
+ 00c52140 bytes 18330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04171ac7ead4b2966ba5e89300fd6d8d"></a>

### [`00c51df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md) → [`00c5221c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db10.md) · 呼出先 2件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df10.md) · 呼出先 2件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

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
      "site": "00c5225c",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51e34",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "00c5225c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ],
  "added": [
    [
      "00c5225c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md#insn-00c51e34) · [`00c51e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md#insn-00c51e14) · [`00c51e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md#insn-00c51e2c)
- 新版 `00c5225c`（命令位置の公開資料なし） · `00c5223c`（命令位置の公開資料なし） · `00c52254`（命令位置の公開資料なし）

~~~diff
- 00c51e34 ["INT_ADD", "register:40f0:8", ["const:c51e34:8", "const:4:8"]]
- 00c51e34 ["CALL", null, ["ram:c523f0:8"]]
+ 00c5225c ["INT_ADD", "register:40f0:8", ["const:c5225c:8", "const:4:8"]]
+ 00c5225c ["CALL", null, ["ram:c52818:8"]]
- 00c51e34 bytes 6f010094
+ 00c5225c bytes 6f010094
- 00c51e14 ["INT_ADD", "register:40f0:8", ["const:c51e14:8", "const:4:8"]]
- 00c51e14 ["CALL", null, ["callee:00c53d00:8"]]
+ 00c5223c ["INT_ADD", "register:40f0:8", ["const:c5223c:8", "const:4:8"]]
+ 00c5223c ["CALL", null, ["callee:00c53d00:8"]]
- 00c51e14 bytes b3060094
+ 00c5223c bytes b1060094
- 00c51e2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51e2c ["INT_ADD", "register:40f0:8", ["const:c51e2c:8", "const:4:8"]]
- 00c51e2c ["CALLIND", null, ["register:0:8"]]
+ 00c52254 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52254 ["INT_ADD", "register:40f0:8", ["const:c52254:8", "const:4:8"]]
+ 00c52254 ["CALLIND", null, ["register:0:8"]]
- 00c51e2c bytes 00013fd6
+ 00c52254 bytes 00013fd6
~~~


<a id="compare-249fabf89286ab8ef77f2524a2169fa9"></a>

### [`00c52150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md) → [`00c52578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md) FUN_00c52578

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 4件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c52458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52458.md) · 呼出先 4件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00c525c4",
      "value": [
        "leaf",
        "ram:c52818:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5219c",
      "value": [
        "leaf",
        "ram:c523f0:8"
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
      "00c525c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ],
    [
      "00c525d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ],
  "added": [
    [
      "00c525c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ],
    [
      "00c525d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md#insn-00c5219c) · [`00c5217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md#insn-00c5217c) · [`00c52194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md#insn-00c52194)
- 新版 `00c525c4`（命令位置の公開資料なし） · `00c525a4`（命令位置の公開資料なし） · `00c525bc`（命令位置の公開資料なし）

~~~diff
- 00c5219c ["INT_ADD", "register:40f0:8", ["const:c5219c:8", "const:4:8"]]
- 00c5219c ["CALL", null, ["ram:c523f0:8"]]
+ 00c525c4 ["INT_ADD", "register:40f0:8", ["const:c525c4:8", "const:4:8"]]
+ 00c525c4 ["CALL", null, ["ram:c52818:8"]]
- 00c5219c bytes 95000094
+ 00c525c4 bytes 95000094
- 00c5217c ["INT_ADD", "register:40f0:8", ["const:c5217c:8", "const:4:8"]]
- 00c5217c ["CALL", null, ["callee:00c53d00:8"]]
+ 00c525a4 ["INT_ADD", "register:40f0:8", ["const:c525a4:8", "const:4:8"]]
+ 00c525a4 ["CALL", null, ["callee:00c53d00:8"]]
- 00c5217c bytes d9050094
+ 00c525a4 bytes d7050094
- 00c52194 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c52194 ["INT_ADD", "register:40f0:8", ["const:c52194:8", "const:4:8"]]
- 00c52194 ["CALLIND", null, ["register:0:8"]]
+ 00c525bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c525bc ["INT_ADD", "register:40f0:8", ["const:c525bc:8", "const:4:8"]]
+ 00c525bc ["CALLIND", null, ["register:0:8"]]
- 00c52194 bytes 00013fd6
+ 00c525bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-140ef1f180f5ffa66df39c3b6134772a"></a>

### [`00c52268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md) → [`00c52690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md) FUN_00c52690

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) · 呼出先 3件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 1件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) · 呼出先 3件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.02% / 新版 82.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c526e0",
      "incomplete_value": true,
      "site": "00c526e0",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c522b8",
      "incomplete_value": true,
      "site": "00c522b8",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c526d8",
      "incomplete_value": false,
      "site": "00c526e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c522b0",
      "incomplete_value": false,
      "site": "00c522b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:6ac:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c526e4",
      "incomplete_value": false,
      "site": "00c526e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c522bc",
      "incomplete_value": false,
      "site": "00c522bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:6ac:8"
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
      "00c526a8",
      "PARAM",
      [
        "storage",
        "01128668",
        null,
        null
      ]
    ],
    [
      "00c526b4",
      "READ",
      [
        "storage",
        "01128690",
        null,
        "undefined8"
      ]
    ],
    [
      "00c526e0",
      "WRITE",
      [
        "storage",
        "01128690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c526a8",
      "PARAM",
      [
        "storage",
        "01128a68",
        null,
        null
      ]
    ],
    [
      "00c526b4",
      "READ",
      [
        "storage",
        "01128a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00c526e0",
      "WRITE",
      [
        "storage",
        "01128a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md#insn-00c52284) · [`00c522b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md#insn-00c522b8) · [`00c52368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md#insn-00c52368)
- 新版 `00c526ac`（命令位置の公開資料なし） · `00c526e0`（命令位置の公開資料なし） · `00c52790`（命令位置の公開資料なし）

~~~diff
- 00c52284 ["INT_ADD", "register:40f0:8", ["const:c52284:8", "const:4:8"]]
- 00c52284 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c526ac ["INT_ADD", "register:40f0:8", ["const:c526ac:8", "const:4:8"]]
+ 00c526ac ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c52284 bytes 07240094
+ 00c526ac bytes fd230094
- 00c522b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:690:8"]]
- 00c522b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
+ 00c526e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
+ 00c526e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00c522b8 bytes 0e4903f9
+ 00c526e0 bytes 0e4905f9
- 00c52368 ["INT_ADD", "register:40f0:8", ["const:c52368:8", "const:4:8"]]
- 00c52368 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c52790 ["INT_ADD", "register:40f0:8", ["const:c52790:8", "const:4:8"]]
+ 00c52790 ["CALL", null, ["callee:00c3800c:8"]]
- 00c52368 bytes 1f96ff97
+ 00c52790 bytes 1f96ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16a289f1521742a7f9b447fcd061c816"></a>

### [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) → [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) __gxx_personality_v0

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c52cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md) [`00c52e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52e80.md) [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c53100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md) [`00c532a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c532a8.md) [`00c540d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c540d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c52c9c",
      "incomplete_value": true,
      "site": "00c52c9c",
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
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52874",
      "incomplete_value": true,
      "site": "00c52874",
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
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
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
      "00c52c8c",
      "DATA",
      [
        "storage",
        "00313d68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c52c8c",
      "DATA",
      [
        "storage",
        "00313da8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c525a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md#insn-00c525a0) · [`00c525b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md#insn-00c525b0) · [`00c525bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md#insn-00c525bc)
- 新版 `00c529c8`（命令位置の公開資料なし） · `00c529d8`（命令位置の公開資料なし） · `00c529e4`（命令位置の公開資料なし）

~~~diff
- 00c525a0 ["INT_ADD", "register:40f0:8", ["const:c525a0:8", "const:4:8"]]
- 00c525a0 ["CALL", null, ["callee:00c54158:8"]]
+ 00c529c8 ["INT_ADD", "register:40f0:8", ["const:c529c8:8", "const:4:8"]]
+ 00c529c8 ["CALL", null, ["callee:00c54158:8"]]
- 00c525a0 bytes e6050094
+ 00c529c8 bytes e4050094
- 00c525b0 ["INT_ADD", "register:40f0:8", ["const:c525b0:8", "const:4:8"]]
- 00c525b0 ["CALL", null, ["callee:00c54158:8"]]
+ 00c529d8 ["INT_ADD", "register:40f0:8", ["const:c529d8:8", "const:4:8"]]
+ 00c529d8 ["CALL", null, ["callee:00c54158:8"]]
- 00c525b0 bytes e2050094
+ 00c529d8 bytes e0050094
- 00c525bc ["INT_ADD", "register:40f0:8", ["const:c525bc:8", "const:4:8"]]
- 00c525bc ["CALL", null, ["callee:00c54190:8"]]
+ 00c529e4 ["INT_ADD", "register:40f0:8", ["const:c529e4:8", "const:4:8"]]
+ 00c529e4 ["CALL", null, ["callee:00c54190:8"]]
- 00c525bc bytes ed050094
+ 00c529e4 bytes eb050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef29fa1001f2b5a8b9627611ddc15c58"></a>

### [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) → [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) __cxa_call_unexpected

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c51a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a2c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c51e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c53038",
      "incomplete_value": true,
      "site": "00c5303c",
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
      "definition_site": "00c52c10",
      "incomplete_value": true,
      "site": "00c52c14",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5304c",
      "incomplete_value": true,
      "site": "00c53060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52c24",
      "incomplete_value": true,
      "site": "00c52c38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53098",
      "incomplete_value": true,
      "site": "00c530a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52c70",
      "incomplete_value": true,
      "site": "00c52c78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
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
      "00c53034",
      "READ",
      [
        "storage",
        "00c9ba58",
        null,
        "pointer"
      ]
    ],
    [
      "00c5303c",
      "DATA",
      [
        "storage",
        "00c96268",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c5304c",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c53034",
      "READ",
      [
        "storage",
        "00c9be58",
        null,
        "pointer"
      ]
    ],
    [
      "00c5303c",
      "DATA",
      [
        "storage",
        "00c96668",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c5304c",
      "READ",
      [
        "storage",
        "00c9be60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md#insn-00c52c38) · [`00c52c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md#insn-00c52c78) · [`00c52ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md#insn-00c52ae4)
- 新版 `00c53060`（命令位置の公開資料なし） · `00c530a0`（命令位置の公開資料なし） · `00c52f0c`（命令位置の公開資料なし）

~~~diff
- 00c52c38 ["INT_ADD", "register:40f0:8", ["const:c52c38:8", "const:4:8"]]
- 00c52c38 ["CALL", null, ["callee:00c532a8:8"]]
+ 00c53060 ["INT_ADD", "register:40f0:8", ["const:c53060:8", "const:4:8"]]
+ 00c53060 ["CALL", null, ["callee:00c532a8:8"]]
- 00c52c38 bytes 92000094
+ 00c53060 bytes 92000094
- 00c52c78 ["INT_ADD", "register:40f0:8", ["const:c52c78:8", "const:4:8"]]
- 00c52c78 ["CALL", null, ["callee:00c57f10:8"]]
+ 00c530a0 ["INT_ADD", "register:40f0:8", ["const:c530a0:8", "const:4:8"]]
+ 00c530a0 ["CALL", null, ["callee:00c57f10:8"]]
- 00c52c78 bytes a6130094
+ 00c530a0 bytes 9c130094
- 00c52ae4 ["INT_ADD", "register:40f0:8", ["const:c52ae4:8", "const:4:8"]]
- 00c52ae4 ["CALL", null, ["callee:00c58010:8"]]
+ 00c52f0c ["INT_ADD", "register:40f0:8", ["const:c52f0c:8", "const:4:8"]]
+ 00c52f0c ["CALL", null, ["callee:00c58010:8"]]
- 00c52ae4 bytes 4b140094
+ 00c52f0c bytes 41140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d5b5e679d2c44b511e76a80be341ec"></a>

### [`00c530dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md) → [`00c53504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md) __emutls_get_address

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md) · 呼出先 11件 [`00c53304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md) · 呼出先 11件 [`00c5372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c535c0",
      "incomplete_value": false,
      "site": "00c535c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53198",
      "incomplete_value": false,
      "site": "00c53198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c535b8",
      "incomplete_value": true,
      "site": "00c535c0",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53190",
      "incomplete_value": true,
      "site": "00c53198",
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
            "const:1:8"
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
      "definition_site": "00c535b8",
      "incomplete_value": true,
      "site": "00c535c4",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53190",
      "incomplete_value": true,
      "site": "00c5319c",
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
            "const:1:8"
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
      "00c5352c",
      "READ",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53594",
      "PARAM",
      [
        "storage",
        "00c53304",
        null,
        null
      ]
    ],
    [
      "00c53598",
      "PARAM",
      [
        "storage",
        "011288a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c5352c",
      "READ",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53594",
      "PARAM",
      [
        "storage",
        "00c5372c",
        null,
        null
      ]
    ],
    [
      "00c53598",
      "PARAM",
      [
        "storage",
        "01128ca8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md#insn-00c53108) · [`00c53174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md#insn-00c53174) · [`00c53198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md#insn-00c53198)
- 新版 `00c53530`（命令位置の公開資料なし） · `00c5359c`（命令位置の公開資料なし） · `00c535c0`（命令位置の公開資料なし）

~~~diff
- 00c53108 ["INT_ADD", "register:40f0:8", ["const:c53108:8", "const:4:8"]]
- 00c53108 ["CALL", null, ["callee:00c5e1f0:8"]]
+ 00c53530 ["INT_ADD", "register:40f0:8", ["const:c53530:8", "const:4:8"]]
+ 00c53530 ["CALL", null, ["callee:00c5e1f0:8"]]
- 00c53108 bytes 3a2b0094
+ 00c53530 bytes 302b0094
- 00c53174 ["INT_ADD", "register:40f0:8", ["const:c53174:8", "const:4:8"]]
- 00c53174 ["CALL", null, ["callee:00c5b6c0:8"]]
+ 00c5359c ["INT_ADD", "register:40f0:8", ["const:c5359c:8", "const:4:8"]]
+ 00c5359c ["CALL", null, ["callee:00c5b6c0:8"]]
- 00c53174 bytes 53200094
+ 00c5359c bytes 49200094
- 00c53198 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8b0:8"]]
- 00c53198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00c535c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 00c535c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00c53198 bytes 165904f9
+ 00c535c0 bytes 165906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a14a89c0098aa6524638361675c3e18c"></a>

### [`00c532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c532c8.md) → [`00c536f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c536f0.md) FUN_00c536f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043ade8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ade8.md) · 呼出先 1件 [`00c5eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb10.md)
- 新版 呼出元 1件 [`0043ae28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae28.md) · 呼出先 1件 [`00c5ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53714",
      "incomplete_value": true,
      "site": "00c53718",
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
      "definition_site": "00c532ec",
      "incomplete_value": true,
      "site": "00c532f0",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c536f8",
      "READ",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c53714",
      "READ",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c5371c",
      "WRITE",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c536f8",
      "READ",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c53714",
      "READ",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c5371c",
      "WRITE",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c532f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c532c8.md#insn-00c532f0) · [`00c532d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c532c8.md#insn-00c532d0) · [`00c532e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c532c8.md#insn-00c532e8)
- 新版 `00c53718`（命令位置の公開資料なし） · `00c536f8`（命令位置の公開資料なし） · `00c53710`（命令位置の公開資料なし）

~~~diff
- 00c532f0 ["INT_ADD", "register:40f0:8", ["const:c532f0:8", "const:4:8"]]
- 00c532f0 ["CALL", null, ["callee:00c5ef10:8"]]
+ 00c53718 ["INT_ADD", "register:40f0:8", ["const:c53718:8", "const:4:8"]]
+ 00c53718 ["CALL", null, ["callee:00c5ef10:8"]]
- 00c532f0 bytes 082e0094
+ 00c53718 bytes fe2d0094
- 00c532d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8a0:8"]]
- 00c532d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00c532d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00c536f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
+ 00c536f8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c536f8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00c532d0 bytes 08816239
+ 00c536f8 bytes 08817239
- 00c532e8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00c532e8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c532e8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c532e8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c53710 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c53710 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c53710 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c53710 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c532e8 bytes 73822291
+ 00c53710 bytes 73823291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49def63108478600159e94d068b0de6f"></a>

### [`00c53304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md) → [`00c5372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md) FUN_00c5372c

採用 · 移動量 `+0x428` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c530dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md) · 呼出先 3件 [`00c53340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53340.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c53504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md) · 呼出先 3件 [`00c53768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53768.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53754",
      "incomplete_value": false,
      "site": "00c53754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5332c",
      "incomplete_value": false,
      "site": "00c5332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c53738",
      "incomplete_value": false,
      "site": "00c53744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ca4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53310",
      "incomplete_value": false,
      "site": "00c5331c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8a4:8"
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
      "definition_site": "00c53740",
      "incomplete_value": false,
      "site": "00c53744",
      "value": [
        "leaf",
        "const:c53768:8"
      ]
    },
    "old": {
      "definition_site": "00c53318",
      "incomplete_value": false,
      "site": "00c5331c",
      "value": [
        "leaf",
        "const:c53340:8"
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
      "00c53738",
      "PARAM",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53740",
      "PARAM",
      [
        "storage",
        "00c53340",
        null,
        null
      ]
    ],
    [
      "00c53754",
      "WRITE",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c53738",
      "PARAM",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53740",
      "PARAM",
      [
        "storage",
        "00c53768",
        null,
        null
      ]
    ],
    [
      "00c53754",
      "WRITE",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md#insn-00c5331c) · [`00c5332c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md#insn-00c5332c) · [`00c53310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md#insn-00c53310)
- 新版 `00c53744`（命令位置の公開資料なし） · `00c53754`（命令位置の公開資料なし） · `00c53738`（命令位置の公開資料なし）

~~~diff
- 00c5331c ["INT_ADD", "register:40f0:8", ["const:c5331c:8", "const:4:8"]]
- 00c5331c ["CALL", null, ["callee:00c5a300:8"]]
+ 00c53744 ["INT_ADD", "register:40f0:8", ["const:c53744:8", "const:4:8"]]
+ 00c53744 ["CALL", null, ["callee:00c5a300:8"]]
- 00c5331c bytes f91a0094
+ 00c53744 bytes ef1a0094
- 00c5332c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00c5332c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8a0:8"]]
- 00c5332c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c53754 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00c53754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:ca0:8"]]
+ 00c53754 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00c5332c bytes 09812239
+ 00c53754 bytes 09813239
- 00c53310 ["COPY", "tmp:0:8", ["const:8a4:8"]]
- 00c53310 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c53310 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c53310 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c53738 ["COPY", "tmp:0:8", ["const:ca4:8"]]
+ 00c53738 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c53738 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c53738 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c53310 bytes 00902291
+ 00c53738 bytes 00903291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df8a52a043934d578b97b67f59f35dad"></a>

### [`00c53404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53404.md) → [`00c53824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53824.md) _INIT_0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md) [`00c5eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md) [`00c5ef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef20.md) [`00c5ef30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53844",
      "incomplete_value": false,
      "site": "00c53844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53424",
      "incomplete_value": false,
      "site": "00c53424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53890",
      "incomplete_value": false,
      "site": "00c53890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53470",
      "incomplete_value": false,
      "site": "00c53470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c538ac",
      "incomplete_value": false,
      "site": "00c538ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5348c",
      "incomplete_value": false,
      "site": "00c5348c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "00c53844",
      "WRITE",
      [
        "storage",
        "011288e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c53858",
      "PARAM",
      [
        "storage",
        "002a62f5",
        null,
        "string"
      ]
    ],
    [
      "00c53870",
      "PARAM",
      [
        "storage",
        "002a9918",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53844",
      "WRITE",
      [
        "storage",
        "01128ce0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c53858",
      "PARAM",
      [
        "storage",
        "002a63d1",
        null,
        "string"
      ]
    ],
    [
      "00c53870",
      "PARAM",
      [
        "storage",
        "002a99e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53404.md#insn-00c53424) · [`00c53440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53404.md#insn-00c53440) · [`00c5345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53404.md#insn-00c5345c)
- 新版 `00c53844`（命令位置の公開資料なし） · `00c53860`（命令位置の公開資料なし） · `00c5387c`（命令位置の公開資料なし）

~~~diff
- 00c53424 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00c53424 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00c53424 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:8e0:8"]]
- 00c53424 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00c53844 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00c53844 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00c53844 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:ce0:8"]]
+ 00c53844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00c53424 bytes 3f812339
+ 00c53844 bytes 3f813339
- 00c53440 ["INT_ADD", "register:40f0:8", ["const:c53440:8", "const:4:8"]]
- 00c53440 ["CALL", null, ["callee:00c5ef30:8"]]
+ 00c53860 ["INT_ADD", "register:40f0:8", ["const:c53860:8", "const:4:8"]]
+ 00c53860 ["CALL", null, ["callee:00c5ef30:8"]]
- 00c53440 bytes bc2d0094
+ 00c53860 bytes b42d0094
- 00c5345c ["INT_ADD", "register:40f0:8", ["const:c5345c:8", "const:4:8"]]
- 00c5345c ["CALL", null, ["callee:00c5d130:8"]]
+ 00c5387c ["INT_ADD", "register:40f0:8", ["const:c5387c:8", "const:4:8"]]
+ 00c5387c ["CALL", null, ["callee:00c5d130:8"]]
- 00c5345c bytes 35260094
+ 00c5387c bytes 2d260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4bbe4b4fe6e44436e8c631a7ae14a7"></a>

### [`00c53748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53748.md) → [`00c53b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md) _INIT_1

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c5349c.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md) [`00c5eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c538bc.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md) [`00c5ef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef20.md) [`00c5ef30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef30.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c53b74",
      "incomplete_value": true,
      "site": "00c53b74",
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
      "definition_site": "00c53754",
      "incomplete_value": true,
      "site": "00c53754",
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
      "definition_site": "00c53b8c",
      "incomplete_value": false,
      "site": "00c53b94",
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
            "const:3d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5376c",
      "incomplete_value": false,
      "site": "00c53774",
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
            "const:2f5:8"
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
      "definition_site": "00c53ba4",
      "incomplete_value": false,
      "site": "00c53bb0",
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
            "const:9e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53784",
      "incomplete_value": false,
      "site": "00c53790",
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
            "const:918:8"
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
      "00c53b70",
      "READ",
      [
        "storage",
        "011288e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53b8c",
      "PARAM",
      [
        "storage",
        "002a62f5",
        null,
        "string"
      ]
    ],
    [
      "00c53ba4",
      "PARAM",
      [
        "storage",
        "002a9918",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53b70",
      "READ",
      [
        "storage",
        "01128ce8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53b8c",
      "PARAM",
      [
        "storage",
        "002a63d1",
        null,
        "string"
      ]
    ],
    [
      "00c53ba4",
      "PARAM",
      [
        "storage",
        "002a99e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53748.md#insn-00c53774) · [`00c53790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53748.md#insn-00c53790) · [`00c537c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53748.md#insn-00c537c0)
- 新版 `00c53b94`（命令位置の公開資料なし） · `00c53bb0`（命令位置の公開資料なし） · `00c53be0`（命令位置の公開資料なし）

~~~diff
- 00c53774 ["INT_ADD", "register:40f0:8", ["const:c53774:8", "const:4:8"]]
- 00c53774 ["CALL", null, ["callee:00c5ef30:8"]]
+ 00c53b94 ["INT_ADD", "register:40f0:8", ["const:c53b94:8", "const:4:8"]]
+ 00c53b94 ["CALL", null, ["callee:00c5ef30:8"]]
- 00c53774 bytes ef2c0094
+ 00c53b94 bytes e72c0094
- 00c53790 ["INT_ADD", "register:40f0:8", ["const:c53790:8", "const:4:8"]]
- 00c53790 ["CALL", null, ["callee:00c5d130:8"]]
+ 00c53bb0 ["INT_ADD", "register:40f0:8", ["const:c53bb0:8", "const:4:8"]]
+ 00c53bb0 ["CALL", null, ["callee:00c5d130:8"]]
- 00c53790 bytes 68250094
+ 00c53bb0 bytes 60250094
- 00c537c0 ["INT_ADD", "register:40f0:8", ["const:c537c0:8", "const:4:8"]]
- 00c537c0 ["CALL", null, ["ram:c5349c:8"]]
+ 00c53be0 ["INT_ADD", "register:40f0:8", ["const:c53be0:8", "const:4:8"]]
+ 00c53be0 ["CALL", null, ["ram:c538bc:8"]]
- 00c537c0 bytes 37ffff97
+ 00c53be0 bytes 37ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2df64930e71001fc2b70132abe24afc"></a>

### [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) → [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) FUN_00c53e28

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) · 呼出先 9件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) [`00c53fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fa4.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md)
- 新版 呼出元 2件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) · 呼出先 9件 [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) [`00c54248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54248.md) [`00c543c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543c4.md) [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md) [`00c54418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54418.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53f00",
      "incomplete_value": true,
      "site": "00c53f04",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ae0",
      "incomplete_value": true,
      "site": "00c53ae4",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53ee8",
      "incomplete_value": false,
      "site": "00c53f04",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ac8",
      "incomplete_value": false,
      "site": "00c53ae4",
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
            "const:e44:8"
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
      "definition_site": "00c53ef4",
      "incomplete_value": false,
      "site": "00c53f04",
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
            "const:57e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ad4",
      "incomplete_value": false,
      "site": "00c53ae4",
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
            "const:53e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c53ee8",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c53eec",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c53ef4",
      "PARAM",
      [
        "storage",
        "002ad53e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53ee8",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c53eec",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c53ef4",
      "PARAM",
      [
        "storage",
        "002ad57e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md#insn-00c53ae4) · [`00c53a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md#insn-00c53a30) · [`00c53a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md#insn-00c53a38)
- 新版 `00c53f04`（命令位置の公開資料なし） · `00c53e50`（命令位置の公開資料なし） · `00c53e58`（命令位置の公開資料なし）

~~~diff
- 00c53ae4 ["INT_ADD", "register:40f0:8", ["const:c53ae4:8", "const:4:8"]]
- 00c53ae4 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c53f04 ["INT_ADD", "register:40f0:8", ["const:c53f04:8", "const:4:8"]]
+ 00c53f04 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c53ae4 bytes 172c0094
+ 00c53f04 bytes 0f2c0094
- 00c53a30 ["INT_ADD", "register:40f0:8", ["const:c53a30:8", "const:4:8"]]
- 00c53a30 ["CALL", null, ["callee:00c541a0:8"]]
+ 00c53e50 ["INT_ADD", "register:40f0:8", ["const:c53e50:8", "const:4:8"]]
+ 00c53e50 ["CALL", null, ["callee:00c541a0:8"]]
- 00c53a30 bytes d4000094
+ 00c53e50 bytes d4000094
- 00c53a38 ["INT_ADD", "register:40f0:8", ["const:c53a38:8", "const:4:8"]]
- 00c53a38 ["CALL", null, ["callee:00c543c4:8"]]
+ 00c53e58 ["INT_ADD", "register:40f0:8", ["const:c53e58:8", "const:4:8"]]
+ 00c53e58 ["CALL", null, ["callee:00c543c4:8"]]
- 00c53a38 bytes 5b010094
+ 00c53e58 bytes 5b010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be56ca0334df837f1b673d528ecfb28"></a>

### [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) → [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) FUN_00c53f5c

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 256件 [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) · 呼出先 7件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) [`00c57828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57828.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 256件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md) · 呼出先 7件 [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) [`00c57c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57c48.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53fcc",
      "incomplete_value": true,
      "site": "00c53fd0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53bac",
      "incomplete_value": true,
      "site": "00c53bb0",
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
            "const:130:8"
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
      "definition_site": "00c53fb4",
      "incomplete_value": false,
      "site": "00c53fd0",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53b94",
      "incomplete_value": false,
      "site": "00c53bb0",
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
            "const:e44:8"
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
      "definition_site": "00c53fc0",
      "incomplete_value": false,
      "site": "00c53fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:6bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ba0",
      "incomplete_value": false,
      "site": "00c53bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:67d:8"
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
      "00c53fb4",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c53fb8",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c53fc0",
      "PARAM",
      [
        "storage",
        "002bd67d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53fb4",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c53fb8",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c53fc0",
      "PARAM",
      [
        "storage",
        "002bd6bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md#insn-00c53bb0) · [`00c53b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md#insn-00c53b58) · [`00c53b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md#insn-00c53b70)
- 新版 `00c53fd0`（命令位置の公開資料なし） · `00c53f78`（命令位置の公開資料なし） · `00c53f90`（命令位置の公開資料なし）

~~~diff
- 00c53bb0 ["INT_ADD", "register:40f0:8", ["const:c53bb0:8", "const:4:8"]]
- 00c53bb0 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c53fd0 ["INT_ADD", "register:40f0:8", ["const:c53fd0:8", "const:4:8"]]
+ 00c53fd0 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c53bb0 bytes e42b0094
+ 00c53fd0 bytes dc2b0094
- 00c53b58 ["INT_ADD", "register:40f0:8", ["const:c53b58:8", "const:4:8"]]
- 00c53b58 ["CALL", null, ["callee:00c57c48:8"]]
+ 00c53f78 ["INT_ADD", "register:40f0:8", ["const:c53f78:8", "const:4:8"]]
+ 00c53f78 ["CALL", null, ["callee:00c57c48:8"]]
- 00c53b58 bytes 340f0094
+ 00c53f78 bytes 340f0094
- 00c53b70 ["INT_ADD", "register:40f0:8", ["const:c53b70:8", "const:4:8"]]
- 00c53b70 ["CALL", null, ["callee:00c53e28:8"]]
+ 00c53f90 ["INT_ADD", "register:40f0:8", ["const:c53f90:8", "const:4:8"]]
+ 00c53f90 ["CALL", null, ["callee:00c53e28:8"]]
- 00c53b70 bytes a6ffff97
+ 00c53f90 bytes a6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0fd9789e632742baa9e4c69e1e10964"></a>

### [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) → [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) FUN_00c541a0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) · 呼出先 2件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) · 呼出先 2件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c541cc",
      "incomplete_value": false,
      "site": "00c541cc",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53dac",
      "incomplete_value": false,
      "site": "00c53dac",
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
            "const:bc0:8"
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
      "definition_site": "00c541cc",
      "incomplete_value": false,
      "site": "00c541cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53dac",
      "incomplete_value": false,
      "site": "00c53dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00c541cc",
      "DATA",
      [
        "storage",
        "00c99bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c541cc",
      "DATA",
      [
        "storage",
        "011288f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c541cc",
      "DATA",
      [
        "storage",
        "00c99fc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c541cc",
      "DATA",
      [
        "storage",
        "01128cf0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md#insn-00c53d94) · [`00c53d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md#insn-00c53d98) · [`00c53d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md#insn-00c53d9c)
- 新版 `00c541b4`（命令位置の公開資料なし） · `00c541bc`（命令位置の公開資料なし）

~~~diff
- 00c53d94 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00c53d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c53d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c53d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c541b4 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 00c541b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c541b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c541b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c53d94 bytes 08012f91
+ 00c541b4 bytes 08013f91
- 00c53d98 ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00c53d98 bytes a92600b0
- 00c53d9c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00c53d9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c53d9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c53d9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c541bc ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00c541bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c541bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c541bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c53d9c bytes 29c12391
+ 00c541bc bytes 29c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d049d10bb2ebe22634a5f758f1ab86"></a>

### [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) → [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) FUN_00c545d0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) · 呼出先 6件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md)
- 新版 呼出元 2件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) · 呼出先 6件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54884",
      "incomplete_value": true,
      "site": "00c54888",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54464",
      "incomplete_value": true,
      "site": "00c54468",
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
            "const:130:8"
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
      "definition_site": "00c5486c",
      "incomplete_value": false,
      "site": "00c54888",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5444c",
      "incomplete_value": false,
      "site": "00c54468",
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
            "const:e44:8"
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
      "definition_site": "00c54878",
      "incomplete_value": false,
      "site": "00c54888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:85f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54458",
      "incomplete_value": false,
      "site": "00c54468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:81f:8"
          ]
        ]
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
      "00c54634",
      "DATA",
      [
        "storage",
        "002bd6d0",
        null,
        "string"
      ]
    ],
    [
      "00c54710",
      "DATA",
      [
        "storage",
        "002a3e22",
        null,
        "string"
      ]
    ],
    [
      "00c5486c",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54634",
      "DATA",
      [
        "storage",
        "002bd710",
        null,
        "string"
      ]
    ],
    [
      "00c54710",
      "DATA",
      [
        "storage",
        "002a3eef",
        null,
        "string"
      ]
    ],
    [
      "00c5486c",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md#insn-00c54468) · [`00c54214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md#insn-00c54214) · [`00c54260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md#insn-00c54260)
- 新版 `00c54888`（命令位置の公開資料なし） · `00c54634`（命令位置の公開資料なし） · `00c54680`（命令位置の公開資料なし）

~~~diff
- 00c54468 ["INT_ADD", "register:40f0:8", ["const:c54468:8", "const:4:8"]]
- 00c54468 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c54888 ["INT_ADD", "register:40f0:8", ["const:c54888:8", "const:4:8"]]
+ 00c54888 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c54468 bytes b6290094
+ 00c54888 bytes ae290094
- 00c54214 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00c54214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c54214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c54214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c54634 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c54634 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c54634 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c54634 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c54214 bytes 00401b91
+ 00c54634 bytes 00401c91
- 00c54260 ["INT_ADD", "register:40f0:8", ["const:c54260:8", "const:4:8"]]
- 00c54260 ["CALL", null, ["callee:00c566ac:8"]]
+ 00c54680 ["INT_ADD", "register:40f0:8", ["const:c54680:8", "const:4:8"]]
+ 00c54680 ["CALL", null, ["callee:00c566ac:8"]]
- 00c54260 bytes 0b080094
+ 00c54680 bytes 0b080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a618048cf011f32c247bf20c66b0507"></a>

### [`00c544cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c544cc.md) → [`00c548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548ec.md) FUN_00c548ec

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c549c0",
      "incomplete_value": true,
      "site": "00c549c4",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c545a0",
      "incomplete_value": true,
      "site": "00c545a4",
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
            "const:130:8"
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
      "definition_site": "00c549a8",
      "incomplete_value": false,
      "site": "00c549c4",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54588",
      "incomplete_value": false,
      "site": "00c545a4",
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
            "const:e44:8"
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
      "definition_site": "00c549b4",
      "incomplete_value": false,
      "site": "00c549c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54594",
      "incomplete_value": false,
      "site": "00c545a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:74a:8"
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
      "00c549a8",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c549ac",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c549b4",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c549a8",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c549ac",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c549b4",
      "PARAM",
      [
        "storage",
        "002af78a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c545a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c544cc.md#insn-00c545a4) · [`00c54588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c544cc.md#insn-00c54588) · [`00c5458c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c544cc.md#insn-00c5458c)
- 新版 `00c549c4`（命令位置の公開資料なし） · `00c549a8`（命令位置の公開資料なし） · `00c549ac`（命令位置の公開資料なし）

~~~diff
- 00c545a4 ["INT_ADD", "register:40f0:8", ["const:c545a4:8", "const:4:8"]]
- 00c545a4 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c549c4 ["INT_ADD", "register:40f0:8", ["const:c549c4:8", "const:4:8"]]
+ 00c549c4 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c545a4 bytes 67290094
+ 00c549c4 bytes 5f290094
- 00c54588 ["COPY", "tmp:0:8", ["const:e44:8"]]
- 00c54588 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c54588 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c54588 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c549a8 ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 00c549a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c549a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c549a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c54588 bytes 21103991
+ 00c549a8 bytes 21443c91
- 00c5458c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00c5458c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c549ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00c549ac ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c5458c bytes 73be43f9
+ 00c549ac bytes 73be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97a65d29e54b98060ace9098f156cbbb"></a>

### [`00c545b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c545b4.md) → [`00c549d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c549d4.md) FUN_00c549d4

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54aa8",
      "incomplete_value": true,
      "site": "00c54aac",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54688",
      "incomplete_value": true,
      "site": "00c5468c",
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
            "const:130:8"
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
      "definition_site": "00c54a90",
      "incomplete_value": false,
      "site": "00c54aac",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54670",
      "incomplete_value": false,
      "site": "00c5468c",
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
            "const:e44:8"
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
      "definition_site": "00c54a9c",
      "incomplete_value": false,
      "site": "00c54aac",
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
            "const:dd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5467c",
      "incomplete_value": false,
      "site": "00c5468c",
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
            "const:d97:8"
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
      "00c54a90",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c54a94",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c54a9c",
      "PARAM",
      [
        "storage",
        "002b5d97",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54a90",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c54a94",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c54a9c",
      "PARAM",
      [
        "storage",
        "002b5dd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5468c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c545b4.md#insn-00c5468c) · [`00c54670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c545b4.md#insn-00c54670) · [`00c54674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c545b4.md#insn-00c54674)
- 新版 `00c54aac`（命令位置の公開資料なし） · `00c54a90`（命令位置の公開資料なし） · `00c54a94`（命令位置の公開資料なし）

~~~diff
- 00c5468c ["INT_ADD", "register:40f0:8", ["const:c5468c:8", "const:4:8"]]
- 00c5468c ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c54aac ["INT_ADD", "register:40f0:8", ["const:c54aac:8", "const:4:8"]]
+ 00c54aac ["CALL", null, ["callee:00c5ef40:8"]]
- 00c5468c bytes 2d290094
+ 00c54aac bytes 25290094
- 00c54670 ["COPY", "tmp:0:8", ["const:e44:8"]]
- 00c54670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c54670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c54670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c54a90 ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 00c54a90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54a90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54a90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c54670 bytes 21103991
+ 00c54a90 bytes 21443c91
- 00c54674 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00c54674 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c54a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00c54a94 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c54674 bytes 73be43f9
+ 00c54a94 bytes 73be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b94721b0f43dbc454ce8db5b94e978b"></a>

### [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) → [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) FUN_00c54c68

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) · 呼出先 10件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) · 呼出先 10件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) [`00c5750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5750c.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54cb8",
      "incomplete_value": false,
      "site": "00c54cc8",
      "value": [
        "leaf",
        "const:c5750c:8"
      ]
    },
    "old": {
      "definition_site": "00c54898",
      "incomplete_value": false,
      "site": "00c548a8",
      "value": [
        "leaf",
        "const:c570ec:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54cf4",
      "incomplete_value": false,
      "site": "00c54cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c548d4",
      "incomplete_value": false,
      "site": "00c548d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8f4:8"
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
      "definition_site": "00c54d3c",
      "incomplete_value": false,
      "site": "00c54d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5491c",
      "incomplete_value": false,
      "site": "00c54920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8f4:8"
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
      "00c54cb8",
      "PARAM",
      [
        "storage",
        "00c570ec",
        null,
        null
      ]
    ],
    [
      "00c54cf4",
      "PARAM",
      [
        "storage",
        "011288f4",
        null,
        null
      ]
    ],
    [
      "00c54d04",
      "READ",
      [
        "storage",
        "00ca44a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c54cb8",
      "PARAM",
      [
        "storage",
        "00c5750c",
        null,
        null
      ]
    ],
    [
      "00c54cf4",
      "PARAM",
      [
        "storage",
        "01128cf4",
        null,
        null
      ]
    ],
    [
      "00c54d04",
      "READ",
      [
        "storage",
        "00ca48a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c548a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md#insn-00c548a8) · [`00c548d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md#insn-00c548d8) · [`00c54920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md#insn-00c54920)
- 新版 `00c54cc8`（命令位置の公開資料なし） · `00c54cf8`（命令位置の公開資料なし） · `00c54d40`（命令位置の公開資料なし）

~~~diff
- 00c548a8 ["INT_ADD", "register:40f0:8", ["const:c548a8:8", "const:4:8"]]
- 00c548a8 ["CALL", null, ["callee:00c5ef70:8"]]
+ 00c54cc8 ["INT_ADD", "register:40f0:8", ["const:c54cc8:8", "const:4:8"]]
+ 00c54cc8 ["CALL", null, ["callee:00c5ef70:8"]]
- 00c548a8 bytes b2280094
+ 00c54cc8 bytes aa280094
- 00c548d8 ["INT_ADD", "register:40f0:8", ["const:c548d8:8", "const:4:8"]]
- 00c548d8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c54cf8 ["INT_ADD", "register:40f0:8", ["const:c54cf8:8", "const:4:8"]]
+ 00c54cf8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c548d8 bytes aa280094
+ 00c54cf8 bytes a2280094
- 00c54920 ["INT_ADD", "register:40f0:8", ["const:c54920:8", "const:4:8"]]
- 00c54920 ["CALL", null, ["callee:00c5ef60:8"]]
+ 00c54d40 ["INT_ADD", "register:40f0:8", ["const:c54d40:8", "const:4:8"]]
+ 00c54d40 ["CALL", null, ["callee:00c5ef60:8"]]
- 00c54920 bytes 90280094
+ 00c54d40 bytes 88280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fdf593adcf5e625e350012ca97ec9ac"></a>

### [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) → [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) FUN_00c54fd0

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c546d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md) · 呼出先 11件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md)
- 新版 呼出元 1件 [`00c54af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54af0.md) · 呼出先 11件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c553e8",
      "incomplete_value": true,
      "site": "00c553ec",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54fc8",
      "incomplete_value": true,
      "site": "00c54fcc",
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
            "const:130:8"
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
      "definition_site": "00c553d0",
      "incomplete_value": false,
      "site": "00c553ec",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54fb0",
      "incomplete_value": false,
      "site": "00c54fcc",
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
            "const:e44:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c553dc",
      "incomplete_value": false,
      "site": "00c553ec",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54fbc",
      "incomplete_value": false,
      "site": "00c54fcc",
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
            "const:cdb:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c553d0",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c553d4",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c553dc",
      "PARAM",
      [
        "storage",
        "002a1cdb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c553d0",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c553d4",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c553dc",
      "PARAM",
      [
        "storage",
        "002a1da8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md#insn-00c54fcc) · [`00c55000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md#insn-00c55000) · [`00c55034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md#insn-00c55034)
- 新版 `00c553ec`（命令位置の公開資料なし） · `00c55420`（命令位置の公開資料なし） · `00c55454`（命令位置の公開資料なし）

~~~diff
- 00c54fcc ["INT_ADD", "register:40f0:8", ["const:c54fcc:8", "const:4:8"]]
- 00c54fcc ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c553ec ["INT_ADD", "register:40f0:8", ["const:c553ec:8", "const:4:8"]]
+ 00c553ec ["CALL", null, ["callee:00c5ef40:8"]]
- 00c54fcc bytes dd260094
+ 00c553ec bytes d5260094
- 00c55000 ["INT_ADD", "register:40f0:8", ["const:c55000:8", "const:4:8"]]
- 00c55000 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c55420 ["INT_ADD", "register:40f0:8", ["const:c55420:8", "const:4:8"]]
+ 00c55420 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55000 bytes d0260094
+ 00c55420 bytes c8260094
- 00c55034 ["INT_ADD", "register:40f0:8", ["const:c55034:8", "const:4:8"]]
- 00c55034 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c55454 ["INT_ADD", "register:40f0:8", ["const:c55454:8", "const:4:8"]]
+ 00c55454 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55034 bytes c3260094
+ 00c55454 bytes bb260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47bd0fb8280057d2f6116dcd73439f64"></a>

### [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) → [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) FUN_00c55464

採用 · 移動量 `+0x420` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 8件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)
- 新版 呼出元 3件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) · 呼出先 8件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.10% / 新版 92.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55e44",
      "incomplete_value": true,
      "site": "00c55e48",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55a24",
      "incomplete_value": true,
      "site": "00c55a28",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55e38",
      "incomplete_value": false,
      "site": "00c55e48",
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
            "const:e89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55a18",
      "incomplete_value": false,
      "site": "00c55a28",
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
            "const:dbc:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55edc",
      "incomplete_value": true,
      "site": "00c55ee0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55abc",
      "incomplete_value": true,
      "site": "00c55ac0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c5553c",
      "DATA",
      [
        "storage",
        "00313dd0",
        "switchD_00c55124::switchdataD_00313dd0",
        "ushort"
      ]
    ],
    [
      "00c55d60",
      "PARAM",
      [
        "storage",
        "002bc319",
        null,
        "string"
      ]
    ],
    [
      "00c55d70",
      "PARAM",
      [
        "storage",
        "002b7e87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c5553c",
      "DATA",
      [
        "storage",
        "00313e10",
        "switchD_00c55544::switchdataD_00313e10",
        "ushort"
      ]
    ],
    [
      "00c55d60",
      "PARAM",
      [
        "storage",
        "002bc359",
        null,
        "string"
      ]
    ],
    [
      "00c55d70",
      "PARAM",
      [
        "storage",
        "002b7ec7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c55a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md#insn-00c55a28) · [`00c55ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md#insn-00c55ac0) · [`00c55b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md#insn-00c55b10)
- 新版 `00c55e48`（命令位置の公開資料なし） · `00c55ee0`（命令位置の公開資料なし） · `00c55f30`（命令位置の公開資料なし）

~~~diff
- 00c55a28 ["INT_ADD", "register:40f0:8", ["const:c55a28:8", "const:4:8"]]
- 00c55a28 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c55e48 ["INT_ADD", "register:40f0:8", ["const:c55e48:8", "const:4:8"]]
+ 00c55e48 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55a28 bytes 46240094
+ 00c55e48 bytes 3e240094
- 00c55ac0 ["INT_ADD", "register:40f0:8", ["const:c55ac0:8", "const:4:8"]]
- 00c55ac0 ["CALL", null, ["callee:00c5a1b0:8"]]
+ 00c55ee0 ["INT_ADD", "register:40f0:8", ["const:c55ee0:8", "const:4:8"]]
+ 00c55ee0 ["CALL", null, ["callee:00c5a1b0:8"]]
- 00c55ac0 bytes bc100094
+ 00c55ee0 bytes b4100094
- 00c55b10 ["INT_ADD", "register:40f0:8", ["const:c55b10:8", "const:4:8"]]
- 00c55b10 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c55f30 ["INT_ADD", "register:40f0:8", ["const:c55f30:8", "const:4:8"]]
+ 00c55f30 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55b10 bytes 0c240094
+ 00c55f30 bytes 04240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-980227b5d3c6bff73731eb12cdd04743"></a>

### [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) → [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) FUN_00c55fdc

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) · 呼出先 5件 [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) · 呼出先 5件 [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c560fc",
      "incomplete_value": true,
      "site": "00c56100",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55cdc",
      "incomplete_value": true,
      "site": "00c55ce0",
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
            "const:130:8"
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
      "definition_site": "00c560e4",
      "incomplete_value": false,
      "site": "00c56100",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55cc4",
      "incomplete_value": false,
      "site": "00c55ce0",
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
            "const:e44:8"
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
      "definition_site": "00c560f0",
      "incomplete_value": false,
      "site": "00c56100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55cd0",
      "incomplete_value": false,
      "site": "00c55ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:74a:8"
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
      "00c560e4",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c560e8",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c560f0",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c560e4",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c560e8",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c560f0",
      "PARAM",
      [
        "storage",
        "002af78a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c55ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md#insn-00c55ce0) · [`00c55cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md#insn-00c55cc4) · [`00c55cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md#insn-00c55cc8)
- 新版 `00c56100`（命令位置の公開資料なし） · `00c560e4`（命令位置の公開資料なし） · `00c560e8`（命令位置の公開資料なし）

~~~diff
- 00c55ce0 ["INT_ADD", "register:40f0:8", ["const:c55ce0:8", "const:4:8"]]
- 00c55ce0 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c56100 ["INT_ADD", "register:40f0:8", ["const:c56100:8", "const:4:8"]]
+ 00c56100 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55ce0 bytes 98230094
+ 00c56100 bytes 90230094
- 00c55cc4 ["COPY", "tmp:0:8", ["const:e44:8"]]
- 00c55cc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c55cc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c55cc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c560e4 ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 00c560e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c560e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c560e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c55cc4 bytes 21103991
+ 00c560e4 bytes 21443c91
- 00c55cc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
- 00c55cc8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c560e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
+ 00c560e8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c55cc8 bytes 73be43f9
+ 00c560e8 bytes 73be45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82a02d94a94e470e2bc45fd1017a781"></a>

### [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) → [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) FUN_00c56110

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) · 呼出先 5件 [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) · 呼出先 5件 [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c562d8",
      "incomplete_value": true,
      "site": "00c562dc",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55eb8",
      "incomplete_value": true,
      "site": "00c55ebc",
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
            "const:130:8"
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
      "definition_site": "00c562c0",
      "incomplete_value": false,
      "site": "00c562dc",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55ea0",
      "incomplete_value": false,
      "site": "00c55ebc",
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
            "const:e44:8"
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
      "definition_site": "00c562cc",
      "incomplete_value": false,
      "site": "00c562dc",
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
            "const:647:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55eac",
      "incomplete_value": false,
      "site": "00c55ebc",
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
            "const:607:8"
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
      "00c562c0",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c562c4",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c562cc",
      "PARAM",
      [
        "storage",
        "002ae607",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c562c0",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c562c4",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c562cc",
      "PARAM",
      [
        "storage",
        "002ae647",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c55ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md#insn-00c55ebc) · [`00c55ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md#insn-00c55ef0) · [`00c55d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md#insn-00c55d80)
- 新版 `00c562dc`（命令位置の公開資料なし） · `00c56310`（命令位置の公開資料なし） · `00c561a0`（命令位置の公開資料なし）

~~~diff
- 00c55ebc ["INT_ADD", "register:40f0:8", ["const:c55ebc:8", "const:4:8"]]
- 00c55ebc ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c562dc ["INT_ADD", "register:40f0:8", ["const:c562dc:8", "const:4:8"]]
+ 00c562dc ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55ebc bytes 21230094
+ 00c562dc bytes 19230094
- 00c55ef0 ["INT_ADD", "register:40f0:8", ["const:c55ef0:8", "const:4:8"]]
- 00c55ef0 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c56310 ["INT_ADD", "register:40f0:8", ["const:c56310:8", "const:4:8"]]
+ 00c56310 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c55ef0 bytes 14230094
+ 00c56310 bytes 0c230094
- 00c55d80 ["INT_ADD", "register:40f0:8", ["const:c55d80:8", "const:4:8"]]
- 00c55d80 ["CALL", null, ["callee:00c56874:8"]]
+ 00c561a0 ["INT_ADD", "register:40f0:8", ["const:c561a0:8", "const:4:8"]]
+ 00c561a0 ["CALL", null, ["callee:00c56874:8"]]
- 00c55d80 bytes b5010094
+ 00c561a0 bytes b5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de1d84f972da5e2ded6b91154bebb266"></a>

### [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) → [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) FUN_00c56320

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) · 呼出先 5件 [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) · 呼出先 5件 [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c56548",
      "incomplete_value": true,
      "site": "00c5654c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56128",
      "incomplete_value": true,
      "site": "00c5612c",
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
            "const:130:8"
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
      "definition_site": "00c56530",
      "incomplete_value": false,
      "site": "00c5654c",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56110",
      "incomplete_value": false,
      "site": "00c5612c",
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
            "const:e44:8"
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
      "definition_site": "00c5653c",
      "incomplete_value": false,
      "site": "00c5654c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:85f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5611c",
      "incomplete_value": false,
      "site": "00c5612c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:81f:8"
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
      "00c56530",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c56534",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c5653c",
      "PARAM",
      [
        "storage",
        "002b381f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c56530",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c56534",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c5653c",
      "PARAM",
      [
        "storage",
        "002b385f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5612c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md#insn-00c5612c) · [`00c56170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md#insn-00c56170) · [`00c561ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md#insn-00c561ac)
- 新版 `00c5654c`（命令位置の公開資料なし） · `00c56590`（命令位置の公開資料なし） · `00c565cc`（命令位置の公開資料なし）

~~~diff
- 00c5612c ["INT_ADD", "register:40f0:8", ["const:c5612c:8", "const:4:8"]]
- 00c5612c ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c5654c ["INT_ADD", "register:40f0:8", ["const:c5654c:8", "const:4:8"]]
+ 00c5654c ["CALL", null, ["callee:00c5ef40:8"]]
- 00c5612c bytes 85220094
+ 00c5654c bytes 7d220094
- 00c56170 ["INT_ADD", "register:40f0:8", ["const:c56170:8", "const:4:8"]]
- 00c56170 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c56590 ["INT_ADD", "register:40f0:8", ["const:c56590:8", "const:4:8"]]
+ 00c56590 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56170 bytes 74220094
+ 00c56590 bytes 6c220094
- 00c561ac ["INT_ADD", "register:40f0:8", ["const:c561ac:8", "const:4:8"]]
- 00c561ac ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c565cc ["INT_ADD", "register:40f0:8", ["const:c565cc:8", "const:4:8"]]
+ 00c565cc ["CALL", null, ["callee:00c5ef40:8"]]
- 00c561ac bytes 65220094
+ 00c565cc bytes 5d220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823e330027a515d98b5f4b213259c693"></a>

### [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) → [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) FUN_00c566ac

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5682c",
      "incomplete_value": true,
      "site": "00c56830",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5640c",
      "incomplete_value": true,
      "site": "00c56410",
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
            "const:130:8"
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
      "definition_site": "00c56814",
      "incomplete_value": false,
      "site": "00c56830",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c563f4",
      "incomplete_value": false,
      "site": "00c56410",
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
            "const:e44:8"
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
      "definition_site": "00c56820",
      "incomplete_value": false,
      "site": "00c56830",
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
            "const:3d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56400",
      "incomplete_value": false,
      "site": "00c56410",
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
            "const:2fd:8"
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
      "00c56814",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c56818",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c56820",
      "PARAM",
      [
        "storage",
        "002a62fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c56814",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c56818",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c56820",
      "PARAM",
      [
        "storage",
        "002a63d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c56410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md#insn-00c56410) · [`00c56444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md#insn-00c56444) · [`00c563f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md#insn-00c563f4)
- 新版 `00c56830`（命令位置の公開資料なし） · `00c56864`（命令位置の公開資料なし） · `00c56814`（命令位置の公開資料なし）

~~~diff
- 00c56410 ["INT_ADD", "register:40f0:8", ["const:c56410:8", "const:4:8"]]
- 00c56410 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c56830 ["INT_ADD", "register:40f0:8", ["const:c56830:8", "const:4:8"]]
+ 00c56830 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56410 bytes cc210094
+ 00c56830 bytes c4210094
- 00c56444 ["INT_ADD", "register:40f0:8", ["const:c56444:8", "const:4:8"]]
- 00c56444 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c56864 ["INT_ADD", "register:40f0:8", ["const:c56864:8", "const:4:8"]]
+ 00c56864 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56444 bytes bf210094
+ 00c56864 bytes b7210094
- 00c563f4 ["COPY", "tmp:0:8", ["const:e44:8"]]
- 00c563f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c563f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c563f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c56814 ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 00c56814 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c56814 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c56814 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c563f4 bytes 21103991
+ 00c56814 bytes 21443c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d54981e127f21425dd8a0d3f70ef15"></a>

### [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) → [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) FUN_00c56874

採用 · 移動量 `+0x420` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) · 呼出先 5件 [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 3件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) · 呼出先 5件 [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57044",
      "incomplete_value": true,
      "site": "00c57048",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56c24",
      "incomplete_value": true,
      "site": "00c56c28",
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
            "const:130:8"
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
      "definition_site": "00c5702c",
      "incomplete_value": false,
      "site": "00c57048",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56c0c",
      "incomplete_value": false,
      "site": "00c56c28",
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
            "const:e44:8"
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
      "definition_site": "00c57038",
      "incomplete_value": false,
      "site": "00c57048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:85f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56c18",
      "incomplete_value": false,
      "site": "00c56c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:81f:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c56920",
      "DATA",
      [
        "storage",
        "00313e30",
        "switchD_00c56508::switchdataD_00313e30",
        "ushort"
      ]
    ],
    [
      "00c5702c",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c57030",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c56920",
      "DATA",
      [
        "storage",
        "00313e70",
        "switchD_00c56928::switchdataD_00313e70",
        "ushort"
      ]
    ],
    [
      "00c5702c",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c57030",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c56c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md#insn-00c56c28) · [`00c56c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md#insn-00c56c5c) · [`00c56c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md#insn-00c56c90)
- 新版 `00c57048`（命令位置の公開資料なし） · `00c5707c`（命令位置の公開資料なし） · `00c570b0`（命令位置の公開資料なし）

~~~diff
- 00c56c28 ["INT_ADD", "register:40f0:8", ["const:c56c28:8", "const:4:8"]]
- 00c56c28 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c57048 ["INT_ADD", "register:40f0:8", ["const:c57048:8", "const:4:8"]]
+ 00c57048 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56c28 bytes c61f0094
+ 00c57048 bytes be1f0094
- 00c56c5c ["INT_ADD", "register:40f0:8", ["const:c56c5c:8", "const:4:8"]]
- 00c56c5c ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c5707c ["INT_ADD", "register:40f0:8", ["const:c5707c:8", "const:4:8"]]
+ 00c5707c ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56c5c bytes b91f0094
+ 00c5707c bytes b11f0094
- 00c56c90 ["INT_ADD", "register:40f0:8", ["const:c56c90:8", "const:4:8"]]
- 00c56c90 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c570b0 ["INT_ADD", "register:40f0:8", ["const:c570b0:8", "const:4:8"]]
+ 00c570b0 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c56c90 bytes ac1f0094
+ 00c570b0 bytes a41f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f7671608295f463159848a1d6035991"></a>

### [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) → [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) FUN_00c57238

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) · 呼出先 10件 [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) · 呼出先 10件 [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 5件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c574b0",
      "incomplete_value": true,
      "site": "00c574b0",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57090",
      "incomplete_value": true,
      "site": "00c57090",
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
            "const:4a8:8"
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
      "definition_site": "00c574b4",
      "incomplete_value": true,
      "site": "00c574b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57094",
      "incomplete_value": true,
      "site": "00c57094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "definition_site": "00c574d4",
      "incomplete_value": true,
      "site": "00c574d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c570b4",
      "incomplete_value": true,
      "site": "00c570b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c572bc",
      "PARAM",
      [
        "storage",
        "011288f4",
        null,
        null
      ]
    ],
    [
      "00c572cc",
      "READ",
      [
        "storage",
        "00ca44a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c572d0",
      "READ",
      [
        "storage",
        "00ca44b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c572bc",
      "PARAM",
      [
        "storage",
        "01128cf4",
        null,
        null
      ]
    ],
    [
      "00c572cc",
      "READ",
      [
        "storage",
        "00ca48a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c572d0",
      "READ",
      [
        "storage",
        "00ca48b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c56ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md#insn-00c56ea0) · [`00c56f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md#insn-00c56f2c) · [`00c56f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md#insn-00c56f64)
- 新版 `00c572c0`（命令位置の公開資料なし） · `00c5734c`（命令位置の公開資料なし） · `00c57384`（命令位置の公開資料なし）

~~~diff
- 00c56ea0 ["INT_ADD", "register:40f0:8", ["const:c56ea0:8", "const:4:8"]]
- 00c56ea0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c572c0 ["INT_ADD", "register:40f0:8", ["const:c572c0:8", "const:4:8"]]
+ 00c572c0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c56ea0 bytes 381f0094
+ 00c572c0 bytes 301f0094
- 00c56f2c ["INT_ADD", "register:40f0:8", ["const:c56f2c:8", "const:4:8"]]
- 00c56f2c ["CALL", null, ["callee:00c5ef60:8"]]
+ 00c5734c ["INT_ADD", "register:40f0:8", ["const:c5734c:8", "const:4:8"]]
+ 00c5734c ["CALL", null, ["callee:00c5ef60:8"]]
- 00c56f2c bytes 0d1f0094
+ 00c5734c bytes 051f0094
- 00c56f64 ["INT_ADD", "register:40f0:8", ["const:c56f64:8", "const:4:8"]]
- 00c56f64 ["CALL", null, ["callee:00c5ef60:8"]]
+ 00c57384 ["INT_ADD", "register:40f0:8", ["const:c57384:8", "const:4:8"]]
+ 00c57384 ["CALL", null, ["callee:00c5ef60:8"]]
- 00c56f64 bytes ff1e0094
+ 00c57384 bytes f71e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634bdf0eb3f0bcfaadd070e25fa34ff6"></a>

### [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) → [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md) FUN_00c5763c

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 呼出先 4件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 2件 [`00c5750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5750c.md) [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) · 呼出先 4件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57684",
      "incomplete_value": true,
      "site": "00c57688",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57264",
      "incomplete_value": true,
      "site": "00c57268",
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
            "const:130:8"
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
      "definition_site": "00c57678",
      "incomplete_value": false,
      "site": "00c57688",
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
            "const:b31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57258",
      "incomplete_value": false,
      "site": "00c57268",
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
            "const:af1:8"
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
      "definition_site": "00c57708",
      "incomplete_value": true,
      "site": "00c5770c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c572e8",
      "incomplete_value": true,
      "site": "00c572ec",
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
            "const:130:8"
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
      "00c57678",
      "PARAM",
      [
        "storage",
        "002b4af1",
        null,
        "string"
      ]
    ],
    [
      "00c5767c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c576f8",
      "PARAM",
      [
        "storage",
        "002a8948",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57678",
      "PARAM",
      [
        "storage",
        "002b4b31",
        null,
        "string"
      ]
    ],
    [
      "00c5767c",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c576f8",
      "PARAM",
      [
        "storage",
        "002a8a15",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md#insn-00c57268) · [`00c572ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md#insn-00c572ec) · [`00c57258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md#insn-00c57258)
- 新版 `00c57688`（命令位置の公開資料なし） · `00c5770c`（命令位置の公開資料なし） · `00c57678`（命令位置の公開資料なし）

~~~diff
- 00c57268 ["INT_ADD", "register:40f0:8", ["const:c57268:8", "const:4:8"]]
- 00c57268 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c57688 ["INT_ADD", "register:40f0:8", ["const:c57688:8", "const:4:8"]]
+ 00c57688 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c57268 bytes 361e0094
+ 00c57688 bytes 2e1e0094
- 00c572ec ["INT_ADD", "register:40f0:8", ["const:c572ec:8", "const:4:8"]]
- 00c572ec ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c5770c ["INT_ADD", "register:40f0:8", ["const:c5770c:8", "const:4:8"]]
+ 00c5770c ["CALL", null, ["callee:00c5ef40:8"]]
- 00c572ec bytes 151e0094
+ 00c5770c bytes 0d1e0094
- 00c57258 ["COPY", "tmp:0:8", ["const:af1:8"]]
- 00c57258 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c57258 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c57258 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c57678 ["COPY", "tmp:0:8", ["const:b31:8"]]
+ 00c57678 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57678 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57678 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c57258 bytes 21c42b91
+ 00c57678 bytes 21c42c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a850c12486c6bb5a8ba25cd08b5ae3bc"></a>

### [`00c5766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md) → [`00c57a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md) FUN_00c57a8c

採用 · 移動量 `+0x420` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.13% / 新版 84.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57b34",
      "incomplete_value": true,
      "site": "00c57b38",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57714",
      "incomplete_value": true,
      "site": "00c57718",
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
            "const:130:8"
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
      "definition_site": "00c57b1c",
      "incomplete_value": false,
      "site": "00c57b38",
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
            "const:f11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c576fc",
      "incomplete_value": false,
      "site": "00c57718",
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
            "const:e44:8"
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
      "definition_site": "00c57b28",
      "incomplete_value": false,
      "site": "00c57b38",
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
            "const:a35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57708",
      "incomplete_value": false,
      "site": "00c57718",
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
            "const:968:8"
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
      "00c57b1c",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c57b20",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c57b28",
      "PARAM",
      [
        "storage",
        "002a9968",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57b1c",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c57b20",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c57b28",
      "PARAM",
      [
        "storage",
        "002a9a35",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md#insn-00c57718) · [`00c57758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md#insn-00c57758) · [`00c576fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md#insn-00c576fc)
- 新版 `00c57b38`（命令位置の公開資料なし） · `00c57b78`（命令位置の公開資料なし） · `00c57b1c`（命令位置の公開資料なし）

~~~diff
- 00c57718 ["INT_ADD", "register:40f0:8", ["const:c57718:8", "const:4:8"]]
- 00c57718 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c57b38 ["INT_ADD", "register:40f0:8", ["const:c57b38:8", "const:4:8"]]
+ 00c57b38 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c57718 bytes 0a1d0094
+ 00c57b38 bytes 021d0094
- 00c57758 ["INT_ADD", "register:40f0:8", ["const:c57758:8", "const:4:8"]]
- 00c57758 ["CALL", null, ["callee:00c5ef40:8"]]
+ 00c57b78 ["INT_ADD", "register:40f0:8", ["const:c57b78:8", "const:4:8"]]
+ 00c57b78 ["CALL", null, ["callee:00c5ef40:8"]]
- 00c57758 bytes fa1c0094
+ 00c57b78 bytes f21c0094
- 00c576fc ["COPY", "tmp:0:8", ["const:e44:8"]]
- 00c576fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c576fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c576fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c57b1c ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 00c57b1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57b1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57b1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c576fc bytes 21103991
+ 00c57b1c bytes 21443c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4034e4183d3c3994ff88c081aeb7dec5"></a>

### [`00c578ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md) → [`00c57cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cf4.md) _Znwm

採用 · 移動量 `+0x408` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57d54",
      "incomplete_value": true,
      "site": "00c57d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5794c",
      "incomplete_value": true,
      "site": "00c57954",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
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
      "definition_site": "00c57d58",
      "incomplete_value": true,
      "site": "00c57d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57950",
      "incomplete_value": true,
      "site": "00c57954",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c57d54",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57d54",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57d58",
      "READ",
      [
        "storage",
        "00c9a9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c57d54",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57d54",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57d58",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md#insn-00c57954) · [`00c57908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md#insn-00c57908) · [`00c57910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c578ec.md#insn-00c57910)
- 新版 `00c57d5c`（命令位置の公開資料なし） · `00c57d10`（命令位置の公開資料なし） · `00c57d18`（命令位置の公開資料なし）

~~~diff
- 00c57954 ["INT_ADD", "register:40f0:8", ["const:c57954:8", "const:4:8"]]
- 00c57954 ["CALL", null, ["callee:00c57f10:8"]]
+ 00c57d5c ["INT_ADD", "register:40f0:8", ["const:c57d5c:8", "const:4:8"]]
+ 00c57d5c ["CALL", null, ["callee:00c57f10:8"]]
- 00c57954 bytes 6f000094
+ 00c57d5c bytes 6d000094
- 00c57908 ["INT_ADD", "register:40f0:8", ["const:c57908:8", "const:4:8"]]
- 00c57908 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c57d10 ["INT_ADD", "register:40f0:8", ["const:c57d10:8", "const:4:8"]]
+ 00c57d10 ["CALL", null, ["callee:00c5a020:8"]]
- 00c57908 bytes c6080094
+ 00c57d10 bytes c4080094
- 00c57910 ["INT_ADD", "register:40f0:8", ["const:c57910:8", "const:4:8"]]
- 00c57910 ["CALL", null, ["callee:00c5ede0:8"]]
+ 00c57d18 ["INT_ADD", "register:40f0:8", ["const:c57d18:8", "const:4:8"]]
+ 00c57d18 ["CALL", null, ["callee:00c5ede0:8"]]
- 00c57910 bytes 341c0094
+ 00c57d18 bytes 321c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aee956bdc795a44242bf63a510e3e99c"></a>

### [`00c57960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57960.md) → [`00c57d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57d68.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0x408` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5eac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eac0.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md) [`00c5e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9e0.md)
- 新版 呼出元 1件 [`00c5eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eec0.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md) [`00c5ede0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ede0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57dec",
      "incomplete_value": true,
      "site": "00c57df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c579e4",
      "incomplete_value": true,
      "site": "00c579ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
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
      "definition_site": "00c57df0",
      "incomplete_value": true,
      "site": "00c57df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c579e8",
      "incomplete_value": true,
      "site": "00c579ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c57dec",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57dec",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57df0",
      "READ",
      [
        "storage",
        "00c9a9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c57dec",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57dec",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57df0",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c579ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57960.md#insn-00c579ec) · [`00c57998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57960.md#insn-00c57998) · [`00c579a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57960.md#insn-00c579a4)
- 新版 `00c57df4`（命令位置の公開資料なし） · `00c57da0`（命令位置の公開資料なし） · `00c57dac`（命令位置の公開資料なし）

~~~diff
- 00c579ec ["INT_ADD", "register:40f0:8", ["const:c579ec:8", "const:4:8"]]
- 00c579ec ["CALL", null, ["callee:00c57f10:8"]]
+ 00c57df4 ["INT_ADD", "register:40f0:8", ["const:c57df4:8", "const:4:8"]]
+ 00c57df4 ["CALL", null, ["callee:00c57f10:8"]]
- 00c579ec bytes 49000094
+ 00c57df4 bytes 47000094
- 00c57998 ["INT_ADD", "register:40f0:8", ["const:c57998:8", "const:4:8"]]
- 00c57998 ["CALL", null, ["callee:00c5eed0:8"]]
+ 00c57da0 ["INT_ADD", "register:40f0:8", ["const:c57da0:8", "const:4:8"]]
+ 00c57da0 ["CALL", null, ["callee:00c5eed0:8"]]
- 00c57998 bytes 4e1c0094
+ 00c57da0 bytes 4c1c0094
- 00c579a4 ["INT_ADD", "register:40f0:8", ["const:c579a4:8", "const:4:8"]]
- 00c579a4 ["CALL", null, ["callee:00c5ede0:8"]]
+ 00c57dac ["INT_ADD", "register:40f0:8", ["const:c57dac:8", "const:4:8"]]
+ 00c57dac ["CALL", null, ["callee:00c5ede0:8"]]
- 00c579a4 bytes 0f1c0094
+ 00c57dac bytes 0d1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

