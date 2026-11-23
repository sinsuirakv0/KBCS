# v16.0.0 → v16.0.1 · 最優先の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-a81dfa4855e3449d1ed3b8d3c95a48f2"></a>

### [`00530b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md) → [`00530b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530b78.md) FUN_00530b78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530bc8",
      "incomplete_value": true,
      "site": "00530bcc",
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
      "definition_site": "00530b88",
      "incomplete_value": true,
      "site": "00530b8c",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530bb0",
      "incomplete_value": true,
      "site": "00530bb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530b70",
      "incomplete_value": true,
      "site": "00530b70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530bec",
      "incomplete_value": true,
      "site": "00530bec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530bac",
      "incomplete_value": true,
      "site": "00530bac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00530ba0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530bc0",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530bcc",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530ba0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530bc0",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530bcc",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530b70) · [`00530bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530bac) · [`00530b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530b60)
- 新版 `00530bb0`（命令位置の公開資料なし） · `00530bec`（命令位置の公開資料なし） · `00530ba0`（命令位置の公開資料なし）

~~~diff
- 00530b70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b70 ["INT_ADD", "register:40f0:8", ["const:530b70:8", "const:4:8"]]
- 00530b70 ["CALLIND", null, ["register:0:8"]]
+ 00530bb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530bb0 ["INT_ADD", "register:40f0:8", ["const:530bb0:8", "const:4:8"]]
+ 00530bb0 ["CALLIND", null, ["register:0:8"]]
- 00530b70 bytes 20013fd6
+ 00530bb0 bytes 20013fd6
- 00530bac ["COPY", "register:0:8", ["register:4048:8"]]
- 00530bac ["INT_ADD", "register:40f0:8", ["const:530bac:8", "const:4:8"]]
- 00530bac ["CALLIND", null, ["register:0:8"]]
+ 00530bec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
+ 00530bec ["CALLIND", null, ["register:0:8"]]
- 00530bac bytes 20013fd6
+ 00530bec bytes 20013fd6
- 00530b60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00530b60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00530ba0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530b60 bytes a99e41f9
+ 00530ba0 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-581e4bf501d01ab964d6926949569f28"></a>

### [`00530c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md) → [`00530c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c7c.md) FUN_00530c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530ccc",
      "incomplete_value": true,
      "site": "00530cd0",
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
      "definition_site": "00530c8c",
      "incomplete_value": true,
      "site": "00530c90",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530cb4",
      "incomplete_value": true,
      "site": "00530cb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530c74",
      "incomplete_value": true,
      "site": "00530c74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530cf0",
      "incomplete_value": true,
      "site": "00530cf0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530cb0",
      "incomplete_value": true,
      "site": "00530cb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00530ca4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530cc4",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530cd0",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530ca4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530cc4",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530cd0",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530c74) · [`00530cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530cb0) · [`00530c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530c64)
- 新版 `00530cb4`（命令位置の公開資料なし） · `00530cf0`（命令位置の公開資料なし） · `00530ca4`（命令位置の公開資料なし）

~~~diff
- 00530c74 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530c74 ["INT_ADD", "register:40f0:8", ["const:530c74:8", "const:4:8"]]
- 00530c74 ["CALLIND", null, ["register:0:8"]]
+ 00530cb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530cb4 ["INT_ADD", "register:40f0:8", ["const:530cb4:8", "const:4:8"]]
+ 00530cb4 ["CALLIND", null, ["register:0:8"]]
- 00530c74 bytes 20013fd6
+ 00530cb4 bytes 20013fd6
- 00530cb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530cb0 ["INT_ADD", "register:40f0:8", ["const:530cb0:8", "const:4:8"]]
- 00530cb0 ["CALLIND", null, ["register:0:8"]]
+ 00530cf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530cf0 ["INT_ADD", "register:40f0:8", ["const:530cf0:8", "const:4:8"]]
+ 00530cf0 ["CALLIND", null, ["register:0:8"]]
- 00530cb0 bytes 20013fd6
+ 00530cf0 bytes 20013fd6
- 00530c64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00530c64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530ca4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00530ca4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530c64 bytes a99e41f9
+ 00530ca4 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-400965683237bd9f07626b83e3733f0a"></a>

### [`00530ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md) → [`00530d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530d20.md) FUN_00530d20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530d70",
      "incomplete_value": true,
      "site": "00530d74",
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
      "definition_site": "00530d30",
      "incomplete_value": true,
      "site": "00530d34",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530d58",
      "incomplete_value": true,
      "site": "00530d58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530d18",
      "incomplete_value": true,
      "site": "00530d18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d94",
      "incomplete_value": true,
      "site": "00530d94",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530d54",
      "incomplete_value": true,
      "site": "00530d54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00530d48",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530d68",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530d74",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530d48",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530d68",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530d74",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530d18) · [`00530d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530d54) · [`00530d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530d08)
- 新版 `00530d58`（命令位置の公開資料なし） · `00530d94`（命令位置の公開資料なし） · `00530d48`（命令位置の公開資料なし）

~~~diff
- 00530d18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d18 ["INT_ADD", "register:40f0:8", ["const:530d18:8", "const:4:8"]]
- 00530d18 ["CALLIND", null, ["register:0:8"]]
+ 00530d58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d58 ["INT_ADD", "register:40f0:8", ["const:530d58:8", "const:4:8"]]
+ 00530d58 ["CALLIND", null, ["register:0:8"]]
- 00530d18 bytes 20013fd6
+ 00530d58 bytes 20013fd6
- 00530d54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d54 ["INT_ADD", "register:40f0:8", ["const:530d54:8", "const:4:8"]]
- 00530d54 ["CALLIND", null, ["register:0:8"]]
+ 00530d94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d94 ["INT_ADD", "register:40f0:8", ["const:530d94:8", "const:4:8"]]
+ 00530d94 ["CALLIND", null, ["register:0:8"]]
- 00530d54 bytes 20013fd6
+ 00530d94 bytes 20013fd6
- 00530d08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00530d08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530d48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00530d48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530d08 bytes a99e41f9
+ 00530d48 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a226fde17a9323900fe6a5225ac8840a"></a>

### [`00530e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md) → [`00530eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530eac.md) FUN_00530eac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530ee4",
      "incomplete_value": true,
      "site": "00530ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530ea4",
      "incomplete_value": true,
      "site": "00530ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:277:8"
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
      "00530ed4",
      "READ",
      [
        "storage",
        "002b7277",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00530ed4",
      "READ",
      [
        "storage",
        "002b72b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530e88) · [`00530eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530eb0) · [`00530ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530ec0)
- 新版 `00530ec8`（命令位置の公開資料なし） · `00530ef0`（命令位置の公開資料なし） · `00530f00`（命令位置の公開資料なし）

~~~diff
- 00530e88 ["COPY", "tmp:0:8", ["const:277:8"]]
- 00530e88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00530e88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00530e88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00530ec8 ["COPY", "tmp:0:8", ["const:2b7:8"]]
+ 00530ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00530ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00530ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00530e88 bytes 29dd0991
+ 00530ec8 bytes 29dd0a91
- 00530eb0 ["INT_ADD", "register:40f0:8", ["const:530eb0:8", "const:4:8"]]
- 00530eb0 ["CALL", null, ["callee:00c58690:8"]]
+ 00530ef0 ["INT_ADD", "register:40f0:8", ["const:530ef0:8", "const:4:8"]]
+ 00530ef0 ["CALL", null, ["callee:00c58690:8"]]
- 00530eb0 bytes f89c1c94
+ 00530ef0 bytes e89d1c94
- 00530ec0 ["INT_ADD", "register:40f0:8", ["const:530ec0:8", "const:4:8"]]
- 00530ec0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00530f00 ["INT_ADD", "register:40f0:8", ["const:530f00:8", "const:4:8"]]
+ 00530f00 ["CALL", null, ["callee:00c57eb0:8"]]
- 00530ec0 bytes fc9a1c94
+ 00530f00 bytes ec9b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c49159b28f796f764255982387cf3153"></a>

### [`00530f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md) → [`00530fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fa4.md) FUN_00530fa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00530fd0",
      "incomplete_value": true,
      "site": "00530fd4",
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
      "definition_site": "00530f90",
      "incomplete_value": true,
      "site": "00530f94",
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
      "00530fc4",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00530fd4",
      "DATA",
      [
        "storage",
        "00c67550",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00530fc4",
      "READ",
      [
        "storage",
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      "00530fd4",
      "DATA",
      [
        "storage",
        "00c67950",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f78) · [`00530f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f7c) · [`00530f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f84)
- 新版 `00530fb8`（命令位置の公開資料なし） · `00530fbc`（命令位置の公開資料なし） · `00530fc4`（命令位置の公開資料なし）

~~~diff
- 00530f78 ["INT_ADD", "register:40f0:8", ["const:530f78:8", "const:4:8"]]
- 00530f78 ["CALL", null, ["callee:00c57e90:8"]]
+ 00530fb8 ["INT_ADD", "register:40f0:8", ["const:530fb8:8", "const:4:8"]]
+ 00530fb8 ["CALL", null, ["callee:00c57e90:8"]]
- 00530f78 bytes c69a1c94
+ 00530fb8 bytes b69b1c94
- 00530f7c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00530fbc ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00530f7c bytes 493b00d0
+ 00530fbc bytes 493b00f0
- 00530f84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
- 00530f84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530fc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:188:8"]]
+ 00530fc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530f84 bytes 29c546f9
+ 00530fc4 bytes 29c540f9
~~~


<a id="compare-733778e4f3809ee5ec316d4d82c6ed14"></a>

### [`00530fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md) → [`00530fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fec.md) FUN_00530fec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531024",
      "incomplete_value": true,
      "site": "00531024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530fe4",
      "incomplete_value": true,
      "site": "00530fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79d:8"
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
      "00531014",
      "READ",
      [
        "storage",
        "002ae79d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531014",
      "READ",
      [
        "storage",
        "002ae7dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00530fc8) · [`00530ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00530ff0) · [`00531000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00531000)
- 新版 `00531008`（命令位置の公開資料なし） · `00531030`（命令位置の公開資料なし） · `00531040`（命令位置の公開資料なし）

~~~diff
- 00530fc8 ["COPY", "tmp:0:8", ["const:79d:8"]]
- 00530fc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00530fc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00530fc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531008 ["COPY", "tmp:0:8", ["const:7dd:8"]]
+ 00531008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00530fc8 bytes 29751e91
+ 00531008 bytes 29751f91
- 00530ff0 ["INT_ADD", "register:40f0:8", ["const:530ff0:8", "const:4:8"]]
- 00530ff0 ["CALL", null, ["callee:00c58690:8"]]
+ 00531030 ["INT_ADD", "register:40f0:8", ["const:531030:8", "const:4:8"]]
+ 00531030 ["CALL", null, ["callee:00c58690:8"]]
- 00530ff0 bytes a89c1c94
+ 00531030 bytes 989d1c94
- 00531000 ["INT_ADD", "register:40f0:8", ["const:531000:8", "const:4:8"]]
- 00531000 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531040 ["INT_ADD", "register:40f0:8", ["const:531040:8", "const:4:8"]]
+ 00531040 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531000 bytes ac9a1c94
+ 00531040 bytes 9c9b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cfc8aacde700be36b9b3f9d57b82c11"></a>

### [`00531054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md) → [`00531094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531094.md) FUN_00531094

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005310b0",
      "incomplete_value": true,
      "site": "005310b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531070",
      "incomplete_value": true,
      "site": "00531070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8d:8"
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
      "definition_site": "005310a8",
      "incomplete_value": true,
      "site": "005310b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00531068",
      "incomplete_value": true,
      "site": "00531074",
      "value": [
        "LOAD",
        "8",
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
      "005310a0",
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "005310a8",
      "READ",
      [
        "storage",
        "002a9a94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005310a0",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "005310a8",
      "READ",
      [
        "storage",
        "002a9b61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053105c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md#insn-0053105c)
- 新版 `0053109c`（命令位置の公開資料なし）

~~~diff
- 0053105c ["COPY", "tmp:0:8", ["const:a8d:8"]]
- 0053105c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053105c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053105c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053109c ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 0053109c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053109c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053109c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053105c bytes 4a352a91
+ 0053109c bytes 4a692d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb82351af212c57098bc1544c0b9e9a"></a>

### [`005310cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md) → [`0053110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053110c.md) FUN_0053110c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531144",
      "incomplete_value": true,
      "site": "00531144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531104",
      "incomplete_value": true,
      "site": "00531104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccb:8"
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
      "00531134",
      "READ",
      [
        "storage",
        "002b4ccb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531134",
      "READ",
      [
        "storage",
        "002b4d0b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005310e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-005310e8) · [`00531110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-00531110) · [`00531120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-00531120)
- 新版 `00531128`（命令位置の公開資料なし） · `00531150`（命令位置の公開資料なし） · `00531160`（命令位置の公開資料なし）

~~~diff
- 005310e8 ["COPY", "tmp:0:8", ["const:ccb:8"]]
- 005310e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005310e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005310e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531128 ["COPY", "tmp:0:8", ["const:d0b:8"]]
+ 00531128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005310e8 bytes 292d3391
+ 00531128 bytes 292d3491
- 00531110 ["INT_ADD", "register:40f0:8", ["const:531110:8", "const:4:8"]]
- 00531110 ["CALL", null, ["callee:00c58690:8"]]
+ 00531150 ["INT_ADD", "register:40f0:8", ["const:531150:8", "const:4:8"]]
+ 00531150 ["CALL", null, ["callee:00c58690:8"]]
- 00531110 bytes 609c1c94
+ 00531150 bytes 509d1c94
- 00531120 ["INT_ADD", "register:40f0:8", ["const:531120:8", "const:4:8"]]
- 00531120 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531160 ["INT_ADD", "register:40f0:8", ["const:531160:8", "const:4:8"]]
+ 00531160 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531120 bytes 649a1c94
+ 00531160 bytes 549b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af95f832f74619f9183ac4bb786eff9d"></a>

### [`005311c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md) → [`00531204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531204.md) FUN_00531204

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531238",
      "incomplete_value": true,
      "site": "00531244",
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
      "definition_site": "005311f8",
      "incomplete_value": true,
      "site": "00531204",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00531228",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00531244",
      "DATA",
      [
        "storage",
        "00c67628",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531228",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00531244",
      "DATA",
      [
        "storage",
        "00c67a28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005311dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311dc) · [`005311e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311e0) · [`005311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311e8)
- 新版 `0053121c`（命令位置の公開資料なし） · `00531220`（命令位置の公開資料なし） · `00531228`（命令位置の公開資料なし）

~~~diff
- 005311dc ["INT_ADD", "register:40f0:8", ["const:5311dc:8", "const:4:8"]]
- 005311dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0053121c ["INT_ADD", "register:40f0:8", ["const:53121c:8", "const:4:8"]]
+ 0053121c ["CALL", null, ["callee:00c57e90:8"]]
- 005311dc bytes 2d9a1c94
+ 0053121c bytes 1d9b1c94
- 005311e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531220 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005311e0 bytes 483b00b0
+ 00531220 bytes 483b00d0
- 005311e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
- 005311e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531228 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
+ 00531228 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005311e8 bytes 08d946f9
+ 00531228 bytes 08d940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3cd551141fbf2b05a67ee9b312608ab"></a>

### [`005312d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md) → [`00531314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531314.md) FUN_00531314

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053134c",
      "incomplete_value": true,
      "site": "0053134c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:103:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053130c",
      "incomplete_value": true,
      "site": "0053130c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36:8"
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
      "0053133c",
      "READ",
      [
        "storage",
        "002a4036",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053133c",
      "READ",
      [
        "storage",
        "002a4103",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005312f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-005312f0) · [`00531318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-00531318) · [`00531328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-00531328)
- 新版 `00531330`（命令位置の公開資料なし） · `00531358`（命令位置の公開資料なし） · `00531368`（命令位置の公開資料なし）

~~~diff
- 005312f0 ["COPY", "tmp:0:8", ["const:36:8"]]
- 005312f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005312f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005312f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531330 ["COPY", "tmp:0:8", ["const:103:8"]]
+ 00531330 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531330 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531330 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005312f0 bytes 29d90091
+ 00531330 bytes 290d0491
- 00531318 ["INT_ADD", "register:40f0:8", ["const:531318:8", "const:4:8"]]
- 00531318 ["CALL", null, ["callee:00c58690:8"]]
+ 00531358 ["INT_ADD", "register:40f0:8", ["const:531358:8", "const:4:8"]]
+ 00531358 ["CALL", null, ["callee:00c58690:8"]]
- 00531318 bytes de9b1c94
+ 00531358 bytes ce9c1c94
- 00531328 ["INT_ADD", "register:40f0:8", ["const:531328:8", "const:4:8"]]
- 00531328 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531368 ["INT_ADD", "register:40f0:8", ["const:531368:8", "const:4:8"]]
+ 00531368 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531328 bytes e2991c94
+ 00531368 bytes d29a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d497e0057c294a040051406681abe4a"></a>

### [`005313cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md) → [`0053140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053140c.md) FUN_0053140c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531440",
      "incomplete_value": true,
      "site": "0053144c",
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
      "definition_site": "00531400",
      "incomplete_value": true,
      "site": "0053140c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00531430",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      "0053144c",
      "DATA",
      [
        "storage",
        "00c685c0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531430",
      "READ",
      [
        "storage",
        "00c9b190",
        null,
        "pointer"
      ]
    ],
    [
      "0053144c",
      "DATA",
      [
        "storage",
        "00c689c0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005313e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313e4) · [`005313e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313e8) · [`005313f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313f0)
- 新版 `00531424`（命令位置の公開資料なし） · `00531428`（命令位置の公開資料なし） · `00531430`（命令位置の公開資料なし）

~~~diff
- 005313e4 ["INT_ADD", "register:40f0:8", ["const:5313e4:8", "const:4:8"]]
- 005313e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00531424 ["INT_ADD", "register:40f0:8", ["const:531424:8", "const:4:8"]]
+ 00531424 ["CALL", null, ["callee:00c57e90:8"]]
- 005313e4 bytes ab991c94
+ 00531424 bytes 9b9a1c94
- 005313e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531428 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005313e8 bytes 483b00b0
+ 00531428 bytes 483b00d0
- 005313f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
- 005313f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531430 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
+ 00531430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005313f0 bytes 08c946f9
+ 00531430 bytes 08c940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b555b604f3f5794290a0ee835b5ff03"></a>

### [`00531514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md) → [`00531554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531554.md) FUN_00531554

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053158c",
      "incomplete_value": true,
      "site": "0053158c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053154c",
      "incomplete_value": true,
      "site": "0053154c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
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
      "0053157c",
      "READ",
      [
        "storage",
        "002bb2e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053157c",
      "READ",
      [
        "storage",
        "002bb320",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-00531530) · [`00531558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-00531558) · [`00531568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-00531568)
- 新版 `00531570`（命令位置の公開資料なし） · `00531598`（命令位置の公開資料なし） · `005315a8`（命令位置の公開資料なし）

~~~diff
- 00531530 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00531530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531570 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00531570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531530 bytes 29810b91
+ 00531570 bytes 29810c91
- 00531558 ["INT_ADD", "register:40f0:8", ["const:531558:8", "const:4:8"]]
- 00531558 ["CALL", null, ["callee:00c58690:8"]]
+ 00531598 ["INT_ADD", "register:40f0:8", ["const:531598:8", "const:4:8"]]
+ 00531598 ["CALL", null, ["callee:00c58690:8"]]
- 00531558 bytes 4e9b1c94
+ 00531598 bytes 3e9c1c94
- 00531568 ["INT_ADD", "register:40f0:8", ["const:531568:8", "const:4:8"]]
- 00531568 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005315a8 ["INT_ADD", "register:40f0:8", ["const:5315a8:8", "const:4:8"]]
+ 005315a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531568 bytes 52991c94
+ 005315a8 bytes 429a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68dedc07b6c987f9f682bda25d9611e"></a>

### [`0053160c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md) → [`0053164c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053164c.md) FUN_0053164c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00531674",
      "incomplete_value": true,
      "site": "00531674",
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
      "definition_site": "00531634",
      "incomplete_value": true,
      "site": "00531634",
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
      "0053166c",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ],
    [
      "00531674",
      "DATA",
      [
        "storage",
        "00c68650",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0053166c",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "00531674",
      "DATA",
      [
        "storage",
        "00c68a50",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-00531620) · [`00531624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-00531624) · [`0053162c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-0053162c)
- 新版 `00531660`（命令位置の公開資料なし） · `00531664`（命令位置の公開資料なし） · `0053166c`（命令位置の公開資料なし）

~~~diff
- 00531620 ["INT_ADD", "register:40f0:8", ["const:531620:8", "const:4:8"]]
- 00531620 ["CALL", null, ["callee:00c57e90:8"]]
+ 00531660 ["INT_ADD", "register:40f0:8", ["const:531660:8", "const:4:8"]]
+ 00531660 ["CALL", null, ["callee:00c57e90:8"]]
- 00531620 bytes 1c991c94
+ 00531660 bytes 0c9a1c94
- 00531624 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531664 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00531624 bytes 483b00b0
+ 00531664 bytes 483b00d0
- 0053162c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 0053162c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053166c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
+ 0053166c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053162c bytes 08cd46f9
+ 0053166c bytes 08cd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcf245daa508e4a0dc816ac4872a21ed"></a>

### [`005317dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md) → [`0053181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053181c.md) FUN_0053181c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00531844",
      "incomplete_value": true,
      "site": "00531844",
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
      "definition_site": "00531804",
      "incomplete_value": true,
      "site": "00531804",
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
      "0053183c",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "00531844",
      "DATA",
      [
        "storage",
        "00c686c8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0053183c",
      "READ",
      [
        "storage",
        "00c9b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00531844",
      "DATA",
      [
        "storage",
        "00c68ac8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005317f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317f0) · [`005317f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317f4) · [`005317fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317fc)
- 新版 `00531830`（命令位置の公開資料なし） · `00531834`（命令位置の公開資料なし） · `0053183c`（命令位置の公開資料なし）

~~~diff
- 005317f0 ["INT_ADD", "register:40f0:8", ["const:5317f0:8", "const:4:8"]]
- 005317f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00531830 ["INT_ADD", "register:40f0:8", ["const:531830:8", "const:4:8"]]
+ 00531830 ["CALL", null, ["callee:00c57e90:8"]]
- 005317f0 bytes a8981c94
+ 00531830 bytes 98991c94
- 005317f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531834 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005317f4 bytes 483b00b0
+ 00531834 bytes 483b00d0
- 005317fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 005317fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053183c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b8:8"]]
+ 0053183c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005317fc bytes 08dd46f9
+ 0053183c bytes 08dd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b1ea2e5b4b34cde44d8f48dc0955fad"></a>

### [`005318b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md) → [`005318f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318f4.md) FUN_005318f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053192c",
      "incomplete_value": true,
      "site": "0053192c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:417:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005318ec",
      "incomplete_value": true,
      "site": "005318ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3d7:8"
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
      "0053191c",
      "READ",
      [
        "storage",
        "002ab3d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053191c",
      "READ",
      [
        "storage",
        "002ab417",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005318d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-005318d0) · [`005318f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-005318f8) · [`00531908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-00531908)
- 新版 `00531910`（命令位置の公開資料なし） · `00531938`（命令位置の公開資料なし） · `00531948`（命令位置の公開資料なし）

~~~diff
- 005318d0 ["COPY", "tmp:0:8", ["const:3d7:8"]]
- 005318d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005318d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005318d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531910 ["COPY", "tmp:0:8", ["const:417:8"]]
+ 00531910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005318d0 bytes 295d0f91
+ 00531910 bytes 295d1091
- 005318f8 ["INT_ADD", "register:40f0:8", ["const:5318f8:8", "const:4:8"]]
- 005318f8 ["CALL", null, ["callee:00c58690:8"]]
+ 00531938 ["INT_ADD", "register:40f0:8", ["const:531938:8", "const:4:8"]]
+ 00531938 ["CALL", null, ["callee:00c58690:8"]]
- 005318f8 bytes 669a1c94
+ 00531938 bytes 569b1c94
- 00531908 ["INT_ADD", "register:40f0:8", ["const:531908:8", "const:4:8"]]
- 00531908 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531948 ["INT_ADD", "register:40f0:8", ["const:531948:8", "const:4:8"]]
+ 00531948 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531908 bytes 6a981c94
+ 00531948 bytes 5a991c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24407806bf0410314b4ac73c081286fb"></a>

### [`005319ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md) → [`005319ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md) FUN_005319ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00531a38",
      "incomplete_value": true,
      "site": "00531a44",
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
      "definition_site": "005319f8",
      "incomplete_value": true,
      "site": "00531a04",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00531a2c",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00531a44",
      "DATA",
      [
        "storage",
        "00c674f0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531a2c",
      "READ",
      [
        "storage",
        "00c9b180",
        null,
        "pointer"
      ]
    ],
    [
      "00531a44",
      "DATA",
      [
        "storage",
        "00c678f0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-00531a44) · [`005319dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-005319dc) · [`005319e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-005319e0)
- 新版 `00531a84`（命令位置の公開資料なし） · `00531a1c`（命令位置の公開資料なし） · `00531a20`（命令位置の公開資料なし）

~~~diff
- 00531a44 ["INT_ADD", "register:40f0:8", ["const:531a44:8", "const:4:8"]]
- 00531a44 ["CALL", null, ["callee:0053ee70:8"]]
+ 00531a84 ["INT_ADD", "register:40f0:8", ["const:531a84:8", "const:4:8"]]
+ 00531a84 ["CALL", null, ["callee:0053ee70:8"]]
- 00531a44 bytes fb340094
+ 00531a84 bytes fb340094
- 005319dc ["INT_ADD", "register:40f0:8", ["const:5319dc:8", "const:4:8"]]
- 005319dc ["CALL", null, ["callee:00c57e90:8"]]
+ 00531a1c ["INT_ADD", "register:40f0:8", ["const:531a1c:8", "const:4:8"]]
+ 00531a1c ["CALL", null, ["callee:00c57e90:8"]]
- 005319dc bytes 2d981c94
+ 00531a1c bytes 1d991c94
- 005319e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531a20 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005319e0 bytes 483b00b0
+ 00531a20 bytes 483b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b9b8dfb7d301855583c010d2d3c046c"></a>

### [`00531bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md) → [`00531c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531c04.md) FUN_00531c04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531c3c",
      "incomplete_value": true,
      "site": "00531c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531bfc",
      "incomplete_value": true,
      "site": "00531bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
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
      "00531c2c",
      "READ",
      [
        "storage",
        "0029eea0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531c2c",
      "READ",
      [
        "storage",
        "0029ef6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531be0) · [`00531c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531c08) · [`00531c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531c18)
- 新版 `00531c20`（命令位置の公開資料なし） · `00531c48`（命令位置の公開資料なし） · `00531c58`（命令位置の公開資料なし）

~~~diff
- 00531be0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00531be0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531be0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531be0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531c20 ["COPY", "tmp:0:8", ["const:f6d:8"]]
+ 00531c20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531be0 bytes 29813a91
+ 00531c20 bytes 29b53d91
- 00531c08 ["INT_ADD", "register:40f0:8", ["const:531c08:8", "const:4:8"]]
- 00531c08 ["CALL", null, ["callee:00c58690:8"]]
+ 00531c48 ["INT_ADD", "register:40f0:8", ["const:531c48:8", "const:4:8"]]
+ 00531c48 ["CALL", null, ["callee:00c58690:8"]]
- 00531c08 bytes a2991c94
+ 00531c48 bytes 929a1c94
- 00531c18 ["INT_ADD", "register:40f0:8", ["const:531c18:8", "const:4:8"]]
- 00531c18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531c58 ["INT_ADD", "register:40f0:8", ["const:531c58:8", "const:4:8"]]
+ 00531c58 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531c18 bytes a6971c94
+ 00531c58 bytes 96981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a890ed9f7f469463e8cfddbaa10d74"></a>

### [`00531c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md) → [`00531cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cac.md) FUN_00531cac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531cb8",
      "incomplete_value": true,
      "site": "00531cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531c78",
      "incomplete_value": true,
      "site": "00531c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3b3:8"
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
      "definition_site": "00531ccc",
      "incomplete_value": true,
      "site": "00531ccc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00531c8c",
      "incomplete_value": true,
      "site": "00531c8c",
      "value": [
        "LOAD",
        "8",
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
      "00531cb8",
      "READ",
      [
        "storage",
        "002a53b3",
        null,
        "string"
      ]
    ],
    [
      "00531cc0",
      "READ",
      [
        "storage",
        "002a53c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531cb8",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ],
    [
      "00531cc0",
      "READ",
      [
        "storage",
        "002a549d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md#insn-00531c74)
- 新版 `00531cb4`（命令位置の公開資料なし）

~~~diff
- 00531c74 ["COPY", "tmp:0:8", ["const:3b3:8"]]
- 00531c74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00531c74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00531c74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00531cb4 ["COPY", "tmp:0:8", ["const:48f:8"]]
+ 00531cb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00531cb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00531cb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00531c74 bytes 4acd0e91
+ 00531cb4 bytes 4a3d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83123e489898badc1ce80957affc99e8"></a>

### [`00531c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md) → [`00531cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md) FUN_00531cd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00531cfc",
      "incomplete_value": true,
      "site": "00531cfc",
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
      "definition_site": "00531cbc",
      "incomplete_value": true,
      "site": "00531cbc",
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
      "00531cf4",
      "READ",
      [
        "storage",
        "00c9adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00531cfc",
      "DATA",
      [
        "storage",
        "00c68758",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531cf4",
      "READ",
      [
        "storage",
        "00c9b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00531cfc",
      "DATA",
      [
        "storage",
        "00c68b58",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531ca8) · [`00531cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531cac) · [`00531cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531cb4)
- 新版 `00531ce8`（命令位置の公開資料なし） · `00531cec`（命令位置の公開資料なし） · `00531cf4`（命令位置の公開資料なし）

~~~diff
- 00531ca8 ["INT_ADD", "register:40f0:8", ["const:531ca8:8", "const:4:8"]]
- 00531ca8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00531ce8 ["INT_ADD", "register:40f0:8", ["const:531ce8:8", "const:4:8"]]
+ 00531ce8 ["CALL", null, ["callee:00c57e90:8"]]
- 00531ca8 bytes 7a971c94
+ 00531ce8 bytes 6a981c94
- 00531cac ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531cec ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00531cac bytes 483b00b0
+ 00531cec bytes 483b00d0
- 00531cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 00531cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00531cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531cb4 bytes 08e146f9
+ 00531cf4 bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c9b8bdcb1cadb9c877e9db3abfee38a"></a>

### [`00531d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md) → [`00531d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d64.md) FUN_00531d64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531d9c",
      "incomplete_value": true,
      "site": "00531d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:741:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531d5c",
      "incomplete_value": true,
      "site": "00531d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:701:8"
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
      "00531d8c",
      "READ",
      [
        "storage",
        "002ad701",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531d8c",
      "READ",
      [
        "storage",
        "002ad741",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d40) · [`00531d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d68) · [`00531d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d78)
- 新版 `00531d80`（命令位置の公開資料なし） · `00531da8`（命令位置の公開資料なし） · `00531db8`（命令位置の公開資料なし）

~~~diff
- 00531d40 ["COPY", "tmp:0:8", ["const:701:8"]]
- 00531d40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531d40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531d40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531d80 ["COPY", "tmp:0:8", ["const:741:8"]]
+ 00531d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531d40 bytes 29051c91
+ 00531d80 bytes 29051d91
- 00531d68 ["INT_ADD", "register:40f0:8", ["const:531d68:8", "const:4:8"]]
- 00531d68 ["CALL", null, ["callee:00c58690:8"]]
+ 00531da8 ["INT_ADD", "register:40f0:8", ["const:531da8:8", "const:4:8"]]
+ 00531da8 ["CALL", null, ["callee:00c58690:8"]]
- 00531d68 bytes 4a991c94
+ 00531da8 bytes 3a9a1c94
- 00531d78 ["INT_ADD", "register:40f0:8", ["const:531d78:8", "const:4:8"]]
- 00531d78 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531db8 ["INT_ADD", "register:40f0:8", ["const:531db8:8", "const:4:8"]]
+ 00531db8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531d78 bytes 4e971c94
+ 00531db8 bytes 3e981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8788f35582b0ddb02aa073959f42722a"></a>

### [`00531e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md) → [`00531e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md) FUN_00531e5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00531ea8",
      "incomplete_value": true,
      "site": "00531eb4",
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
      "definition_site": "00531e68",
      "incomplete_value": true,
      "site": "00531e74",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00531e9c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00531eb4",
      "DATA",
      [
        "storage",
        "00c687d0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531e9c",
      "READ",
      [
        "storage",
        "00c9b1d0",
        null,
        "pointer"
      ]
    ],
    [
      "00531eb4",
      "DATA",
      [
        "storage",
        "00c68bd0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531eb4) · [`00531e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531e4c) · [`00531e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531e50)
- 新版 `00531ef4`（命令位置の公開資料なし） · `00531e8c`（命令位置の公開資料なし） · `00531e90`（命令位置の公開資料なし）

~~~diff
- 00531eb4 ["INT_ADD", "register:40f0:8", ["const:531eb4:8", "const:4:8"]]
- 00531eb4 ["CALL", null, ["callee:0053ee70:8"]]
+ 00531ef4 ["INT_ADD", "register:40f0:8", ["const:531ef4:8", "const:4:8"]]
+ 00531ef4 ["CALL", null, ["callee:0053ee70:8"]]
- 00531eb4 bytes df330094
+ 00531ef4 bytes df330094
- 00531e4c ["INT_ADD", "register:40f0:8", ["const:531e4c:8", "const:4:8"]]
- 00531e4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00531e8c ["INT_ADD", "register:40f0:8", ["const:531e8c:8", "const:4:8"]]
+ 00531e8c ["CALL", null, ["callee:00c57e90:8"]]
- 00531e4c bytes 11971c94
+ 00531e8c bytes 01981c94
- 00531e50 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00531e90 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00531e50 bytes 483b00b0
+ 00531e90 bytes 483b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cffbb7ad7f474241c3f761a4b6de40c"></a>

### [`00532034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md) → [`00532074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532074.md) FUN_00532074

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053209c",
      "incomplete_value": true,
      "site": "005320ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a97:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053205c",
      "incomplete_value": true,
      "site": "0053206c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a57:8"
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
      "0053209c",
      "READ",
      [
        "storage",
        "002b0a57",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053209c",
      "READ",
      [
        "storage",
        "002b0a97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-00532050) · [`00532078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-00532078) · [`00532088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-00532088)
- 新版 `00532090`（命令位置の公開資料なし） · `005320b8`（命令位置の公開資料なし） · `005320c8`（命令位置の公開資料なし）

~~~diff
- 00532050 ["COPY", "tmp:0:8", ["const:a57:8"]]
- 00532050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532090 ["COPY", "tmp:0:8", ["const:a97:8"]]
+ 00532090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532050 bytes 295d2991
+ 00532090 bytes 295d2a91
- 00532078 ["INT_ADD", "register:40f0:8", ["const:532078:8", "const:4:8"]]
- 00532078 ["CALL", null, ["callee:00c58690:8"]]
+ 005320b8 ["INT_ADD", "register:40f0:8", ["const:5320b8:8", "const:4:8"]]
+ 005320b8 ["CALL", null, ["callee:00c58690:8"]]
- 00532078 bytes 86981c94
+ 005320b8 bytes 76991c94
- 00532088 ["INT_ADD", "register:40f0:8", ["const:532088:8", "const:4:8"]]
- 00532088 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005320c8 ["INT_ADD", "register:40f0:8", ["const:5320c8:8", "const:4:8"]]
+ 005320c8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532088 bytes 8a961c94
+ 005320c8 bytes 7a971c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70023ec5f3e34441f84f9f51a340b934"></a>

### [`0053212c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md) → [`0053216c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md) FUN_0053216c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005321a4",
      "incomplete_value": true,
      "site": "005321a4",
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
      "definition_site": "00532164",
      "incomplete_value": true,
      "site": "00532164",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00532194",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "005321a4",
      "DATA",
      [
        "storage",
        "00c68848",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532194",
      "READ",
      [
        "storage",
        "00c9b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "005321a4",
      "DATA",
      [
        "storage",
        "00c68c48",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532144) · [`00532148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532148) · [`00532154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532154)
- 新版 `00532184`（命令位置の公開資料なし） · `00532188`（命令位置の公開資料なし） · `00532194`（命令位置の公開資料なし）

~~~diff
- 00532144 ["INT_ADD", "register:40f0:8", ["const:532144:8", "const:4:8"]]
- 00532144 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532184 ["INT_ADD", "register:40f0:8", ["const:532184:8", "const:4:8"]]
+ 00532184 ["CALL", null, ["callee:00c57e90:8"]]
- 00532144 bytes 53961c94
+ 00532184 bytes 43971c94
- 00532148 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00532188 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00532148 bytes 493b0090
+ 00532188 bytes 493b00b0
- 00532154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
- 00532154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532194 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
+ 00532194 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00532154 bytes 29ed46f9
+ 00532194 bytes 29ed40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d41fab2fb194e44ba2ef8d0085e4b8"></a>

### [`00532324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md) → [`00532364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532364.md) FUN_00532364

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053239c",
      "incomplete_value": true,
      "site": "0053239c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053235c",
      "incomplete_value": true,
      "site": "0053235c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c5e:8"
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
      "0053238c",
      "READ",
      [
        "storage",
        "002bec5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053238c",
      "READ",
      [
        "storage",
        "002bec9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-00532340) · [`00532368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-00532368) · [`00532378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-00532378)
- 新版 `00532380`（命令位置の公開資料なし） · `005323a8`（命令位置の公開資料なし） · `005323b8`（命令位置の公開資料なし）

~~~diff
- 00532340 ["COPY", "tmp:0:8", ["const:c5e:8"]]
- 00532340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532380 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00532380 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532380 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532380 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532340 bytes 29793191
+ 00532380 bytes 29793291
- 00532368 ["INT_ADD", "register:40f0:8", ["const:532368:8", "const:4:8"]]
- 00532368 ["CALL", null, ["callee:00c58690:8"]]
+ 005323a8 ["INT_ADD", "register:40f0:8", ["const:5323a8:8", "const:4:8"]]
+ 005323a8 ["CALL", null, ["callee:00c58690:8"]]
- 00532368 bytes ca971c94
+ 005323a8 bytes ba981c94
- 00532378 ["INT_ADD", "register:40f0:8", ["const:532378:8", "const:4:8"]]
- 00532378 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005323b8 ["INT_ADD", "register:40f0:8", ["const:5323b8:8", "const:4:8"]]
+ 005323b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532378 bytes ce951c94
+ 005323b8 bytes be961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0459db37c574329a11f0318fa05a755"></a>

### [`005323cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md) → [`0053240c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053240c.md) FUN_0053240c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532418",
      "incomplete_value": true,
      "site": "00532424",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3fc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005323d8",
      "incomplete_value": true,
      "site": "005323e4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3bc:8"
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
      "00532418",
      "READ",
      [
        "storage",
        "002ab3bc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532418",
      "READ",
      [
        "storage",
        "002ab3fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005323d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md#insn-005323d0)
- 新版 `00532410`（命令位置の公開資料なし）

~~~diff
- 005323d0 ["COPY", "tmp:0:8", ["const:3bc:8"]]
- 005323d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005323d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005323d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532410 ["COPY", "tmp:0:8", ["const:3fc:8"]]
+ 00532410 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532410 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532410 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005323d0 bytes 4af10e91
+ 00532410 bytes 4af10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9344e673323de54a0b978ce8a1f47efe"></a>

### [`005323f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md) → [`00532438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532438.md) FUN_00532438

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532470",
      "incomplete_value": true,
      "site": "00532470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532430",
      "incomplete_value": true,
      "site": "00532430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "00532460",
      "READ",
      [
        "storage",
        "002a6498",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532460",
      "READ",
      [
        "storage",
        "002a6574",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-00532414) · [`0053243c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-0053243c) · [`0053244c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-0053244c)
- 新版 `00532454`（命令位置の公開資料なし） · `0053247c`（命令位置の公開資料なし） · `0053248c`（命令位置の公開資料なし）

~~~diff
- 00532414 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00532414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532454 ["COPY", "tmp:0:8", ["const:574:8"]]
+ 00532454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532414 bytes 29611291
+ 00532454 bytes 29d11591
- 0053243c ["INT_ADD", "register:40f0:8", ["const:53243c:8", "const:4:8"]]
- 0053243c ["CALL", null, ["callee:00c58690:8"]]
+ 0053247c ["INT_ADD", "register:40f0:8", ["const:53247c:8", "const:4:8"]]
+ 0053247c ["CALL", null, ["callee:00c58690:8"]]
- 0053243c bytes 95971c94
+ 0053247c bytes 85981c94
- 0053244c ["INT_ADD", "register:40f0:8", ["const:53244c:8", "const:4:8"]]
- 0053244c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053248c ["INT_ADD", "register:40f0:8", ["const:53248c:8", "const:4:8"]]
+ 0053248c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053244c bytes 99951c94
+ 0053248c bytes 89961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a63dfae6fdd7d7053293db4be90a7cc"></a>

### [`005324a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md) → [`005324e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005324e0.md) FUN_005324e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005324ec",
      "incomplete_value": true,
      "site": "005324fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005324ac",
      "incomplete_value": true,
      "site": "005324bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f0d:8"
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
      "005324ec",
      "READ",
      [
        "storage",
        "002b8f0d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005324ec",
      "READ",
      [
        "storage",
        "002b8f4d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005324a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md#insn-005324a4)
- 新版 `005324e4`（命令位置の公開資料なし）

~~~diff
- 005324a4 ["COPY", "tmp:0:8", ["const:f0d:8"]]
- 005324a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005324a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005324a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005324e4 ["COPY", "tmp:0:8", ["const:f4d:8"]]
+ 005324e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005324e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005324e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005324a4 bytes 4a353c91
+ 005324e4 bytes 4a353d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89ec7a4ce09afaa80b47379b7525bc3"></a>

### [`00532518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md) → [`00532558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532558.md) FUN_00532558

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532590",
      "incomplete_value": true,
      "site": "00532590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:789:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532550",
      "incomplete_value": true,
      "site": "00532550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
      "00532580",
      "READ",
      [
        "storage",
        "002a76ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532580",
      "READ",
      [
        "storage",
        "002a7789",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-00532534) · [`0053255c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-0053255c) · [`0053256c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-0053256c)
- 新版 `00532574`（命令位置の公開資料なし） · `0053259c`（命令位置の公開資料なし） · `005325ac`（命令位置の公開資料なし）

~~~diff
- 00532534 ["COPY", "tmp:0:8", ["const:6ad:8"]]
- 00532534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532574 ["COPY", "tmp:0:8", ["const:789:8"]]
+ 00532574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532534 bytes 29b51a91
+ 00532574 bytes 29251e91
- 0053255c ["INT_ADD", "register:40f0:8", ["const:53255c:8", "const:4:8"]]
- 0053255c ["CALL", null, ["callee:00c58690:8"]]
+ 0053259c ["INT_ADD", "register:40f0:8", ["const:53259c:8", "const:4:8"]]
+ 0053259c ["CALL", null, ["callee:00c58690:8"]]
- 0053255c bytes 4d971c94
+ 0053259c bytes 3d981c94
- 0053256c ["INT_ADD", "register:40f0:8", ["const:53256c:8", "const:4:8"]]
- 0053256c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005325ac ["INT_ADD", "register:40f0:8", ["const:5325ac:8", "const:4:8"]]
+ 005325ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0053256c bytes 51951c94
+ 005325ac bytes 41961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7b93be348fae053d1bda51222377109"></a>

### [`00532610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md) → [`00532650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532650.md) FUN_00532650

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fad8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053267c",
      "incomplete_value": true,
      "site": "00532680",
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
      "definition_site": "0053263c",
      "incomplete_value": true,
      "site": "00532640",
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
      "00532670",
      "READ",
      [
        "storage",
        "00c9adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00532680",
      "DATA",
      [
        "storage",
        "00c689b0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532670",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00532680",
      "DATA",
      [
        "storage",
        "00c68db0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532624) · [`00532628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532628) · [`00532630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532630)
- 新版 `00532664`（命令位置の公開資料なし） · `00532668`（命令位置の公開資料なし） · `00532670`（命令位置の公開資料なし）

~~~diff
- 00532624 ["INT_ADD", "register:40f0:8", ["const:532624:8", "const:4:8"]]
- 00532624 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532664 ["INT_ADD", "register:40f0:8", ["const:532664:8", "const:4:8"]]
+ 00532664 ["CALL", null, ["callee:00c57e90:8"]]
- 00532624 bytes 1b951c94
+ 00532664 bytes 0b961c94
- 00532628 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00532668 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00532628 bytes 483b0090
+ 00532668 bytes 483b00b0
- 00532630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
- 00532630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
+ 00532670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00532630 bytes 08e546f9
+ 00532670 bytes 08e540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f7eae21b5bd3fe42550db8bfdde63f2"></a>

### [`00532888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md) → [`005328c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005328c8.md) FUN_005328c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532900",
      "incomplete_value": true,
      "site": "00532900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005328c0",
      "incomplete_value": true,
      "site": "005328c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49d:8"
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
      "005328f0",
      "READ",
      [
        "storage",
        "002bc49d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005328f0",
      "READ",
      [
        "storage",
        "002bc4dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005328a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328a4) · [`005328cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328cc) · [`005328dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328dc)
- 新版 `005328e4`（命令位置の公開資料なし） · `0053290c`（命令位置の公開資料なし） · `0053291c`（命令位置の公開資料なし）

~~~diff
- 005328a4 ["COPY", "tmp:0:8", ["const:49d:8"]]
- 005328a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005328a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005328a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005328e4 ["COPY", "tmp:0:8", ["const:4dd:8"]]
+ 005328e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005328e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005328e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005328a4 bytes 29751291
+ 005328e4 bytes 29751391
- 005328cc ["INT_ADD", "register:40f0:8", ["const:5328cc:8", "const:4:8"]]
- 005328cc ["CALL", null, ["callee:00c58690:8"]]
+ 0053290c ["INT_ADD", "register:40f0:8", ["const:53290c:8", "const:4:8"]]
+ 0053290c ["CALL", null, ["callee:00c58690:8"]]
- 005328cc bytes 71961c94
+ 0053290c bytes 61971c94
- 005328dc ["INT_ADD", "register:40f0:8", ["const:5328dc:8", "const:4:8"]]
- 005328dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053291c ["INT_ADD", "register:40f0:8", ["const:53291c:8", "const:4:8"]]
+ 0053291c ["CALL", null, ["callee:00c57eb0:8"]]
- 005328dc bytes 75941c94
+ 0053291c bytes 65951c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f1753a6ab7e63fa6c8fe248d7bf910"></a>

### [`00532980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md) → [`005329c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005329c0.md) FUN_005329c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005329f0",
      "incomplete_value": false,
      "site": "005329f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c68000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005329b0",
      "incomplete_value": false,
      "site": "005329b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c68000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "definition_site": "005329f0",
      "incomplete_value": true,
      "site": "005329f0",
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
      "definition_site": "005329b0",
      "incomplete_value": true,
      "site": "005329b0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005329e8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "005329f0",
      "DATA",
      [
        "storage",
        "00c68a70",
        null,
        "undefined *"
      ]
    ],
    [
      "005329f0",
      "DATA",
      [
        "storage",
        "00c68a28",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005329e8",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "005329f0",
      "DATA",
      [
        "storage",
        "00c68e70",
        null,
        "undefined *"
      ]
    ],
    [
      "005329f0",
      "DATA",
      [
        "storage",
        "00c68e28",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-00532994) · [`00532998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-00532998) · [`005329a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-005329a4)
- 新版 `005329d4`（命令位置の公開資料なし） · `005329d8`（命令位置の公開資料なし） · `005329e4`（命令位置の公開資料なし）

~~~diff
- 00532994 ["INT_ADD", "register:40f0:8", ["const:532994:8", "const:4:8"]]
- 00532994 ["CALL", null, ["callee:00c57e90:8"]]
+ 005329d4 ["INT_ADD", "register:40f0:8", ["const:5329d4:8", "const:4:8"]]
+ 005329d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00532994 bytes 3f941c94
+ 005329d4 bytes 2f951c94
- 00532998 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005329d8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00532998 bytes 483b0090
+ 005329d8 bytes 483b00b0
- 005329a4 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 005329a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005329a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005329a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005329e4 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 005329e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005329e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005329e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005329a4 bytes 29c12991
+ 005329e4 bytes 29c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca524ba006926f9fd5cb1420df65a9e3"></a>

### [`00532af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md) → [`00532b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532b34.md) FUN_00532b34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532b7c",
      "incomplete_value": true,
      "site": "00532b7c",
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
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00532b7c",
      "incomplete_value": true,
      "site": "00532b7c",
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
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
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
      "00532b60",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00532b64",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00532b7c",
      "DATA",
      [
        "storage",
        "00c68ae8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532b60",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00532b64",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00532b7c",
      "DATA",
      [
        "storage",
        "00c68ee8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b10) · [`00532b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b14) · [`00532b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b20)
- 新版 `00532b50`（命令位置の公開資料なし） · `00532b54`（命令位置の公開資料なし） · `00532b60`（命令位置の公開資料なし）

~~~diff
- 00532b10 ["INT_ADD", "register:40f0:8", ["const:532b10:8", "const:4:8"]]
- 00532b10 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532b50 ["INT_ADD", "register:40f0:8", ["const:532b50:8", "const:4:8"]]
+ 00532b50 ["CALL", null, ["callee:00c57e90:8"]]
- 00532b10 bytes e0931c94
+ 00532b50 bytes d0941c94
- 00532b14 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00532b54 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00532b14 bytes 483b0090
+ 00532b54 bytes 483b00b0
- 00532b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
- 00532b20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532b60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
+ 00532b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00532b20 bytes 08f146f9
+ 00532b60 bytes 08f140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42da2e60100326b59232305b8fe7167"></a>

### [`00532d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d40.md) → [`00532d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md) FUN_00532d80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053fcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053fd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fd18.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00532dac",
      "incomplete_value": false,
      "site": "00532dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532d6c",
      "incomplete_value": false,
      "site": "00532d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00532dac",
      "DATA",
      [
        "storage",
        "00c669b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00532dac",
      "DATA",
      [
        "storage",
        "00c66db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d40.md#insn-00532d58) · [`00532d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d40.md#insn-00532d64) · [`00532d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532d40.md#insn-00532d68)
- 新版 `00532d98`（命令位置の公開資料なし） · `00532da4`（命令位置の公開資料なし）

~~~diff
- 00532d58 ["INT_ADD", "register:40f0:8", ["const:532d58:8", "const:4:8"]]
- 00532d58 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532d98 ["INT_ADD", "register:40f0:8", ["const:532d98:8", "const:4:8"]]
+ 00532d98 ["CALL", null, ["callee:00c57e90:8"]]
- 00532d58 bytes 4e931c94
+ 00532d98 bytes 3e941c94
- 00532d64 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00532d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532da4 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00532da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532d64 bytes 08e12691
+ 00532da4 bytes 08e13691
- 00532d68 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00532d68 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee13bff90e64ddd3e00395ab8643f759"></a>

### [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) → [`00532e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md) FUN_00532e7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00532f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md) · 呼出先 4件 [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00532f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md) · 呼出先 4件 [`004de6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532ee4",
      "incomplete_value": true,
      "site": "00532ee4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532ea4",
      "incomplete_value": true,
      "site": "00532ea4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532f20",
      "incomplete_value": true,
      "site": "00532f20",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532ee0",
      "incomplete_value": true,
      "site": "00532ee0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00532ed4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00532f10",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532ed4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00532f10",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532ea4) · [`00532ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532ee0) · [`00532e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532e94)
- 新版 `00532ee4`（命令位置の公開資料なし） · `00532f20`（命令位置の公開資料なし） · `00532ed4`（命令位置の公開資料なし）

~~~diff
- 00532ea4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532ea4 ["INT_ADD", "register:40f0:8", ["const:532ea4:8", "const:4:8"]]
- 00532ea4 ["CALLIND", null, ["register:0:8"]]
+ 00532ee4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532ee4 ["INT_ADD", "register:40f0:8", ["const:532ee4:8", "const:4:8"]]
+ 00532ee4 ["CALLIND", null, ["register:0:8"]]
- 00532ea4 bytes 20013fd6
+ 00532ee4 bytes 20013fd6
- 00532ee0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532ee0 ["INT_ADD", "register:40f0:8", ["const:532ee0:8", "const:4:8"]]
- 00532ee0 ["CALLIND", null, ["register:0:8"]]
+ 00532f20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532f20 ["INT_ADD", "register:40f0:8", ["const:532f20:8", "const:4:8"]]
+ 00532f20 ["CALLIND", null, ["register:0:8"]]
- 00532ee0 bytes 20013fd6
+ 00532f20 bytes 20013fd6
- 00532e94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00532e94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532ed4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00532ed4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00532e94 bytes a99e41f9
+ 00532ed4 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89d394d423192b65ac6338a13330cec"></a>

### [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) → [`00532fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md) FUN_00532fb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005330ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md) · 呼出先 4件 [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0053312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md) · 呼出先 4件 [`004de6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533020",
      "incomplete_value": true,
      "site": "00533020",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532fe0",
      "incomplete_value": true,
      "site": "00532fe0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533064",
      "incomplete_value": true,
      "site": "00533064",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533024",
      "incomplete_value": true,
      "site": "00533024",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533090",
      "incomplete_value": true,
      "site": "00533090",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533050",
      "incomplete_value": true,
      "site": "00533050",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "00533010",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533054",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533080",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533010",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533054",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533080",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00532fe0) · [`00533024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00533024) · [`00533050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00533050)
- 新版 `00533020`（命令位置の公開資料なし） · `00533064`（命令位置の公開資料なし） · `00533090`（命令位置の公開資料なし）

~~~diff
- 00532fe0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532fe0 ["INT_ADD", "register:40f0:8", ["const:532fe0:8", "const:4:8"]]
- 00532fe0 ["CALLIND", null, ["register:0:8"]]
+ 00533020 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533020 ["INT_ADD", "register:40f0:8", ["const:533020:8", "const:4:8"]]
+ 00533020 ["CALLIND", null, ["register:0:8"]]
- 00532fe0 bytes 20013fd6
+ 00533020 bytes 20013fd6
- 00533024 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533024 ["INT_ADD", "register:40f0:8", ["const:533024:8", "const:4:8"]]
- 00533024 ["CALLIND", null, ["register:0:8"]]
+ 00533064 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533064 ["INT_ADD", "register:40f0:8", ["const:533064:8", "const:4:8"]]
+ 00533064 ["CALLIND", null, ["register:0:8"]]
- 00533024 bytes 20013fd6
+ 00533064 bytes 20013fd6
- 00533050 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533050 ["INT_ADD", "register:40f0:8", ["const:533050:8", "const:4:8"]]
- 00533050 ["CALLIND", null, ["register:0:8"]]
+ 00533090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533090 ["INT_ADD", "register:40f0:8", ["const:533090:8", "const:4:8"]]
+ 00533090 ["CALLIND", null, ["register:0:8"]]
- 00533050 bytes 20013fd6
+ 00533090 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ccae8f5de162720e5f460195c4bde5"></a>

### [`00533420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md) → [`00533460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533460.md) FUN_00533460

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533504",
      "incomplete_value": true,
      "site": "00533504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005334c4",
      "incomplete_value": true,
      "site": "005334c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:caa:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005334a0",
      "incomplete_value": false,
      "site": "005334a8",
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
            "const:e9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533460",
      "incomplete_value": false,
      "site": "00533468",
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
            "const:e5b:8"
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
      "definition_site": "005334b0",
      "incomplete_value": false,
      "site": "005334b8",
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
            "const:332:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533470",
      "incomplete_value": false,
      "site": "00533478",
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
            "const:265:8"
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
      "005334a0",
      "PARAM",
      [
        "storage",
        "002bfe5b",
        null,
        "string"
      ]
    ],
    [
      "005334b0",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "005334f4",
      "READ",
      [
        "storage",
        "002a8caa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005334a0",
      "PARAM",
      [
        "storage",
        "002bfe9b",
        null,
        "string"
      ]
    ],
    [
      "005334b0",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ],
    [
      "005334f4",
      "READ",
      [
        "storage",
        "002a8d77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-00533468) · [`00533478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-00533478) · [`00533460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-00533460)
- 新版 `005334a8`（命令位置の公開資料なし） · `005334b8`（命令位置の公開資料なし） · `005334a0`（命令位置の公開資料なし）

~~~diff
- 00533468 ["INT_ADD", "register:40f0:8", ["const:533468:8", "const:4:8"]]
- 00533468 ["CALL", null, ["callee:00c580b0:8"]]
+ 005334a8 ["INT_ADD", "register:40f0:8", ["const:5334a8:8", "const:4:8"]]
+ 005334a8 ["CALL", null, ["callee:00c580b0:8"]]
- 00533468 bytes 12921c94
+ 005334a8 bytes 02931c94
- 00533478 ["INT_ADD", "register:40f0:8", ["const:533478:8", "const:4:8"]]
- 00533478 ["CALL", null, ["callee:00c57f70:8"]]
+ 005334b8 ["INT_ADD", "register:40f0:8", ["const:5334b8:8", "const:4:8"]]
+ 005334b8 ["CALL", null, ["callee:00c57f70:8"]]
- 00533478 bytes be911c94
+ 005334b8 bytes ae921c94
- 00533460 ["COPY", "tmp:0:8", ["const:e5b:8"]]
- 00533460 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00533460 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00533460 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005334a0 ["COPY", "tmp:0:8", ["const:e9b:8"]]
+ 005334a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005334a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005334a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00533460 bytes 006c3991
+ 005334a0 bytes 006c3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f08937454d2cecb9af251712cc383ec"></a>

### [`0053372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md) → [`0053376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md) FUN_0053376c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005337f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00533838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533838.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005337d4",
      "incomplete_value": true,
      "site": "005337d8",
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
      "definition_site": "00533794",
      "incomplete_value": true,
      "site": "00533798",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005337bc",
      "incomplete_value": true,
      "site": "005337bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053377c",
      "incomplete_value": true,
      "site": "0053377c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533808",
      "incomplete_value": true,
      "site": "00533808",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005337c8",
      "incomplete_value": true,
      "site": "005337c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
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
      "005337ac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005337cc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "005337d8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005337ac",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005337cc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "005337d8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053377c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-0053377c) · [`005337c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-005337c8) · [`00533754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-00533754)
- 新版 `005337bc`（命令位置の公開資料なし） · `00533808`（命令位置の公開資料なし） · `00533794`（命令位置の公開資料なし）

~~~diff
- 0053377c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053377c ["INT_ADD", "register:40f0:8", ["const:53377c:8", "const:4:8"]]
- 0053377c ["CALLIND", null, ["register:0:8"]]
+ 005337bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005337bc ["INT_ADD", "register:40f0:8", ["const:5337bc:8", "const:4:8"]]
+ 005337bc ["CALLIND", null, ["register:0:8"]]
- 0053377c bytes 20013fd6
+ 005337bc bytes 20013fd6
- 005337c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005337c8 ["INT_ADD", "register:40f0:8", ["const:5337c8:8", "const:4:8"]]
- 005337c8 ["CALLIND", null, ["register:0:8"]]
+ 00533808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533808 ["INT_ADD", "register:40f0:8", ["const:533808:8", "const:4:8"]]
+ 00533808 ["CALLIND", null, ["register:0:8"]]
- 005337c8 bytes 20013fd6
+ 00533808 bytes 20013fd6
- 00533754 ["COPY", "register:0:8", ["register:4040:8"]]
- 00533754 ["INT_ADD", "register:40f0:8", ["const:533754:8", "const:4:8"]]
- 00533754 ["CALLIND", null, ["register:0:8"]]
+ 00533794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00533794 ["INT_ADD", "register:40f0:8", ["const:533794:8", "const:4:8"]]
+ 00533794 ["CALLIND", null, ["register:0:8"]]
- 00533754 bytes 00013fd6
+ 00533794 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42997d1552a4328e3acff71a0e072662"></a>

### [`00533870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md) → [`005338b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005338b0.md) FUN_005338b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005338cc",
      "incomplete_value": true,
      "site": "005338d0",
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
      "definition_site": "0053388c",
      "incomplete_value": true,
      "site": "00533890",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533904",
      "incomplete_value": true,
      "site": "00533904",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005338c4",
      "incomplete_value": true,
      "site": "005338c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "005338c4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "005338d0",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005338f4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005338c4",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "005338d0",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005338f4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-00533884) · [`005338c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-005338c4) · [`0053389c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-0053389c)
- 新版 `005338c4`（命令位置の公開資料なし） · `00533904`（命令位置の公開資料なし） · `005338dc`（命令位置の公開資料なし）

~~~diff
- 00533884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00533884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005338c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005338c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00533884 bytes 083945f9
+ 005338c4 bytes 083947f9
- 005338c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005338c4 ["INT_ADD", "register:40f0:8", ["const:5338c4:8", "const:4:8"]]
- 005338c4 ["CALLIND", null, ["register:0:8"]]
+ 00533904 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533904 ["INT_ADD", "register:40f0:8", ["const:533904:8", "const:4:8"]]
+ 00533904 ["CALLIND", null, ["register:0:8"]]
- 005338c4 bytes 20013fd6
+ 00533904 bytes 20013fd6
- 0053389c ["INT_ADD", "register:40f0:8", ["const:53389c:8", "const:4:8"]]
- 0053389c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005338dc ["INT_ADD", "register:40f0:8", ["const:5338dc:8", "const:4:8"]]
+ 005338dc ["CALL", null, ["callee:00c57eb0:8"]]
- 0053389c bytes 85901c94
+ 005338dc bytes 75911c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-516b8bf52adc711a0b9c6afdb5216ff8"></a>

### [`005338f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md) → [`00533930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533930.md) FUN_00533930

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053394c",
      "incomplete_value": true,
      "site": "00533950",
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
      "definition_site": "0053390c",
      "incomplete_value": true,
      "site": "00533910",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533984",
      "incomplete_value": true,
      "site": "00533984",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533944",
      "incomplete_value": true,
      "site": "00533944",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "00533944",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00533950",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533974",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533944",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00533950",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533974",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-00533904) · [`00533944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-00533944) · [`0053391c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-0053391c)
- 新版 `00533944`（命令位置の公開資料なし） · `00533984`（命令位置の公開資料なし） · `0053395c`（命令位置の公開資料なし）

~~~diff
- 00533904 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00533904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533944 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00533944 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00533904 bytes 083945f9
+ 00533944 bytes 083947f9
- 00533944 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533944 ["INT_ADD", "register:40f0:8", ["const:533944:8", "const:4:8"]]
- 00533944 ["CALLIND", null, ["register:0:8"]]
+ 00533984 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533984 ["INT_ADD", "register:40f0:8", ["const:533984:8", "const:4:8"]]
+ 00533984 ["CALLIND", null, ["register:0:8"]]
- 00533944 bytes 20013fd6
+ 00533984 bytes 20013fd6
- 0053391c ["INT_ADD", "register:40f0:8", ["const:53391c:8", "const:4:8"]]
- 0053391c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053395c ["INT_ADD", "register:40f0:8", ["const:53395c:8", "const:4:8"]]
+ 0053395c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053391c bytes 65901c94
+ 0053395c bytes 55911c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba04c71c23f5fb443e8b3b58c7ed17c"></a>

### [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) → [`005339a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md) FUN_005339a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00533a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md) [`00533aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aa4.md) [`00533aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 3件 [`00533ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533ac0.md) [`00533ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533ae4.md) [`00533aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533aec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533a1c",
      "incomplete_value": true,
      "site": "00533a20",
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
      "definition_site": "005339dc",
      "incomplete_value": true,
      "site": "005339e0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00533a58",
      "incomplete_value": true,
      "site": "00533a5c",
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
      "definition_site": "00533a18",
      "incomplete_value": true,
      "site": "00533a1c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005339dc",
      "incomplete_value": true,
      "site": "005339dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053399c",
      "incomplete_value": true,
      "site": "0053399c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "005339cc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533a14",
      "READ",
      [
        "storage",
        "00c9aaa0",
        null,
        "pointer"
      ]
    ],
    [
      "00533a20",
      "DATA",
      [
        "storage",
        "00c664a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005339cc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533a14",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00533a20",
      "DATA",
      [
        "storage",
        "00c668a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-0053399c) · [`00533a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-00533a00) · [`00533a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-00533a4c)
- 新版 `005339dc`（命令位置の公開資料なし） · `00533a40`（命令位置の公開資料なし） · `00533a8c`（命令位置の公開資料なし）

~~~diff
- 0053399c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053399c ["INT_ADD", "register:40f0:8", ["const:53399c:8", "const:4:8"]]
- 0053399c ["CALLIND", null, ["register:0:8"]]
+ 005339dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005339dc ["INT_ADD", "register:40f0:8", ["const:5339dc:8", "const:4:8"]]
+ 005339dc ["CALLIND", null, ["register:0:8"]]
- 0053399c bytes 20013fd6
+ 005339dc bytes 20013fd6
- 00533a00 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a00 ["INT_ADD", "register:40f0:8", ["const:533a00:8", "const:4:8"]]
- 00533a00 ["CALLIND", null, ["register:0:8"]]
+ 00533a40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a40 ["INT_ADD", "register:40f0:8", ["const:533a40:8", "const:4:8"]]
+ 00533a40 ["CALLIND", null, ["register:0:8"]]
- 00533a00 bytes 20013fd6
+ 00533a40 bytes 20013fd6
- 00533a4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a4c ["INT_ADD", "register:40f0:8", ["const:533a4c:8", "const:4:8"]]
- 00533a4c ["CALLIND", null, ["register:0:8"]]
+ 00533a8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a8c ["INT_ADD", "register:40f0:8", ["const:533a8c:8", "const:4:8"]]
+ 00533a8c ["CALLIND", null, ["register:0:8"]]
- 00533a4c bytes 20013fd6
+ 00533a8c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc54f41e22973ce81008ce84dead031c"></a>

### [`00533b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md) → [`00533b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533b48.md) FUN_00533b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533b80",
      "incomplete_value": true,
      "site": "00533b80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533b40",
      "incomplete_value": true,
      "site": "00533b40",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533bac",
      "incomplete_value": true,
      "site": "00533bac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533b6c",
      "incomplete_value": true,
      "site": "00533b6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00533b70",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533b9c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533b70",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533b9c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b40) · [`00533b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b6c) · [`00533b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b30)
- 新版 `00533b80`（命令位置の公開資料なし） · `00533bac`（命令位置の公開資料なし） · `00533b70`（命令位置の公開資料なし）

~~~diff
- 00533b40 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533b40 ["INT_ADD", "register:40f0:8", ["const:533b40:8", "const:4:8"]]
- 00533b40 ["CALLIND", null, ["register:0:8"]]
+ 00533b80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533b80 ["INT_ADD", "register:40f0:8", ["const:533b80:8", "const:4:8"]]
+ 00533b80 ["CALLIND", null, ["register:0:8"]]
- 00533b40 bytes 20013fd6
+ 00533b80 bytes 20013fd6
- 00533b6c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533b6c ["INT_ADD", "register:40f0:8", ["const:533b6c:8", "const:4:8"]]
- 00533b6c ["CALLIND", null, ["register:0:8"]]
+ 00533bac ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533bac ["INT_ADD", "register:40f0:8", ["const:533bac:8", "const:4:8"]]
+ 00533bac ["CALLIND", null, ["register:0:8"]]
- 00533b6c bytes 20013fd6
+ 00533bac bytes 20013fd6
- 00533b30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00533b30 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533b70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00533b70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533b30 bytes a99e41f9
+ 00533b70 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c2c17079644273b67071a6f5e8f9d8"></a>

### [`00533bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md) → [`00533bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533bf4.md) FUN_00533bf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533c2c",
      "incomplete_value": true,
      "site": "00533c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533bec",
      "incomplete_value": true,
      "site": "00533bec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533c58",
      "incomplete_value": true,
      "site": "00533c58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533c18",
      "incomplete_value": true,
      "site": "00533c18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00533c1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533c48",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533c1c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533c48",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533bec) · [`00533c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533c18) · [`00533bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533bdc)
- 新版 `00533c2c`（命令位置の公開資料なし） · `00533c58`（命令位置の公開資料なし） · `00533c1c`（命令位置の公開資料なし）

~~~diff
- 00533bec ["COPY", "register:0:8", ["register:4048:8"]]
- 00533bec ["INT_ADD", "register:40f0:8", ["const:533bec:8", "const:4:8"]]
- 00533bec ["CALLIND", null, ["register:0:8"]]
+ 00533c2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c2c ["INT_ADD", "register:40f0:8", ["const:533c2c:8", "const:4:8"]]
+ 00533c2c ["CALLIND", null, ["register:0:8"]]
- 00533bec bytes 20013fd6
+ 00533c2c bytes 20013fd6
- 00533c18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533c18 ["INT_ADD", "register:40f0:8", ["const:533c18:8", "const:4:8"]]
- 00533c18 ["CALLIND", null, ["register:0:8"]]
+ 00533c58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c58 ["INT_ADD", "register:40f0:8", ["const:533c58:8", "const:4:8"]]
+ 00533c58 ["CALLIND", null, ["register:0:8"]]
- 00533c18 bytes 20013fd6
+ 00533c58 bytes 20013fd6
- 00533bdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00533bdc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533c1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00533c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533bdc bytes a99e41f9
+ 00533c1c bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbc50b9ef6eb51a2d89c64825eddb1e"></a>

### [`00533c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md) → [`00533c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533c98.md) FUN_00533c98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": "00533d40",
      "incomplete_value": true,
      "site": "00533d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533d00",
      "incomplete_value": true,
      "site": "00533d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
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
      "definition_site": "00533d3c",
      "incomplete_value": false,
      "site": "00533d4c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00533cfc",
      "incomplete_value": false,
      "site": "00533d0c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00533d3c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00533d40",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "00533d40",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00533d3c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00533d40",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00533d40",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533d0c) · [`00533cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533cb0) · [`00533cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533cc8)
- 新版 `00533d4c`（命令位置の公開資料なし） · `00533cf0`（命令位置の公開資料なし） · `00533d08`（命令位置の公開資料なし）

~~~diff
- 00533d0c ["INT_ADD", "register:40f0:8", ["const:533d0c:8", "const:4:8"]]
- 00533d0c ["CALL", null, ["callee:00c57f10:8"]]
+ 00533d4c ["INT_ADD", "register:40f0:8", ["const:533d4c:8", "const:4:8"]]
+ 00533d4c ["CALL", null, ["callee:00c57f10:8"]]
- 00533d0c bytes 818f1c94
+ 00533d4c bytes 71901c94
- 00533cb0 ["INT_ADD", "register:40f0:8", ["const:533cb0:8", "const:4:8"]]
- 00533cb0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00533cf0 ["INT_ADD", "register:40f0:8", ["const:533cf0:8", "const:4:8"]]
+ 00533cf0 ["CALL", null, ["callee:00c57ef0:8"]]
- 00533cb0 bytes 908f1c94
+ 00533cf0 bytes 80901c94
- 00533cc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533cc8 ["INT_ADD", "register:40f0:8", ["const:533cc8:8", "const:4:8"]]
- 00533cc8 ["CALLIND", null, ["register:0:8"]]
+ 00533d08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533d08 ["INT_ADD", "register:40f0:8", ["const:533d08:8", "const:4:8"]]
+ 00533d08 ["CALLIND", null, ["register:0:8"]]
- 00533cc8 bytes 20013fd6
+ 00533d08 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817111e169e044a7ce80625d8a96e371"></a>

### [`00533dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md) → [`00533dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533dec.md) FUN_00533dec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533e24",
      "incomplete_value": true,
      "site": "00533e24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533de4",
      "incomplete_value": true,
      "site": "00533de4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533e50",
      "incomplete_value": true,
      "site": "00533e50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533e10",
      "incomplete_value": true,
      "site": "00533e10",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00533e14",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533e40",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533e14",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533e40",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533de4) · [`00533e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533e10) · [`00533dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533dd4)
- 新版 `00533e24`（命令位置の公開資料なし） · `00533e50`（命令位置の公開資料なし） · `00533e14`（命令位置の公開資料なし）

~~~diff
- 00533de4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533de4 ["INT_ADD", "register:40f0:8", ["const:533de4:8", "const:4:8"]]
- 00533de4 ["CALLIND", null, ["register:0:8"]]
+ 00533e24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e24 ["INT_ADD", "register:40f0:8", ["const:533e24:8", "const:4:8"]]
+ 00533e24 ["CALLIND", null, ["register:0:8"]]
- 00533de4 bytes 20013fd6
+ 00533e24 bytes 20013fd6
- 00533e10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e10 ["INT_ADD", "register:40f0:8", ["const:533e10:8", "const:4:8"]]
- 00533e10 ["CALLIND", null, ["register:0:8"]]
+ 00533e50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e50 ["INT_ADD", "register:40f0:8", ["const:533e50:8", "const:4:8"]]
+ 00533e50 ["CALLIND", null, ["register:0:8"]]
- 00533e10 bytes 20013fd6
+ 00533e50 bytes 20013fd6
- 00533dd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00533dd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533e14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00533e14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533dd4 bytes a99e41f9
+ 00533e14 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673599c85acb792ae0ba46bab44e4d29"></a>

### [`00533e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md) → [`00533e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533e98.md) FUN_00533e98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533ed0",
      "incomplete_value": true,
      "site": "00533ed0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533e90",
      "incomplete_value": true,
      "site": "00533e90",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533efc",
      "incomplete_value": true,
      "site": "00533efc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533ebc",
      "incomplete_value": true,
      "site": "00533ebc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00533ec0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533eec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533ec0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533eec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533e90) · [`00533ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533ebc) · [`00533e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533e80)
- 新版 `00533ed0`（命令位置の公開資料なし） · `00533efc`（命令位置の公開資料なし） · `00533ec0`（命令位置の公開資料なし）

~~~diff
- 00533e90 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e90 ["INT_ADD", "register:40f0:8", ["const:533e90:8", "const:4:8"]]
- 00533e90 ["CALLIND", null, ["register:0:8"]]
+ 00533ed0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533ed0 ["INT_ADD", "register:40f0:8", ["const:533ed0:8", "const:4:8"]]
+ 00533ed0 ["CALLIND", null, ["register:0:8"]]
- 00533e90 bytes 20013fd6
+ 00533ed0 bytes 20013fd6
- 00533ebc ["COPY", "register:0:8", ["register:4048:8"]]
- 00533ebc ["INT_ADD", "register:40f0:8", ["const:533ebc:8", "const:4:8"]]
- 00533ebc ["CALLIND", null, ["register:0:8"]]
+ 00533efc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533efc ["INT_ADD", "register:40f0:8", ["const:533efc:8", "const:4:8"]]
+ 00533efc ["CALLIND", null, ["register:0:8"]]
- 00533ebc bytes 20013fd6
+ 00533efc bytes 20013fd6
- 00533e80 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00533e80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533ec0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00533ec0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533e80 bytes a99e41f9
+ 00533ec0 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09cc2b948b4adc31ab780697abcac57d"></a>

### [`00533ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md) → [`0053403c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053403c.md) FUN_0053403c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00534054",
      "incomplete_value": false,
      "site": "00534058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534014",
      "incomplete_value": false,
      "site": "00534018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
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
      "00534058",
      "DATA",
      [
        "storage",
        "00c66a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534058",
      "DATA",
      [
        "storage",
        "00c66e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md#insn-00534014) · [`00534024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md#insn-00534024)
- 新版 `00534054`（命令位置の公開資料なし） · `00534064`（命令位置の公開資料なし）

~~~diff
- 00534014 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00534014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534054 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00534054 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534054 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534054 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534014 bytes 29a12991
+ 00534054 bytes 29a13991
- 00534024 ["INT_ADD", "register:40f0:8", ["const:534024:8", "const:4:8"]]
- 00534024 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534064 ["INT_ADD", "register:40f0:8", ["const:534064:8", "const:4:8"]]
+ 00534064 ["CALL", null, ["callee:00c57eb0:8"]]
- 00534024 bytes a38e1c94
+ 00534064 bytes 938f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c6e8180bc021e7f204fcf9cfce7f9c"></a>

### [`00534060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md) → [`005340a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005340a0.md) FUN_005340a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c587c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "005340e8",
      "incomplete_value": true,
      "site": "005340e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:422:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005340a8",
      "incomplete_value": true,
      "site": "005340a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
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
      "definition_site": "00534114",
      "incomplete_value": true,
      "site": "00534120",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005340d4",
      "incomplete_value": true,
      "site": "005340e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "definition_site": "00534110",
      "incomplete_value": false,
      "site": "00534120",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005340d0",
      "incomplete_value": false,
      "site": "005340e0",
      "value": [
        "leaf",
        "const:535828:8"
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
      "005340d4",
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      "00534110",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00534114",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005340d4",
      "READ",
      [
        "storage",
        "002b7422",
        null,
        "string"
      ]
    ],
    [
      "00534110",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00534114",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005340e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-005340e0) · [`00534084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-00534084) · [`0053408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-0053408c)
- 新版 `00534120`（命令位置の公開資料なし） · `005340c4`（命令位置の公開資料なし） · `005340cc`（命令位置の公開資料なし）

~~~diff
- 005340e0 ["INT_ADD", "register:40f0:8", ["const:5340e0:8", "const:4:8"]]
- 005340e0 ["CALL", null, ["callee:00c57f10:8"]]
+ 00534120 ["INT_ADD", "register:40f0:8", ["const:534120:8", "const:4:8"]]
+ 00534120 ["CALL", null, ["callee:00c57f10:8"]]
- 005340e0 bytes 8c8e1c94
+ 00534120 bytes 7c8f1c94
- 00534084 ["INT_ADD", "register:40f0:8", ["const:534084:8", "const:4:8"]]
- 00534084 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005340c4 ["INT_ADD", "register:40f0:8", ["const:5340c4:8", "const:4:8"]]
+ 005340c4 ["CALL", null, ["callee:00c57ef0:8"]]
- 00534084 bytes 9b8e1c94
+ 005340c4 bytes 8b8f1c94
- 0053408c ["COPY", "tmp:0:8", ["const:3e2:8"]]
- 0053408c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053408c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053408c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005340cc ["COPY", "tmp:0:8", ["const:422:8"]]
+ 005340cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005340cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005340cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053408c bytes 29890f91
+ 005340cc bytes 29891091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb105b1e265528bc2dea0768c2b29bf9"></a>

### [`00534128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md) → [`00534168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534168.md) FUN_00534168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00534180",
      "incomplete_value": false,
      "site": "00534184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534140",
      "incomplete_value": false,
      "site": "00534144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "00534184",
      "DATA",
      [
        "storage",
        "00c66ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534184",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md#insn-00534140) · [`00534150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md#insn-00534150)
- 新版 `00534180`（命令位置の公開資料なし） · `00534190`（命令位置の公開資料なし）

~~~diff
- 00534140 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00534140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534180 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 00534180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534140 bytes 29e12a91
+ 00534180 bytes 29e13a91
- 00534150 ["INT_ADD", "register:40f0:8", ["const:534150:8", "const:4:8"]]
- 00534150 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534190 ["INT_ADD", "register:40f0:8", ["const:534190:8", "const:4:8"]]
+ 00534190 ["CALL", null, ["callee:00c57eb0:8"]]
- 00534150 bytes 588e1c94
+ 00534190 bytes 488f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a47434a06ccfba45eb9ac19ca1ebe07"></a>

### [`0053418c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md) → [`005341cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005341cc.md) FUN_005341cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c587c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00534214",
      "incomplete_value": true,
      "site": "00534214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:422:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005341d4",
      "incomplete_value": true,
      "site": "005341d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
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
      "definition_site": "00534240",
      "incomplete_value": true,
      "site": "0053424c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534200",
      "incomplete_value": true,
      "site": "0053420c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "definition_site": "0053423c",
      "incomplete_value": false,
      "site": "0053424c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005341fc",
      "incomplete_value": false,
      "site": "0053420c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00534200",
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      "0053423c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00534240",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534200",
      "READ",
      [
        "storage",
        "002b7422",
        null,
        "string"
      ]
    ],
    [
      "0053423c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00534240",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-0053420c) · [`005341b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-005341b0) · [`005341b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-005341b8)
- 新版 `0053424c`（命令位置の公開資料なし） · `005341f0`（命令位置の公開資料なし） · `005341f8`（命令位置の公開資料なし）

~~~diff
- 0053420c ["INT_ADD", "register:40f0:8", ["const:53420c:8", "const:4:8"]]
- 0053420c ["CALL", null, ["callee:00c57f10:8"]]
+ 0053424c ["INT_ADD", "register:40f0:8", ["const:53424c:8", "const:4:8"]]
+ 0053424c ["CALL", null, ["callee:00c57f10:8"]]
- 0053420c bytes 418e1c94
+ 0053424c bytes 318f1c94
- 005341b0 ["INT_ADD", "register:40f0:8", ["const:5341b0:8", "const:4:8"]]
- 005341b0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005341f0 ["INT_ADD", "register:40f0:8", ["const:5341f0:8", "const:4:8"]]
+ 005341f0 ["CALL", null, ["callee:00c57ef0:8"]]
- 005341b0 bytes 508e1c94
+ 005341f0 bytes 408f1c94
- 005341b8 ["COPY", "tmp:0:8", ["const:3e2:8"]]
- 005341b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005341b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005341b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005341f8 ["COPY", "tmp:0:8", ["const:422:8"]]
+ 005341f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005341f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005341f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005341b8 bytes 29890f91
+ 005341f8 bytes 29891091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecbf41d0a02cc99d47cb73cc2834b101"></a>

### [`00534254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md) → [`00534294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534294.md) FUN_00534294

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005342c4",
      "incomplete_value": true,
      "site": "005342d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534284",
      "incomplete_value": true,
      "site": "00534298",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d90:8"
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
      "definition_site": "005342c8",
      "incomplete_value": true,
      "site": "005342dc",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534288",
      "incomplete_value": true,
      "site": "0053429c",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
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
      "definition_site": "005342e8",
      "incomplete_value": true,
      "site": "005342e8",
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
      "definition_site": "005342a8",
      "incomplete_value": true,
      "site": "005342a8",
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
      "005342c4",
      "READ",
      [
        "storage",
        "002b1d90",
        null,
        "string"
      ]
    ],
    [
      "005342c8",
      "READ",
      [
        "storage",
        "002b1d99",
        null,
        "string"
      ]
    ],
    [
      "005342d0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005342c4",
      "READ",
      [
        "storage",
        "002b1dd0",
        null,
        "string"
      ]
    ],
    [
      "005342c8",
      "READ",
      [
        "storage",
        "002b1dd9",
        null,
        "string"
      ]
    ],
    [
      "005342d0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-00534268) · [`005342d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-005342d8) · [`005342dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-005342dc)
- 新版 `005342a8`（命令位置の公開資料なし） · `0053431c`（命令位置の公開資料なし）

~~~diff
- 00534268 ["INT_ADD", "register:40f0:8", ["const:534268:8", "const:4:8"]]
- 00534268 ["CALL", null, ["callee:00c57ef0:8"]]
+ 005342a8 ["INT_ADD", "register:40f0:8", ["const:5342a8:8", "const:4:8"]]
+ 005342a8 ["CALL", null, ["callee:00c57ef0:8"]]
- 00534268 bytes 228e1c94
+ 005342a8 bytes 128f1c94
- 005342d8 ["COPY", "register:4000:8", ["register:4098:8"]]
- 005342d8 bytes e00313aa
- 005342dc ["INT_ADD", "register:40f0:8", ["const:5342dc:8", "const:4:8"]]
- 005342dc ["CALL", null, ["callee:00c57f10:8"]]
+ 0053431c ["INT_ADD", "register:40f0:8", ["const:53431c:8", "const:4:8"]]
+ 0053431c ["CALL", null, ["callee:00c57f10:8"]]
- 005342dc bytes 0d8e1c94
+ 0053431c bytes fd8e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc39ae3193c398a2f83f78ba776b9e73"></a>

### [`00534320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md) → [`00534360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534360.md) FUN_00534360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534390",
      "incomplete_value": true,
      "site": "005343a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534350",
      "incomplete_value": true,
      "site": "00534364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c8:8"
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
      "definition_site": "00534394",
      "incomplete_value": true,
      "site": "005343a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00534354",
      "incomplete_value": true,
      "site": "00534368",
      "value": [
        "LOAD",
        "16",
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
    "kind": "store_value",
    "new": {
      "definition_site": "005343b4",
      "incomplete_value": true,
      "site": "005343b4",
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
      "definition_site": "00534374",
      "incomplete_value": true,
      "site": "00534374",
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
      "00534390",
      "READ",
      [
        "storage",
        "002a66c8",
        null,
        "string"
      ]
    ],
    [
      "00534394",
      "READ",
      [
        "storage",
        "002a66d6",
        null,
        "string"
      ]
    ],
    [
      "0053439c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534390",
      "READ",
      [
        "storage",
        "002a67a4",
        null,
        "string"
      ]
    ],
    [
      "00534394",
      "READ",
      [
        "storage",
        "002a67b2",
        null,
        "string"
      ]
    ],
    [
      "0053439c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-00534334) · [`005343a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-005343a4) · [`005343a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-005343a8)
- 新版 `00534374`（命令位置の公開資料なし） · `005343e8`（命令位置の公開資料なし）

~~~diff
- 00534334 ["INT_ADD", "register:40f0:8", ["const:534334:8", "const:4:8"]]
- 00534334 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00534374 ["INT_ADD", "register:40f0:8", ["const:534374:8", "const:4:8"]]
+ 00534374 ["CALL", null, ["callee:00c57ef0:8"]]
- 00534334 bytes ef8d1c94
+ 00534374 bytes df8e1c94
- 005343a4 ["COPY", "register:4000:8", ["register:4098:8"]]
- 005343a4 bytes e00313aa
- 005343a8 ["INT_ADD", "register:40f0:8", ["const:5343a8:8", "const:4:8"]]
- 005343a8 ["CALL", null, ["callee:00c57f10:8"]]
+ 005343e8 ["INT_ADD", "register:40f0:8", ["const:5343e8:8", "const:4:8"]]
+ 005343e8 ["CALL", null, ["callee:00c57f10:8"]]
- 005343a8 bytes da8d1c94
+ 005343e8 bytes ca8e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a91bf6a33de849616c199e0f70018b"></a>

### [`005343ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md) → [`0053442c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053442c.md) FUN_0053442c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0053443c",
      "incomplete_value": false,
      "site": "0053443c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005343fc",
      "incomplete_value": false,
      "site": "005343fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
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
      "0053443c",
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053443c",
      "DATA",
      [
        "storage",
        "00c66f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005343f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md#insn-005343f8)
- 新版 `00534438`（命令位置の公開資料なし）

~~~diff
- 005343f8 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 005343f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005343f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005343f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534438 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 00534438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005343f8 bytes 29612c91
+ 00534438 bytes 29613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d45d6864e629a433bb702ea21c318502"></a>

### [`00534418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md) → [`00534458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534458.md) FUN_00534458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00534468",
      "incomplete_value": false,
      "site": "00534468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534428",
      "incomplete_value": false,
      "site": "00534428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
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
      "00534468",
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534468",
      "DATA",
      [
        "storage",
        "00c66f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md#insn-00534424)
- 新版 `00534464`（命令位置の公開資料なし）

~~~diff
- 00534424 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00534424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534464 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00534464 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534464 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534464 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534424 bytes 29212d91
+ 00534464 bytes 29213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e24a1deb133ea082b1a4b3867d8655c"></a>

### [`00534444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md) → [`00534484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534484.md) FUN_00534484

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005344a8",
      "incomplete_value": true,
      "site": "005344b4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534468",
      "incomplete_value": true,
      "site": "00534474",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005344d4",
      "incomplete_value": true,
      "site": "005344d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534494",
      "incomplete_value": true,
      "site": "00534494",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534500",
      "incomplete_value": true,
      "site": "00534500",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005344c0",
      "incomplete_value": true,
      "site": "005344c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "0053449c",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "005344b4",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005344c4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053449c",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005344b4",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005344c4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-00534494) · [`005344c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-005344c0) · [`0053445c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-0053445c)
- 新版 `005344d4`（命令位置の公開資料なし） · `00534500`（命令位置の公開資料なし） · `0053449c`（命令位置の公開資料なし）

~~~diff
- 00534494 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534494 ["INT_ADD", "register:40f0:8", ["const:534494:8", "const:4:8"]]
- 00534494 ["CALLIND", null, ["register:0:8"]]
+ 005344d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005344d4 ["INT_ADD", "register:40f0:8", ["const:5344d4:8", "const:4:8"]]
+ 005344d4 ["CALLIND", null, ["register:0:8"]]
- 00534494 bytes 20013fd6
+ 005344d4 bytes 20013fd6
- 005344c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005344c0 ["INT_ADD", "register:40f0:8", ["const:5344c0:8", "const:4:8"]]
- 005344c0 ["CALLIND", null, ["register:0:8"]]
+ 00534500 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534500 ["INT_ADD", "register:40f0:8", ["const:534500:8", "const:4:8"]]
+ 00534500 ["CALLIND", null, ["register:0:8"]]
- 005344c0 bytes 20013fd6
+ 00534500 bytes 20013fd6
- 0053445c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 0053445c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053449c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 0053449c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053445c bytes 08ed45f9
+ 0053449c bytes 08ed47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82766efa161f0144101d520863d52d77"></a>

### [`005344f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md) → [`00534530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534530.md) FUN_00534530

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534554",
      "incomplete_value": true,
      "site": "00534560",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534514",
      "incomplete_value": true,
      "site": "00534520",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534580",
      "incomplete_value": true,
      "site": "00534580",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534540",
      "incomplete_value": true,
      "site": "00534540",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005345ac",
      "incomplete_value": true,
      "site": "005345ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053456c",
      "incomplete_value": true,
      "site": "0053456c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00534548",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "00534560",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534570",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534548",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "00534560",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534570",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-00534540) · [`0053456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-0053456c) · [`00534508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-00534508)
- 新版 `00534580`（命令位置の公開資料なし） · `005345ac`（命令位置の公開資料なし） · `00534548`（命令位置の公開資料なし）

~~~diff
- 00534540 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534540 ["INT_ADD", "register:40f0:8", ["const:534540:8", "const:4:8"]]
- 00534540 ["CALLIND", null, ["register:0:8"]]
+ 00534580 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534580 ["INT_ADD", "register:40f0:8", ["const:534580:8", "const:4:8"]]
+ 00534580 ["CALLIND", null, ["register:0:8"]]
- 00534540 bytes 20013fd6
+ 00534580 bytes 20013fd6
- 0053456c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053456c ["INT_ADD", "register:40f0:8", ["const:53456c:8", "const:4:8"]]
- 0053456c ["CALLIND", null, ["register:0:8"]]
+ 005345ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 005345ac ["INT_ADD", "register:40f0:8", ["const:5345ac:8", "const:4:8"]]
+ 005345ac ["CALLIND", null, ["register:0:8"]]
- 0053456c bytes 20013fd6
+ 005345ac bytes 20013fd6
- 00534508 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
- 00534508 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 00534548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534508 bytes 08ed45f9
+ 00534548 bytes 08ed47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d6f9d3d7df514bc88592434f11fc0d"></a>

### [`005345b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md) → [`005345f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005345f8.md) FUN_005345f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00540094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005400d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005400d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053460c",
      "incomplete_value": true,
      "site": "00534610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005345cc",
      "incomplete_value": true,
      "site": "005345d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
      "0053460c",
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      "0053460c",
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "0053460c",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "0053460c",
      "PARAM",
      [
        "storage",
        "00c67328",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005345d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md#insn-005345d0) · [`005345cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md#insn-005345cc)
- 新版 `00534610`（命令位置の公開資料なし） · `0053460c`（命令位置の公開資料なし）

~~~diff
- 005345d0 ["INT_ADD", "register:40f0:8", ["const:5345d0:8", "const:4:8"]]
- 005345d0 ["CALL", null, ["callee:005400d4:8"]]
+ 00534610 ["INT_ADD", "register:40f0:8", ["const:534610:8", "const:4:8"]]
+ 00534610 ["CALL", null, ["callee:005400d4:8"]]
- 005345d0 bytes b12e0094
+ 00534610 bytes b12e0094
- 005345cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
- 005345cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053460c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
+ 0053460c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005345cc bytes 21f445f9
+ 0053460c bytes 21f447f9
~~~


<a id="compare-368c30a4361e2b080355c31f23777634"></a>

### [`005345f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md) → [`00534634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534634.md) FUN_00534634

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00540094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005400d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005400d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534648",
      "incomplete_value": true,
      "site": "00534650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534608",
      "incomplete_value": true,
      "site": "00534610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
      "00534648",
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      "00534648",
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "00534648",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "00534648",
      "PARAM",
      [
        "storage",
        "00c67328",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md#insn-00534610) · [`00534608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md#insn-00534608)
- 新版 `00534650`（命令位置の公開資料なし） · `00534648`（命令位置の公開資料なし）

~~~diff
- 00534610 ["INT_ADD", "register:40f0:8", ["const:534610:8", "const:4:8"]]
- 00534610 ["CALL", null, ["callee:005400d4:8"]]
+ 00534650 ["INT_ADD", "register:40f0:8", ["const:534650:8", "const:4:8"]]
+ 00534650 ["CALL", null, ["callee:005400d4:8"]]
- 00534610 bytes a12e0094
+ 00534650 bytes a12e0094
- 00534608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
- 00534608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534648 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
+ 00534648 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00534608 bytes 21f445f9
+ 00534648 bytes 21f447f9
~~~


<a id="compare-7423e9a6e79069e313e13ea4b927076f"></a>

### [`005347cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md) → [`0053480c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053480c.md) FUN_0053480c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

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
      "definition_site": "00534828",
      "incomplete_value": true,
      "site": "0053482c",
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
      "definition_site": "005347e8",
      "incomplete_value": true,
      "site": "005347ec",
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
      "definition_site": "00534868",
      "incomplete_value": true,
      "site": "0053486c",
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
      "definition_site": "00534828",
      "incomplete_value": true,
      "site": "0053482c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00534820",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "0053482c",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534860",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534820",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "0053482c",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534860",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005347d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347d8) · [`005347e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347e0) · [`005347fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347fc)
- 新版 `00534818`（命令位置の公開資料なし） · `00534820`（命令位置の公開資料なし） · `0053483c`（命令位置の公開資料なし）

~~~diff
- 005347d8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00534818 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005347d8 bytes 283b00d0
+ 00534818 bytes 283b00f0
- 005347e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
- 005347e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534820 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
+ 00534820 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005347e0 bytes 087146f9
+ 00534820 bytes 087140f9
- 005347fc ["INT_ADD", "register:40f0:8", ["const:5347fc:8", "const:4:8"]]
- 005347fc ["CALL", null, ["callee:00c53d00:8"]]
+ 0053483c ["INT_ADD", "register:40f0:8", ["const:53483c:8", "const:4:8"]]
+ 0053483c ["CALL", null, ["callee:00c53d00:8"]]
- 005347fc bytes 397c1c94
+ 0053483c bytes 317d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e89ea222af1758b5f47c299f2d3e0e04"></a>

### [`0053487c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md) → [`005348bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005348bc.md) FUN_005348bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005348d8",
      "incomplete_value": true,
      "site": "005348dc",
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
      "definition_site": "00534898",
      "incomplete_value": true,
      "site": "0053489c",
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
      "005348d0",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "005348dc",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "005348d0",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "005348dc",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-00534888) · [`00534890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-00534890) · [`005348a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-005348a8)
- 新版 `005348c8`（命令位置の公開資料なし） · `005348d0`（命令位置の公開資料なし） · `005348e8`（命令位置の公開資料なし）

~~~diff
- 00534888 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005348c8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534888 bytes 283b00d0
+ 005348c8 bytes 283b00f0
- 00534890 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00534890 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005348d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 005348d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534890 bytes 08ad46f9
+ 005348d0 bytes 08ad40f9
- 005348a8 ["INT_ADD", "register:40f0:8", ["const:5348a8:8", "const:4:8"]]
- 005348a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005348e8 ["INT_ADD", "register:40f0:8", ["const:5348e8:8", "const:4:8"]]
+ 005348e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005348a8 bytes 828c1c94
+ 005348e8 bytes 728d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-196f30d25b53875c9ea769fdc17c679a"></a>

### [`00534d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md) → [`00534d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534d88.md) FUN_00534d88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534da4",
      "incomplete_value": true,
      "site": "00534da8",
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
      "definition_site": "00534d64",
      "incomplete_value": true,
      "site": "00534d68",
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
      "00534d9c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00534da8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00534d9c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00534da8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d5c) · [`00534d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d74) · [`00534d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d7c)
- 新版 `00534d9c`（命令位置の公開資料なし） · `00534db4`（命令位置の公開資料なし） · `00534dbc`（命令位置の公開資料なし）

~~~diff
- 00534d5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00534d5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534d9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00534d9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534d5c bytes 08e944f9
+ 00534d9c bytes 08e946f9
- 00534d74 ["INT_ADD", "register:40f0:8", ["const:534d74:8", "const:4:8"]]
- 00534d74 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534db4 ["INT_ADD", "register:40f0:8", ["const:534db4:8", "const:4:8"]]
+ 00534db4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00534d74 bytes 4f8b1c94
+ 00534db4 bytes 3f8c1c94
- 00534d7c ["INT_ADD", "register:40f0:8", ["const:534d7c:8", "const:4:8"]]
- 00534d7c ["CALL", null, ["callee:00c582e0:8"]]
+ 00534dbc ["INT_ADD", "register:40f0:8", ["const:534dbc:8", "const:4:8"]]
+ 00534dbc ["CALL", null, ["callee:00c582e0:8"]]
- 00534d7c bytes 598c1c94
+ 00534dbc bytes 498d1c94
~~~


<a id="compare-c7656765a5bdf99eee56c739ca3ea16b"></a>

### [`00534da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md) → [`00534de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534de8.md) FUN_00534de8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534e04",
      "incomplete_value": true,
      "site": "00534e08",
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
      "definition_site": "00534dc4",
      "incomplete_value": true,
      "site": "00534dc8",
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
      "00534dfc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00534e08",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00534dfc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00534e08",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534dbc) · [`00534dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534dd4) · [`00534ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534ddc)
- 新版 `00534dfc`（命令位置の公開資料なし） · `00534e14`（命令位置の公開資料なし） · `00534e1c`（命令位置の公開資料なし）

~~~diff
- 00534dbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00534dbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00534dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534dbc bytes 08e944f9
+ 00534dfc bytes 08e946f9
- 00534dd4 ["INT_ADD", "register:40f0:8", ["const:534dd4:8", "const:4:8"]]
- 00534dd4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534e14 ["INT_ADD", "register:40f0:8", ["const:534e14:8", "const:4:8"]]
+ 00534e14 ["CALL", null, ["callee:00c57eb0:8"]]
- 00534dd4 bytes 378b1c94
+ 00534e14 bytes 278c1c94
- 00534ddc ["INT_ADD", "register:40f0:8", ["const:534ddc:8", "const:4:8"]]
- 00534ddc ["CALL", null, ["callee:00c582e0:8"]]
+ 00534e1c ["INT_ADD", "register:40f0:8", ["const:534e1c:8", "const:4:8"]]
+ 00534e1c ["CALL", null, ["callee:00c582e0:8"]]
- 00534ddc bytes 418c1c94
+ 00534e1c bytes 318d1c94
~~~


<a id="compare-b7b1ec34ac86d79906c6b0da4b415249"></a>

### [`00534e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md) → [`00534eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534eb8.md) FUN_00534eb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534ed4",
      "incomplete_value": true,
      "site": "00534ed8",
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
      "definition_site": "00534e94",
      "incomplete_value": true,
      "site": "00534e98",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00534f0c",
      "incomplete_value": true,
      "site": "00534f0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534ecc",
      "incomplete_value": true,
      "site": "00534ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "00534ecc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00534ed8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534efc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534ecc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00534ed8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534efc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534e8c) · [`00534ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534ecc) · [`00534ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534ea4)
- 新版 `00534ecc`（命令位置の公開資料なし） · `00534f0c`（命令位置の公開資料なし） · `00534ee4`（命令位置の公開資料なし）

~~~diff
- 00534e8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00534e8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534ecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00534ecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534e8c bytes 083945f9
+ 00534ecc bytes 083947f9
- 00534ecc ["COPY", "register:0:8", ["register:4048:8"]]
- 00534ecc ["INT_ADD", "register:40f0:8", ["const:534ecc:8", "const:4:8"]]
- 00534ecc ["CALLIND", null, ["register:0:8"]]
+ 00534f0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534f0c ["INT_ADD", "register:40f0:8", ["const:534f0c:8", "const:4:8"]]
+ 00534f0c ["CALLIND", null, ["register:0:8"]]
- 00534ecc bytes 20013fd6
+ 00534f0c bytes 20013fd6
- 00534ea4 ["INT_ADD", "register:40f0:8", ["const:534ea4:8", "const:4:8"]]
- 00534ea4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534ee4 ["INT_ADD", "register:40f0:8", ["const:534ee4:8", "const:4:8"]]
+ 00534ee4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00534ea4 bytes 038b1c94
+ 00534ee4 bytes f38b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c5be709f3be6be20c8667c08aff9f56"></a>

### [`00534ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md) → [`00534f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534f30.md) FUN_00534f30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534f4c",
      "incomplete_value": true,
      "site": "00534f50",
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
      "definition_site": "00534f0c",
      "incomplete_value": true,
      "site": "00534f10",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00534f84",
      "incomplete_value": true,
      "site": "00534f84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534f44",
      "incomplete_value": true,
      "site": "00534f44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "00534f44",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00534f50",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f74",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534f44",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00534f50",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f74",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534f04) · [`00534f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534f44) · [`00534f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534f1c)
- 新版 `00534f44`（命令位置の公開資料なし） · `00534f84`（命令位置の公開資料なし） · `00534f5c`（命令位置の公開資料なし）

~~~diff
- 00534f04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00534f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534f44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00534f44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534f04 bytes 083945f9
+ 00534f44 bytes 083947f9
- 00534f44 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534f44 ["INT_ADD", "register:40f0:8", ["const:534f44:8", "const:4:8"]]
- 00534f44 ["CALLIND", null, ["register:0:8"]]
+ 00534f84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534f84 ["INT_ADD", "register:40f0:8", ["const:534f84:8", "const:4:8"]]
+ 00534f84 ["CALLIND", null, ["register:0:8"]]
- 00534f44 bytes 20013fd6
+ 00534f84 bytes 20013fd6
- 00534f1c ["INT_ADD", "register:40f0:8", ["const:534f1c:8", "const:4:8"]]
- 00534f1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00534f5c ["INT_ADD", "register:40f0:8", ["const:534f5c:8", "const:4:8"]]
+ 00534f5c ["CALL", null, ["callee:00c57eb0:8"]]
- 00534f1c bytes e58a1c94
+ 00534f5c bytes d58b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68437834c4d7d5109c485c220e9f367a"></a>

### [`00534ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md) → [`00535034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535034.md) FUN_00535034

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535048",
      "incomplete_value": true,
      "site": "00535048",
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
      "definition_site": "00535008",
      "incomplete_value": true,
      "site": "00535008",
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
      "0053503c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "00535048",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "0053503c",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "00535048",
      "DATA",
      [
        "storage",
        "00c66d58",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md#insn-00534ffc)
- 新版 `0053503c`（命令位置の公開資料なし）

~~~diff
- 00534ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bb0:8"]]
- 00534ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053503c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fb0:8"]]
+ 0053503c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00534ffc bytes 29d945f9
+ 0053503c bytes 29d947f9
~~~


<a id="compare-5ddb73b9e2f761f28514d6f31742ea6d"></a>

### [`00535318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md) → [`00535358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535358.md) FUN_00535358

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535374",
      "incomplete_value": true,
      "site": "00535378",
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
      "definition_site": "00535334",
      "incomplete_value": true,
      "site": "00535338",
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
      "0053536c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535378",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053536c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535378",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-0053532c) · [`00535344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-00535344) · [`0053534c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-0053534c)
- 新版 `0053536c`（命令位置の公開資料なし） · `00535384`（命令位置の公開資料なし） · `0053538c`（命令位置の公開資料なし）

~~~diff
- 0053532c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0053532c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053536c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053536c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053532c bytes 08e944f9
+ 0053536c bytes 08e946f9
- 00535344 ["INT_ADD", "register:40f0:8", ["const:535344:8", "const:4:8"]]
- 00535344 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535384 ["INT_ADD", "register:40f0:8", ["const:535384:8", "const:4:8"]]
+ 00535384 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535344 bytes db891c94
+ 00535384 bytes cb8a1c94
- 0053534c ["INT_ADD", "register:40f0:8", ["const:53534c:8", "const:4:8"]]
- 0053534c ["CALL", null, ["callee:00c582e0:8"]]
+ 0053538c ["INT_ADD", "register:40f0:8", ["const:53538c:8", "const:4:8"]]
+ 0053538c ["CALL", null, ["callee:00c582e0:8"]]
- 0053534c bytes e58a1c94
+ 0053538c bytes d58b1c94
~~~


<a id="compare-83b4ec2c9c5bfe1c2d4cb652fe9dd019"></a>

### [`00535360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md) → [`005353a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353a0.md) FUN_005353a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005353bc",
      "incomplete_value": true,
      "site": "005353c0",
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
      "definition_site": "0053537c",
      "incomplete_value": true,
      "site": "00535380",
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
      "005353b4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005353c0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005353b4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005353c0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-00535374) · [`0053538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-0053538c) · [`00535394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-00535394)
- 新版 `005353b4`（命令位置の公開資料なし） · `005353cc`（命令位置の公開資料なし） · `005353d4`（命令位置の公開資料なし）

~~~diff
- 00535374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005353b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005353b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535374 bytes 08e944f9
+ 005353b4 bytes 08e946f9
- 0053538c ["INT_ADD", "register:40f0:8", ["const:53538c:8", "const:4:8"]]
- 0053538c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005353cc ["INT_ADD", "register:40f0:8", ["const:5353cc:8", "const:4:8"]]
+ 005353cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0053538c bytes c9891c94
+ 005353cc bytes b98a1c94
- 00535394 ["INT_ADD", "register:40f0:8", ["const:535394:8", "const:4:8"]]
- 00535394 ["CALL", null, ["callee:00c582e0:8"]]
+ 005353d4 ["INT_ADD", "register:40f0:8", ["const:5353d4:8", "const:4:8"]]
+ 005353d4 ["CALL", null, ["callee:00c582e0:8"]]
- 00535394 bytes d38a1c94
+ 005353d4 bytes c38b1c94
~~~


<a id="compare-d5614a1d48dc89fd0efd3c7faf1a6a2e"></a>

### [`005353a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md) → [`005353e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353e8.md) FUN_005353e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535404",
      "incomplete_value": true,
      "site": "00535408",
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
      "definition_site": "005353c4",
      "incomplete_value": true,
      "site": "005353c8",
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
      "005353fc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535408",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005353fc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535408",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005353bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353bc) · [`005353d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353d4) · [`005353dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353dc)
- 新版 `005353fc`（命令位置の公開資料なし） · `00535414`（命令位置の公開資料なし） · `0053541c`（命令位置の公開資料なし）

~~~diff
- 005353bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005353bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005353fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005353fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005353bc bytes 08e944f9
+ 005353fc bytes 08e946f9
- 005353d4 ["INT_ADD", "register:40f0:8", ["const:5353d4:8", "const:4:8"]]
- 005353d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535414 ["INT_ADD", "register:40f0:8", ["const:535414:8", "const:4:8"]]
+ 00535414 ["CALL", null, ["callee:00c57eb0:8"]]
- 005353d4 bytes b7891c94
+ 00535414 bytes a78a1c94
- 005353dc ["INT_ADD", "register:40f0:8", ["const:5353dc:8", "const:4:8"]]
- 005353dc ["CALL", null, ["callee:00c582e0:8"]]
+ 0053541c ["INT_ADD", "register:40f0:8", ["const:53541c:8", "const:4:8"]]
+ 0053541c ["CALL", null, ["callee:00c582e0:8"]]
- 005353dc bytes c18a1c94
+ 0053541c bytes b18b1c94
~~~


<a id="compare-001e02be3098794fee9044aaf6631e6e"></a>

### [`005353f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md) → [`00535430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535430.md) FUN_00535430

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053544c",
      "incomplete_value": true,
      "site": "00535450",
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
      "definition_site": "0053540c",
      "incomplete_value": true,
      "site": "00535410",
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
      "00535444",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535450",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535444",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535450",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-00535404) · [`0053541c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-0053541c) · [`00535424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-00535424)
- 新版 `00535444`（命令位置の公開資料なし） · `0053545c`（命令位置の公開資料なし） · `00535464`（命令位置の公開資料なし）

~~~diff
- 00535404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535404 bytes 08e944f9
+ 00535444 bytes 08e946f9
- 0053541c ["INT_ADD", "register:40f0:8", ["const:53541c:8", "const:4:8"]]
- 0053541c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053545c ["INT_ADD", "register:40f0:8", ["const:53545c:8", "const:4:8"]]
+ 0053545c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053541c bytes a5891c94
+ 0053545c bytes 958a1c94
- 00535424 ["INT_ADD", "register:40f0:8", ["const:535424:8", "const:4:8"]]
- 00535424 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535464 ["INT_ADD", "register:40f0:8", ["const:535464:8", "const:4:8"]]
+ 00535464 ["CALL", null, ["callee:00c582e0:8"]]
- 00535424 bytes af8a1c94
+ 00535464 bytes 9f8b1c94
~~~


<a id="compare-a55ec21f49f3f8d799492a1aca53a62a"></a>

### [`00535438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md) → [`00535478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535478.md) FUN_00535478

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535494",
      "incomplete_value": true,
      "site": "00535498",
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
      "definition_site": "00535454",
      "incomplete_value": true,
      "site": "00535458",
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
      "0053548c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535498",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053548c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535498",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-0053544c) · [`00535464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-00535464) · [`0053546c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-0053546c)
- 新版 `0053548c`（命令位置の公開資料なし） · `005354a4`（命令位置の公開資料なし） · `005354ac`（命令位置の公開資料なし）

~~~diff
- 0053544c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0053544c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053548c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053548c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053544c bytes 08e944f9
+ 0053548c bytes 08e946f9
- 00535464 ["INT_ADD", "register:40f0:8", ["const:535464:8", "const:4:8"]]
- 00535464 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005354a4 ["INT_ADD", "register:40f0:8", ["const:5354a4:8", "const:4:8"]]
+ 005354a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535464 bytes 93891c94
+ 005354a4 bytes 838a1c94
- 0053546c ["INT_ADD", "register:40f0:8", ["const:53546c:8", "const:4:8"]]
- 0053546c ["CALL", null, ["callee:00c582e0:8"]]
+ 005354ac ["INT_ADD", "register:40f0:8", ["const:5354ac:8", "const:4:8"]]
+ 005354ac ["CALL", null, ["callee:00c582e0:8"]]
- 0053546c bytes 9d8a1c94
+ 005354ac bytes 8d8b1c94
~~~


<a id="compare-1da75a357681ff9c61083891c5f21d86"></a>

### [`00535480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md) → [`005354c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005354c0.md) FUN_005354c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005354dc",
      "incomplete_value": true,
      "site": "005354e0",
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
      "definition_site": "0053549c",
      "incomplete_value": true,
      "site": "005354a0",
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
      "005354d4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005354e0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005354d4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005354e0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-00535494) · [`005354ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-005354ac) · [`005354b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-005354b4)
- 新版 `005354d4`（命令位置の公開資料なし） · `005354ec`（命令位置の公開資料なし） · `005354f4`（命令位置の公開資料なし）

~~~diff
- 00535494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005354d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005354d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535494 bytes 08e944f9
+ 005354d4 bytes 08e946f9
- 005354ac ["INT_ADD", "register:40f0:8", ["const:5354ac:8", "const:4:8"]]
- 005354ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 005354ec ["INT_ADD", "register:40f0:8", ["const:5354ec:8", "const:4:8"]]
+ 005354ec ["CALL", null, ["callee:00c57eb0:8"]]
- 005354ac bytes 81891c94
+ 005354ec bytes 718a1c94
- 005354b4 ["INT_ADD", "register:40f0:8", ["const:5354b4:8", "const:4:8"]]
- 005354b4 ["CALL", null, ["callee:00c582e0:8"]]
+ 005354f4 ["INT_ADD", "register:40f0:8", ["const:5354f4:8", "const:4:8"]]
+ 005354f4 ["CALL", null, ["callee:00c582e0:8"]]
- 005354b4 bytes 8b8a1c94
+ 005354f4 bytes 7b8b1c94
~~~


<a id="compare-9dd3d63496f4a03f18001e0a351e5660"></a>

### [`005354c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md) → [`00535508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535508.md) FUN_00535508

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535524",
      "incomplete_value": true,
      "site": "00535528",
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
      "definition_site": "005354e4",
      "incomplete_value": true,
      "site": "005354e8",
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
      "0053551c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535528",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053551c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535528",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005354dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354dc) · [`005354f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354f4) · [`005354fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354fc)
- 新版 `0053551c`（命令位置の公開資料なし） · `00535534`（命令位置の公開資料なし） · `0053553c`（命令位置の公開資料なし）

~~~diff
- 005354dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005354dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053551c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053551c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005354dc bytes 08e944f9
+ 0053551c bytes 08e946f9
- 005354f4 ["INT_ADD", "register:40f0:8", ["const:5354f4:8", "const:4:8"]]
- 005354f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535534 ["INT_ADD", "register:40f0:8", ["const:535534:8", "const:4:8"]]
+ 00535534 ["CALL", null, ["callee:00c57eb0:8"]]
- 005354f4 bytes 6f891c94
+ 00535534 bytes 5f8a1c94
- 005354fc ["INT_ADD", "register:40f0:8", ["const:5354fc:8", "const:4:8"]]
- 005354fc ["CALL", null, ["callee:00c582e0:8"]]
+ 0053553c ["INT_ADD", "register:40f0:8", ["const:53553c:8", "const:4:8"]]
+ 0053553c ["CALL", null, ["callee:00c582e0:8"]]
- 005354fc bytes 798a1c94
+ 0053553c bytes 698b1c94
~~~


<a id="compare-53b3743513558909b4f6ee35bb30c622"></a>

### [`00535510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md) → [`00535550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535550.md) FUN_00535550

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053556c",
      "incomplete_value": true,
      "site": "00535570",
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
      "definition_site": "0053552c",
      "incomplete_value": true,
      "site": "00535530",
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
      "00535564",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535570",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535564",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535570",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-00535524) · [`0053553c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-0053553c) · [`00535544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-00535544)
- 新版 `00535564`（命令位置の公開資料なし） · `0053557c`（命令位置の公開資料なし） · `00535584`（命令位置の公開資料なし）

~~~diff
- 00535524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535564 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535524 bytes 08e944f9
+ 00535564 bytes 08e946f9
- 0053553c ["INT_ADD", "register:40f0:8", ["const:53553c:8", "const:4:8"]]
- 0053553c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053557c ["INT_ADD", "register:40f0:8", ["const:53557c:8", "const:4:8"]]
+ 0053557c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053553c bytes 5d891c94
+ 0053557c bytes 4d8a1c94
- 00535544 ["INT_ADD", "register:40f0:8", ["const:535544:8", "const:4:8"]]
- 00535544 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535584 ["INT_ADD", "register:40f0:8", ["const:535584:8", "const:4:8"]]
+ 00535584 ["CALL", null, ["callee:00c582e0:8"]]
- 00535544 bytes 678a1c94
+ 00535584 bytes 578b1c94
~~~


<a id="compare-53d356dee0065d73c9e5c6f6cb53b305"></a>

### [`00535558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md) → [`00535598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535598.md) FUN_00535598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005355b4",
      "incomplete_value": true,
      "site": "005355b8",
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
      "definition_site": "00535574",
      "incomplete_value": true,
      "site": "00535578",
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
      "005355ac",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005355b8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005355ac",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005355b8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053556c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-0053556c) · [`00535584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-00535584) · [`0053558c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-0053558c)
- 新版 `005355ac`（命令位置の公開資料なし） · `005355c4`（命令位置の公開資料なし） · `005355cc`（命令位置の公開資料なし）

~~~diff
- 0053556c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0053556c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005355ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053556c bytes 08e944f9
+ 005355ac bytes 08e946f9
- 00535584 ["INT_ADD", "register:40f0:8", ["const:535584:8", "const:4:8"]]
- 00535584 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005355c4 ["INT_ADD", "register:40f0:8", ["const:5355c4:8", "const:4:8"]]
+ 005355c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535584 bytes 4b891c94
+ 005355c4 bytes 3b8a1c94
- 0053558c ["INT_ADD", "register:40f0:8", ["const:53558c:8", "const:4:8"]]
- 0053558c ["CALL", null, ["callee:00c582e0:8"]]
+ 005355cc ["INT_ADD", "register:40f0:8", ["const:5355cc:8", "const:4:8"]]
+ 005355cc ["CALL", null, ["callee:00c582e0:8"]]
- 0053558c bytes 558a1c94
+ 005355cc bytes 458b1c94
~~~


<a id="compare-a66b0efe5b9cb6240c503495611e72e3"></a>

### [`005355a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md) → [`005355e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005355e0.md) FUN_005355e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005355fc",
      "incomplete_value": true,
      "site": "00535600",
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
      "definition_site": "005355bc",
      "incomplete_value": true,
      "site": "005355c0",
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
      "005355f4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535600",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005355f4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535600",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005355b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355b4) · [`005355cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355cc) · [`005355d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355d4)
- 新版 `005355f4`（命令位置の公開資料なし） · `0053560c`（命令位置の公開資料なし） · `00535614`（命令位置の公開資料なし）

~~~diff
- 005355b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005355b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005355f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355b4 bytes 08e944f9
+ 005355f4 bytes 08e946f9
- 005355cc ["INT_ADD", "register:40f0:8", ["const:5355cc:8", "const:4:8"]]
- 005355cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053560c ["INT_ADD", "register:40f0:8", ["const:53560c:8", "const:4:8"]]
+ 0053560c ["CALL", null, ["callee:00c57eb0:8"]]
- 005355cc bytes 39891c94
+ 0053560c bytes 298a1c94
- 005355d4 ["INT_ADD", "register:40f0:8", ["const:5355d4:8", "const:4:8"]]
- 005355d4 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535614 ["INT_ADD", "register:40f0:8", ["const:535614:8", "const:4:8"]]
+ 00535614 ["CALL", null, ["callee:00c582e0:8"]]
- 005355d4 bytes 438a1c94
+ 00535614 bytes 338b1c94
~~~


<a id="compare-ebffd2f9eacfbb813a2b06c41bcf8f43"></a>

### [`005355e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md) → [`00535628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535628.md) FUN_00535628

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535644",
      "incomplete_value": true,
      "site": "00535648",
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
      "definition_site": "00535604",
      "incomplete_value": true,
      "site": "00535608",
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
      "0053563c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535648",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053563c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535648",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005355fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-005355fc) · [`00535614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-00535614) · [`0053561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-0053561c)
- 新版 `0053563c`（命令位置の公開資料なし） · `00535654`（命令位置の公開資料なし） · `0053565c`（命令位置の公開資料なし）

~~~diff
- 005355fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005355fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053563c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053563c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355fc bytes 08e944f9
+ 0053563c bytes 08e946f9
- 00535614 ["INT_ADD", "register:40f0:8", ["const:535614:8", "const:4:8"]]
- 00535614 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535654 ["INT_ADD", "register:40f0:8", ["const:535654:8", "const:4:8"]]
+ 00535654 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535614 bytes 27891c94
+ 00535654 bytes 178a1c94
- 0053561c ["INT_ADD", "register:40f0:8", ["const:53561c:8", "const:4:8"]]
- 0053561c ["CALL", null, ["callee:00c582e0:8"]]
+ 0053565c ["INT_ADD", "register:40f0:8", ["const:53565c:8", "const:4:8"]]
+ 0053565c ["CALL", null, ["callee:00c582e0:8"]]
- 0053561c bytes 318a1c94
+ 0053565c bytes 218b1c94
~~~


<a id="compare-516ff65a8b0e137d25dabec5f274ad6d"></a>

### [`00535630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md) → [`00535670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535670.md) FUN_00535670

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053568c",
      "incomplete_value": true,
      "site": "00535690",
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
      "definition_site": "0053564c",
      "incomplete_value": true,
      "site": "00535650",
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
      "00535684",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535690",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535684",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535690",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-00535644) · [`0053565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-0053565c) · [`00535664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-00535664)
- 新版 `00535684`（命令位置の公開資料なし） · `0053569c`（命令位置の公開資料なし） · `005356a4`（命令位置の公開資料なし）

~~~diff
- 00535644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535684 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535644 bytes 08e944f9
+ 00535684 bytes 08e946f9
- 0053565c ["INT_ADD", "register:40f0:8", ["const:53565c:8", "const:4:8"]]
- 0053565c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053569c ["INT_ADD", "register:40f0:8", ["const:53569c:8", "const:4:8"]]
+ 0053569c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053565c bytes 15891c94
+ 0053569c bytes 058a1c94
- 00535664 ["INT_ADD", "register:40f0:8", ["const:535664:8", "const:4:8"]]
- 00535664 ["CALL", null, ["callee:00c582e0:8"]]
+ 005356a4 ["INT_ADD", "register:40f0:8", ["const:5356a4:8", "const:4:8"]]
+ 005356a4 ["CALL", null, ["callee:00c582e0:8"]]
- 00535664 bytes 1f8a1c94
+ 005356a4 bytes 0f8b1c94
~~~


<a id="compare-0e6bb51a8d6a3b5d1bd93f94fb88b161"></a>

### [`00535678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md) → [`005356b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005356b8.md) FUN_005356b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005356d4",
      "incomplete_value": true,
      "site": "005356d8",
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
      "definition_site": "00535694",
      "incomplete_value": true,
      "site": "00535698",
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
      "005356cc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005356d8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005356cc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005356d8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-0053568c) · [`005356a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-005356a4) · [`005356ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-005356ac)
- 新版 `005356cc`（命令位置の公開資料なし） · `005356e4`（命令位置の公開資料なし） · `005356ec`（命令位置の公開資料なし）

~~~diff
- 0053568c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0053568c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005356cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005356cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053568c bytes 08e944f9
+ 005356cc bytes 08e946f9
- 005356a4 ["INT_ADD", "register:40f0:8", ["const:5356a4:8", "const:4:8"]]
- 005356a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005356e4 ["INT_ADD", "register:40f0:8", ["const:5356e4:8", "const:4:8"]]
+ 005356e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005356a4 bytes 03891c94
+ 005356e4 bytes f3891c94
- 005356ac ["INT_ADD", "register:40f0:8", ["const:5356ac:8", "const:4:8"]]
- 005356ac ["CALL", null, ["callee:00c582e0:8"]]
+ 005356ec ["INT_ADD", "register:40f0:8", ["const:5356ec:8", "const:4:8"]]
+ 005356ec ["CALL", null, ["callee:00c582e0:8"]]
- 005356ac bytes 0d8a1c94
+ 005356ec bytes fd8a1c94
~~~


<a id="compare-c56ed13a28c44fdeb933ea1c24591754"></a>

### [`005356c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md) → [`00535700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535700.md) FUN_00535700

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053571c",
      "incomplete_value": true,
      "site": "00535720",
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
      "definition_site": "005356dc",
      "incomplete_value": true,
      "site": "005356e0",
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
      "00535714",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535720",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535714",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535720",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005356d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356d4) · [`005356ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356ec) · [`005356f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356f4)
- 新版 `00535714`（命令位置の公開資料なし） · `0053572c`（命令位置の公開資料なし） · `00535734`（命令位置の公開資料なし）

~~~diff
- 005356d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005356d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005356d4 bytes 08e944f9
+ 00535714 bytes 08e946f9
- 005356ec ["INT_ADD", "register:40f0:8", ["const:5356ec:8", "const:4:8"]]
- 005356ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053572c ["INT_ADD", "register:40f0:8", ["const:53572c:8", "const:4:8"]]
+ 0053572c ["CALL", null, ["callee:00c57eb0:8"]]
- 005356ec bytes f1881c94
+ 0053572c bytes e1891c94
- 005356f4 ["INT_ADD", "register:40f0:8", ["const:5356f4:8", "const:4:8"]]
- 005356f4 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535734 ["INT_ADD", "register:40f0:8", ["const:535734:8", "const:4:8"]]
+ 00535734 ["CALL", null, ["callee:00c582e0:8"]]
- 005356f4 bytes fb891c94
+ 00535734 bytes eb8a1c94
~~~


<a id="compare-1716a476e59b620e82c270931180c767"></a>

### [`00535708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md) → [`00535748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535748.md) FUN_00535748

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535764",
      "incomplete_value": true,
      "site": "00535768",
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
      "definition_site": "00535724",
      "incomplete_value": true,
      "site": "00535728",
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
      "0053575c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535768",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053575c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535768",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053571c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-0053571c) · [`00535734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-00535734) · [`0053573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-0053573c)
- 新版 `0053575c`（命令位置の公開資料なし） · `00535774`（命令位置の公開資料なし） · `0053577c`（命令位置の公開資料なし）

~~~diff
- 0053571c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 0053571c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053575c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053575c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053571c bytes 08e944f9
+ 0053575c bytes 08e946f9
- 00535734 ["INT_ADD", "register:40f0:8", ["const:535734:8", "const:4:8"]]
- 00535734 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535774 ["INT_ADD", "register:40f0:8", ["const:535774:8", "const:4:8"]]
+ 00535774 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535734 bytes df881c94
+ 00535774 bytes cf891c94
- 0053573c ["INT_ADD", "register:40f0:8", ["const:53573c:8", "const:4:8"]]
- 0053573c ["CALL", null, ["callee:00c582e0:8"]]
+ 0053577c ["INT_ADD", "register:40f0:8", ["const:53577c:8", "const:4:8"]]
+ 0053577c ["CALL", null, ["callee:00c582e0:8"]]
- 0053573c bytes e9891c94
+ 0053577c bytes d98a1c94
~~~


<a id="compare-32ffeaa0cc72cb7598fd7e0cd82094a8"></a>

### [`00535750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md) → [`00535790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535790.md) FUN_00535790

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005357ac",
      "incomplete_value": true,
      "site": "005357b0",
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
      "definition_site": "0053576c",
      "incomplete_value": true,
      "site": "00535770",
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
      "005357a4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005357b0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005357a4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005357b0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-00535764) · [`0053577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-0053577c) · [`00535784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-00535784)
- 新版 `005357a4`（命令位置の公開資料なし） · `005357bc`（命令位置の公開資料なし） · `005357c4`（命令位置の公開資料なし）

~~~diff
- 00535764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005357a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535764 bytes 08e944f9
+ 005357a4 bytes 08e946f9
- 0053577c ["INT_ADD", "register:40f0:8", ["const:53577c:8", "const:4:8"]]
- 0053577c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005357bc ["INT_ADD", "register:40f0:8", ["const:5357bc:8", "const:4:8"]]
+ 005357bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0053577c bytes cd881c94
+ 005357bc bytes bd891c94
- 00535784 ["INT_ADD", "register:40f0:8", ["const:535784:8", "const:4:8"]]
- 00535784 ["CALL", null, ["callee:00c582e0:8"]]
+ 005357c4 ["INT_ADD", "register:40f0:8", ["const:5357c4:8", "const:4:8"]]
+ 005357c4 ["CALL", null, ["callee:00c582e0:8"]]
- 00535784 bytes d7891c94
+ 005357c4 bytes c78a1c94
~~~


<a id="compare-d26eba243c0720107da6beb98f1ca154"></a>

### [`00535798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md) → [`005357d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005357d8.md) FUN_005357d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005357f4",
      "incomplete_value": true,
      "site": "005357f8",
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
      "definition_site": "005357b4",
      "incomplete_value": true,
      "site": "005357b8",
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
      "005357ec",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005357f8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005357ec",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005357f8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005357ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357ac) · [`005357c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357c4) · [`005357cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357cc)
- 新版 `005357ec`（命令位置の公開資料なし） · `00535804`（命令位置の公開資料なし） · `0053580c`（命令位置の公開資料なし）

~~~diff
- 005357ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005357ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005357ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005357ac bytes 08e944f9
+ 005357ec bytes 08e946f9
- 005357c4 ["INT_ADD", "register:40f0:8", ["const:5357c4:8", "const:4:8"]]
- 005357c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535804 ["INT_ADD", "register:40f0:8", ["const:535804:8", "const:4:8"]]
+ 00535804 ["CALL", null, ["callee:00c57eb0:8"]]
- 005357c4 bytes bb881c94
+ 00535804 bytes ab891c94
- 005357cc ["INT_ADD", "register:40f0:8", ["const:5357cc:8", "const:4:8"]]
- 005357cc ["CALL", null, ["callee:00c582e0:8"]]
+ 0053580c ["INT_ADD", "register:40f0:8", ["const:53580c:8", "const:4:8"]]
+ 0053580c ["CALL", null, ["callee:00c582e0:8"]]
- 005357cc bytes c5891c94
+ 0053580c bytes b58a1c94
~~~


<a id="compare-3596d2fa9e1ac13a7aa5e0defebfa8b9"></a>

### [`005357e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md) → [`00535820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535820.md) FUN_00535820

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053583c",
      "incomplete_value": true,
      "site": "00535840",
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
      "definition_site": "005357fc",
      "incomplete_value": true,
      "site": "00535800",
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
      "00535834",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535840",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535834",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535840",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005357f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-005357f4) · [`0053580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-0053580c) · [`00535814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-00535814)
- 新版 `00535834`（命令位置の公開資料なし） · `0053584c`（命令位置の公開資料なし） · `00535854`（命令位置の公開資料なし）

~~~diff
- 005357f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005357f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005357f4 bytes 08e944f9
+ 00535834 bytes 08e946f9
- 0053580c ["INT_ADD", "register:40f0:8", ["const:53580c:8", "const:4:8"]]
- 0053580c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053584c ["INT_ADD", "register:40f0:8", ["const:53584c:8", "const:4:8"]]
+ 0053584c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053580c bytes a9881c94
+ 0053584c bytes 99891c94
- 00535814 ["INT_ADD", "register:40f0:8", ["const:535814:8", "const:4:8"]]
- 00535814 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535854 ["INT_ADD", "register:40f0:8", ["const:535854:8", "const:4:8"]]
+ 00535854 ["CALL", null, ["callee:00c582e0:8"]]
- 00535814 bytes b3891c94
+ 00535854 bytes a38a1c94
~~~


<a id="compare-b3b5df88dd83493170be6277395ac9ca"></a>

### [`0053586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md) → [`005358ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358ac.md) FUN_005358ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005358c8",
      "incomplete_value": true,
      "site": "005358cc",
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
      "definition_site": "00535888",
      "incomplete_value": true,
      "site": "0053588c",
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
      "005358c0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005358cc",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005358c0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005358cc",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-00535880) · [`00535898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-00535898) · [`005358a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-005358a0)
- 新版 `005358c0`（命令位置の公開資料なし） · `005358d8`（命令位置の公開資料なし） · `005358e0`（命令位置の公開資料なし）

~~~diff
- 00535880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005358c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 005358c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535880 bytes 08e944f9
+ 005358c0 bytes 08e946f9
- 00535898 ["INT_ADD", "register:40f0:8", ["const:535898:8", "const:4:8"]]
- 00535898 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005358d8 ["INT_ADD", "register:40f0:8", ["const:5358d8:8", "const:4:8"]]
+ 005358d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535898 bytes 86881c94
+ 005358d8 bytes 76891c94
- 005358a0 ["INT_ADD", "register:40f0:8", ["const:5358a0:8", "const:4:8"]]
- 005358a0 ["CALL", null, ["callee:00c582e0:8"]]
+ 005358e0 ["INT_ADD", "register:40f0:8", ["const:5358e0:8", "const:4:8"]]
+ 005358e0 ["CALL", null, ["callee:00c582e0:8"]]
- 005358a0 bytes 90891c94
+ 005358e0 bytes 808a1c94
~~~


<a id="compare-ffea5ad02ed34a2e073e8142fa794bc8"></a>

### [`005358b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md) → [`005358f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358f4.md) FUN_005358f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535910",
      "incomplete_value": true,
      "site": "00535914",
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
      "definition_site": "005358d0",
      "incomplete_value": true,
      "site": "005358d4",
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
      "00535908",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535914",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535908",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535914",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005358c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358c8) · [`005358e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358e0) · [`005358e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358e8)
- 新版 `00535908`（命令位置の公開資料なし） · `00535920`（命令位置の公開資料なし） · `00535928`（命令位置の公開資料なし）

~~~diff
- 005358c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 005358c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535908 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535908 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005358c8 bytes 08e944f9
+ 00535908 bytes 08e946f9
- 005358e0 ["INT_ADD", "register:40f0:8", ["const:5358e0:8", "const:4:8"]]
- 005358e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535920 ["INT_ADD", "register:40f0:8", ["const:535920:8", "const:4:8"]]
+ 00535920 ["CALL", null, ["callee:00c57eb0:8"]]
- 005358e0 bytes 74881c94
+ 00535920 bytes 64891c94
- 005358e8 ["INT_ADD", "register:40f0:8", ["const:5358e8:8", "const:4:8"]]
- 005358e8 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535928 ["INT_ADD", "register:40f0:8", ["const:535928:8", "const:4:8"]]
+ 00535928 ["CALL", null, ["callee:00c582e0:8"]]
- 005358e8 bytes 7e891c94
+ 00535928 bytes 6e8a1c94
~~~


<a id="compare-aee59dffe5a6a9fecc9bb6bf0ec66090"></a>

### [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) → [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) FUN_00535b6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 35件 [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) [`004a4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md) [`004a5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md) [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) [`004a7bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 35件 [`004a21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) [`004a502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md) [`004a5ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md) [`004a762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md) [`004a7c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00535b78",
      "incomplete_value": false,
      "site": "00535b7c",
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
      "definition_site": "00535b38",
      "incomplete_value": false,
      "site": "00535b3c",
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
      "00535b78",
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
      "00535b78",
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

- 旧版 [`00535b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md#insn-00535b3c) · [`00535b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md#insn-00535b38)
- 新版 `00535b7c`（命令位置の公開資料なし） · `00535b78`（命令位置の公開資料なし）

~~~diff
- 00535b3c ["INT_ADD", "register:40f0:8", ["const:535b3c:8", "const:4:8"]]
- 00535b3c ["CALL", null, ["callee:0043b778:8"]]
+ 00535b7c ["INT_ADD", "register:40f0:8", ["const:535b7c:8", "const:4:8"]]
+ 00535b7c ["CALL", null, ["callee:0043b778:8"]]
- 00535b3c bytes ff16fc97
+ 00535b7c bytes ff16fc97
- 00535b38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00535b38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535b38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535b38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535b78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00535b78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535b78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535b78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535b38 bytes 00303c91
+ 00535b78 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0df07a3f19652cc4671f395484736071"></a>

### [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) → [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) FUN_00535b80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`004a6ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6ebc.md) [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) [`004c24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 32件 [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`004a6efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6efc.md) [`004a8e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md) [`004c24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535be8",
      "incomplete_value": true,
      "site": "00535be8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535ba8",
      "incomplete_value": true,
      "site": "00535ba8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535c24",
      "incomplete_value": true,
      "site": "00535c24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535be4",
      "incomplete_value": true,
      "site": "00535be4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "00535bd8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00535c14",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00535bd8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00535c14",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535ba8) · [`00535be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535be4) · [`00535b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535b98)
- 新版 `00535be8`（命令位置の公開資料なし） · `00535c24`（命令位置の公開資料なし） · `00535bd8`（命令位置の公開資料なし）

~~~diff
- 00535ba8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535ba8 ["INT_ADD", "register:40f0:8", ["const:535ba8:8", "const:4:8"]]
- 00535ba8 ["CALLIND", null, ["register:0:8"]]
+ 00535be8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535be8 ["INT_ADD", "register:40f0:8", ["const:535be8:8", "const:4:8"]]
+ 00535be8 ["CALLIND", null, ["register:0:8"]]
- 00535ba8 bytes 20013fd6
+ 00535be8 bytes 20013fd6
- 00535be4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535be4 ["INT_ADD", "register:40f0:8", ["const:535be4:8", "const:4:8"]]
- 00535be4 ["CALLIND", null, ["register:0:8"]]
+ 00535c24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535c24 ["INT_ADD", "register:40f0:8", ["const:535c24:8", "const:4:8"]]
+ 00535c24 ["CALLIND", null, ["register:0:8"]]
- 00535be4 bytes 20013fd6
+ 00535c24 bytes 20013fd6
- 00535b98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00535b98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535bd8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 00535bd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00535b98 bytes a99e41f9
+ 00535bd8 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b9cb6c1f1f54da4e144b694dd87d80"></a>

### [`00535c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md) → [`00535c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535c5c.md) FUN_00535c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535c78",
      "incomplete_value": true,
      "site": "00535c7c",
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
      "definition_site": "00535c38",
      "incomplete_value": true,
      "site": "00535c3c",
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
      "00535c70",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c7c",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535c70",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c7c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c30) · [`00535c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c48) · [`00535c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c50)
- 新版 `00535c70`（命令位置の公開資料なし） · `00535c88`（命令位置の公開資料なし） · `00535c90`（命令位置の公開資料なし）

~~~diff
- 00535c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535c30 bytes 08e944f9
+ 00535c70 bytes 08e946f9
- 00535c48 ["INT_ADD", "register:40f0:8", ["const:535c48:8", "const:4:8"]]
- 00535c48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535c88 ["INT_ADD", "register:40f0:8", ["const:535c88:8", "const:4:8"]]
+ 00535c88 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535c48 bytes 9a871c94
+ 00535c88 bytes 8a881c94
- 00535c50 ["INT_ADD", "register:40f0:8", ["const:535c50:8", "const:4:8"]]
- 00535c50 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535c90 ["INT_ADD", "register:40f0:8", ["const:535c90:8", "const:4:8"]]
+ 00535c90 ["CALL", null, ["callee:00c582e0:8"]]
- 00535c50 bytes a4881c94
+ 00535c90 bytes 94891c94
~~~


<a id="compare-ccb259e879a029500b94e669c47032a5"></a>

### [`00535c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md) → [`00535ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ca4.md) FUN_00535ca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535d64",
      "incomplete_value": true,
      "site": "00535d64",
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
      "definition_site": "00535d24",
      "incomplete_value": true,
      "site": "00535d24",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00535db0",
      "incomplete_value": false,
      "site": "00535db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535d70",
      "incomplete_value": false,
      "site": "00535d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535cc4",
      "incomplete_value": false,
      "site": "00535cd8",
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
            "const:24c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535c84",
      "incomplete_value": false,
      "site": "00535c98",
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
            "const:20c:8"
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
      "00535cc4",
      "PARAM",
      [
        "storage",
        "002c120c",
        null,
        "string"
      ]
    ],
    [
      "00535ce0",
      "PARAM",
      [
        "storage",
        "002b0987",
        null,
        null
      ]
    ],
    [
      "00535d50",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00535cc4",
      "PARAM",
      [
        "storage",
        "002c124c",
        null,
        "string"
      ]
    ],
    [
      "00535ce0",
      "PARAM",
      [
        "storage",
        "002b09c7",
        null,
        null
      ]
    ],
    [
      "00535d50",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535c98) · [`00535ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535ca8) · [`00535c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535c84)
- 新版 `00535cd8`（命令位置の公開資料なし） · `00535ce8`（命令位置の公開資料なし） · `00535cc4`（命令位置の公開資料なし）

~~~diff
- 00535c98 ["INT_ADD", "register:40f0:8", ["const:535c98:8", "const:4:8"]]
- 00535c98 ["CALL", null, ["callee:00c580b0:8"]]
+ 00535cd8 ["INT_ADD", "register:40f0:8", ["const:535cd8:8", "const:4:8"]]
+ 00535cd8 ["CALL", null, ["callee:00c580b0:8"]]
- 00535c98 bytes 06881c94
+ 00535cd8 bytes f6881c94
- 00535ca8 ["INT_ADD", "register:40f0:8", ["const:535ca8:8", "const:4:8"]]
- 00535ca8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00535ce8 ["INT_ADD", "register:40f0:8", ["const:535ce8:8", "const:4:8"]]
+ 00535ce8 ["CALL", null, ["callee:00c57f70:8"]]
- 00535ca8 bytes b2871c94
+ 00535ce8 bytes a2881c94
- 00535c84 ["COPY", "tmp:0:8", ["const:20c:8"]]
- 00535c84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535c84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535c84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535cc4 ["COPY", "tmp:0:8", ["const:24c:8"]]
+ 00535cc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535cc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535cc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535c84 bytes 00300891
+ 00535cc4 bytes 00300991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d87d8ee697ad3b478f2a20e3f616dd3"></a>

### [`00535e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md) → [`00535eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535eac.md) FUN_00535eac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535ec8",
      "incomplete_value": true,
      "site": "00535ecc",
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
      "definition_site": "00535e88",
      "incomplete_value": true,
      "site": "00535e8c",
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
      "00535ec0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ecc",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535ec0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ecc",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535e80) · [`00535e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535e98) · [`00535ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535ea0)
- 新版 `00535ec0`（命令位置の公開資料なし） · `00535ed8`（命令位置の公開資料なし） · `00535ee0`（命令位置の公開資料なし）

~~~diff
- 00535e80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535e80 bytes 08e944f9
+ 00535ec0 bytes 08e946f9
- 00535e98 ["INT_ADD", "register:40f0:8", ["const:535e98:8", "const:4:8"]]
- 00535e98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535ed8 ["INT_ADD", "register:40f0:8", ["const:535ed8:8", "const:4:8"]]
+ 00535ed8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535e98 bytes 06871c94
+ 00535ed8 bytes f6871c94
- 00535ea0 ["INT_ADD", "register:40f0:8", ["const:535ea0:8", "const:4:8"]]
- 00535ea0 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535ee0 ["INT_ADD", "register:40f0:8", ["const:535ee0:8", "const:4:8"]]
+ 00535ee0 ["CALL", null, ["callee:00c582e0:8"]]
- 00535ea0 bytes 10881c94
+ 00535ee0 bytes 00891c94
~~~


<a id="compare-89386642351e8a8c2f1afd6ffa0071dc"></a>

### [`00535eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md) → [`00535ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ef4.md) FUN_00535ef4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535f10",
      "incomplete_value": true,
      "site": "00535f14",
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
      "definition_site": "00535ed0",
      "incomplete_value": true,
      "site": "00535ed4",
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
      "00535f08",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f14",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535f08",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f14",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ec8) · [`00535ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ee0) · [`00535ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ee8)
- 新版 `00535f08`（命令位置の公開資料なし） · `00535f20`（命令位置の公開資料なし） · `00535f28`（命令位置の公開資料なし）

~~~diff
- 00535ec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00535ec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535f08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00535f08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535ec8 bytes 08e944f9
+ 00535f08 bytes 08e946f9
- 00535ee0 ["INT_ADD", "register:40f0:8", ["const:535ee0:8", "const:4:8"]]
- 00535ee0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00535f20 ["INT_ADD", "register:40f0:8", ["const:535f20:8", "const:4:8"]]
+ 00535f20 ["CALL", null, ["callee:00c57eb0:8"]]
- 00535ee0 bytes f4861c94
+ 00535f20 bytes e4871c94
- 00535ee8 ["INT_ADD", "register:40f0:8", ["const:535ee8:8", "const:4:8"]]
- 00535ee8 ["CALL", null, ["callee:00c582e0:8"]]
+ 00535f28 ["INT_ADD", "register:40f0:8", ["const:535f28:8", "const:4:8"]]
+ 00535f28 ["CALL", null, ["callee:00c582e0:8"]]
- 00535ee8 bytes fe871c94
+ 00535f28 bytes ee881c94
~~~


<a id="compare-5bb70308f1d03bd61fb4f1605e93b328"></a>

### [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) → [`00535f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md) FUN_00535f64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004f8e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md) [`004f8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535f8c",
      "incomplete_value": false,
      "site": "00535f9c",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535f4c",
      "incomplete_value": false,
      "site": "00535f5c",
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
            "const:e80:8"
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
      "definition_site": "00535fb4",
      "incomplete_value": false,
      "site": "00535fb8",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535f74",
      "incomplete_value": false,
      "site": "00535f78",
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
            "const:e90:8"
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
      "definition_site": "00535fc8",
      "incomplete_value": false,
      "site": "00535fdc",
      "value": [
        "leaf",
        "const:4f8f6c:8"
      ]
    },
    "old": {
      "definition_site": "00535f88",
      "incomplete_value": false,
      "site": "00535f9c",
      "value": [
        "leaf",
        "const:4f8f2c:8"
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
      "00535f7c",
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      "00535f8c",
      "PARAM",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "00535fb4",
      "PARAM",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00535f7c",
      "READ",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ],
    [
      "00535f8c",
      "PARAM",
      [
        "storage",
        "00ca5280",
        null,
        "undefined8"
      ]
    ],
    [
      "00535fb4",
      "PARAM",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f5c) · [`00535f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f78) · [`00535f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f9c)
- 新版 `00535f9c`（命令位置の公開資料なし） · `00535fb8`（命令位置の公開資料なし） · `00535fdc`（命令位置の公開資料なし）

~~~diff
- 00535f5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00535f5c ["INT_ADD", "register:40f0:8", ["const:535f5c:8", "const:4:8"]]
- 00535f5c ["CALLIND", null, ["register:0:8"]]
+ 00535f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535f9c ["INT_ADD", "register:40f0:8", ["const:535f9c:8", "const:4:8"]]
+ 00535f9c ["CALLIND", null, ["register:0:8"]]
- 00535f5c bytes 00013fd6
+ 00535f9c bytes 00013fd6
- 00535f78 ["INT_ADD", "register:40f0:8", ["const:535f78:8", "const:4:8"]]
- 00535f78 ["CALL", null, ["callee:00c57e50:8"]]
+ 00535fb8 ["INT_ADD", "register:40f0:8", ["const:535fb8:8", "const:4:8"]]
+ 00535fb8 ["CALL", null, ["callee:00c57e50:8"]]
- 00535f78 bytes b6861c94
+ 00535fb8 bytes a6871c94
- 00535f9c ["INT_ADD", "register:40f0:8", ["const:535f9c:8", "const:4:8"]]
- 00535f9c ["CALL", null, ["callee:00c57e30:8"]]
+ 00535fdc ["INT_ADD", "register:40f0:8", ["const:535fdc:8", "const:4:8"]]
+ 00535fdc ["CALL", null, ["callee:00c57e30:8"]]
- 00535f9c bytes a5861c94
+ 00535fdc bytes 95871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-094c1eb3b4d50c08e4eeee922a7b788b"></a>

### [`00535fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md) → [`00536010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md) FUN_00536010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004c5d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5d74.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md)
- 新版 呼出元 3件 [`004c5db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5db4.md) [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`004e34c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e34c4.md) · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "00536108",
      "incomplete_value": true,
      "site": "00536114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005360c8",
      "incomplete_value": true,
      "site": "005360d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
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
      "definition_site": "00536104",
      "incomplete_value": false,
      "site": "00536114",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005360c4",
      "incomplete_value": false,
      "site": "005360d4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00536104",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00536108",
      "READ",
      [
        "storage",
        "00c9aa38",
        null,
        "pointer"
      ]
    ],
    [
      "00536108",
      "PARAM",
      [
        "storage",
        "00c66a28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00536104",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00536108",
      "READ",
      [
        "storage",
        "00c9ae38",
        null,
        "pointer"
      ]
    ],
    [
      "00536108",
      "PARAM",
      [
        "storage",
        "00c66e28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-00536094) · [`005360d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-005360d4) · [`00536008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-00536008)
- 新版 `005360d4`（命令位置の公開資料なし） · `00536114`（命令位置の公開資料なし） · `00536048`（命令位置の公開資料なし）

~~~diff
- 00536094 ["COPY", "register:0:8", ["register:4050:8"]]
- 00536094 ["INT_ADD", "register:40f0:8", ["const:536094:8", "const:4:8"]]
- 00536094 ["CALLIND", null, ["register:0:8"]]
+ 005360d4 ["COPY", "register:0:8", ["register:4050:8"]]
+ 005360d4 ["INT_ADD", "register:40f0:8", ["const:5360d4:8", "const:4:8"]]
+ 005360d4 ["CALLIND", null, ["register:0:8"]]
- 00536094 bytes 40013fd6
+ 005360d4 bytes 40013fd6
- 005360d4 ["INT_ADD", "register:40f0:8", ["const:5360d4:8", "const:4:8"]]
- 005360d4 ["CALL", null, ["callee:00c57f10:8"]]
+ 00536114 ["INT_ADD", "register:40f0:8", ["const:536114:8", "const:4:8"]]
+ 00536114 ["CALL", null, ["callee:00c57f10:8"]]
- 005360d4 bytes 8f861c94
+ 00536114 bytes 7f871c94
- 00536008 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536008 ["INT_ADD", "register:40f0:8", ["const:536008:8", "const:4:8"]]
- 00536008 ["CALLIND", null, ["register:0:8"]]
+ 00536048 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536048 ["INT_ADD", "register:40f0:8", ["const:536048:8", "const:4:8"]]
+ 00536048 ["CALLIND", null, ["register:0:8"]]
- 00536008 bytes 20013fd6
+ 00536048 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6f632f718558717ad336e5dcfd8bc1"></a>

### [`00536124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md) → [`00536164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536164.md) FUN_00536164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536180",
      "incomplete_value": true,
      "site": "00536184",
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
      "definition_site": "00536140",
      "incomplete_value": true,
      "site": "00536144",
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
      "00536178",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00536184",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00536178",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00536184",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536138) · [`00536150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536150) · [`00536158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536158)
- 新版 `00536178`（命令位置の公開資料なし） · `00536190`（命令位置の公開資料なし） · `00536198`（命令位置の公開資料なし）

~~~diff
- 00536138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00536138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00536178 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00536138 bytes 08e944f9
+ 00536178 bytes 08e946f9
- 00536150 ["INT_ADD", "register:40f0:8", ["const:536150:8", "const:4:8"]]
- 00536150 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00536190 ["INT_ADD", "register:40f0:8", ["const:536190:8", "const:4:8"]]
+ 00536190 ["CALL", null, ["callee:00c57eb0:8"]]
- 00536150 bytes 58861c94
+ 00536190 bytes 48871c94
- 00536158 ["INT_ADD", "register:40f0:8", ["const:536158:8", "const:4:8"]]
- 00536158 ["CALL", null, ["callee:00c582e0:8"]]
+ 00536198 ["INT_ADD", "register:40f0:8", ["const:536198:8", "const:4:8"]]
+ 00536198 ["CALL", null, ["callee:00c582e0:8"]]
- 00536158 bytes 62871c94
+ 00536198 bytes 52881c94
~~~


<a id="compare-cbb4989535f4b87dca4d16974113b2a6"></a>

### [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) → [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) FUN_005361ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ce954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md) [`004f5a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) [`004f6984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) [`004f6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) · 呼出先 8件 [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 4件 [`004ce994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce994.md) [`004f5a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md) [`004f69c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md) [`004f6a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md) · 呼出先 8件 [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005362a0",
      "incomplete_value": true,
      "site": "005362a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00536260",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005362a4",
      "incomplete_value": true,
      "site": "005362a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00536264",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005362a0",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "005362a0",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005362a4",
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
      "005362a0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "005362a0",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005362a4",
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

- 旧版 [`00536268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-00536268) · [`005361bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-005361bc) · [`005361e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-005361e8)
- 新版 `005362a8`（命令位置の公開資料なし） · `005361fc`（命令位置の公開資料なし） · `00536228`（命令位置の公開資料なし）

~~~diff
- 00536268 ["INT_ADD", "register:40f0:8", ["const:536268:8", "const:4:8"]]
- 00536268 ["CALL", null, ["callee:00c57f10:8"]]
+ 005362a8 ["INT_ADD", "register:40f0:8", ["const:5362a8:8", "const:4:8"]]
+ 005362a8 ["CALL", null, ["callee:00c57f10:8"]]
- 00536268 bytes 2a861c94
+ 005362a8 bytes 1a871c94
- 005361bc ["INT_ADD", "register:40f0:8", ["const:5361bc:8", "const:4:8"]]
- 005361bc ["CALL", null, ["callee:00c58a30:8"]]
+ 005361fc ["INT_ADD", "register:40f0:8", ["const:5361fc:8", "const:4:8"]]
+ 005361fc ["CALL", null, ["callee:00c58a30:8"]]
- 005361bc bytes 1d891c94
+ 005361fc bytes 0d8a1c94
- 005361e8 ["INT_ADD", "register:40f0:8", ["const:5361e8:8", "const:4:8"]]
- 005361e8 ["CALL", null, ["callee:00c58000:8"]]
+ 00536228 ["INT_ADD", "register:40f0:8", ["const:536228:8", "const:4:8"]]
+ 00536228 ["CALL", null, ["callee:00c58000:8"]]
- 005361e8 bytes 86861c94
+ 00536228 bytes 76871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78d5e34678c2858e40896f6d225cdff7"></a>

### [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) → [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) FUN_00536334

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 4件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00536340",
      "incomplete_value": false,
      "site": "00536344",
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
      "definition_site": "00536300",
      "incomplete_value": false,
      "site": "00536304",
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
      "00536340",
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
      "00536340",
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

- 旧版 [`00536304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md#insn-00536304) · [`00536300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md#insn-00536300)
- 新版 `00536344`（命令位置の公開資料なし） · `00536340`（命令位置の公開資料なし）

~~~diff
- 00536304 ["INT_ADD", "register:40f0:8", ["const:536304:8", "const:4:8"]]
- 00536304 ["CALL", null, ["callee:0043b778:8"]]
+ 00536344 ["INT_ADD", "register:40f0:8", ["const:536344:8", "const:4:8"]]
+ 00536344 ["CALL", null, ["callee:0043b778:8"]]
- 00536304 bytes 0d15fc97
+ 00536344 bytes 0d15fc97
- 00536300 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00536300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00536300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00536300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00536340 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00536340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00536340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00536340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00536300 bytes 00303c91
+ 00536340 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d51517d57c5f7e57f32075ddf3ec05"></a>

### [`00536674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md) → [`005366b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md) FUN_005366b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00549a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005366fc",
      "incomplete_value": true,
      "site": "005366fc",
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
      "definition_site": "005366bc",
      "incomplete_value": true,
      "site": "005366bc",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005366fc",
      "incomplete_value": true,
      "site": "005366fc",
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
      "definition_site": "005366bc",
      "incomplete_value": true,
      "site": "005366bc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005366dc",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "005366e8",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "005366fc",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005366dc",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "005366e8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005366fc",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md#insn-0053669c) · [`005366a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md#insn-005366a4) · [`005366a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md#insn-005366a8)
- 新版 `005366dc`（命令位置の公開資料なし） · `005366e8`（命令位置の公開資料なし）

~~~diff
- 0053669c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 0053669c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005366dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 005366dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053669c bytes 089d44f9
+ 005366dc bytes 089d46f9
- 005366a4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005366a4 bytes f30300aa
- 005366a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 005366a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005366e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 005366e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005366a8 bytes 29a144f9
+ 005366e8 bytes 29a146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dd7d0955e4686071e410bb3fd2747ff"></a>

### [`0053679c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053679c.md) → [`005367dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005367dc.md) FUN_005367dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c59b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c59f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536828",
      "incomplete_value": true,
      "site": "00536828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:412:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005367e8",
      "incomplete_value": true,
      "site": "005367e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d2:8"
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
      "definition_site": "00536818",
      "incomplete_value": true,
      "site": "0053682c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005367d8",
      "incomplete_value": true,
      "site": "005367ec",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536854",
      "incomplete_value": true,
      "site": "00536860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536814",
      "incomplete_value": true,
      "site": "00536820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00536810",
      "READ",
      [
        "storage",
        "002b73d2",
        null,
        "string"
      ]
    ],
    [
      "00536818",
      "READ",
      [
        "storage",
        "002b73d9",
        null,
        "string"
      ]
    ],
    [
      "00536850",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00536810",
      "READ",
      [
        "storage",
        "002b7412",
        null,
        "string"
      ]
    ],
    [
      "00536818",
      "READ",
      [
        "storage",
        "002b7419",
        null,
        "string"
      ]
    ],
    [
      "00536850",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053679c.md#insn-00536820) · [`005367c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053679c.md#insn-005367c0) · [`005367cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053679c.md#insn-005367cc)
- 新版 `00536860`（命令位置の公開資料なし） · `00536800`（命令位置の公開資料なし） · `0053680c`（命令位置の公開資料なし）

~~~diff
- 00536820 ["INT_ADD", "register:40f0:8", ["const:536820:8", "const:4:8"]]
- 00536820 ["CALL", null, ["callee:00c57f10:8"]]
+ 00536860 ["INT_ADD", "register:40f0:8", ["const:536860:8", "const:4:8"]]
+ 00536860 ["CALL", null, ["callee:00c57f10:8"]]
- 00536820 bytes bc841c94
+ 00536860 bytes ac851c94
- 005367c0 ["INT_ADD", "register:40f0:8", ["const:5367c0:8", "const:4:8"]]
- 005367c0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00536800 ["INT_ADD", "register:40f0:8", ["const:536800:8", "const:4:8"]]
+ 00536800 ["CALL", null, ["callee:00c57ef0:8"]]
- 005367c0 bytes cc841c94
+ 00536800 bytes bc851c94
- 005367cc ["COPY", "tmp:0:8", ["const:3d2:8"]]
- 005367cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005367cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005367cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053680c ["COPY", "tmp:0:8", ["const:412:8"]]
+ 0053680c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053680c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053680c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005367cc bytes 29490f91
+ 0053680c bytes 29491091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512307c92f62e0a19a3eeb619f422296"></a>

### [`005369e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005369e8.md) → [`00536a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536a28.md) FUN_00536a28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545938.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545978.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536a8c",
      "incomplete_value": true,
      "site": "00536a90",
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
      "definition_site": "00536a4c",
      "incomplete_value": true,
      "site": "00536a50",
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
      "definition_site": "00536aac",
      "incomplete_value": true,
      "site": "00536ab0",
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
      "definition_site": "00536a6c",
      "incomplete_value": true,
      "site": "00536a70",
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
      "definition_site": "00536ac8",
      "incomplete_value": true,
      "site": "00536acc",
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
      "definition_site": "00536a88",
      "incomplete_value": true,
      "site": "00536a8c",
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
      "00536a44",
      "PARAM",
      [
        "storage",
        "002bc6e3",
        null,
        "string"
      ]
    ],
    [
      "00536a5c",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "00536a70",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00536a44",
      "PARAM",
      [
        "storage",
        "002bc723",
        null,
        "string"
      ]
    ],
    [
      "00536a5c",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "00536a70",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005369e8.md#insn-00536a14) · [`00536a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005369e8.md#insn-00536a28) · [`00536a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005369e8.md#insn-00536a30)
- 新版 `00536a54`（命令位置の公開資料なし） · `00536a68`（命令位置の公開資料なし） · `00536a70`（命令位置の公開資料なし）

~~~diff
- 00536a14 ["INT_ADD", "register:40f0:8", ["const:536a14:8", "const:4:8"]]
- 00536a14 ["CALL", null, ["callee:00c580b0:8"]]
+ 00536a54 ["INT_ADD", "register:40f0:8", ["const:536a54:8", "const:4:8"]]
+ 00536a54 ["CALL", null, ["callee:00c580b0:8"]]
- 00536a14 bytes a7841c94
+ 00536a54 bytes 97851c94
- 00536a28 ["INT_ADD", "register:40f0:8", ["const:536a28:8", "const:4:8"]]
- 00536a28 ["CALL", null, ["callee:00c580b0:8"]]
+ 00536a68 ["INT_ADD", "register:40f0:8", ["const:536a68:8", "const:4:8"]]
+ 00536a68 ["CALL", null, ["callee:00c580b0:8"]]
- 00536a28 bytes a2841c94
+ 00536a68 bytes 92851c94
- 00536a30 ["COPY", "tmp:0:8", ["const:372:8"]]
- 00536a30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00536a30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00536a30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00536a70 ["COPY", "tmp:0:8", ["const:44e:8"]]
+ 00536a70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00536a70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00536a70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00536a30 bytes 21c80d91
+ 00536a70 bytes 21381191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56439b591454a699defd2b0bcdeaf8fe"></a>

### [`00536af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md) → [`00536b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536b38.md) FUN_00536b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md) [`00c58680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a20.md) [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00536bf8",
      "incomplete_value": true,
      "site": "00536bf8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536bb8",
      "incomplete_value": true,
      "site": "00536bb8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00536c3c",
      "incomplete_value": true,
      "site": "00536c3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536bfc",
      "incomplete_value": true,
      "site": "00536bfc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00536be8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00536c2c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00536be8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00536c2c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md#insn-00536b78) · [`00536bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md#insn-00536bb8) · [`00536bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536af8.md#insn-00536bfc)
- 新版 `00536bb8`（命令位置の公開資料なし） · `00536bf8`（命令位置の公開資料なし） · `00536c3c`（命令位置の公開資料なし）

~~~diff
- 00536b78 ["INT_ADD", "register:40f0:8", ["const:536b78:8", "const:4:8"]]
- 00536b78 ["CALL", null, ["callee:00c58a20:8"]]
+ 00536bb8 ["INT_ADD", "register:40f0:8", ["const:536bb8:8", "const:4:8"]]
+ 00536bb8 ["CALL", null, ["callee:00c58a20:8"]]
- 00536b78 bytes aa861c94
+ 00536bb8 bytes 9a871c94
- 00536bb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536bb8 ["INT_ADD", "register:40f0:8", ["const:536bb8:8", "const:4:8"]]
- 00536bb8 ["CALLIND", null, ["register:0:8"]]
+ 00536bf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536bf8 ["INT_ADD", "register:40f0:8", ["const:536bf8:8", "const:4:8"]]
+ 00536bf8 ["CALLIND", null, ["register:0:8"]]
- 00536bb8 bytes 20013fd6
+ 00536bf8 bytes 20013fd6
- 00536bfc ["COPY", "register:0:8", ["register:4048:8"]]
- 00536bfc ["INT_ADD", "register:40f0:8", ["const:536bfc:8", "const:4:8"]]
- 00536bfc ["CALLIND", null, ["register:0:8"]]
+ 00536c3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536c3c ["INT_ADD", "register:40f0:8", ["const:536c3c:8", "const:4:8"]]
+ 00536c3c ["CALLIND", null, ["register:0:8"]]
- 00536bfc bytes 20013fd6
+ 00536c3c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ac86feaa306c28409a1215dec3ff503"></a>

### [`00536c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536c7c.md) → [`00536cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536cbc.md) FUN_00536cbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536cd8",
      "incomplete_value": true,
      "site": "00536cdc",
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
      "definition_site": "00536c98",
      "incomplete_value": true,
      "site": "00536c9c",
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
      "00536cd0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00536cdc",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00536cd0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00536cdc",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536c7c.md#insn-00536c90) · [`00536ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536c7c.md#insn-00536ca8) · [`00536cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536c7c.md#insn-00536cb0)
- 新版 `00536cd0`（命令位置の公開資料なし） · `00536ce8`（命令位置の公開資料なし） · `00536cf0`（命令位置の公開資料なし）

~~~diff
- 00536c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00536c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536cd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00536cd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00536c90 bytes 08e944f9
+ 00536cd0 bytes 08e946f9
- 00536ca8 ["INT_ADD", "register:40f0:8", ["const:536ca8:8", "const:4:8"]]
- 00536ca8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00536ce8 ["INT_ADD", "register:40f0:8", ["const:536ce8:8", "const:4:8"]]
+ 00536ce8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00536ca8 bytes 82831c94
+ 00536ce8 bytes 72841c94
- 00536cb0 ["INT_ADD", "register:40f0:8", ["const:536cb0:8", "const:4:8"]]
- 00536cb0 ["CALL", null, ["callee:00c582e0:8"]]
+ 00536cf0 ["INT_ADD", "register:40f0:8", ["const:536cf0:8", "const:4:8"]]
+ 00536cf0 ["CALL", null, ["callee:00c582e0:8"]]
- 00536cb0 bytes 8c841c94
+ 00536cf0 bytes 7c851c94
~~~


