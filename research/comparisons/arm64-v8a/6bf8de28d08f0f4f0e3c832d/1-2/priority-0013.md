# v16.0.1 → v16.0.2 · 最優先の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-8e565fd083be4e1450fb5ec5b6ce4f28"></a>

### [`00530d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530d20.md) → [`00530d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md) FUN_00530d60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00530db0",
      "incomplete_value": true,
      "site": "00530db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d98",
      "incomplete_value": true,
      "site": "00530d98",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530dd4",
      "incomplete_value": true,
      "site": "00530dd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00530d88",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530da8",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530db4",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530d88",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530da8",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530db4",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530d20.md#insn-00530d58) · [`00530d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530d20.md#insn-00530d94) · [`00530d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530d20.md#insn-00530d48)
- 新版 [`00530d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530d98) · [`00530dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530dd4) · [`00530d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530d88)

~~~diff
- 00530d58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d58 ["INT_ADD", "register:40f0:8", ["const:530d58:8", "const:4:8"]]
- 00530d58 ["CALLIND", null, ["register:0:8"]]
+ 00530d98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d98 ["INT_ADD", "register:40f0:8", ["const:530d98:8", "const:4:8"]]
+ 00530d98 ["CALLIND", null, ["register:0:8"]]
- 00530d58 bytes 20013fd6
+ 00530d98 bytes 20013fd6
- 00530d94 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d94 ["INT_ADD", "register:40f0:8", ["const:530d94:8", "const:4:8"]]
- 00530d94 ["CALLIND", null, ["register:0:8"]]
+ 00530dd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530dd4 ["INT_ADD", "register:40f0:8", ["const:530dd4:8", "const:4:8"]]
+ 00530dd4 ["CALLIND", null, ["register:0:8"]]
- 00530d94 bytes 20013fd6
+ 00530dd4 bytes 20013fd6
- 00530d48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00530d48 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530d88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00530d88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530d48 bytes a99e43f9
+ 00530d88 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602c7d90ce7d4542a0453dc6ad07540b"></a>

### [`00530eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530eac.md) → [`00530eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md) FUN_00530eec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00530f24",
      "incomplete_value": true,
      "site": "00530f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00530f14",
      "READ",
      [
        "storage",
        "002b72b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00530f14",
      "READ",
      [
        "storage",
        "002b72f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530eac.md#insn-00530ec8) · [`00530ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530eac.md#insn-00530ef0) · [`00530f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530eac.md#insn-00530f00)
- 新版 [`00530f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f08) · [`00530f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f30) · [`00530f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f40)

~~~diff
- 00530ec8 ["COPY", "tmp:0:8", ["const:2b7:8"]]
- 00530ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00530ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00530ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00530f08 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 00530f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00530f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00530f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00530ec8 bytes 29dd0a91
+ 00530f08 bytes 29dd0b91
- 00530ef0 ["INT_ADD", "register:40f0:8", ["const:530ef0:8", "const:4:8"]]
- 00530ef0 ["CALL", null, ["callee:00c58760:8"]]
+ 00530f30 ["INT_ADD", "register:40f0:8", ["const:530f30:8", "const:4:8"]]
+ 00530f30 ["CALL", null, ["callee:00c58760:8"]]
- 00530ef0 bytes e89d1c94
+ 00530f30 bytes 0c9e1c94
- 00530f00 ["INT_ADD", "register:40f0:8", ["const:530f00:8", "const:4:8"]]
- 00530f00 ["CALL", null, ["callee:00c57f80:8"]]
+ 00530f40 ["INT_ADD", "register:40f0:8", ["const:530f40:8", "const:4:8"]]
+ 00530f40 ["CALL", null, ["callee:00c57f80:8"]]
- 00530f00 bytes ec9b1c94
+ 00530f40 bytes 109c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aa10d0aeb2b4874928c7d9e14911a14"></a>

### [`00530fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fec.md) → [`0053102c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md) FUN_0053102c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00531064",
      "incomplete_value": true,
      "site": "00531064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:781:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00531054",
      "READ",
      [
        "storage",
        "002ae7dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531054",
      "READ",
      [
        "storage",
        "002ae781",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fec.md#insn-00531008) · [`00531030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fec.md#insn-00531030) · [`00531040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fec.md#insn-00531040)
- 新版 [`00531048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531048) · [`00531070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531070) · [`00531080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531080)

~~~diff
- 00531008 ["COPY", "tmp:0:8", ["const:7dd:8"]]
- 00531008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531048 ["COPY", "tmp:0:8", ["const:781:8"]]
+ 00531048 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531048 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531048 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531008 bytes 29751f91
+ 00531048 bytes 29051e91
- 00531030 ["INT_ADD", "register:40f0:8", ["const:531030:8", "const:4:8"]]
- 00531030 ["CALL", null, ["callee:00c58760:8"]]
+ 00531070 ["INT_ADD", "register:40f0:8", ["const:531070:8", "const:4:8"]]
+ 00531070 ["CALL", null, ["callee:00c58760:8"]]
- 00531030 bytes 989d1c94
+ 00531070 bytes bc9d1c94
- 00531040 ["INT_ADD", "register:40f0:8", ["const:531040:8", "const:4:8"]]
- 00531040 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531080 ["INT_ADD", "register:40f0:8", ["const:531080:8", "const:4:8"]]
+ 00531080 ["CALL", null, ["callee:00c57f80:8"]]
- 00531040 bytes 9c9b1c94
+ 00531080 bytes c09b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb36c9344265f3b23d5cd0ecf8b1380"></a>

### [`00531094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531094.md) → [`005310d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005310d4.md) FUN_005310d4

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
      "definition_site": "005310f0",
      "incomplete_value": true,
      "site": "005310f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b89:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005310e8",
      "incomplete_value": true,
      "site": "005310f4",
      "value": [
        "LOAD",
        "8",
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
      "005310e0",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "005310e8",
      "READ",
      [
        "storage",
        "002a9b61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005310e0",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "005310e8",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053109c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531094.md#insn-0053109c)
- 新版 [`005310dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005310d4.md#insn-005310dc)

~~~diff
- 0053109c ["COPY", "tmp:0:8", ["const:b5a:8"]]
- 0053109c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053109c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053109c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005310dc ["COPY", "tmp:0:8", ["const:b89:8"]]
+ 005310dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005310dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005310dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053109c bytes 4a692d91
+ 005310dc bytes 4a252e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999841cda39babf6ba55091318472c5b"></a>

### [`0053110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053110c.md) → [`0053114c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md) FUN_0053114c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00531184",
      "incomplete_value": true,
      "site": "00531184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00531174",
      "READ",
      [
        "storage",
        "002b4d0b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531174",
      "READ",
      [
        "storage",
        "002b4d3c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053110c.md#insn-00531128) · [`00531150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053110c.md#insn-00531150) · [`00531160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053110c.md#insn-00531160)
- 新版 [`00531168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-00531168) · [`00531190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-00531190) · [`005311a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-005311a0)

~~~diff
- 00531128 ["COPY", "tmp:0:8", ["const:d0b:8"]]
- 00531128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531168 ["COPY", "tmp:0:8", ["const:d3c:8"]]
+ 00531168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531128 bytes 292d3491
+ 00531168 bytes 29f13491
- 00531150 ["INT_ADD", "register:40f0:8", ["const:531150:8", "const:4:8"]]
- 00531150 ["CALL", null, ["callee:00c58760:8"]]
+ 00531190 ["INT_ADD", "register:40f0:8", ["const:531190:8", "const:4:8"]]
+ 00531190 ["CALL", null, ["callee:00c58760:8"]]
- 00531150 bytes 509d1c94
+ 00531190 bytes 749d1c94
- 00531160 ["INT_ADD", "register:40f0:8", ["const:531160:8", "const:4:8"]]
- 00531160 ["CALL", null, ["callee:00c57f80:8"]]
+ 005311a0 ["INT_ADD", "register:40f0:8", ["const:5311a0:8", "const:4:8"]]
+ 005311a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00531160 bytes 549b1c94
+ 005311a0 bytes 789b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976f96a4e833b5e7d79680813f625d4c"></a>

### [`00531204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531204.md) → [`00531244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md) FUN_00531244

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "00531278",
      "incomplete_value": true,
      "site": "00531284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00531268",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00531284",
      "DATA",
      [
        "storage",
        "00c67a28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531268",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00531284",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053121c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531204.md#insn-0053121c) · [`00531228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531204.md#insn-00531228) · [`00531254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531204.md#insn-00531254)
- 新版 [`0053125c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-0053125c) · [`00531268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-00531268) · [`00531294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-00531294)

~~~diff
- 0053121c ["INT_ADD", "register:40f0:8", ["const:53121c:8", "const:4:8"]]
- 0053121c ["CALL", null, ["callee:00c57f60:8"]]
+ 0053125c ["INT_ADD", "register:40f0:8", ["const:53125c:8", "const:4:8"]]
+ 0053125c ["CALL", null, ["callee:00c57f60:8"]]
- 0053121c bytes 1d9b1c94
+ 0053125c bytes 419b1c94
- 00531228 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 00531228 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00531268 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531228 bytes 08d940f9
+ 00531268 bytes 084141f9
- 00531254 ["INT_ADD", "register:40f0:8", ["const:531254:8", "const:4:8"]]
- 00531254 ["CALL", null, ["callee:00c57f60:8"]]
+ 00531294 ["INT_ADD", "register:40f0:8", ["const:531294:8", "const:4:8"]]
+ 00531294 ["CALL", null, ["callee:00c57f60:8"]]
- 00531254 bytes 0f9b1c94
+ 00531294 bytes 339b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-832bb959d4bfd13491e7906ef60caa2b"></a>

### [`00531314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531314.md) → [`00531354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md) FUN_00531354

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "0053138c",
      "incomplete_value": true,
      "site": "0053138c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "0053137c",
      "READ",
      [
        "storage",
        "002a4103",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053137c",
      "READ",
      [
        "storage",
        "002a40b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531314.md#insn-00531330) · [`00531358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531314.md#insn-00531358) · [`00531368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531314.md#insn-00531368)
- 新版 [`00531370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-00531370) · [`00531398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-00531398) · [`005313a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-005313a8)

~~~diff
- 00531330 ["COPY", "tmp:0:8", ["const:103:8"]]
- 00531330 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531330 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531330 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531370 ["COPY", "tmp:0:8", ["const:b6:8"]]
+ 00531370 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531370 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531370 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531330 bytes 290d0491
+ 00531370 bytes 29d90291
- 00531358 ["INT_ADD", "register:40f0:8", ["const:531358:8", "const:4:8"]]
- 00531358 ["CALL", null, ["callee:00c58760:8"]]
+ 00531398 ["INT_ADD", "register:40f0:8", ["const:531398:8", "const:4:8"]]
+ 00531398 ["CALL", null, ["callee:00c58760:8"]]
- 00531358 bytes ce9c1c94
+ 00531398 bytes f29c1c94
- 00531368 ["INT_ADD", "register:40f0:8", ["const:531368:8", "const:4:8"]]
- 00531368 ["CALL", null, ["callee:00c57f80:8"]]
+ 005313a8 ["INT_ADD", "register:40f0:8", ["const:5313a8:8", "const:4:8"]]
+ 005313a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00531368 bytes d29a1c94
+ 005313a8 bytes f69a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0ff2b7c4cb2d40b84035d4469c306ba"></a>

### [`0053140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053140c.md) → [`0053144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md) FUN_0053144c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "00531480",
      "incomplete_value": true,
      "site": "0053148c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00531470",
      "READ",
      [
        "storage",
        "00c9b190",
        null,
        "pointer"
      ]
    ],
    [
      "0053148c",
      "DATA",
      [
        "storage",
        "00c689c0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531470",
      "READ",
      [
        "storage",
        "00c9b260",
        null,
        "pointer"
      ]
    ],
    [
      "0053148c",
      "DATA",
      [
        "storage",
        "00c68a90",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053140c.md#insn-00531424) · [`00531430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053140c.md#insn-00531430) · [`0053145c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053140c.md#insn-0053145c)
- 新版 [`00531464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-00531464) · [`00531470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-00531470) · [`0053149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-0053149c)

~~~diff
- 00531424 ["INT_ADD", "register:40f0:8", ["const:531424:8", "const:4:8"]]
- 00531424 ["CALL", null, ["callee:00c57f60:8"]]
+ 00531464 ["INT_ADD", "register:40f0:8", ["const:531464:8", "const:4:8"]]
+ 00531464 ["CALL", null, ["callee:00c57f60:8"]]
- 00531424 bytes 9b9a1c94
+ 00531464 bytes bf9a1c94
- 00531430 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
- 00531430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 00531470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531430 bytes 08c940f9
+ 00531470 bytes 083141f9
- 0053145c ["INT_ADD", "register:40f0:8", ["const:53145c:8", "const:4:8"]]
- 0053145c ["CALL", null, ["callee:00c57f60:8"]]
+ 0053149c ["INT_ADD", "register:40f0:8", ["const:53149c:8", "const:4:8"]]
+ 0053149c ["CALL", null, ["callee:00c57f60:8"]]
- 0053145c bytes 8d9a1c94
+ 0053149c bytes b19a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c38c042c55101f68005e898ad2d2a75e"></a>

### [`00531554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531554.md) → [`00531594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md) FUN_00531594

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005315cc",
      "incomplete_value": true,
      "site": "005315cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005315bc",
      "READ",
      [
        "storage",
        "002bb320",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005315bc",
      "READ",
      [
        "storage",
        "002bb2cc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531554.md#insn-00531570) · [`00531598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531554.md#insn-00531598) · [`005315a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531554.md#insn-005315a8)
- 新版 [`005315b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315b0) · [`005315d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315d8) · [`005315e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315e8)

~~~diff
- 00531570 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00531570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005315b0 ["COPY", "tmp:0:8", ["const:2cc:8"]]
+ 005315b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005315b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005315b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531570 bytes 29810c91
+ 005315b0 bytes 29310b91
- 00531598 ["INT_ADD", "register:40f0:8", ["const:531598:8", "const:4:8"]]
- 00531598 ["CALL", null, ["callee:00c58760:8"]]
+ 005315d8 ["INT_ADD", "register:40f0:8", ["const:5315d8:8", "const:4:8"]]
+ 005315d8 ["CALL", null, ["callee:00c58760:8"]]
- 00531598 bytes 3e9c1c94
+ 005315d8 bytes 629c1c94
- 005315a8 ["INT_ADD", "register:40f0:8", ["const:5315a8:8", "const:4:8"]]
- 005315a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005315e8 ["INT_ADD", "register:40f0:8", ["const:5315e8:8", "const:4:8"]]
+ 005315e8 ["CALL", null, ["callee:00c57f80:8"]]
- 005315a8 bytes 429a1c94
+ 005315e8 bytes 669a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79390c74b3432a1c1892eae97aeab7b9"></a>

### [`0053164c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053164c.md) → [`0053168c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md) FUN_0053168c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "005316b4",
      "incomplete_value": true,
      "site": "005316b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005316ac",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "005316b4",
      "DATA",
      [
        "storage",
        "00c68a50",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005316ac",
      "READ",
      [
        "storage",
        "00c9b268",
        null,
        "pointer"
      ]
    ],
    [
      "005316b4",
      "DATA",
      [
        "storage",
        "00c68b20",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053164c.md#insn-00531660) · [`0053166c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053164c.md#insn-0053166c) · [`0053167c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053164c.md#insn-0053167c)
- 新版 [`005316a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316a0) · [`005316ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316ac) · [`005316bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316bc)

~~~diff
- 00531660 ["INT_ADD", "register:40f0:8", ["const:531660:8", "const:4:8"]]
- 00531660 ["CALL", null, ["callee:00c57f60:8"]]
+ 005316a0 ["INT_ADD", "register:40f0:8", ["const:5316a0:8", "const:4:8"]]
+ 005316a0 ["CALL", null, ["callee:00c57f60:8"]]
- 00531660 bytes 0c9a1c94
+ 005316a0 bytes 309a1c94
- 0053166c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 0053166c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005316ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
+ 005316ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053166c bytes 08cd40f9
+ 005316ac bytes 083541f9
- 0053167c ["INT_ADD", "register:40f0:8", ["const:53167c:8", "const:4:8"]]
- 0053167c ["CALL", null, ["callee:0053c980:8"]]
+ 005316bc ["INT_ADD", "register:40f0:8", ["const:5316bc:8", "const:4:8"]]
+ 005316bc ["CALL", null, ["callee:0053c980:8"]]
- 0053167c bytes b12c0094
+ 005316bc bytes b12c0094
~~~


<a id="compare-73d64d011542a201369f61ceb12468cb"></a>

### [`0053181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053181c.md) → [`0053185c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md) FUN_0053185c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00531884",
      "incomplete_value": true,
      "site": "00531884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053187c",
      "READ",
      [
        "storage",
        "00c9b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00531884",
      "DATA",
      [
        "storage",
        "00c68ac8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0053187c",
      "READ",
      [
        "storage",
        "00c9b288",
        null,
        "pointer"
      ]
    ],
    [
      "00531884",
      "DATA",
      [
        "storage",
        "00c68b98",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053181c.md#insn-00531830) · [`0053183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053181c.md#insn-0053183c) · [`0053184c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053181c.md#insn-0053184c)
- 新版 [`00531870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-00531870) · [`0053187c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-0053187c) · [`0053188c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-0053188c)

~~~diff
- 00531830 ["INT_ADD", "register:40f0:8", ["const:531830:8", "const:4:8"]]
- 00531830 ["CALL", null, ["callee:00c57f60:8"]]
+ 00531870 ["INT_ADD", "register:40f0:8", ["const:531870:8", "const:4:8"]]
+ 00531870 ["CALL", null, ["callee:00c57f60:8"]]
- 00531830 bytes 98991c94
+ 00531870 bytes bc991c94
- 0053183c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b8:8"]]
- 0053183c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053187c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
+ 0053187c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053183c bytes 08dd40f9
+ 0053187c bytes 084541f9
- 0053184c ["INT_ADD", "register:40f0:8", ["const:53184c:8", "const:4:8"]]
- 0053184c ["CALL", null, ["callee:0053c980:8"]]
+ 0053188c ["INT_ADD", "register:40f0:8", ["const:53188c:8", "const:4:8"]]
+ 0053188c ["CALL", null, ["callee:0053c980:8"]]
- 0053184c bytes 3d2c0094
+ 0053188c bytes 3d2c0094
~~~


<a id="compare-3b5a6bfa80db10ace28ab98255f5f0ea"></a>

### [`005318f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318f4.md) → [`00531934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md) FUN_00531934

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "0053196c",
      "incomplete_value": true,
      "site": "0053196c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "0053195c",
      "READ",
      [
        "storage",
        "002ab417",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053195c",
      "READ",
      [
        "storage",
        "002ab3bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318f4.md#insn-00531910) · [`00531938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318f4.md#insn-00531938) · [`00531948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318f4.md#insn-00531948)
- 新版 [`00531950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531950) · [`00531978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531978) · [`00531988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531988)

~~~diff
- 00531910 ["COPY", "tmp:0:8", ["const:417:8"]]
- 00531910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531950 ["COPY", "tmp:0:8", ["const:3bb:8"]]
+ 00531950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531910 bytes 295d1091
+ 00531950 bytes 29ed0e91
- 00531938 ["INT_ADD", "register:40f0:8", ["const:531938:8", "const:4:8"]]
- 00531938 ["CALL", null, ["callee:00c58760:8"]]
+ 00531978 ["INT_ADD", "register:40f0:8", ["const:531978:8", "const:4:8"]]
+ 00531978 ["CALL", null, ["callee:00c58760:8"]]
- 00531938 bytes 569b1c94
+ 00531978 bytes 7a9b1c94
- 00531948 ["INT_ADD", "register:40f0:8", ["const:531948:8", "const:4:8"]]
- 00531948 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531988 ["INT_ADD", "register:40f0:8", ["const:531988:8", "const:4:8"]]
+ 00531988 ["CALL", null, ["callee:00c57f80:8"]]
- 00531948 bytes 5a991c94
+ 00531988 bytes 7e991c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e7c0f1aa775f5ee1e54f41f393c15b4"></a>

### [`005319ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md) → [`00531a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md) FUN_00531a2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00531a78",
      "incomplete_value": true,
      "site": "00531a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00531a6c",
      "READ",
      [
        "storage",
        "00c9b180",
        null,
        "pointer"
      ]
    ],
    [
      "00531a84",
      "DATA",
      [
        "storage",
        "00c678f0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531a6c",
      "READ",
      [
        "storage",
        "00c9b250",
        null,
        "pointer"
      ]
    ],
    [
      "00531a84",
      "DATA",
      [
        "storage",
        "00c679c0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md#insn-00531a84) · [`00531a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md#insn-00531a1c) · [`00531a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005319ec.md#insn-00531a2c)
- 新版 [`00531ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531ac4) · [`00531a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531a5c) · [`00531a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531a6c)

~~~diff
- 00531a84 ["INT_ADD", "register:40f0:8", ["const:531a84:8", "const:4:8"]]
- 00531a84 ["CALL", null, ["callee:0053eeb0:8"]]
+ 00531ac4 ["INT_ADD", "register:40f0:8", ["const:531ac4:8", "const:4:8"]]
+ 00531ac4 ["CALL", null, ["callee:0053eeb0:8"]]
- 00531a84 bytes fb340094
+ 00531ac4 bytes fb340094
- 00531a1c ["INT_ADD", "register:40f0:8", ["const:531a1c:8", "const:4:8"]]
- 00531a1c ["CALL", null, ["callee:00c57f60:8"]]
+ 00531a5c ["INT_ADD", "register:40f0:8", ["const:531a5c:8", "const:4:8"]]
+ 00531a5c ["CALL", null, ["callee:00c57f60:8"]]
- 00531a1c bytes 1d991c94
+ 00531a5c bytes 41991c94
- 00531a2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:180:8"]]
- 00531a2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:250:8"]]
+ 00531a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531a2c bytes 08c140f9
+ 00531a6c bytes 082941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e02d7fa9563b8c5dec8bed12c06f1ac"></a>

### [`00531c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531c04.md) → [`00531c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md) FUN_00531c44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00531c7c",
      "incomplete_value": true,
      "site": "00531c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00531c6c",
      "READ",
      [
        "storage",
        "0029ef6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531c6c",
      "READ",
      [
        "storage",
        "0029ef20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531c04.md#insn-00531c20) · [`00531c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531c04.md#insn-00531c48) · [`00531c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531c04.md#insn-00531c58)
- 新版 [`00531c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c60) · [`00531c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c88) · [`00531c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c98)

~~~diff
- 00531c20 ["COPY", "tmp:0:8", ["const:f6d:8"]]
- 00531c20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531c20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531c20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531c60 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00531c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531c20 bytes 29b53d91
+ 00531c60 bytes 29813c91
- 00531c48 ["INT_ADD", "register:40f0:8", ["const:531c48:8", "const:4:8"]]
- 00531c48 ["CALL", null, ["callee:00c58760:8"]]
+ 00531c88 ["INT_ADD", "register:40f0:8", ["const:531c88:8", "const:4:8"]]
+ 00531c88 ["CALL", null, ["callee:00c58760:8"]]
- 00531c48 bytes 929a1c94
+ 00531c88 bytes b69a1c94
- 00531c58 ["INT_ADD", "register:40f0:8", ["const:531c58:8", "const:4:8"]]
- 00531c58 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531c98 ["INT_ADD", "register:40f0:8", ["const:531c98:8", "const:4:8"]]
+ 00531c98 ["CALL", null, ["callee:00c57f80:8"]]
- 00531c58 bytes 96981c94
+ 00531c98 bytes ba981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86aa009957e071026d213e532117f849"></a>

### [`00531cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cac.md) → [`00531cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531cec.md) FUN_00531cec

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
      "definition_site": "00531cf8",
      "incomplete_value": true,
      "site": "00531d08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:433:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531d0c",
      "incomplete_value": true,
      "site": "00531d0c",
      "value": [
        "LOAD",
        "8",
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
      "00531cf8",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ],
    [
      "00531d00",
      "READ",
      [
        "storage",
        "002a549d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531cf8",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ],
    [
      "00531d00",
      "READ",
      [
        "storage",
        "002a5441",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cac.md#insn-00531cb4)
- 新版 [`00531cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531cec.md#insn-00531cf4)

~~~diff
- 00531cb4 ["COPY", "tmp:0:8", ["const:48f:8"]]
- 00531cb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00531cb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00531cb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00531cf4 ["COPY", "tmp:0:8", ["const:433:8"]]
+ 00531cf4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00531cf4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00531cf4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00531cb4 bytes 4a3d1291
+ 00531cf4 bytes 4acd1091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e72881c367333111d08a6524eb9f0ab"></a>

### [`00531cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md) → [`00531d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md) FUN_00531d14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f910.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f950.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00531d3c",
      "incomplete_value": true,
      "site": "00531d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00531d34",
      "READ",
      [
        "storage",
        "00c9b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00531d3c",
      "DATA",
      [
        "storage",
        "00c68b58",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531d34",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00531d3c",
      "DATA",
      [
        "storage",
        "00c68c28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md#insn-00531ce8) · [`00531cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md#insn-00531cf4) · [`00531d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531cd4.md#insn-00531d04)
- 新版 [`00531d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d28) · [`00531d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d34) · [`00531d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d44)

~~~diff
- 00531ce8 ["INT_ADD", "register:40f0:8", ["const:531ce8:8", "const:4:8"]]
- 00531ce8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00531d28 ["INT_ADD", "register:40f0:8", ["const:531d28:8", "const:4:8"]]
+ 00531d28 ["CALL", null, ["callee:00c57f60:8"]]
- 00531ce8 bytes 6a981c94
+ 00531d28 bytes 8e981c94
- 00531cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 00531cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 00531d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531cf4 bytes 08e140f9
+ 00531d34 bytes 084941f9
- 00531d04 ["INT_ADD", "register:40f0:8", ["const:531d04:8", "const:4:8"]]
- 00531d04 ["CALL", null, ["callee:0053f950:8"]]
+ 00531d44 ["INT_ADD", "register:40f0:8", ["const:531d44:8", "const:4:8"]]
+ 00531d44 ["CALL", null, ["callee:0053f950:8"]]
- 00531d04 bytes 03370094
+ 00531d44 bytes 03370094
~~~


<a id="compare-d1797ff78a66fe91bed4e190ad564141"></a>

### [`00531d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d64.md) → [`00531da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md) FUN_00531da4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00531ddc",
      "incomplete_value": true,
      "site": "00531ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00531dcc",
      "READ",
      [
        "storage",
        "002ad741",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531dcc",
      "READ",
      [
        "storage",
        "002ad6e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d64.md#insn-00531d80) · [`00531da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d64.md#insn-00531da8) · [`00531db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d64.md#insn-00531db8)
- 新版 [`00531dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531dc0) · [`00531de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531de8) · [`00531df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531df8)

~~~diff
- 00531d80 ["COPY", "tmp:0:8", ["const:741:8"]]
- 00531d80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531d80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531d80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531dc0 ["COPY", "tmp:0:8", ["const:6e5:8"]]
+ 00531dc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531dc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531dc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531d80 bytes 29051d91
+ 00531dc0 bytes 29951b91
- 00531da8 ["INT_ADD", "register:40f0:8", ["const:531da8:8", "const:4:8"]]
- 00531da8 ["CALL", null, ["callee:00c58760:8"]]
+ 00531de8 ["INT_ADD", "register:40f0:8", ["const:531de8:8", "const:4:8"]]
+ 00531de8 ["CALL", null, ["callee:00c58760:8"]]
- 00531da8 bytes 3a9a1c94
+ 00531de8 bytes 5e9a1c94
- 00531db8 ["INT_ADD", "register:40f0:8", ["const:531db8:8", "const:4:8"]]
- 00531db8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531df8 ["INT_ADD", "register:40f0:8", ["const:531df8:8", "const:4:8"]]
+ 00531df8 ["CALL", null, ["callee:00c57f80:8"]]
- 00531db8 bytes 3e981c94
+ 00531df8 bytes 62981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2a625cc7d4038d82ebffaad6011751d"></a>

### [`00531e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md) → [`00531e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md) FUN_00531e9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00531ee8",
      "incomplete_value": true,
      "site": "00531ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00531edc",
      "READ",
      [
        "storage",
        "00c9b1d0",
        null,
        "pointer"
      ]
    ],
    [
      "00531ef4",
      "DATA",
      [
        "storage",
        "00c68bd0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531edc",
      "READ",
      [
        "storage",
        "00c9b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00531ef4",
      "DATA",
      [
        "storage",
        "00c68ca0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md#insn-00531ef4) · [`00531e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md#insn-00531e8c) · [`00531e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531e5c.md#insn-00531e9c)
- 新版 [`00531f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531f34) · [`00531ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531ecc) · [`00531edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531edc)

~~~diff
- 00531ef4 ["INT_ADD", "register:40f0:8", ["const:531ef4:8", "const:4:8"]]
- 00531ef4 ["CALL", null, ["callee:0053eeb0:8"]]
+ 00531f34 ["INT_ADD", "register:40f0:8", ["const:531f34:8", "const:4:8"]]
+ 00531f34 ["CALL", null, ["callee:0053eeb0:8"]]
- 00531ef4 bytes df330094
+ 00531f34 bytes df330094
- 00531e8c ["INT_ADD", "register:40f0:8", ["const:531e8c:8", "const:4:8"]]
- 00531e8c ["CALL", null, ["callee:00c57f60:8"]]
+ 00531ecc ["INT_ADD", "register:40f0:8", ["const:531ecc:8", "const:4:8"]]
+ 00531ecc ["CALL", null, ["callee:00c57f60:8"]]
- 00531e8c bytes 01981c94
+ 00531ecc bytes 25981c94
- 00531e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1d0:8"]]
- 00531e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531edc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 00531edc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531e9c bytes 08e940f9
+ 00531edc bytes 085141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4693451307534007c03648610e530a"></a>

### [`00532074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532074.md) → [`005320b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md) FUN_005320b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005320dc",
      "incomplete_value": true,
      "site": "005320ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005320dc",
      "READ",
      [
        "storage",
        "002b0a97",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005320dc",
      "READ",
      [
        "storage",
        "002b0a3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532074.md#insn-00532090) · [`005320b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532074.md#insn-005320b8) · [`005320c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532074.md#insn-005320c8)
- 新版 [`005320d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-005320d0) · [`005320f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-005320f8) · [`00532108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-00532108)

~~~diff
- 00532090 ["COPY", "tmp:0:8", ["const:a97:8"]]
- 00532090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005320d0 ["COPY", "tmp:0:8", ["const:a3b:8"]]
+ 005320d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005320d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005320d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532090 bytes 295d2a91
+ 005320d0 bytes 29ed2891
- 005320b8 ["INT_ADD", "register:40f0:8", ["const:5320b8:8", "const:4:8"]]
- 005320b8 ["CALL", null, ["callee:00c58760:8"]]
+ 005320f8 ["INT_ADD", "register:40f0:8", ["const:5320f8:8", "const:4:8"]]
+ 005320f8 ["CALL", null, ["callee:00c58760:8"]]
- 005320b8 bytes 76991c94
+ 005320f8 bytes 9a991c94
- 005320c8 ["INT_ADD", "register:40f0:8", ["const:5320c8:8", "const:4:8"]]
- 005320c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532108 ["INT_ADD", "register:40f0:8", ["const:532108:8", "const:4:8"]]
+ 00532108 ["CALL", null, ["callee:00c57f80:8"]]
- 005320c8 bytes 7a971c94
+ 00532108 bytes 9e971c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d616aede702527654f42ec7ced573a4"></a>

### [`0053216c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md) → [`005321ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md) FUN_005321ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "005321e4",
      "incomplete_value": true,
      "site": "005321e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005321d4",
      "READ",
      [
        "storage",
        "00c9b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "005321e4",
      "DATA",
      [
        "storage",
        "00c68c48",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005321d4",
      "READ",
      [
        "storage",
        "00c9b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "005321e4",
      "DATA",
      [
        "storage",
        "00c68d18",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md#insn-00532184) · [`00532194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md#insn-00532194) · [`0053219c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053216c.md#insn-0053219c)
- 新版 [`005321c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md#insn-005321c4) · [`005321d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md#insn-005321d4)

~~~diff
- 00532184 ["INT_ADD", "register:40f0:8", ["const:532184:8", "const:4:8"]]
- 00532184 ["CALL", null, ["callee:00c57f60:8"]]
+ 005321c4 ["INT_ADD", "register:40f0:8", ["const:5321c4:8", "const:4:8"]]
+ 005321c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00532184 bytes 43971c94
+ 005321c4 bytes 67971c94
- 00532194 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
- 00532194 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005321d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2a8:8"]]
+ 005321d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00532194 bytes 29ed40f9
+ 005321d4 bytes 295541f9
- 0053219c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0053219c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d576abce44faff9c80a887e7488c6c72"></a>

### [`00532364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532364.md) → [`005323a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md) FUN_005323a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005323dc",
      "incomplete_value": true,
      "site": "005323dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005323cc",
      "READ",
      [
        "storage",
        "002bec9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005323cc",
      "READ",
      [
        "storage",
        "002bec4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532364.md#insn-00532380) · [`005323a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532364.md#insn-005323a8) · [`005323b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532364.md#insn-005323b8)
- 新版 [`005323c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323c0) · [`005323e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323e8) · [`005323f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323f8)

~~~diff
- 00532380 ["COPY", "tmp:0:8", ["const:c9e:8"]]
- 00532380 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532380 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532380 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005323c0 ["COPY", "tmp:0:8", ["const:c4a:8"]]
+ 005323c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005323c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005323c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532380 bytes 29793291
+ 005323c0 bytes 29293191
- 005323a8 ["INT_ADD", "register:40f0:8", ["const:5323a8:8", "const:4:8"]]
- 005323a8 ["CALL", null, ["callee:00c58760:8"]]
+ 005323e8 ["INT_ADD", "register:40f0:8", ["const:5323e8:8", "const:4:8"]]
+ 005323e8 ["CALL", null, ["callee:00c58760:8"]]
- 005323a8 bytes ba981c94
+ 005323e8 bytes de981c94
- 005323b8 ["INT_ADD", "register:40f0:8", ["const:5323b8:8", "const:4:8"]]
- 005323b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005323f8 ["INT_ADD", "register:40f0:8", ["const:5323f8:8", "const:4:8"]]
+ 005323f8 ["CALL", null, ["callee:00c57f80:8"]]
- 005323b8 bytes be961c94
+ 005323f8 bytes e2961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f26b49dd2d0056a2421cb9871ed3568"></a>

### [`0053240c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053240c.md) → [`0053244c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/0053244c.md) FUN_0053244c

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
      "definition_site": "00532458",
      "incomplete_value": true,
      "site": "00532464",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00532458",
      "READ",
      [
        "storage",
        "002ab3fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532458",
      "READ",
      [
        "storage",
        "002ab3a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053240c.md#insn-00532410)
- 新版 [`00532450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/0053244c.md#insn-00532450)

~~~diff
- 00532410 ["COPY", "tmp:0:8", ["const:3fc:8"]]
- 00532410 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00532410 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00532410 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532450 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00532450 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532450 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532450 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00532410 bytes 4af10f91
+ 00532450 bytes 4a810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5cf507f8c7688f951653fde8d6bf307"></a>

### [`00532438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532438.md) → [`00532478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532478.md) FUN_00532478

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005324b0",
      "incomplete_value": true,
      "site": "005324b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005324a0",
      "READ",
      [
        "storage",
        "002a6574",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005324a0",
      "READ",
      [
        "storage",
        "002a6518",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532438.md#insn-00532454) · [`0053247c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532438.md#insn-0053247c) · [`0053248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532438.md#insn-0053248c)
- 新版 [`00532494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532478.md#insn-00532494) · [`005324bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532478.md#insn-005324bc) · [`005324cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532478.md#insn-005324cc)

~~~diff
- 00532454 ["COPY", "tmp:0:8", ["const:574:8"]]
- 00532454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532494 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00532494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532454 bytes 29d11591
+ 00532494 bytes 29611491
- 0053247c ["INT_ADD", "register:40f0:8", ["const:53247c:8", "const:4:8"]]
- 0053247c ["CALL", null, ["callee:00c58760:8"]]
+ 005324bc ["INT_ADD", "register:40f0:8", ["const:5324bc:8", "const:4:8"]]
+ 005324bc ["CALL", null, ["callee:00c58760:8"]]
- 0053247c bytes 85981c94
+ 005324bc bytes a9981c94
- 0053248c ["INT_ADD", "register:40f0:8", ["const:53248c:8", "const:4:8"]]
- 0053248c ["CALL", null, ["callee:00c57f80:8"]]
+ 005324cc ["INT_ADD", "register:40f0:8", ["const:5324cc:8", "const:4:8"]]
+ 005324cc ["CALL", null, ["callee:00c57f80:8"]]
- 0053248c bytes 89961c94
+ 005324cc bytes ad961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e1afb849503b48bd48a7e60843f24b"></a>

### [`005324e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005324e0.md) → [`00532520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532520.md) FUN_00532520

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
      "definition_site": "0053252c",
      "incomplete_value": true,
      "site": "0053253c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "0053252c",
      "READ",
      [
        "storage",
        "002b8f4d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053252c",
      "READ",
      [
        "storage",
        "002b8ef9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005324e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005324e0.md#insn-005324e4)
- 新版 [`00532524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532520.md#insn-00532524)

~~~diff
- 005324e4 ["COPY", "tmp:0:8", ["const:f4d:8"]]
- 005324e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005324e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005324e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532524 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00532524 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532524 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532524 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005324e4 bytes 4a353d91
+ 00532524 bytes 4ae53b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad1781c1ebf2a0211f774c1a7d64d1e"></a>

### [`00532558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532558.md) → [`00532598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md) FUN_00532598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005325d0",
      "incomplete_value": true,
      "site": "005325d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:72d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005325c0",
      "READ",
      [
        "storage",
        "002a7789",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005325c0",
      "READ",
      [
        "storage",
        "002a772d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532558.md#insn-00532574) · [`0053259c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532558.md#insn-0053259c) · [`005325ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532558.md#insn-005325ac)
- 新版 [`005325b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325b4) · [`005325dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325dc) · [`005325ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325ec)

~~~diff
- 00532574 ["COPY", "tmp:0:8", ["const:789:8"]]
- 00532574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005325b4 ["COPY", "tmp:0:8", ["const:72d:8"]]
+ 005325b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005325b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005325b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532574 bytes 29251e91
+ 005325b4 bytes 29b51c91
- 0053259c ["INT_ADD", "register:40f0:8", ["const:53259c:8", "const:4:8"]]
- 0053259c ["CALL", null, ["callee:00c58760:8"]]
+ 005325dc ["INT_ADD", "register:40f0:8", ["const:5325dc:8", "const:4:8"]]
+ 005325dc ["CALL", null, ["callee:00c58760:8"]]
- 0053259c bytes 3d981c94
+ 005325dc bytes 61981c94
- 005325ac ["INT_ADD", "register:40f0:8", ["const:5325ac:8", "const:4:8"]]
- 005325ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005325ec ["INT_ADD", "register:40f0:8", ["const:5325ec:8", "const:4:8"]]
+ 005325ec ["CALL", null, ["callee:00c57f80:8"]]
- 005325ac bytes 41961c94
+ 005325ec bytes 65961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-125147b2e31627003745da950b54816d"></a>

### [`00532650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532650.md) → [`00532690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md) FUN_00532690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fad8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fb18.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "005326bc",
      "incomplete_value": true,
      "site": "005326c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005326b0",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "005326c0",
      "DATA",
      [
        "storage",
        "00c68db0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005326b0",
      "READ",
      [
        "storage",
        "00c9b298",
        null,
        "pointer"
      ]
    ],
    [
      "005326c0",
      "DATA",
      [
        "storage",
        "00c68e80",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532650.md#insn-00532664) · [`00532670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532650.md#insn-00532670) · [`00532690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532650.md#insn-00532690)
- 新版 [`005326a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326a4) · [`005326b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326b0) · [`005326d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326d0)

~~~diff
- 00532664 ["INT_ADD", "register:40f0:8", ["const:532664:8", "const:4:8"]]
- 00532664 ["CALL", null, ["callee:00c57f60:8"]]
+ 005326a4 ["INT_ADD", "register:40f0:8", ["const:5326a4:8", "const:4:8"]]
+ 005326a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00532664 bytes 0b961c94
+ 005326a4 bytes 2f961c94
- 00532670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
- 00532670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005326b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
+ 005326b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00532670 bytes 08e540f9
+ 005326b0 bytes 084d41f9
- 00532690 ["INT_ADD", "register:40f0:8", ["const:532690:8", "const:4:8"]]
- 00532690 ["CALL", null, ["callee:0053fb18:8"]]
+ 005326d0 ["INT_ADD", "register:40f0:8", ["const:5326d0:8", "const:4:8"]]
+ 005326d0 ["CALL", null, ["callee:0053fb18:8"]]
- 00532690 bytes 12350094
+ 005326d0 bytes 12350094
~~~


<a id="compare-38c489649d5d3b77b18d68ef2a1b62ca"></a>

### [`005328c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005328c8.md) → [`00532908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md) FUN_00532908

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00532940",
      "incomplete_value": true,
      "site": "00532940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:489:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00532930",
      "READ",
      [
        "storage",
        "002bc4dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532930",
      "READ",
      [
        "storage",
        "002bc489",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005328e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005328c8.md#insn-005328e4) · [`0053290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005328c8.md#insn-0053290c) · [`0053291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005328c8.md#insn-0053291c)
- 新版 [`00532924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-00532924) · [`0053294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-0053294c) · [`0053295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-0053295c)

~~~diff
- 005328e4 ["COPY", "tmp:0:8", ["const:4dd:8"]]
- 005328e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005328e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005328e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532924 ["COPY", "tmp:0:8", ["const:489:8"]]
+ 00532924 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532924 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532924 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005328e4 bytes 29751391
+ 00532924 bytes 29251291
- 0053290c ["INT_ADD", "register:40f0:8", ["const:53290c:8", "const:4:8"]]
- 0053290c ["CALL", null, ["callee:00c58760:8"]]
+ 0053294c ["INT_ADD", "register:40f0:8", ["const:53294c:8", "const:4:8"]]
+ 0053294c ["CALL", null, ["callee:00c58760:8"]]
- 0053290c bytes 61971c94
+ 0053294c bytes 85971c94
- 0053291c ["INT_ADD", "register:40f0:8", ["const:53291c:8", "const:4:8"]]
- 0053291c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053295c ["INT_ADD", "register:40f0:8", ["const:53295c:8", "const:4:8"]]
+ 0053295c ["CALL", null, ["callee:00c57f80:8"]]
- 0053291c bytes 65951c94
+ 0053295c bytes 89951c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e7b8d53a160d4d3fb7d29fe5b62015f"></a>

### [`005329c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005329c0.md) → [`00532a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md) FUN_00532a00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00532a30",
      "incomplete_value": false,
      "site": "00532a30",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532a30",
      "incomplete_value": true,
      "site": "00532a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00532a28",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00532a30",
      "DATA",
      [
        "storage",
        "00c68e70",
        null,
        "undefined *"
      ]
    ],
    [
      "00532a30",
      "DATA",
      [
        "storage",
        "00c68e28",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00532a28",
      "READ",
      [
        "storage",
        "00c9b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "00532a30",
      "DATA",
      [
        "storage",
        "00c68f40",
        null,
        "undefined *"
      ]
    ],
    [
      "00532a30",
      "DATA",
      [
        "storage",
        "00c68ef8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005329d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005329c0.md#insn-005329d4) · [`005329e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005329c0.md#insn-005329e4) · [`005329e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005329c0.md#insn-005329e8)
- 新版 [`00532a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a14) · [`00532a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a24) · [`00532a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a28)

~~~diff
- 005329d4 ["INT_ADD", "register:40f0:8", ["const:5329d4:8", "const:4:8"]]
- 005329d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00532a14 ["INT_ADD", "register:40f0:8", ["const:532a14:8", "const:4:8"]]
+ 00532a14 ["CALL", null, ["callee:00c57f60:8"]]
- 005329d4 bytes 2f951c94
+ 00532a14 bytes 53951c94
- 005329e4 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 005329e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005329e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005329e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532a24 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00532a24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532a24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532a24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005329e4 bytes 29c13991
+ 00532a24 bytes 29013d91
- 005329e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
- 005329e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532a28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
+ 00532a28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005329e8 bytes 08f540f9
+ 00532a28 bytes 085d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e11df8246eb468a4cf4392e0059bc9"></a>

### [`00532b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532b34.md) → [`00532b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md) FUN_00532b74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "00532bbc",
      "incomplete_value": true,
      "site": "00532bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532bbc",
      "incomplete_value": true,
      "site": "00532bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00532ba0",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00532ba4",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00532bbc",
      "DATA",
      [
        "storage",
        "00c68ee8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532ba0",
      "READ",
      [
        "storage",
        "00c9b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00532ba4",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00532bbc",
      "DATA",
      [
        "storage",
        "00c68fb8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532b34.md#insn-00532b50) · [`00532b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532b34.md#insn-00532b60) · [`00532b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532b34.md#insn-00532b64)
- 新版 [`00532b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532b90) · [`00532ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532ba0) · [`00532ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532ba4)

~~~diff
- 00532b50 ["INT_ADD", "register:40f0:8", ["const:532b50:8", "const:4:8"]]
- 00532b50 ["CALL", null, ["callee:00c57f60:8"]]
+ 00532b90 ["INT_ADD", "register:40f0:8", ["const:532b90:8", "const:4:8"]]
+ 00532b90 ["CALL", null, ["callee:00c57f60:8"]]
- 00532b50 bytes d0941c94
+ 00532b90 bytes f4941c94
- 00532b60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 00532b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532ba0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 00532ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00532b60 bytes 08f140f9
+ 00532ba0 bytes 085941f9
- 00532b64 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 00532b64 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532ba4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 00532ba4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00532b64 bytes 29a146f9
+ 00532ba4 bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7dbead366d41e1d4f00de243507bb8"></a>

### [`00532d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md) → [`00532dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md) FUN_00532dc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053fd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fd18.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fd58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)

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
      "definition_site": "00532dec",
      "incomplete_value": false,
      "site": "00532dec",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00532dec",
      "DATA",
      [
        "storage",
        "00c66db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00532dec",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md#insn-00532d98) · [`00532da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md#insn-00532da4) · [`00532da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d80.md#insn-00532da8)
- 新版 [`00532dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md#insn-00532dd8) · [`00532de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md#insn-00532de4)

~~~diff
- 00532d98 ["INT_ADD", "register:40f0:8", ["const:532d98:8", "const:4:8"]]
- 00532d98 ["CALL", null, ["callee:00c57f60:8"]]
+ 00532dd8 ["INT_ADD", "register:40f0:8", ["const:532dd8:8", "const:4:8"]]
+ 00532dd8 ["CALL", null, ["callee:00c57f60:8"]]
- 00532d98 bytes 3e941c94
+ 00532dd8 bytes 62941c94
- 00532da4 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00532da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532de4 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00532de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532da4 bytes 08e13691
+ 00532de4 bytes 08213a91
- 00532da8 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00532da8 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f6736cb171f78d21142a83d8c810676"></a>

### [`00532e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md) → [`00532ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md) FUN_00532ebc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00532f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md) · 呼出先 4件 [`004de6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00532f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532f8c.md) · 呼出先 4件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00532f24",
      "incomplete_value": true,
      "site": "00532f24",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532f60",
      "incomplete_value": true,
      "site": "00532f60",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00532f14",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00532f50",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532f14",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00532f50",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md#insn-00532ee4) · [`00532f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md#insn-00532f20) · [`00532ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md#insn-00532ed4)
- 新版 [`00532f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532f24) · [`00532f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532f60) · [`00532f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532f14)

~~~diff
- 00532ee4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532ee4 ["INT_ADD", "register:40f0:8", ["const:532ee4:8", "const:4:8"]]
- 00532ee4 ["CALLIND", null, ["register:0:8"]]
+ 00532f24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532f24 ["INT_ADD", "register:40f0:8", ["const:532f24:8", "const:4:8"]]
+ 00532f24 ["CALLIND", null, ["register:0:8"]]
- 00532ee4 bytes 20013fd6
+ 00532f24 bytes 20013fd6
- 00532f20 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532f20 ["INT_ADD", "register:40f0:8", ["const:532f20:8", "const:4:8"]]
- 00532f20 ["CALLIND", null, ["register:0:8"]]
+ 00532f60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532f60 ["INT_ADD", "register:40f0:8", ["const:532f60:8", "const:4:8"]]
+ 00532f60 ["CALLIND", null, ["register:0:8"]]
- 00532f20 bytes 20013fd6
+ 00532f60 bytes 20013fd6
- 00532ed4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00532ed4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532f14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00532f14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00532ed4 bytes a99e43f9
+ 00532f14 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ec248e46915c297e510932beb1a2c6b"></a>

### [`00532fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md) → [`00532ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md) FUN_00532ff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md) · 呼出先 4件 [`004de6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de6e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0053316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/0053316c.md) · 呼出先 4件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533060",
      "incomplete_value": true,
      "site": "00533060",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005330a4",
      "incomplete_value": true,
      "site": "005330a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005330d0",
      "incomplete_value": true,
      "site": "005330d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533050",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533094",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005330c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533050",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533094",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005330c0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md#insn-00533020) · [`00533064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md#insn-00533064) · [`00533090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md#insn-00533090)
- 新版 [`00533060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-00533060) · [`005330a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-005330a4) · [`005330d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-005330d0)

~~~diff
- 00533020 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533020 ["INT_ADD", "register:40f0:8", ["const:533020:8", "const:4:8"]]
- 00533020 ["CALLIND", null, ["register:0:8"]]
+ 00533060 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533060 ["INT_ADD", "register:40f0:8", ["const:533060:8", "const:4:8"]]
+ 00533060 ["CALLIND", null, ["register:0:8"]]
- 00533020 bytes 20013fd6
+ 00533060 bytes 20013fd6
- 00533064 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533064 ["INT_ADD", "register:40f0:8", ["const:533064:8", "const:4:8"]]
- 00533064 ["CALLIND", null, ["register:0:8"]]
+ 005330a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005330a4 ["INT_ADD", "register:40f0:8", ["const:5330a4:8", "const:4:8"]]
+ 005330a4 ["CALLIND", null, ["register:0:8"]]
- 00533064 bytes 20013fd6
+ 005330a4 bytes 20013fd6
- 00533090 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533090 ["INT_ADD", "register:40f0:8", ["const:533090:8", "const:4:8"]]
- 00533090 ["CALLIND", null, ["register:0:8"]]
+ 005330d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005330d0 ["INT_ADD", "register:40f0:8", ["const:5330d0:8", "const:4:8"]]
+ 005330d0 ["CALLIND", null, ["register:0:8"]]
- 00533090 bytes 20013fd6
+ 005330d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1101b026c4e17e8869e1e8aaeb71a9fa"></a>

### [`00533460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533460.md) → [`005334a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md) FUN_005334a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

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
      "definition_site": "00533544",
      "incomplete_value": true,
      "site": "00533544",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005334e0",
      "incomplete_value": false,
      "site": "005334e8",
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
            "const:edb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005334f0",
      "incomplete_value": false,
      "site": "005334f8",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
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
      "005334e0",
      "PARAM",
      [
        "storage",
        "002bfe9b",
        null,
        "string"
      ]
    ],
    [
      "005334f0",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ],
    [
      "00533534",
      "READ",
      [
        "storage",
        "002a8d77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005334e0",
      "PARAM",
      [
        "storage",
        "002bfedb",
        null,
        "string"
      ]
    ],
    [
      "005334f0",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ],
    [
      "00533534",
      "READ",
      [
        "storage",
        "002a8da6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005334a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533460.md#insn-005334a8) · [`005334b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533460.md#insn-005334b8) · [`005334a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533460.md#insn-005334a0)
- 新版 [`005334e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334e8) · [`005334f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334f8) · [`005334e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334e0)

~~~diff
- 005334a8 ["INT_ADD", "register:40f0:8", ["const:5334a8:8", "const:4:8"]]
- 005334a8 ["CALL", null, ["callee:00c58180:8"]]
+ 005334e8 ["INT_ADD", "register:40f0:8", ["const:5334e8:8", "const:4:8"]]
+ 005334e8 ["CALL", null, ["callee:00c58180:8"]]
- 005334a8 bytes 02931c94
+ 005334e8 bytes 26931c94
- 005334b8 ["INT_ADD", "register:40f0:8", ["const:5334b8:8", "const:4:8"]]
- 005334b8 ["CALL", null, ["callee:00c58040:8"]]
+ 005334f8 ["INT_ADD", "register:40f0:8", ["const:5334f8:8", "const:4:8"]]
+ 005334f8 ["CALL", null, ["callee:00c58040:8"]]
- 005334b8 bytes ae921c94
+ 005334f8 bytes d2921c94
- 005334a0 ["COPY", "tmp:0:8", ["const:e9b:8"]]
- 005334a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005334a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005334a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005334e0 ["COPY", "tmp:0:8", ["const:edb:8"]]
+ 005334e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005334e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005334e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005334a0 bytes 006c3a91
+ 005334e0 bytes 006c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e8aeb221f7726f1fee31e89eac457e8"></a>

### [`0053376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md) → [`005337ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md) FUN_005337ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00533838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533838.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00533878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533878.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533814",
      "incomplete_value": true,
      "site": "00533818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005337fc",
      "incomplete_value": true,
      "site": "005337fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533848",
      "incomplete_value": true,
      "site": "00533848",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005337ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0053380c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00533818",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005337ec",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053380c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533818",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005337bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md#insn-005337bc) · [`00533808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md#insn-00533808) · [`00533794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053376c.md#insn-00533794)
- 新版 [`005337fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-005337fc) · [`00533848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-00533848) · [`005337d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-005337d4)

~~~diff
- 005337bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005337bc ["INT_ADD", "register:40f0:8", ["const:5337bc:8", "const:4:8"]]
- 005337bc ["CALLIND", null, ["register:0:8"]]
+ 005337fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005337fc ["INT_ADD", "register:40f0:8", ["const:5337fc:8", "const:4:8"]]
+ 005337fc ["CALLIND", null, ["register:0:8"]]
- 005337bc bytes 20013fd6
+ 005337fc bytes 20013fd6
- 00533808 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533808 ["INT_ADD", "register:40f0:8", ["const:533808:8", "const:4:8"]]
- 00533808 ["CALLIND", null, ["register:0:8"]]
+ 00533848 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533848 ["INT_ADD", "register:40f0:8", ["const:533848:8", "const:4:8"]]
+ 00533848 ["CALLIND", null, ["register:0:8"]]
- 00533808 bytes 20013fd6
+ 00533848 bytes 20013fd6
- 00533794 ["COPY", "register:0:8", ["register:4040:8"]]
- 00533794 ["INT_ADD", "register:40f0:8", ["const:533794:8", "const:4:8"]]
- 00533794 ["CALLIND", null, ["register:0:8"]]
+ 005337d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005337d4 ["INT_ADD", "register:40f0:8", ["const:5337d4:8", "const:4:8"]]
+ 005337d4 ["CALLIND", null, ["register:0:8"]]
- 00533794 bytes 00013fd6
+ 005337d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aafaa6e6ab39d7ce25d09f435acfda7f"></a>

### [`005338b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005338b0.md) → [`005338f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md) FUN_005338f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533904",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00533910",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533934",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533904",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533910",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533934",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005338c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005338b0.md#insn-005338c4) · [`00533904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005338b0.md#insn-00533904) · [`005338dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005338b0.md#insn-005338dc)
- 新版 [`00533904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-00533904) · [`00533944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-00533944) · [`0053391c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-0053391c)

~~~diff
- 005338c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 005338c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533904 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00533904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005338c4 bytes 083947f9
+ 00533904 bytes 08a147f9
- 00533904 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533904 ["INT_ADD", "register:40f0:8", ["const:533904:8", "const:4:8"]]
- 00533904 ["CALLIND", null, ["register:0:8"]]
+ 00533944 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533944 ["INT_ADD", "register:40f0:8", ["const:533944:8", "const:4:8"]]
+ 00533944 ["CALLIND", null, ["register:0:8"]]
- 00533904 bytes 20013fd6
+ 00533944 bytes 20013fd6
- 005338dc ["INT_ADD", "register:40f0:8", ["const:5338dc:8", "const:4:8"]]
- 005338dc ["CALL", null, ["callee:00c57f80:8"]]
+ 0053391c ["INT_ADD", "register:40f0:8", ["const:53391c:8", "const:4:8"]]
+ 0053391c ["CALL", null, ["callee:00c57f80:8"]]
- 005338dc bytes 75911c94
+ 0053391c bytes 99911c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2272f5b196fd5acd0cbd048c86a0947"></a>

### [`00533930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533930.md) → [`00533970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md) FUN_00533970

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "0053398c",
      "incomplete_value": true,
      "site": "00533990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005339c4",
      "incomplete_value": true,
      "site": "005339c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533984",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00533990",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005339b4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533984",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533990",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005339b4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533930.md#insn-00533944) · [`00533984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533930.md#insn-00533984) · [`0053395c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533930.md#insn-0053395c)
- 新版 [`00533984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-00533984) · [`005339c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-005339c4) · [`0053399c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-0053399c)

~~~diff
- 00533944 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00533944 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533984 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00533984 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00533944 bytes 083947f9
+ 00533984 bytes 08a147f9
- 00533984 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533984 ["INT_ADD", "register:40f0:8", ["const:533984:8", "const:4:8"]]
- 00533984 ["CALLIND", null, ["register:0:8"]]
+ 005339c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005339c4 ["INT_ADD", "register:40f0:8", ["const:5339c4:8", "const:4:8"]]
+ 005339c4 ["CALLIND", null, ["register:0:8"]]
- 00533984 bytes 20013fd6
+ 005339c4 bytes 20013fd6
- 0053395c ["INT_ADD", "register:40f0:8", ["const:53395c:8", "const:4:8"]]
- 0053395c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053399c ["INT_ADD", "register:40f0:8", ["const:53399c:8", "const:4:8"]]
+ 0053399c ["CALL", null, ["callee:00c57f80:8"]]
- 0053395c bytes 55911c94
+ 0053399c bytes 79911c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588272234d53134e0512ce64cffeb252"></a>

### [`005339a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md) → [`005339e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md) FUN_005339e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00533ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533ac0.md) [`00533ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533ae4.md) [`00533aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533aec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 3件 [`00533b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b00.md) [`00533b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b24.md) [`00533b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b2c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533a5c",
      "incomplete_value": true,
      "site": "00533a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533a98",
      "incomplete_value": true,
      "site": "00533a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533a1c",
      "incomplete_value": true,
      "site": "00533a1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533a0c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533a54",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00533a60",
      "DATA",
      [
        "storage",
        "00c668a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00533a0c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533a54",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ],
    [
      "00533a60",
      "DATA",
      [
        "storage",
        "00c66978",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005339dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md#insn-005339dc) · [`00533a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md#insn-00533a40) · [`00533a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005339a4.md#insn-00533a8c)
- 新版 [`00533a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533a1c) · [`00533a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533a80) · [`00533acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533acc)

~~~diff
- 005339dc ["COPY", "register:0:8", ["register:4048:8"]]
- 005339dc ["INT_ADD", "register:40f0:8", ["const:5339dc:8", "const:4:8"]]
- 005339dc ["CALLIND", null, ["register:0:8"]]
+ 00533a1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a1c ["INT_ADD", "register:40f0:8", ["const:533a1c:8", "const:4:8"]]
+ 00533a1c ["CALLIND", null, ["register:0:8"]]
- 005339dc bytes 20013fd6
+ 00533a1c bytes 20013fd6
- 00533a40 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a40 ["INT_ADD", "register:40f0:8", ["const:533a40:8", "const:4:8"]]
- 00533a40 ["CALLIND", null, ["register:0:8"]]
+ 00533a80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a80 ["INT_ADD", "register:40f0:8", ["const:533a80:8", "const:4:8"]]
+ 00533a80 ["CALLIND", null, ["register:0:8"]]
- 00533a40 bytes 20013fd6
+ 00533a80 bytes 20013fd6
- 00533a8c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a8c ["INT_ADD", "register:40f0:8", ["const:533a8c:8", "const:4:8"]]
- 00533a8c ["CALLIND", null, ["register:0:8"]]
+ 00533acc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533acc ["INT_ADD", "register:40f0:8", ["const:533acc:8", "const:4:8"]]
+ 00533acc ["CALLIND", null, ["register:0:8"]]
- 00533a8c bytes 20013fd6
+ 00533acc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31ca53ef7dc24d2e7d6fce07e5aa5a1f"></a>

### [`00533b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533b48.md) → [`00533b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md) FUN_00533b88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533bc0",
      "incomplete_value": true,
      "site": "00533bc0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533bb0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533bdc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533bb0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533bdc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533b48.md#insn-00533b80) · [`00533bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533b48.md#insn-00533bac) · [`00533b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533b48.md#insn-00533b70)
- 新版 [`00533bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533bc0) · [`00533bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533bec) · [`00533bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533bb0)

~~~diff
- 00533b80 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533b80 ["INT_ADD", "register:40f0:8", ["const:533b80:8", "const:4:8"]]
- 00533b80 ["CALLIND", null, ["register:0:8"]]
+ 00533bc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533bc0 ["INT_ADD", "register:40f0:8", ["const:533bc0:8", "const:4:8"]]
+ 00533bc0 ["CALLIND", null, ["register:0:8"]]
- 00533b80 bytes 20013fd6
+ 00533bc0 bytes 20013fd6
- 00533bac ["COPY", "register:0:8", ["register:4048:8"]]
- 00533bac ["INT_ADD", "register:40f0:8", ["const:533bac:8", "const:4:8"]]
- 00533bac ["CALLIND", null, ["register:0:8"]]
+ 00533bec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533bec ["INT_ADD", "register:40f0:8", ["const:533bec:8", "const:4:8"]]
+ 00533bec ["CALLIND", null, ["register:0:8"]]
- 00533bac bytes 20013fd6
+ 00533bec bytes 20013fd6
- 00533b70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00533b70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533bb0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00533bb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533b70 bytes a99e43f9
+ 00533bb0 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bebdea2217c913f061b1b5177e9a14e6"></a>

### [`00533bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533bf4.md) → [`00533c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md) FUN_00533c34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533c6c",
      "incomplete_value": true,
      "site": "00533c6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533c98",
      "incomplete_value": true,
      "site": "00533c98",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533c5c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533c88",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533c5c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533c88",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533bf4.md#insn-00533c2c) · [`00533c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533bf4.md#insn-00533c58) · [`00533c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533bf4.md#insn-00533c1c)
- 新版 [`00533c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c6c) · [`00533c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c98) · [`00533c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c5c)

~~~diff
- 00533c2c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533c2c ["INT_ADD", "register:40f0:8", ["const:533c2c:8", "const:4:8"]]
- 00533c2c ["CALLIND", null, ["register:0:8"]]
+ 00533c6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c6c ["INT_ADD", "register:40f0:8", ["const:533c6c:8", "const:4:8"]]
+ 00533c6c ["CALLIND", null, ["register:0:8"]]
- 00533c2c bytes 20013fd6
+ 00533c6c bytes 20013fd6
- 00533c58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533c58 ["INT_ADD", "register:40f0:8", ["const:533c58:8", "const:4:8"]]
- 00533c58 ["CALLIND", null, ["register:0:8"]]
+ 00533c98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c98 ["INT_ADD", "register:40f0:8", ["const:533c98:8", "const:4:8"]]
+ 00533c98 ["CALLIND", null, ["register:0:8"]]
- 00533c58 bytes 20013fd6
+ 00533c98 bytes 20013fd6
- 00533c1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00533c1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533c5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00533c5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533c1c bytes a99e43f9
+ 00533c5c bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5742a7529401d67a2eaaf12e68a94367"></a>

### [`00533c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533c98.md) → [`00533cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md) FUN_00533cd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)

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
      "definition_site": "00533d80",
      "incomplete_value": true,
      "site": "00533d8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00533d7c",
      "incomplete_value": false,
      "site": "00533d8c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00533d3c",
      "incomplete_value": false,
      "site": "00533d4c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00533d7c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00533d80",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00533d80",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00533d7c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00533d80",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "00533d80",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533c98.md#insn-00533d4c) · [`00533cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533c98.md#insn-00533cf0) · [`00533d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533c98.md#insn-00533d08)
- 新版 [`00533d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d8c) · [`00533d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d30) · [`00533d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d48)

~~~diff
- 00533d4c ["INT_ADD", "register:40f0:8", ["const:533d4c:8", "const:4:8"]]
- 00533d4c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00533d8c ["INT_ADD", "register:40f0:8", ["const:533d8c:8", "const:4:8"]]
+ 00533d8c ["CALL", null, ["callee:00c57fe0:8"]]
- 00533d4c bytes 71901c94
+ 00533d8c bytes 95901c94
- 00533cf0 ["INT_ADD", "register:40f0:8", ["const:533cf0:8", "const:4:8"]]
- 00533cf0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00533d30 ["INT_ADD", "register:40f0:8", ["const:533d30:8", "const:4:8"]]
+ 00533d30 ["CALL", null, ["callee:00c57fc0:8"]]
- 00533cf0 bytes 80901c94
+ 00533d30 bytes a4901c94
- 00533d08 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533d08 ["INT_ADD", "register:40f0:8", ["const:533d08:8", "const:4:8"]]
- 00533d08 ["CALLIND", null, ["register:0:8"]]
+ 00533d48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533d48 ["INT_ADD", "register:40f0:8", ["const:533d48:8", "const:4:8"]]
+ 00533d48 ["CALLIND", null, ["register:0:8"]]
- 00533d08 bytes 20013fd6
+ 00533d48 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-605d96944f96e499960f6c48fb292082"></a>

### [`00533dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533dec.md) → [`00533e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md) FUN_00533e2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533e64",
      "incomplete_value": true,
      "site": "00533e64",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533e54",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533e80",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533e54",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533e80",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533dec.md#insn-00533e24) · [`00533e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533dec.md#insn-00533e50) · [`00533e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533dec.md#insn-00533e14)
- 新版 [`00533e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e64) · [`00533e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e90) · [`00533e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e54)

~~~diff
- 00533e24 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e24 ["INT_ADD", "register:40f0:8", ["const:533e24:8", "const:4:8"]]
- 00533e24 ["CALLIND", null, ["register:0:8"]]
+ 00533e64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e64 ["INT_ADD", "register:40f0:8", ["const:533e64:8", "const:4:8"]]
+ 00533e64 ["CALLIND", null, ["register:0:8"]]
- 00533e24 bytes 20013fd6
+ 00533e64 bytes 20013fd6
- 00533e50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e50 ["INT_ADD", "register:40f0:8", ["const:533e50:8", "const:4:8"]]
- 00533e50 ["CALLIND", null, ["register:0:8"]]
+ 00533e90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e90 ["INT_ADD", "register:40f0:8", ["const:533e90:8", "const:4:8"]]
+ 00533e90 ["CALLIND", null, ["register:0:8"]]
- 00533e50 bytes 20013fd6
+ 00533e90 bytes 20013fd6
- 00533e14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00533e14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533e54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00533e54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533e14 bytes a99e43f9
+ 00533e54 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650ca524bdf2e491838e5f7918da4cda"></a>

### [`00533e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533e98.md) → [`00533ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md) FUN_00533ed8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00533f10",
      "incomplete_value": true,
      "site": "00533f10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533f3c",
      "incomplete_value": true,
      "site": "00533f3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00533f00",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00533f2c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00533f00",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533f2c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533e98.md#insn-00533ed0) · [`00533efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533e98.md#insn-00533efc) · [`00533ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533e98.md#insn-00533ec0)
- 新版 [`00533f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533f10) · [`00533f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533f3c) · [`00533f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533f00)

~~~diff
- 00533ed0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533ed0 ["INT_ADD", "register:40f0:8", ["const:533ed0:8", "const:4:8"]]
- 00533ed0 ["CALLIND", null, ["register:0:8"]]
+ 00533f10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533f10 ["INT_ADD", "register:40f0:8", ["const:533f10:8", "const:4:8"]]
+ 00533f10 ["CALLIND", null, ["register:0:8"]]
- 00533ed0 bytes 20013fd6
+ 00533f10 bytes 20013fd6
- 00533efc ["COPY", "register:0:8", ["register:4048:8"]]
- 00533efc ["INT_ADD", "register:40f0:8", ["const:533efc:8", "const:4:8"]]
- 00533efc ["CALLIND", null, ["register:0:8"]]
+ 00533f3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533f3c ["INT_ADD", "register:40f0:8", ["const:533f3c:8", "const:4:8"]]
+ 00533f3c ["CALLIND", null, ["register:0:8"]]
- 00533efc bytes 20013fd6
+ 00533f3c bytes 20013fd6
- 00533ec0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00533ec0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533f00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00533f00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00533ec0 bytes a99e43f9
+ 00533f00 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c375cb19877870d05013d601b8761281"></a>

### [`0053403c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053403c.md) → [`0053407c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md) FUN_0053407c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00534094",
      "incomplete_value": false,
      "site": "00534098",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00534098",
      "DATA",
      [
        "storage",
        "00c66e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534098",
      "DATA",
      [
        "storage",
        "00c66f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053403c.md#insn-00534054) · [`00534064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053403c.md#insn-00534064)
- 新版 [`00534094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md#insn-00534094) · [`005340a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md#insn-005340a4)

~~~diff
- 00534054 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00534054 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534054 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534054 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534094 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00534094 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534094 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534094 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534054 bytes 29a13991
+ 00534094 bytes 29e13c91
- 00534064 ["INT_ADD", "register:40f0:8", ["const:534064:8", "const:4:8"]]
- 00534064 ["CALL", null, ["callee:00c57f80:8"]]
+ 005340a4 ["INT_ADD", "register:40f0:8", ["const:5340a4:8", "const:4:8"]]
+ 005340a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00534064 bytes 938f1c94
+ 005340a4 bytes b78f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d4be722a2ad94a95d2cc09a5523fc5"></a>

### [`005340a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005340a0.md) → [`005340e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md) FUN_005340e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c587c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58890.md)

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
      "definition_site": "00534128",
      "incomplete_value": true,
      "site": "00534128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:462:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534154",
      "incomplete_value": true,
      "site": "00534160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534150",
      "incomplete_value": false,
      "site": "00534160",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00534110",
      "incomplete_value": false,
      "site": "00534120",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00534114",
      "READ",
      [
        "storage",
        "002b7422",
        null,
        "string"
      ]
    ],
    [
      "00534150",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00534154",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534114",
      "READ",
      [
        "storage",
        "002b7462",
        null,
        "string"
      ]
    ],
    [
      "00534150",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00534154",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005340a0.md#insn-00534120) · [`005340c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005340a0.md#insn-005340c4) · [`005340cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005340a0.md#insn-005340cc)
- 新版 [`00534160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-00534160) · [`00534104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-00534104) · [`0053410c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-0053410c)

~~~diff
- 00534120 ["INT_ADD", "register:40f0:8", ["const:534120:8", "const:4:8"]]
- 00534120 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00534160 ["INT_ADD", "register:40f0:8", ["const:534160:8", "const:4:8"]]
+ 00534160 ["CALL", null, ["callee:00c57fe0:8"]]
- 00534120 bytes 7c8f1c94
+ 00534160 bytes a08f1c94
- 005340c4 ["INT_ADD", "register:40f0:8", ["const:5340c4:8", "const:4:8"]]
- 005340c4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00534104 ["INT_ADD", "register:40f0:8", ["const:534104:8", "const:4:8"]]
+ 00534104 ["CALL", null, ["callee:00c57fc0:8"]]
- 005340c4 bytes 8b8f1c94
+ 00534104 bytes af8f1c94
- 005340cc ["COPY", "tmp:0:8", ["const:422:8"]]
- 005340cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005340cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005340cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053410c ["COPY", "tmp:0:8", ["const:462:8"]]
+ 0053410c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053410c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053410c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005340cc bytes 29891091
+ 0053410c bytes 29891191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bff38f36af5bc1903dbf737ebc924c5f"></a>

### [`00534168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534168.md) → [`005341a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md) FUN_005341a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005341c0",
      "incomplete_value": false,
      "site": "005341c4",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
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
      "005341c4",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005341c4",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534168.md#insn-00534180) · [`00534190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534168.md#insn-00534190)
- 新版 [`005341c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md#insn-005341c0) · [`005341d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md#insn-005341d0)

~~~diff
- 00534180 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00534180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005341c0 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 005341c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005341c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005341c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534180 bytes 29e13a91
+ 005341c0 bytes 29213e91
- 00534190 ["INT_ADD", "register:40f0:8", ["const:534190:8", "const:4:8"]]
- 00534190 ["CALL", null, ["callee:00c57f80:8"]]
+ 005341d0 ["INT_ADD", "register:40f0:8", ["const:5341d0:8", "const:4:8"]]
+ 005341d0 ["CALL", null, ["callee:00c57f80:8"]]
- 00534190 bytes 488f1c94
+ 005341d0 bytes 6c8f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-385344e49f880e7def7f568dab16ebd2"></a>

### [`005341cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005341cc.md) → [`0053420c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md) FUN_0053420c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c587c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58890.md)

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
      "definition_site": "00534254",
      "incomplete_value": true,
      "site": "00534254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:462:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534280",
      "incomplete_value": true,
      "site": "0053428c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053427c",
      "incomplete_value": false,
      "site": "0053428c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0053423c",
      "incomplete_value": false,
      "site": "0053424c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00534240",
      "READ",
      [
        "storage",
        "002b7422",
        null,
        "string"
      ]
    ],
    [
      "0053427c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00534280",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534240",
      "READ",
      [
        "storage",
        "002b7462",
        null,
        "string"
      ]
    ],
    [
      "0053427c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00534280",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053424c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005341cc.md#insn-0053424c) · [`005341f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005341cc.md#insn-005341f0) · [`005341f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005341cc.md#insn-005341f8)
- 新版 [`0053428c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-0053428c) · [`00534230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-00534230) · [`00534238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-00534238)

~~~diff
- 0053424c ["INT_ADD", "register:40f0:8", ["const:53424c:8", "const:4:8"]]
- 0053424c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0053428c ["INT_ADD", "register:40f0:8", ["const:53428c:8", "const:4:8"]]
+ 0053428c ["CALL", null, ["callee:00c57fe0:8"]]
- 0053424c bytes 318f1c94
+ 0053428c bytes 558f1c94
- 005341f0 ["INT_ADD", "register:40f0:8", ["const:5341f0:8", "const:4:8"]]
- 005341f0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00534230 ["INT_ADD", "register:40f0:8", ["const:534230:8", "const:4:8"]]
+ 00534230 ["CALL", null, ["callee:00c57fc0:8"]]
- 005341f0 bytes 408f1c94
+ 00534230 bytes 648f1c94
- 005341f8 ["COPY", "tmp:0:8", ["const:422:8"]]
- 005341f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005341f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005341f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534238 ["COPY", "tmp:0:8", ["const:462:8"]]
+ 00534238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005341f8 bytes 29891091
+ 00534238 bytes 29891191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a95b2d4f180339cfa3caf450562456da"></a>

### [`00534294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534294.md) → [`005342d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md) FUN_005342d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "00534304",
      "incomplete_value": true,
      "site": "00534318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e01:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534308",
      "incomplete_value": true,
      "site": "0053431c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534328",
      "incomplete_value": true,
      "site": "00534328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00534304",
      "READ",
      [
        "storage",
        "002b1dd0",
        null,
        "string"
      ]
    ],
    [
      "00534308",
      "READ",
      [
        "storage",
        "002b1dd9",
        null,
        "string"
      ]
    ],
    [
      "00534310",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534304",
      "READ",
      [
        "storage",
        "002b1e01",
        null,
        "string"
      ]
    ],
    [
      "00534308",
      "READ",
      [
        "storage",
        "002b1e0a",
        null,
        "string"
      ]
    ],
    [
      "00534310",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005342a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534294.md#insn-005342a8) · [`00534318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534294.md#insn-00534318) · [`0053431c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534294.md#insn-0053431c)
- 新版 [`005342e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md#insn-005342e8) · [`0053435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md#insn-0053435c)

~~~diff
- 005342a8 ["INT_ADD", "register:40f0:8", ["const:5342a8:8", "const:4:8"]]
- 005342a8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 005342e8 ["INT_ADD", "register:40f0:8", ["const:5342e8:8", "const:4:8"]]
+ 005342e8 ["CALL", null, ["callee:00c57fc0:8"]]
- 005342a8 bytes 128f1c94
+ 005342e8 bytes 368f1c94
- 00534318 ["COPY", "register:4000:8", ["register:4098:8"]]
- 00534318 bytes e00313aa
- 0053431c ["INT_ADD", "register:40f0:8", ["const:53431c:8", "const:4:8"]]
- 0053431c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0053435c ["INT_ADD", "register:40f0:8", ["const:53435c:8", "const:4:8"]]
+ 0053435c ["CALL", null, ["callee:00c57fe0:8"]]
- 0053431c bytes fd8e1c94
+ 0053435c bytes 218f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cb470b241cac3fec0145fc2008b99fd"></a>

### [`00534360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534360.md) → [`005343a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md) FUN_005343a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "005343d0",
      "incomplete_value": true,
      "site": "005343e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005343d4",
      "incomplete_value": true,
      "site": "005343e8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005343f4",
      "incomplete_value": true,
      "site": "005343f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005343d0",
      "READ",
      [
        "storage",
        "002a67a4",
        null,
        "string"
      ]
    ],
    [
      "005343d4",
      "READ",
      [
        "storage",
        "002a67b2",
        null,
        "string"
      ]
    ],
    [
      "005343dc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005343d0",
      "READ",
      [
        "storage",
        "002a6748",
        null,
        "string"
      ]
    ],
    [
      "005343d4",
      "READ",
      [
        "storage",
        "002a6756",
        null,
        "string"
      ]
    ],
    [
      "005343dc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534360.md#insn-00534374) · [`005343e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534360.md#insn-005343e4) · [`005343e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534360.md#insn-005343e8)
- 新版 [`005343b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md#insn-005343b4) · [`00534428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md#insn-00534428)

~~~diff
- 00534374 ["INT_ADD", "register:40f0:8", ["const:534374:8", "const:4:8"]]
- 00534374 ["CALL", null, ["callee:00c57fc0:8"]]
+ 005343b4 ["INT_ADD", "register:40f0:8", ["const:5343b4:8", "const:4:8"]]
+ 005343b4 ["CALL", null, ["callee:00c57fc0:8"]]
- 00534374 bytes df8e1c94
+ 005343b4 bytes 038f1c94
- 005343e4 ["COPY", "register:4000:8", ["register:4098:8"]]
- 005343e4 bytes e00313aa
- 005343e8 ["INT_ADD", "register:40f0:8", ["const:5343e8:8", "const:4:8"]]
- 005343e8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00534428 ["INT_ADD", "register:40f0:8", ["const:534428:8", "const:4:8"]]
+ 00534428 ["CALL", null, ["callee:00c57fe0:8"]]
- 005343e8 bytes ca8e1c94
+ 00534428 bytes ee8e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba0b984cdf01542ff899587682ee5a0"></a>

### [`0053442c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053442c.md) → [`0053446c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053446c.md) FUN_0053446c

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
      "definition_site": "0053447c",
      "incomplete_value": false,
      "site": "0053447c",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "0053447c",
      "DATA",
      [
        "storage",
        "00c66f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053447c",
      "DATA",
      [
        "storage",
        "00c66fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053442c.md#insn-00534438)
- 新版 [`00534478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053446c.md#insn-00534478)

~~~diff
- 00534438 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00534438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534478 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00534478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534438 bytes 29613c91
+ 00534478 bytes 29a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1dce583d947e2debc02db229cd40a3"></a>

### [`00534458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534458.md) → [`00534498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534498.md) FUN_00534498

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
      "definition_site": "005344a8",
      "incomplete_value": false,
      "site": "005344a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
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
      "005344a8",
      "DATA",
      [
        "storage",
        "00c66f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005344a8",
      "DATA",
      [
        "storage",
        "00c67018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534458.md#insn-00534460) · [`00534464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534458.md#insn-00534464)
- 新版 [`005344a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534498.md#insn-005344a0) · [`005344a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534498.md#insn-005344a4)

~~~diff
- 00534460 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 005344a0 ["COPY", "register:4048:8", ["const:c67000:8"]]
- 00534460 bytes 893900d0
+ 005344a0 bytes 893900f0
- 00534464 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00534464 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534464 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534464 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005344a4 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 005344a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005344a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005344a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534464 bytes 29213d91
+ 005344a4 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fbd0e7f9450384c6f58b2313d89a781"></a>

### [`00534484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534484.md) → [`005344c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md) FUN_005344c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "005344e8",
      "incomplete_value": true,
      "site": "005344f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534514",
      "incomplete_value": true,
      "site": "00534514",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005344dc",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005344f4",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534504",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005344dc",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "005344f4",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534504",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534484.md#insn-00534494) · [`005344d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534484.md#insn-005344d4) · [`00534500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534484.md#insn-00534500)
- 新版 [`005344d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-005344d4) · [`00534514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-00534514) · [`00534540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-00534540)

~~~diff
- 00534494 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005344d4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534494 bytes 283b00d0
+ 005344d4 bytes 283b00f0
- 005344d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005344d4 ["INT_ADD", "register:40f0:8", ["const:5344d4:8", "const:4:8"]]
- 005344d4 ["CALLIND", null, ["register:0:8"]]
+ 00534514 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534514 ["INT_ADD", "register:40f0:8", ["const:534514:8", "const:4:8"]]
+ 00534514 ["CALLIND", null, ["register:0:8"]]
- 005344d4 bytes 20013fd6
+ 00534514 bytes 20013fd6
- 00534500 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534500 ["INT_ADD", "register:40f0:8", ["const:534500:8", "const:4:8"]]
- 00534500 ["CALLIND", null, ["register:0:8"]]
+ 00534540 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534540 ["INT_ADD", "register:40f0:8", ["const:534540:8", "const:4:8"]]
+ 00534540 ["CALLIND", null, ["register:0:8"]]
- 00534500 bytes 20013fd6
+ 00534540 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e01397c0877156f492f408536bc1988"></a>

### [`00534530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534530.md) → [`00534570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md) FUN_00534570

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00534594",
      "incomplete_value": true,
      "site": "005345a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005345c0",
      "incomplete_value": true,
      "site": "005345c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005345ec",
      "incomplete_value": true,
      "site": "005345ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00534588",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005345a0",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005345b0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534588",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "005345a0",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005345b0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534530.md#insn-00534540) · [`00534580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534530.md#insn-00534580) · [`005345ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534530.md#insn-005345ac)
- 新版 [`00534580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-00534580) · [`005345c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-005345c0) · [`005345ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-005345ec)

~~~diff
- 00534540 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00534580 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534540 bytes 283b00d0
+ 00534580 bytes 283b00f0
- 00534580 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534580 ["INT_ADD", "register:40f0:8", ["const:534580:8", "const:4:8"]]
- 00534580 ["CALLIND", null, ["register:0:8"]]
+ 005345c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005345c0 ["INT_ADD", "register:40f0:8", ["const:5345c0:8", "const:4:8"]]
+ 005345c0 ["CALLIND", null, ["register:0:8"]]
- 00534580 bytes 20013fd6
+ 005345c0 bytes 20013fd6
- 005345ac ["COPY", "register:0:8", ["register:4048:8"]]
- 005345ac ["INT_ADD", "register:40f0:8", ["const:5345ac:8", "const:4:8"]]
- 005345ac ["CALLIND", null, ["register:0:8"]]
+ 005345ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005345ec ["INT_ADD", "register:40f0:8", ["const:5345ec:8", "const:4:8"]]
+ 005345ec ["CALLIND", null, ["register:0:8"]]
- 005345ac bytes 20013fd6
+ 005345ec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d910d4418e1bb9dad4279db21cc1b89a"></a>

### [`005345f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005345f8.md) → [`00534638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md) FUN_00534638

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005400d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005400d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0053464c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "0053464c",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "0053464c",
      "PARAM",
      [
        "storage",
        "00c67328",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "0053464c",
      "READ",
      [
        "storage",
        "00c9b0b8",
        null,
        "pointer"
      ]
    ],
    [
      "0053464c",
      "PARAM",
      [
        "storage",
        "00c673f8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005345f8.md#insn-00534610) · [`00534604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005345f8.md#insn-00534604) · [`0053460c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005345f8.md#insn-0053460c)
- 新版 [`00534650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-00534650) · [`00534644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-00534644) · [`0053464c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-0053464c)

~~~diff
- 00534610 ["INT_ADD", "register:40f0:8", ["const:534610:8", "const:4:8"]]
- 00534610 ["CALL", null, ["callee:00540114:8"]]
+ 00534650 ["INT_ADD", "register:40f0:8", ["const:534650:8", "const:4:8"]]
+ 00534650 ["CALL", null, ["callee:00540114:8"]]
- 00534610 bytes b12e0094
+ 00534650 bytes b12e0094
- 00534604 ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 00534644 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00534604 bytes 213b00d0
+ 00534644 bytes 213b00f0
- 0053460c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 0053460c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053464c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b8:8"]]
+ 0053464c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053460c bytes 21f447f9
+ 0053464c bytes 215c40f9
~~~


<a id="compare-596029a594acee12d6d9579695bbcd32"></a>

### [`00534634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534634.md) → [`00534674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md) FUN_00534674

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005400d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005400d4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00534688",
      "incomplete_value": true,
      "site": "00534690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00534688",
      "READ",
      [
        "storage",
        "00c9afe8",
        null,
        "pointer"
      ]
    ],
    [
      "00534688",
      "PARAM",
      [
        "storage",
        "00c67328",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "00534688",
      "READ",
      [
        "storage",
        "00c9b0b8",
        null,
        "pointer"
      ]
    ],
    [
      "00534688",
      "PARAM",
      [
        "storage",
        "00c673f8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534634.md#insn-00534650) · [`00534640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534634.md#insn-00534640) · [`00534648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534634.md#insn-00534648)
- 新版 [`00534690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534690) · [`00534680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534680) · [`00534688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534688)

~~~diff
- 00534650 ["INT_ADD", "register:40f0:8", ["const:534650:8", "const:4:8"]]
- 00534650 ["CALL", null, ["callee:00540114:8"]]
+ 00534690 ["INT_ADD", "register:40f0:8", ["const:534690:8", "const:4:8"]]
+ 00534690 ["CALL", null, ["callee:00540114:8"]]
- 00534650 bytes a12e0094
+ 00534690 bytes a12e0094
- 00534640 ["COPY", "register:4008:8", ["const:c9a000:8"]]
+ 00534680 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00534640 bytes 213b00d0
+ 00534680 bytes 213b00f0
- 00534648 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 00534648 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b8:8"]]
+ 00534688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00534648 bytes 21f447f9
+ 00534688 bytes 215c40f9
~~~


<a id="compare-cba58eb6afa79e571441671c05976760"></a>

### [`0053480c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053480c.md) → [`0053484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md) FUN_0053484c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005348a8",
      "incomplete_value": true,
      "site": "005348ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00534860",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "0053486c",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005348a0",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534860",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "0053486c",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005348a0",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053480c.md#insn-00534820) · [`0053483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053480c.md#insn-0053483c) · [`00534850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/0053480c.md#insn-00534850)
- 新版 [`00534860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-00534860) · [`0053487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-0053487c) · [`00534890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-00534890)

~~~diff
- 00534820 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
- 00534820 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534860 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
+ 00534860 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534820 bytes 087140f9
+ 00534860 bytes 08d940f9
- 0053483c ["INT_ADD", "register:40f0:8", ["const:53483c:8", "const:4:8"]]
- 0053483c ["CALL", null, ["callee:00c53da0:8"]]
+ 0053487c ["INT_ADD", "register:40f0:8", ["const:53487c:8", "const:4:8"]]
+ 0053487c ["CALL", null, ["callee:00c53da0:8"]]
- 0053483c bytes 317d1c94
+ 0053487c bytes 497d1c94
- 00534850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00534850 ["INT_ADD", "register:40f0:8", ["const:534850:8", "const:4:8"]]
- 00534850 ["CALLIND", null, ["register:0:8"]]
+ 00534890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00534890 ["INT_ADD", "register:40f0:8", ["const:534890:8", "const:4:8"]]
+ 00534890 ["CALLIND", null, ["register:0:8"]]
- 00534850 bytes 00013fd6
+ 00534890 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f9910ce3c1a2efb6768472a12a826d"></a>

### [`005348bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005348bc.md) → [`005348fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md) FUN_005348fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00534918",
      "incomplete_value": true,
      "site": "0053491c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00534910",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0053491c",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00534910",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0053491c",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005348d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005348bc.md#insn-005348d0) · [`005348e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005348bc.md#insn-005348e8) · [`005348f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/005348bc.md#insn-005348f8)
- 新版 [`00534910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534910) · [`00534928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534928) · [`00534938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534938)

~~~diff
- 005348d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 005348d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00534910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005348d0 bytes 08ad40f9
+ 00534910 bytes 081541f9
- 005348e8 ["INT_ADD", "register:40f0:8", ["const:5348e8:8", "const:4:8"]]
- 005348e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00534928 ["INT_ADD", "register:40f0:8", ["const:534928:8", "const:4:8"]]
+ 00534928 ["CALL", null, ["callee:00c57f80:8"]]
- 005348e8 bytes 728d1c94
+ 00534928 bytes 968d1c94
- 005348f8 ["INT_ADD", "register:40f0:8", ["const:5348f8:8", "const:4:8"]]
- 005348f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00534938 ["INT_ADD", "register:40f0:8", ["const:534938:8", "const:4:8"]]
+ 00534938 ["CALL", null, ["callee:00c57f80:8"]]
- 005348f8 bytes 6e8d1c94
+ 00534938 bytes 928d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bd79380bc0de0923f835c8445dabe1a"></a>

### [`00534d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534d88.md) → [`00534dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md) FUN_00534dc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00534de4",
      "incomplete_value": true,
      "site": "00534de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00534ddc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00534de8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00534ddc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00534de8",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534d88.md#insn-00534d9c) · [`00534db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534d88.md#insn-00534db4) · [`00534dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534d88.md#insn-00534dbc)
- 新版 [`00534ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534ddc) · [`00534df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534df4) · [`00534dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534dfc)

~~~diff
- 00534d9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00534d9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534ddc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00534ddc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534d9c bytes 08e946f9
+ 00534ddc bytes 085147f9
- 00534db4 ["INT_ADD", "register:40f0:8", ["const:534db4:8", "const:4:8"]]
- 00534db4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00534df4 ["INT_ADD", "register:40f0:8", ["const:534df4:8", "const:4:8"]]
+ 00534df4 ["CALL", null, ["callee:00c57f80:8"]]
- 00534db4 bytes 3f8c1c94
+ 00534df4 bytes 638c1c94
- 00534dbc ["INT_ADD", "register:40f0:8", ["const:534dbc:8", "const:4:8"]]
- 00534dbc ["CALL", null, ["callee:00c583b0:8"]]
+ 00534dfc ["INT_ADD", "register:40f0:8", ["const:534dfc:8", "const:4:8"]]
+ 00534dfc ["CALL", null, ["callee:00c583b0:8"]]
- 00534dbc bytes 498d1c94
+ 00534dfc bytes 6d8d1c94
~~~


<a id="compare-99955734b4f89199b9b1bac481c3c830"></a>

### [`00534de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534de8.md) → [`00534e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md) FUN_00534e28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00534e44",
      "incomplete_value": true,
      "site": "00534e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00534e3c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00534e48",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00534e3c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00534e48",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534de8.md#insn-00534dfc) · [`00534e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534de8.md#insn-00534e14) · [`00534e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534de8.md#insn-00534e1c)
- 新版 [`00534e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e3c) · [`00534e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e54) · [`00534e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e5c)

~~~diff
- 00534dfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00534dfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00534e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534dfc bytes 08e946f9
+ 00534e3c bytes 085147f9
- 00534e14 ["INT_ADD", "register:40f0:8", ["const:534e14:8", "const:4:8"]]
- 00534e14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00534e54 ["INT_ADD", "register:40f0:8", ["const:534e54:8", "const:4:8"]]
+ 00534e54 ["CALL", null, ["callee:00c57f80:8"]]
- 00534e14 bytes 278c1c94
+ 00534e54 bytes 4b8c1c94
- 00534e1c ["INT_ADD", "register:40f0:8", ["const:534e1c:8", "const:4:8"]]
- 00534e1c ["CALL", null, ["callee:00c583b0:8"]]
+ 00534e5c ["INT_ADD", "register:40f0:8", ["const:534e5c:8", "const:4:8"]]
+ 00534e5c ["CALL", null, ["callee:00c583b0:8"]]
- 00534e1c bytes 318d1c94
+ 00534e5c bytes 558d1c94
~~~


<a id="compare-15bc814786e280c49dd6eb418c36996b"></a>

### [`00534eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534eb8.md) → [`00534ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md) FUN_00534ef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00534f14",
      "incomplete_value": true,
      "site": "00534f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534f4c",
      "incomplete_value": true,
      "site": "00534f4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00534f0c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00534f18",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f3c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534f0c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00534f18",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f3c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534eb8.md#insn-00534ecc) · [`00534f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534eb8.md#insn-00534f0c) · [`00534ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534eb8.md#insn-00534ee4)
- 新版 [`00534f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f0c) · [`00534f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f4c) · [`00534f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f24)

~~~diff
- 00534ecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00534ecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534f0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00534f0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534ecc bytes 083947f9
+ 00534f0c bytes 08a147f9
- 00534f0c ["COPY", "register:0:8", ["register:4048:8"]]
- 00534f0c ["INT_ADD", "register:40f0:8", ["const:534f0c:8", "const:4:8"]]
- 00534f0c ["CALLIND", null, ["register:0:8"]]
+ 00534f4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534f4c ["INT_ADD", "register:40f0:8", ["const:534f4c:8", "const:4:8"]]
+ 00534f4c ["CALLIND", null, ["register:0:8"]]
- 00534f0c bytes 20013fd6
+ 00534f4c bytes 20013fd6
- 00534ee4 ["INT_ADD", "register:40f0:8", ["const:534ee4:8", "const:4:8"]]
- 00534ee4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00534f24 ["INT_ADD", "register:40f0:8", ["const:534f24:8", "const:4:8"]]
+ 00534f24 ["CALL", null, ["callee:00c57f80:8"]]
- 00534ee4 bytes f38b1c94
+ 00534f24 bytes 178c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4da80f1e1815b7fdd9b0c2fc3cb75bdd"></a>

### [`00534f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534f30.md) → [`00534f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md) FUN_00534f70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00534f8c",
      "incomplete_value": true,
      "site": "00534f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534fc4",
      "incomplete_value": true,
      "site": "00534fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00534f84",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00534f90",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534fb4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534f84",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00534f90",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534fb4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534f30.md#insn-00534f44) · [`00534f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534f30.md#insn-00534f84) · [`00534f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00534/00534f30.md#insn-00534f5c)
- 新版 [`00534f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534f84) · [`00534fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534fc4) · [`00534f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534f9c)

~~~diff
- 00534f44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00534f44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534f84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00534f84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534f44 bytes 083947f9
+ 00534f84 bytes 08a147f9
- 00534f84 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534f84 ["INT_ADD", "register:40f0:8", ["const:534f84:8", "const:4:8"]]
- 00534f84 ["CALLIND", null, ["register:0:8"]]
+ 00534fc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534fc4 ["INT_ADD", "register:40f0:8", ["const:534fc4:8", "const:4:8"]]
+ 00534fc4 ["CALLIND", null, ["register:0:8"]]
- 00534f84 bytes 20013fd6
+ 00534fc4 bytes 20013fd6
- 00534f5c ["INT_ADD", "register:40f0:8", ["const:534f5c:8", "const:4:8"]]
- 00534f5c ["CALL", null, ["callee:00c57f80:8"]]
+ 00534f9c ["INT_ADD", "register:40f0:8", ["const:534f9c:8", "const:4:8"]]
+ 00534f9c ["CALL", null, ["callee:00c57f80:8"]]
- 00534f5c bytes d58b1c94
+ 00534f9c bytes f98b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec6a2bd3263277d7e600229c9bdb0464"></a>

### [`00535034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535034.md) → [`00535074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md) FUN_00535074

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
      "definition_site": "00535088",
      "incomplete_value": true,
      "site": "00535088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053507c",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "00535088",
      "DATA",
      [
        "storage",
        "00c66d58",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "0053507c",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00535088",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535034.md#insn-00535034) · [`0053503c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535034.md#insn-0053503c)
- 新版 [`00535074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md#insn-00535074) · [`0053507c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md#insn-0053507c)

~~~diff
- 00535034 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00535074 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00535034 bytes 293b00b0
+ 00535074 bytes 293b00d0
- 0053503c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fb0:8"]]
- 0053503c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053507c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
+ 0053507c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053503c bytes 29d947f9
+ 0053507c bytes 294140f9
~~~


<a id="compare-9195dae28d9ff12a8e0e9bd370c8e2cf"></a>

### [`00535358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535358.md) → [`00535398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md) FUN_00535398

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005353b4",
      "incomplete_value": true,
      "site": "005353b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005353ac",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005353b8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005353ac",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005353b8",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053536c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535358.md#insn-0053536c) · [`00535384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535358.md#insn-00535384) · [`0053538c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535358.md#insn-0053538c)
- 新版 [`005353ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353ac) · [`005353c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353c4) · [`005353cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353cc)

~~~diff
- 0053536c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0053536c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005353ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005353ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053536c bytes 08e946f9
+ 005353ac bytes 085147f9
- 00535384 ["INT_ADD", "register:40f0:8", ["const:535384:8", "const:4:8"]]
- 00535384 ["CALL", null, ["callee:00c57f80:8"]]
+ 005353c4 ["INT_ADD", "register:40f0:8", ["const:5353c4:8", "const:4:8"]]
+ 005353c4 ["CALL", null, ["callee:00c57f80:8"]]
- 00535384 bytes cb8a1c94
+ 005353c4 bytes ef8a1c94
- 0053538c ["INT_ADD", "register:40f0:8", ["const:53538c:8", "const:4:8"]]
- 0053538c ["CALL", null, ["callee:00c583b0:8"]]
+ 005353cc ["INT_ADD", "register:40f0:8", ["const:5353cc:8", "const:4:8"]]
+ 005353cc ["CALL", null, ["callee:00c583b0:8"]]
- 0053538c bytes d58b1c94
+ 005353cc bytes f98b1c94
~~~


<a id="compare-2eb9d5f21b28037e732ce6f76ddf1a4d"></a>

### [`005353a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353a0.md) → [`005353e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md) FUN_005353e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005353fc",
      "incomplete_value": true,
      "site": "00535400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005353f4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535400",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005353f4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535400",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005353b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353a0.md#insn-005353b4) · [`005353cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353a0.md#insn-005353cc) · [`005353d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353a0.md#insn-005353d4)
- 新版 [`005353f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-005353f4) · [`0053540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-0053540c) · [`00535414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-00535414)

~~~diff
- 005353b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005353b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005353f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005353f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005353b4 bytes 08e946f9
+ 005353f4 bytes 085147f9
- 005353cc ["INT_ADD", "register:40f0:8", ["const:5353cc:8", "const:4:8"]]
- 005353cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0053540c ["INT_ADD", "register:40f0:8", ["const:53540c:8", "const:4:8"]]
+ 0053540c ["CALL", null, ["callee:00c57f80:8"]]
- 005353cc bytes b98a1c94
+ 0053540c bytes dd8a1c94
- 005353d4 ["INT_ADD", "register:40f0:8", ["const:5353d4:8", "const:4:8"]]
- 005353d4 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535414 ["INT_ADD", "register:40f0:8", ["const:535414:8", "const:4:8"]]
+ 00535414 ["CALL", null, ["callee:00c583b0:8"]]
- 005353d4 bytes c38b1c94
+ 00535414 bytes e78b1c94
~~~


<a id="compare-226bf47c4e25a43dd0f0f1c2edd23a44"></a>

### [`005353e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353e8.md) → [`00535428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md) FUN_00535428

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535444",
      "incomplete_value": true,
      "site": "00535448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053543c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535448",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053543c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535448",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005353fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353e8.md#insn-005353fc) · [`00535414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353e8.md#insn-00535414) · [`0053541c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005353e8.md#insn-0053541c)
- 新版 [`0053543c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-0053543c) · [`00535454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-00535454) · [`0053545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-0053545c)

~~~diff
- 005353fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005353fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053543c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053543c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005353fc bytes 08e946f9
+ 0053543c bytes 085147f9
- 00535414 ["INT_ADD", "register:40f0:8", ["const:535414:8", "const:4:8"]]
- 00535414 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535454 ["INT_ADD", "register:40f0:8", ["const:535454:8", "const:4:8"]]
+ 00535454 ["CALL", null, ["callee:00c57f80:8"]]
- 00535414 bytes a78a1c94
+ 00535454 bytes cb8a1c94
- 0053541c ["INT_ADD", "register:40f0:8", ["const:53541c:8", "const:4:8"]]
- 0053541c ["CALL", null, ["callee:00c583b0:8"]]
+ 0053545c ["INT_ADD", "register:40f0:8", ["const:53545c:8", "const:4:8"]]
+ 0053545c ["CALL", null, ["callee:00c583b0:8"]]
- 0053541c bytes b18b1c94
+ 0053545c bytes d58b1c94
~~~


<a id="compare-166e6551357cb409ee2743c6e315251e"></a>

### [`00535430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535430.md) → [`00535470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md) FUN_00535470

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "0053548c",
      "incomplete_value": true,
      "site": "00535490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535484",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535490",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535484",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535490",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535430.md#insn-00535444) · [`0053545c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535430.md#insn-0053545c) · [`00535464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535430.md#insn-00535464)
- 新版 [`00535484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-00535484) · [`0053549c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-0053549c) · [`005354a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-005354a4)

~~~diff
- 00535444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535444 bytes 08e946f9
+ 00535484 bytes 085147f9
- 0053545c ["INT_ADD", "register:40f0:8", ["const:53545c:8", "const:4:8"]]
- 0053545c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053549c ["INT_ADD", "register:40f0:8", ["const:53549c:8", "const:4:8"]]
+ 0053549c ["CALL", null, ["callee:00c57f80:8"]]
- 0053545c bytes 958a1c94
+ 0053549c bytes b98a1c94
- 00535464 ["INT_ADD", "register:40f0:8", ["const:535464:8", "const:4:8"]]
- 00535464 ["CALL", null, ["callee:00c583b0:8"]]
+ 005354a4 ["INT_ADD", "register:40f0:8", ["const:5354a4:8", "const:4:8"]]
+ 005354a4 ["CALL", null, ["callee:00c583b0:8"]]
- 00535464 bytes 9f8b1c94
+ 005354a4 bytes c38b1c94
~~~


<a id="compare-07bbf653696707c43a235099bb40e672"></a>

### [`00535478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535478.md) → [`005354b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md) FUN_005354b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005354d4",
      "incomplete_value": true,
      "site": "005354d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005354cc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005354d8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005354cc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005354d8",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535478.md#insn-0053548c) · [`005354a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535478.md#insn-005354a4) · [`005354ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535478.md#insn-005354ac)
- 新版 [`005354cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354cc) · [`005354e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354e4) · [`005354ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354ec)

~~~diff
- 0053548c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0053548c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005354cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005354cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053548c bytes 08e946f9
+ 005354cc bytes 085147f9
- 005354a4 ["INT_ADD", "register:40f0:8", ["const:5354a4:8", "const:4:8"]]
- 005354a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005354e4 ["INT_ADD", "register:40f0:8", ["const:5354e4:8", "const:4:8"]]
+ 005354e4 ["CALL", null, ["callee:00c57f80:8"]]
- 005354a4 bytes 838a1c94
+ 005354e4 bytes a78a1c94
- 005354ac ["INT_ADD", "register:40f0:8", ["const:5354ac:8", "const:4:8"]]
- 005354ac ["CALL", null, ["callee:00c583b0:8"]]
+ 005354ec ["INT_ADD", "register:40f0:8", ["const:5354ec:8", "const:4:8"]]
+ 005354ec ["CALL", null, ["callee:00c583b0:8"]]
- 005354ac bytes 8d8b1c94
+ 005354ec bytes b18b1c94
~~~


<a id="compare-91a35cc3dfb0c80fe4f4b7c67f8db83b"></a>

### [`005354c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005354c0.md) → [`00535500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md) FUN_00535500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "0053551c",
      "incomplete_value": true,
      "site": "00535520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535514",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535520",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535514",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535520",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005354d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005354c0.md#insn-005354d4) · [`005354ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005354c0.md#insn-005354ec) · [`005354f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005354c0.md#insn-005354f4)
- 新版 [`00535514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-00535514) · [`0053552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-0053552c) · [`00535534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-00535534)

~~~diff
- 005354d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005354d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005354d4 bytes 08e946f9
+ 00535514 bytes 085147f9
- 005354ec ["INT_ADD", "register:40f0:8", ["const:5354ec:8", "const:4:8"]]
- 005354ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0053552c ["INT_ADD", "register:40f0:8", ["const:53552c:8", "const:4:8"]]
+ 0053552c ["CALL", null, ["callee:00c57f80:8"]]
- 005354ec bytes 718a1c94
+ 0053552c bytes 958a1c94
- 005354f4 ["INT_ADD", "register:40f0:8", ["const:5354f4:8", "const:4:8"]]
- 005354f4 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535534 ["INT_ADD", "register:40f0:8", ["const:535534:8", "const:4:8"]]
+ 00535534 ["CALL", null, ["callee:00c583b0:8"]]
- 005354f4 bytes 7b8b1c94
+ 00535534 bytes 9f8b1c94
~~~


<a id="compare-7b231220bdf51973e640183f363208b4"></a>

### [`00535508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535508.md) → [`00535548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md) FUN_00535548

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535564",
      "incomplete_value": true,
      "site": "00535568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053555c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535568",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053555c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535568",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053551c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535508.md#insn-0053551c) · [`00535534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535508.md#insn-00535534) · [`0053553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535508.md#insn-0053553c)
- 新版 [`0053555c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-0053555c) · [`00535574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-00535574) · [`0053557c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-0053557c)

~~~diff
- 0053551c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0053551c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053555c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053555c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053551c bytes 08e946f9
+ 0053555c bytes 085147f9
- 00535534 ["INT_ADD", "register:40f0:8", ["const:535534:8", "const:4:8"]]
- 00535534 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535574 ["INT_ADD", "register:40f0:8", ["const:535574:8", "const:4:8"]]
+ 00535574 ["CALL", null, ["callee:00c57f80:8"]]
- 00535534 bytes 5f8a1c94
+ 00535574 bytes 838a1c94
- 0053553c ["INT_ADD", "register:40f0:8", ["const:53553c:8", "const:4:8"]]
- 0053553c ["CALL", null, ["callee:00c583b0:8"]]
+ 0053557c ["INT_ADD", "register:40f0:8", ["const:53557c:8", "const:4:8"]]
+ 0053557c ["CALL", null, ["callee:00c583b0:8"]]
- 0053553c bytes 698b1c94
+ 0053557c bytes 8d8b1c94
~~~


<a id="compare-27d577e68072c6a8ef4c5e1468455ce1"></a>

### [`00535550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535550.md) → [`00535590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md) FUN_00535590

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005355ac",
      "incomplete_value": true,
      "site": "005355b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005355a4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005355b0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005355a4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005355b0",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535550.md#insn-00535564) · [`0053557c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535550.md#insn-0053557c) · [`00535584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535550.md#insn-00535584)
- 新版 [`005355a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-005355a4) · [`005355bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-005355bc) · [`005355c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-005355c4)

~~~diff
- 00535564 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005355a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535564 bytes 08e946f9
+ 005355a4 bytes 085147f9
- 0053557c ["INT_ADD", "register:40f0:8", ["const:53557c:8", "const:4:8"]]
- 0053557c ["CALL", null, ["callee:00c57f80:8"]]
+ 005355bc ["INT_ADD", "register:40f0:8", ["const:5355bc:8", "const:4:8"]]
+ 005355bc ["CALL", null, ["callee:00c57f80:8"]]
- 0053557c bytes 4d8a1c94
+ 005355bc bytes 718a1c94
- 00535584 ["INT_ADD", "register:40f0:8", ["const:535584:8", "const:4:8"]]
- 00535584 ["CALL", null, ["callee:00c583b0:8"]]
+ 005355c4 ["INT_ADD", "register:40f0:8", ["const:5355c4:8", "const:4:8"]]
+ 005355c4 ["CALL", null, ["callee:00c583b0:8"]]
- 00535584 bytes 578b1c94
+ 005355c4 bytes 7b8b1c94
~~~


<a id="compare-81acb0a845f4f57c28ee3ebfcdd0bd4b"></a>

### [`00535598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535598.md) → [`005355d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md) FUN_005355d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005355f4",
      "incomplete_value": true,
      "site": "005355f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005355ec",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005355f8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005355ec",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005355f8",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005355ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535598.md#insn-005355ac) · [`005355c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535598.md#insn-005355c4) · [`005355cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535598.md#insn-005355cc)
- 新版 [`005355ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-005355ec) · [`00535604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-00535604) · [`0053560c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-0053560c)

~~~diff
- 005355ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005355ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005355ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355ac bytes 08e946f9
+ 005355ec bytes 085147f9
- 005355c4 ["INT_ADD", "register:40f0:8", ["const:5355c4:8", "const:4:8"]]
- 005355c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535604 ["INT_ADD", "register:40f0:8", ["const:535604:8", "const:4:8"]]
+ 00535604 ["CALL", null, ["callee:00c57f80:8"]]
- 005355c4 bytes 3b8a1c94
+ 00535604 bytes 5f8a1c94
- 005355cc ["INT_ADD", "register:40f0:8", ["const:5355cc:8", "const:4:8"]]
- 005355cc ["CALL", null, ["callee:00c583b0:8"]]
+ 0053560c ["INT_ADD", "register:40f0:8", ["const:53560c:8", "const:4:8"]]
+ 0053560c ["CALL", null, ["callee:00c583b0:8"]]
- 005355cc bytes 458b1c94
+ 0053560c bytes 698b1c94
~~~


<a id="compare-215059fae3ff16ebf28189539e218039"></a>

### [`005355e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005355e0.md) → [`00535620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md) FUN_00535620

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "0053563c",
      "incomplete_value": true,
      "site": "00535640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535634",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535640",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535634",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535640",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005355f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005355e0.md#insn-005355f4) · [`0053560c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005355e0.md#insn-0053560c) · [`00535614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005355e0.md#insn-00535614)
- 新版 [`00535634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-00535634) · [`0053564c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-0053564c) · [`00535654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-00535654)

~~~diff
- 005355f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005355f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535634 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355f4 bytes 08e946f9
+ 00535634 bytes 085147f9
- 0053560c ["INT_ADD", "register:40f0:8", ["const:53560c:8", "const:4:8"]]
- 0053560c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053564c ["INT_ADD", "register:40f0:8", ["const:53564c:8", "const:4:8"]]
+ 0053564c ["CALL", null, ["callee:00c57f80:8"]]
- 0053560c bytes 298a1c94
+ 0053564c bytes 4d8a1c94
- 00535614 ["INT_ADD", "register:40f0:8", ["const:535614:8", "const:4:8"]]
- 00535614 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535654 ["INT_ADD", "register:40f0:8", ["const:535654:8", "const:4:8"]]
+ 00535654 ["CALL", null, ["callee:00c583b0:8"]]
- 00535614 bytes 338b1c94
+ 00535654 bytes 578b1c94
~~~


<a id="compare-b0aa7bfdb785f9bb0fada3648e25b64e"></a>

### [`00535628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535628.md) → [`00535668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md) FUN_00535668

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535684",
      "incomplete_value": true,
      "site": "00535688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053567c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535688",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053567c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535688",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053563c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535628.md#insn-0053563c) · [`00535654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535628.md#insn-00535654) · [`0053565c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535628.md#insn-0053565c)
- 新版 [`0053567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-0053567c) · [`00535694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-00535694) · [`0053569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-0053569c)

~~~diff
- 0053563c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0053563c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053567c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053567c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053563c bytes 08e946f9
+ 0053567c bytes 085147f9
- 00535654 ["INT_ADD", "register:40f0:8", ["const:535654:8", "const:4:8"]]
- 00535654 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535694 ["INT_ADD", "register:40f0:8", ["const:535694:8", "const:4:8"]]
+ 00535694 ["CALL", null, ["callee:00c57f80:8"]]
- 00535654 bytes 178a1c94
+ 00535694 bytes 3b8a1c94
- 0053565c ["INT_ADD", "register:40f0:8", ["const:53565c:8", "const:4:8"]]
- 0053565c ["CALL", null, ["callee:00c583b0:8"]]
+ 0053569c ["INT_ADD", "register:40f0:8", ["const:53569c:8", "const:4:8"]]
+ 0053569c ["CALL", null, ["callee:00c583b0:8"]]
- 0053565c bytes 218b1c94
+ 0053569c bytes 458b1c94
~~~


<a id="compare-75c776cbe2076d88e98826bf691a39de"></a>

### [`00535670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535670.md) → [`005356b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md) FUN_005356b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005356cc",
      "incomplete_value": true,
      "site": "005356d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005356c4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005356d0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005356c4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005356d0",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535670.md#insn-00535684) · [`0053569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535670.md#insn-0053569c) · [`005356a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535670.md#insn-005356a4)
- 新版 [`005356c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356c4) · [`005356dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356dc) · [`005356e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356e4)

~~~diff
- 00535684 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005356c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005356c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535684 bytes 08e946f9
+ 005356c4 bytes 085147f9
- 0053569c ["INT_ADD", "register:40f0:8", ["const:53569c:8", "const:4:8"]]
- 0053569c ["CALL", null, ["callee:00c57f80:8"]]
+ 005356dc ["INT_ADD", "register:40f0:8", ["const:5356dc:8", "const:4:8"]]
+ 005356dc ["CALL", null, ["callee:00c57f80:8"]]
- 0053569c bytes 058a1c94
+ 005356dc bytes 298a1c94
- 005356a4 ["INT_ADD", "register:40f0:8", ["const:5356a4:8", "const:4:8"]]
- 005356a4 ["CALL", null, ["callee:00c583b0:8"]]
+ 005356e4 ["INT_ADD", "register:40f0:8", ["const:5356e4:8", "const:4:8"]]
+ 005356e4 ["CALL", null, ["callee:00c583b0:8"]]
- 005356a4 bytes 0f8b1c94
+ 005356e4 bytes 338b1c94
~~~


<a id="compare-a3dc525588756b589b5f1b5232b9d2a5"></a>

### [`005356b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005356b8.md) → [`005356f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md) FUN_005356f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535714",
      "incomplete_value": true,
      "site": "00535718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053570c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535718",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053570c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535718",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005356cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005356b8.md#insn-005356cc) · [`005356e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005356b8.md#insn-005356e4) · [`005356ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005356b8.md#insn-005356ec)
- 新版 [`0053570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-0053570c) · [`00535724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-00535724) · [`0053572c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-0053572c)

~~~diff
- 005356cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005356cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053570c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053570c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005356cc bytes 08e946f9
+ 0053570c bytes 085147f9
- 005356e4 ["INT_ADD", "register:40f0:8", ["const:5356e4:8", "const:4:8"]]
- 005356e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535724 ["INT_ADD", "register:40f0:8", ["const:535724:8", "const:4:8"]]
+ 00535724 ["CALL", null, ["callee:00c57f80:8"]]
- 005356e4 bytes f3891c94
+ 00535724 bytes 178a1c94
- 005356ec ["INT_ADD", "register:40f0:8", ["const:5356ec:8", "const:4:8"]]
- 005356ec ["CALL", null, ["callee:00c583b0:8"]]
+ 0053572c ["INT_ADD", "register:40f0:8", ["const:53572c:8", "const:4:8"]]
+ 0053572c ["CALL", null, ["callee:00c583b0:8"]]
- 005356ec bytes fd8a1c94
+ 0053572c bytes 218b1c94
~~~


<a id="compare-436e521d8bbef8e87a401962fb63edd6"></a>

### [`00535700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535700.md) → [`00535740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md) FUN_00535740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "0053575c",
      "incomplete_value": true,
      "site": "00535760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535754",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535760",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535754",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535760",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535700.md#insn-00535714) · [`0053572c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535700.md#insn-0053572c) · [`00535734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535700.md#insn-00535734)
- 新版 [`00535754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-00535754) · [`0053576c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-0053576c) · [`00535774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-00535774)

~~~diff
- 00535714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535754 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535754 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535714 bytes 08e946f9
+ 00535754 bytes 085147f9
- 0053572c ["INT_ADD", "register:40f0:8", ["const:53572c:8", "const:4:8"]]
- 0053572c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053576c ["INT_ADD", "register:40f0:8", ["const:53576c:8", "const:4:8"]]
+ 0053576c ["CALL", null, ["callee:00c57f80:8"]]
- 0053572c bytes e1891c94
+ 0053576c bytes 058a1c94
- 00535734 ["INT_ADD", "register:40f0:8", ["const:535734:8", "const:4:8"]]
- 00535734 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535774 ["INT_ADD", "register:40f0:8", ["const:535774:8", "const:4:8"]]
+ 00535774 ["CALL", null, ["callee:00c583b0:8"]]
- 00535734 bytes eb8a1c94
+ 00535774 bytes 0f8b1c94
~~~


<a id="compare-b00b9c0087a39d3420c1b9499998840e"></a>

### [`00535748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535748.md) → [`00535788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md) FUN_00535788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005357a4",
      "incomplete_value": true,
      "site": "005357a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053579c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005357a8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053579c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005357a8",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535748.md#insn-0053575c) · [`00535774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535748.md#insn-00535774) · [`0053577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535748.md#insn-0053577c)
- 新版 [`0053579c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-0053579c) · [`005357b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-005357b4) · [`005357bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-005357bc)

~~~diff
- 0053575c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0053575c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053579c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053579c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053575c bytes 08e946f9
+ 0053579c bytes 085147f9
- 00535774 ["INT_ADD", "register:40f0:8", ["const:535774:8", "const:4:8"]]
- 00535774 ["CALL", null, ["callee:00c57f80:8"]]
+ 005357b4 ["INT_ADD", "register:40f0:8", ["const:5357b4:8", "const:4:8"]]
+ 005357b4 ["CALL", null, ["callee:00c57f80:8"]]
- 00535774 bytes cf891c94
+ 005357b4 bytes f3891c94
- 0053577c ["INT_ADD", "register:40f0:8", ["const:53577c:8", "const:4:8"]]
- 0053577c ["CALL", null, ["callee:00c583b0:8"]]
+ 005357bc ["INT_ADD", "register:40f0:8", ["const:5357bc:8", "const:4:8"]]
+ 005357bc ["CALL", null, ["callee:00c583b0:8"]]
- 0053577c bytes d98a1c94
+ 005357bc bytes fd8a1c94
~~~


<a id="compare-a1bf7fc76e79556166e2654af0cc207e"></a>

### [`00535790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535790.md) → [`005357d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md) FUN_005357d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005357ec",
      "incomplete_value": true,
      "site": "005357f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005357e4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005357f0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005357e4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005357f0",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005357a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535790.md#insn-005357a4) · [`005357bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535790.md#insn-005357bc) · [`005357c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535790.md#insn-005357c4)
- 新版 [`005357e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-005357e4) · [`005357fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-005357fc) · [`00535804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-00535804)

~~~diff
- 005357a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005357a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005357e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005357a4 bytes 08e946f9
+ 005357e4 bytes 085147f9
- 005357bc ["INT_ADD", "register:40f0:8", ["const:5357bc:8", "const:4:8"]]
- 005357bc ["CALL", null, ["callee:00c57f80:8"]]
+ 005357fc ["INT_ADD", "register:40f0:8", ["const:5357fc:8", "const:4:8"]]
+ 005357fc ["CALL", null, ["callee:00c57f80:8"]]
- 005357bc bytes bd891c94
+ 005357fc bytes e1891c94
- 005357c4 ["INT_ADD", "register:40f0:8", ["const:5357c4:8", "const:4:8"]]
- 005357c4 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535804 ["INT_ADD", "register:40f0:8", ["const:535804:8", "const:4:8"]]
+ 00535804 ["CALL", null, ["callee:00c583b0:8"]]
- 005357c4 bytes c78a1c94
+ 00535804 bytes eb8a1c94
~~~


<a id="compare-5c5c31b8fe2857a16c3063f8abb84a5d"></a>

### [`005357d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005357d8.md) → [`00535818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md) FUN_00535818

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535834",
      "incomplete_value": true,
      "site": "00535838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053582c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535838",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053582c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535838",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005357ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005357d8.md#insn-005357ec) · [`00535804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005357d8.md#insn-00535804) · [`0053580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005357d8.md#insn-0053580c)
- 新版 [`0053582c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-0053582c) · [`00535844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-00535844) · [`0053584c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-0053584c)

~~~diff
- 005357ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005357ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053582c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0053582c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005357ec bytes 08e946f9
+ 0053582c bytes 085147f9
- 00535804 ["INT_ADD", "register:40f0:8", ["const:535804:8", "const:4:8"]]
- 00535804 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535844 ["INT_ADD", "register:40f0:8", ["const:535844:8", "const:4:8"]]
+ 00535844 ["CALL", null, ["callee:00c57f80:8"]]
- 00535804 bytes ab891c94
+ 00535844 bytes cf891c94
- 0053580c ["INT_ADD", "register:40f0:8", ["const:53580c:8", "const:4:8"]]
- 0053580c ["CALL", null, ["callee:00c583b0:8"]]
+ 0053584c ["INT_ADD", "register:40f0:8", ["const:53584c:8", "const:4:8"]]
+ 0053584c ["CALL", null, ["callee:00c583b0:8"]]
- 0053580c bytes b58a1c94
+ 0053584c bytes d98a1c94
~~~


<a id="compare-a410e7f5035f04b220379b1c496cf76b"></a>

### [`00535820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535820.md) → [`00535860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md) FUN_00535860

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "0053587c",
      "incomplete_value": true,
      "site": "00535880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535874",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535880",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535874",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535880",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535820.md#insn-00535834) · [`0053584c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535820.md#insn-0053584c) · [`00535854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535820.md#insn-00535854)
- 新版 [`00535874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-00535874) · [`0053588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-0053588c) · [`00535894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-00535894)

~~~diff
- 00535834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535834 bytes 08e946f9
+ 00535874 bytes 085147f9
- 0053584c ["INT_ADD", "register:40f0:8", ["const:53584c:8", "const:4:8"]]
- 0053584c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053588c ["INT_ADD", "register:40f0:8", ["const:53588c:8", "const:4:8"]]
+ 0053588c ["CALL", null, ["callee:00c57f80:8"]]
- 0053584c bytes 99891c94
+ 0053588c bytes bd891c94
- 00535854 ["INT_ADD", "register:40f0:8", ["const:535854:8", "const:4:8"]]
- 00535854 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535894 ["INT_ADD", "register:40f0:8", ["const:535894:8", "const:4:8"]]
+ 00535894 ["CALL", null, ["callee:00c583b0:8"]]
- 00535854 bytes a38a1c94
+ 00535894 bytes c78a1c94
~~~


<a id="compare-43609ddd6eb5588c62e1b36b640adcfa"></a>

### [`005358ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358ac.md) → [`005358ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md) FUN_005358ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535908",
      "incomplete_value": true,
      "site": "0053590c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535900",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "0053590c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535900",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "0053590c",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005358c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358ac.md#insn-005358c0) · [`005358d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358ac.md#insn-005358d8) · [`005358e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358ac.md#insn-005358e0)
- 新版 [`00535900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-00535900) · [`00535918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-00535918) · [`00535920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-00535920)

~~~diff
- 005358c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 005358c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005358c0 bytes 08e946f9
+ 00535900 bytes 085147f9
- 005358d8 ["INT_ADD", "register:40f0:8", ["const:5358d8:8", "const:4:8"]]
- 005358d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535918 ["INT_ADD", "register:40f0:8", ["const:535918:8", "const:4:8"]]
+ 00535918 ["CALL", null, ["callee:00c57f80:8"]]
- 005358d8 bytes 76891c94
+ 00535918 bytes 9a891c94
- 005358e0 ["INT_ADD", "register:40f0:8", ["const:5358e0:8", "const:4:8"]]
- 005358e0 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535920 ["INT_ADD", "register:40f0:8", ["const:535920:8", "const:4:8"]]
+ 00535920 ["CALL", null, ["callee:00c583b0:8"]]
- 005358e0 bytes 808a1c94
+ 00535920 bytes a48a1c94
~~~


<a id="compare-b9fbdddb69ddbad081e8838e1a89cf95"></a>

### [`005358f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358f4.md) → [`00535934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md) FUN_00535934

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535950",
      "incomplete_value": true,
      "site": "00535954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535948",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535954",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535948",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535954",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358f4.md#insn-00535908) · [`00535920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358f4.md#insn-00535920) · [`00535928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/005358f4.md#insn-00535928)
- 新版 [`00535948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535948) · [`00535960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535960) · [`00535968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535968)

~~~diff
- 00535908 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535908 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535908 bytes 08e946f9
+ 00535948 bytes 085147f9
- 00535920 ["INT_ADD", "register:40f0:8", ["const:535920:8", "const:4:8"]]
- 00535920 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535960 ["INT_ADD", "register:40f0:8", ["const:535960:8", "const:4:8"]]
+ 00535960 ["CALL", null, ["callee:00c57f80:8"]]
- 00535920 bytes 64891c94
+ 00535960 bytes 88891c94
- 00535928 ["INT_ADD", "register:40f0:8", ["const:535928:8", "const:4:8"]]
- 00535928 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535968 ["INT_ADD", "register:40f0:8", ["const:535968:8", "const:4:8"]]
+ 00535968 ["CALL", null, ["callee:00c583b0:8"]]
- 00535928 bytes 6e8a1c94
+ 00535968 bytes 928a1c94
~~~


<a id="compare-1177deaba5562d1e42f13fb73ed7f720"></a>

### [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) → [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) FUN_00535bac

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 35件 [`004a21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) [`004a502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md) [`004a5ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md) [`004a762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md) [`004a7c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 35件 [`004a21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a21e8.md) [`004a506c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a506c.md) [`004a5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5d0c.md) [`004a766c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a766c.md) [`004a7c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00535bb8",
      "incomplete_value": false,
      "site": "00535bbc",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00535bb8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00535bb8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md#insn-00535b7c) · [`00535b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md#insn-00535b78)
- 新版 [`00535bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md#insn-00535bbc) · [`00535bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md#insn-00535bb8)

~~~diff
- 00535b7c ["INT_ADD", "register:40f0:8", ["const:535b7c:8", "const:4:8"]]
- 00535b7c ["CALL", null, ["callee:0043b7b8:8"]]
+ 00535bbc ["INT_ADD", "register:40f0:8", ["const:535bbc:8", "const:4:8"]]
+ 00535bbc ["CALL", null, ["callee:0043b7b8:8"]]
- 00535b7c bytes ff16fc97
+ 00535bbc bytes ff16fc97
- 00535b78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00535b78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535b78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535b78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535bb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00535bb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535bb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535bb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535b78 bytes 00303d91
+ 00535bb8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aed4eca869f494b30cb6bf5bd139856"></a>

### [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) → [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) FUN_00535bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`004a6efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6efc.md) [`004a8e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md) [`004c24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 32件 [`004a55dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`004a6f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6f3c.md) [`004a8e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8e6c.md) [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "00535c28",
      "incomplete_value": true,
      "site": "00535c28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535c64",
      "incomplete_value": true,
      "site": "00535c64",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00535c18",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00535c54",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00535c18",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00535c54",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md#insn-00535be8) · [`00535c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md#insn-00535c24) · [`00535bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md#insn-00535bd8)
- 新版 [`00535c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535c28) · [`00535c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535c64) · [`00535c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535c18)

~~~diff
- 00535be8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535be8 ["INT_ADD", "register:40f0:8", ["const:535be8:8", "const:4:8"]]
- 00535be8 ["CALLIND", null, ["register:0:8"]]
+ 00535c28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535c28 ["INT_ADD", "register:40f0:8", ["const:535c28:8", "const:4:8"]]
+ 00535c28 ["CALLIND", null, ["register:0:8"]]
- 00535be8 bytes 20013fd6
+ 00535c28 bytes 20013fd6
- 00535c24 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535c24 ["INT_ADD", "register:40f0:8", ["const:535c24:8", "const:4:8"]]
- 00535c24 ["CALLIND", null, ["register:0:8"]]
+ 00535c64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535c64 ["INT_ADD", "register:40f0:8", ["const:535c64:8", "const:4:8"]]
+ 00535c64 ["CALLIND", null, ["register:0:8"]]
- 00535c24 bytes 20013fd6
+ 00535c64 bytes 20013fd6
- 00535bd8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00535bd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535c18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00535c18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00535bd8 bytes a99e43f9
+ 00535c18 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-298517309b87643c94955ab9f29f7b28"></a>

### [`00535c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535c5c.md) → [`00535c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md) FUN_00535c9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535cb8",
      "incomplete_value": true,
      "site": "00535cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535cb0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535cbc",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535cb0",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535cbc",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535c5c.md#insn-00535c70) · [`00535c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535c5c.md#insn-00535c88) · [`00535c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535c5c.md#insn-00535c90)
- 新版 [`00535cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535cb0) · [`00535cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535cc8) · [`00535cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535cd0)

~~~diff
- 00535c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535c70 bytes 08e946f9
+ 00535cb0 bytes 085147f9
- 00535c88 ["INT_ADD", "register:40f0:8", ["const:535c88:8", "const:4:8"]]
- 00535c88 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535cc8 ["INT_ADD", "register:40f0:8", ["const:535cc8:8", "const:4:8"]]
+ 00535cc8 ["CALL", null, ["callee:00c57f80:8"]]
- 00535c88 bytes 8a881c94
+ 00535cc8 bytes ae881c94
- 00535c90 ["INT_ADD", "register:40f0:8", ["const:535c90:8", "const:4:8"]]
- 00535c90 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535cd0 ["INT_ADD", "register:40f0:8", ["const:535cd0:8", "const:4:8"]]
+ 00535cd0 ["CALL", null, ["callee:00c583b0:8"]]
- 00535c90 bytes 94891c94
+ 00535cd0 bytes b8891c94
~~~


<a id="compare-530b93b79ff12c0899c5dedc263026c2"></a>

### [`00535ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ca4.md) → [`00535ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md) FUN_00535ce4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

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
      "definition_site": "00535da4",
      "incomplete_value": true,
      "site": "00535da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00535df0",
      "incomplete_value": false,
      "site": "00535df4",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535d04",
      "incomplete_value": false,
      "site": "00535d18",
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
            "const:28c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00535d04",
      "PARAM",
      [
        "storage",
        "002c124c",
        null,
        "string"
      ]
    ],
    [
      "00535d20",
      "PARAM",
      [
        "storage",
        "002b09c7",
        null,
        null
      ]
    ],
    [
      "00535d90",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00535d04",
      "PARAM",
      [
        "storage",
        "002c128c",
        null,
        "string"
      ]
    ],
    [
      "00535d20",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ],
    [
      "00535d90",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ca4.md#insn-00535cd8) · [`00535ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ca4.md#insn-00535ce8) · [`00535cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ca4.md#insn-00535cc4)
- 新版 [`00535d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d18) · [`00535d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d28) · [`00535d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d04)

~~~diff
- 00535cd8 ["INT_ADD", "register:40f0:8", ["const:535cd8:8", "const:4:8"]]
- 00535cd8 ["CALL", null, ["callee:00c58180:8"]]
+ 00535d18 ["INT_ADD", "register:40f0:8", ["const:535d18:8", "const:4:8"]]
+ 00535d18 ["CALL", null, ["callee:00c58180:8"]]
- 00535cd8 bytes f6881c94
+ 00535d18 bytes 1a891c94
- 00535ce8 ["INT_ADD", "register:40f0:8", ["const:535ce8:8", "const:4:8"]]
- 00535ce8 ["CALL", null, ["callee:00c58040:8"]]
+ 00535d28 ["INT_ADD", "register:40f0:8", ["const:535d28:8", "const:4:8"]]
+ 00535d28 ["CALL", null, ["callee:00c58040:8"]]
- 00535ce8 bytes a2881c94
+ 00535d28 bytes c6881c94
- 00535cc4 ["COPY", "tmp:0:8", ["const:24c:8"]]
- 00535cc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535cc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535cc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535d04 ["COPY", "tmp:0:8", ["const:28c:8"]]
+ 00535d04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535d04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535d04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535cc4 bytes 00300991
+ 00535d04 bytes 00300a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09c4e38f9524a57c7c52d0765005ff1"></a>

### [`00535eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535eac.md) → [`00535eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md) FUN_00535eec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535f08",
      "incomplete_value": true,
      "site": "00535f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535f00",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f0c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535f00",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f0c",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535eac.md#insn-00535ec0) · [`00535ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535eac.md#insn-00535ed8) · [`00535ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535eac.md#insn-00535ee0)
- 新版 [`00535f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535f00) · [`00535f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535f18) · [`00535f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535f20)

~~~diff
- 00535ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535f00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535f00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535ec0 bytes 08e946f9
+ 00535f00 bytes 085147f9
- 00535ed8 ["INT_ADD", "register:40f0:8", ["const:535ed8:8", "const:4:8"]]
- 00535ed8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535f18 ["INT_ADD", "register:40f0:8", ["const:535f18:8", "const:4:8"]]
+ 00535f18 ["CALL", null, ["callee:00c57f80:8"]]
- 00535ed8 bytes f6871c94
+ 00535f18 bytes 1a881c94
- 00535ee0 ["INT_ADD", "register:40f0:8", ["const:535ee0:8", "const:4:8"]]
- 00535ee0 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535f20 ["INT_ADD", "register:40f0:8", ["const:535f20:8", "const:4:8"]]
+ 00535f20 ["CALL", null, ["callee:00c583b0:8"]]
- 00535ee0 bytes 00891c94
+ 00535f20 bytes 24891c94
~~~


<a id="compare-fde72a3fb6b68aac534bd7f587ba7ff4"></a>

### [`00535ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ef4.md) → [`00535f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md) FUN_00535f34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00535f50",
      "incomplete_value": true,
      "site": "00535f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00535f48",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f54",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00535f48",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535f54",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ef4.md#insn-00535f08) · [`00535f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ef4.md#insn-00535f20) · [`00535f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535ef4.md#insn-00535f28)
- 新版 [`00535f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f48) · [`00535f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f60) · [`00535f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f68)

~~~diff
- 00535f08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00535f08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00535f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535f08 bytes 08e946f9
+ 00535f48 bytes 085147f9
- 00535f20 ["INT_ADD", "register:40f0:8", ["const:535f20:8", "const:4:8"]]
- 00535f20 ["CALL", null, ["callee:00c57f80:8"]]
+ 00535f60 ["INT_ADD", "register:40f0:8", ["const:535f60:8", "const:4:8"]]
+ 00535f60 ["CALL", null, ["callee:00c57f80:8"]]
- 00535f20 bytes e4871c94
+ 00535f60 bytes 08881c94
- 00535f28 ["INT_ADD", "register:40f0:8", ["const:535f28:8", "const:4:8"]]
- 00535f28 ["CALL", null, ["callee:00c583b0:8"]]
+ 00535f68 ["INT_ADD", "register:40f0:8", ["const:535f68:8", "const:4:8"]]
+ 00535f68 ["CALL", null, ["callee:00c583b0:8"]]
- 00535f28 bytes ee881c94
+ 00535f68 bytes 12891c94
~~~


<a id="compare-66280419484f03c3c21cd6217cb2dd5e"></a>

### [`00535f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md) → [`00535fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md) FUN_00535fa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004f8e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md) [`004f8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004f8e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8e70.md) [`004f8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8fac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

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
      "definition_site": "00535fcc",
      "incomplete_value": false,
      "site": "00535fdc",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535ff4",
      "incomplete_value": false,
      "site": "00535ff8",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536008",
      "incomplete_value": false,
      "site": "0053601c",
      "value": [
        "leaf",
        "const:4f8fac:8"
      ]
    },
    "old": {
      "definition_site": "00535fc8",
      "incomplete_value": false,
      "site": "00535fdc",
      "value": [
        "leaf",
        "const:4f8f6c:8"
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
      "00535fbc",
      "READ",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ],
    [
      "00535fcc",
      "PARAM",
      [
        "storage",
        "00ca5280",
        null,
        "undefined8"
      ]
    ],
    [
      "00535ff4",
      "PARAM",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00535fbc",
      "READ",
      [
        "storage",
        "00ca5390",
        null,
        "undefined1"
      ]
    ],
    [
      "00535fcc",
      "PARAM",
      [
        "storage",
        "00ca5380",
        null,
        "undefined8"
      ]
    ],
    [
      "00535ff4",
      "PARAM",
      [
        "storage",
        "00ca5390",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md#insn-00535f9c) · [`00535fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md#insn-00535fb8) · [`00535fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md#insn-00535fdc)
- 新版 [`00535fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-00535fdc) · [`00535ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-00535ff8) · [`0053601c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-0053601c)

~~~diff
- 00535f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00535f9c ["INT_ADD", "register:40f0:8", ["const:535f9c:8", "const:4:8"]]
- 00535f9c ["CALLIND", null, ["register:0:8"]]
+ 00535fdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535fdc ["INT_ADD", "register:40f0:8", ["const:535fdc:8", "const:4:8"]]
+ 00535fdc ["CALLIND", null, ["register:0:8"]]
- 00535f9c bytes 00013fd6
+ 00535fdc bytes 00013fd6
- 00535fb8 ["INT_ADD", "register:40f0:8", ["const:535fb8:8", "const:4:8"]]
- 00535fb8 ["CALL", null, ["callee:00c57f20:8"]]
+ 00535ff8 ["INT_ADD", "register:40f0:8", ["const:535ff8:8", "const:4:8"]]
+ 00535ff8 ["CALL", null, ["callee:00c57f20:8"]]
- 00535fb8 bytes a6871c94
+ 00535ff8 bytes ca871c94
- 00535fdc ["INT_ADD", "register:40f0:8", ["const:535fdc:8", "const:4:8"]]
- 00535fdc ["CALL", null, ["callee:00c57f00:8"]]
+ 0053601c ["INT_ADD", "register:40f0:8", ["const:53601c:8", "const:4:8"]]
+ 0053601c ["CALL", null, ["callee:00c57f00:8"]]
- 00535fdc bytes 95871c94
+ 0053601c bytes b9871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b70da344c1e8e0f3e6f04b2ea203bd0"></a>

### [`00536010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md) → [`00536050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md) FUN_00536050

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004c5db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5db4.md) [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`004e34c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e34c4.md) · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d80.md)
- 新版 呼出元 3件 [`004c5df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5df4.md) [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`004e3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3504.md) · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e50.md)

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
      "definition_site": "00536148",
      "incomplete_value": true,
      "site": "00536154",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536144",
      "incomplete_value": false,
      "site": "00536154",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00536104",
      "incomplete_value": false,
      "site": "00536114",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00536144",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00536148",
      "READ",
      [
        "storage",
        "00c9ae38",
        null,
        "pointer"
      ]
    ],
    [
      "00536148",
      "PARAM",
      [
        "storage",
        "00c66e28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00536144",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00536148",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "00536148",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005360d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md#insn-005360d4) · [`00536114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md#insn-00536114) · [`00536048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md#insn-00536048)
- 新版 [`00536114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-00536114) · [`00536154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-00536154) · [`00536088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-00536088)

~~~diff
- 005360d4 ["COPY", "register:0:8", ["register:4050:8"]]
- 005360d4 ["INT_ADD", "register:40f0:8", ["const:5360d4:8", "const:4:8"]]
- 005360d4 ["CALLIND", null, ["register:0:8"]]
+ 00536114 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00536114 ["INT_ADD", "register:40f0:8", ["const:536114:8", "const:4:8"]]
+ 00536114 ["CALLIND", null, ["register:0:8"]]
- 005360d4 bytes 40013fd6
+ 00536114 bytes 40013fd6
- 00536114 ["INT_ADD", "register:40f0:8", ["const:536114:8", "const:4:8"]]
- 00536114 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00536154 ["INT_ADD", "register:40f0:8", ["const:536154:8", "const:4:8"]]
+ 00536154 ["CALL", null, ["callee:00c57fe0:8"]]
- 00536114 bytes 7f871c94
+ 00536154 bytes a3871c94
- 00536048 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536048 ["INT_ADD", "register:40f0:8", ["const:536048:8", "const:4:8"]]
- 00536048 ["CALLIND", null, ["register:0:8"]]
+ 00536088 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536088 ["INT_ADD", "register:40f0:8", ["const:536088:8", "const:4:8"]]
+ 00536088 ["CALLIND", null, ["register:0:8"]]
- 00536048 bytes 20013fd6
+ 00536088 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1651fc029c41e3864aeb146fbe045a16"></a>

### [`00536164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536164.md) → [`005361a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md) FUN_005361a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "005361c0",
      "incomplete_value": true,
      "site": "005361c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "005361b8",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "005361c4",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005361b8",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005361c4",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536164.md#insn-00536178) · [`00536190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536164.md#insn-00536190) · [`00536198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536164.md#insn-00536198)
- 新版 [`005361b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361b8) · [`005361d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361d0) · [`005361d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361d8)

~~~diff
- 00536178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00536178 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005361b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 005361b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00536178 bytes 08e946f9
+ 005361b8 bytes 085147f9
- 00536190 ["INT_ADD", "register:40f0:8", ["const:536190:8", "const:4:8"]]
- 00536190 ["CALL", null, ["callee:00c57f80:8"]]
+ 005361d0 ["INT_ADD", "register:40f0:8", ["const:5361d0:8", "const:4:8"]]
+ 005361d0 ["CALL", null, ["callee:00c57f80:8"]]
- 00536190 bytes 48871c94
+ 005361d0 bytes 6c871c94
- 00536198 ["INT_ADD", "register:40f0:8", ["const:536198:8", "const:4:8"]]
- 00536198 ["CALL", null, ["callee:00c583b0:8"]]
+ 005361d8 ["INT_ADD", "register:40f0:8", ["const:5361d8:8", "const:4:8"]]
+ 005361d8 ["CALL", null, ["callee:00c583b0:8"]]
- 00536198 bytes 52881c94
+ 005361d8 bytes 76881c94
~~~


<a id="compare-3937dd2c034bd0285c10e62dc69bac1c"></a>

### [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) → [`005361ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md) FUN_005361ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ce994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce994.md) [`004f5a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md) [`004f69c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md) [`004f6a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md) · 呼出先 8件 [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 4件 [`004ce9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce9d4.md) [`004f5aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5aa4.md) [`004f6a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f6/004f6a04.md) [`004f6ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f6/004f6ab8.md) · 呼出先 8件 [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "005362e0",
      "incomplete_value": true,
      "site": "005362e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005362e4",
      "incomplete_value": true,
      "site": "005362e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "005362e0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "005362e0",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005362e4",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005362e0",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "005362e0",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005362e4",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005362a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md#insn-005362a8) · [`005361fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md#insn-005361fc) · [`00536228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md#insn-00536228)
- 新版 [`005362e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-005362e8) · [`0053623c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-0053623c) · [`00536268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-00536268)

~~~diff
- 005362a8 ["INT_ADD", "register:40f0:8", ["const:5362a8:8", "const:4:8"]]
- 005362a8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005362e8 ["INT_ADD", "register:40f0:8", ["const:5362e8:8", "const:4:8"]]
+ 005362e8 ["CALL", null, ["callee:00c57fe0:8"]]
- 005362a8 bytes 1a871c94
+ 005362e8 bytes 3e871c94
- 005361fc ["INT_ADD", "register:40f0:8", ["const:5361fc:8", "const:4:8"]]
- 005361fc ["CALL", null, ["callee:00c58b00:8"]]
+ 0053623c ["INT_ADD", "register:40f0:8", ["const:53623c:8", "const:4:8"]]
+ 0053623c ["CALL", null, ["callee:00c58b00:8"]]
- 005361fc bytes 0d8a1c94
+ 0053623c bytes 318a1c94
- 00536228 ["INT_ADD", "register:40f0:8", ["const:536228:8", "const:4:8"]]
- 00536228 ["CALL", null, ["callee:00c580d0:8"]]
+ 00536268 ["INT_ADD", "register:40f0:8", ["const:536268:8", "const:4:8"]]
+ 00536268 ["CALL", null, ["callee:00c580d0:8"]]
- 00536228 bytes 76871c94
+ 00536268 bytes 9a871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-606dcef9d602605f2ec84bfe506cff1f"></a>

### [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) → [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) FUN_00536374

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 4件 [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`005361ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00536380",
      "incomplete_value": false,
      "site": "00536384",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00536380",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00536380",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md#insn-00536344) · [`00536340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md#insn-00536340)
- 新版 [`00536384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md#insn-00536384) · [`00536380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md#insn-00536380)

~~~diff
- 00536344 ["INT_ADD", "register:40f0:8", ["const:536344:8", "const:4:8"]]
- 00536344 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00536384 ["INT_ADD", "register:40f0:8", ["const:536384:8", "const:4:8"]]
+ 00536384 ["CALL", null, ["callee:0043b7b8:8"]]
- 00536344 bytes 0d15fc97
+ 00536384 bytes 0d15fc97
- 00536340 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00536340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00536340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00536340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00536380 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00536380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00536380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00536380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00536340 bytes 00303d91
+ 00536380 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96414b110f44acf644811151efcf67e6"></a>

### [`005366b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md) → [`005366f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md) FUN_005366f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00549acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549acc.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "0053673c",
      "incomplete_value": true,
      "site": "0053673c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053673c",
      "incomplete_value": true,
      "site": "0053673c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0053671c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00536728",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0053673c",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0053671c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00536728",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0053673c",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005366dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md#insn-005366dc) · [`005366e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md#insn-005366e4) · [`005366e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md#insn-005366e8)
- 新版 [`0053671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md#insn-0053671c) · [`00536728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md#insn-00536728)

~~~diff
- 005366dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
- 005366dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053671c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
+ 0053671c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005366dc bytes 089d46f9
+ 0053671c bytes 080547f9
- 005366e4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005366e4 bytes f30300aa
- 005366e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 005366e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536728 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 00536728 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005366e8 bytes 29a146f9
+ 00536728 bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4472ec5b2403a35e74e02b9a987b65ed"></a>

### [`005367dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005367dc.md) → [`0053681c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md) FUN_0053681c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c59f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a050.md)

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
      "definition_site": "00536868",
      "incomplete_value": true,
      "site": "00536868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:452:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536858",
      "incomplete_value": true,
      "site": "0053686c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536894",
      "incomplete_value": true,
      "site": "005368a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00536850",
      "READ",
      [
        "storage",
        "002b7412",
        null,
        "string"
      ]
    ],
    [
      "00536858",
      "READ",
      [
        "storage",
        "002b7419",
        null,
        "string"
      ]
    ],
    [
      "00536890",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00536850",
      "READ",
      [
        "storage",
        "002b7452",
        null,
        "string"
      ]
    ],
    [
      "00536858",
      "READ",
      [
        "storage",
        "002b7459",
        null,
        "string"
      ]
    ],
    [
      "00536890",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005367dc.md#insn-00536860) · [`00536800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005367dc.md#insn-00536800) · [`0053680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005367dc.md#insn-0053680c)
- 新版 [`005368a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-005368a0) · [`00536840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-00536840) · [`0053684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-0053684c)

~~~diff
- 00536860 ["INT_ADD", "register:40f0:8", ["const:536860:8", "const:4:8"]]
- 00536860 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005368a0 ["INT_ADD", "register:40f0:8", ["const:5368a0:8", "const:4:8"]]
+ 005368a0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00536860 bytes ac851c94
+ 005368a0 bytes d0851c94
- 00536800 ["INT_ADD", "register:40f0:8", ["const:536800:8", "const:4:8"]]
- 00536800 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00536840 ["INT_ADD", "register:40f0:8", ["const:536840:8", "const:4:8"]]
+ 00536840 ["CALL", null, ["callee:00c57fc0:8"]]
- 00536800 bytes bc851c94
+ 00536840 bytes e0851c94
- 0053680c ["COPY", "tmp:0:8", ["const:412:8"]]
- 0053680c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053680c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053680c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053684c ["COPY", "tmp:0:8", ["const:452:8"]]
+ 0053684c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053684c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053684c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053680c bytes 29491091
+ 0053684c bytes 29491191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b498c25a9c702560ffaa4a8b8386fe4a"></a>

### [`00536a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536a28.md) → [`00536a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md) FUN_00536a68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545978.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)
- 新版 呼出元 2件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`005459b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)

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
      "definition_site": "00536acc",
      "incomplete_value": true,
      "site": "00536ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536aec",
      "incomplete_value": true,
      "site": "00536af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536b08",
      "incomplete_value": true,
      "site": "00536b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00536a84",
      "PARAM",
      [
        "storage",
        "002bc723",
        null,
        "string"
      ]
    ],
    [
      "00536a9c",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "00536ab0",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00536a84",
      "PARAM",
      [
        "storage",
        "002bc6cf",
        null,
        "string"
      ]
    ],
    [
      "00536a9c",
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      "00536ab0",
      "PARAM",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536a28.md#insn-00536a54) · [`00536a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536a28.md#insn-00536a68) · [`00536a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536a28.md#insn-00536a70)
- 新版 [`00536a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536a94) · [`00536aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536aa8) · [`00536ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536ab0)

~~~diff
- 00536a54 ["INT_ADD", "register:40f0:8", ["const:536a54:8", "const:4:8"]]
- 00536a54 ["CALL", null, ["callee:00c58180:8"]]
+ 00536a94 ["INT_ADD", "register:40f0:8", ["const:536a94:8", "const:4:8"]]
+ 00536a94 ["CALL", null, ["callee:00c58180:8"]]
- 00536a54 bytes 97851c94
+ 00536a94 bytes bb851c94
- 00536a68 ["INT_ADD", "register:40f0:8", ["const:536a68:8", "const:4:8"]]
- 00536a68 ["CALL", null, ["callee:00c58180:8"]]
+ 00536aa8 ["INT_ADD", "register:40f0:8", ["const:536aa8:8", "const:4:8"]]
+ 00536aa8 ["CALL", null, ["callee:00c58180:8"]]
- 00536a68 bytes 92851c94
+ 00536aa8 bytes b6851c94
- 00536a70 ["COPY", "tmp:0:8", ["const:44e:8"]]
- 00536a70 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00536a70 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00536a70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00536ab0 ["COPY", "tmp:0:8", ["const:3f2:8"]]
+ 00536ab0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00536ab0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00536ab0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00536a70 bytes 21381191
+ 00536ab0 bytes 21c80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331312c548e2392c55c900c7f6f1891d"></a>

### [`00536b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536b38.md) → [`00536b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md) FUN_00536b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a20.md) [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md)
- 新版 呼出元 1件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c58af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58af0.md) [`00c58b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md)

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
      "definition_site": "00536c38",
      "incomplete_value": true,
      "site": "00536c38",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00536c7c",
      "incomplete_value": true,
      "site": "00536c7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00536c28",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00536c6c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00536c28",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00536c6c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536b38.md#insn-00536bb8) · [`00536bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536b38.md#insn-00536bf8) · [`00536c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536b38.md#insn-00536c3c)
- 新版 [`00536bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536bf8) · [`00536c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536c38) · [`00536c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536c7c)

~~~diff
- 00536bb8 ["INT_ADD", "register:40f0:8", ["const:536bb8:8", "const:4:8"]]
- 00536bb8 ["CALL", null, ["callee:00c58af0:8"]]
+ 00536bf8 ["INT_ADD", "register:40f0:8", ["const:536bf8:8", "const:4:8"]]
+ 00536bf8 ["CALL", null, ["callee:00c58af0:8"]]
- 00536bb8 bytes 9a871c94
+ 00536bf8 bytes be871c94
- 00536bf8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536bf8 ["INT_ADD", "register:40f0:8", ["const:536bf8:8", "const:4:8"]]
- 00536bf8 ["CALLIND", null, ["register:0:8"]]
+ 00536c38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536c38 ["INT_ADD", "register:40f0:8", ["const:536c38:8", "const:4:8"]]
+ 00536c38 ["CALLIND", null, ["register:0:8"]]
- 00536bf8 bytes 20013fd6
+ 00536c38 bytes 20013fd6
- 00536c3c ["COPY", "register:0:8", ["register:4048:8"]]
- 00536c3c ["INT_ADD", "register:40f0:8", ["const:536c3c:8", "const:4:8"]]
- 00536c3c ["CALLIND", null, ["register:0:8"]]
+ 00536c7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536c7c ["INT_ADD", "register:40f0:8", ["const:536c7c:8", "const:4:8"]]
+ 00536c7c ["CALLIND", null, ["register:0:8"]]
- 00536c3c bytes 20013fd6
+ 00536c7c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e327d4d7b7b9d100b8e986d7e856b437"></a>

### [`00536cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536cbc.md) → [`00536cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md) FUN_00536cfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)

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
      "definition_site": "00536d18",
      "incomplete_value": true,
      "site": "00536d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00536d10",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00536d1c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00536d10",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00536d1c",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536cbc.md#insn-00536cd0) · [`00536ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536cbc.md#insn-00536ce8) · [`00536cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536cbc.md#insn-00536cf0)
- 新版 [`00536d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d10) · [`00536d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d28) · [`00536d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d30)

~~~diff
- 00536cd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00536cd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536d10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00536d10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00536cd0 bytes 08e946f9
+ 00536d10 bytes 085147f9
- 00536ce8 ["INT_ADD", "register:40f0:8", ["const:536ce8:8", "const:4:8"]]
- 00536ce8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00536d28 ["INT_ADD", "register:40f0:8", ["const:536d28:8", "const:4:8"]]
+ 00536d28 ["CALL", null, ["callee:00c57f80:8"]]
- 00536ce8 bytes 72841c94
+ 00536d28 bytes 96841c94
- 00536cf0 ["INT_ADD", "register:40f0:8", ["const:536cf0:8", "const:4:8"]]
- 00536cf0 ["CALL", null, ["callee:00c583b0:8"]]
+ 00536d30 ["INT_ADD", "register:40f0:8", ["const:536d30:8", "const:4:8"]]
+ 00536d30 ["CALL", null, ["callee:00c583b0:8"]]
- 00536cf0 bytes 7c851c94
+ 00536d30 bytes a0851c94
~~~


<a id="compare-3def075f63b37640d0db007070291598"></a>

### [`00536d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md) → [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) FUN_00536d44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004f15d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f15d4.md) [`0050ef8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md) · 呼出先 8件 [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`004f1614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1614.md) [`0050efcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md) · 呼出先 8件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536e34",
      "incomplete_value": true,
      "site": "00536e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536df4",
      "incomplete_value": true,
      "site": "00536dfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536e38",
      "incomplete_value": true,
      "site": "00536e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536df8",
      "incomplete_value": true,
      "site": "00536dfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00536e34",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00536e34",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00536e38",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00536e34",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00536e34",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00536e38",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md#insn-00536dfc) · [`00536d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md#insn-00536d50) · [`00536d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md#insn-00536d7c)
- 新版 [`00536e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536e3c) · [`00536d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536d90) · [`00536dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536dbc)

~~~diff
- 00536dfc ["INT_ADD", "register:40f0:8", ["const:536dfc:8", "const:4:8"]]
- 00536dfc ["CALL", null, ["callee:00c57fe0:8"]]
+ 00536e3c ["INT_ADD", "register:40f0:8", ["const:536e3c:8", "const:4:8"]]
+ 00536e3c ["CALL", null, ["callee:00c57fe0:8"]]
- 00536dfc bytes 45841c94
+ 00536e3c bytes 69841c94
- 00536d50 ["INT_ADD", "register:40f0:8", ["const:536d50:8", "const:4:8"]]
- 00536d50 ["CALL", null, ["callee:00c58b00:8"]]
+ 00536d90 ["INT_ADD", "register:40f0:8", ["const:536d90:8", "const:4:8"]]
+ 00536d90 ["CALL", null, ["callee:00c58b00:8"]]
- 00536d50 bytes 38871c94
+ 00536d90 bytes 5c871c94
- 00536d7c ["INT_ADD", "register:40f0:8", ["const:536d7c:8", "const:4:8"]]
- 00536d7c ["CALL", null, ["callee:00c58010:8"]]
+ 00536dbc ["INT_ADD", "register:40f0:8", ["const:536dbc:8", "const:4:8"]]
+ 00536dbc ["CALL", null, ["callee:00c58010:8"]]
- 00536d7c bytes 71841c94
+ 00536dbc bytes 95841c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253918c1e5c4473db2ae0bc6164446b7"></a>

### [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) → [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) FUN_00536ec8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00536d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 12件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00536ed4",
      "incomplete_value": false,
      "site": "00536ed8",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536e94",
      "incomplete_value": false,
      "site": "00536e98",
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
      "00536ed4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00536ed4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md#insn-00536e98) · [`00536e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md#insn-00536e94)
- 新版 [`00536ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md#insn-00536ed8) · [`00536ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md#insn-00536ed4)

~~~diff
- 00536e98 ["INT_ADD", "register:40f0:8", ["const:536e98:8", "const:4:8"]]
- 00536e98 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00536ed8 ["INT_ADD", "register:40f0:8", ["const:536ed8:8", "const:4:8"]]
+ 00536ed8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00536e98 bytes 3812fc97
+ 00536ed8 bytes 3812fc97
- 00536e94 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00536e94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00536e94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00536e94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00536ed4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00536ed4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00536ed4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00536ed4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00536e94 bytes 00303d91
+ 00536ed4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1993829bcc833a86b5c75ff6c9c5282a"></a>

### [`00536e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e9c.md) → [`00536edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md) FUN_00536edc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00537084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537084.md) [`00537558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537558.md) · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`005370c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md) [`00537598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md) · 呼出先 9件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536f64",
      "incomplete_value": false,
      "site": "00536f6c",
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
            "const:725:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536f24",
      "incomplete_value": false,
      "site": "00536f2c",
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
            "const:781:8"
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
      "definition_site": "00536f9c",
      "incomplete_value": true,
      "site": "00536fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536f5c",
      "incomplete_value": true,
      "site": "00536f68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "00536f98",
      "incomplete_value": false,
      "site": "00536fa8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00536f58",
      "incomplete_value": false,
      "site": "00536f68",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00536f64",
      "PARAM",
      [
        "storage",
        "002a6781",
        null,
        "string"
      ]
    ],
    [
      "00536f98",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00536f9c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00536f64",
      "PARAM",
      [
        "storage",
        "002a6725",
        null,
        "string"
      ]
    ],
    [
      "00536f98",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00536f9c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e9c.md#insn-00536f2c) · [`00536f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e9c.md#insn-00536f68) · [`00536ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e9c.md#insn-00536ed4)
- 新版 [`00536f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536f6c) · [`00536fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536fa8) · [`00536f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536f14)

~~~diff
- 00536f2c ["INT_ADD", "register:40f0:8", ["const:536f2c:8", "const:4:8"]]
- 00536f2c ["CALL", null, ["callee:0043de18:8"]]
+ 00536f6c ["INT_ADD", "register:40f0:8", ["const:536f6c:8", "const:4:8"]]
+ 00536f6c ["CALL", null, ["callee:0043de18:8"]]
- 00536f2c bytes ab1bfc97
+ 00536f6c bytes ab1bfc97
- 00536f68 ["INT_ADD", "register:40f0:8", ["const:536f68:8", "const:4:8"]]
- 00536f68 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00536fa8 ["INT_ADD", "register:40f0:8", ["const:536fa8:8", "const:4:8"]]
+ 00536fa8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00536f68 bytes ea831c94
+ 00536fa8 bytes 0e841c94
- 00536ed4 ["INT_ADD", "register:40f0:8", ["const:536ed4:8", "const:4:8"]]
- 00536ed4 ["CALL", null, ["callee:00c58bf0:8"]]
+ 00536f14 ["INT_ADD", "register:40f0:8", ["const:536f14:8", "const:4:8"]]
+ 00536f14 ["CALL", null, ["callee:00c58bf0:8"]]
- 00536ed4 bytes 13871c94
+ 00536f14 bytes 37871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

