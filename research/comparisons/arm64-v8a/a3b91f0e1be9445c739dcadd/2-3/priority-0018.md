# v15.7.4 → v16.0.0 · 最優先の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-9ff6aaef49517f6c33f5960a905e0e43"></a>

### [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) → [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) FUN_0057facc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005323c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323c0.md) [`0055ce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ce48.md) [`0055ced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md) [`0055cf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md) [`0055d024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d024.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 6件 [`00555258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555258.md) [`0057fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md) [`0057fd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md) [`0057fe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md) [`0057febc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md) · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fb30",
      "incomplete_value": true,
      "site": "0057fb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc98",
      "incomplete_value": true,
      "site": "0055cc98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dd:8"
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
      "definition_site": "0057fb38",
      "incomplete_value": true,
      "site": "0057fb38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055cca0",
      "incomplete_value": true,
      "site": "0055cca0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fb34",
      "incomplete_value": true,
      "site": "0057fb48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc9c",
      "incomplete_value": true,
      "site": "0055ccb0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:bdc:8"
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
      "0057fb18",
      "READ",
      [
        "storage",
        "002a25dd",
        null,
        "string"
      ]
    ],
    [
      "0057fb20",
      "READ",
      [
        "storage",
        "002a25e2",
        null,
        "string"
      ]
    ],
    [
      "0057fb34",
      "READ",
      [
        "storage",
        "00291bdc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fb18",
      "READ",
      [
        "storage",
        "002b2c9e",
        null,
        "string"
      ]
    ],
    [
      "0057fb20",
      "READ",
      [
        "storage",
        "002b2ca3",
        null,
        "string"
      ]
    ],
    [
      "0057fb34",
      "READ",
      [
        "storage",
        "002a11f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md#insn-0055cc68) · [`0055cc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md#insn-0055cc70) · [`0055cc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md#insn-0055cc78)
- 新版 `0057fb00`（命令位置の公開資料なし） · `0057fb08`（命令位置の公開資料なし） · `0057fb10`（命令位置の公開資料なし）

~~~diff
- 0055cc68 ["INT_ADD", "register:40f0:8", ["const:55cc68:8", "const:4:8"]]
- 0055cc68 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057fb00 ["INT_ADD", "register:40f0:8", ["const:57fb00:8", "const:4:8"]]
+ 0057fb00 ["CALL", null, ["callee:00588e2c:8"]]
- 0055cc68 bytes cb240094
+ 0057fb00 bytes cb240094
- 0055cc70 ["INT_ADD", "register:40f0:8", ["const:55cc70:8", "const:4:8"]]
- 0055cc70 ["CALL", null, ["callee:0058911c:8"]]
+ 0057fb08 ["INT_ADD", "register:40f0:8", ["const:57fb08:8", "const:4:8"]]
+ 0057fb08 ["CALL", null, ["callee:0058911c:8"]]
- 0055cc70 bytes 85250094
+ 0057fb08 bytes 85250094
- 0055cc78 ["COPY", "register:4048:8", ["const:2a2000:8"]]
+ 0057fb10 ["COPY", "register:4048:8", ["const:2b2000:8"]]
- 0055cc78 bytes 29eaffd0
+ 0057fb10 bytes 89e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8279a1d6f3de157a733a5788ccd222f"></a>

### [`0055ced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md) → [`0057fd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md) FUN_0057fd68

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323c8.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00555260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555260.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fda4",
      "incomplete_value": true,
      "site": "0057fda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cf0c",
      "incomplete_value": true,
      "site": "0055cf0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:75d:8"
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
      "0057fd88",
      "READ",
      [
        "storage",
        "0029c75d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fd88",
      "READ",
      [
        "storage",
        "002ac8f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md#insn-0055cee4) · [`0055cee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md#insn-0055cee8) · [`0055cf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055ced0.md#insn-0055cf18)
- 新版 `0057fd7c`（命令位置の公開資料なし） · `0057fd80`（命令位置の公開資料なし） · `0057fdb0`（命令位置の公開資料なし）

~~~diff
- 0055cee4 ["COPY", "register:4058:8", ["const:29c000:8"]]
+ 0057fd7c ["COPY", "register:4058:8", ["const:2ac000:8"]]
- 0055cee4 bytes 0beaff90
+ 0057fd7c bytes 6be9ffb0
- 0055cee8 ["COPY", "tmp:0:8", ["const:75d:8"]]
- 0055cee8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0057fd80 ["COPY", "tmp:0:8", ["const:8f6:8"]]
+ 0057fd80 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fd80 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fd80 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 bytes 6b751d91
+ 0057fd80 bytes 6bd92391
- 0055cf18 ["INT_ADD", "register:40f0:8", ["const:55cf18:8", "const:4:8"]]
- 0055cf18 ["CALL", null, ["callee:0057facc:8"]]
+ 0057fdb0 ["INT_ADD", "register:40f0:8", ["const:57fdb0:8", "const:4:8"]]
+ 0057fdb0 ["CALL", null, ["callee:0057facc:8"]]
- 0055cf18 bytes 47ffff97
+ 0057fdb0 bytes 47ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af7ed1c4760aaff2c0efdbca8f6eea6e"></a>

### [`0055cf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md) → [`0057fe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md) FUN_0057fe14

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323cc.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00555264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555264.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fe48",
      "incomplete_value": true,
      "site": "0057fe48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
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
    "old": {
      "definition_site": "0055cfb0",
      "incomplete_value": true,
      "site": "0055cfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76d:8"
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
      "definition_site": "0057fe4c",
      "incomplete_value": true,
      "site": "0057fe4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055cfb4",
      "incomplete_value": true,
      "site": "0055cfb4",
      "value": [
        "LOAD",
        "8",
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
      "0057fe34",
      "READ",
      [
        "storage",
        "002a976d",
        null,
        "string"
      ]
    ],
    [
      "0057fe40",
      "READ",
      [
        "storage",
        "002a9773",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fe34",
      "READ",
      [
        "storage",
        "002ba410",
        null,
        "string"
      ]
    ],
    [
      "0057fe40",
      "READ",
      [
        "storage",
        "002ba416",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md#insn-0055cf90) · [`0055cf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md#insn-0055cf94) · [`0055cfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cf7c.md#insn-0055cfc0)
- 新版 `0057fe28`（命令位置の公開資料なし） · `0057fe2c`（命令位置の公開資料なし） · `0057fe58`（命令位置の公開資料なし）

~~~diff
- 0055cf90 ["COPY", "register:4050:8", ["const:2a9000:8"]]
+ 0057fe28 ["COPY", "register:4050:8", ["const:2ba000:8"]]
- 0055cf90 bytes 6aeaffb0
+ 0057fe28 bytes cae9fff0
- 0055cf94 ["COPY", "tmp:0:8", ["const:76d:8"]]
- 0055cf94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057fe2c ["COPY", "tmp:0:8", ["const:410:8"]]
+ 0057fe2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fe2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fe2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 bytes 4ab51d91
+ 0057fe2c bytes 4a411091
- 0055cfc0 ["INT_ADD", "register:40f0:8", ["const:55cfc0:8", "const:4:8"]]
- 0055cfc0 ["CALL", null, ["callee:0057facc:8"]]
+ 0057fe58 ["INT_ADD", "register:40f0:8", ["const:57fe58:8", "const:4:8"]]
+ 0057fe58 ["CALL", null, ["callee:0057facc:8"]]
- 0055cfc0 bytes 1dffff97
+ 0057fe58 bytes 1dffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2345b6d3ac08309e9f296977ebef745"></a>

### [`0055d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md) → [`0057ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057ff60.md) FUN_0057ff60

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323d4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055cc34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0055526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/0055526c.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ff94",
      "incomplete_value": true,
      "site": "0057ff94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d0fc",
      "incomplete_value": true,
      "site": "0055d0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ce:8"
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
      "definition_site": "0057ff98",
      "incomplete_value": true,
      "site": "0057ff98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055d100",
      "incomplete_value": true,
      "site": "0055d100",
      "value": [
        "LOAD",
        "8",
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
      "0057ff80",
      "READ",
      [
        "storage",
        "0029f6ce",
        null,
        "string"
      ]
    ],
    [
      "0057ff8c",
      "READ",
      [
        "storage",
        "0029f6d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ff80",
      "READ",
      [
        "storage",
        "002afae1",
        null,
        "string"
      ]
    ],
    [
      "0057ff8c",
      "READ",
      [
        "storage",
        "002afae6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md#insn-0055d0dc) · [`0055d0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md#insn-0055d0e0) · [`0055d10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d0c8.md#insn-0055d10c)
- 新版 `0057ff74`（命令位置の公開資料なし） · `0057ff78`（命令位置の公開資料なし） · `0057ffa4`（命令位置の公開資料なし）

~~~diff
- 0055d0dc ["COPY", "register:4050:8", ["const:29f000:8"]]
+ 0057ff74 ["COPY", "register:4050:8", ["const:2af000:8"]]
- 0055d0dc bytes 0aeaffd0
+ 0057ff74 bytes 8ae9ff90
- 0055d0e0 ["COPY", "tmp:0:8", ["const:6ce:8"]]
- 0055d0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057ff78 ["COPY", "tmp:0:8", ["const:ae1:8"]]
+ 0057ff78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057ff78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057ff78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 bytes 4a391b91
+ 0057ff78 bytes 4a852b91
- 0055d10c ["INT_ADD", "register:40f0:8", ["const:55d10c:8", "const:4:8"]]
- 0055d10c ["CALL", null, ["callee:0057facc:8"]]
+ 0057ffa4 ["INT_ADD", "register:40f0:8", ["const:57ffa4:8", "const:4:8"]]
+ 0057ffa4 ["CALL", null, ["callee:0057facc:8"]]
- 0055d10c bytes cafeff97
+ 0057ffa4 bytes cafeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b292188ce5d1230d0f4ba6c13ce4f10"></a>

### [`0055d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md) → [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) FUN_00580058

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005397f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397f8.md) · 呼出先 17件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`005397fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539804.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`0055c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c690.md) · 呼出先 17件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`0055c694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c694.md) [`0055c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c69c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.14% / 新版 94.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005800c0",
      "incomplete_value": true,
      "site": "005800c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d228",
      "incomplete_value": true,
      "site": "0055d228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5eb:8"
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
      "definition_site": "005800dc",
      "incomplete_value": true,
      "site": "005800e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d244",
      "incomplete_value": true,
      "site": "0055d24c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
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
      "definition_site": "005800d8",
      "incomplete_value": true,
      "site": "005800e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:606:8"
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
      "005800ac",
      "READ",
      [
        "storage",
        "002a25eb",
        null,
        "string"
      ]
    ],
    [
      "005800d8",
      "READ",
      [
        "storage",
        "0029d606",
        null,
        "string"
      ]
    ],
    [
      "005800d8",
      "READ",
      [
        "storage",
        "0029d616",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005800ac",
      "READ",
      [
        "storage",
        "002b2cac",
        null,
        "string"
      ]
    ],
    [
      "005800d8",
      "READ",
      [
        "storage",
        "002ad890",
        null,
        "string"
      ]
    ],
    [
      "005800d8",
      "READ",
      [
        "storage",
        "002ad8a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md#insn-0055d1f4) · [`0055d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md#insn-0055d1fc) · [`0055d204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md#insn-0055d204)
- 新版 `0058008c`（命令位置の公開資料なし） · `00580094`（命令位置の公開資料なし） · `0058009c`（命令位置の公開資料なし）

~~~diff
- 0055d1f4 ["INT_ADD", "register:40f0:8", ["const:55d1f4:8", "const:4:8"]]
- 0055d1f4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058008c ["INT_ADD", "register:40f0:8", ["const:58008c:8", "const:4:8"]]
+ 0058008c ["CALL", null, ["callee:00588e2c:8"]]
- 0055d1f4 bytes 68230094
+ 0058008c bytes 68230094
- 0055d1fc ["INT_ADD", "register:40f0:8", ["const:55d1fc:8", "const:4:8"]]
- 0055d1fc ["CALL", null, ["callee:0058911c:8"]]
+ 00580094 ["INT_ADD", "register:40f0:8", ["const:580094:8", "const:4:8"]]
+ 00580094 ["CALL", null, ["callee:0058911c:8"]]
- 0055d1fc bytes 22240094
+ 00580094 bytes 22240094
- 0055d204 ["COPY", "register:4048:8", ["const:2a2000:8"]]
+ 0058009c ["COPY", "register:4048:8", ["const:2b2000:8"]]
- 0055d204 bytes 29eaffb0
+ 0058009c bytes 89e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fabf17229a22f9a1a0f814dbcffc5856"></a>

### [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) → [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) FUN_00580464

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00539948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539948.md) · 呼出先 20件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) [`0055af10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af10.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0055c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e0.md) · 呼出先 20件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) [`0057dda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005804b8",
      "incomplete_value": true,
      "site": "005804b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d620",
      "incomplete_value": true,
      "site": "0055d620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1e:8"
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
      "definition_site": "005804d8",
      "incomplete_value": true,
      "site": "005804e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:160:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d640",
      "incomplete_value": true,
      "site": "0055d648",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
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
      "definition_site": "005804d4",
      "incomplete_value": true,
      "site": "005804e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4d:8"
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
      "005804a8",
      "READ",
      [
        "storage",
        "002aca1e",
        null,
        "string"
      ]
    ],
    [
      "005804d4",
      "READ",
      [
        "storage",
        "00297c4d",
        null,
        "string"
      ]
    ],
    [
      "005804d4",
      "READ",
      [
        "storage",
        "00297c5d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005804a8",
      "READ",
      [
        "storage",
        "002bda96",
        null,
        "string"
      ]
    ],
    [
      "005804d4",
      "READ",
      [
        "storage",
        "002a78a6",
        null,
        "string"
      ]
    ],
    [
      "005804d4",
      "READ",
      [
        "storage",
        "002a78b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md#insn-0055d6c4) · [`0055d5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md#insn-0055d5f8) · [`0055d600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md#insn-0055d600)
- 新版 `0058055c`（命令位置の公開資料なし） · `00580490`（命令位置の公開資料なし） · `00580498`（命令位置の公開資料なし）

~~~diff
- 0055d6c4 ["INT_ADD", "register:40f0:8", ["const:55d6c4:8", "const:4:8"]]
- 0055d6c4 ["CALL", null, ["callee:00c58210:8"]]
+ 0058055c ["INT_ADD", "register:40f0:8", ["const:58055c:8", "const:4:8"]]
+ 0058055c ["CALL", null, ["callee:00c58210:8"]]
- 0055d6c4 bytes 3ff81994
+ 0058055c bytes 2d5f1b94
- 0055d5f8 ["INT_ADD", "register:40f0:8", ["const:55d5f8:8", "const:4:8"]]
- 0055d5f8 ["CALL", null, ["callee:00588e2c:8"]]
+ 00580490 ["INT_ADD", "register:40f0:8", ["const:580490:8", "const:4:8"]]
+ 00580490 ["CALL", null, ["callee:00588e2c:8"]]
- 0055d5f8 bytes 67220094
+ 00580490 bytes 67220094
- 0055d600 ["INT_ADD", "register:40f0:8", ["const:55d600:8", "const:4:8"]]
- 0055d600 ["CALL", null, ["callee:0058911c:8"]]
+ 00580498 ["INT_ADD", "register:40f0:8", ["const:580498:8", "const:4:8"]]
+ 00580498 ["CALL", null, ["callee:0058911c:8"]]
- 0055d600 bytes 21230094
+ 00580498 bytes 21230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d86f45638687a8609269eb56aa6cc82"></a>

### [`0055d9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md) → [`00580848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md) FUN_00580848

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053d57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d57c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00560414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560414.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005808bc",
      "incomplete_value": true,
      "site": "005808cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:149:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055da24",
      "incomplete_value": true,
      "site": "0055da34",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:290000:8"
              ],
              [
                "leaf",
                "const:c07:8"
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
      "definition_site": "005808c0",
      "incomplete_value": true,
      "site": "005808d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055da28",
      "incomplete_value": true,
      "site": "0055da38",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005808c4",
      "incomplete_value": true,
      "site": "005808d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0055da2c",
      "incomplete_value": true,
      "site": "0055da3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c60:8"
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
      "00580890",
      "READ",
      [
        "storage",
        "002afcfc",
        null,
        "string"
      ]
    ],
    [
      "005808bc",
      "READ",
      [
        "storage",
        "00290c07",
        null,
        "string"
      ]
    ],
    [
      "005808c0",
      "READ",
      [
        "storage",
        "00290c17",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580890",
      "READ",
      [
        "storage",
        "002c128c",
        null,
        "string"
      ]
    ],
    [
      "005808bc",
      "READ",
      [
        "storage",
        "002a0149",
        null,
        "string"
      ]
    ],
    [
      "005808c0",
      "READ",
      [
        "storage",
        "002a0159",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md#insn-0055d9dc) · [`0055d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md#insn-0055d9e4) · [`0055d9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md#insn-0055d9ec)
- 新版 `00580874`（命令位置の公開資料なし） · `0058087c`（命令位置の公開資料なし） · `00580884`（命令位置の公開資料なし）

~~~diff
- 0055d9dc ["INT_ADD", "register:40f0:8", ["const:55d9dc:8", "const:4:8"]]
- 0055d9dc ["CALL", null, ["callee:00588e2c:8"]]
+ 00580874 ["INT_ADD", "register:40f0:8", ["const:580874:8", "const:4:8"]]
+ 00580874 ["CALL", null, ["callee:00588e2c:8"]]
- 0055d9dc bytes 6e210094
+ 00580874 bytes 6e210094
- 0055d9e4 ["INT_ADD", "register:40f0:8", ["const:55d9e4:8", "const:4:8"]]
- 0055d9e4 ["CALL", null, ["callee:0058911c:8"]]
+ 0058087c ["INT_ADD", "register:40f0:8", ["const:58087c:8", "const:4:8"]]
+ 0058087c ["CALL", null, ["callee:0058911c:8"]]
- 0055d9e4 bytes 28220094
+ 0058087c bytes 28220094
- 0055d9ec ["COPY", "register:4048:8", ["const:2af000:8"]]
+ 00580884 ["COPY", "register:4048:8", ["const:2c1000:8"]]
- 0055d9ec bytes 89eaffd0
+ 00580884 bytes 09eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d260b2407f399ed7f996a6ae40b8975e"></a>

### [`0055dc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md) → [`00580af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md) FUN_00580af0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053d584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d584.md) · 呼出先 8件 [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0056041c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056041c.md) · 呼出先 8件 [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580b54",
      "incomplete_value": false,
      "site": "00580b60",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dcbc",
      "incomplete_value": false,
      "site": "0055dcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "00580b60",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00580b60",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055dca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md#insn-0055dca8) · [`0055dcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md#insn-0055dcb0) · [`0055dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md#insn-0055dcb8)
- 新版 `00580b40`（命令位置の公開資料なし） · `00580b48`（命令位置の公開資料なし） · `00580b50`（命令位置の公開資料なし）

~~~diff
- 0055dca8 ["INT_ADD", "register:40f0:8", ["const:55dca8:8", "const:4:8"]]
- 0055dca8 ["CALL", null, ["callee:00c58d60:8"]]
+ 00580b40 ["INT_ADD", "register:40f0:8", ["const:580b40:8", "const:4:8"]]
+ 00580b40 ["CALL", null, ["callee:00c58d60:8"]]
- 0055dca8 bytes 9af91994
+ 00580b40 bytes 88601b94
- 0055dcb0 ["INT_ADD", "register:40f0:8", ["const:55dcb0:8", "const:4:8"]]
- 0055dcb0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00580b48 ["INT_ADD", "register:40f0:8", ["const:580b48:8", "const:4:8"]]
+ 00580b48 ["CALL", null, ["callee:00c57a90:8"]]
- 0055dcb0 bytes e4f41994
+ 00580b48 bytes d25b1b94
- 0055dcb8 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00580b50 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055dcb8 bytes 883400d0
+ 00580b50 bytes 483700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa8b1b24b044e31b3c88d10458adf17"></a>

### [`0055ddc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md) → [`00580c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md) FUN_00580c60

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bda8.md) · 呼出先 9件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0055ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec40.md) · 呼出先 9件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00536e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536e48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580d20",
      "incomplete_value": true,
      "site": "00580d20",
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
      "definition_site": "0055de88",
      "incomplete_value": true,
      "site": "0055de88",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580d74",
      "incomplete_value": false,
      "site": "00580d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dedc",
      "incomplete_value": false,
      "site": "0055dee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00580d8c",
      "incomplete_value": false,
      "site": "00580d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055def4",
      "incomplete_value": false,
      "site": "0055def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00580d08",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "00580d20",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580d7c",
      "DATA",
      [
        "storage",
        "00bef5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580d08",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00580d20",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580d7c",
      "DATA",
      [
        "storage",
        "00c6c160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md#insn-0055de48) · [`0055de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md#insn-0055de60) · [`0055de64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055ddc8.md#insn-0055de64)
- 新版 `00580ce0`（命令位置の公開資料なし） · `00580cf8`（命令位置の公開資料なし） · `00580cfc`（命令位置の公開資料なし）

~~~diff
- 0055de48 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055de48 ["INT_ADD", "register:40f0:8", ["const:55de48:8", "const:4:8"]]
- 0055de48 ["CALLIND", null, ["register:0:8"]]
+ 00580ce0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580ce0 ["INT_ADD", "register:40f0:8", ["const:580ce0:8", "const:4:8"]]
+ 00580ce0 ["CALLIND", null, ["register:0:8"]]
- 0055de48 bytes 20013fd6
+ 00580ce0 bytes 20013fd6
- 0055de60 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055de60 ["INT_ADD", "register:40f0:8", ["const:55de60:8", "const:4:8"]]
- 0055de60 ["CALLIND", null, ["register:0:8"]]
+ 00580cf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580cf8 ["INT_ADD", "register:40f0:8", ["const:580cf8:8", "const:4:8"]]
+ 00580cf8 ["CALLIND", null, ["register:0:8"]]
- 0055de60 bytes 20013fd6
+ 00580cf8 bytes 20013fd6
- 0055de64 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00580cfc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0055de64 bytes e83500b0
+ 00580cfc bytes c83800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4528d04210ea6630f976d6b40b20b3db"></a>

### [`0055e170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md) → [`00581008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581008.md) FUN_00581008

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053bdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdac.md) · 呼出先 12件 [`00574734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574734.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0055ec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec44.md) · 呼出先 12件 [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005810a8",
      "incomplete_value": true,
      "site": "005810a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a53:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e210",
      "incomplete_value": true,
      "site": "0055e210",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:6ce:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00581044",
      "incomplete_value": false,
      "site": "00581054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1ac",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "0058104c",
      "incomplete_value": false,
      "site": "00581054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1b4",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00581044",
      "PARAM",
      [
        "storage",
        "00bef608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0058104c",
      "PARAM",
      [
        "storage",
        "00bef6a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581088",
      "READ",
      [
        "storage",
        "0029e6ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581044",
      "PARAM",
      [
        "storage",
        "00c6c1c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0058104c",
      "PARAM",
      [
        "storage",
        "00c6c268",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581088",
      "READ",
      [
        "storage",
        "002aea53",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1bc) · [`0055e1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1a8) · [`0055e1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e170.md#insn-0055e1ac)
- 新版 `00581054`（命令位置の公開資料なし） · `00581040`（命令位置の公開資料なし） · `00581044`（命令位置の公開資料なし）

~~~diff
- 0055e1bc ["INT_ADD", "register:40f0:8", ["const:55e1bc:8", "const:4:8"]]
- 0055e1bc ["CALL", null, ["callee:00c58210:8"]]
+ 00581054 ["INT_ADD", "register:40f0:8", ["const:581054:8", "const:4:8"]]
+ 00581054 ["CALL", null, ["callee:00c58210:8"]]
- 0055e1bc bytes 81f51994
+ 00581054 bytes 6f5c1b94
- 0055e1a8 ["COPY", "register:4008:8", ["const:bef000:8"]]
+ 00581040 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0055e1a8 bytes 813400b0
+ 00581040 bytes 413700f0
- 0055e1ac ["COPY", "tmp:0:8", ["const:608:8"]]
- 0055e1ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00581044 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00581044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00581044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00581044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac bytes 21201891
+ 00581044 bytes 21200791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d22c179d5de43ceb3ca3a926e2e8f7"></a>

### [`0055e3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md) → [`0058123c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/0058123c.md) FUN_0058123c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bdb0.md) · 呼出先 10件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0055ec48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec48.md) · 呼出先 10件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005812c8",
      "incomplete_value": true,
      "site": "005812d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e430",
      "incomplete_value": true,
      "site": "0055e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6dc:8"
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
      "definition_site": "005812cc",
      "incomplete_value": true,
      "site": "005812dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055e434",
      "incomplete_value": true,
      "site": "0055e444",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005812d0",
      "incomplete_value": true,
      "site": "005812e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0055e438",
      "incomplete_value": true,
      "site": "0055e448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c60:8"
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
      "00581278",
      "PARAM",
      [
        "storage",
        "00bef608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581280",
      "PARAM",
      [
        "storage",
        "00bef618",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005812c8",
      "READ",
      [
        "storage",
        "0029f6dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581278",
      "PARAM",
      [
        "storage",
        "00c6c1c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581280",
      "PARAM",
      [
        "storage",
        "00c6c1d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005812c8",
      "READ",
      [
        "storage",
        "002afaef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e3f4) · [`0055e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e4f8) · [`0055e3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e3a4.md#insn-0055e3dc)
- 新版 `0058128c`（命令位置の公開資料なし） · `00581390`（命令位置の公開資料なし） · `00581274`（命令位置の公開資料なし）

~~~diff
- 0055e3f4 ["INT_ADD", "register:40f0:8", ["const:55e3f4:8", "const:4:8"]]
- 0055e3f4 ["CALL", null, ["callee:00c58210:8"]]
+ 0058128c ["INT_ADD", "register:40f0:8", ["const:58128c:8", "const:4:8"]]
+ 0058128c ["CALL", null, ["callee:00c58210:8"]]
- 0055e3f4 bytes f3f41994
+ 0058128c bytes e15b1b94
- 0055e4f8 ["INT_ADD", "register:40f0:8", ["const:55e4f8:8", "const:4:8"]]
- 0055e4f8 ["CALL", null, ["ram:bdc420:8"]]
+ 00581390 ["INT_ADD", "register:40f0:8", ["const:581390:8", "const:4:8"]]
+ 00581390 ["CALL", null, ["ram:c58e70:8"]]
- 0055e4f8 bytes caf71994
+ 00581390 bytes b85e1b94
- 0055e3dc ["COPY", "register:4008:8", ["const:bef000:8"]]
+ 00581274 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0055e3dc bytes 813400b0
+ 00581274 bytes 413700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b37f417eb5c0414a0f52c2d4b87ec76"></a>

### [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) → [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) FUN_00581454

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0055ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.36% / 新版 92.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005814d8",
      "incomplete_value": true,
      "site": "005814ec",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
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
      "definition_site": "005814d8",
      "incomplete_value": true,
      "site": "005814ec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005814e4",
      "incomplete_value": true,
      "site": "005814f0",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e64c",
      "incomplete_value": true,
      "site": "0055e658",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
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
      "005814cc",
      "READ",
      [
        "storage",
        "002b1800",
        null,
        null
      ]
    ],
    [
      "005814d8",
      "READ",
      [
        "storage",
        "002a6965",
        null,
        "string"
      ]
    ],
    [
      "005814d8",
      "READ",
      [
        "storage",
        "002a6975",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005814cc",
      "READ",
      [
        "storage",
        "002c2e90",
        null,
        null
      ]
    ],
    [
      "005814d8",
      "READ",
      [
        "storage",
        "002b7456",
        null,
        "string"
      ]
    ],
    [
      "005814d8",
      "READ",
      [
        "storage",
        "002b7466",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md#insn-0055e5f0) · [`0055e5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md#insn-0055e5f8) · [`0055e624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md#insn-0055e624)
- 新版 `00581488`（命令位置の公開資料なし） · `00581490`（命令位置の公開資料なし） · `005814bc`（命令位置の公開資料なし）

~~~diff
- 0055e5f0 ["INT_ADD", "register:40f0:8", ["const:55e5f0:8", "const:4:8"]]
- 0055e5f0 ["CALL", null, ["callee:00588e2c:8"]]
+ 00581488 ["INT_ADD", "register:40f0:8", ["const:581488:8", "const:4:8"]]
+ 00581488 ["CALL", null, ["callee:00588e2c:8"]]
- 0055e5f0 bytes 691e0094
+ 00581488 bytes 691e0094
- 0055e5f8 ["INT_ADD", "register:40f0:8", ["const:55e5f8:8", "const:4:8"]]
- 0055e5f8 ["CALL", null, ["callee:0058911c:8"]]
+ 00581490 ["INT_ADD", "register:40f0:8", ["const:581490:8", "const:4:8"]]
+ 00581490 ["CALL", null, ["callee:0058911c:8"]]
- 0055e5f8 bytes 231f0094
+ 00581490 bytes 231f0094
- 0055e624 ["INT_ADD", "register:40f0:8", ["const:55e624:8", "const:4:8"]]
- 0055e624 ["CALL", null, ["callee:00c57a90:8"]]
+ 005814bc ["INT_ADD", "register:40f0:8", ["const:5814bc:8", "const:4:8"]]
+ 005814bc ["CALL", null, ["callee:00c57a90:8"]]
- 0055e624 bytes 87f21994
+ 005814bc bytes 75591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0de7212e713888dd5e63349894ae465b"></a>

### [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) → [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) FUN_00581724

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0053c1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1bc.md) [`0053c1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1c0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 2件 [`0055f054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f054.md) [`0055f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058179c",
      "incomplete_value": true,
      "site": "005817b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e904",
      "incomplete_value": true,
      "site": "0055e918",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:800:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005818e0",
      "incomplete_value": false,
      "site": "005818ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ea48",
      "incomplete_value": false,
      "site": "0055ea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "0058179c",
      "READ",
      [
        "storage",
        "002b1800",
        null,
        null
      ]
    ],
    [
      "005817a8",
      "READ",
      [
        "storage",
        "002a6965",
        null,
        "string"
      ]
    ],
    [
      "005817a8",
      "READ",
      [
        "storage",
        "002a6975",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058179c",
      "READ",
      [
        "storage",
        "002c2e90",
        null,
        null
      ]
    ],
    [
      "005817a8",
      "READ",
      [
        "storage",
        "002b7456",
        null,
        "string"
      ]
    ],
    [
      "005817a8",
      "READ",
      [
        "storage",
        "002b7466",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md#insn-0055e8c0) · [`0055e8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md#insn-0055e8c8) · [`0055e8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md#insn-0055e8f4)
- 新版 `00581758`（命令位置の公開資料なし） · `00581760`（命令位置の公開資料なし） · `0058178c`（命令位置の公開資料なし）

~~~diff
- 0055e8c0 ["INT_ADD", "register:40f0:8", ["const:55e8c0:8", "const:4:8"]]
- 0055e8c0 ["CALL", null, ["callee:00588e2c:8"]]
+ 00581758 ["INT_ADD", "register:40f0:8", ["const:581758:8", "const:4:8"]]
+ 00581758 ["CALL", null, ["callee:00588e2c:8"]]
- 0055e8c0 bytes b51d0094
+ 00581758 bytes b51d0094
- 0055e8c8 ["INT_ADD", "register:40f0:8", ["const:55e8c8:8", "const:4:8"]]
- 0055e8c8 ["CALL", null, ["callee:0058911c:8"]]
+ 00581760 ["INT_ADD", "register:40f0:8", ["const:581760:8", "const:4:8"]]
+ 00581760 ["CALL", null, ["callee:0058911c:8"]]
- 0055e8c8 bytes 6f1e0094
+ 00581760 bytes 6f1e0094
- 0055e8f4 ["INT_ADD", "register:40f0:8", ["const:55e8f4:8", "const:4:8"]]
- 0055e8f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058178c ["INT_ADD", "register:40f0:8", ["const:58178c:8", "const:4:8"]]
+ 0058178c ["CALL", null, ["callee:00c57a90:8"]]
- 0055e8f4 bytes d3f11994
+ 0058178c bytes c1581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fda6923c8b8934dbbc4fc2548615be"></a>

### [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) → [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) FUN_005819f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0053b878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b878.md) [`0053b998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b998.md) [`0053b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b99c.md) · 呼出先 2件 [`0055f8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`0055e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md) [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md) · 呼出先 2件 [`00582778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581a1c",
      "incomplete_value": false,
      "site": "00581a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eb84",
      "incomplete_value": false,
      "site": "0055eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00581a28",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581a28",
      "DATA",
      [
        "storage",
        "00c6c348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055eb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md#insn-0055eb78) · [`0055eb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md#insn-0055eb80) · [`0055eb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md#insn-0055eb84)
- 新版 `00581a10`（命令位置の公開資料なし） · `00581a18`（命令位置の公開資料なし） · `00581a1c`（命令位置の公開資料なし）

~~~diff
- 0055eb78 ["INT_ADD", "register:40f0:8", ["const:55eb78:8", "const:4:8"]]
- 0055eb78 ["CALL", null, ["callee:00c57a90:8"]]
+ 00581a10 ["INT_ADD", "register:40f0:8", ["const:581a10:8", "const:4:8"]]
+ 00581a10 ["CALL", null, ["callee:00c57a90:8"]]
- 0055eb78 bytes 32f11994
+ 00581a10 bytes 20581b94
- 0055eb80 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00581a18 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0055eb80 bytes 883400b0
+ 00581a18 bytes 483700f0
- 0055eb84 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0055eb84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581a1c ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00581a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 bytes 08211e91
+ 00581a1c bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-208bd8e92c6c36e0560146ab2347f11c"></a>

### [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) → [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) FUN_00581a68

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md) [`0053bc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053bc44.md) · 呼出先 2件 [`0055fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) [`0055eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md) · 呼出先 2件 [`00582ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00581a98",
      "incomplete_value": false,
      "site": "00581aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ec00",
      "incomplete_value": false,
      "site": "0055ec0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "00581aa4",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581aa4",
      "DATA",
      [
        "storage",
        "00c6c3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ebf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md#insn-0055ebf4) · [`0055ebfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md#insn-0055ebfc) · [`0055ec00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md#insn-0055ec00)
- 新版 `00581a8c`（命令位置の公開資料なし） · `00581a94`（命令位置の公開資料なし） · `00581a98`（命令位置の公開資料なし）

~~~diff
- 0055ebf4 ["INT_ADD", "register:40f0:8", ["const:55ebf4:8", "const:4:8"]]
- 0055ebf4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00581a8c ["INT_ADD", "register:40f0:8", ["const:581a8c:8", "const:4:8"]]
+ 00581a8c ["CALL", null, ["callee:00c57a90:8"]]
- 0055ebf4 bytes 13f11994
+ 00581a8c bytes 01581b94
- 0055ebfc ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00581a94 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0055ebfc bytes 883400b0
+ 00581a94 bytes 483700f0
- 0055ec00 ["COPY", "tmp:0:8", ["const:830:8"]]
- 0055ec00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581a98 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00581a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 bytes 08c12091
+ 00581a98 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb33c259914483e62b1de1ff2b8f439b"></a>

### [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) → [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) FUN_00581f7c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) · 呼出先 5件 [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`005668b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) · 呼出先 5件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.63% / 新版 81.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581fb8",
      "incomplete_value": false,
      "site": "00581fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f120",
      "incomplete_value": false,
      "site": "0055f120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00581ffc",
      "incomplete_value": true,
      "site": "00582004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f164",
      "incomplete_value": true,
      "site": "0055f16c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a0:8"
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
      "definition_site": "00581ff8",
      "incomplete_value": true,
      "site": "00582008",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:687:8"
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
      "00581fb8",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ],
    [
      "00581ff8",
      "READ",
      [
        "storage",
        "002a4687",
        null,
        "string"
      ]
    ],
    [
      "00581ff8",
      "READ",
      [
        "storage",
        "002a4697",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581fb8",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00581ff8",
      "READ",
      [
        "storage",
        "002b4ef4",
        null,
        "string"
      ]
    ],
    [
      "00581ff8",
      "READ",
      [
        "storage",
        "002b4f04",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md#insn-0055f0fc) · [`0055f100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md#insn-0055f100) · [`0055f128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md#insn-0055f128)
- 新版 `00581f94`（命令位置の公開資料なし） · `00581f98`（命令位置の公開資料なし） · `00581fc0`（命令位置の公開資料なし）

~~~diff
- 0055f0fc ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00581f94 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0055f0fc bytes 89340090
+ 00581f94 bytes 493700f0
- 0055f100 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0055f100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00581f98 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00581f98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00581f98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00581f98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f100 bytes 29811c91
+ 00581f98 bytes 29810b91
- 0055f128 ["INT_ADD", "register:40f0:8", ["const:55f128:8", "const:4:8"]]
- 0055f128 ["CALL", null, ["callee:00589750:8"]]
+ 00581fc0 ["INT_ADD", "register:40f0:8", ["const:581fc0:8", "const:4:8"]]
+ 00581fc0 ["CALL", null, ["callee:00589750:8"]]
- 0055f128 bytes e41d0094
+ 00581fc0 bytes e41d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a048fb50728401da280f5ef09e4ca917"></a>

### [`0055f2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2c0.md) → [`00582158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582158.md) FUN_00582158

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)

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
      "definition_site": "00582160",
      "incomplete_value": false,
      "site": "00582160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2c8",
      "incomplete_value": false,
      "site": "0055f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "00582160",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582160",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2c0.md#insn-0055f2c0) · [`0055f2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2c0.md#insn-0055f2c4)
- 新版 `00582158`（命令位置の公開資料なし） · `0058215c`（命令位置の公開資料なし）

~~~diff
- 0055f2c0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00582158 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0055f2c0 bytes 88340090
+ 00582158 bytes 483700d0
- 0055f2c4 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0055f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058215c ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 0058215c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058215c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058215c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 bytes 08811c91
+ 0058215c bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e2383ab68d6a21e4d965ae3f37713f"></a>

### [`0055f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md) → [`00582168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582168.md) FUN_00582168

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00582180",
      "incomplete_value": false,
      "site": "00582180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2e8",
      "incomplete_value": false,
      "site": "0055f2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "00582180",
      "DATA",
      [
        "storage",
        "00bef720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582180",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md#insn-0055f2dc) · [`0055f2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md#insn-0055f2e0) · [`0055f2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f2d0.md#insn-0055f2ec)
- 新版 `00582174`（命令位置の公開資料なし） · `00582178`（命令位置の公開資料なし） · `00582184`（命令位置の公開資料なし）

~~~diff
- 0055f2dc ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00582174 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0055f2dc bytes 88340090
+ 00582174 bytes 483700d0
- 0055f2e0 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0055f2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582178 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00582178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 bytes 08811c91
+ 00582178 bytes 08810b91
- 0055f2ec ["INT_ADD", "register:40f0:8", ["const:55f2ec:8", "const:4:8"]]
- 0055f2ec ["CALL", null, ["callee:0058a87c:8"]]
+ 00582184 ["INT_ADD", "register:40f0:8", ["const:582184:8", "const:4:8"]]
+ 00582184 ["CALL", null, ["callee:0058a87c:8"]]
- 0055f2ec bytes be210094
+ 00582184 bytes be210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb15e4c55d966e7370123b80d86ddfc"></a>

### [`0055f300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md) → [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) FUN_00582198

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582274",
      "incomplete_value": false,
      "site": "00582280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f3dc",
      "incomplete_value": false,
      "site": "0055f3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "00582280",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582280",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md#insn-0055f330) · [`0055f348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md#insn-0055f348) · [`0055f350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md#insn-0055f350)
- 新版 `005821c8`（命令位置の公開資料なし） · `005821e0`（命令位置の公開資料なし） · `005821e8`（命令位置の公開資料なし）

~~~diff
- 0055f330 ["INT_ADD", "register:40f0:8", ["const:55f330:8", "const:4:8"]]
- 0055f330 ["CALL", null, ["callee:00588e2c:8"]]
+ 005821c8 ["INT_ADD", "register:40f0:8", ["const:5821c8:8", "const:4:8"]]
+ 005821c8 ["CALL", null, ["callee:00588e2c:8"]]
- 0055f330 bytes 191b0094
+ 005821c8 bytes 191b0094
- 0055f348 ["INT_ADD", "register:40f0:8", ["const:55f348:8", "const:4:8"]]
- 0055f348 ["CALL", null, ["callee:00589c88:8"]]
+ 005821e0 ["INT_ADD", "register:40f0:8", ["const:5821e0:8", "const:4:8"]]
+ 005821e0 ["CALL", null, ["callee:00589c88:8"]]
- 0055f348 bytes aa1e0094
+ 005821e0 bytes aa1e0094
- 0055f350 ["INT_ADD", "register:40f0:8", ["const:55f350:8", "const:4:8"]]
- 0055f350 ["CALL", null, ["callee:00589818:8"]]
+ 005821e8 ["INT_ADD", "register:40f0:8", ["const:5821e8:8", "const:4:8"]]
+ 005821e8 ["CALL", null, ["callee:00589818:8"]]
- 0055f350 bytes 8c1d0094
+ 005821e8 bytes 8c1d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a74dd34e15b8c68dcdceaa148969375"></a>

### [`0055f488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md) → [`00582320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md) FUN_00582320

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589d30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582404",
      "incomplete_value": false,
      "site": "00582410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f56c",
      "incomplete_value": false,
      "site": "0055f578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "00582410",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582410",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md#insn-0055f4bc) · [`0055f4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md#insn-0055f4d4) · [`0055f4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md#insn-0055f4dc)
- 新版 `00582354`（命令位置の公開資料なし） · `0058236c`（命令位置の公開資料なし） · `00582374`（命令位置の公開資料なし）

~~~diff
- 0055f4bc ["INT_ADD", "register:40f0:8", ["const:55f4bc:8", "const:4:8"]]
- 0055f4bc ["CALL", null, ["callee:00588e2c:8"]]
+ 00582354 ["INT_ADD", "register:40f0:8", ["const:582354:8", "const:4:8"]]
+ 00582354 ["CALL", null, ["callee:00588e2c:8"]]
- 0055f4bc bytes b61a0094
+ 00582354 bytes b61a0094
- 0055f4d4 ["INT_ADD", "register:40f0:8", ["const:55f4d4:8", "const:4:8"]]
- 0055f4d4 ["CALL", null, ["callee:00589d30:8"]]
+ 0058236c ["INT_ADD", "register:40f0:8", ["const:58236c:8", "const:4:8"]]
+ 0058236c ["CALL", null, ["callee:00589d30:8"]]
- 0055f4d4 bytes 711e0094
+ 0058236c bytes 711e0094
- 0055f4dc ["INT_ADD", "register:40f0:8", ["const:55f4dc:8", "const:4:8"]]
- 0055f4dc ["CALL", null, ["callee:00589818:8"]]
+ 00582374 ["INT_ADD", "register:40f0:8", ["const:582374:8", "const:4:8"]]
+ 00582374 ["CALL", null, ["callee:00589818:8"]]
- 0055f4dc bytes 291d0094
+ 00582374 bytes 291d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cad44e9f791b655bc09456145a7131c"></a>

### [`0055f61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md) → [`005824b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md) FUN_005824b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589d30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582584",
      "incomplete_value": false,
      "site": "00582590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f6ec",
      "incomplete_value": false,
      "site": "0055f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "00582590",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582590",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md#insn-0055f650) · [`0055f668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md#insn-0055f668) · [`0055f670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md#insn-0055f670)
- 新版 `005824e8`（命令位置の公開資料なし） · `00582500`（命令位置の公開資料なし） · `00582508`（命令位置の公開資料なし）

~~~diff
- 0055f650 ["INT_ADD", "register:40f0:8", ["const:55f650:8", "const:4:8"]]
- 0055f650 ["CALL", null, ["callee:00588e2c:8"]]
+ 005824e8 ["INT_ADD", "register:40f0:8", ["const:5824e8:8", "const:4:8"]]
+ 005824e8 ["CALL", null, ["callee:00588e2c:8"]]
- 0055f650 bytes 511a0094
+ 005824e8 bytes 511a0094
- 0055f668 ["INT_ADD", "register:40f0:8", ["const:55f668:8", "const:4:8"]]
- 0055f668 ["CALL", null, ["callee:00589d30:8"]]
+ 00582500 ["INT_ADD", "register:40f0:8", ["const:582500:8", "const:4:8"]]
+ 00582500 ["CALL", null, ["callee:00589d30:8"]]
- 0055f668 bytes 0c1e0094
+ 00582500 bytes 0c1e0094
- 0055f670 ["INT_ADD", "register:40f0:8", ["const:55f670:8", "const:4:8"]]
- 0055f670 ["CALL", null, ["callee:00589818:8"]]
+ 00582508 ["INT_ADD", "register:40f0:8", ["const:582508:8", "const:4:8"]]
+ 00582508 ["CALL", null, ["callee:00589818:8"]]
- 0055f670 bytes c41c0094
+ 00582508 bytes c41c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eb954d89b0837c1ee2d40417dd10178"></a>

### [`0055f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md) → [`00582630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md) FUN_00582630

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005826c0",
      "incomplete_value": false,
      "site": "005826cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f828",
      "incomplete_value": false,
      "site": "0055f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "005826cc",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005826cc",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md#insn-0055f7b4) · [`0055f7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md#insn-0055f7c0) · [`0055f7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md#insn-0055f7d4)
- 新版 `0058264c`（命令位置の公開資料なし） · `00582658`（命令位置の公開資料なし） · `0058266c`（命令位置の公開資料なし）

~~~diff
- 0055f7b4 ["INT_ADD", "register:40f0:8", ["const:55f7b4:8", "const:4:8"]]
- 0055f7b4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058264c ["INT_ADD", "register:40f0:8", ["const:58264c:8", "const:4:8"]]
+ 0058264c ["CALL", null, ["callee:00588e2c:8"]]
- 0055f7b4 bytes f8190094
+ 0058264c bytes f8190094
- 0055f7c0 ["INT_ADD", "register:40f0:8", ["const:55f7c0:8", "const:4:8"]]
- 0055f7c0 ["CALL", null, ["callee:00589818:8"]]
+ 00582658 ["INT_ADD", "register:40f0:8", ["const:582658:8", "const:4:8"]]
+ 00582658 ["CALL", null, ["callee:00589818:8"]]
- 0055f7c0 bytes 701c0094
+ 00582658 bytes 701c0094
- 0055f7d4 ["INT_ADD", "register:40f0:8", ["const:55f7d4:8", "const:4:8"]]
- 0055f7d4 ["CALL", null, ["callee:004977f4:8"]]
+ 0058266c ["INT_ADD", "register:40f0:8", ["const:58266c:8", "const:4:8"]]
+ 0058266c ["CALL", null, ["callee:004977f4:8"]]
- 0055f7d4 bytes 6254fc97
+ 0058266c bytes 6254fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71307af76e304ae9240c2b7b383256e0"></a>

### [`0055f8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md) → [`00582778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md) FUN_00582778

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055eb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055eb5c.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005827a8",
      "incomplete_value": false,
      "site": "005827a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f910",
      "incomplete_value": false,
      "site": "0055f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "005827a8",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ],
    [
      "005827d0",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "005827a8",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ],
    [
      "005827d0",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md#insn-0055f8fc) · [`0055f900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md#insn-0055f900) · [`0055f948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f8e0.md#insn-0055f948)
- 新版 `00582794`（命令位置の公開資料なし） · `00582798`（命令位置の公開資料なし） · `005827e0`（命令位置の公開資料なし）

~~~diff
- 0055f8fc ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00582794 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0055f8fc bytes 89340090
+ 00582794 bytes 493700d0
- 0055f900 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0055f900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582798 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00582798 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582798 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582798 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f900 bytes 29611f91
+ 00582798 bytes 29610e91
- 0055f948 ["INT_ADD", "register:40f0:8", ["const:55f948:8", "const:4:8"]]
- 0055f948 ["CALL", null, ["callee:00c589f0:8"]]
+ 005827e0 ["INT_ADD", "register:40f0:8", ["const:5827e0:8", "const:4:8"]]
+ 005827e0 ["CALL", null, ["callee:00c589f0:8"]]
- 0055f948 bytes 96f11994
+ 005827e0 bytes 84581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8339de9e993e48e49e25917c163ac63"></a>

### [`0055fa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fa98.md) → [`00582930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582930.md) FUN_00582930

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582940",
      "incomplete_value": false,
      "site": "00582940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055faa8",
      "incomplete_value": false,
      "site": "0055faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "00582940",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582940",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055faa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fa98.md#insn-0055faa0) · [`0055faa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fa98.md#insn-0055faa4)
- 新版 `00582938`（命令位置の公開資料なし） · `0058293c`（命令位置の公開資料なし）

~~~diff
- 0055faa0 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00582938 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0055faa0 bytes 89340090
+ 00582938 bytes 493700d0
- 0055faa4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0055faa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058293c ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0058293c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058293c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058293c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 bytes 29611f91
+ 0058293c bytes 29610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c159dfa0eace0c31fc2bdeb6a0247989"></a>

### [`0055fac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md) → [`00582958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582958.md) FUN_00582958

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00582964",
      "incomplete_value": false,
      "site": "00582964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055facc",
      "incomplete_value": false,
      "site": "0055facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "00582964",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582964",
      "DATA",
      [
        "storage",
        "00c6c398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md#insn-0055fac4) · [`0055fac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md#insn-0055fac8) · [`0055faf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fac0.md#insn-0055faf0)
- 新版 `0058295c`（命令位置の公開資料なし） · `00582960`（命令位置の公開資料なし） · `00582988`（命令位置の公開資料なし）

~~~diff
- 0055fac4 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058295c ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0055fac4 bytes 89340090
+ 0058295c bytes 493700d0
- 0055fac8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0055fac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582960 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00582960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 bytes 29611f91
+ 00582960 bytes 29610e91
- 0055faf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055faf0 ["INT_ADD", "register:40f0:8", ["const:55faf0:8", "const:4:8"]]
- 0055faf0 ["CALLIND", null, ["register:0:8"]]
+ 00582988 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582988 ["INT_ADD", "register:40f0:8", ["const:582988:8", "const:4:8"]]
+ 00582988 ["CALLIND", null, ["register:0:8"]]
- 0055faf0 bytes 20013fd6
+ 00582988 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e09bd07d02082407546691e6f2406bd"></a>

### [`0055fe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md) → [`00582ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md) FUN_00582ca0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ebd0.md) · 呼出先 4件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc040.md)
- 新版 呼出元 1件 [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) · 呼出先 4件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582cd8",
      "incomplete_value": false,
      "site": "00582cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe40",
      "incomplete_value": false,
      "site": "0055fe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "definition_site": "00582d08",
      "incomplete_value": true,
      "site": "00582d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe70",
      "incomplete_value": true,
      "site": "0055fe70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c7e:8"
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
      "definition_site": "00582dc4",
      "incomplete_value": true,
      "site": "00582dc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ff2c",
      "incomplete_value": true,
      "site": "0055ff2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:95c:8"
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
      "00582cd8",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ],
    [
      "00582cf8",
      "READ",
      [
        "storage",
        "00297c7e",
        null,
        "string"
      ]
    ],
    [
      "00582db0",
      "READ",
      [
        "storage",
        "0029295c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582cd8",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ],
    [
      "00582cf8",
      "READ",
      [
        "storage",
        "002a78d7",
        null,
        "string"
      ]
    ],
    [
      "00582db0",
      "READ",
      [
        "storage",
        "002a206c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055fe30) · [`0055fe34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055fe34) · [`0055fe54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055fe08.md#insn-0055fe54)
- 新版 `00582cc8`（命令位置の公開資料なし） · `00582ccc`（命令位置の公開資料なし） · `00582cec`（命令位置の公開資料なし）

~~~diff
- 0055fe30 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00582cc8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0055fe30 bytes 89340090
+ 00582cc8 bytes 493700d0
- 0055fe34 ["COPY", "tmp:0:8", ["const:880:8"]]
- 0055fe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582ccc ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00582ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 bytes 29012291
+ 00582ccc bytes 29011191
- 0055fe54 ["COPY", "register:4048:8", ["const:297000:8"]]
+ 00582cec ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0055fe54 bytes c9e9ff90
+ 00582cec bytes 29e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0354acecf17a602844e74f757f2375fe"></a>

### [`00560124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560124.md) → [`00582fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fbc.md) FUN_00582fbc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582fcc",
      "incomplete_value": false,
      "site": "00582fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560134",
      "incomplete_value": false,
      "site": "00560134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "00582fcc",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582fcc",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056012c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560124.md#insn-0056012c) · [`00560130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560124.md#insn-00560130)
- 新版 `00582fc4`（命令位置の公開資料なし） · `00582fc8`（命令位置の公開資料なし）

~~~diff
- 0056012c ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00582fc4 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056012c bytes 693400f0
+ 00582fc4 bytes 493700d0
- 00560130 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00560130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582fc8 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00582fc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560130 bytes 29012291
+ 00582fc8 bytes 29011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba33041fb83c85591255113784d46ccd"></a>

### [`0056014c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md) → [`00582fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582fe4.md) FUN_00582fe4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00582ff0",
      "incomplete_value": false,
      "site": "00582ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560158",
      "incomplete_value": false,
      "site": "00560158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "00582ff0",
      "DATA",
      [
        "storage",
        "00bef880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582ff0",
      "DATA",
      [
        "storage",
        "00c6c440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md#insn-00560150) · [`00560154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md#insn-00560154) · [`0056017c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/0056014c.md#insn-0056017c)
- 新版 `00582fe8`（命令位置の公開資料なし） · `00582fec`（命令位置の公開資料なし） · `00583014`（命令位置の公開資料なし）

~~~diff
- 00560150 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00582fe8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00560150 bytes 693400f0
+ 00582fe8 bytes 493700d0
- 00560154 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00560154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582fec ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00582fec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582fec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560154 bytes 29012291
+ 00582fec bytes 29011191
- 0056017c ["COPY", "register:0:8", ["register:4048:8"]]
- 0056017c ["INT_ADD", "register:40f0:8", ["const:56017c:8", "const:4:8"]]
- 0056017c ["CALLIND", null, ["register:0:8"]]
+ 00583014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00583014 ["INT_ADD", "register:40f0:8", ["const:583014:8", "const:4:8"]]
+ 00583014 ["CALLIND", null, ["register:0:8"]]
- 0056017c bytes 20013fd6
+ 00583014 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16415596a0b15de0ed3b240c2f404ad8"></a>

### [`005605e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md) → [`00583478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md) FUN_00583478

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00560748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`005835e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
      "definition_site": "00583498",
      "incomplete_value": false,
      "site": "00583498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560600",
      "incomplete_value": false,
      "site": "00560600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00583498",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00583498",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005605f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md#insn-005605f4) · [`005605f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md#insn-005605f8) · [`0056063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md#insn-0056063c)
- 新版 `0058348c`（命令位置の公開資料なし） · `00583490`（命令位置の公開資料なし） · `005834d4`（命令位置の公開資料なし）

~~~diff
- 005605f4 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058348c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005605f4 bytes 683400f0
+ 0058348c bytes 483700b0
- 005605f8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 005605f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583490 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00583490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005605f8 bytes 08212491
+ 00583490 bytes 08211391
- 0056063c ["INT_ADD", "register:40f0:8", ["const:56063c:8", "const:4:8"]]
- 0056063c ["CALL", null, ["callee:0043bae0:8"]]
+ 005834d4 ["INT_ADD", "register:40f0:8", ["const:5834d4:8", "const:4:8"]]
+ 005834d4 ["CALL", null, ["callee:0043bae0:8"]]
- 0056063c bytes 69e2fa97
+ 005834d4 bytes 83e1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-246e31829d9f1b9769c5161dffbaf584"></a>

### [`00560748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md) → [`005835e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005835e0.md) FUN_005835e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053ee58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee58.md) · 呼出先 2件 [`005605e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005605e0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00561cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf0.md) · 呼出先 2件 [`00583478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583478.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0058361c",
      "incomplete_value": false,
      "site": "00583628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560784",
      "incomplete_value": false,
      "site": "00560790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00583628",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583628",
      "DATA",
      [
        "storage",
        "00c6c608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md#insn-00560778) · [`00560780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md#insn-00560780) · [`00560784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560748.md#insn-00560784)
- 新版 `00583610`（命令位置の公開資料なし） · `00583618`（命令位置の公開資料なし） · `0058361c`（命令位置の公開資料なし）

~~~diff
- 00560778 ["INT_ADD", "register:40f0:8", ["const:560778:8", "const:4:8"]]
- 00560778 ["CALL", null, ["callee:00c57a90:8"]]
+ 00583610 ["INT_ADD", "register:40f0:8", ["const:583610:8", "const:4:8"]]
+ 00583610 ["CALL", null, ["callee:00c57a90:8"]]
- 00560778 bytes 32ea1994
+ 00583610 bytes 20511b94
- 00560780 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00583618 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560780 bytes 683400f0
+ 00583618 bytes 483700b0
- 00560784 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00560784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058361c ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0058361c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058361c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058361c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560784 bytes 08212991
+ 0058361c bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818e99e0f8cf7ac1cdbd21f179ab6491"></a>

### [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) → [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) FUN_0058386c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005609cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609cc.md) [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 25件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) [`00564250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564250.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 2件 [`00583864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583864.md) [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 25件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) [`005870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005870e8.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.01% / 新版 94.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005838f4",
      "incomplete_value": true,
      "site": "00583908",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00560a5c",
      "incomplete_value": true,
      "site": "00560a70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:50:8"
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
      "definition_site": "00583900",
      "incomplete_value": true,
      "site": "00583910",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
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
      "definition_site": "00583900",
      "incomplete_value": true,
      "site": "00583910",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005838c4",
      "READ",
      [
        "storage",
        "0029d645",
        null,
        "string"
      ]
    ],
    [
      "005838cc",
      "READ",
      [
        "storage",
        "0029d64b",
        null,
        "string"
      ]
    ],
    [
      "005838f4",
      "READ",
      [
        "storage",
        "002b1050",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005838c4",
      "READ",
      [
        "storage",
        "002ad8cf",
        null,
        "string"
      ]
    ],
    [
      "005838cc",
      "READ",
      [
        "storage",
        "002ad8d5",
        null,
        "string"
      ]
    ],
    [
      "005838f4",
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

- 旧版 [`00560d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560d68) · [`00560a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560a14) · [`00560a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md#insn-00560a1c)
- 新版 `00583c00`（命令位置の公開資料なし） · `005838ac`（命令位置の公開資料なし） · `005838b4`（命令位置の公開資料なし）

~~~diff
- 00560d68 ["INT_ADD", "register:40f0:8", ["const:560d68:8", "const:4:8"]]
- 00560d68 ["CALL", null, ["callee:005870e8:8"]]
+ 00583c00 ["INT_ADD", "register:40f0:8", ["const:583c00:8", "const:4:8"]]
+ 00583c00 ["CALL", null, ["callee:005870e8:8"]]
- 00560d68 bytes 3a0d0094
+ 00583c00 bytes 3a0d0094
- 00560a14 ["INT_ADD", "register:40f0:8", ["const:560a14:8", "const:4:8"]]
- 00560a14 ["CALL", null, ["callee:00588e2c:8"]]
+ 005838ac ["INT_ADD", "register:40f0:8", ["const:5838ac:8", "const:4:8"]]
+ 005838ac ["CALL", null, ["callee:00588e2c:8"]]
- 00560a14 bytes 60150094
+ 005838ac bytes 60150094
- 00560a1c ["INT_ADD", "register:40f0:8", ["const:560a1c:8", "const:4:8"]]
- 00560a1c ["CALL", null, ["callee:0058911c:8"]]
+ 005838b4 ["INT_ADD", "register:40f0:8", ["const:5838b4:8", "const:4:8"]]
+ 005838b4 ["CALL", null, ["callee:0058911c:8"]]
- 00560a1c bytes 1a160094
+ 005838b4 bytes 1a160094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3913985cb600f1bd026174832d7de93"></a>

### [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) → [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) FUN_00583d98

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00583ea8",
      "incomplete_value": false,
      "site": "00583eb0",
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
            "const:11e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561010",
      "incomplete_value": false,
      "site": "00561018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:bdc:8"
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
      "definition_site": "00583f0c",
      "incomplete_value": false,
      "site": "00583f14",
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
            "const:d2e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561074",
      "incomplete_value": false,
      "site": "0056107c",
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
            "const:774:8"
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
      "definition_site": "00583f70",
      "incomplete_value": false,
      "site": "00583f78",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005610d8",
      "incomplete_value": false,
      "site": "005610e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:743:8"
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
      "00583ea8",
      "PARAM",
      [
        "storage",
        "00290bdc",
        null,
        "string"
      ]
    ],
    [
      "00583f0c",
      "PARAM",
      [
        "storage",
        "002a0774",
        null,
        "string"
      ]
    ],
    [
      "00583f70",
      "PARAM",
      [
        "storage",
        "0029c743",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583ea8",
      "PARAM",
      [
        "storage",
        "002a011e",
        null,
        "string"
      ]
    ],
    [
      "00583f0c",
      "PARAM",
      [
        "storage",
        "002b0d2e",
        null,
        "string"
      ]
    ],
    [
      "00583f70",
      "PARAM",
      [
        "storage",
        "002ac8dc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md#insn-00561018) · [`0056107c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md#insn-0056107c) · [`005610e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md#insn-005610e0)
- 新版 `00583eb0`（命令位置の公開資料なし） · `00583f14`（命令位置の公開資料なし） · `00583f78`（命令位置の公開資料なし）

~~~diff
- 00561018 ["INT_ADD", "register:40f0:8", ["const:561018:8", "const:4:8"]]
- 00561018 ["CALL", null, ["callee:00c57b70:8"]]
+ 00583eb0 ["INT_ADD", "register:40f0:8", ["const:583eb0:8", "const:4:8"]]
+ 00583eb0 ["CALL", null, ["callee:00c57b70:8"]]
- 00561018 bytes 42e81994
+ 00583eb0 bytes 304f1b94
- 0056107c ["INT_ADD", "register:40f0:8", ["const:56107c:8", "const:4:8"]]
- 0056107c ["CALL", null, ["callee:00c57b70:8"]]
+ 00583f14 ["INT_ADD", "register:40f0:8", ["const:583f14:8", "const:4:8"]]
+ 00583f14 ["CALL", null, ["callee:00c57b70:8"]]
- 0056107c bytes 29e81994
+ 00583f14 bytes 174f1b94
- 005610e0 ["INT_ADD", "register:40f0:8", ["const:5610e0:8", "const:4:8"]]
- 005610e0 ["CALL", null, ["callee:00c57b70:8"]]
+ 00583f78 ["INT_ADD", "register:40f0:8", ["const:583f78:8", "const:4:8"]]
+ 00583f78 ["CALL", null, ["callee:00c57b70:8"]]
- 005610e0 bytes 10e81994
+ 00583f78 bytes fe4e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-153f8aee056fda2cba03eea0f6690afc"></a>

### [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) → [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) FUN_0058416c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005612cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612cc.md) · 呼出先 27件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560f00.md) [`00563938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563938.md) [`00563a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563a9c.md) [`00564374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564374.md)
- 新版 呼出元 1件 [`00584164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/00584164.md) · 呼出先 27件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00583d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583d98.md) [`005867d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005867d0.md) [`00586934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586934.md) [`0058720c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058720c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00584204",
      "incomplete_value": true,
      "site": "00584210",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056136c",
      "incomplete_value": true,
      "site": "00561378",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:50:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005844e0",
      "incomplete_value": false,
      "site": "005844f0",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561648",
      "incomplete_value": false,
      "site": "00561658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "005841d0",
      "READ",
      [
        "storage",
        "0029d645",
        null,
        "string"
      ]
    ],
    [
      "005841d8",
      "READ",
      [
        "storage",
        "0029d64b",
        null,
        "string"
      ]
    ],
    [
      "00584200",
      "READ",
      [
        "storage",
        "002949f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005841d0",
      "READ",
      [
        "storage",
        "002ad8cf",
        null,
        "string"
      ]
    ],
    [
      "005841d8",
      "READ",
      [
        "storage",
        "002ad8d5",
        null,
        "string"
      ]
    ],
    [
      "00584200",
      "READ",
      [
        "storage",
        "002a430f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md#insn-00561658) · [`00561320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md#insn-00561320) · [`00561328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md#insn-00561328)
- 新版 `005844f0`（命令位置の公開資料なし） · `005841b8`（命令位置の公開資料なし） · `005841c0`（命令位置の公開資料なし）

~~~diff
- 00561658 ["INT_ADD", "register:40f0:8", ["const:561658:8", "const:4:8"]]
- 00561658 ["CALL", null, ["callee:0058720c:8"]]
+ 005844f0 ["INT_ADD", "register:40f0:8", ["const:5844f0:8", "const:4:8"]]
+ 005844f0 ["CALL", null, ["callee:0058720c:8"]]
- 00561658 bytes 470b0094
+ 005844f0 bytes 470b0094
- 00561320 ["INT_ADD", "register:40f0:8", ["const:561320:8", "const:4:8"]]
- 00561320 ["CALL", null, ["callee:00588e2c:8"]]
+ 005841b8 ["INT_ADD", "register:40f0:8", ["const:5841b8:8", "const:4:8"]]
+ 005841b8 ["CALL", null, ["callee:00588e2c:8"]]
- 00561320 bytes 1d130094
+ 005841b8 bytes 1d130094
- 00561328 ["INT_ADD", "register:40f0:8", ["const:561328:8", "const:4:8"]]
- 00561328 ["CALL", null, ["callee:0058911c:8"]]
+ 005841c0 ["INT_ADD", "register:40f0:8", ["const:5841c0:8", "const:4:8"]]
+ 005841c0 ["CALL", null, ["callee:0058911c:8"]]
- 00561328 bytes d7130094
+ 005841c0 bytes d7130094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64c4911dd0917f1c8563919253fa1bd"></a>

### [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) → [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) FUN_005848f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`00564590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564590.md) [`005645f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005645f0.md) [`00564974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564974.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`00587428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587428.md) [`00587488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587488.md) [`0058780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058780c.md)

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
      "definition_site": "0058493c",
      "incomplete_value": false,
      "site": "00584944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561aa4",
      "incomplete_value": false,
      "site": "00561aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "00584968",
      "incomplete_value": false,
      "site": "00584970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561ad0",
      "incomplete_value": false,
      "site": "00561ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "definition_site": "005849d8",
      "incomplete_value": false,
      "site": "005849d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b40",
      "incomplete_value": false,
      "site": "00561b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00584944",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ],
    [
      "00584970",
      "DATA",
      [
        "storage",
        "00befae8",
        null,
        "pointer"
      ]
    ],
    [
      "005849d8",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00584944",
      "DATA",
      [
        "storage",
        "00c6c658",
        null,
        "pointer"
      ]
    ],
    [
      "00584970",
      "DATA",
      [
        "storage",
        "00c6c6a8",
        null,
        "pointer"
      ]
    ],
    [
      "005849d8",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561a98) · [`00561aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561aa0) · [`00561aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md#insn-00561aa4)
- 新版 `00584930`（命令位置の公開資料なし） · `00584938`（命令位置の公開資料なし） · `0058493c`（命令位置の公開資料なし）

~~~diff
- 00561a98 ["INT_ADD", "register:40f0:8", ["const:561a98:8", "const:4:8"]]
- 00561a98 ["CALL", null, ["callee:00c57a90:8"]]
+ 00584930 ["INT_ADD", "register:40f0:8", ["const:584930:8", "const:4:8"]]
+ 00584930 ["CALL", null, ["callee:00c57a90:8"]]
- 00561a98 bytes 6ae51994
+ 00584930 bytes 584c1b94
- 00561aa0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00584938 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00561aa0 bytes 683400d0
+ 00584938 bytes 48370090
- 00561aa4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00561aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058493c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0058493c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058493c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058493c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 bytes 08612a91
+ 0058493c bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ab24ad36b2afd85e40e8c48b8720c36"></a>

### [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) → [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) FUN_0058538c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`005636f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005636f4.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0056503c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md) [`0056508c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md) [`0056521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056521c.md)
- 新版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`0058658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058658c.md) · 呼出先 10件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) [`00587f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md) [`005880b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005880b4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005855b8",
      "incomplete_value": true,
      "site": "005855b8",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562720",
      "incomplete_value": true,
      "site": "00562720",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005853bc",
      "incomplete_value": true,
      "site": "005853bc",
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
      "definition_site": "00562524",
      "incomplete_value": true,
      "site": "00562524",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0058544c",
      "incomplete_value": true,
      "site": "0058544c",
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
      "definition_site": "005625b4",
      "incomplete_value": true,
      "site": "005625b4",
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
      "005853b8",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "00585400",
      "READ",
      [
        "storage",
        "00c26530",
        null,
        "undefined8"
      ]
    ],
    [
      "00585424",
      "PARAM",
      [
        "storage",
        "00c26478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005853b8",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00585400",
      "READ",
      [
        "storage",
        "00ca5ff0",
        null,
        "undefined8"
      ]
    ],
    [
      "00585424",
      "PARAM",
      [
        "storage",
        "00ca5f38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-00562594) · [`0056264c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-0056264c) · [`00562720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md#insn-00562720)
- 新版 `0058542c`（命令位置の公開資料なし） · `005854e4`（命令位置の公開資料なし） · `005855b8`（命令位置の公開資料なし）

~~~diff
- 00562594 ["INT_ADD", "register:40f0:8", ["const:562594:8", "const:4:8"]]
- 00562594 ["CALL", null, ["callee:005880b4:8"]]
+ 0058542c ["INT_ADD", "register:40f0:8", ["const:58542c:8", "const:4:8"]]
+ 0058542c ["CALL", null, ["callee:005880b4:8"]]
- 00562594 bytes 220b0094
+ 0058542c bytes 220b0094
- 0056264c ["INT_ADD", "register:40f0:8", ["const:56264c:8", "const:4:8"]]
- 0056264c ["CALL", null, ["callee:00587f24:8"]]
+ 005854e4 ["INT_ADD", "register:40f0:8", ["const:5854e4:8", "const:4:8"]]
+ 005854e4 ["CALL", null, ["callee:00587f24:8"]]
- 0056264c bytes 900a0094
+ 005854e4 bytes 900a0094
- 00562720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00562720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005855b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f20:8"]]
+ 005855b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562720 bytes 283102f9
+ 005855b8 bytes 289107f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df42c3184a755c0c26d5216d09047f87"></a>

### [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) → [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef38.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) [`00581dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581dd0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件, `store_condition` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005857e8",
      "incomplete_value": false,
      "site": "005857f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562950",
      "incomplete_value": false,
      "site": "0056295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00585b88",
      "incomplete_value": true,
      "site": "00585b88",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562cf0",
      "incomplete_value": true,
      "site": "00562cf0",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005856d4",
      "incomplete_value": true,
      "site": "005856d4",
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
      "definition_site": "0056283c",
      "incomplete_value": true,
      "site": "0056283c",
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
      "005856cc",
      "READ",
      [
        "storage",
        "00c26468",
        null,
        "undefined8"
      ]
    ],
    [
      "00585718",
      "READ",
      [
        "storage",
        "00c264b8",
        null,
        "undefined8"
      ]
    ],
    [
      "005857f4",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005856cc",
      "READ",
      [
        "storage",
        "00ca5f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00585718",
      "READ",
      [
        "storage",
        "00ca5f78",
        null,
        "undefined8"
      ]
    ],
    [
      "005857f4",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562cf0) · [`00562814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562814) · [`00562818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md#insn-00562818)
- 新版 `00585b88`（命令位置の公開資料なし） · `005856ac`（命令位置の公開資料なし） · `005856b0`（命令位置の公開資料なし）

~~~diff
- 00562cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00562cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00585b88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f20:8"]]
+ 00585b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562cf0 bytes 283102f9
+ 00585b88 bytes 289107f9
- 00562814 ["COPY", "register:40d0:8", ["const:c26000:8"]]
+ 005856ac ["COPY", "register:40d0:8", ["const:ca5000:8"]]
- 00562814 bytes 3a360090
+ 005856ac bytes 1a390090
- 00562818 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00562818 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 005856b0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 005856b0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 005856b0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 005856b0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00562818 bytes 5aa31191
+ 005856b0 bytes 5aa33c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daa7963d1f64c80b810b8c201bf0328b"></a>

### [`00563038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md) → [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00562e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562e78.md) [`0056547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00585d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585d10.md) [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00585f04",
      "incomplete_value": true,
      "site": "00585f04",
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
      "definition_site": "0056306c",
      "incomplete_value": true,
      "site": "0056306c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0058601c",
      "incomplete_value": true,
      "site": "0058601c",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "00563184",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00563184"
      ],
      [
        "FALL_THROUGH",
        "0058601c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0058601c",
      "incomplete_value": true,
      "site": "0058603c",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "005631a4",
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
      "00585efc",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "00585f58",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ],
    [
      "00586014",
      "READ",
      [
        "storage",
        "00c26420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00585efc",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00585f58",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ],
    [
      "00586014",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056305c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-0056305c) · [`00563060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-00563060) · [`00563070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md#insn-00563070)
- 新版 `00585ef4`（命令位置の公開資料なし） · `00585ef8`（命令位置の公開資料なし） · `00585f08`（命令位置の公開資料なし）

~~~diff
- 0056305c ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 00585ef4 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0056305c bytes 083600f0
+ 00585ef4 bytes 08390090
- 00563060 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00563060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00585ef8 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00585ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00585ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00585ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563060 bytes 08011291
+ 00585ef8 bytes 08013d91
- 00563070 ["COPY", "register:40b0:8", ["const:c26000:8"]]
+ 00585f08 ["COPY", "register:40b0:8", ["const:ca5000:8"]]
- 00563070 bytes 163600f0
+ 00585f08 bytes 16390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9d39304216aef86e8ae881edaf7bfc"></a>

### [`0056340c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md) → [`005862a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055ef38.md) [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) [`00581dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581dd0.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005862d4",
      "incomplete_value": true,
      "site": "005862d4",
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
      "definition_site": "0056343c",
      "incomplete_value": true,
      "site": "0056343c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00586414",
      "incomplete_value": true,
      "site": "00586414",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056357c",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0056357c"
      ],
      [
        "FALL_THROUGH",
        "00586414"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00586414",
      "incomplete_value": true,
      "site": "00586434",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056359c",
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
      "005862d0",
      "READ",
      [
        "storage",
        "00c26480",
        null,
        "undefined8"
      ]
    ],
    [
      "00586328",
      "READ",
      [
        "storage",
        "00c26500",
        null,
        "undefined8"
      ]
    ],
    [
      "00586358",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005862d0",
      "READ",
      [
        "storage",
        "00ca5f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00586328",
      "READ",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00586358",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-00563430) · [`00563434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-00563434) · [`00563440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md#insn-00563440)
- 新版 `005862c8`（命令位置の公開資料なし） · `005862cc`（命令位置の公開資料なし） · `005862d8`（命令位置の公開資料なし）

~~~diff
- 00563430 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 005862c8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00563430 bytes 083600f0
+ 005862c8 bytes e83800f0
- 00563434 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00563434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005862cc ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 005862cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005862cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005862cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563434 bytes 08011291
+ 005862cc bytes 08013d91
- 00563440 ["COPY", "register:40c0:8", ["const:c26000:8"]]
+ 005862d8 ["COPY", "register:40c0:8", ["const:ca5000:8"]]
- 00563440 bytes 183600f0
+ 005862d8 bytes f83800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c74708b47c1a6a0c6ac3c53a16d2463"></a>

### [`00563704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md) → [`0058659c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058659c.md) FUN_0058659c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00563804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563804.md) · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0058669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/0058669c.md) · 呼出先 4件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005865b8",
      "incomplete_value": false,
      "site": "005865bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563720",
      "incomplete_value": false,
      "site": "00563724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "005865bc",
      "DATA",
      [
        "storage",
        "00bef928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005865bc",
      "DATA",
      [
        "storage",
        "00c6c4e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056371c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md#insn-0056371c) · [`00563720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md#insn-00563720) · [`0056375c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563704.md#insn-0056375c)
- 新版 `005865b4`（命令位置の公開資料なし） · `005865b8`（命令位置の公開資料なし） · `005865f4`（命令位置の公開資料なし）

~~~diff
- 0056371c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005865b4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056371c bytes 68340090
+ 005865b4 bytes 283700d0
- 00563720 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00563720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005865b8 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 005865b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005865b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005865b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563720 bytes 08a12491
+ 005865b8 bytes 08a11391
- 0056375c ["INT_ADD", "register:40f0:8", ["const:56375c:8", "const:4:8"]]
- 0056375c ["CALL", null, ["callee:00c538e0:8"]]
+ 005865f4 ["INT_ADD", "register:40f0:8", ["const:5865f4:8", "const:4:8"]]
+ 005865f4 ["CALL", null, ["callee:00c538e0:8"]]
- 0056375c bytes cdcd1994
+ 005865f4 bytes bb341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb04adf5019fe4cf03d5ebfdf1c970a"></a>

### [`00563828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md) → [`005866c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005866c0.md) FUN_005866c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005866d8",
      "incomplete_value": false,
      "site": "005866dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "005866dc",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005866dc",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md#insn-0056383c) · [`00563840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md#insn-00563840) · [`00563874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563828.md#insn-00563874)
- 新版 `005866d4`（命令位置の公開資料なし） · `005866d8`（命令位置の公開資料なし） · `0058670c`（命令位置の公開資料なし）

~~~diff
- 0056383c ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 005866d4 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056383c bytes 69340090
+ 005866d4 bytes 293700d0
- 00563840 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00563840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005866d8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005866d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005866d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005866d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563840 bytes 29212491
+ 005866d8 bytes 29211391
- 00563874 ["INT_ADD", "register:40f0:8", ["const:563874:8", "const:4:8"]]
- 00563874 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058670c ["INT_ADD", "register:40f0:8", ["const:58670c:8", "const:4:8"]]
+ 0058670c ["CALL", null, ["callee:00c57ab0:8"]]
- 00563874 bytes fbdd1994
+ 0058670c bytes e9441b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57075965a8973b972c0299e41c0bad4a"></a>

### [`005638b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md) → [`00586748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586748.md) FUN_00586748

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00586760",
      "incomplete_value": false,
      "site": "00586764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00586764",
      "DATA",
      [
        "storage",
        "00bef908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586764",
      "DATA",
      [
        "storage",
        "00c6c4c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005638c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md#insn-005638c4) · [`005638c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md#insn-005638c8) · [`005638f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/005638b0.md#insn-005638f0)
- 新版 `0058675c`（命令位置の公開資料なし） · `00586760`（命令位置の公開資料なし） · `00586788`（命令位置の公開資料なし）

~~~diff
- 005638c4 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058675c ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 005638c4 bytes 69340090
+ 0058675c bytes 293700d0
- 005638c8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 005638c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00586760 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00586760 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00586760 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00586760 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005638c8 bytes 29212491
+ 00586760 bytes 29211391
- 005638f0 ["INT_ADD", "register:40f0:8", ["const:5638f0:8", "const:4:8"]]
- 005638f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00586788 ["INT_ADD", "register:40f0:8", ["const:586788:8", "const:4:8"]]
+ 00586788 ["CALL", null, ["callee:00c57ab0:8"]]
- 005638f0 bytes dcdd1994
+ 00586788 bytes ca441b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e9beaf45d4c5dcdc0a90194aa5cd23f"></a>

### [`00564710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md) → [`005875a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005875a8.md) FUN_005875a8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00564590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564590.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00587428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587428.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058764c",
      "incomplete_value": true,
      "site": "00587650",
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
      "definition_site": "005647b4",
      "incomplete_value": true,
      "site": "005647b8",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005875e8",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00564750",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00587628",
      "incomplete_value": true,
      "site": "00587630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00564790",
      "incomplete_value": true,
      "site": "00564798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
      "005875e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "00587624",
      "PARAM",
      [
        "storage",
        "004377f0",
        null,
        null
      ]
    ],
    [
      "00587628",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005875e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "00587624",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "00587628",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md#insn-00564750) · [`00564798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md#insn-00564798) · [`005647a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564710.md#insn-005647a4)
- 新版 `005875e8`（命令位置の公開資料なし） · `00587630`（命令位置の公開資料なし） · `0058763c`（命令位置の公開資料なし）

~~~diff
- 00564750 ["INT_ADD", "register:40f0:8", ["const:564750:8", "const:4:8"]]
- 00564750 ["CALL", null, ["ram:bdb4a0:8"]]
+ 005875e8 ["INT_ADD", "register:40f0:8", ["const:5875e8:8", "const:4:8"]]
+ 005875e8 ["CALL", null, ["ram:c57ef0:8"]]
- 00564750 bytes 54db1994
+ 005875e8 bytes 42421b94
- 00564798 ["INT_ADD", "register:40f0:8", ["const:564798:8", "const:4:8"]]
- 00564798 ["CALL", null, ["callee:00c57f30:8"]]
+ 00587630 ["INT_ADD", "register:40f0:8", ["const:587630:8", "const:4:8"]]
+ 00587630 ["CALL", null, ["callee:00c57f30:8"]]
- 00564798 bytes 52db1994
+ 00587630 bytes 40421b94
- 005647a4 ["INT_ADD", "register:40f0:8", ["const:5647a4:8", "const:4:8"]]
- 005647a4 ["CALL", null, ["ram:bdb4f0:8"]]
+ 0058763c ["INT_ADD", "register:40f0:8", ["const:58763c:8", "const:4:8"]]
+ 0058763c ["CALL", null, ["ram:c57f40:8"]]
- 005647a4 bytes 53db1994
+ 0058763c bytes 41421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9714fae08679b511dc27d285679c3409"></a>

### [`00564838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md) → [`005876d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005876d0.md) FUN_005876d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "005876e4",
      "incomplete_value": false,
      "site": "005876e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056484c",
      "incomplete_value": false,
      "site": "00564850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "005876e8",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005876e8",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md#insn-00564848) · [`0056484c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md#insn-0056484c) · [`00564860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564838.md#insn-00564860)
- 新版 `005876e0`（命令位置の公開資料なし） · `005876e4`（命令位置の公開資料なし） · `005876f8`（命令位置の公開資料なし）

~~~diff
- 00564848 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005876e0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00564848 bytes 483400f0
+ 005876e0 bytes 283700b0
- 0056484c ["COPY", "tmp:0:8", ["const:b30:8"]]
- 0056484c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005876e4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005876e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005876e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005876e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056484c bytes 08c12c91
+ 005876e4 bytes 08c11b91
- 00564860 ["INT_ADD", "register:40f0:8", ["const:564860:8", "const:4:8"]]
- 00564860 ["CALL", null, ["callee:00c538e0:8"]]
+ 005876f8 ["INT_ADD", "register:40f0:8", ["const:5876f8:8", "const:4:8"]]
+ 005876f8 ["CALL", null, ["callee:00c538e0:8"]]
- 00564860 bytes 8cc91994
+ 005876f8 bytes 7a301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2936a9cdd9acfcb1f01774bb7f725882"></a>

### [`00564894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md) → [`0058772c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/0058772c.md) FUN_0058772c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00587744",
      "incomplete_value": false,
      "site": "00587748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005648ac",
      "incomplete_value": false,
      "site": "005648b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00587748",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587748",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005648a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md#insn-005648a8) · [`005648ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md#insn-005648ac) · [`005648c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564894.md#insn-005648c0)
- 新版 `00587740`（命令位置の公開資料なし） · `00587744`（命令位置の公開資料なし） · `00587758`（命令位置の公開資料なし）

~~~diff
- 005648a8 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00587740 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005648a8 bytes 483400f0
+ 00587740 bytes 283700b0
- 005648ac ["COPY", "tmp:0:8", ["const:b30:8"]]
- 005648ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587744 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00587744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005648ac bytes 08c12c91
+ 00587744 bytes 08c11b91
- 005648c0 ["INT_ADD", "register:40f0:8", ["const:5648c0:8", "const:4:8"]]
- 005648c0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00587758 ["INT_ADD", "register:40f0:8", ["const:587758:8", "const:4:8"]]
+ 00587758 ["CALL", null, ["callee:00c538e0:8"]]
- 005648c0 bytes 74c91994
+ 00587758 bytes 62301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce66642315ea65506ded3fc019029b0"></a>

### [`005648f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md) → [`00587788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587788.md) FUN_00587788

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "005877ac",
      "incomplete_value": false,
      "site": "005877ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564914",
      "incomplete_value": false,
      "site": "00564914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "005877ac",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005877ac",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md#insn-00564904) · [`0056490c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md#insn-0056490c) · [`00564910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005648f0.md#insn-00564910)
- 新版 `0058779c`（命令位置の公開資料なし） · `005877a4`（命令位置の公開資料なし） · `005877a8`（命令位置の公開資料なし）

~~~diff
- 00564904 ["INT_ADD", "register:40f0:8", ["const:564904:8", "const:4:8"]]
- 00564904 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058779c ["INT_ADD", "register:40f0:8", ["const:58779c:8", "const:4:8"]]
+ 0058779c ["CALL", null, ["callee:00c57a90:8"]]
- 00564904 bytes cfd91994
+ 0058779c bytes bd401b94
- 0056490c ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 005877a4 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056490c bytes 493400f0
+ 005877a4 bytes 293700b0
- 00564910 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00564910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005877a8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005877a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005877a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005877a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564910 bytes 29c12c91
+ 005877a8 bytes 29c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62da1197f7950d756eb7ea161fa2c013"></a>

### [`00564940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md) → [`005877d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005877d8.md) FUN_005877d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "005877e4",
      "incomplete_value": false,
      "site": "005877e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056494c",
      "incomplete_value": false,
      "site": "0056494c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "005877e4",
      "DATA",
      [
        "storage",
        "00befb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005877e4",
      "DATA",
      [
        "storage",
        "00c6c6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md#insn-00564944) · [`00564948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md#insn-00564948) · [`00564968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564940.md#insn-00564968)
- 新版 `005877dc`（命令位置の公開資料なし） · `005877e0`（命令位置の公開資料なし） · `00587800`（命令位置の公開資料なし）

~~~diff
- 00564944 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 005877dc ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00564944 bytes 493400f0
+ 005877dc bytes 293700b0
- 00564948 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00564948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005877e0 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005877e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005877e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005877e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564948 bytes 29c12c91
+ 005877e0 bytes 29c11b91
- 00564968 ["INT_ADD", "register:40f0:8", ["const:564968:8", "const:4:8"]]
- 00564968 ["CALL", null, ["callee:00c538b0:8"]]
+ 00587800 ["INT_ADD", "register:40f0:8", ["const:587800:8", "const:4:8"]]
+ 00587800 ["CALL", null, ["callee:00c538b0:8"]]
- 00564968 bytes 3ec91994
+ 00587800 bytes 2c301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7055a780722968a1c30c5aa47688ad83"></a>

### [`00564b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564b70.md) → [`00587a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587a08.md) FUN_00587a08

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564a14.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`005878ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/005878ac.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

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
      "site": "00587a4c",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00564bb4",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00587a4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00587a4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564b70.md#insn-00564bb4) · [`00564b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564b70.md#insn-00564b9c) · [`00564bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564b70.md#insn-00564bf0)
- 新版 `00587a4c`（命令位置の公開資料なし） · `00587a34`（命令位置の公開資料なし） · `00587a88`（命令位置の公開資料なし）

~~~diff
- 00564bb4 ["INT_ADD", "register:40f0:8", ["const:564bb4:8", "const:4:8"]]
- 00564bb4 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00587a4c ["INT_ADD", "register:40f0:8", ["const:587a4c:8", "const:4:8"]]
+ 00587a4c ["CALL", null, ["ram:c57ef0:8"]]
- 00564bb4 bytes 3bda1994
+ 00587a4c bytes 29411b94
- 00564b9c ["INT_ADD", "register:40f0:8", ["const:564b9c:8", "const:4:8"]]
- 00564b9c ["CALL", null, ["callee:00c57ce0:8"]]
+ 00587a34 ["INT_ADD", "register:40f0:8", ["const:587a34:8", "const:4:8"]]
+ 00587a34 ["CALL", null, ["callee:00c57ce0:8"]]
- 00564b9c bytes bdd91994
+ 00587a34 bytes ab401b94
- 00564bf0 ["INT_ADD", "register:40f0:8", ["const:564bf0:8", "const:4:8"]]
- 00564bf0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00587a88 ["INT_ADD", "register:40f0:8", ["const:587a88:8", "const:4:8"]]
+ 00587a88 ["CALL", null, ["callee:00c57f80:8"]]
- 00564bf0 bytes 50da1994
+ 00587a88 bytes 3e411b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bee05217ece9b12d6fb145da4a8d118"></a>

### [`00564c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md) → [`00587af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587af8.md) FUN_00587af8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00561a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/00561a60.md) · 呼出先 8件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`005848f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/005848f8.md) · 呼出先 8件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "00587b54",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00564cbc",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "site": "00587bdc",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00564d44",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00587b54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "00587bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00587b54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "00587bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md#insn-00564cbc) · [`00564d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md#insn-00564d44) · [`00564c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564c60.md#insn-00564c9c)
- 新版 `00587b54`（命令位置の公開資料なし） · `00587bdc`（命令位置の公開資料なし） · `00587b34`（命令位置の公開資料なし）

~~~diff
- 00564cbc ["INT_ADD", "register:40f0:8", ["const:564cbc:8", "const:4:8"]]
- 00564cbc ["CALL", null, ["ram:bdb4a0:8"]]
+ 00587b54 ["INT_ADD", "register:40f0:8", ["const:587b54:8", "const:4:8"]]
+ 00587b54 ["CALL", null, ["ram:c57ef0:8"]]
- 00564cbc bytes f9d91994
+ 00587b54 bytes e7401b94
- 00564d44 ["INT_ADD", "register:40f0:8", ["const:564d44:8", "const:4:8"]]
- 00564d44 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00587bdc ["INT_ADD", "register:40f0:8", ["const:587bdc:8", "const:4:8"]]
+ 00587bdc ["CALL", null, ["ram:c57ef0:8"]]
- 00564d44 bytes d7d91994
+ 00587bdc bytes c5401b94
- 00564c9c ["INT_ADD", "register:40f0:8", ["const:564c9c:8", "const:4:8"]]
- 00564c9c ["CALL", null, ["callee:00c57ce0:8"]]
+ 00587b34 ["INT_ADD", "register:40f0:8", ["const:587b34:8", "const:4:8"]]
+ 00587b34 ["CALL", null, ["callee:00c57ce0:8"]]
- 00564c9c bytes 7dd91994
+ 00587b34 bytes 6b401b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c28cacfb6c345998524d02478847132"></a>

### [`00564ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md) → [`00587d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d54.md) FUN_00587d54

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

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
      "site": "00587d64",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00564ecc",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00587d60",
      "incomplete_value": false,
      "site": "00587d64",
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
    "old": {
      "definition_site": "00564ec8",
      "incomplete_value": false,
      "site": "00564ecc",
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
            "const:39d:8"
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
      "00587d60",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00587d64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00587d60",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00587d64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md#insn-00564ecc) · [`00564ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md#insn-00564ec4) · [`00564ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ebc.md#insn-00564ec8)
- 新版 `00587d64`（命令位置の公開資料なし） · `00587d5c`（命令位置の公開資料なし） · `00587d60`（命令位置の公開資料なし）

~~~diff
- 00564ecc ["INT_ADD", "register:40f0:8", ["const:564ecc:8", "const:4:8"]]
- 00564ecc ["CALL", null, ["ram:418c38:8"]]
+ 00587d64 ["INT_ADD", "register:40f0:8", ["const:587d64:8", "const:4:8"]]
+ 00587d64 ["CALL", null, ["ram:43b738:8"]]
- 00564ecc bytes 5bcffa97
+ 00587d64 bytes 75cefa97
- 00564ec4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00587d5c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00564ec4 bytes 00eafff0
+ 00587d5c bytes 80e9ff90
- 00564ec8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00564ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00587d60 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00587d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00587d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00587d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 bytes 00740e91
+ 00587d60 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bdb4c40ab549b94eee1b7f065161f61"></a>

### [`00564ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md) → [`00587d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587d68.md) FUN_00587d68

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056244c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587d84",
      "incomplete_value": false,
      "site": "00587d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564eec",
      "incomplete_value": false,
      "site": "00564eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "definition_site": "00587d90",
      "incomplete_value": false,
      "site": "00587d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564ef8",
      "incomplete_value": false,
      "site": "00564ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00587d84",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00587d90",
      "DATA",
      [
        "storage",
        "00bef928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587d84",
      "DATA",
      [
        "storage",
        "00c6c770",
        null,
        "undefined *"
      ]
    ],
    [
      "00587d90",
      "DATA",
      [
        "storage",
        "00c6c4e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md#insn-00564ee0) · [`00564ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md#insn-00564ee4) · [`00564ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564ed0.md#insn-00564ef0)
- 新版 `00587d78`（命令位置の公開資料なし） · `00587d7c`（命令位置の公開資料なし）

~~~diff
- 00564ee0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00587d78 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00564ee0 bytes 483400f0
+ 00587d78 bytes 283700b0
- 00564ee4 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00564ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587d7c ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00587d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 bytes 08c12e91
+ 00587d7c bytes 08c11d91
- 00564ef0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 00564ef0 bytes 483400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5245efa057c8fb75ae49292345e59b02"></a>

### [`0056503c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md) → [`00587ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587ed4.md) FUN_00587ed4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/005641a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 2件 [`00587038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587038.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00587ee8",
      "incomplete_value": false,
      "site": "00587ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565050",
      "incomplete_value": false,
      "site": "00565058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00587ef0",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587ef0",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056504c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md#insn-0056504c) · [`00565050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md#insn-00565050) · [`00565060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056503c.md#insn-00565060)
- 新版 `00587ee4`（命令位置の公開資料なし） · `00587ee8`（命令位置の公開資料なし） · `00587ef8`（命令位置の公開資料なし）

~~~diff
- 0056504c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00587ee4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056504c bytes 483400d0
+ 00587ee4 bytes 283700b0
- 00565050 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00565050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ee8 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00587ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565050 bytes 08612391
+ 00587ee8 bytes 08611291
- 00565060 ["INT_ADD", "register:40f0:8", ["const:565060:8", "const:4:8"]]
- 00565060 ["CALL", null, ["callee:00587038:8"]]
+ 00587ef8 ["INT_ADD", "register:40f0:8", ["const:587ef8:8", "const:4:8"]]
+ 00587ef8 ["CALL", null, ["callee:00587038:8"]]
- 00565060 bytes 50fcff97
+ 00587ef8 bytes 50fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254ea97b56991c5868e05fff094b2a63"></a>

### [`0056508c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md) → [`00587f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587f24.md) FUN_00587f24

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005624f4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0058538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058538c.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587fd4",
      "incomplete_value": false,
      "site": "00587fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056513c",
      "incomplete_value": false,
      "site": "00565144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00587fdc",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587fdc",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005650c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md#insn-005650c4) · [`00565110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md#insn-00565110) · [`00565130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056508c.md#insn-00565130)
- 新版 `00587f5c`（命令位置の公開資料なし） · `00587fa8`（命令位置の公開資料なし） · `00587fc8`（命令位置の公開資料なし）

~~~diff
- 005650c4 ["INT_ADD", "register:40f0:8", ["const:5650c4:8", "const:4:8"]]
- 005650c4 ["CALL", null, ["callee:00c57be0:8"]]
+ 00587f5c ["INT_ADD", "register:40f0:8", ["const:587f5c:8", "const:4:8"]]
+ 00587f5c ["CALL", null, ["callee:00c57be0:8"]]
- 005650c4 bytes 33d81994
+ 00587f5c bytes 213f1b94
- 00565110 ["INT_ADD", "register:40f0:8", ["const:565110:8", "const:4:8"]]
- 00565110 ["CALL", null, ["callee:00c57a90:8"]]
+ 00587fa8 ["INT_ADD", "register:40f0:8", ["const:587fa8:8", "const:4:8"]]
+ 00587fa8 ["CALL", null, ["callee:00c57a90:8"]]
- 00565110 bytes ccd71994
+ 00587fa8 bytes ba3e1b94
- 00565130 ["INT_ADD", "register:40f0:8", ["const:565130:8", "const:4:8"]]
- 00565130 ["CALL", null, ["callee:00c57c00:8"]]
+ 00587fc8 ["INT_ADD", "register:40f0:8", ["const:587fc8:8", "const:4:8"]]
+ 00587fc8 ["CALL", null, ["callee:00c57c00:8"]]
- 00565130 bytes 20d81994
+ 00587fc8 bytes 0e3f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a0796639b95b9dce485ed401378780"></a>

### [`0056547c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md) → [`00588314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588314.md) FUN_00588314

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563038.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00563d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/00563d44.md)
- 新版 呼出元 2件 [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`00585ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585ed0.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00586bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/00586bdc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058832c",
      "incomplete_value": false,
      "site": "00588330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565494",
      "incomplete_value": false,
      "site": "00565498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "definition_site": "0058833c",
      "incomplete_value": false,
      "site": "00588348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00588330",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "pointer"
      ]
    ],
    [
      "00588348",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588330",
      "DATA",
      [
        "storage",
        "00c6c7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00588348",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md#insn-00565490) · [`00565494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md#insn-00565494) · [`005654a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056547c.md#insn-005654a0)
- 新版 `00588328`（命令位置の公開資料なし） · `0058832c`（命令位置の公開資料なし）

~~~diff
- 00565490 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00588328 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00565490 bytes 493400d0
+ 00588328 bytes 29370090
- 00565494 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00565494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058832c ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 0058832c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058832c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058832c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565494 bytes 29013091
+ 0058832c bytes 29011f91
- 005654a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 005654a0 bytes 483400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78ee3c17cf872b5c50a8bdada63e6e2b"></a>

### [`0056554c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md) → [`005883e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005883e4.md) _INIT_32

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00560444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560444.md) [`00560474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/00560474.md) [`005604a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604a4.md) [`005604ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005604ac.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005832dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/005832dc.md) [`0058330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058330c.md) [`0058333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058333c.md) [`00583344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/00583344.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件, `store_value` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058840c",
      "incomplete_value": false,
      "site": "0058840c",
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
                "const:ec0:8"
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
      "definition_site": "00565574",
      "incomplete_value": false,
      "site": "00565574",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:400:8"
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
      "definition_site": "00588428",
      "incomplete_value": false,
      "site": "00588428",
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
                "const:ef0:8"
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
      "definition_site": "00565590",
      "incomplete_value": false,
      "site": "00565590",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:430:8"
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
      "definition_site": "00588448",
      "incomplete_value": false,
      "site": "00588448",
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
                "const:f20:8"
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
      "definition_site": "005655b0",
      "incomplete_value": false,
      "site": "005655b0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:460:8"
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
      "005883fc",
      "PARAM",
      [
        "storage",
        "00c26400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0056556c",
      "PARAM",
      [
        "storage",
        "00560444",
        null,
        null
      ]
    ],
    [
      "00588408",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005883fc",
      "PARAM",
      [
        "storage",
        "00ca5ec0",
        null,
        "undefined8"
      ]
    ],
    [
      "00588404",
      "PARAM",
      [
        "storage",
        "005832dc",
        null,
        null
      ]
    ],
    [
      "00588408",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md#insn-00565578) · [`00565594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md#insn-00565594) · [`005655bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/0056554c.md#insn-005655bc)

~~~diff
- 00565578 ["INT_ADD", "register:40f0:8", ["const:565578:8", "const:4:8"]]
- 00565578 ["CALL", null, ["callee:00c57a30:8"]]
- 00565578 bytes 9ad61994
- 00565594 ["INT_ADD", "register:40f0:8", ["const:565594:8", "const:4:8"]]
- 00565594 ["CALL", null, ["callee:00c57a30:8"]]
- 00565594 bytes 93d61994
- 005655bc ["INT_ADD", "register:40f0:8", ["const:5655bc:8", "const:4:8"]]
- 005655bc ["CALL", null, ["callee:00c57a30:8"]]
- 005655bc bytes 89d61994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd20add3a85dc6b205b7afa3e5b199d0"></a>

### [`005655f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md) → [`00588488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md) FUN_00588488

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574724.md) · 呼出先 2件 [`00571a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975bc.md) · 呼出先 2件 [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "005884c0",
      "incomplete_value": false,
      "site": "005884cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565628",
      "incomplete_value": false,
      "site": "00565634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "005884cc",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005884cc",
      "DATA",
      [
        "storage",
        "00c6c810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md#insn-0056561c) · [`00565624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md#insn-00565624) · [`00565628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/005655f0.md#insn-00565628)
- 新版 `005884b4`（命令位置の公開資料なし） · `005884bc`（命令位置の公開資料なし） · `005884c0`（命令位置の公開資料なし）

~~~diff
- 0056561c ["INT_ADD", "register:40f0:8", ["const:56561c:8", "const:4:8"]]
- 0056561c ["CALL", null, ["callee:00c57a90:8"]]
+ 005884b4 ["INT_ADD", "register:40f0:8", ["const:5884b4:8", "const:4:8"]]
+ 005884b4 ["CALL", null, ["callee:00c57a90:8"]]
- 0056561c bytes 89d61994
+ 005884b4 bytes 773d1b94
- 00565624 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005884bc ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00565624 bytes 483400d0
+ 005884bc bytes 28370090
- 00565628 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00565628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005884c0 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005884c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005884c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005884c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565628 bytes 08413191
+ 005884c0 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2beddcacd3bcb2730407920e70bb12"></a>

### [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) → [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) FUN_005885b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00565ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md) · 呼出先 7件 [`00565e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) · 呼出先 7件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005885e8",
      "incomplete_value": false,
      "site": "005885fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565750",
      "incomplete_value": false,
      "site": "00565764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "005885fc",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "undefined *"
      ]
    ],
    [
      "005886cc",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005885fc",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ],
    [
      "005886cc",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md#insn-0056574c) · [`00565750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md#insn-00565750) · [`00565780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md#insn-00565780)
- 新版 `005885e4`（命令位置の公開資料なし） · `005885e8`（命令位置の公開資料なし） · `00588618`（命令位置の公開資料なし）

~~~diff
- 0056574c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005885e4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056574c bytes 483400d0
+ 005885e4 bytes 28370090
- 00565750 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00565750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005885e8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005885e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005885e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005885e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565750 bytes 08813291
+ 005885e8 bytes 08812191
- 00565780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565780 ["INT_ADD", "register:40f0:8", ["const:565780:8", "const:4:8"]]
- 00565780 ["CALLIND", null, ["register:0:8"]]
+ 00588618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588618 ["INT_ADD", "register:40f0:8", ["const:588618:8", "const:4:8"]]
+ 00588618 ["CALLIND", null, ["register:0:8"]]
- 00565780 bytes 00013fd6
+ 00588618 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1a72fa4dd8456a15f13e4184f3dadd7"></a>

### [`00565908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md) → [`005887a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887a0.md) FUN_005887a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "005887b4",
      "incomplete_value": false,
      "site": "005887b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056591c",
      "incomplete_value": false,
      "site": "00565920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "005887b8",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005887b8",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md#insn-00565918) · [`0056591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md#insn-0056591c) · [`00565930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565908.md#insn-00565930)
- 新版 `005887b0`（命令位置の公開資料なし） · `005887b4`（命令位置の公開資料なし） · `005887c8`（命令位置の公開資料なし）

~~~diff
- 00565918 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005887b0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00565918 bytes 483400d0
+ 005887b0 bytes 28370090
- 0056591c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0056591c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005887b4 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005887b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005887b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005887b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056591c bytes 08813291
+ 005887b4 bytes 08812191
- 00565930 ["INT_ADD", "register:40f0:8", ["const:565930:8", "const:4:8"]]
- 00565930 ["CALL", null, ["callee:00c538e0:8"]]
+ 005887c8 ["INT_ADD", "register:40f0:8", ["const:5887c8:8", "const:4:8"]]
+ 005887c8 ["CALL", null, ["callee:00c538e0:8"]]
- 00565930 bytes 58c51994
+ 005887c8 bytes 462c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb08b4e98f04b62a430152ac2d1fb66a"></a>

### [`00565964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565964.md) → [`005887fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005887fc.md) FUN_005887fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00588814",
      "incomplete_value": false,
      "site": "00588818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056597c",
      "incomplete_value": false,
      "site": "00565980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "00588818",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588818",
      "DATA",
      [
        "storage",
        "00c6c860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565964.md#insn-00565978) · [`0056597c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565964.md#insn-0056597c) · [`00565990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565964.md#insn-00565990)
- 新版 `00588810`（命令位置の公開資料なし） · `00588814`（命令位置の公開資料なし） · `00588828`（命令位置の公開資料なし）

~~~diff
- 00565978 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00588810 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00565978 bytes 483400d0
+ 00588810 bytes 28370090
- 0056597c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0056597c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056597c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056597c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588814 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00588814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056597c bytes 08813291
+ 00588814 bytes 08812191
- 00565990 ["INT_ADD", "register:40f0:8", ["const:565990:8", "const:4:8"]]
- 00565990 ["CALL", null, ["callee:00c538e0:8"]]
+ 00588828 ["INT_ADD", "register:40f0:8", ["const:588828:8", "const:4:8"]]
+ 00588828 ["CALL", null, ["callee:00c538e0:8"]]
- 00565990 bytes 40c51994
+ 00588828 bytes 2e2c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a2a0d91de058f0248c3ec3d56094a2c"></a>

### [`00565ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md) → [`00588b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588b80.md) FUN_00588b80

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00565c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565c20.md) [`0057472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057472c.md) · 呼出先 6件 [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) [`00574724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574724.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00588ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588ab8.md) [`005975c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c4.md) · 呼出先 6件 [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) [`005975bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588bd0",
      "incomplete_value": false,
      "site": "00588bdc",
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
    "old": {
      "definition_site": "00565d38",
      "incomplete_value": false,
      "site": "00565d44",
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
            "const:980:8"
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
      "00588bdc",
      "DATA",
      [
        "storage",
        "00bee980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588bdc",
      "DATA",
      [
        "storage",
        "00c6b540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md#insn-00565d1c) · [`00565d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md#insn-00565d2c) · [`00565d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ce8.md#insn-00565d34)
- 新版 `00588bb4`（命令位置の公開資料なし） · `00588bc4`（命令位置の公開資料なし） · `00588bcc`（命令位置の公開資料なし）

~~~diff
- 00565d1c ["INT_ADD", "register:40f0:8", ["const:565d1c:8", "const:4:8"]]
- 00565d1c ["CALL", null, ["callee:005975bc:8"]]
+ 00588bb4 ["INT_ADD", "register:40f0:8", ["const:588bb4:8", "const:4:8"]]
+ 00588bb4 ["CALL", null, ["callee:005975bc:8"]]
- 00565d1c bytes 823a0094
+ 00588bb4 bytes 823a0094
- 00565d2c ["INT_ADD", "register:40f0:8", ["const:565d2c:8", "const:4:8"]]
- 00565d2c ["CALL", null, ["callee:00c57a90:8"]]
+ 00588bc4 ["INT_ADD", "register:40f0:8", ["const:588bc4:8", "const:4:8"]]
+ 00588bc4 ["CALL", null, ["callee:00c57a90:8"]]
- 00565d2c bytes c5d41994
+ 00588bc4 bytes b33b1b94
- 00565d34 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00588bcc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00565d34 bytes 483400b0
+ 00588bcc bytes 083700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99f80ae5b50e1dd72e18fb050a10330"></a>

### [`00565f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f20.md) → [`00588db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md) FUN_00588db8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004183e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183e4.md) · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 1件 [`0043aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aee4.md) · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588dcc",
      "incomplete_value": false,
      "site": "00588dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565f34",
      "incomplete_value": false,
      "site": "00565f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "00588df8",
      "incomplete_value": true,
      "site": "00588df8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00565f60",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588de8",
      "incomplete_value": true,
      "site": "00588df8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565f50",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:490:8"
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
      "00588dcc",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "00588de8",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e04",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00588dcc",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588de8",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e04",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f20.md#insn-00565f38) · [`00565f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f20.md#insn-00565f60) · [`00565f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f20.md#insn-00565f70)
- 新版 `00588dd0`（命令位置の公開資料なし） · `00588df8`（命令位置の公開資料なし） · `00588e08`（命令位置の公開資料なし）

~~~diff
- 00565f38 ["INT_ADD", "register:40f0:8", ["const:565f38:8", "const:4:8"]]
- 00565f38 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00588dd0 ["INT_ADD", "register:40f0:8", ["const:588dd0:8", "const:4:8"]]
+ 00588dd0 ["CALL", null, ["callee:00c59ef0:8"]]
- 00565f38 bytes 5add1994
+ 00588dd0 bytes 48441b94
- 00565f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565f60 ["INT_ADD", "register:40f0:8", ["const:565f60:8", "const:4:8"]]
- 00565f60 ["CALLIND", null, ["register:0:8"]]
+ 00588df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588df8 ["INT_ADD", "register:40f0:8", ["const:588df8:8", "const:4:8"]]
+ 00588df8 ["CALLIND", null, ["register:0:8"]]
- 00565f60 bytes 00013fd6
+ 00588df8 bytes 00013fd6
- 00565f70 ["INT_ADD", "register:40f0:8", ["const:565f70:8", "const:4:8"]]
- 00565f70 ["CALL", null, ["callee:00c57d40:8"]]
+ 00588e08 ["INT_ADD", "register:40f0:8", ["const:588e08:8", "const:4:8"]]
+ 00588e08 ["CALL", null, ["callee:00c57d40:8"]]
- 00565f70 bytes e0d41994
+ 00588e08 bytes ce3b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9f4cf47298ed9bffeb46d7b548998e8"></a>

### [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) → [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) FUN_00588e2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 138件 [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ea94.md) · 呼出先 2件 [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 138件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588e3c",
      "incomplete_value": false,
      "site": "00588e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565fa4",
      "incomplete_value": false,
      "site": "00565fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "00588e68",
      "incomplete_value": true,
      "site": "00588e68",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00565fd0",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588e5c",
      "incomplete_value": true,
      "site": "00588e68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565fc4",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:490:8"
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
      "00588e3c",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "00588e5c",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e74",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00588e3c",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588e5c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e74",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md#insn-00565fa8) · [`00565fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md#insn-00565fd0) · [`00565fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md#insn-00565fe0)
- 新版 `00588e40`（命令位置の公開資料なし） · `00588e68`（命令位置の公開資料なし） · `00588e78`（命令位置の公開資料なし）

~~~diff
- 00565fa8 ["INT_ADD", "register:40f0:8", ["const:565fa8:8", "const:4:8"]]
- 00565fa8 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00588e40 ["INT_ADD", "register:40f0:8", ["const:588e40:8", "const:4:8"]]
+ 00588e40 ["CALL", null, ["callee:00c59ef0:8"]]
- 00565fa8 bytes 3edd1994
+ 00588e40 bytes 2c441b94
- 00565fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00565fd0 ["INT_ADD", "register:40f0:8", ["const:565fd0:8", "const:4:8"]]
- 00565fd0 ["CALLIND", null, ["register:0:8"]]
+ 00588e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588e68 ["INT_ADD", "register:40f0:8", ["const:588e68:8", "const:4:8"]]
+ 00588e68 ["CALLIND", null, ["register:0:8"]]
- 00565fd0 bytes 00013fd6
+ 00588e68 bytes 00013fd6
- 00565fe0 ["INT_ADD", "register:40f0:8", ["const:565fe0:8", "const:4:8"]]
- 00565fe0 ["CALL", null, ["callee:00c57d40:8"]]
+ 00588e78 ["INT_ADD", "register:40f0:8", ["const:588e78:8", "const:4:8"]]
+ 00588e78 ["CALL", null, ["callee:00c57d40:8"]]
- 00565fe0 bytes c4d41994
+ 00588e78 bytes b23b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09c1944a58e65cc0bcf9119f9ec6642"></a>

### [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) → [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) FUN_00588e8c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00565f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f20.md) [`005668b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md) [`0056691c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md) [`00566988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566988.md) [`005673dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md) · 呼出先 3件 [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 11件 [`00588db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588db8.md) [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) [`00589820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589820.md) [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) · 呼出先 3件 [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00588eb8",
      "incomplete_value": false,
      "site": "00588ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566020",
      "incomplete_value": false,
      "site": "00566024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "00588ee4",
      "incomplete_value": true,
      "site": "00588ee4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056604c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588ed4",
      "incomplete_value": true,
      "site": "00588ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056603c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:490:8"
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
      "00588eb8",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "00588ed4",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ],
    [
      "00588ef0",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00588eb8",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00588ed4",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00588ef0",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md#insn-00566024) · [`0056604c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md#insn-0056604c) · [`0056605c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md#insn-0056605c)
- 新版 `00588ebc`（命令位置の公開資料なし） · `00588ee4`（命令位置の公開資料なし） · `00588ef4`（命令位置の公開資料なし）

~~~diff
- 00566024 ["INT_ADD", "register:40f0:8", ["const:566024:8", "const:4:8"]]
- 00566024 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00588ebc ["INT_ADD", "register:40f0:8", ["const:588ebc:8", "const:4:8"]]
+ 00588ebc ["CALL", null, ["callee:00c59ef0:8"]]
- 00566024 bytes 1fdd1994
+ 00588ebc bytes 0d441b94
- 0056604c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056604c ["INT_ADD", "register:40f0:8", ["const:56604c:8", "const:4:8"]]
- 0056604c ["CALLIND", null, ["register:0:8"]]
+ 00588ee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588ee4 ["INT_ADD", "register:40f0:8", ["const:588ee4:8", "const:4:8"]]
+ 00588ee4 ["CALLIND", null, ["register:0:8"]]
- 0056604c bytes 00013fd6
+ 00588ee4 bytes 00013fd6
- 0056605c ["INT_ADD", "register:40f0:8", ["const:56605c:8", "const:4:8"]]
- 0056605c ["CALL", null, ["callee:00c57d40:8"]]
+ 00588ef4 ["INT_ADD", "register:40f0:8", ["const:588ef4:8", "const:4:8"]]
+ 00588ef4 ["CALL", null, ["callee:00c57d40:8"]]
- 0056605c bytes a5d41994
+ 00588ef4 bytes 933b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce3d944dabd4bbf40f4f5c0cd53de9b"></a>

### [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) → [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) FUN_0058911c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 122件 [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ea94.md) · 呼出先 0件 
- 新版 呼出元 122件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00589120",
      "incomplete_value": false,
      "site": "00589124",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566288",
      "incomplete_value": false,
      "site": "0056628c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "00589120",
      "DATA",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589120",
      "DATA",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md#insn-00566284) · [`00566288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md#insn-00566288)
- 新版 `0058911c`（命令位置の公開資料なし） · `00589120`（命令位置の公開資料なし）

~~~diff
- 00566284 ["COPY", "register:4000:8", ["const:c26000:8"]]
+ 0058911c ["COPY", "register:4000:8", ["const:ca5000:8"]]
- 00566284 bytes 00360090
+ 0058911c bytes e0380090
- 00566288 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00566288 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00566288 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00566288 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00589120 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00589120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00589120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00589120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00566288 bytes 00601291
+ 00589120 bytes 00603d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b15b05bc509dc34ca45dc4fd417e60"></a>

### [`00566290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566290.md) → [`00589128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589128.md) FUN_00589128

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056a298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056a/0056a298.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589134",
      "incomplete_value": false,
      "site": "00589134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056629c",
      "incomplete_value": false,
      "site": "0056629c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589134",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589134",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566290.md#insn-00566290) · [`00566294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566290.md#insn-00566294)
- 新版 `00589128`（命令位置の公開資料なし） · `0058912c`（命令位置の公開資料なし）

~~~diff
- 00566290 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00589128 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00566290 bytes 483400b0
+ 00589128 bytes 083700f0
- 00566294 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00566294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058912c ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058912c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058912c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058912c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566294 bytes 08a13491
+ 0058912c bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1285877b0ed03e7c1dc13948381889a4"></a>

### [`005662b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md) → [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md) FUN_00589150

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00567388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567388.md) · 呼出先 4件 [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0058a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md) · 呼出先 4件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589180",
      "incomplete_value": false,
      "site": "00589180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005662e8",
      "incomplete_value": false,
      "site": "005662e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589180",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589180",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005662e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md#insn-005662e0) · [`005662e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md#insn-005662e4) · [`0056630c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md#insn-0056630c)
- 新版 `00589178`（命令位置の公開資料なし） · `0058917c`（命令位置の公開資料なし） · `005891a4`（命令位置の公開資料なし）

~~~diff
- 005662e0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00589178 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005662e0 bytes 483400b0
+ 00589178 bytes 083700f0
- 005662e4 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005662e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005662e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005662e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058917c ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058917c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058917c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058917c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005662e4 bytes 08a13491
+ 0058917c bytes 08a12391
- 0056630c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056630c ["INT_ADD", "register:40f0:8", ["const:56630c:8", "const:4:8"]]
- 0056630c ["CALLIND", null, ["register:0:8"]]
+ 005891a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005891a4 ["INT_ADD", "register:40f0:8", ["const:5891a4:8", "const:4:8"]]
+ 005891a4 ["CALLIND", null, ["register:0:8"]]
- 0056630c bytes 00013fd6
+ 005891a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91dc730c8ef39700b5dc2879fcf02ab1"></a>

### [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) → [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) FUN_005892e0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 130件 [`004747cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ea94.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00567ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ad4.md) [`00567bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567bfc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 130件 [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`005717c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717c0.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0058a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a96c.md) [`0058aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aa94.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005893d0",
      "incomplete_value": false,
      "site": "005893d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566538",
      "incomplete_value": false,
      "site": "0056653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "005893f4",
      "incomplete_value": false,
      "site": "005893f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056655c",
      "incomplete_value": false,
      "site": "00566560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00589420",
      "incomplete_value": true,
      "site": "00589420",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00566588",
      "incomplete_value": true,
      "site": "00566588",
      "value": [
        "LOAD",
        "8",
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
      "005893d0",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "005893f4",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "0058940c",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005893d0",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "005893f4",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058940c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056653c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md#insn-0056653c) · [`00566560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md#insn-00566560) · [`00566588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md#insn-00566588)
- 新版 `005893d4`（命令位置の公開資料なし） · `005893f8`（命令位置の公開資料なし） · `00589420`（命令位置の公開資料なし）

~~~diff
- 0056653c ["INT_ADD", "register:40f0:8", ["const:56653c:8", "const:4:8"]]
- 0056653c ["CALL", null, ["callee:00c59ef0:8"]]
+ 005893d4 ["INT_ADD", "register:40f0:8", ["const:5893d4:8", "const:4:8"]]
+ 005893d4 ["CALL", null, ["callee:00c59ef0:8"]]
- 0056653c bytes d9db1994
+ 005893d4 bytes c7421b94
- 00566560 ["INT_ADD", "register:40f0:8", ["const:566560:8", "const:4:8"]]
- 00566560 ["CALL", null, ["callee:00c59ef0:8"]]
+ 005893f8 ["INT_ADD", "register:40f0:8", ["const:5893f8:8", "const:4:8"]]
+ 005893f8 ["CALL", null, ["callee:00c59ef0:8"]]
- 00566560 bytes d0db1994
+ 005893f8 bytes be421b94
- 00566588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00566588 ["INT_ADD", "register:40f0:8", ["const:566588:8", "const:4:8"]]
- 00566588 ["CALLIND", null, ["register:0:8"]]
+ 00589420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589420 ["INT_ADD", "register:40f0:8", ["const:589420:8", "const:4:8"]]
+ 00589420 ["CALLIND", null, ["register:0:8"]]
- 00566588 bytes 00013fd6
+ 00589420 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35617dbfdd4e18c260dfb214e95e4589"></a>

### [`005668b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md) → [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) FUN_00589750

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055b604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md) [`0055b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md) [`0055f0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f0e4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md)
- 新版 呼出元 3件 [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589768",
      "incomplete_value": false,
      "site": "00589768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005668d0",
      "incomplete_value": false,
      "site": "005668d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589768",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589768",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005668c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md#insn-005668c4) · [`005668c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md#insn-005668c8) · [`005668cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005668b8.md#insn-005668cc)
- 新版 `0058975c`（命令位置の公開資料なし） · `00589760`（命令位置の公開資料なし）

~~~diff
- 005668c4 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058975c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005668c4 bytes 483400b0
+ 0058975c bytes 083700f0
- 005668c8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005668c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005668c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005668c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589760 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00589760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005668c8 bytes 08a13491
+ 00589760 bytes 08a12391
- 005668cc ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005668cc bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b8f4e852c8e3861b7f6c3e75a7bca0"></a>

### [`0056691c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md) → [`005897b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005897b4.md) FUN_005897b4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005897c8",
      "incomplete_value": false,
      "site": "005897cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566930",
      "incomplete_value": false,
      "site": "00566934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "005897cc",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005897cc",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056692c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md#insn-0056692c) · [`00566930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md#insn-00566930) · [`00566944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056691c.md#insn-00566944)
- 新版 `005897c4`（命令位置の公開資料なし） · `005897c8`（命令位置の公開資料なし） · `005897dc`（命令位置の公開資料なし）

~~~diff
- 0056692c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005897c4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056692c bytes 483400b0
+ 005897c4 bytes 083700f0
- 00566930 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00566930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005897c8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 005897c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005897c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005897c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566930 bytes 08a13491
+ 005897c8 bytes 08a12391
- 00566944 ["INT_ADD", "register:40f0:8", ["const:566944:8", "const:4:8"]]
- 00566944 ["CALL", null, ["callee:00588e8c:8"]]
+ 005897dc ["INT_ADD", "register:40f0:8", ["const:5897dc:8", "const:4:8"]]
+ 005897dc ["CALL", null, ["callee:00588e8c:8"]]
- 00566944 bytes acfdff97
+ 005897dc bytes acfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab26bcd04dfe4d513caed3e17644b48d"></a>

### [`005669f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669f8.md) → [`00589890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589890.md) FUN_00589890

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md) · 呼出先 0件 
- 新版 呼出元 55件 [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) · 呼出先 0件 

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
      "definition_site": "005898c4",
      "incomplete_value": false,
      "site": "005898c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566a2c",
      "incomplete_value": false,
      "site": "00566a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "005898c4",
      "DATA",
      [
        "storage",
        "00befd48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005898c4",
      "DATA",
      [
        "storage",
        "00c6c908",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669f8.md#insn-00566a24) · [`00566a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669f8.md#insn-00566a28) · [`00566a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005669f8.md#insn-00566a4c)
- 新版 `005898bc`（命令位置の公開資料なし） · `005898c0`（命令位置の公開資料なし） · `005898e4`（命令位置の公開資料なし）

~~~diff
- 00566a24 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 005898bc ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00566a24 bytes 493400b0
+ 005898bc bytes 093700f0
- 00566a28 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00566a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00566a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00566a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005898c0 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 005898c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005898c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005898c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00566a28 bytes 29213591
+ 005898c0 bytes 29212491
- 00566a4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00566a4c ["INT_ADD", "register:40f0:8", ["const:566a4c:8", "const:4:8"]]
- 00566a4c ["CALLIND", null, ["register:0:8"]]
+ 005898e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005898e4 ["INT_ADD", "register:40f0:8", ["const:5898e4:8", "const:4:8"]]
+ 005898e4 ["CALLIND", null, ["register:0:8"]]
- 00566a4c bytes 20013fd6
+ 005898e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2748387ff12bf816769a0cff991f0f21"></a>

### [`00566d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md) → [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) FUN_00589ba8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0055d9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d9b0.md) [`0055f300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md) [`0055f488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f488.md) [`0055f61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f61c.md) [`0055f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f798.md) · 呼出先 0件 
- 新版 呼出元 7件 [`00580848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md) [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) [`00582320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md) [`005824b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md) [`00582630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582630.md) · 呼出先 0件 

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
      "definition_site": "00589bc8",
      "incomplete_value": false,
      "site": "00589bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566d30",
      "incomplete_value": false,
      "site": "00566d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00589bc8",
      "DATA",
      [
        "storage",
        "00befd68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589bc8",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md#insn-00566d28) · [`00566d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md#insn-00566d2c) · [`00566d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566d10.md#insn-00566d50)
- 新版 `00589bc0`（命令位置の公開資料なし） · `00589bc4`（命令位置の公開資料なし） · `00589be8`（命令位置の公開資料なし）

~~~diff
- 00566d28 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00589bc0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00566d28 bytes 483400b0
+ 00589bc0 bytes 083700f0
- 00566d2c ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00566d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589bc4 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00589bc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589bc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589bc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566d2c bytes 08a13591
+ 00589bc4 bytes 08a12491
- 00566d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00566d50 ["INT_ADD", "register:40f0:8", ["const:566d50:8", "const:4:8"]]
- 00566d50 ["CALLIND", null, ["register:0:8"]]
+ 00589be8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589be8 ["INT_ADD", "register:40f0:8", ["const:589be8:8", "const:4:8"]]
+ 00589be8 ["CALLIND", null, ["register:0:8"]]
- 00566d50 bytes 00013fd6
+ 00589be8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24aaf44fd6f76112ad6b8b041d93da7c"></a>

### [`00566dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566dac.md) → [`00589c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c44.md) FUN_00589c44

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) · 呼出先 0件 

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
      "definition_site": "00589c58",
      "incomplete_value": false,
      "site": "00589c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566dc0",
      "incomplete_value": false,
      "site": "00566dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00589c60",
      "DATA",
      [
        "storage",
        "00befd68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589c60",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566dac.md#insn-00566dbc) · [`00566dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566dac.md#insn-00566dc0) · [`00566ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566dac.md#insn-00566ddc)
- 新版 `00589c54`（命令位置の公開資料なし） · `00589c58`（命令位置の公開資料なし） · `00589c74`（命令位置の公開資料なし）

~~~diff
- 00566dbc ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 00589c54 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00566dbc bytes 493400b0
+ 00589c54 bytes 093700f0
- 00566dc0 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00566dc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589c58 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00589c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 bytes 29a13591
+ 00589c58 bytes 29a12491
- 00566ddc ["COPY", "register:0:8", ["register:4040:8"]]
- 00566ddc ["INT_ADD", "register:40f0:8", ["const:566ddc:8", "const:4:8"]]
- 00566ddc ["CALLIND", null, ["register:0:8"]]
+ 00589c74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589c74 ["INT_ADD", "register:40f0:8", ["const:589c74:8", "const:4:8"]]
+ 00589c74 ["CALLIND", null, ["register:0:8"]]
- 00566ddc bytes 00013fd6
+ 00589c74 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0f3b119506f53186ea810f94569085d"></a>

### [`00566df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md) → [`00589c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md) FUN_00589c88

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055f300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) · 呼出先 0件 

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
      "definition_site": "00589ca4",
      "incomplete_value": false,
      "site": "00589ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566e0c",
      "incomplete_value": false,
      "site": "00566e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00589ca4",
      "DATA",
      [
        "storage",
        "00befd68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589ca4",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md#insn-00566e00) · [`00566e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md#insn-00566e04) · [`00566e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566df0.md#insn-00566e3c)
- 新版 `00589c98`（命令位置の公開資料なし） · `00589c9c`（命令位置の公開資料なし） · `00589cd4`（命令位置の公開資料なし）

~~~diff
- 00566e00 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00589c98 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00566e00 bytes 483400b0
+ 00589c98 bytes 083700f0
- 00566e04 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00566e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589c9c ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00589c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566e04 bytes 08a13591
+ 00589c9c bytes 08a12491
- 00566e3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00566e3c ["INT_ADD", "register:40f0:8", ["const:566e3c:8", "const:4:8"]]
- 00566e3c ["CALLIND", null, ["register:0:8"]]
+ 00589cd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589cd4 ["INT_ADD", "register:40f0:8", ["const:589cd4:8", "const:4:8"]]
+ 00589cd4 ["CALLIND", null, ["register:0:8"]]
- 00566e3c bytes 00013fd6
+ 00589cd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1421554effe1f0582a7ebbddc8187a4d"></a>

### [`00567030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567030.md) → [`00589ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ec8.md) FUN_00589ec8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0055d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d1c0.md) [`0055d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055d5cc.md) [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e88c.md) [`0055f300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055f/0055f300.md) · 呼出先 2件 [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 10件 [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) · 呼出先 2件 [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.08% / 新版 86.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589ed8",
      "incomplete_value": false,
      "site": "00589ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567040",
      "incomplete_value": false,
      "site": "00567048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00589ee8",
      "incomplete_value": false,
      "site": "00589eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567050",
      "incomplete_value": false,
      "site": "00567054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "00589f20",
      "incomplete_value": true,
      "site": "00589f20",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00567088",
      "incomplete_value": true,
      "site": "00567088",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00589ee0",
      "DATA",
      [
        "storage",
        "00befd68",
        null,
        "undefined *"
      ]
    ],
    [
      "00589ee8",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "00589f0c",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589ee0",
      "DATA",
      [
        "storage",
        "00c6c928",
        null,
        "undefined *"
      ]
    ],
    [
      "00589ee8",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "00589f0c",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567030.md#insn-00567054) · [`00567088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567030.md#insn-00567088) · [`005670fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567030.md#insn-005670fc)
- 新版 `00589eec`（命令位置の公開資料なし） · `00589f20`（命令位置の公開資料なし） · `00589f94`（命令位置の公開資料なし）

~~~diff
- 00567054 ["INT_ADD", "register:40f0:8", ["const:567054:8", "const:4:8"]]
- 00567054 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00589eec ["INT_ADD", "register:40f0:8", ["const:589eec:8", "const:4:8"]]
+ 00589eec ["CALL", null, ["callee:00c59ef0:8"]]
- 00567054 bytes 13d91994
+ 00589eec bytes 01401b94
- 00567088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00567088 ["INT_ADD", "register:40f0:8", ["const:567088:8", "const:4:8"]]
- 00567088 ["CALLIND", null, ["register:0:8"]]
+ 00589f20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589f20 ["INT_ADD", "register:40f0:8", ["const:589f20:8", "const:4:8"]]
+ 00589f20 ["CALLIND", null, ["register:0:8"]]
- 00567088 bytes 00013fd6
+ 00589f20 bytes 00013fd6
- 005670fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005670fc ["INT_ADD", "register:40f0:8", ["const:5670fc:8", "const:4:8"]]
- 005670fc ["CALLIND", null, ["register:0:8"]]
+ 00589f94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589f94 ["INT_ADD", "register:40f0:8", ["const:589f94:8", "const:4:8"]]
+ 00589f94 ["CALLIND", null, ["register:0:8"]]
- 005670fc bytes 00013fd6
+ 00589f94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15d9cac74024c010bf2fcf47a1f1f70"></a>

### [`00567274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567274.md) → [`0058a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a10c.md) FUN_0058a10c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058a154",
      "incomplete_value": true,
      "site": "0058a154",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005672bc",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a144",
      "incomplete_value": true,
      "site": "0058a154",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005672ac",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:490:8"
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
      "definition_site": "0058a160",
      "incomplete_value": true,
      "site": "0058a164",
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
      "definition_site": "005672c8",
      "incomplete_value": true,
      "site": "005672cc",
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
      "0058a124",
      "PARAM",
      [
        "storage",
        "00c23f18",
        null,
        null
      ]
    ],
    [
      "0058a144",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a160",
      "READ",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058a124",
      "PARAM",
      [
        "storage",
        "00ca3a00",
        null,
        null
      ]
    ],
    [
      "0058a144",
      "READ",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a160",
      "READ",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005672bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567274.md#insn-005672bc) · [`005672cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567274.md#insn-005672cc) · [`00567288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567274.md#insn-00567288)
- 新版 `0058a154`（命令位置の公開資料なし） · `0058a164`（命令位置の公開資料なし） · `0058a120`（命令位置の公開資料なし）

~~~diff
- 005672bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005672bc ["INT_ADD", "register:40f0:8", ["const:5672bc:8", "const:4:8"]]
- 005672bc ["CALLIND", null, ["register:0:8"]]
+ 0058a154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a154 ["INT_ADD", "register:40f0:8", ["const:58a154:8", "const:4:8"]]
+ 0058a154 ["CALLIND", null, ["register:0:8"]]
- 005672bc bytes 00013fd6
+ 0058a154 bytes 00013fd6
- 005672cc ["INT_ADD", "register:40f0:8", ["const:5672cc:8", "const:4:8"]]
- 005672cc ["CALL", null, ["callee:00c57d40:8"]]
+ 0058a164 ["INT_ADD", "register:40f0:8", ["const:58a164:8", "const:4:8"]]
+ 0058a164 ["CALL", null, ["callee:00c57d40:8"]]
- 005672cc bytes 09d01994
+ 0058a164 bytes f7361b94
- 00567288 ["COPY", "register:4000:8", ["const:c23000:8"]]
+ 0058a120 ["COPY", "register:4000:8", ["const:ca3000:8"]]
- 00567288 bytes e0350090
+ 0058a120 bytes c03800b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e2e13e75243ed2f06dd966e0d04dadc"></a>

### [`00567388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567388.md) → [`0058a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a220.md) FUN_0058a220

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 1件 [`005662b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/005662b8.md)
- 新版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 1件 [`00589150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a260",
      "incomplete_value": false,
      "site": "0058a264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005673c8",
      "incomplete_value": false,
      "site": "005673cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "definition_site": "0058a23c",
      "incomplete_value": false,
      "site": "0058a248",
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
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005673a4",
      "incomplete_value": false,
      "site": "005673b0",
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
            "const:bd5:8"
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
      "0058a23c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "0058a264",
      "DATA",
      [
        "storage",
        "00befda0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a23c",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "0058a264",
      "DATA",
      [
        "storage",
        "00c6c960",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005673b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567388.md#insn-005673b0) · [`005673a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567388.md#insn-005673a0) · [`005673a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567388.md#insn-005673a4)
- 新版 `0058a248`（命令位置の公開資料なし） · `0058a238`（命令位置の公開資料なし） · `0058a23c`（命令位置の公開資料なし）

~~~diff
- 005673b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005673b0 ["INT_ADD", "register:40f0:8", ["const:5673b0:8", "const:4:8"]]
- 005673b0 ["CALLIND", null, ["register:0:8"]]
+ 0058a248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a248 ["INT_ADD", "register:40f0:8", ["const:58a248:8", "const:4:8"]]
+ 0058a248 ["CALLIND", null, ["register:0:8"]]
- 005673b0 bytes 00013fd6
+ 0058a248 bytes 00013fd6
- 005673a0 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 0058a238 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 005673a0 bytes 61e9fff0
+ 0058a238 bytes e1e8ff90
- 005673a4 ["COPY", "tmp:0:8", ["const:bd5:8"]]
- 005673a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005673a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005673a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058a23c ["COPY", "tmp:0:8", ["const:70a:8"]]
+ 0058a23c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a23c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a23c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005673a4 bytes 21542f91
+ 0058a23c bytes 21281c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5397943d527489cc15670b4a31a32102"></a>

### [`005673dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md) → [`0058a274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a274.md) FUN_0058a274

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a2dc",
      "incomplete_value": true,
      "site": "0058a2e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567444",
      "incomplete_value": true,
      "site": "0056744c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
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
      "definition_site": "0058a2d8",
      "incomplete_value": true,
      "site": "0058a2e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a28:8"
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
      "definition_site": "0058a2d8",
      "incomplete_value": true,
      "site": "0058a2e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
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
      "0058a2d8",
      "READ",
      [
        "storage",
        "002aca28",
        null,
        "string"
      ]
    ],
    [
      "0058a2d8",
      "READ",
      [
        "storage",
        "002aca38",
        null,
        "string"
      ]
    ],
    [
      "0058a2dc",
      "READ",
      [
        "storage",
        "002b1510",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058a2d8",
      "READ",
      [
        "storage",
        "002bdaa0",
        null,
        "string"
      ]
    ],
    [
      "0058a2d8",
      "READ",
      [
        "storage",
        "002bdab0",
        null,
        "string"
      ]
    ],
    [
      "0058a2dc",
      "READ",
      [
        "storage",
        "002c2b60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md#insn-00567430) · [`00567434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md#insn-00567434) · [`00567438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005673dc.md#insn-00567438)
- 新版 `0058a2c8`（命令位置の公開資料なし） · `0058a2cc`（命令位置の公開資料なし） · `0058a2d0`（命令位置の公開資料なし）

~~~diff
- 00567430 ["INT_ADD", "register:40f0:8", ["const:567430:8", "const:4:8"]]
- 00567430 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058a2c8 ["INT_ADD", "register:40f0:8", ["const:58a2c8:8", "const:4:8"]]
+ 0058a2c8 ["CALL", null, ["callee:00c57a90:8"]]
- 00567430 bytes 04cf1994
+ 0058a2c8 bytes f2351b94
- 00567434 ["COPY", "register:4040:8", ["const:2ac000:8"]]
+ 0058a2cc ["COPY", "register:4040:8", ["const:2bd000:8"]]
- 00567434 bytes 28eaffb0
+ 0058a2cc bytes 88e9fff0
- 00567438 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00567438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a2d0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 0058a2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567438 bytes 08a12891
+ 0058a2d0 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e55820a8f28e59a5f44270c066e0ba"></a>

### [`0056766c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056766c.md) → [`0058a504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a504.md) FUN_0058a504

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0054f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md) [`00555fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md) [`0055828c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md) [`005609d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00561/005612d4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md)
- 新版 呼出元 5件 [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) [`0058386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00583/0058386c.md) [`0058416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00584/0058416c.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a57c",
      "incomplete_value": false,
      "site": "0058a57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005676e4",
      "incomplete_value": false,
      "site": "005676e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "0058a5b4",
      "incomplete_value": false,
      "site": "0058a5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056771c",
      "incomplete_value": false,
      "site": "00567720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a524",
      "incomplete_value": true,
      "site": "0058a534",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056768c",
      "incomplete_value": true,
      "site": "0056769c",
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
            "const:6db:8"
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
      "0058a524",
      "PARAM",
      [
        "storage",
        "0029e6db",
        null,
        "string"
      ]
    ],
    [
      "0058a544",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a57c",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a524",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "0058a544",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a57c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056769c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056766c.md#insn-0056769c) · [`005676b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056766c.md#insn-005676b8) · [`00567688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056766c.md#insn-00567688)
- 新版 `0058a534`（命令位置の公開資料なし） · `0058a550`（命令位置の公開資料なし） · `0058a520`（命令位置の公開資料なし）

~~~diff
- 0056769c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056769c ["INT_ADD", "register:40f0:8", ["const:56769c:8", "const:4:8"]]
- 0056769c ["CALLIND", null, ["register:0:8"]]
+ 0058a534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a534 ["INT_ADD", "register:40f0:8", ["const:58a534:8", "const:4:8"]]
+ 0058a534 ["CALLIND", null, ["register:0:8"]]
- 0056769c bytes 00013fd6
+ 0058a534 bytes 00013fd6
- 005676b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005676b8 ["INT_ADD", "register:40f0:8", ["const:5676b8:8", "const:4:8"]]
- 005676b8 ["CALLIND", null, ["register:0:8"]]
+ 0058a550 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a550 ["INT_ADD", "register:40f0:8", ["const:58a550:8", "const:4:8"]]
+ 0058a550 ["CALLIND", null, ["register:0:8"]]
- 005676b8 bytes 00013fd6
+ 0058a550 bytes 00013fd6
- 00567688 ["COPY", "register:4008:8", ["const:29e000:8"]]
+ 0058a520 ["COPY", "register:4008:8", ["const:2ae000:8"]]
- 00567688 bytes a1e9fff0
+ 0058a520 bytes 21e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f89c1c353d2c7fa95981cdabfd1416"></a>

### [`0056774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md) → [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) FUN_0058a5e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) [`00550fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md)
- 新版 呼出元 3件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 1件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a60c",
      "incomplete_value": true,
      "site": "0058a60c",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567774",
      "incomplete_value": true,
      "site": "00567774",
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
            "const:d28:8"
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
      "definition_site": "0058a634",
      "incomplete_value": false,
      "site": "0058a638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056779c",
      "incomplete_value": false,
      "site": "005677a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "0058a60c",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ],
    [
      "0058a638",
      "DATA",
      [
        "storage",
        "00befdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a60c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a638",
      "DATA",
      [
        "storage",
        "00c6c980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md#insn-00567764) · [`00567768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md#insn-00567768) · [`0056776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md#insn-0056776c)
- 新版 `0058a5fc`（命令位置の公開資料なし） · `0058a600`（命令位置の公開資料なし）

~~~diff
- 00567764 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058a5fc ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00567764 bytes 49340090
+ 0058a5fc bytes 093700d0
- 00567768 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00567768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00567768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00567768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058a600 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058a600 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a600 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a600 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00567768 bytes 29a13491
+ 0058a600 bytes 29a12391
- 0056776c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0056776c bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-678d55b0c915832b6617910203087fe2"></a>

### [`00567918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567918.md) → [`0058a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7b0.md) JNI_OnLoad

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00566234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566234.md) [`00bdd4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005890cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005890cc.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.62% / 新版 84.62%

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
      "definition_site": "0058a7c4",
      "incomplete_value": false,
      "site": "0058a7c4",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056792c",
      "incomplete_value": false,
      "site": "0056792c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "definition_site": "0058a7cc",
      "incomplete_value": false,
      "site": "0058a7d0",
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
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567934",
      "incomplete_value": false,
      "site": "00567938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "0058a7c0",
      "incomplete_value": false,
      "site": "0058a7d0",
      "value": [
        "leaf",
        "const:5890cc:8"
      ]
    },
    "old": {
      "definition_site": "00567928",
      "incomplete_value": false,
      "site": "00567938",
      "value": [
        "leaf",
        "const:566234:8"
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
      "0058a7c0",
      "PARAM",
      [
        "storage",
        "00566234",
        null,
        null
      ]
    ],
    [
      "0058a7c4",
      "WRITE",
      [
        "storage",
        "00c26490",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a7cc",
      "PARAM",
      [
        "storage",
        "00c264d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058a7c0",
      "PARAM",
      [
        "storage",
        "005890cc",
        null,
        null
      ]
    ],
    [
      "0058a7c4",
      "WRITE",
      [
        "storage",
        "00ca5f50",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a7cc",
      "PARAM",
      [
        "storage",
        "00ca5f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567918.md#insn-0056792c) · [`00567938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567918.md#insn-00567938) · [`00567920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567918.md#insn-00567920)
- 新版 `0058a7c4`（命令位置の公開資料なし） · `0058a7d0`（命令位置の公開資料なし） · `0058a7b8`（命令位置の公開資料なし）

~~~diff
- 0056792c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
- 0056792c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0058a7c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0058a7c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0056792c bytes 004902f9
+ 0058a7c4 bytes 00a907f9
- 00567938 ["INT_ADD", "register:40f0:8", ["const:567938:8", "const:4:8"]]
- 00567938 ["CALL", null, ["callee:00c59f00:8"]]
+ 0058a7d0 ["INT_ADD", "register:40f0:8", ["const:58a7d0:8", "const:4:8"]]
+ 0058a7d0 ["CALL", null, ["callee:00c59f00:8"]]
- 00567938 bytes ded61994
+ 0058a7d0 bytes cc3d1b94
- 00567920 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0058a7b8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00567920 bytes e83500f0
+ 0058a7b8 bytes c83800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e6b6bce4f81a7744e0c74406ea7bfa6"></a>

### [`0056794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056794c.md) → [`0058a7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a7e4.md) FUN_0058a7e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a7f8",
      "incomplete_value": false,
      "site": "0058a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567960",
      "incomplete_value": false,
      "site": "00567964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0058a7fc",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a7fc",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056794c.md#insn-0056795c) · [`00567960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056794c.md#insn-00567960) · [`00567974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056794c.md#insn-00567974)
- 新版 `0058a7f4`（命令位置の公開資料なし） · `0058a7f8`（命令位置の公開資料なし） · `0058a80c`（命令位置の公開資料なし）

~~~diff
- 0056795c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058a7f4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056795c bytes 48340090
+ 0058a7f4 bytes 083700d0
- 00567960 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00567960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a7f8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567960 bytes 08a13491
+ 0058a7f8 bytes 08a12391
- 00567974 ["INT_ADD", "register:40f0:8", ["const:567974:8", "const:4:8"]]
- 00567974 ["CALL", null, ["callee:00588e8c:8"]]
+ 0058a80c ["INT_ADD", "register:40f0:8", ["const:58a80c:8", "const:4:8"]]
+ 0058a80c ["CALL", null, ["callee:00588e8c:8"]]
- 00567974 bytes a0f9ff97
+ 0058a80c bytes a0f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b0a2bea68a72943bc7d8147472a434"></a>

### [`00567998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567998.md) → [`0058a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a830.md) FUN_0058a830

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a844",
      "incomplete_value": false,
      "site": "0058a848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005679ac",
      "incomplete_value": false,
      "site": "005679b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0058a848",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a848",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005679a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567998.md#insn-005679a8) · [`005679ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567998.md#insn-005679ac) · [`005679c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567998.md#insn-005679c0)
- 新版 `0058a840`（命令位置の公開資料なし） · `0058a844`（命令位置の公開資料なし） · `0058a858`（命令位置の公開資料なし）

~~~diff
- 005679a8 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058a840 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005679a8 bytes 48340090
+ 0058a840 bytes 083700d0
- 005679ac ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005679ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005679ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005679ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a844 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058a844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005679ac bytes 08a13491
+ 0058a844 bytes 08a12391
- 005679c0 ["INT_ADD", "register:40f0:8", ["const:5679c0:8", "const:4:8"]]
- 005679c0 ["CALL", null, ["callee:00588e8c:8"]]
+ 0058a858 ["INT_ADD", "register:40f0:8", ["const:58a858:8", "const:4:8"]]
+ 0058a858 ["CALL", null, ["callee:00588e8c:8"]]
- 005679c0 bytes 8df9ff97
+ 0058a858 bytes 8df9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a20604e26a170bc9d64a7bcf7751f1"></a>

### [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md) → [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) FUN_0058a87c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 65件 [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md) · 呼出先 2件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md)
- 新版 呼出元 65件 [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) · 呼出先 2件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md)

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
      "definition_site": "0058a890",
      "incomplete_value": false,
      "site": "0058a894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005679f8",
      "incomplete_value": false,
      "site": "005679fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0058a894",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a894",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005679f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md#insn-005679f4) · [`005679f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md#insn-005679f8) · [`00567a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md#insn-00567a0c)
- 新版 `0058a88c`（命令位置の公開資料なし） · `0058a890`（命令位置の公開資料なし） · `0058a8a4`（命令位置の公開資料なし）

~~~diff
- 005679f4 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058a88c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005679f4 bytes 48340090
+ 0058a88c bytes 083700d0
- 005679f8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005679f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005679f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005679f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a890 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058a890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005679f8 bytes 08a13491
+ 0058a890 bytes 08a12391
- 00567a0c ["INT_ADD", "register:40f0:8", ["const:567a0c:8", "const:4:8"]]
- 00567a0c ["CALL", null, ["callee:00588e8c:8"]]
+ 0058a8a4 ["INT_ADD", "register:40f0:8", ["const:58a8a4:8", "const:4:8"]]
+ 0058a8a4 ["CALL", null, ["callee:00588e8c:8"]]
- 00567a0c bytes 7af9ff97
+ 0058a8a4 bytes 7af9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53ed452168ddd0f7cd48a57630b1a68"></a>

### [`00567a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a28.md) → [`0058a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a8c0.md) FUN_0058a8c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a74.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e8c.md) [`0058a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a90c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a8d4",
      "incomplete_value": false,
      "site": "0058a8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567a3c",
      "incomplete_value": false,
      "site": "00567a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "0058a8d8",
      "DATA",
      [
        "storage",
        "00befd28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a8d8",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a28.md#insn-00567a38) · [`00567a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a28.md#insn-00567a3c) · [`00567a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567a28.md#insn-00567a50)
- 新版 `0058a8d0`（命令位置の公開資料なし） · `0058a8d4`（命令位置の公開資料なし） · `0058a8e8`（命令位置の公開資料なし）

~~~diff
- 00567a38 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058a8d0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00567a38 bytes 48340090
+ 0058a8d0 bytes 083700d0
- 00567a3c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00567a3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567a3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567a3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0058a8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567a3c bytes 08a13491
+ 0058a8d4 bytes 08a12391
- 00567a50 ["INT_ADD", "register:40f0:8", ["const:567a50:8", "const:4:8"]]
- 00567a50 ["CALL", null, ["callee:00588e8c:8"]]
+ 0058a8e8 ["INT_ADD", "register:40f0:8", ["const:58a8e8:8", "const:4:8"]]
+ 0058a8e8 ["CALL", null, ["callee:00588e8c:8"]]
- 00567a50 bytes 69f9ff97
+ 0058a8e8 bytes 69f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912f62cc3745fdb3d38b659dcace916b"></a>

### [`00567d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d0c.md) → [`0058aba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aba4.md) _INIT_33

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058abbc",
      "incomplete_value": false,
      "site": "0058abbc",
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
                "const:f58:8"
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
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:498:8"
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
      "0058aba8",
      "PARAM",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ],
    [
      "0058abb8",
      "PARAM",
      [
        "storage",
        "005679e4",
        null,
        null
      ]
    ],
    [
      "0058abbc",
      "WRITE",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058aba8",
      "PARAM",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ],
    [
      "0058abb8",
      "PARAM",
      [
        "storage",
        "0058a87c",
        null,
        null
      ]
    ],
    [
      "0058abbc",
      "WRITE",
      [
        "storage",
        "00ca5f58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d0c.md#insn-00567d0c) · [`00567d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d0c.md#insn-00567d10) · [`00567d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d0c.md#insn-00567d14)
- 新版 `0058aba4`（命令位置の公開資料なし） · `0058aba8`（命令位置の公開資料なし） · `0058abac`（命令位置の公開資料なし）

~~~diff
- 00567d0c ["COPY", "register:4008:8", ["const:c26000:8"]]
+ 0058aba4 ["COPY", "register:4008:8", ["const:ca5000:8"]]
- 00567d0c bytes e13500f0
+ 0058aba4 bytes c13800f0
- 00567d10 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00567d10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00567d10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00567d10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058aba8 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0058aba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058aba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058aba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00567d10 bytes 21601291
+ 0058aba8 bytes 21603d91
- 00567d14 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058abac ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00567d14 bytes 48340090
+ 0058abac bytes 083700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f37d11364f71e0dc8d19148b4be467"></a>

### [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) → [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) FUN_0058abe4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00559fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md) [`0055a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md) [`0055af38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af38.md) [`0055dc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055d/0055dc58.md) [`00565720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565720.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`0057ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md) [`0057d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md) [`0057ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057ddd0.md) [`00580af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md) [`005885b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/005885b8.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "0058ac0c",
      "incomplete_value": false,
      "site": "0058ac10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d74",
      "incomplete_value": false,
      "site": "00567d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0058ac10",
      "DATA",
      [
        "storage",
        "00befe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ac10",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md#insn-00567d70) · [`00567d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md#insn-00567d74) · [`00567d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md#insn-00567d8c)
- 新版 `0058ac08`（命令位置の公開資料なし） · `0058ac0c`（命令位置の公開資料なし） · `0058ac24`（命令位置の公開資料なし）

~~~diff
- 00567d70 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058ac08 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00567d70 bytes 48340090
+ 0058ac08 bytes 083700d0
- 00567d74 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00567d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac0c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0058ac0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567d74 bytes 08413991
+ 0058ac0c bytes 08412891
- 00567d8c ["INT_ADD", "register:40f0:8", ["const:567d8c:8", "const:4:8"]]
- 00567d8c ["CALL", null, ["callee:00c57a90:8"]]
+ 0058ac24 ["INT_ADD", "register:40f0:8", ["const:58ac24:8", "const:4:8"]]
+ 0058ac24 ["CALL", null, ["callee:00c57a90:8"]]
- 00567d8c bytes adcc1994
+ 0058ac24 bytes 9b331b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b548da8452eed6a0518f6d1eb4e5c95"></a>

### [`00568674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568674.md) → [`0058b50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b50c.md) FUN_0058b50c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0058b518",
      "incomplete_value": false,
      "site": "0058b51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568680",
      "incomplete_value": false,
      "site": "00568684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0058b51c",
      "DATA",
      [
        "storage",
        "00befe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b51c",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056867c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568674.md#insn-0056867c) · [`00568680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568674.md#insn-00568680)
- 新版 `0058b514`（命令位置の公開資料なし） · `0058b518`（命令位置の公開資料なし）

~~~diff
- 0056867c ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058b514 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056867c bytes 293400f0
+ 0058b514 bytes 093700b0
- 00568680 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00568680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00568680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00568680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b518 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0058b518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00568680 bytes 29413991
+ 0058b518 bytes 29412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f860b1402102b584255e1b385576cb"></a>

### [`00568698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568698.md) → [`0058b530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b530.md) FUN_0058b530

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0058b538",
      "incomplete_value": false,
      "site": "0058b53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005686a0",
      "incomplete_value": false,
      "site": "005686a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0058b53c",
      "DATA",
      [
        "storage",
        "00befe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b53c",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568698.md#insn-0056869c) · [`005686a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568698.md#insn-005686a0) · [`005686c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568698.md#insn-005686c4)
- 新版 `0058b534`（命令位置の公開資料なし） · `0058b538`（命令位置の公開資料なし） · `0058b55c`（命令位置の公開資料なし）

~~~diff
- 0056869c ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058b534 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056869c bytes 293400f0
+ 0058b534 bytes 093700b0
- 005686a0 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 005686a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005686a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005686a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b538 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0058b538 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b538 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b538 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005686a0 bytes 29413991
+ 0058b538 bytes 29412891
- 005686c4 ["INT_ADD", "register:40f0:8", ["const:5686c4:8", "const:4:8"]]
- 005686c4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058b55c ["INT_ADD", "register:40f0:8", ["const:58b55c:8", "const:4:8"]]
+ 0058b55c ["CALL", null, ["callee:00c57ab0:8"]]
- 005686c4 bytes 67ca1994
+ 0058b55c bytes 55311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f18b046942dccd4be647afab817fcae"></a>

### [`005686d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686d8.md) → [`0058b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b570.md) FUN_0058b570

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0058b57c",
      "incomplete_value": false,
      "site": "0058b580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005686e4",
      "incomplete_value": false,
      "site": "005686e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0058b580",
      "DATA",
      [
        "storage",
        "00befe88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b580",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005686e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686d8.md#insn-005686e0) · [`005686e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686d8.md#insn-005686e4)
- 新版 `0058b578`（命令位置の公開資料なし） · `0058b57c`（命令位置の公開資料なし）

~~~diff
- 005686e0 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058b578 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 005686e0 bytes 293400f0
+ 0058b578 bytes 093700b0
- 005686e4 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 005686e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005686e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005686e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b57c ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 0058b57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005686e4 bytes 29213a91
+ 0058b57c bytes 29212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f9eb6f8adbad0675d0d9f6b52c479e"></a>

### [`005686fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686fc.md) → [`0058b594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b594.md) FUN_0058b594

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0058b59c",
      "incomplete_value": false,
      "site": "0058b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568704",
      "incomplete_value": false,
      "site": "00568708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0058b5a0",
      "DATA",
      [
        "storage",
        "00befe88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b5a0",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686fc.md#insn-00568700) · [`00568704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686fc.md#insn-00568704) · [`00568728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005686fc.md#insn-00568728)
- 新版 `0058b598`（命令位置の公開資料なし） · `0058b59c`（命令位置の公開資料なし） · `0058b5c0`（命令位置の公開資料なし）

~~~diff
- 00568700 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0058b598 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00568700 bytes 293400f0
+ 0058b598 bytes 093700b0
- 00568704 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00568704 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00568704 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00568704 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b59c ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 0058b59c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b59c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b59c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00568704 bytes 29213a91
+ 0058b59c bytes 29212991
- 00568728 ["INT_ADD", "register:40f0:8", ["const:568728:8", "const:4:8"]]
- 00568728 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0058b5c0 ["INT_ADD", "register:40f0:8", ["const:58b5c0:8", "const:4:8"]]
+ 0058b5c0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00568728 bytes 4eca1994
+ 0058b5c0 bytes 3c311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81372835bceef292926258218aa9707b"></a>

### [`0056873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md) → [`0058b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b5d4.md) FUN_0058b5d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00567e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567e94.md) [`00567ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md) [`00568064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568064.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 3件 [`0058ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad2c.md) [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) [`0058aefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058aefc.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "0058b5fc",
      "incomplete_value": false,
      "site": "0058b604",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568764",
      "incomplete_value": false,
      "site": "0056876c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "definition_site": "0058b610",
      "incomplete_value": false,
      "site": "0058b610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568778",
      "incomplete_value": false,
      "site": "00568778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0058b604",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ],
    [
      "0058b610",
      "DATA",
      [
        "storage",
        "00befe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b604",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ],
    [
      "0058b610",
      "DATA",
      [
        "storage",
        "00c6ca10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056875c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md#insn-0056875c) · [`00568760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md#insn-00568760) · [`00568764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056873c.md#insn-00568764)
- 新版 `0058b5f4`（命令位置の公開資料なし） · `0058b5f8`（命令位置の公開資料なし） · `0058b5fc`（命令位置の公開資料なし）

~~~diff
- 0056875c ["INT_ADD", "register:40f0:8", ["const:56875c:8", "const:4:8"]]
- 0056875c ["CALL", null, ["callee:00c57a90:8"]]
+ 0058b5f4 ["INT_ADD", "register:40f0:8", ["const:58b5f4:8", "const:4:8"]]
+ 0058b5f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0056875c bytes 39ca1994
+ 0058b5f4 bytes 27311b94
- 00568760 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058b5f8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00568760 bytes 283400f0
+ 0058b5f8 bytes 08370090
- 00568764 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00568764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b5fc ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0058b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568764 bytes 08810a91
+ 0058b5fc bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b3f10deb0837683367933632969151"></a>

### [`0056891c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md) → [`0058b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b7b4.md) FUN_0058b7b4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005682f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/005682f8.md) [`0056839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056839c.md) [`00568510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568510.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 3件 [`0058b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b190.md) [`0058b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b234.md) [`0058b3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b3a8.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "0058b7dc",
      "incomplete_value": false,
      "site": "0058b7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568944",
      "incomplete_value": false,
      "site": "0056894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "0058b7f0",
      "incomplete_value": false,
      "site": "0058b7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568958",
      "incomplete_value": false,
      "site": "00568958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0058b7e4",
      "DATA",
      [
        "storage",
        "00beff28",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b7f0",
      "DATA",
      [
        "storage",
        "00befe88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b7e4",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b7f0",
      "DATA",
      [
        "storage",
        "00c6ca48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056893c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md#insn-0056893c) · [`00568940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md#insn-00568940) · [`00568944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/0056891c.md#insn-00568944)
- 新版 `0058b7d4`（命令位置の公開資料なし） · `0058b7d8`（命令位置の公開資料なし） · `0058b7dc`（命令位置の公開資料なし）

~~~diff
- 0056893c ["INT_ADD", "register:40f0:8", ["const:56893c:8", "const:4:8"]]
- 0056893c ["CALL", null, ["callee:00c57a90:8"]]
+ 0058b7d4 ["INT_ADD", "register:40f0:8", ["const:58b7d4:8", "const:4:8"]]
+ 0058b7d4 ["CALL", null, ["callee:00c57a90:8"]]
- 0056893c bytes c1c91994
+ 0058b7d4 bytes af301b94
- 00568940 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0058b7d8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00568940 bytes 283400f0
+ 0058b7d8 bytes 083700b0
- 00568944 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00568944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b7dc ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0058b7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568944 bytes 08a13c91
+ 0058b7dc bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e8be9e1a8392fafbb4d2f151c6f44df"></a>

### [`00568a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568a6c.md) → [`0058b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058b904.md) FUN_0058b904

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574748.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b958",
      "incomplete_value": true,
      "site": "0058b958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568ac0",
      "incomplete_value": true,
      "site": "00568ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "definition_site": "0058b960",
      "incomplete_value": true,
      "site": "0058b960",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568ac8",
      "incomplete_value": true,
      "site": "00568ac8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b95c",
      "incomplete_value": true,
      "site": "0058b974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568ac4",
      "incomplete_value": true,
      "site": "00568adc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:8cc:8"
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
      "0058b940",
      "READ",
      [
        "storage",
        "002a83c0",
        null,
        "string"
      ]
    ],
    [
      "0058b948",
      "READ",
      [
        "storage",
        "002a83c6",
        null,
        "string"
      ]
    ],
    [
      "0058b95c",
      "READ",
      [
        "storage",
        "002918cc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058b940",
      "READ",
      [
        "storage",
        "002b9062",
        null,
        "string"
      ]
    ],
    [
      "0058b948",
      "READ",
      [
        "storage",
        "002b9068",
        null,
        "string"
      ]
    ],
    [
      "0058b95c",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568a6c.md#insn-00568a90) · [`00568a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568a6c.md#insn-00568a98) · [`00568aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568a6c.md#insn-00568aa0)
- 新版 `0058b928`（命令位置の公開資料なし） · `0058b930`（命令位置の公開資料なし） · `0058b938`（命令位置の公開資料なし）

~~~diff
- 00568a90 ["INT_ADD", "register:40f0:8", ["const:568a90:8", "const:4:8"]]
- 00568a90 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058b928 ["INT_ADD", "register:40f0:8", ["const:58b928:8", "const:4:8"]]
+ 0058b928 ["CALL", null, ["callee:00588e2c:8"]]
- 00568a90 bytes 41f5ff97
+ 0058b928 bytes 41f5ff97
- 00568a98 ["INT_ADD", "register:40f0:8", ["const:568a98:8", "const:4:8"]]
- 00568a98 ["CALL", null, ["callee:0058911c:8"]]
+ 0058b930 ["INT_ADD", "register:40f0:8", ["const:58b930:8", "const:4:8"]]
+ 0058b930 ["CALL", null, ["callee:0058911c:8"]]
- 00568a98 bytes fbf5ff97
+ 0058b930 bytes fbf5ff97
- 00568aa0 ["COPY", "register:4048:8", ["const:2a8000:8"]]
+ 0058b938 ["COPY", "register:4048:8", ["const:2b9000:8"]]
- 00568aa0 bytes 09eaff90
+ 0058b938 bytes 69e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcfd014bef1f557547546ea24686c582"></a>

### [`00568c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568c04.md) → [`0058ba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058ba9c.md) FUN_0058ba9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057474c.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e4.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058baf4",
      "incomplete_value": true,
      "site": "0058baf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568c5c",
      "incomplete_value": true,
      "site": "00568c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b34:8"
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
      "definition_site": "0058bb08",
      "incomplete_value": true,
      "site": "0058bb18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568c70",
      "incomplete_value": true,
      "site": "00568c80",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:8cc:8"
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
      "0058bae4",
      "READ",
      [
        "storage",
        "002adb34",
        null,
        "string"
      ]
    ],
    [
      "0058bb08",
      "READ",
      [
        "storage",
        "002918cc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bae4",
      "READ",
      [
        "storage",
        "002bee5a",
        null,
        "string"
      ]
    ],
    [
      "0058bb08",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568c04.md#insn-00568c28) · [`00568c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568c04.md#insn-00568c30) · [`00568c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568c04.md#insn-00568c44)
- 新版 `0058bac0`（命令位置の公開資料なし） · `0058bac8`（命令位置の公開資料なし） · `0058badc`（命令位置の公開資料なし）

~~~diff
- 00568c28 ["INT_ADD", "register:40f0:8", ["const:568c28:8", "const:4:8"]]
- 00568c28 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058bac0 ["INT_ADD", "register:40f0:8", ["const:58bac0:8", "const:4:8"]]
+ 0058bac0 ["CALL", null, ["callee:00588e2c:8"]]
- 00568c28 bytes dbf4ff97
+ 0058bac0 bytes dbf4ff97
- 00568c30 ["INT_ADD", "register:40f0:8", ["const:568c30:8", "const:4:8"]]
- 00568c30 ["CALL", null, ["callee:0058911c:8"]]
+ 0058bac8 ["INT_ADD", "register:40f0:8", ["const:58bac8:8", "const:4:8"]]
+ 0058bac8 ["CALL", null, ["callee:0058911c:8"]]
- 00568c30 bytes 95f5ff97
+ 0058bac8 bytes 95f5ff97
- 00568c44 ["COPY", "register:4040:8", ["const:2ad000:8"]]
+ 0058badc ["COPY", "register:4040:8", ["const:2be000:8"]]
- 00568c44 bytes 28eaffb0
+ 0058badc bytes 88e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b240b5212e787ae551a71f148821ec0"></a>

### [`00568da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568da0.md) → [`0058bc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bc38.md) FUN_0058bc38

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574750.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e8.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bc8c",
      "incomplete_value": true,
      "site": "0058bc8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:335:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568df4",
      "incomplete_value": true,
      "site": "00568df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:a1f:8"
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
      "definition_site": "0058bca0",
      "incomplete_value": true,
      "site": "0058bca8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00568e08",
      "incomplete_value": true,
      "site": "00568e10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57a:8"
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
      "definition_site": "0058bcac",
      "incomplete_value": true,
      "site": "0058bcac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568e14",
      "incomplete_value": true,
      "site": "00568e14",
      "value": [
        "LOAD",
        "8",
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
      "0058bc80",
      "READ",
      [
        "storage",
        "00294a1f",
        null,
        "string"
      ]
    ],
    [
      "0058bca0",
      "READ",
      [
        "storage",
        "002a357a",
        null,
        "string"
      ]
    ],
    [
      "0058bca4",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bc80",
      "READ",
      [
        "storage",
        "002a4335",
        null,
        "string"
      ]
    ],
    [
      "0058bca0",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "0058bca4",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568da0.md#insn-00568dc4) · [`00568dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568da0.md#insn-00568dcc) · [`00568de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568da0.md#insn-00568de0)
- 新版 `0058bc5c`（命令位置の公開資料なし） · `0058bc64`（命令位置の公開資料なし） · `0058bc78`（命令位置の公開資料なし）

~~~diff
- 00568dc4 ["INT_ADD", "register:40f0:8", ["const:568dc4:8", "const:4:8"]]
- 00568dc4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058bc5c ["INT_ADD", "register:40f0:8", ["const:58bc5c:8", "const:4:8"]]
+ 0058bc5c ["CALL", null, ["callee:00588e2c:8"]]
- 00568dc4 bytes 74f4ff97
+ 0058bc5c bytes 74f4ff97
- 00568dcc ["INT_ADD", "register:40f0:8", ["const:568dcc:8", "const:4:8"]]
- 00568dcc ["CALL", null, ["callee:0058911c:8"]]
+ 0058bc64 ["INT_ADD", "register:40f0:8", ["const:58bc64:8", "const:4:8"]]
+ 0058bc64 ["CALL", null, ["callee:0058911c:8"]]
- 00568dcc bytes 2ef5ff97
+ 0058bc64 bytes 2ef5ff97
- 00568de0 ["COPY", "register:4040:8", ["const:294000:8"]]
+ 0058bc78 ["COPY", "register:4040:8", ["const:2a4000:8"]]
- 00568de0 bytes 68e9ff90
+ 0058bc78 bytes c8e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d8156270a0e4c7b3feb83559cd07ce"></a>

### [`00568f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568f64.md) → [`0058bdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bdfc.md) FUN_0058bdfc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574758.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f0.md) · 呼出先 9件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
      "definition_site": "0058be44",
      "incomplete_value": true,
      "site": "0058be50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568fac",
      "incomplete_value": true,
      "site": "00568fb8",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058be40",
      "incomplete_value": true,
      "site": "0058be58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568fa8",
      "incomplete_value": true,
      "site": "00568fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:968:8"
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
      "definition_site": "0058be5c",
      "incomplete_value": true,
      "site": "0058be6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00568fc4",
      "incomplete_value": true,
      "site": "00568fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c60:8"
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
      "0058be40",
      "READ",
      [
        "storage",
        "00292968",
        null,
        "string"
      ]
    ],
    [
      "0058be44",
      "READ",
      [
        "storage",
        "00292978",
        null,
        "string"
      ]
    ],
    [
      "0058be5c",
      "READ",
      [
        "storage",
        "002b0c60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058be40",
      "READ",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ],
    [
      "0058be44",
      "READ",
      [
        "storage",
        "002a2088",
        null,
        "string"
      ]
    ],
    [
      "0058be5c",
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568f64.md#insn-00568f84) · [`00568f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568f64.md#insn-00568f8c) · [`00568f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00568/00568f64.md#insn-00568f98)
- 新版 `0058be1c`（命令位置の公開資料なし） · `0058be24`（命令位置の公開資料なし） · `0058be30`（命令位置の公開資料なし）

~~~diff
- 00568f84 ["INT_ADD", "register:40f0:8", ["const:568f84:8", "const:4:8"]]
- 00568f84 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058be1c ["INT_ADD", "register:40f0:8", ["const:58be1c:8", "const:4:8"]]
+ 0058be1c ["CALL", null, ["callee:00588e2c:8"]]
- 00568f84 bytes 04f4ff97
+ 0058be1c bytes 04f4ff97
- 00568f8c ["INT_ADD", "register:40f0:8", ["const:568f8c:8", "const:4:8"]]
- 00568f8c ["CALL", null, ["callee:0058911c:8"]]
+ 0058be24 ["INT_ADD", "register:40f0:8", ["const:58be24:8", "const:4:8"]]
+ 0058be24 ["CALL", null, ["callee:0058911c:8"]]
- 00568f8c bytes bef4ff97
+ 0058be24 bytes bef4ff97
- 00568f98 ["INT_ADD", "register:40f0:8", ["const:568f98:8", "const:4:8"]]
- 00568f98 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058be30 ["INT_ADD", "register:40f0:8", ["const:58be30:8", "const:4:8"]]
+ 0058be30 ["CALL", null, ["callee:00c57a90:8"]]
- 00568f98 bytes 2ac81994
+ 0058be30 bytes 182f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf3113cb8134fcf741da10544d7b99a"></a>

### [`005690ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005690ec.md) → [`0058bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058b/0058bf84.md) FUN_0058bf84

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574754.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975ec.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
      "definition_site": "0058bfec",
      "incomplete_value": true,
      "site": "0058bff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00569154",
      "incomplete_value": true,
      "site": "0056915c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57a:8"
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
      "definition_site": "0058bff8",
      "incomplete_value": true,
      "site": "0058bff8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00569160",
      "incomplete_value": true,
      "site": "00569160",
      "value": [
        "LOAD",
        "8",
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
      "0058bfec",
      "READ",
      [
        "storage",
        "002a357a",
        null,
        "string"
      ]
    ],
    [
      "0058bff0",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bfec",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "0058bff0",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005690ec.md#insn-00569110) · [`00569118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005690ec.md#insn-00569118) · [`0056914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005690ec.md#insn-0056914c)
- 新版 `0058bfa8`（命令位置の公開資料なし） · `0058bfb0`（命令位置の公開資料なし） · `0058bfe4`（命令位置の公開資料なし）

~~~diff
- 00569110 ["INT_ADD", "register:40f0:8", ["const:569110:8", "const:4:8"]]
- 00569110 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058bfa8 ["INT_ADD", "register:40f0:8", ["const:58bfa8:8", "const:4:8"]]
+ 0058bfa8 ["CALL", null, ["callee:00588e2c:8"]]
- 00569110 bytes a1f3ff97
+ 0058bfa8 bytes a1f3ff97
- 00569118 ["INT_ADD", "register:40f0:8", ["const:569118:8", "const:4:8"]]
- 00569118 ["CALL", null, ["callee:0058911c:8"]]
+ 0058bfb0 ["INT_ADD", "register:40f0:8", ["const:58bfb0:8", "const:4:8"]]
+ 0058bfb0 ["CALL", null, ["callee:0058911c:8"]]
- 00569118 bytes 5bf4ff97
+ 0058bfb0 bytes 5bf4ff97
- 0056914c ["COPY", "register:4040:8", ["const:2a3000:8"]]
+ 0058bfe4 ["COPY", "register:4040:8", ["const:2b3000:8"]]
- 0056914c bytes c8e9ffd0
+ 0058bfe4 bytes 48e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af1f858822084dedb4924741e6d1043a"></a>

### [`005692b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005692b0.md) → [`0058c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c148.md) FUN_0058c148

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057475c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057475c.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f4.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c184",
      "incomplete_value": true,
      "site": "0058c19c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005692ec",
      "incomplete_value": true,
      "site": "00569304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:77b:8"
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
      "definition_site": "0058c1a0",
      "incomplete_value": true,
      "site": "0058c1ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00569308",
      "incomplete_value": true,
      "site": "00569314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:725:8"
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
      "definition_site": "0058c1b0",
      "incomplete_value": true,
      "site": "0058c1b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00569318",
      "incomplete_value": true,
      "site": "00569318",
      "value": [
        "LOAD",
        "8",
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
      "0058c184",
      "READ",
      [
        "storage",
        "002a077b",
        null,
        "string"
      ]
    ],
    [
      "0058c1a0",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "0058c1a4",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c184",
      "READ",
      [
        "storage",
        "002b0d35",
        null,
        "string"
      ]
    ],
    [
      "0058c1a0",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0058c1a4",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005692d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005692b0.md#insn-005692d4) · [`005692dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005692b0.md#insn-005692dc) · [`005692e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/005692b0.md#insn-005692e4)
- 新版 `0058c16c`（命令位置の公開資料なし） · `0058c174`（命令位置の公開資料なし） · `0058c17c`（命令位置の公開資料なし）

~~~diff
- 005692d4 ["INT_ADD", "register:40f0:8", ["const:5692d4:8", "const:4:8"]]
- 005692d4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058c16c ["INT_ADD", "register:40f0:8", ["const:58c16c:8", "const:4:8"]]
+ 0058c16c ["CALL", null, ["callee:00588e2c:8"]]
- 005692d4 bytes 30f3ff97
+ 0058c16c bytes 30f3ff97
- 005692dc ["INT_ADD", "register:40f0:8", ["const:5692dc:8", "const:4:8"]]
- 005692dc ["CALL", null, ["callee:0058911c:8"]]
+ 0058c174 ["INT_ADD", "register:40f0:8", ["const:58c174:8", "const:4:8"]]
+ 0058c174 ["CALL", null, ["callee:0058911c:8"]]
- 005692dc bytes eaf3ff97
+ 0058c174 bytes eaf3ff97
- 005692e4 ["COPY", "register:4048:8", ["const:2a0000:8"]]
+ 0058c17c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005692e4 bytes a9e9fff0
+ 0058c17c bytes 29e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc0ec3c9867e319ca8f483c2f2681060"></a>

### [`00569418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569418.md) → [`0058c2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c2b0.md) FUN_0058c2b0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00574760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574760.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005975f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975f8.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c300",
      "incomplete_value": true,
      "site": "0058c300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569468",
      "incomplete_value": true,
      "site": "00569468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "0058c2f0",
      "READ",
      [
        "storage",
        "00297c88",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c2f0",
      "READ",
      [
        "storage",
        "002a78e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056943c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569418.md#insn-0056943c) · [`00569444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569418.md#insn-00569444) · [`0056944c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569418.md#insn-0056944c)
- 新版 `0058c2d4`（命令位置の公開資料なし） · `0058c2dc`（命令位置の公開資料なし） · `0058c2e4`（命令位置の公開資料なし）

~~~diff
- 0056943c ["INT_ADD", "register:40f0:8", ["const:56943c:8", "const:4:8"]]
- 0056943c ["CALL", null, ["callee:00588e2c:8"]]
+ 0058c2d4 ["INT_ADD", "register:40f0:8", ["const:58c2d4:8", "const:4:8"]]
+ 0058c2d4 ["CALL", null, ["callee:00588e2c:8"]]
- 0056943c bytes d6f2ff97
+ 0058c2d4 bytes d6f2ff97
- 00569444 ["INT_ADD", "register:40f0:8", ["const:569444:8", "const:4:8"]]
- 00569444 ["CALL", null, ["callee:0058911c:8"]]
+ 0058c2dc ["INT_ADD", "register:40f0:8", ["const:58c2dc:8", "const:4:8"]]
+ 0058c2dc ["CALL", null, ["callee:0058911c:8"]]
- 00569444 bytes 90f3ff97
+ 0058c2dc bytes 90f3ff97
- 0056944c ["COPY", "register:4048:8", ["const:297000:8"]]
+ 0058c2e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0056944c bytes 69e9ffd0
+ 0058c2e4 bytes c9e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2469d87e84ef96f9d8edec94cd89840e"></a>

### [`00569550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569550.md) → [`0058c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c3e8.md) FUN_0058c3e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00574768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574768.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`005596c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005596c4.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00597600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597600.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c55c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
      "definition_site": "0058c410",
      "incomplete_value": false,
      "site": "0058c41c",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569578",
      "incomplete_value": false,
      "site": "00569584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "definition_site": "0058c418",
      "incomplete_value": true,
      "site": "0058c41c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569580",
      "incomplete_value": true,
      "site": "00569584",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
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
      "0058c410",
      "PARAM",
      [
        "storage",
        "00c264d8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c418",
      "READ",
      [
        "storage",
        "00c264e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c420",
      "WRITE",
      [
        "storage",
        "00c264d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c410",
      "PARAM",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c418",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c420",
      "WRITE",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569550.md#insn-00569584) · [`00569568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569550.md#insn-00569568) · [`0056956c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569550.md#insn-0056956c)
- 新版 `0058c41c`（命令位置の公開資料なし） · `0058c400`（命令位置の公開資料なし） · `0058c404`（命令位置の公開資料なし）

~~~diff
- 00569584 ["INT_ADD", "register:40f0:8", ["const:569584:8", "const:4:8"]]
- 00569584 ["CALL", null, ["callee:0057c55c:8"]]
+ 0058c41c ["INT_ADD", "register:40f0:8", ["const:58c41c:8", "const:4:8"]]
+ 0058c41c ["CALL", null, ["callee:0057c55c:8"]]
- 00569584 bytes 50c0ff97
+ 0058c41c bytes 50c0ff97
- 00569568 ["COPY", "register:4098:8", ["const:c26000:8"]]
+ 0058c400 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 00569568 bytes f33500b0
+ 0058c400 bytes d33800b0
- 0056956c ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0056956c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056956c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056956c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058c404 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0058c404 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c404 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c404 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056956c bytes 73621391
+ 0058c404 bytes 73623e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ac56bf5738d81fd0a770a0bc200848b"></a>

### [`0056968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/0056968c.md) → [`0058c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058c524.md) FUN_0058c524

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057476c.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) · 呼出先 12件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c574",
      "incomplete_value": true,
      "site": "0058c574",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:41f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005696dc",
      "incomplete_value": true,
      "site": "005696dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:77c:8"
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
      "definition_site": "0058c5f0",
      "incomplete_value": true,
      "site": "0058c5f0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00569758",
      "incomplete_value": true,
      "site": "00569758",
      "value": [
        "INT_NOTEQUAL",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058c6bc",
      "incomplete_value": false,
      "site": "0058c6c0",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569824",
      "incomplete_value": false,
      "site": "00569828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058c568",
      "READ",
      [
        "storage",
        "002a977c",
        null,
        "string"
      ]
    ],
    [
      "0058c5d8",
      "PARAM",
      [
        "storage",
        "00c264f0",
        null,
        null
      ]
    ],
    [
      "0058c5e8",
      "READ",
      [
        "storage",
        "00c264e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c568",
      "READ",
      [
        "storage",
        "002ba41f",
        null,
        "string"
      ]
    ],
    [
      "0058c5d8",
      "PARAM",
      [
        "storage",
        "00ca5fb0",
        null,
        null
      ]
    ],
    [
      "0058c5e8",
      "READ",
      [
        "storage",
        "00ca5fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/0056968c.md#insn-00569828) · [`005696b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/0056968c.md#insn-005696b4) · [`005696bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/0056968c.md#insn-005696bc)
- 新版 `0058c6c0`（命令位置の公開資料なし） · `0058c54c`（命令位置の公開資料なし） · `0058c554`（命令位置の公開資料なし）

~~~diff
- 00569828 ["INT_ADD", "register:40f0:8", ["const:569828:8", "const:4:8"]]
- 00569828 ["CALL", null, ["callee:00c57cf0:8"]]
+ 0058c6c0 ["INT_ADD", "register:40f0:8", ["const:58c6c0:8", "const:4:8"]]
+ 0058c6c0 ["CALL", null, ["callee:00c57cf0:8"]]
- 00569828 bytes 9ec61994
+ 0058c6c0 bytes 8c2d1b94
- 005696b4 ["INT_ADD", "register:40f0:8", ["const:5696b4:8", "const:4:8"]]
- 005696b4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058c54c ["INT_ADD", "register:40f0:8", ["const:58c54c:8", "const:4:8"]]
+ 0058c54c ["CALL", null, ["callee:00588e2c:8"]]
- 005696b4 bytes 38f2ff97
+ 0058c54c bytes 38f2ff97
- 005696bc ["INT_ADD", "register:40f0:8", ["const:5696bc:8", "const:4:8"]]
- 005696bc ["CALL", null, ["callee:0058911c:8"]]
+ 0058c554 ["INT_ADD", "register:40f0:8", ["const:58c554:8", "const:4:8"]]
+ 0058c554 ["CALL", null, ["callee:0058911c:8"]]
- 005696bc bytes f2f2ff97
+ 0058c554 bytes f2f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

