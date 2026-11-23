# v16.0.0 → v16.0.1 · 最優先の変更候補 (29)

[一覧の目次](README.md)

<a id="compare-d617e7516ffe3c1a618855e5134283c4"></a>

### [`0065f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f03c.md) → [`0065f07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f07c.md) FUN_0065f07c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0065f0a0",
      "incomplete_value": false,
      "site": "0065f0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f060",
      "incomplete_value": false,
      "site": "0065f064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0065f0a4",
      "DATA",
      [
        "storage",
        "00c740c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065f0a4",
      "DATA",
      [
        "storage",
        "00c744c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f03c.md#insn-0065f050) · [`0065f060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f03c.md#insn-0065f060)
- 新版 `0065f090`（命令位置の公開資料なし） · `0065f0a0`（命令位置の公開資料なし）

~~~diff
- 0065f050 ["INT_ADD", "register:40f0:8", ["const:65f050:8", "const:4:8"]]
- 0065f050 ["CALL", null, ["callee:00c57e90:8"]]
+ 0065f090 ["INT_ADD", "register:40f0:8", ["const:65f090:8", "const:4:8"]]
+ 0065f090 ["CALL", null, ["callee:00c57e90:8"]]
- 0065f050 bytes 90e21794
+ 0065f090 bytes 80e31794
- 0065f060 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 0065f060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f0a0 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0065f0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f060 bytes 08210391
+ 0065f0a0 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-069e678811f799452beea7b4f90c5688"></a>

### [`0065f07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f07c.md) → [`0065f0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f0bc.md) FUN_0065f0bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0065f0c0",
      "incomplete_value": false,
      "site": "0065f0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f080",
      "incomplete_value": false,
      "site": "0065f084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0065f0c4",
      "DATA",
      [
        "storage",
        "00c740c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065f0c4",
      "DATA",
      [
        "storage",
        "00c744c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f07c.md#insn-0065f080)
- 新版 `0065f0c0`（命令位置の公開資料なし）

~~~diff
- 0065f080 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 0065f080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f0c0 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0065f0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f080 bytes 08210391
+ 0065f0c0 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a1aae34e090d2e5f87c3cb1873322df"></a>

### [`0065f0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md) → [`0065f11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f11c.md) FUN_0065f11c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0065f0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0a4.md) · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00658448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658448.md)
- 新版 呼出元 1件 [`0065f0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f0e4.md) · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00658488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658488.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 76.40% / 新版 76.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 3件, `store_destination` 14件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065f228",
      "incomplete_value": true,
      "site": "0065f238",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:424:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f1e8",
      "incomplete_value": true,
      "site": "0065f1f8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3e4:8"
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
      "definition_site": "0065f22c",
      "incomplete_value": true,
      "site": "0065f23c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0065f1ec",
      "incomplete_value": true,
      "site": "0065f1fc",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065f230",
      "incomplete_value": true,
      "site": "0065f240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f1f0",
      "incomplete_value": true,
      "site": "0065f200",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:250:8"
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
      "0065f154",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f170",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f1f8",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0065f154",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f170",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f1f8",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[39]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md#insn-0065f114) · [`0065f130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md#insn-0065f130) · [`0065f1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f0dc.md#insn-0065f1c0)
- 新版 `0065f154`（命令位置の公開資料なし） · `0065f170`（命令位置の公開資料なし） · `0065f200`（命令位置の公開資料なし）

~~~diff
- 0065f114 ["INT_ADD", "register:40f0:8", ["const:65f114:8", "const:4:8"]]
- 0065f114 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f154 ["INT_ADD", "register:40f0:8", ["const:65f154:8", "const:4:8"]]
+ 0065f154 ["CALL", null, ["ram:47acf4:8"]]
- 0065f114 bytes e86ef897
+ 0065f154 bytes e86ef897
- 0065f130 ["INT_ADD", "register:40f0:8", ["const:65f130:8", "const:4:8"]]
- 0065f130 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f170 ["INT_ADD", "register:40f0:8", ["const:65f170:8", "const:4:8"]]
+ 0065f170 ["CALL", null, ["ram:47acf4:8"]]
- 0065f130 bytes e16ef897
+ 0065f170 bytes e16ef897
- 0065f1c0 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0065f1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f200 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0065f200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f1c0 bytes 08e12c91
+ 0065f200 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc57aa213f0e991d4a9f6eb032c91ce7"></a>

### [`0065f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f630.md) → [`0065f670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f670.md) FUN_0065f670

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065f600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f600.md) · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md)
- 新版 呼出元 1件 [`0065f640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f640.md) · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

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
      "site": "0065f690",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065f650",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065f6b8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065f678",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0065f690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f6b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0065f690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f6b8",
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

- 旧版 [`0065f650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f630.md#insn-0065f650) · [`0065f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f630.md#insn-0065f678) · [`0065f68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f630.md#insn-0065f68c)
- 新版 `0065f690`（命令位置の公開資料なし） · `0065f6b8`（命令位置の公開資料なし） · `0065f6cc`（命令位置の公開資料なし）

~~~diff
- 0065f650 ["INT_ADD", "register:40f0:8", ["const:65f650:8", "const:4:8"]]
- 0065f650 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f690 ["INT_ADD", "register:40f0:8", ["const:65f690:8", "const:4:8"]]
+ 0065f690 ["CALL", null, ["ram:47acf4:8"]]
- 0065f650 bytes 996df897
+ 0065f690 bytes 996df897
- 0065f678 ["INT_ADD", "register:40f0:8", ["const:65f678:8", "const:4:8"]]
- 0065f678 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f6b8 ["INT_ADD", "register:40f0:8", ["const:65f6b8:8", "const:4:8"]]
+ 0065f6b8 ["CALL", null, ["ram:47acf4:8"]]
- 0065f678 bytes 8f6df897
+ 0065f6b8 bytes 8f6df897
- 0065f68c ["INT_ADD", "register:40f0:8", ["const:65f68c:8", "const:4:8"]]
- 0065f68c ["CALL", null, ["callee:0047cdd4:8"]]
+ 0065f6cc ["INT_ADD", "register:40f0:8", ["const:65f6cc:8", "const:4:8"]]
+ 0065f6cc ["CALL", null, ["callee:0047cdd4:8"]]
- 0065f68c bytes c275f897
+ 0065f6cc bytes c275f897
~~~


<a id="compare-a1ffabb29398ec83decb21cb4369ed3b"></a>

### [`0065f6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f6d8.md) → [`0065f718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f718.md) FUN_0065f718

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0065f73c",
      "incomplete_value": false,
      "site": "0065f740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f6fc",
      "incomplete_value": false,
      "site": "0065f700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "0065f740",
      "DATA",
      [
        "storage",
        "00c741c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065f740",
      "DATA",
      [
        "storage",
        "00c745c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f6d8.md#insn-0065f6ec) · [`0065f6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f6d8.md#insn-0065f6fc)
- 新版 `0065f72c`（命令位置の公開資料なし） · `0065f73c`（命令位置の公開資料なし）

~~~diff
- 0065f6ec ["INT_ADD", "register:40f0:8", ["const:65f6ec:8", "const:4:8"]]
- 0065f6ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0065f72c ["INT_ADD", "register:40f0:8", ["const:65f72c:8", "const:4:8"]]
+ 0065f72c ["CALL", null, ["callee:00c57e90:8"]]
- 0065f6ec bytes e9e01794
+ 0065f72c bytes d9e11794
- 0065f6fc ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 0065f6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f73c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0065f73c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f73c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f73c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f6fc bytes 08210791
+ 0065f73c bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e664765b1e76f42e94f638a987edf4d"></a>

### [`0065f718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f718.md) → [`0065f758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f758.md) FUN_0065f758

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065f75c",
      "incomplete_value": true,
      "site": "0065f760",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f71c",
      "incomplete_value": true,
      "site": "0065f720",
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
            "const:1c8:8"
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
      "0065f760",
      "DATA",
      [
        "storage",
        "00c741c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065f760",
      "DATA",
      [
        "storage",
        "00c745c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f718.md#insn-0065f71c)
- 新版 `0065f75c`（命令位置の公開資料なし）

~~~diff
- 0065f71c ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 0065f71c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f71c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f71c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f75c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0065f75c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f75c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f75c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f71c bytes 08210791
+ 0065f75c bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68d1094947fb1a30c3336fc1f619261"></a>

### [`0065f778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md) → [`0065f7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f7b8.md) FUN_0065f7b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0065f740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f740.md) · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00658448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658448.md)
- 新版 呼出元 1件 [`0065f780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f780.md) · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00658488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658488.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 77.61% / 新版 77.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 3件, `store_destination` 14件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065f8cc",
      "incomplete_value": true,
      "site": "0065f8dc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f88c",
      "incomplete_value": true,
      "site": "0065f89c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:250:8"
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
      "definition_site": "0065f93c",
      "incomplete_value": true,
      "site": "0065f94c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f8fc",
      "incomplete_value": true,
      "site": "0065f90c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e82:8"
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
      "definition_site": "0065f940",
      "incomplete_value": true,
      "site": "0065f950",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0065f900",
      "incomplete_value": true,
      "site": "0065f910",
      "value": [
        "LOAD",
        "16",
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
      "0065f7f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f80c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f894",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0065f7f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f80c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f894",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[39]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065f7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md#insn-0065f7b0) · [`0065f7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md#insn-0065f7cc) · [`0065f85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f778.md#insn-0065f85c)
- 新版 `0065f7f0`（命令位置の公開資料なし） · `0065f80c`（命令位置の公開資料なし） · `0065f89c`（命令位置の公開資料なし）

~~~diff
- 0065f7b0 ["INT_ADD", "register:40f0:8", ["const:65f7b0:8", "const:4:8"]]
- 0065f7b0 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f7f0 ["INT_ADD", "register:40f0:8", ["const:65f7f0:8", "const:4:8"]]
+ 0065f7f0 ["CALL", null, ["ram:47acf4:8"]]
- 0065f7b0 bytes 416df897
+ 0065f7f0 bytes 416df897
- 0065f7cc ["INT_ADD", "register:40f0:8", ["const:65f7cc:8", "const:4:8"]]
- 0065f7cc ["CALL", null, ["ram:47acb4:8"]]
+ 0065f80c ["INT_ADD", "register:40f0:8", ["const:65f80c:8", "const:4:8"]]
+ 0065f80c ["CALL", null, ["ram:47acf4:8"]]
- 0065f7cc bytes 3a6df897
+ 0065f80c bytes 3a6df897
- 0065f85c ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0065f85c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f85c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f85c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f89c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0065f89c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f89c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f89c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f85c bytes 08e12c91
+ 0065f89c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac77edfb1b9b6bb37e5f564f4feb665"></a>

### [`0065ff98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065ff98.md) → [`0065ffd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065ffd8.md) _INIT_83

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660058",
      "incomplete_value": true,
      "site": "00660074",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00660018",
      "incomplete_value": true,
      "site": "00660034",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660078",
      "incomplete_value": true,
      "site": "00660090",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00660038",
      "incomplete_value": true,
      "site": "00660050",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006601f8",
      "incomplete_value": false,
      "site": "0066020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006601b8",
      "incomplete_value": false,
      "site": "006601cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00660014",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00660038",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00660058",
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
      "00660014",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00660038",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00660058",
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

- 旧版 [`00660010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065ff98.md#insn-00660010) · [`006601cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065ff98.md#insn-006601cc) · [`0065ffc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065ff98.md#insn-0065ffc4)
- 新版 `00660050`（命令位置の公開資料なし） · `0066020c`（命令位置の公開資料なし） · `00660004`（命令位置の公開資料なし）

~~~diff
- 00660010 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00660010 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00660010 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00660010 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00660050 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00660050 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00660050 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00660050 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00660010 bytes 4a093691
+ 00660050 bytes 4a093791
- 006601cc ["INT_ADD", "register:40f0:8", ["const:6601cc:8", "const:4:8"]]
- 006601cc ["CALL", null, ["callee:00c57e30:8"]]
+ 0066020c ["INT_ADD", "register:40f0:8", ["const:66020c:8", "const:4:8"]]
+ 0066020c ["CALL", null, ["callee:00c57e30:8"]]
- 006601cc bytes 19de1794
+ 0066020c bytes 09df1794
- 0065ffc4 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0065ffc4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0065ffc4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0065ffc4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00660004 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00660004 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00660004 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00660004 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0065ffc4 bytes 73e22291
+ 00660004 bytes 73e23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09b9e6bbcd5099617613a56468603572"></a>

### [`006608f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00660/006608f8.md) → [`00660938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00660/00660938.md) FUN_00660938

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006609a0",
      "incomplete_value": true,
      "site": "006609b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:441:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00660960",
      "incomplete_value": true,
      "site": "00660978",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:401:8"
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
      "definition_site": "006609bc",
      "incomplete_value": true,
      "site": "006609bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0066097c",
      "incomplete_value": true,
      "site": "0066097c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660f0c",
      "incomplete_value": true,
      "site": "00660f24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00660ecc",
      "incomplete_value": true,
      "site": "00660ee4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 97,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066098c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006609a0",
      "READ",
      [
        "storage",
        "002c1401",
        null,
        "string"
      ]
    ],
    [
      "006609a8",
      "READ",
      [
        "storage",
        "002c140f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0066098c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006609a0",
      "READ",
      [
        "storage",
        "002c1441",
        null,
        "string"
      ]
    ],
    [
      "006609a8",
      "READ",
      [
        "storage",
        "002c144f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006609bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00660/006608f8.md#insn-006609bc) · [`00662058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00660/006608f8.md#insn-00662058) · [`00662204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00660/006608f8.md#insn-00662204)
- 新版 `006609fc`（命令位置の公開資料なし） · `00662098`（命令位置の公開資料なし） · `00662244`（命令位置の公開資料なし）

~~~diff
- 006609bc ["INT_ADD", "register:40f0:8", ["const:6609bc:8", "const:4:8"]]
- 006609bc ["CALL", null, ["callee:00488178:8"]]
+ 006609fc ["INT_ADD", "register:40f0:8", ["const:6609fc:8", "const:4:8"]]
+ 006609fc ["CALL", null, ["callee:00488178:8"]]
- 006609bc bytes df9df897
+ 006609fc bytes df9df897
- 00662058 ["INT_ADD", "register:40f0:8", ["const:662058:8", "const:4:8"]]
- 00662058 ["CALL", null, ["callee:00488178:8"]]
+ 00662098 ["INT_ADD", "register:40f0:8", ["const:662098:8", "const:4:8"]]
+ 00662098 ["CALL", null, ["callee:00488178:8"]]
- 00662058 bytes 3898f897
+ 00662098 bytes 3898f897
- 00662204 ["INT_ADD", "register:40f0:8", ["const:662204:8", "const:4:8"]]
- 00662204 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00662244 ["INT_ADD", "register:40f0:8", ["const:662244:8", "const:4:8"]]
+ 00662244 ["CALL", null, ["callee:00c57fb0:8"]]
- 00662204 bytes 6bd61794
+ 00662244 bytes 5bd71794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44308f836a8e7eb44ef17f6f998bf4fa"></a>

### [`00662a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a10.md) → [`00662a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662a50.md) FUN_00662a50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006608f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00660/006608f8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00660938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00660/00660938.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00662a5c",
      "incomplete_value": false,
      "site": "00662a60",
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
      "definition_site": "00662a1c",
      "incomplete_value": false,
      "site": "00662a20",
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
      "00662a5c",
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
      "00662a5c",
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

- 旧版 [`00662a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a10.md#insn-00662a20) · [`00662a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a10.md#insn-00662a1c)
- 新版 `00662a60`（命令位置の公開資料なし） · `00662a5c`（命令位置の公開資料なし）

~~~diff
- 00662a20 ["INT_ADD", "register:40f0:8", ["const:662a20:8", "const:4:8"]]
- 00662a20 ["CALL", null, ["callee:0043b778:8"]]
+ 00662a60 ["INT_ADD", "register:40f0:8", ["const:662a60:8", "const:4:8"]]
+ 00662a60 ["CALL", null, ["callee:0043b778:8"]]
- 00662a20 bytes 4663f797
+ 00662a60 bytes 4663f797
- 00662a1c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00662a1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00662a1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00662a1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00662a5c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00662a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00662a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00662a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00662a1c bytes 00303c91
+ 00662a5c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eb088a90481a0eb1d474ba996b28642"></a>

### [`00662a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a24.md) → [`00662a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662a64.md) _INIT_84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00662aa0",
      "incomplete_value": true,
      "site": "00662abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00662a60",
      "incomplete_value": true,
      "site": "00662a7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00662ac4",
      "incomplete_value": true,
      "site": "00662ae0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00662a84",
      "incomplete_value": true,
      "site": "00662aa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00662ae4",
      "incomplete_value": true,
      "site": "00662b00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00662aa4",
      "incomplete_value": true,
      "site": "00662ac0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00662aa0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00662ac4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00662ae4",
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
      "00662aa0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00662ac4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00662ae4",
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

- 旧版 [`00662abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a24.md#insn-00662abc) · [`00662c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a24.md#insn-00662c58) · [`00662a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662a24.md#insn-00662a50)
- 新版 `00662afc`（命令位置の公開資料なし） · `00662c98`（命令位置の公開資料なし） · `00662a90`（命令位置の公開資料なし）

~~~diff
- 00662abc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00662abc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00662abc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00662abc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00662afc ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00662afc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00662afc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00662afc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00662abc bytes 4a553a91
+ 00662afc bytes 4a893d91
- 00662c58 ["INT_ADD", "register:40f0:8", ["const:662c58:8", "const:4:8"]]
- 00662c58 ["CALL", null, ["callee:00c57e30:8"]]
+ 00662c98 ["INT_ADD", "register:40f0:8", ["const:662c98:8", "const:4:8"]]
+ 00662c98 ["CALL", null, ["callee:00c57e30:8"]]
- 00662c58 bytes 76d31794
+ 00662c98 bytes 66d41794
- 00662a50 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00662a50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00662a50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00662a50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00662a90 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00662a90 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00662a90 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00662a90 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00662a50 bytes 73822391
+ 00662a90 bytes 73823391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d0dc33fa61615fe2d45a6be95f4982c"></a>

### [`00662db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662db4.md) → [`00662df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662df4.md) FUN_00662df4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00662e38",
      "incomplete_value": false,
      "site": "00662e44",
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
      "definition_site": "00662df8",
      "incomplete_value": false,
      "site": "00662e04",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00662e60",
      "incomplete_value": true,
      "site": "00662e78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ceb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00662e20",
      "incomplete_value": true,
      "site": "00662e38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cab:8"
              ]
            ]
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
      "definition_site": "00663944",
      "incomplete_value": true,
      "site": "00663948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00663904",
      "incomplete_value": true,
      "site": "00663908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 140,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00662e44",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00662e60",
      "READ",
      [
        "storage",
        "002afcab",
        null,
        "string"
      ]
    ],
    [
      "00663934",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00662e44",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00662e60",
      "READ",
      [
        "storage",
        "002afceb",
        null,
        "string"
      ]
    ],
    [
      "00663934",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00662df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662db4.md#insn-00662df8) · [`006638c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662db4.md#insn-006638c8) · [`0066394c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662db4.md#insn-0066394c)
- 新版 `00662e38`（命令位置の公開資料なし） · `00663908`（命令位置の公開資料なし） · `0066398c`（命令位置の公開資料なし）

~~~diff
- 00662df8 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00662df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00662df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00662df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00662e38 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00662e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00662e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00662e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00662df8 bytes 08e12491
+ 00662e38 bytes 08e13491
- 006638c8 ["INT_ADD", "register:40f0:8", ["const:6638c8:8", "const:4:8"]]
- 006638c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00663908 ["INT_ADD", "register:40f0:8", ["const:663908:8", "const:4:8"]]
+ 00663908 ["CALL", null, ["callee:00c53d00:8"]]
- 006638c8 bytes 06c01794
+ 00663908 bytes fec01794
- 0066394c ["INT_ADD", "register:40f0:8", ["const:66394c:8", "const:4:8"]]
- 0066394c ["CALL", null, ["callee:00c57fb0:8"]]
+ 0066398c ["INT_ADD", "register:40f0:8", ["const:66398c:8", "const:4:8"]]
+ 0066398c ["CALL", null, ["callee:00c57fb0:8"]]
- 0066394c bytes 99d01794
+ 0066398c bytes 89d11794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bca464bd564b1172c8f3a8477f1bbb51"></a>

### [`006643dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643dc.md) → [`0066441c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/0066441c.md) FUN_0066441c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00664258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664258.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00664298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664298.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00664428",
      "incomplete_value": false,
      "site": "0066442c",
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
      "definition_site": "006643e8",
      "incomplete_value": false,
      "site": "006643ec",
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
      "00664428",
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
      "00664428",
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

- 旧版 [`006643ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643dc.md#insn-006643ec) · [`006643e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643dc.md#insn-006643e8)
- 新版 `0066442c`（命令位置の公開資料なし） · `00664428`（命令位置の公開資料なし）

~~~diff
- 006643ec ["INT_ADD", "register:40f0:8", ["const:6643ec:8", "const:4:8"]]
- 006643ec ["CALL", null, ["callee:0043b778:8"]]
+ 0066442c ["INT_ADD", "register:40f0:8", ["const:66442c:8", "const:4:8"]]
+ 0066442c ["CALL", null, ["callee:0043b778:8"]]
- 006643ec bytes d35cf797
+ 0066442c bytes d35cf797
- 006643e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 006643e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006643e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006643e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00664428 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00664428 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00664428 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00664428 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006643e8 bytes 00303c91
+ 00664428 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2abfba3e8f9e7df8275a9e23122c739b"></a>

### [`006643f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643f0.md) → [`00664430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664430.md) _INIT_85

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066446c",
      "incomplete_value": true,
      "site": "00664488",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066442c",
      "incomplete_value": true,
      "site": "00664448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00664490",
      "incomplete_value": true,
      "site": "006644ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00664450",
      "incomplete_value": true,
      "site": "0066446c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006644b0",
      "incomplete_value": true,
      "site": "006644cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00664470",
      "incomplete_value": true,
      "site": "0066448c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0066446c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00664490",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006644b0",
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
      "0066446c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00664490",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006644b0",
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

- 旧版 [`00664468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643f0.md#insn-00664468) · [`00664488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643f0.md#insn-00664488) · [`00664578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006643f0.md#insn-00664578)
- 新版 `006644a8`（命令位置の公開資料なし） · `006644c8`（命令位置の公開資料なし） · `006645b8`（命令位置の公開資料なし）

~~~diff
- 00664468 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00664468 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00664468 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00664468 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006644a8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006644a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006644a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006644a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00664468 bytes 4a093691
+ 006644a8 bytes 4a093791
- 00664488 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00664488 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00664488 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00664488 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006644c8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006644c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006644c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006644c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00664488 bytes 4a553a91
+ 006644c8 bytes 4a893d91
- 00664578 ["INT_ADD", "register:40f0:8", ["const:664578:8", "const:4:8"]]
- 00664578 ["CALL", null, ["callee:0043b7f8:8"]]
+ 006645b8 ["INT_ADD", "register:40f0:8", ["const:6645b8:8", "const:4:8"]]
+ 006645b8 ["CALL", null, ["callee:0043b7f8:8"]]
- 00664578 bytes 905cf797
+ 006645b8 bytes 905cf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546012a92332ae256e4d844afade5e04"></a>

### [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md) → [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md) FUN_006649ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 9件 [`007525ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/007525ac.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) · 呼出先 2件 [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 9件 [`007525ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/007525ec.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`008ed1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ed/008ed1b8.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) · 呼出先 2件 [`0082eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00664a34",
      "incomplete_value": false,
      "site": "00664a34",
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
            "const:e9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006649f4",
      "incomplete_value": false,
      "site": "006649f4",
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
            "const:a9c:8"
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
      "00664a34",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00664a34",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006649f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md#insn-006649f4) · [`006649bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md#insn-006649bc) · [`006649f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md#insn-006649f8)
- 新版 `00664a34`（命令位置の公開資料なし） · `006649fc`（命令位置の公開資料なし） · `00664a38`（命令位置の公開資料なし）

~~~diff
- 006649f4 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 006649f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a9c:8"]]
- 006649f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00664a34 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00664a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e9c:8"]]
+ 00664a34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 006649f4 bytes 13712a39
+ 00664a34 bytes 13713a39
- 006649bc ["INT_ADD", "register:40f0:8", ["const:6649bc:8", "const:4:8"]]
- 006649bc ["CALL", null, ["callee:008514f8:8"]]
+ 006649fc ["INT_ADD", "register:40f0:8", ["const:6649fc:8", "const:4:8"]]
+ 006649fc ["CALL", null, ["callee:008514f8:8"]]
- 006649bc bytes bfb20794
+ 006649fc bytes bfb20794
- 006649f8 ["INT_ADD", "register:40f0:8", ["const:6649f8:8", "const:4:8"]]
- 006649f8 ["CALL", null, ["callee:008514f8:8"]]
+ 00664a38 ["INT_ADD", "register:40f0:8", ["const:664a38:8", "const:4:8"]]
+ 00664a38 ["CALL", null, ["callee:008514f8:8"]]
- 006649f8 bytes b0b20794
+ 00664a38 bytes b0b20794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23215dfe29ad6c8130b5661cb4fd406d"></a>

### [`006653cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md) → [`0066540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/0066540c.md) FUN_0066540c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00996a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996a80.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md) [`00663b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00663/00663b50.md) [`0066759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md)
- 新版 呼出元 5件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`00996c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996c1c.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md) [`00663b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00663/00663b90.md) [`006675dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/006675dc.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.54% / 新版 97.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006654dc",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066549c",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006654ec",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006654ac",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00665500",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006654c0",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "00665488",
      "READ",
      [
        "storage",
        "002c4208",
        null,
        "undefined8"
      ]
    ],
    [
      "006654dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "006654ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "00665488",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "006654dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "006654ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066549c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md#insn-0066549c) · [`006654ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md#insn-006654ac) · [`006654c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md#insn-006654c0)
- 新版 `006654dc`（命令位置の公開資料なし） · `006654ec`（命令位置の公開資料なし） · `00665500`（命令位置の公開資料なし）

~~~diff
- 0066549c ["INT_ADD", "register:40f0:8", ["const:66549c:8", "const:4:8"]]
- 0066549c ["CALL", null, ["ram:71be98:8"]]
+ 006654dc ["INT_ADD", "register:40f0:8", ["const:6654dc:8", "const:4:8"]]
+ 006654dc ["CALL", null, ["ram:71bed8:8"]]
- 0066549c bytes 7fda0294
+ 006654dc bytes 7fda0294
- 006654ac ["INT_ADD", "register:40f0:8", ["const:6654ac:8", "const:4:8"]]
- 006654ac ["CALL", null, ["ram:71be98:8"]]
+ 006654ec ["INT_ADD", "register:40f0:8", ["const:6654ec:8", "const:4:8"]]
+ 006654ec ["CALL", null, ["ram:71bed8:8"]]
- 006654ac bytes 7bda0294
+ 006654ec bytes 7bda0294
- 006654c0 ["INT_ADD", "register:40f0:8", ["const:6654c0:8", "const:4:8"]]
- 006654c0 ["CALL", null, ["ram:71be98:8"]]
+ 00665500 ["INT_ADD", "register:40f0:8", ["const:665500:8", "const:4:8"]]
+ 00665500 ["CALL", null, ["ram:71bed8:8"]]
- 006654c0 bytes 76da0294
+ 00665500 bytes 76da0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e430d537f4740f25ba00c515f046c38"></a>

### [`00665d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md) → [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md) FUN_00665d64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 14件 [`006a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a7/006a7480.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`008d0b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md) [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) · 呼出先 12件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 14件 [`006a74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a74c0.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`008ec2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec2a0.md) [`008ed1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ed/008ed1b8.md) · 呼出先 12件 [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 79.30% / 新版 79.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00665e28",
      "incomplete_value": true,
      "site": "00665e38",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00665de8",
      "incomplete_value": true,
      "site": "00665df8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:418:8"
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
      "definition_site": "00665e6c",
      "incomplete_value": true,
      "site": "00665e6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00665e2c",
      "incomplete_value": true,
      "site": "00665e2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3cf:8"
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
      "definition_site": "00665ecc",
      "incomplete_value": true,
      "site": "00665ee4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:352:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00665e8c",
      "incomplete_value": true,
      "site": "00665ea4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
      "00665e14",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00665e28",
      "READ",
      [
        "storage",
        "002c1418",
        null,
        "string"
      ]
    ],
    [
      "00665e5c",
      "READ",
      [
        "storage",
        "002b83cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00665e14",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00665e28",
      "READ",
      [
        "storage",
        "002c1458",
        null,
        "string"
      ]
    ],
    [
      "00665e5c",
      "READ",
      [
        "storage",
        "002b840f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00665e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md#insn-00665e0c) · [`00665e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md#insn-00665e38) · [`00665e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md#insn-00665e4c)
- 新版 `00665e4c`（命令位置の公開資料なし） · `00665e78`（命令位置の公開資料なし） · `00665e8c`（命令位置の公開資料なし）

~~~diff
- 00665e0c ["INT_ADD", "register:40f0:8", ["const:665e0c:8", "const:4:8"]]
- 00665e0c ["CALL", null, ["callee:004476f4:8"]]
+ 00665e4c ["INT_ADD", "register:40f0:8", ["const:665e4c:8", "const:4:8"]]
+ 00665e4c ["CALL", null, ["callee:004476f4:8"]]
- 00665e0c bytes 2a86f797
+ 00665e4c bytes 2a86f797
- 00665e38 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00665e38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00665e38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00665e38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00665e78 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00665e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00665e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00665e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00665e38 bytes 00002c91
+ 00665e78 bytes 00003c91
- 00665e4c ["INT_ADD", "register:40f0:8", ["const:665e4c:8", "const:4:8"]]
- 00665e4c ["CALL", null, ["callee:0047e60c:8"]]
+ 00665e8c ["INT_ADD", "register:40f0:8", ["const:665e8c:8", "const:4:8"]]
+ 00665e8c ["CALL", null, ["callee:0047e60c:8"]]
- 00665e4c bytes e061f897
+ 00665e8c bytes e061f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc10733e0effb2e23fd01c57923a555"></a>

### [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) → [`00666320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666320.md) FUN_00666320

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) [`008bc884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc884.md) [`008c4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4784.md) [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) [`008db480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md) · 呼出先 12件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md)
- 新版 呼出元 7件 [`007de8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de8c0.md) [`008bc8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bc/008bc8c8.md) [`008c4920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c4/008c4920.md) [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) [`008db61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db61c.md) · 呼出先 12件 [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 79.30% / 新版 79.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006663e4",
      "incomplete_value": true,
      "site": "006663f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006663a4",
      "incomplete_value": true,
      "site": "006663b4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:418:8"
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
      "definition_site": "00666428",
      "incomplete_value": true,
      "site": "00666428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006663e8",
      "incomplete_value": true,
      "site": "006663e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3cf:8"
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
      "definition_site": "00666488",
      "incomplete_value": true,
      "site": "006664a0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:352:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00666448",
      "incomplete_value": true,
      "site": "00666460",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
      "006663d0",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006663e4",
      "READ",
      [
        "storage",
        "002c1418",
        null,
        "string"
      ]
    ],
    [
      "00666418",
      "READ",
      [
        "storage",
        "002b83cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006663d0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006663e4",
      "READ",
      [
        "storage",
        "002c1458",
        null,
        "string"
      ]
    ],
    [
      "00666418",
      "READ",
      [
        "storage",
        "002b840f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006663c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md#insn-006663c8) · [`006663f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md#insn-006663f4) · [`00666408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md#insn-00666408)
- 新版 `00666408`（命令位置の公開資料なし） · `00666434`（命令位置の公開資料なし） · `00666448`（命令位置の公開資料なし）

~~~diff
- 006663c8 ["INT_ADD", "register:40f0:8", ["const:6663c8:8", "const:4:8"]]
- 006663c8 ["CALL", null, ["callee:004476f4:8"]]
+ 00666408 ["INT_ADD", "register:40f0:8", ["const:666408:8", "const:4:8"]]
+ 00666408 ["CALL", null, ["callee:004476f4:8"]]
- 006663c8 bytes bb84f797
+ 00666408 bytes bb84f797
- 006663f4 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 006663f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006663f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006663f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00666434 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00666434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00666434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00666434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006663f4 bytes 00002c91
+ 00666434 bytes 00003c91
- 00666408 ["INT_ADD", "register:40f0:8", ["const:666408:8", "const:4:8"]]
- 00666408 ["CALL", null, ["callee:00633374:8"]]
+ 00666448 ["INT_ADD", "register:40f0:8", ["const:666448:8", "const:4:8"]]
+ 00666448 ["CALL", null, ["callee:00633374:8"]]
- 00666408 bytes cb33ff97
+ 00666448 bytes cb33ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f4f39890a6b47f54d6221b255eb793"></a>

### [`00666768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md) → [`006667a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/006667a8.md) FUN_006667a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) [`009f4e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f4/009f4e08.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 12件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 4件 [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`00984c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984c34.md) [`009f4fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 12件 [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.22% / 新版 78.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00666868",
      "incomplete_value": true,
      "site": "00666878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:924:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00666828",
      "incomplete_value": true,
      "site": "00666838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:848:8"
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
      "definition_site": "006668ac",
      "incomplete_value": true,
      "site": "006668ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066686c",
      "incomplete_value": true,
      "site": "0066686c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e:8"
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
      "definition_site": "0066691c",
      "incomplete_value": true,
      "site": "0066691c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006668dc",
      "incomplete_value": true,
      "site": "006668dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a4f:8"
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
      "00666854",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00666868",
      "READ",
      [
        "storage",
        "002a6848",
        null,
        "string"
      ]
    ],
    [
      "0066689c",
      "READ",
      [
        "storage",
        "002c009e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00666854",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00666868",
      "READ",
      [
        "storage",
        "002a6924",
        null,
        "string"
      ]
    ],
    [
      "0066689c",
      "READ",
      [
        "storage",
        "002c00de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066684c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md#insn-0066684c) · [`00666878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md#insn-00666878) · [`0066688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md#insn-0066688c)
- 新版 `0066688c`（命令位置の公開資料なし） · `006668b8`（命令位置の公開資料なし） · `006668cc`（命令位置の公開資料なし）

~~~diff
- 0066684c ["INT_ADD", "register:40f0:8", ["const:66684c:8", "const:4:8"]]
- 0066684c ["CALL", null, ["callee:004476f4:8"]]
+ 0066688c ["INT_ADD", "register:40f0:8", ["const:66688c:8", "const:4:8"]]
+ 0066688c ["CALL", null, ["callee:004476f4:8"]]
- 0066684c bytes 9a83f797
+ 0066688c bytes 9a83f797
- 00666878 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00666878 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00666878 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00666878 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006668b8 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 006668b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006668b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006668b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00666878 bytes 00002c91
+ 006668b8 bytes 00003c91
- 0066688c ["INT_ADD", "register:40f0:8", ["const:66688c:8", "const:4:8"]]
- 0066688c ["CALL", null, ["callee:0047e60c:8"]]
+ 006668cc ["INT_ADD", "register:40f0:8", ["const:6668cc:8", "const:4:8"]]
+ 006668cc ["CALL", null, ["callee:0047e60c:8"]]
- 0066688c bytes 505ff897
+ 006668cc bytes 505ff897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf7cf97fd82a652bbd4a35deb008e1d"></a>

### [`00666be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md) → [`00666c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666c28.md) FUN_00666c28

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00982bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982bd0.md) [`00acfac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md) · 呼出先 12件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 2件 [`00982d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982d6c.md) [`00acfcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acfcc0.md) · 呼出先 12件 [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.22% / 新版 78.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_destination` 14件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00666ce8",
      "incomplete_value": true,
      "site": "00666cf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:924:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00666ca8",
      "incomplete_value": true,
      "site": "00666cb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:848:8"
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
      "definition_site": "00666d2c",
      "incomplete_value": true,
      "site": "00666d2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00666cec",
      "incomplete_value": true,
      "site": "00666cec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e:8"
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
      "definition_site": "00666d9c",
      "incomplete_value": true,
      "site": "00666d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00666d5c",
      "incomplete_value": true,
      "site": "00666d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a4f:8"
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
      "00666cd4",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00666ce8",
      "READ",
      [
        "storage",
        "002a6848",
        null,
        "string"
      ]
    ],
    [
      "00666d1c",
      "READ",
      [
        "storage",
        "002c009e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00666cd4",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00666ce8",
      "READ",
      [
        "storage",
        "002a6924",
        null,
        "string"
      ]
    ],
    [
      "00666d1c",
      "READ",
      [
        "storage",
        "002c00de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00666ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md#insn-00666ccc) · [`00666cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md#insn-00666cf8) · [`00666d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md#insn-00666d0c)
- 新版 `00666d0c`（命令位置の公開資料なし） · `00666d38`（命令位置の公開資料なし） · `00666d4c`（命令位置の公開資料なし）

~~~diff
- 00666ccc ["INT_ADD", "register:40f0:8", ["const:666ccc:8", "const:4:8"]]
- 00666ccc ["CALL", null, ["callee:004476f4:8"]]
+ 00666d0c ["INT_ADD", "register:40f0:8", ["const:666d0c:8", "const:4:8"]]
+ 00666d0c ["CALL", null, ["callee:004476f4:8"]]
- 00666ccc bytes 7a82f797
+ 00666d0c bytes 7a82f797
- 00666cf8 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00666cf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00666cf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00666cf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00666d38 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00666d38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00666d38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00666d38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00666cf8 bytes 00002c91
+ 00666d38 bytes 00003c91
- 00666d0c ["INT_ADD", "register:40f0:8", ["const:666d0c:8", "const:4:8"]]
- 00666d0c ["CALL", null, ["callee:00633374:8"]]
+ 00666d4c ["INT_ADD", "register:40f0:8", ["const:666d4c:8", "const:4:8"]]
+ 00666d4c ["CALL", null, ["callee:00633374:8"]]
- 00666d0c bytes 8a31ff97
+ 00666d4c bytes 8a31ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad2111270387c753c709075b9da8d59e"></a>

### [`00667068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667068.md) → [`006670a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/006670a8.md) FUN_006670a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`006ab344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ab/006ab344.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) [`00912918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00912/00912918.md) · 呼出先 6件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`006ab384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ab/006ab384.md) [`008ed1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ed/008ed1b8.md) [`009049b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009049b4.md) [`00912ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00912/00912ab4.md) · 呼出先 6件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006671cc",
      "incomplete_value": true,
      "site": "006671cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:341:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066718c",
      "incomplete_value": true,
      "site": "0066718c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:274:8"
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
      "006671c8",
      "READ",
      [
        "storage",
        "002a0274",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006671c8",
      "READ",
      [
        "storage",
        "002a0341",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006670ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667068.md#insn-006670ac) · [`0066713c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667068.md#insn-0066713c) · [`00667184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667068.md#insn-00667184)
- 新版 `006670ec`（命令位置の公開資料なし） · `0066717c`（命令位置の公開資料なし） · `006671c4`（命令位置の公開資料なし）

~~~diff
- 006670ac ["INT_ADD", "register:40f0:8", ["const:6670ac:8", "const:4:8"]]
- 006670ac ["CALL", null, ["callee:008514f8:8"]]
+ 006670ec ["INT_ADD", "register:40f0:8", ["const:6670ec:8", "const:4:8"]]
+ 006670ec ["CALL", null, ["callee:008514f8:8"]]
- 006670ac bytes 03a90794
+ 006670ec bytes 03a90794
- 0066713c ["INT_ADD", "register:40f0:8", ["const:66713c:8", "const:4:8"]]
- 0066713c ["CALL", null, ["callee:00447ef4:8"]]
+ 0066717c ["INT_ADD", "register:40f0:8", ["const:66717c:8", "const:4:8"]]
+ 0066717c ["CALL", null, ["callee:00447ef4:8"]]
- 0066713c bytes 5e83f797
+ 0066717c bytes 5e83f797
- 00667184 ["COPY", "tmp:0:8", ["const:274:8"]]
- 00667184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00667184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00667184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006671c4 ["COPY", "tmp:0:8", ["const:341:8"]]
+ 006671c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006671c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006671c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00667184 bytes 08d10991
+ 006671c4 bytes 08050d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2725054d7a3eb4a4a21f3a380f568a09"></a>

### [`00667324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667324.md) → [`00667364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/00667364.md) FUN_00667364

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`006db3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md) [`00904818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00904/00904818.md) [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) [`00a6fb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6f/00a6fb90.md) [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · 呼出先 6件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 7件 [`006db3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db3e0.md) [`009049b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00904/009049b4.md) [`0090b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090b/0090b908.md) [`00a6fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6f/00a6fd88.md) [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) · 呼出先 6件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00667410",
      "incomplete_value": true,
      "site": "00667420",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:46a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006673d0",
      "incomplete_value": true,
      "site": "006673e0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:42a:8"
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
      "definition_site": "0066744c",
      "incomplete_value": true,
      "site": "00667464",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066740c",
      "incomplete_value": true,
      "site": "00667424",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:446:8"
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
      "definition_site": "00667480",
      "incomplete_value": true,
      "site": "00667480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:341:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00667440",
      "incomplete_value": true,
      "site": "00667440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:274:8"
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
      "00667410",
      "READ",
      [
        "storage",
        "002c142a",
        null,
        "string"
      ]
    ],
    [
      "0066744c",
      "READ",
      [
        "storage",
        "002a4446",
        null,
        "string"
      ]
    ],
    [
      "00667474",
      "READ",
      [
        "storage",
        "002a0274",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00667410",
      "READ",
      [
        "storage",
        "002c146a",
        null,
        "string"
      ]
    ],
    [
      "0066744c",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "00667474",
      "READ",
      [
        "storage",
        "002a0341",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00667400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667324.md#insn-00667400) · [`00667360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667324.md#insn-00667360) · [`006673c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667324.md#insn-006673c8)
- 新版 `00667440`（命令位置の公開資料なし） · `006673a0`（命令位置の公開資料なし） · `00667408`（命令位置の公開資料なし）

~~~diff
- 00667400 ["COPY", "tmp:0:8", ["const:446:8"]]
- 00667400 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00667400 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00667400 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00667440 ["COPY", "tmp:0:8", ["const:513:8"]]
+ 00667440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00667440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00667440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00667400 bytes 29191191
+ 00667440 bytes 294d1491
- 00667360 ["INT_ADD", "register:40f0:8", ["const:667360:8", "const:4:8"]]
- 00667360 ["CALL", null, ["callee:008514f8:8"]]
+ 006673a0 ["INT_ADD", "register:40f0:8", ["const:6673a0:8", "const:4:8"]]
+ 006673a0 ["CALL", null, ["callee:008514f8:8"]]
- 00667360 bytes 56a80794
+ 006673a0 bytes 56a80794
- 006673c8 ["COPY", "tmp:0:8", ["const:42a:8"]]
- 006673c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006673c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006673c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00667408 ["COPY", "tmp:0:8", ["const:46a:8"]]
+ 00667408 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00667408 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00667408 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006673c8 bytes 29a91091
+ 00667408 bytes 29a91191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a780360ed6a9a58a859f3f596c76fb"></a>

### [`006675e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md) → [`00667620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/00667620.md) FUN_00667620

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006661ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006661ac.md) [`006675e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`006661ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/006661ec.md) [`00667620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/00667620.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00667780",
      "incomplete_value": false,
      "site": "00667788",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00667740",
      "incomplete_value": false,
      "site": "00667748",
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
            "const:f13:8"
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
      "definition_site": "006677a4",
      "incomplete_value": false,
      "site": "006677b0",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00667764",
      "incomplete_value": false,
      "site": "00667770",
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
            "const:ea9:8"
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
      "definition_site": "006678d8",
      "incomplete_value": false,
      "site": "006678e0",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00667898",
      "incomplete_value": false,
      "site": "006678a0",
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
            "const:da7:8"
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
      "00667780",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "006677a4",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "006678d8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00667780",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006677a4",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "006678d8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00667748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md#insn-00667748) · [`00667770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md#insn-00667770) · [`006678a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/006675e0.md#insn-006678a0)
- 新版 `00667788`（命令位置の公開資料なし） · `006677b0`（命令位置の公開資料なし） · `006678e0`（命令位置の公開資料なし）

~~~diff
- 00667748 ["INT_ADD", "register:40f0:8", ["const:667748:8", "const:4:8"]]
- 00667748 ["CALL", null, ["callee:00441e94:8"]]
+ 00667788 ["INT_ADD", "register:40f0:8", ["const:667788:8", "const:4:8"]]
+ 00667788 ["CALL", null, ["callee:00441e94:8"]]
- 00667748 bytes c369f797
+ 00667788 bytes c369f797
- 00667770 ["INT_ADD", "register:40f0:8", ["const:667770:8", "const:4:8"]]
- 00667770 ["CALL", null, ["callee:004427f4:8"]]
+ 006677b0 ["INT_ADD", "register:40f0:8", ["const:6677b0:8", "const:4:8"]]
+ 006677b0 ["CALL", null, ["callee:004427f4:8"]]
- 00667770 bytes 116cf797
+ 006677b0 bytes 116cf797
- 006678a0 ["INT_ADD", "register:40f0:8", ["const:6678a0:8", "const:4:8"]]
- 006678a0 ["CALL", null, ["callee:00441e94:8"]]
+ 006678e0 ["INT_ADD", "register:40f0:8", ["const:6678e0:8", "const:4:8"]]
+ 006678e0 ["CALL", null, ["callee:00441e94:8"]]
- 006678a0 bytes 6d69f797
+ 006678e0 bytes 6d69f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636969899e052c8962396b84b2d54023"></a>

### [`00667f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667f50.md) → [`00667f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00667/00667f90.md) _INIT_86

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
      "definition_site": "00667fcc",
      "incomplete_value": true,
      "site": "00667fe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00667f8c",
      "incomplete_value": true,
      "site": "00667fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00667ff0",
      "incomplete_value": true,
      "site": "0066800c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00667fb0",
      "incomplete_value": true,
      "site": "00667fcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668010",
      "incomplete_value": true,
      "site": "0066802c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00667fd0",
      "incomplete_value": true,
      "site": "00667fec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00667fcc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00667ff0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00668010",
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
      "00667fcc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00667ff0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00668010",
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

- 旧版 [`00667fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667f50.md#insn-00667fc8) · [`00667fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667f50.md#insn-00667fe8) · [`006680b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/00667f50.md#insn-006680b0)
- 新版 `00668008`（命令位置の公開資料なし） · `00668028`（命令位置の公開資料なし） · `006680f0`（命令位置の公開資料なし）

~~~diff
- 00667fc8 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00667fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00667fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00667fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00668008 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00668008 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00668008 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00668008 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00667fc8 bytes 4a093691
+ 00668008 bytes 4a093791
- 00667fe8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00667fe8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00667fe8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00667fe8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00668028 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00668028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00668028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00668028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00667fe8 bytes 4a553a91
+ 00668028 bytes 4a893d91
- 006680b0 ["INT_ADD", "register:40f0:8", ["const:6680b0:8", "const:4:8"]]
- 006680b0 ["CALL", null, ["callee:0043b7f8:8"]]
+ 006680f0 ["INT_ADD", "register:40f0:8", ["const:6680f0:8", "const:4:8"]]
+ 006680f0 ["CALL", null, ["callee:0043b7f8:8"]]
- 006680b0 bytes c24df797
+ 006680f0 bytes c24df797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c81dbc4b0df8ee0b3aada5c6fa73715"></a>

### [`00668424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668424.md) → [`00668464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00668/00668464.md) FUN_00668464

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.51% / 新版 92.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006684a0",
      "incomplete_value": false,
      "site": "006684a8",
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
      "definition_site": "00668460",
      "incomplete_value": false,
      "site": "00668468",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006684c0",
      "incomplete_value": true,
      "site": "006684cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:601:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668480",
      "incomplete_value": true,
      "site": "0066848c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c1:8"
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
      "definition_site": "006686a8",
      "incomplete_value": true,
      "site": "006686ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00668668",
      "incomplete_value": true,
      "site": "0066866c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "006684a8",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "002b75c1",
        null,
        "string"
      ]
    ],
    [
      "00668698",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006684a8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "002b7601",
        null,
        "string"
      ]
    ],
    [
      "00668698",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006686b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668424.md#insn-006686b0) · [`00668458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668424.md#insn-00668458) · [`00668460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668424.md#insn-00668460)
- 新版 `006686f0`（命令位置の公開資料なし） · `00668498`（命令位置の公開資料なし） · `006684a0`（命令位置の公開資料なし）

~~~diff
- 006686b0 ["INT_ADD", "register:40f0:8", ["const:6686b0:8", "const:4:8"]]
- 006686b0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 006686f0 ["INT_ADD", "register:40f0:8", ["const:6686f0:8", "const:4:8"]]
+ 006686f0 ["CALL", null, ["callee:00c57fb0:8"]]
- 006686b0 bytes 40bd1794
+ 006686f0 bytes 30be1794
- 00668458 ["INT_ADD", "register:40f0:8", ["const:668458:8", "const:4:8"]]
- 00668458 ["CALL", null, ["callee:00487e20:8"]]
+ 00668498 ["INT_ADD", "register:40f0:8", ["const:668498:8", "const:4:8"]]
+ 00668498 ["CALL", null, ["callee:00487e20:8"]]
- 00668458 bytes 627ef897
+ 00668498 bytes 627ef897
- 00668460 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00668460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00668460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00668460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006684a0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 006684a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006684a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006684a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00668460 bytes 08e12491
+ 006684a0 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cb6690bb253238617ed22474b2c19f7"></a>

### [`00668a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668a20.md) → [`00668a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00668/00668a60.md) _INIT_87

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
      "definition_site": "00668a9c",
      "incomplete_value": true,
      "site": "00668ab8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668a5c",
      "incomplete_value": true,
      "site": "00668a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668ac0",
      "incomplete_value": true,
      "site": "00668adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668a80",
      "incomplete_value": true,
      "site": "00668a9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668ae0",
      "incomplete_value": true,
      "site": "00668afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00668aa0",
      "incomplete_value": true,
      "site": "00668abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00668a9c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00668ac0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00668ae0",
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
      "00668a9c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00668ac0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00668ae0",
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

- 旧版 [`00668a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668a20.md#insn-00668a98) · [`00668ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668a20.md#insn-00668ab8) · [`00668b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668a20.md#insn-00668b80)
- 新版 `00668ad8`（命令位置の公開資料なし） · `00668af8`（命令位置の公開資料なし） · `00668bc0`（命令位置の公開資料なし）

~~~diff
- 00668a98 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00668a98 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00668a98 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00668a98 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00668ad8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00668ad8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00668ad8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00668ad8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00668a98 bytes 4a093691
+ 00668ad8 bytes 4a093791
- 00668ab8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00668ab8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00668ab8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00668ab8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00668af8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00668af8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00668af8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00668af8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00668ab8 bytes 4a553a91
+ 00668af8 bytes 4a893d91
- 00668b80 ["INT_ADD", "register:40f0:8", ["const:668b80:8", "const:4:8"]]
- 00668b80 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00668bc0 ["INT_ADD", "register:40f0:8", ["const:668bc0:8", "const:4:8"]]
+ 00668bc0 ["CALL", null, ["callee:0043b7f8:8"]]
- 00668b80 bytes 0e4bf797
+ 00668bc0 bytes 0e4bf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2ed39c3d128620faeaeb51632a9b73"></a>

### [`00668db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md) → [`00668df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00668/00668df0.md) FUN_00668df0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 23件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 23件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00668e34",
      "incomplete_value": false,
      "site": "00668e40",
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
      "definition_site": "00668df4",
      "incomplete_value": false,
      "site": "00668e00",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00668e78",
      "incomplete_value": true,
      "site": "00668e90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:194:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668e38",
      "incomplete_value": true,
      "site": "00668e50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:154:8"
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
      "definition_site": "006699cc",
      "incomplete_value": true,
      "site": "006699d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:795:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066998c",
      "incomplete_value": true,
      "site": "00669998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:755:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 133,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00668e40",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00668e78",
      "READ",
      [
        "storage",
        "002b9154",
        null,
        "string"
      ]
    ],
    [
      "006690a4",
      "READ",
      [
        "storage",
        "002ad979",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00668e40",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00668e78",
      "READ",
      [
        "storage",
        "002b9194",
        null,
        "string"
      ]
    ],
    [
      "006690a4",
      "READ",
      [
        "storage",
        "002ad9b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00669154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md#insn-00669154) · [`00669304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md#insn-00669304) · [`006694d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668db0.md#insn-006694d4)
- 新版 `00669194`（命令位置の公開資料なし） · `00669344`（命令位置の公開資料なし） · `00669514`（命令位置の公開資料なし）

~~~diff
- 00669154 ["INT_ADD", "register:40f0:8", ["const:669154:8", "const:4:8"]]
- 00669154 ["CALL", null, ["callee:0066baf4:8"]]
+ 00669194 ["INT_ADD", "register:40f0:8", ["const:669194:8", "const:4:8"]]
+ 00669194 ["CALL", null, ["callee:0066baf4:8"]]
- 00669154 bytes 580a0094
+ 00669194 bytes 580a0094
- 00669304 ["INT_ADD", "register:40f0:8", ["const:669304:8", "const:4:8"]]
- 00669304 ["CALL", null, ["callee:0066baf4:8"]]
+ 00669344 ["INT_ADD", "register:40f0:8", ["const:669344:8", "const:4:8"]]
+ 00669344 ["CALL", null, ["callee:0066baf4:8"]]
- 00669304 bytes ec090094
+ 00669344 bytes ec090094
- 006694d4 ["INT_ADD", "register:40f0:8", ["const:6694d4:8", "const:4:8"]]
- 006694d4 ["CALL", null, ["callee:0066baf4:8"]]
+ 00669514 ["INT_ADD", "register:40f0:8", ["const:669514:8", "const:4:8"]]
+ 00669514 ["CALL", null, ["callee:0066baf4:8"]]
- 006694d4 bytes 78090094
+ 00669514 bytes 78090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da96b7f9afeadeba85369e5a3ea793f2"></a>

### [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) → [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) FUN_0066a408

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 14件 [`005e7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`0066a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md) [`0066ac5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ac5c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 4件 [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 14件 [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`0066a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a61c.md) [`0066ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066ac9c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 4件 [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066a49c",
      "incomplete_value": false,
      "site": "0066a4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a45c",
      "incomplete_value": false,
      "site": "0066a464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "definition_site": "0066a500",
      "incomplete_value": false,
      "site": "0066a518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a4c0",
      "incomplete_value": false,
      "site": "0066a4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066a49c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0066a500",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066a49c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0066a500",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066a464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md#insn-0066a464) · [`0066a498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md#insn-0066a498) · [`0066a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md#insn-0066a4d8)
- 新版 `0066a4a4`（命令位置の公開資料なし） · `0066a4d8`（命令位置の公開資料なし） · `0066a518`（命令位置の公開資料なし）

~~~diff
- 0066a464 ["INT_ADD", "register:40f0:8", ["const:66a464:8", "const:4:8"]]
- 0066a464 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a4a4 ["INT_ADD", "register:40f0:8", ["const:66a4a4:8", "const:4:8"]]
+ 0066a4a4 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a464 bytes 94050094
+ 0066a4a4 bytes 94050094
- 0066a498 ["INT_ADD", "register:40f0:8", ["const:66a498:8", "const:4:8"]]
- 0066a498 ["CALL", null, ["callee:008514f8:8"]]
+ 0066a4d8 ["INT_ADD", "register:40f0:8", ["const:66a4d8:8", "const:4:8"]]
+ 0066a4d8 ["CALL", null, ["callee:008514f8:8"]]
- 0066a498 bytes 089c0794
+ 0066a4d8 bytes 089c0794
- 0066a4d8 ["INT_ADD", "register:40f0:8", ["const:66a4d8:8", "const:4:8"]]
- 0066a4d8 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a518 ["INT_ADD", "register:40f0:8", ["const:66a518:8", "const:4:8"]]
+ 0066a518 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a4d8 bytes 77050094
+ 0066a518 bytes 77050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4222549b7c143708e49d3550540e4d9"></a>

### [`0066a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a544.md) → [`0066a584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a584.md) FUN_0066a584

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) [`007c970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 2件 [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`005e7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7504.md) [`007c974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 2件 [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066a5dc",
      "incomplete_value": false,
      "site": "0066a5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a59c",
      "incomplete_value": false,
      "site": "0066a5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066a5dc",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066a5dc",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066a5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a544.md#insn-0066a5b0) · [`0066a59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a544.md#insn-0066a59c) · [`0066a5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a544.md#insn-0066a5d8)
- 新版 `0066a5f0`（命令位置の公開資料なし） · `0066a5dc`（命令位置の公開資料なし） · `0066a618`（命令位置の公開資料なし）

~~~diff
- 0066a5b0 ["INT_ADD", "register:40f0:8", ["const:66a5b0:8", "const:4:8"]]
- 0066a5b0 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a5f0 ["INT_ADD", "register:40f0:8", ["const:66a5f0:8", "const:4:8"]]
+ 0066a5f0 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a5b0 bytes 41050094
+ 0066a5f0 bytes 41050094
- 0066a59c ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 0066a59c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0066a59c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0066a59c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0066a5dc ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 0066a5dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0066a5dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0066a5dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0066a59c bytes 42d41a91
+ 0066a5dc bytes 42d41b91
- 0066a5d8 ["INT_ADD", "register:40f0:8", ["const:66a5d8:8", "const:4:8"]]
- 0066a5d8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0066a618 ["INT_ADD", "register:40f0:8", ["const:66a618:8", "const:4:8"]]
+ 0066a618 ["CALL", null, ["callee:00c57ee0:8"]]
- 0066a5d8 bytes 42b51794
+ 0066a618 bytes 32b61794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a12f01007beceff40733c490b093e5"></a>

### [`0066a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md) → [`0066a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a61c.md) FUN_0066a61c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 19件 [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) [`005e2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2e00.md) [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`0066b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md)
- 新版 呼出元 19件 [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) [`005e2e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2e40.md) [`005e7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7504.md) [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`0066b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b5a0.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066a678",
      "incomplete_value": false,
      "site": "0066a690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a638",
      "incomplete_value": false,
      "site": "0066a650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "definition_site": "0066a6a4",
      "incomplete_value": false,
      "site": "0066a6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a664",
      "incomplete_value": false,
      "site": "0066a67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "definition_site": "0066a784",
      "incomplete_value": false,
      "site": "0066a79c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a744",
      "incomplete_value": false,
      "site": "0066a75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066a678",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0066a6a4",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0066a784",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066a678",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0066a6a4",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0066a784",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md#insn-0066a650) · [`0066a67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md#insn-0066a67c) · [`0066a75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md#insn-0066a75c)
- 新版 `0066a690`（命令位置の公開資料なし） · `0066a6bc`（命令位置の公開資料なし） · `0066a79c`（命令位置の公開資料なし）

~~~diff
- 0066a650 ["INT_ADD", "register:40f0:8", ["const:66a650:8", "const:4:8"]]
- 0066a650 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a690 ["INT_ADD", "register:40f0:8", ["const:66a690:8", "const:4:8"]]
+ 0066a690 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a650 bytes 19050094
+ 0066a690 bytes 19050094
- 0066a67c ["INT_ADD", "register:40f0:8", ["const:66a67c:8", "const:4:8"]]
- 0066a67c ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a6bc ["INT_ADD", "register:40f0:8", ["const:66a6bc:8", "const:4:8"]]
+ 0066a6bc ["CALL", null, ["callee:0066baf4:8"]]
- 0066a67c bytes 0e050094
+ 0066a6bc bytes 0e050094
- 0066a75c ["INT_ADD", "register:40f0:8", ["const:66a75c:8", "const:4:8"]]
- 0066a75c ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a79c ["INT_ADD", "register:40f0:8", ["const:66a79c:8", "const:4:8"]]
+ 0066a79c ["CALL", null, ["callee:0066baf4:8"]]
- 0066a75c bytes d6040094
+ 0066a79c bytes d6040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4b0f2c5b478d2a3cf69c5ce2539b9f8"></a>

### [`0066a82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a82c.md) → [`0066a86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a86c.md) FUN_0066a86c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.21% / 新版 99.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066a8f4",
      "incomplete_value": false,
      "site": "0066a900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a8b4",
      "incomplete_value": false,
      "site": "0066a8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066a8f4",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0066a918",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066a8f4",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0066a918",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a82c.md#insn-0066a8c0) · [`0066a89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a82c.md#insn-0066a89c) · [`0066a8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a82c.md#insn-0066a8e0)
- 新版 `0066a900`（命令位置の公開資料なし） · `0066a8dc`（命令位置の公開資料なし） · `0066a920`（命令位置の公開資料なし）

~~~diff
- 0066a8c0 ["INT_ADD", "register:40f0:8", ["const:66a8c0:8", "const:4:8"]]
- 0066a8c0 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a900 ["INT_ADD", "register:40f0:8", ["const:66a900:8", "const:4:8"]]
+ 0066a900 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a8c0 bytes 7d040094
+ 0066a900 bytes 7d040094
- 0066a89c ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 0066a89c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0066a89c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0066a89c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0066a8dc ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 0066a8dc ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0066a8dc ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0066a8dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0066a89c bytes b5d61a91
+ 0066a8dc bytes b5d61b91
- 0066a8e0 ["INT_ADD", "register:40f0:8", ["const:66a8e0:8", "const:4:8"]]
- 0066a8e0 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066a920 ["INT_ADD", "register:40f0:8", ["const:66a920:8", "const:4:8"]]
+ 0066a920 ["CALL", null, ["callee:0066baf4:8"]]
- 0066a8e0 bytes 75040094
+ 0066a920 bytes 75040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb9ac819cbc3172bcc2da867bfbe04b8"></a>

### [`0066ac5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ac5c.md) → [`0066ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066ac9c.md) FUN_0066ac9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0066ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ae10.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0066ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066ae50.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066ace8",
      "incomplete_value": false,
      "site": "0066ad04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066aca8",
      "incomplete_value": false,
      "site": "0066acc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066ace8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0066ad58",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066ace8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0066ad58",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066acc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ac5c.md#insn-0066acc4) · [`0066ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ac5c.md#insn-0066ac90) · [`0066aca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066ac5c.md#insn-0066aca8)
- 新版 `0066ad04`（命令位置の公開資料なし） · `0066acd0`（命令位置の公開資料なし） · `0066ace8`（命令位置の公開資料なし）

~~~diff
- 0066acc4 ["INT_ADD", "register:40f0:8", ["const:66acc4:8", "const:4:8"]]
- 0066acc4 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066ad04 ["INT_ADD", "register:40f0:8", ["const:66ad04:8", "const:4:8"]]
+ 0066ad04 ["CALL", null, ["callee:0066baf4:8"]]
- 0066acc4 bytes 7c030094
+ 0066ad04 bytes 7c030094
- 0066ac90 ["INT_ADD", "register:40f0:8", ["const:66ac90:8", "const:4:8"]]
- 0066ac90 ["CALL", null, ["callee:0066a408:8"]]
+ 0066acd0 ["INT_ADD", "register:40f0:8", ["const:66acd0:8", "const:4:8"]]
+ 0066acd0 ["CALL", null, ["callee:0066a408:8"]]
- 0066ac90 bytes cefdff97
+ 0066acd0 bytes cefdff97
- 0066aca8 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 0066aca8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0066aca8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0066aca8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0066ace8 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 0066ace8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0066ace8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0066ace8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0066aca8 bytes 42d41a91
+ 0066ace8 bytes 42d41b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4b20231c4cabb049dafaea13e95847"></a>

### [`0066b02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b02c.md) → [`0066b06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b06c.md) FUN_0066b06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 3件 [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066b0c8",
      "incomplete_value": false,
      "site": "0066b0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066b088",
      "incomplete_value": false,
      "site": "0066b0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066b0c8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066b0c8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066b0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b02c.md#insn-0066b0a0) · [`0066b088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b02c.md#insn-0066b088) · [`0066b0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b02c.md#insn-0066b0b8)
- 新版 `0066b0e0`（命令位置の公開資料なし） · `0066b0c8`（命令位置の公開資料なし） · `0066b0f8`（命令位置の公開資料なし）

~~~diff
- 0066b0a0 ["INT_ADD", "register:40f0:8", ["const:66b0a0:8", "const:4:8"]]
- 0066b0a0 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066b0e0 ["INT_ADD", "register:40f0:8", ["const:66b0e0:8", "const:4:8"]]
+ 0066b0e0 ["CALL", null, ["callee:0066baf4:8"]]
- 0066b0a0 bytes 85020094
+ 0066b0e0 bytes 85020094
- 0066b088 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 0066b088 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0066b088 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0066b088 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0066b0c8 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 0066b0c8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0066b0c8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0066b0c8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0066b088 bytes 42d41a91
+ 0066b0c8 bytes 42d41b91
- 0066b0b8 ["INT_ADD", "register:40f0:8", ["const:66b0b8:8", "const:4:8"]]
- 0066b0b8 ["CALL", null, ["callee:00c58450:8"]]
+ 0066b0f8 ["INT_ADD", "register:40f0:8", ["const:66b0f8:8", "const:4:8"]]
+ 0066b0f8 ["CALL", null, ["callee:00c58450:8"]]
- 0066b0b8 bytes e6b31794
+ 0066b0f8 bytes d6b41794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-901377f172881674795381c38f7cb156"></a>

### [`0066b1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b1ac.md) → [`0066b1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b1ec.md) FUN_0066b1ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0066bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0066baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baf4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066b270",
      "incomplete_value": false,
      "site": "0066b288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066b230",
      "incomplete_value": false,
      "site": "0066b248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "0066b270",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066b270",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b1ac.md#insn-0066b248) · [`0066b230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b1ac.md#insn-0066b230) · [`0066b2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b1ac.md#insn-0066b2c0)
- 新版 `0066b288`（命令位置の公開資料なし） · `0066b270`（命令位置の公開資料なし） · `0066b300`（命令位置の公開資料なし）

~~~diff
- 0066b248 ["INT_ADD", "register:40f0:8", ["const:66b248:8", "const:4:8"]]
- 0066b248 ["CALL", null, ["callee:0066baf4:8"]]
+ 0066b288 ["INT_ADD", "register:40f0:8", ["const:66b288:8", "const:4:8"]]
+ 0066b288 ["CALL", null, ["callee:0066baf4:8"]]
- 0066b248 bytes 1b020094
+ 0066b288 bytes 1b020094
- 0066b230 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 0066b230 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0066b230 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0066b230 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0066b270 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 0066b270 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0066b270 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0066b270 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0066b230 bytes 42d41a91
+ 0066b270 bytes 42d41b91
- 0066b2c0 ["INT_ADD", "register:40f0:8", ["const:66b2c0:8", "const:4:8"]]
- 0066b2c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0066b300 ["INT_ADD", "register:40f0:8", ["const:66b300:8", "const:4:8"]]
+ 0066b300 ["CALL", null, ["callee:00c57e90:8"]]
- 0066b2c0 bytes f4b11794
+ 0066b300 bytes e4b21794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ce2b6949f7fa73cd2ba65c386c436c4"></a>

### [`0066b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md) → [`0066b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b5a0.md) FUN_0066b5a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0066a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md) [`0066b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0066a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a61c.md) [`0066b6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b6c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

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
      "site": "0066b6a8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066b668",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0066b6a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0066b6a8",
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

- 旧版 [`0066b668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md#insn-0066b668) · [`0066b578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md#insn-0066b578) · [`0066b588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md#insn-0066b588)
- 新版 `0066b6a8`（命令位置の公開資料なし） · `0066b5b8`（命令位置の公開資料なし） · `0066b5c8`（命令位置の公開資料なし）

~~~diff
- 0066b668 ["INT_ADD", "register:40f0:8", ["const:66b668:8", "const:4:8"]]
- 0066b668 ["CALL", null, ["ram:47acb4:8"]]
+ 0066b6a8 ["INT_ADD", "register:40f0:8", ["const:66b6a8:8", "const:4:8"]]
+ 0066b6a8 ["CALL", null, ["ram:47acf4:8"]]
- 0066b668 bytes 933df897
+ 0066b6a8 bytes 933df897
- 0066b578 ["INT_ADD", "register:40f0:8", ["const:66b578:8", "const:4:8"]]
- 0066b578 ["CALL", null, ["callee:00802b58:8"]]
+ 0066b5b8 ["INT_ADD", "register:40f0:8", ["const:66b5b8:8", "const:4:8"]]
+ 0066b5b8 ["CALL", null, ["callee:00802b58:8"]]
- 0066b578 bytes 685d0694
+ 0066b5b8 bytes 685d0694
- 0066b588 ["INT_ADD", "register:40f0:8", ["const:66b588:8", "const:4:8"]]
- 0066b588 ["CALL", null, ["callee:0066a61c:8"]]
+ 0066b5c8 ["INT_ADD", "register:40f0:8", ["const:66b5c8:8", "const:4:8"]]
+ 0066b5c8 ["CALL", null, ["callee:0066a61c:8"]]
- 0066b588 bytes 15fcff97
+ 0066b5c8 bytes 15fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e905523e1fe0e290971061e36d8d91e6"></a>

### [`0066b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md) → [`0066b6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b6c4.md) FUN_0066b6c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0066b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b560.md) · 呼出先 7件 [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`00af34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af34c8.md) [`00af3588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3588.md) [`00af399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af399c.md)
- 新版 呼出元 1件 [`0066b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b5a0.md) · 呼出先 7件 [`005e0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`00af38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af38f0.md) [`00af39b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af39b0.md) [`00af3dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3dc4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "site": "0066b738",
      "value": [
        "leaf",
        "ram:aff4a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066b6f8",
      "value": [
        "leaf",
        "ram:aff078:8"
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
      "0066b738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aff078"
      ]
    ]
  ],
  "added": [
    [
      "0066b738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aff4a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md#insn-0066b6f8) · [`0066b6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md#insn-0066b6ac) · [`0066b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b684.md#insn-0066b6bc)
- 新版 `0066b738`（命令位置の公開資料なし） · `0066b6ec`（命令位置の公開資料なし） · `0066b6fc`（命令位置の公開資料なし）

~~~diff
- 0066b6f8 ["INT_ADD", "register:40f0:8", ["const:66b6f8:8", "const:4:8"]]
- 0066b6f8 ["CALL", null, ["ram:aff078:8"]]
+ 0066b738 ["INT_ADD", "register:40f0:8", ["const:66b738:8", "const:4:8"]]
+ 0066b738 ["CALL", null, ["ram:aff4a0:8"]]
- 0066b6f8 bytes 604e1294
+ 0066b738 bytes 5a4f1294
- 0066b6ac ["INT_ADD", "register:40f0:8", ["const:66b6ac:8", "const:4:8"]]
- 0066b6ac ["CALL", null, ["callee:00af38f0:8"]]
+ 0066b6ec ["INT_ADD", "register:40f0:8", ["const:66b6ec:8", "const:4:8"]]
+ 0066b6ec ["CALL", null, ["callee:00af38f0:8"]]
- 0066b6ac bytes 871f1294
+ 0066b6ec bytes 81201294
- 0066b6bc ["INT_ADD", "register:40f0:8", ["const:66b6bc:8", "const:4:8"]]
- 0066b6bc ["CALL", null, ["callee:00af3dc4:8"]]
+ 0066b6fc ["INT_ADD", "register:40f0:8", ["const:66b6fc:8", "const:4:8"]]
+ 0066b6fc ["CALL", null, ["callee:00af3dc4:8"]]
- 0066b6bc bytes b8201294
+ 0066b6fc bytes b2211294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f81e71b1b1a50fef48383e0c44acd66"></a>

### [`0066bc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bc84.md) → [`0066bcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066bcc4.md) _INIT_88

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
      "definition_site": "0066bd00",
      "incomplete_value": true,
      "site": "0066bd1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066bcc0",
      "incomplete_value": true,
      "site": "0066bcdc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066bd24",
      "incomplete_value": true,
      "site": "0066bd40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066bce4",
      "incomplete_value": true,
      "site": "0066bd00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066bd44",
      "incomplete_value": true,
      "site": "0066bd60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0066bd04",
      "incomplete_value": true,
      "site": "0066bd20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0066bd00",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0066bd24",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0066bd44",
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
      "0066bd00",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0066bd24",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0066bd44",
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

- 旧版 [`0066bcfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bc84.md#insn-0066bcfc) · [`0066bd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bc84.md#insn-0066bd1c) · [`0066bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bc84.md#insn-0066bde4)
- 新版 `0066bd3c`（命令位置の公開資料なし） · `0066bd5c`（命令位置の公開資料なし） · `0066be24`（命令位置の公開資料なし）

~~~diff
- 0066bcfc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0066bcfc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0066bcfc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0066bcfc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0066bd3c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0066bd3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0066bd3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0066bd3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0066bcfc bytes 4a093691
+ 0066bd3c bytes 4a093791
- 0066bd1c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0066bd1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0066bd1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0066bd1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0066bd5c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0066bd5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0066bd5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0066bd5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0066bd1c bytes 4a553a91
+ 0066bd5c bytes 4a893d91
- 0066bde4 ["INT_ADD", "register:40f0:8", ["const:66bde4:8", "const:4:8"]]
- 0066bde4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0066be24 ["INT_ADD", "register:40f0:8", ["const:66be24:8", "const:4:8"]]
+ 0066be24 ["CALL", null, ["callee:0043b7f8:8"]]
- 0066bde4 bytes 753ef797
+ 0066be24 bytes 753ef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11440b74e9842617dc55820512b1b03b"></a>

### [`0066d0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0c8.md) → [`0066d108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d108.md) FUN_0066d108

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0066d0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0bc.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00b353c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b353c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0066d0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0fc.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00b357e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b35/00b357e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066d2f8",
      "incomplete_value": false,
      "site": "0066d300",
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
            "const:f39:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d2b8",
      "incomplete_value": false,
      "site": "0066d2c0",
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
            "const:e6c:8"
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
      "definition_site": "0066d33c",
      "incomplete_value": false,
      "site": "0066d344",
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
            "const:fc7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d2fc",
      "incomplete_value": false,
      "site": "0066d304",
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
            "const:efa:8"
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
      "0066d1a4",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ],
    [
      "0066d1b4",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "0066d1c0",
      "PARAM",
      [
        "storage",
        "002ad9a4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0066d1a4",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ],
    [
      "0066d1b4",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "0066d1c0",
      "PARAM",
      [
        "storage",
        "002ad9e4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0c8.md#insn-0066d280) · [`0066d2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0c8.md#insn-0066d2c0) · [`0066d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d0c8.md#insn-0066d304)
- 新版 `0066d2c0`（命令位置の公開資料なし） · `0066d300`（命令位置の公開資料なし） · `0066d344`（命令位置の公開資料なし）

~~~diff
- 0066d280 ["INT_ADD", "register:40f0:8", ["const:66d280:8", "const:4:8"]]
- 0066d280 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0066d2c0 ["INT_ADD", "register:40f0:8", ["const:66d2c0:8", "const:4:8"]]
+ 0066d2c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0066d280 bytes 0caa1794
+ 0066d2c0 bytes fcaa1794
- 0066d2c0 ["INT_ADD", "register:40f0:8", ["const:66d2c0:8", "const:4:8"]]
- 0066d2c0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0066d300 ["INT_ADD", "register:40f0:8", ["const:66d300:8", "const:4:8"]]
+ 0066d300 ["CALL", null, ["callee:00c57f70:8"]]
- 0066d2c0 bytes 2caa1794
+ 0066d300 bytes 1cab1794
- 0066d304 ["INT_ADD", "register:40f0:8", ["const:66d304:8", "const:4:8"]]
- 0066d304 ["CALL", null, ["callee:00c57f70:8"]]
+ 0066d344 ["INT_ADD", "register:40f0:8", ["const:66d344:8", "const:4:8"]]
+ 0066d344 ["CALL", null, ["callee:00c57f70:8"]]
- 0066d304 bytes 1baa1794
+ 0066d344 bytes 0bab1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf3d01234245bd87b6ef3826b043312"></a>

### [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) → [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) FUN_0066d6a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 38件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)
- 新版 呼出元 2件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 38件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 34件, `call_target` 4件, `store_destination` 25件, `store_value` 15件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0066d6e8",
      "incomplete_value": false,
      "site": "0066d6e8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d6a8",
      "incomplete_value": false,
      "site": "0066d6a8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066d6e0",
      "incomplete_value": true,
      "site": "0066d6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d6a0",
      "incomplete_value": true,
      "site": "0066d6a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0066d6ec",
      "incomplete_value": false,
      "site": "0066d6ec",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d6ac",
      "incomplete_value": false,
      "site": "0066d6ac",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066d6e0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0066d6e4",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "0066d6e8",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0066d6e0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0066d6e4",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "0066d6e8",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md#insn-0066d6a8) · [`0066d6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md#insn-0066d6ac) · [`0066d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md#insn-0066d6d4)
- 新版 `0066d6e8`（命令位置の公開資料なし） · `0066d6ec`（命令位置の公開資料なし） · `0066d714`（命令位置の公開資料なし）

~~~diff
- 0066d6a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 0066d6a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0066d6e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 0066d6e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0066d6a8 bytes 09b502f9
+ 0066d6e8 bytes 09b504f9
- 0066d6ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
- 0066d6ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0066d6ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 0066d6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0066d6ac bytes 6abe02f9
+ 0066d6ec bytes 6abe04f9
- 0066d6d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
- 0066d6d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0066d714 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 0066d714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0066d6d4 bytes 74be02f9
+ 0066d714 bytes 74be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79c59de17f2dcfe84441e90a33102f09"></a>

### [`0066e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066e/0066e910.md) → [`0066e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066e/0066e950.md) FUN_0066e950

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · 呼出先 24件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e738.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)
- 新版 呼出元 1件 [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) · 呼出先 24件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e778.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.07% / 新版 86.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `store_destination` 21件, `store_value` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066e9e4",
      "incomplete_value": true,
      "site": "0066e9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:622:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e9a4",
      "incomplete_value": true,
      "site": "0066e9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e2:8"
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
      "definition_site": "0066e9e8",
      "incomplete_value": true,
      "site": "0066e9e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0066e9a8",
      "incomplete_value": true,
      "site": "0066e9a8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066ea2c",
      "incomplete_value": true,
      "site": "0066ea48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e9ec",
      "incomplete_value": true,
      "site": "0066ea08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d62:8"
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
      "0066e980",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0066e990",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066e998",
      "PARAM",
      [
        "storage",
        "00c74238",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0066e980",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0066e990",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066e998",
      "PARAM",
      [
        "storage",
        "00c74638",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066e/0066e910.md#insn-0066e964) · [`0066e9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066e/0066e910.md#insn-0066e9e4) · [`0066eaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066e/0066e910.md#insn-0066eaf8)
- 新版 `0066e9a4`（命令位置の公開資料なし） · `0066ea24`（命令位置の公開資料なし） · `0066eb38`（命令位置の公開資料なし）

~~~diff
- 0066e964 ["INT_ADD", "register:40f0:8", ["const:66e964:8", "const:4:8"]]
- 0066e964 ["CALL", null, ["callee:00c58610:8"]]
+ 0066e9a4 ["INT_ADD", "register:40f0:8", ["const:66e9a4:8", "const:4:8"]]
+ 0066e9a4 ["CALL", null, ["callee:00c58610:8"]]
- 0066e964 bytes 2ba61794
+ 0066e9a4 bytes 1ba71794
- 0066e9e4 ["COPY", "tmp:0:8", ["const:d62:8"]]
- 0066e9e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066ea24 ["COPY", "tmp:0:8", ["const:da2:8"]]
+ 0066ea24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ea24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ea24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e9e4 bytes 08893591
+ 0066ea24 bytes 08893691
- 0066eaf8 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0066eaf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066eaf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066eaf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066eb38 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0066eb38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066eb38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066eb38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066eaf8 bytes 08e12c91
+ 0066eb38 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e14ab6412f4d1b7ea87ea13adefa262b"></a>

### [`0066f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md) → [`0066f838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066f838.md) FUN_0066f838

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) [`0066ff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md) · 呼出先 15件 [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md)
- 新版 呼出元 2件 [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) [`0066ff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066ff74.md) · 呼出先 15件 [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.03% / 新版 89.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 8件, `store_value` 4件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0066f8dc",
      "incomplete_value": false,
      "site": "0066f8dc",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066f89c",
      "incomplete_value": false,
      "site": "0066f89c",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066fa58",
      "incomplete_value": true,
      "site": "0066fa68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066fa18",
      "incomplete_value": true,
      "site": "0066fa28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d51:8"
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
      "definition_site": "0066fab0",
      "incomplete_value": true,
      "site": "0066fac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066fa70",
      "incomplete_value": true,
      "site": "0066fa88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1:8"
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
      "0066f874",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0066f880",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066f888",
      "PARAM",
      [
        "storage",
        "00c74238",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0066f874",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0066f880",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066f888",
      "PARAM",
      [
        "storage",
        "00c74638",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066f854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md#insn-0066f854) · [`0066f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md#insn-0066f878) · [`0066f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md#insn-0066f89c)
- 新版 `0066f894`（命令位置の公開資料なし） · `0066f8b8`（命令位置の公開資料なし） · `0066f8dc`（命令位置の公開資料なし）

~~~diff
- 0066f854 ["INT_ADD", "register:40f0:8", ["const:66f854:8", "const:4:8"]]
- 0066f854 ["CALL", null, ["callee:00c58610:8"]]
+ 0066f894 ["INT_ADD", "register:40f0:8", ["const:66f894:8", "const:4:8"]]
+ 0066f894 ["CALL", null, ["callee:00c58610:8"]]
- 0066f854 bytes 6fa21794
+ 0066f894 bytes 5fa31794
- 0066f878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa0:8"]]
- 0066f878 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0066f878 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 0066f8b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0066f8b8 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0066f8b8 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 0066f878 bytes 08a14ab9
+ 0066f8b8 bytes 08a14eb9
- 0066f89c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:aa0:8"]]
- 0066f89c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0066f8dc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ea0:8"]]
+ 0066f8dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0066f89c bytes 8ba10ab9
+ 0066f8dc bytes 8ba10eb9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8998c3753596366a5ae7664d059b49"></a>

### [`0066ff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md) → [`0066ff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066ff74.md) FUN_0066ff74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 20件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0066f7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066f7f8.md) [`00672d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d80.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 20件 [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0066f838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066f/0066f838.md) [`00672dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672dc0.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.68% / 新版 96.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00670098",
      "incomplete_value": false,
      "site": "006700a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670058",
      "incomplete_value": false,
      "site": "00670064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "definition_site": "00670208",
      "incomplete_value": false,
      "site": "00670210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006701c8",
      "incomplete_value": false,
      "site": "006701d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00670020",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066ffe0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00670020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00670084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006700a4",
      "DATA",
      [
        "storage",
        "00c742a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00670084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006700a4",
      "DATA",
      [
        "storage",
        "00c746a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ffe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md#insn-0066ffe0) · [`00670044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md#insn-00670044) · [`0067045c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066f/0066ff34.md#insn-0067045c)
- 新版 `00670020`（命令位置の公開資料なし） · `00670084`（命令位置の公開資料なし） · `0067049c`（命令位置の公開資料なし）

~~~diff
- 0066ffe0 ["INT_ADD", "register:40f0:8", ["const:66ffe0:8", "const:4:8"]]
- 0066ffe0 ["CALL", null, ["ram:47acb4:8"]]
+ 00670020 ["INT_ADD", "register:40f0:8", ["const:670020:8", "const:4:8"]]
+ 00670020 ["CALL", null, ["ram:47acf4:8"]]
- 0066ffe0 bytes 352bf897
+ 00670020 bytes 352bf897
- 00670044 ["INT_ADD", "register:40f0:8", ["const:670044:8", "const:4:8"]]
- 00670044 ["CALL", null, ["ram:47acb4:8"]]
+ 00670084 ["INT_ADD", "register:40f0:8", ["const:670084:8", "const:4:8"]]
+ 00670084 ["CALL", null, ["ram:47acf4:8"]]
- 00670044 bytes 1c2bf897
+ 00670084 bytes 1c2bf897
- 0067045c ["INT_ADD", "register:40f0:8", ["const:67045c:8", "const:4:8"]]
- 0067045c ["CALL", null, ["ram:47acb4:8"]]
+ 0067049c ["INT_ADD", "register:40f0:8", ["const:67049c:8", "const:4:8"]]
+ 0067049c ["CALL", null, ["ram:47acf4:8"]]
- 0067045c bytes 162af897
+ 0067049c bytes 162af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc40bc571e9e4b075f317de3cd656b4d"></a>

### [`006706ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00670/006706ac.md) → [`006706ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00670/006706ec.md) FUN_006706ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 23件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 23件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 25件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00670724",
      "incomplete_value": true,
      "site": "00670724",
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
      "definition_site": "006706e4",
      "incomplete_value": true,
      "site": "006706e4",
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
      "definition_site": "00670730",
      "incomplete_value": false,
      "site": "00670744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006706f0",
      "incomplete_value": false,
      "site": "00670704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00670738",
      "incomplete_value": false,
      "site": "00670744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006706f8",
      "incomplete_value": false,
      "site": "00670704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "00670720",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00670730",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00670738",
      "PARAM",
      [
        "storage",
        "00c74238",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00670720",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00670730",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00670738",
      "PARAM",
      [
        "storage",
        "00c74638",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00670/006706ac.md#insn-00670704) · [`0067078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00670/006706ac.md#insn-0067078c) · [`006707d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00670/006706ac.md#insn-006707d0)
- 新版 `00670744`（命令位置の公開資料なし） · `006707cc`（命令位置の公開資料なし） · `00670810`（命令位置の公開資料なし）

~~~diff
- 00670704 ["INT_ADD", "register:40f0:8", ["const:670704:8", "const:4:8"]]
- 00670704 ["CALL", null, ["callee:00c58610:8"]]
+ 00670744 ["INT_ADD", "register:40f0:8", ["const:670744:8", "const:4:8"]]
+ 00670744 ["CALL", null, ["callee:00c58610:8"]]
- 00670704 bytes c39e1794
+ 00670744 bytes b39f1794
- 0067078c ["INT_ADD", "register:40f0:8", ["const:67078c:8", "const:4:8"]]
- 0067078c ["CALL", null, ["ram:46c984:8"]]
+ 006707cc ["INT_ADD", "register:40f0:8", ["const:6707cc:8", "const:4:8"]]
+ 006707cc ["CALL", null, ["ram:46c9c4:8"]]
- 0067078c bytes 7ef0f797
+ 006707cc bytes 7ef0f797
- 006707d0 ["INT_ADD", "register:40f0:8", ["const:6707d0:8", "const:4:8"]]
- 006707d0 ["CALL", null, ["ram:46c984:8"]]
+ 00670810 ["INT_ADD", "register:40f0:8", ["const:670810:8", "const:4:8"]]
+ 00670810 ["CALL", null, ["ram:46c9c4:8"]]
- 006707d0 bytes 6df0f797
+ 00670810 bytes 6df0f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aae2af60a5664fb1cae8c7dabb7a8ad"></a>

### [`0067146c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00671/0067146c.md) → [`006714ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00671/006714ac.md) FUN_006714ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) · 呼出先 22件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) · 呼出先 22件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.84% / 新版 89.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `store_destination` 2件, `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006714f0",
      "incomplete_value": false,
      "site": "006714f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006714b0",
      "incomplete_value": false,
      "site": "006714b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067158c",
      "incomplete_value": true,
      "site": "0067158c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067154c",
      "incomplete_value": true,
      "site": "0067154c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006716c4",
      "incomplete_value": true,
      "site": "006716c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fbe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671684",
      "incomplete_value": true,
      "site": "00671684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f7e:8"
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
      "006714f8",
      "DATA",
      [
        "storage",
        "00c74260",
        null,
        "pointer"
      ]
    ],
    [
      "00671544",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00671558",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006714f8",
      "DATA",
      [
        "storage",
        "00c74660",
        null,
        "pointer"
      ]
    ],
    [
      "00671544",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00671558",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00671/0067146c.md#insn-00671840) · [`006718e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00671/0067146c.md#insn-006718e0) · [`00671a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00671/0067146c.md#insn-00671a24)
- 新版 `00671880`（命令位置の公開資料なし） · `00671920`（命令位置の公開資料なし） · `00671a64`（命令位置の公開資料なし）

~~~diff
- 00671840 ["INT_ADD", "register:40f0:8", ["const:671840:8", "const:4:8"]]
- 00671840 ["CALL", null, ["callee:00c53d00:8"]]
+ 00671880 ["INT_ADD", "register:40f0:8", ["const:671880:8", "const:4:8"]]
+ 00671880 ["CALL", null, ["callee:00c53d00:8"]]
- 00671840 bytes 28881794
+ 00671880 bytes 20891794
- 006718e0 ["COPY", "tmp:0:8", ["const:11f:8"]]
- 006718e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006718e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006718e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00671920 ["COPY", "tmp:0:8", ["const:15f:8"]]
+ 00671920 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00671920 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00671920 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006718e0 bytes 297d0491
+ 00671920 bytes 297d0591
- 00671a24 ["INT_ADD", "register:40f0:8", ["const:671a24:8", "const:4:8"]]
- 00671a24 ["CALL", null, ["callee:0047e60c:8"]]
+ 00671a64 ["INT_ADD", "register:40f0:8", ["const:671a64:8", "const:4:8"]]
+ 00671a64 ["CALL", null, ["callee:0047e60c:8"]]
- 00671a24 bytes ea32f897
+ 00671a64 bytes ea32f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d55886c71689c4c5f3fa5b5fdd5d4f84"></a>

### [`006728c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md) → [`00672904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672904.md) FUN_00672904

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00672ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672ae4.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d4c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00672b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b24.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067291c",
      "incomplete_value": true,
      "site": "00672920",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006728dc",
      "incomplete_value": true,
      "site": "006728e0",
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
            "const:260:8"
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
      "00672920",
      "DATA",
      [
        "storage",
        "00c74260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00672920",
      "DATA",
      [
        "storage",
        "00c74660",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006728dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md#insn-006728dc) · [`006728e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md#insn-006728e4) · [`006728e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md#insn-006728e8)
- 新版 `0067291c`（命令位置の公開資料なし） · `00672924`（命令位置の公開資料なし） · `00672928`（命令位置の公開資料なし）

~~~diff
- 006728dc ["COPY", "tmp:0:8", ["const:260:8"]]
- 006728dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006728dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006728dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067291c ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0067291c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067291c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067291c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006728dc bytes 08810991
+ 0067291c bytes 08811991
- 006728e4 ["INT_ADD", "register:40f0:8", ["const:6728e4:8", "const:4:8"]]
- 006728e4 ["CALL", null, ["callee:00467860:8"]]
+ 00672924 ["INT_ADD", "register:40f0:8", ["const:672924:8", "const:4:8"]]
+ 00672924 ["CALL", null, ["callee:00467860:8"]]
- 006728e4 bytes cfd3f797
+ 00672924 bytes cfd3f797
- 006728e8 ["INT_ADD", "register:40f0:8", ["const:6728e8:8", "const:4:8"]]
- 006728e8 ["CALL", null, ["callee:00467d8c:8"]]
+ 00672928 ["INT_ADD", "register:40f0:8", ["const:672928:8", "const:4:8"]]
+ 00672928 ["CALL", null, ["callee:00467d8c:8"]]
- 006728e8 bytes 19d5f797
+ 00672928 bytes 19d5f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d665e48dc370b5e91dd689e4cfa3408"></a>

### [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) → [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) FUN_00672b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`006728c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md) [`00672d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d24.md) [`0067b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b7b4.md) [`0067b8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b8a0.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 12件 [`00672904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672904.md) [`00672d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672d64.md) [`0067b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067b7f4.md) [`0067b8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067b8e0.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00672b60",
      "incomplete_value": false,
      "site": "00672b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672b20",
      "incomplete_value": false,
      "site": "00672b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00672b64",
      "DATA",
      [
        "storage",
        "00c74280",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00672b64",
      "DATA",
      [
        "storage",
        "00c74680",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md#insn-00672b64) · [`00672b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md#insn-00672b20) · [`00672b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md#insn-00672b34)
- 新版 `00672ba4`（命令位置の公開資料なし） · `00672b60`（命令位置の公開資料なし） · `00672b74`（命令位置の公開資料なし）

~~~diff
- 00672b64 ["INT_ADD", "register:40f0:8", ["const:672b64:8", "const:4:8"]]
- 00672b64 ["CALL", null, ["callee:00c53d00:8"]]
+ 00672ba4 ["INT_ADD", "register:40f0:8", ["const:672ba4:8", "const:4:8"]]
+ 00672ba4 ["CALL", null, ["callee:00c53d00:8"]]
- 00672b64 bytes 5f831794
+ 00672ba4 bytes 57841794
- 00672b20 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00672b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672b60 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00672b60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672b60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672b60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672b20 bytes 08010a91
+ 00672b60 bytes 08011a91
- 00672b34 ["INT_ADD", "register:40f0:8", ["const:672b34:8", "const:4:8"]]
- 00672b34 ["CALL", null, ["callee:00c53d00:8"]]
+ 00672b74 ["INT_ADD", "register:40f0:8", ["const:672b74:8", "const:4:8"]]
+ 00672b74 ["CALL", null, ["callee:00c53d00:8"]]
- 00672b34 bytes 6b831794
+ 00672b74 bytes 63841794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fbf80b653f908c94180f85569472ed"></a>

### [`00672d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d4c.md) → [`00672d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672d8c.md) FUN_00672d8c

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
      "definition_site": "00672da0",
      "incomplete_value": false,
      "site": "00672da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672d60",
      "incomplete_value": false,
      "site": "00672d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "00672da4",
      "DATA",
      [
        "storage",
        "00c742a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672da4",
      "DATA",
      [
        "storage",
        "00c746a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d4c.md#insn-00672d58) · [`00672d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d4c.md#insn-00672d60)
- 新版 `00672d98`（命令位置の公開資料なし） · `00672da0`（命令位置の公開資料なし）

~~~diff
- 00672d58 ["INT_ADD", "register:40f0:8", ["const:672d58:8", "const:4:8"]]
- 00672d58 ["CALL", null, ["callee:00c57e90:8"]]
+ 00672d98 ["INT_ADD", "register:40f0:8", ["const:672d98:8", "const:4:8"]]
+ 00672d98 ["CALL", null, ["callee:00c57e90:8"]]
- 00672d58 bytes 4e931794
+ 00672d98 bytes 3e941794
- 00672d60 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00672d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672da0 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00672da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672d60 bytes 08810a91
+ 00672da0 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a936c2267890526d34aab51514d1d491"></a>

### [`00672d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d70.md) → [`00672db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672db0.md) FUN_00672db0

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
      "definition_site": "00672db4",
      "incomplete_value": false,
      "site": "00672db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672d74",
      "incomplete_value": false,
      "site": "00672d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "00672db8",
      "DATA",
      [
        "storage",
        "00c742a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672db8",
      "DATA",
      [
        "storage",
        "00c746a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d70.md#insn-00672d74)
- 新版 `00672db4`（命令位置の公開資料なし）

~~~diff
- 00672d74 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00672d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672db4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00672db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672d74 bytes 08810a91
+ 00672db4 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34ec710becc0b60585d4ab99fd505856"></a>

### [`00672d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d88.md) → [`00672dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672dc8.md) FUN_00672dc8

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
      "site": "00672dec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00672dac",
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
      "00672dec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00672dec",
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

- 旧版 [`00672dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d88.md#insn-00672dac) · [`00672db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d88.md#insn-00672db8)
- 新版 `00672dec`（命令位置の公開資料なし） · `00672df8`（命令位置の公開資料なし）

~~~diff
- 00672dac ["INT_ADD", "register:40f0:8", ["const:672dac:8", "const:4:8"]]
- 00672dac ["CALL", null, ["ram:47acb4:8"]]
+ 00672dec ["INT_ADD", "register:40f0:8", ["const:672dec:8", "const:4:8"]]
+ 00672dec ["CALL", null, ["ram:47acf4:8"]]
- 00672dac bytes c21ff897
+ 00672dec bytes c21ff897
- 00672db8 ["INT_ADD", "register:40f0:8", ["const:672db8:8", "const:4:8"]]
- 00672db8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00672df8 ["INT_ADD", "register:40f0:8", ["const:672df8:8", "const:4:8"]]
+ 00672df8 ["CALL", null, ["callee:0047cdd4:8"]]
- 00672db8 bytes f727f897
+ 00672df8 bytes f727f897
~~~


<a id="compare-529105aa9c00aafe9835cf4e665b5445"></a>

### [`00672dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672dfc.md) → [`00672e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672e3c.md) FUN_00672e3c

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
      "definition_site": "00672e50",
      "incomplete_value": false,
      "site": "00672e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672e10",
      "incomplete_value": false,
      "site": "00672e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "00672e54",
      "DATA",
      [
        "storage",
        "00c74320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672e54",
      "DATA",
      [
        "storage",
        "00c74720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672dfc.md#insn-00672e08) · [`00672e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672dfc.md#insn-00672e10)
- 新版 `00672e48`（命令位置の公開資料なし） · `00672e50`（命令位置の公開資料なし）

~~~diff
- 00672e08 ["INT_ADD", "register:40f0:8", ["const:672e08:8", "const:4:8"]]
- 00672e08 ["CALL", null, ["callee:00c57e90:8"]]
+ 00672e48 ["INT_ADD", "register:40f0:8", ["const:672e48:8", "const:4:8"]]
+ 00672e48 ["CALL", null, ["callee:00c57e90:8"]]
- 00672e08 bytes 22931794
+ 00672e48 bytes 12941794
- 00672e10 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00672e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672e50 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00672e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672e10 bytes 08810c91
+ 00672e50 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f452331c4eec842fd60edc947204c0ea"></a>

### [`00672e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e20.md) → [`00672e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672e60.md) FUN_00672e60

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
      "definition_site": "00672e64",
      "incomplete_value": false,
      "site": "00672e68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672e24",
      "incomplete_value": false,
      "site": "00672e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "00672e68",
      "DATA",
      [
        "storage",
        "00c74320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672e68",
      "DATA",
      [
        "storage",
        "00c74720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e20.md#insn-00672e24)
- 新版 `00672e64`（命令位置の公開資料なし）

~~~diff
- 00672e24 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00672e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672e64 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00672e64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672e64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672e64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672e24 bytes 08810c91
+ 00672e64 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-727560e41903e6546f6d53f8d3514ffd"></a>

### [`00672e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e38.md) → [`00672e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672e78.md) FUN_00672e78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00672ec0",
      "incomplete_value": true,
      "site": "00672ec0",
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
      "definition_site": "00672e80",
      "incomplete_value": true,
      "site": "00672e80",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00672ec8",
      "incomplete_value": false,
      "site": "00672ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672e88",
      "incomplete_value": false,
      "site": "00672e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00672ed0",
      "incomplete_value": false,
      "site": "00672ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672e90",
      "incomplete_value": false,
      "site": "00672e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "00672ebc",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00672ec8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672ed0",
      "PARAM",
      [
        "storage",
        "00c74238",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00672ebc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00672ec8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672ed0",
      "PARAM",
      [
        "storage",
        "00c74638",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e38.md#insn-00672e88) · [`00672e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e38.md#insn-00672e98) · [`00672ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672e38.md#insn-00672ec8)
- 新版 `00672ec8`（命令位置の公開資料なし） · `00672ed8`（命令位置の公開資料なし） · `00672f08`（命令位置の公開資料なし）

~~~diff
- 00672e88 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00672e88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00672e88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00672e88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00672ec8 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00672ec8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00672ec8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00672ec8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00672e88 bytes 21602991
+ 00672ec8 bytes 21603991
- 00672e98 ["INT_ADD", "register:40f0:8", ["const:672e98:8", "const:4:8"]]
- 00672e98 ["CALL", null, ["callee:00c58610:8"]]
+ 00672ed8 ["INT_ADD", "register:40f0:8", ["const:672ed8:8", "const:4:8"]]
+ 00672ed8 ["CALL", null, ["callee:00c58610:8"]]
- 00672e98 bytes de941794
+ 00672ed8 bytes ce951794
- 00672ec8 ["INT_ADD", "register:40f0:8", ["const:672ec8:8", "const:4:8"]]
- 00672ec8 ["CALL", null, ["ram:46c984:8"]]
+ 00672f08 ["INT_ADD", "register:40f0:8", ["const:672f08:8", "const:4:8"]]
+ 00672f08 ["CALL", null, ["ram:46c9c4:8"]]
- 00672ec8 bytes afe6f797
+ 00672f08 bytes afe6f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5cb7ae86c8cb01ca41980af84bfb80"></a>

### [`00673370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673370.md) → [`006733b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00673/006733b0.md) _INIT_90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006733ec",
      "incomplete_value": true,
      "site": "00673408",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006733ac",
      "incomplete_value": true,
      "site": "006733c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673430",
      "incomplete_value": true,
      "site": "0067344c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006733f0",
      "incomplete_value": true,
      "site": "0067340c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067346c",
      "incomplete_value": true,
      "site": "00673488",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067342c",
      "incomplete_value": true,
      "site": "00673448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:592:8"
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
      "006733ec",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00673410",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00673430",
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
      "006733ec",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00673410",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00673430",
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

- 旧版 [`00673408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673370.md#insn-00673408) · [`006735a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673370.md#insn-006735a4) · [`0067339c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673370.md#insn-0067339c)
- 新版 `00673448`（命令位置の公開資料なし） · `006735e4`（命令位置の公開資料なし） · `006733dc`（命令位置の公開資料なし）

~~~diff
- 00673408 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00673408 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673408 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673408 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00673448 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00673448 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00673448 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00673448 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673408 bytes 4a553a91
+ 00673448 bytes 4a893d91
- 006735a4 ["INT_ADD", "register:40f0:8", ["const:6735a4:8", "const:4:8"]]
- 006735a4 ["CALL", null, ["callee:00c57e30:8"]]
+ 006735e4 ["INT_ADD", "register:40f0:8", ["const:6735e4:8", "const:4:8"]]
+ 006735e4 ["CALL", null, ["callee:00c57e30:8"]]
- 006735a4 bytes 23911794
+ 006735e4 bytes 13921794
- 0067339c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 0067339c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0067339c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0067339c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006733dc ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 006733dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006733dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006733dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0067339c bytes 73c20691
+ 006733dc bytes 73c21691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d9228513dc33987a9aa8c828c233481"></a>

### [`00673700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673700.md) → [`00673740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00673/00673740.md) _INIT_91

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006737a0",
      "incomplete_value": true,
      "site": "006737bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673760",
      "incomplete_value": true,
      "site": "0067377c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006737e0",
      "incomplete_value": true,
      "site": "006737f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006737a0",
      "incomplete_value": true,
      "site": "006737b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "definition_site": "006737fc",
      "incomplete_value": true,
      "site": "00673818",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006737bc",
      "incomplete_value": true,
      "site": "006737d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:592:8"
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
      "0067377c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006737a0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006737c0",
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
      "0067377c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006737a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006737c0",
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

- 旧版 [`00673778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673700.md#insn-00673778) · [`00673798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673700.md#insn-00673798) · [`00673934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673700.md#insn-00673934)
- 新版 `006737b8`（命令位置の公開資料なし） · `006737d8`（命令位置の公開資料なし） · `00673974`（命令位置の公開資料なし）

~~~diff
- 00673778 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00673778 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673778 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673778 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006737b8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006737b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006737b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006737b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673778 bytes 4a093691
+ 006737b8 bytes 4a093791
- 00673798 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00673798 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673798 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673798 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006737d8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006737d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006737d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006737d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673798 bytes 4a553a91
+ 006737d8 bytes 4a893d91
- 00673934 ["INT_ADD", "register:40f0:8", ["const:673934:8", "const:4:8"]]
- 00673934 ["CALL", null, ["callee:00c57e30:8"]]
+ 00673974 ["INT_ADD", "register:40f0:8", ["const:673974:8", "const:4:8"]]
+ 00673974 ["CALL", null, ["callee:00c57e30:8"]]
- 00673934 bytes 3f901794
+ 00673974 bytes 2f911794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbcca23811bfc32d9ca82e6475d49f9e"></a>

### [`00673a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673a90.md) → [`00673ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00673/00673ad0.md) _INIT_92

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00673b70",
      "incomplete_value": true,
      "site": "00673b88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673b30",
      "incomplete_value": true,
      "site": "00673b48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "definition_site": "00673b8c",
      "incomplete_value": true,
      "site": "00673ba8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673b4c",
      "incomplete_value": true,
      "site": "00673b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:592:8"
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
      "definition_site": "00673cf0",
      "incomplete_value": false,
      "site": "00673d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673cb0",
      "incomplete_value": false,
      "site": "00673cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00673b0c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00673b30",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00673b50",
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
      "00673b0c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00673b30",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00673b50",
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

- 旧版 [`00673b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673a90.md#insn-00673b08) · [`00673b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673a90.md#insn-00673b28) · [`00673cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673a90.md#insn-00673cc4)
- 新版 `00673b48`（命令位置の公開資料なし） · `00673b68`（命令位置の公開資料なし） · `00673d04`（命令位置の公開資料なし）

~~~diff
- 00673b08 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00673b08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673b08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673b08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00673b48 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00673b48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00673b48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00673b48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673b08 bytes 4a093691
+ 00673b48 bytes 4a093791
- 00673b28 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00673b28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673b28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673b28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00673b68 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00673b68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00673b68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00673b68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673b28 bytes 4a553a91
+ 00673b68 bytes 4a893d91
- 00673cc4 ["INT_ADD", "register:40f0:8", ["const:673cc4:8", "const:4:8"]]
- 00673cc4 ["CALL", null, ["callee:00c57e30:8"]]
+ 00673d04 ["INT_ADD", "register:40f0:8", ["const:673d04:8", "const:4:8"]]
+ 00673d04 ["CALL", null, ["callee:00c57e30:8"]]
- 00673cc4 bytes 5b8f1794
+ 00673d04 bytes 4b901794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a48d8b5dbe9258a1c809b633d68d1a3"></a>

### [`00673e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673e20.md) → [`00673e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00673/00673e60.md) _INIT_93

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00673e9c",
      "incomplete_value": true,
      "site": "00673eb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673e5c",
      "incomplete_value": true,
      "site": "00673e78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673ee0",
      "incomplete_value": true,
      "site": "00673efc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00673ea0",
      "incomplete_value": true,
      "site": "00673ebc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00673f5c",
      "incomplete_value": true,
      "site": "00673fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673f1c",
      "incomplete_value": true,
      "site": "00673f60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3c:8"
              ]
            ]
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
      "00673e9c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00673ec0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00673ee0",
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
      "00673e9c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00673ec0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00673ee0",
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

- 旧版 [`00673eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673e20.md#insn-00673eb8) · [`00674054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673e20.md#insn-00674054) · [`00673e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00673/00673e20.md#insn-00673e4c)
- 新版 `00673ef8`（命令位置の公開資料なし） · `00674094`（命令位置の公開資料なし） · `00673e8c`（命令位置の公開資料なし）

~~~diff
- 00673eb8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00673eb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00673eb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00673eb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00673ef8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00673ef8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00673ef8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00673ef8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00673eb8 bytes 4a553a91
+ 00673ef8 bytes 4a893d91
- 00674054 ["INT_ADD", "register:40f0:8", ["const:674054:8", "const:4:8"]]
- 00674054 ["CALL", null, ["callee:00c57e30:8"]]
+ 00674094 ["INT_ADD", "register:40f0:8", ["const:674094:8", "const:4:8"]]
+ 00674094 ["CALL", null, ["callee:00c57e30:8"]]
- 00674054 bytes 778e1794
+ 00674094 bytes 678f1794
- 00673e4c ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00673e4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00673e4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00673e4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00673e8c ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00673e8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00673e8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00673e8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00673e4c bytes 73e20791
+ 00673e8c bytes 73e21791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c8775f677a9b5671de601f2dd70a355"></a>

### [`006743e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006743e8.md) → [`00674428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674428.md) FUN_00674428

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`006741b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006741b0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`006741f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/006741f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00674460",
      "incomplete_value": false,
      "site": "0067446c",
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
      "definition_site": "00674420",
      "incomplete_value": false,
      "site": "0067442c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00674494",
      "incomplete_value": true,
      "site": "006744a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00674454",
      "incomplete_value": true,
      "site": "00674464",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:66f:8"
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
      "definition_site": "00674498",
      "incomplete_value": true,
      "site": "006744a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00674458",
      "incomplete_value": true,
      "site": "00674468",
      "value": [
        "LOAD",
        "8",
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
      "0067446c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00674494",
      "READ",
      [
        "storage",
        "002bb66f",
        null,
        "string"
      ]
    ],
    [
      "00674498",
      "READ",
      [
        "storage",
        "002bb67f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067446c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00674494",
      "READ",
      [
        "storage",
        "002bb6af",
        null,
        "string"
      ]
    ],
    [
      "00674498",
      "READ",
      [
        "storage",
        "002bb6bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00674414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006743e8.md#insn-00674414) · [`00674420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006743e8.md#insn-00674420) · [`00674430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006743e8.md#insn-00674430)
- 新版 `00674454`（命令位置の公開資料なし） · `00674460`（命令位置の公開資料なし） · `00674470`（命令位置の公開資料なし）

~~~diff
- 00674414 ["INT_ADD", "register:40f0:8", ["const:674414:8", "const:4:8"]]
- 00674414 ["CALL", null, ["callee:00487e20:8"]]
+ 00674454 ["INT_ADD", "register:40f0:8", ["const:674454:8", "const:4:8"]]
+ 00674454 ["CALL", null, ["callee:00487e20:8"]]
- 00674414 bytes 734ef897
+ 00674454 bytes 734ef897
- 00674420 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00674420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00674420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00674420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00674460 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00674460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00674460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00674460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00674420 bytes 08e12491
+ 00674460 bytes 08e13491
- 00674430 ["INT_ADD", "register:40f0:8", ["const:674430:8", "const:4:8"]]
- 00674430 ["CALL", null, ["callee:00676ab8:8"]]
+ 00674470 ["INT_ADD", "register:40f0:8", ["const:674470:8", "const:4:8"]]
+ 00674470 ["CALL", null, ["callee:00676ab8:8"]]
- 00674430 bytes 92090094
+ 00674470 bytes 92090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d2693b4cde402b24f4ff6a91ef953c"></a>

### [`00674af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md) → [`00674b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674b30.md) FUN_00674b30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a8509c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a85/00a8509c.md) · 呼出先 17件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)
- 新版 呼出元 1件 [`00a85294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a85/00a85294.md) · 呼出先 17件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.70% / 新版 99.70%

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
      "site": "00674d54",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00674d14",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "00674d54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "006752a0",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "006752a8",
      "PARAM",
      [
        "storage",
        "00310461",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00674d54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "006752a0",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "006752a8",
      "PARAM",
      [
        "storage",
        "003104a1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00674d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md#insn-00674d14) · [`00674b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md#insn-00674b3c) · [`00674b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md#insn-00674b98)
- 新版 `00674d54`（命令位置の公開資料なし） · `00674b7c`（命令位置の公開資料なし） · `00674bd8`（命令位置の公開資料なし）

~~~diff
- 00674d14 ["INT_ADD", "register:40f0:8", ["const:674d14:8", "const:4:8"]]
- 00674d14 ["CALL", null, ["ram:a65bf4:8"]]
+ 00674d54 ["INT_ADD", "register:40f0:8", ["const:674d54:8", "const:4:8"]]
+ 00674d54 ["CALL", null, ["ram:a65dec:8"]]
- 00674d14 bytes b8c30f94
+ 00674d54 bytes 26c40f94
- 00674b3c ["INT_ADD", "register:40f0:8", ["const:674b3c:8", "const:4:8"]]
- 00674b3c ["CALL", null, ["callee:005c3e7c:8"]]
+ 00674b7c ["INT_ADD", "register:40f0:8", ["const:674b7c:8", "const:4:8"]]
+ 00674b7c ["CALL", null, ["callee:005c3e7c:8"]]
- 00674b3c bytes c03cfd97
+ 00674b7c bytes c03cfd97
- 00674b98 ["INT_ADD", "register:40f0:8", ["const:674b98:8", "const:4:8"]]
- 00674b98 ["CALL", null, ["callee:00c57e90:8"]]
+ 00674bd8 ["INT_ADD", "register:40f0:8", ["const:674bd8:8", "const:4:8"]]
+ 00674bd8 ["CALL", null, ["callee:00c57e90:8"]]
- 00674b98 bytes be8b1794
+ 00674bd8 bytes ae8c1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ef0bbcb42a66cd86b0e4411a2b9214"></a>

### [`00675578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675578.md) → [`006755b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/006755b8.md) FUN_006755b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00674af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)
- 新版 呼出元 5件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00674b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674b30.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.99% / 新版 98.99%

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
      "site": "0067580c",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006757cc",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006758cc",
      "incomplete_value": false,
      "site": "006758d0",
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
      "definition_site": "0067588c",
      "incomplete_value": false,
      "site": "00675890",
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
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0067580c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "006758cc",
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
      "0067580c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "006758cc",
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

- 旧版 [`006757cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675578.md#insn-006757cc) · [`00675890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675578.md#insn-00675890) · [`006755a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675578.md#insn-006755a4)
- 新版 `0067580c`（命令位置の公開資料なし） · `006758d0`（命令位置の公開資料なし） · `006755e4`（命令位置の公開資料なし）

~~~diff
- 006757cc ["INT_ADD", "register:40f0:8", ["const:6757cc:8", "const:4:8"]]
- 006757cc ["CALL", null, ["ram:a65bf4:8"]]
+ 0067580c ["INT_ADD", "register:40f0:8", ["const:67580c:8", "const:4:8"]]
+ 0067580c ["CALL", null, ["ram:a65dec:8"]]
- 006757cc bytes 0ac10f94
+ 0067580c bytes 78c10f94
- 00675890 ["INT_ADD", "register:40f0:8", ["const:675890:8", "const:4:8"]]
- 00675890 ["CALL", null, ["callee:00442930:8"]]
+ 006758d0 ["INT_ADD", "register:40f0:8", ["const:6758d0:8", "const:4:8"]]
+ 006758d0 ["CALL", null, ["callee:00442930:8"]]
- 00675890 bytes 1834f797
+ 006758d0 bytes 1834f797
- 006755a4 ["INT_ADD", "register:40f0:8", ["const:6755a4:8", "const:4:8"]]
- 006755a4 ["CALL", null, ["callee:005c179c:8"]]
+ 006755e4 ["INT_ADD", "register:40f0:8", ["const:6755e4:8", "const:4:8"]]
+ 006755e4 ["CALL", null, ["callee:005c179c:8"]]
- 006755a4 bytes 6e30fd97
+ 006755e4 bytes 6e30fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bd529d4720dae70dd4b54dd0dd5d46f"></a>

### [`00675894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675894.md) → [`006758d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/006758d4.md) FUN_006758d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00674af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/00674af0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 10件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`00674b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674b30.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00675998",
      "incomplete_value": false,
      "site": "0067599c",
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
      "definition_site": "00675958",
      "incomplete_value": false,
      "site": "0067595c",
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
      "00675998",
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
      "00675998",
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

- 旧版 [`0067595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675894.md#insn-0067595c) · [`00675958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675894.md#insn-00675958)
- 新版 `0067599c`（命令位置の公開資料なし） · `00675998`（命令位置の公開資料なし）

~~~diff
- 0067595c ["INT_ADD", "register:40f0:8", ["const:67595c:8", "const:4:8"]]
- 0067595c ["CALL", null, ["callee:00442930:8"]]
+ 0067599c ["INT_ADD", "register:40f0:8", ["const:67599c:8", "const:4:8"]]
+ 0067599c ["CALL", null, ["callee:00442930:8"]]
- 0067595c bytes e533f797
+ 0067599c bytes e533f797
- 00675958 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00675958 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00675958 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00675958 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00675998 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00675998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00675998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00675998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00675958 bytes 00c00391
+ 00675998 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782fc3aff3d480bd84b46e262b029dd9"></a>

### [`006760d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006760d8.md) → [`00676118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676118.md) FUN_00676118

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.71% / 新版 96.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00676158",
      "incomplete_value": false,
      "site": "00676164",
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
      "definition_site": "00676118",
      "incomplete_value": false,
      "site": "00676124",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006764a0",
      "incomplete_value": true,
      "site": "006764b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:beb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00676460",
      "incomplete_value": true,
      "site": "00676470",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006764b4",
      "incomplete_value": true,
      "site": "006764b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00676474",
      "incomplete_value": true,
      "site": "00676474",
      "value": [
        "LOAD",
        "8",
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
      "00676164",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0067619c",
      "READ",
      [
        "storage",
        "002b0e77",
        null,
        "string"
      ]
    ],
    [
      "006764a0",
      "READ",
      [
        "storage",
        "002bdbab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00676164",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0067619c",
      "READ",
      [
        "storage",
        "002b0eb7",
        null,
        "string"
      ]
    ],
    [
      "006764a0",
      "READ",
      [
        "storage",
        "002bdbeb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006764b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006760d8.md#insn-006764b4) · [`0067610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006760d8.md#insn-0067610c) · [`00676118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006760d8.md#insn-00676118)
- 新版 `006764f4`（命令位置の公開資料なし） · `0067614c`（命令位置の公開資料なし） · `00676158`（命令位置の公開資料なし）

~~~diff
- 006764b4 ["INT_ADD", "register:40f0:8", ["const:6764b4:8", "const:4:8"]]
- 006764b4 ["CALL", null, ["callee:0043bba4:8"]]
+ 006764f4 ["INT_ADD", "register:40f0:8", ["const:6764f4:8", "const:4:8"]]
+ 006764f4 ["CALL", null, ["callee:0043bba4:8"]]
- 006764b4 bytes ac15f797
+ 006764f4 bytes ac15f797
- 0067610c ["INT_ADD", "register:40f0:8", ["const:67610c:8", "const:4:8"]]
- 0067610c ["CALL", null, ["callee:00487e20:8"]]
+ 0067614c ["INT_ADD", "register:40f0:8", ["const:67614c:8", "const:4:8"]]
+ 0067614c ["CALL", null, ["callee:00487e20:8"]]
- 0067610c bytes 3547f897
+ 0067614c bytes 3547f897
- 00676118 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00676118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00676118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00676118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00676158 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00676158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00676158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00676158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00676118 bytes 08e12491
+ 00676158 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf1f001f28c3007e8c2ddcef1646f06b"></a>

### [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) → [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) FUN_0067674c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007ef644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef644.md) [`00802cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md) [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md) · 呼出先 4件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`008056ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)
- 新版 呼出元 11件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md) [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) · 呼出先 4件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`008056ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00676784",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00676744",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "site": "006767a4",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00676764",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "site": "00676800",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006767c0",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "00676784",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "006767a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "00676800",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "00676784",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "006767a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00676800",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00676744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md#insn-00676744) · [`00676764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md#insn-00676764) · [`006767c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md#insn-006767c0)
- 新版 `00676784`（命令位置の公開資料なし） · `006767a4`（命令位置の公開資料なし） · `00676800`（命令位置の公開資料なし）

~~~diff
- 00676744 ["INT_ADD", "register:40f0:8", ["const:676744:8", "const:4:8"]]
- 00676744 ["CALL", null, ["ram:a65bf4:8"]]
+ 00676784 ["INT_ADD", "register:40f0:8", ["const:676784:8", "const:4:8"]]
+ 00676784 ["CALL", null, ["ram:a65dec:8"]]
- 00676744 bytes 2cbd0f94
+ 00676784 bytes 9abd0f94
- 00676764 ["INT_ADD", "register:40f0:8", ["const:676764:8", "const:4:8"]]
- 00676764 ["CALL", null, ["ram:a65bf4:8"]]
+ 006767a4 ["INT_ADD", "register:40f0:8", ["const:6767a4:8", "const:4:8"]]
+ 006767a4 ["CALL", null, ["ram:a65dec:8"]]
- 00676764 bytes 24bd0f94
+ 006767a4 bytes 92bd0f94
- 006767c0 ["INT_ADD", "register:40f0:8", ["const:6767c0:8", "const:4:8"]]
- 006767c0 ["CALL", null, ["ram:a65bf4:8"]]
+ 00676800 ["INT_ADD", "register:40f0:8", ["const:676800:8", "const:4:8"]]
+ 00676800 ["CALL", null, ["ram:a65dec:8"]]
- 006767c0 bytes 0dbd0f94
+ 00676800 bytes 7bbd0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f77a6e319d2b9c9876eb9e612b13655"></a>

### [`006767fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006767fc.md) → [`0067683c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067683c.md) FUN_0067683c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`00ab0504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0504.md) · 呼出先 1件 [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)
- 新版 呼出元 2件 [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) [`00ab0700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab0700.md) · 呼出先 1件 [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "00676858",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00676818",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "00676858",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "00676858",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00676818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006767fc.md#insn-00676818)
- 新版 `00676858`（命令位置の公開資料なし）

~~~diff
- 00676818 ["INT_ADD", "register:40f0:8", ["const:676818:8", "const:4:8"]]
- 00676818 ["CALL", null, ["ram:a65bf4:8"]]
+ 00676858 ["INT_ADD", "register:40f0:8", ["const:676858:8", "const:4:8"]]
+ 00676858 ["CALL", null, ["ram:a65dec:8"]]
- 00676818 bytes f7bc0f94
+ 00676858 bytes 65bd0f94
~~~


<a id="compare-098521bc42e2ddfe07435527ee5f1c56"></a>

### [`0067682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md) → [`0067686c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067686c.md) FUN_0067686c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`006bea48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bea48.md) [`0072b4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b4b8.md) · 呼出先 2件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md)
- 新版 呼出元 10件 [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006bea88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bea88.md) [`0072b4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b4f8.md) · 呼出先 2件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

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
      "site": "006768a8",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00676868",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "006768a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "006768a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00676868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md#insn-00676868) · [`00676838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md#insn-00676838) · [`00676854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md#insn-00676854)
- 新版 `006768a8`（命令位置の公開資料なし） · `00676878`（命令位置の公開資料なし） · `00676894`（命令位置の公開資料なし）

~~~diff
- 00676868 ["INT_ADD", "register:40f0:8", ["const:676868:8", "const:4:8"]]
- 00676868 ["CALL", null, ["ram:802b4c:8"]]
+ 006768a8 ["INT_ADD", "register:40f0:8", ["const:6768a8:8", "const:4:8"]]
+ 006768a8 ["CALL", null, ["ram:802b8c:8"]]
- 00676868 bytes b9300694
+ 006768a8 bytes b9300694
- 00676838 ["INT_ADD", "register:40f0:8", ["const:676838:8", "const:4:8"]]
- 00676838 ["CALL", null, ["callee:008026b8:8"]]
+ 00676878 ["INT_ADD", "register:40f0:8", ["const:676878:8", "const:4:8"]]
+ 00676878 ["CALL", null, ["callee:008026b8:8"]]
- 00676838 bytes 902f0694
+ 00676878 bytes 902f0694
- 00676854 ["INT_ADD", "register:40f0:8", ["const:676854:8", "const:4:8"]]
- 00676854 ["CALL", null, ["callee:008026b8:8"]]
+ 00676894 ["INT_ADD", "register:40f0:8", ["const:676894:8", "const:4:8"]]
+ 00676894 ["CALL", null, ["callee:008026b8:8"]]
- 00676854 bytes 892f0694
+ 00676894 bytes 892f0694
~~~


<a id="compare-cf40dde11c251ca76e60293ffa90be8f"></a>

### [`0067687c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067687c.md) → [`006768bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/006768bc.md) FUN_006768bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`006794f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006794f4.md) [`007efb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md) [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) · 呼出先 2件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md)
- 新版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) [`00679534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00679/00679534.md) [`007efbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efbb0.md) [`00934078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934078.md) · 呼出先 2件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "006768dc",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0067689c",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "006768dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "006768dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067687c.md#insn-0067689c) · [`00676888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067687c.md#insn-00676888)
- 新版 `006768dc`（命令位置の公開資料なし） · `006768c8`（命令位置の公開資料なし）

~~~diff
- 0067689c ["INT_ADD", "register:40f0:8", ["const:67689c:8", "const:4:8"]]
- 0067689c ["CALL", null, ["ram:802b4c:8"]]
+ 006768dc ["INT_ADD", "register:40f0:8", ["const:6768dc:8", "const:4:8"]]
+ 006768dc ["CALL", null, ["ram:802b8c:8"]]
- 0067689c bytes ac300694
+ 006768dc bytes ac300694
- 00676888 ["INT_ADD", "register:40f0:8", ["const:676888:8", "const:4:8"]]
- 00676888 ["CALL", null, ["callee:008026b8:8"]]
+ 006768c8 ["INT_ADD", "register:40f0:8", ["const:6768c8:8", "const:4:8"]]
+ 006768c8 ["CALL", null, ["callee:008026b8:8"]]
- 00676888 bytes 7c2f0694
+ 006768c8 bytes 7c2f0694
~~~


<a id="compare-5fde7f7d4309bd9f73db1316e85147bf"></a>

### [`006768b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006768b0.md) → [`006768f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/006768f0.md) FUN_006768f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 6件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0067694c",
      "incomplete_value": false,
      "site": "00676950",
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
      "definition_site": "0067690c",
      "incomplete_value": false,
      "site": "00676910",
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
      "0067694c",
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
      "0067694c",
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

- 旧版 [`00676910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006768b0.md#insn-00676910) · [`0067690c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006768b0.md#insn-0067690c)
- 新版 `00676950`（命令位置の公開資料なし） · `0067694c`（命令位置の公開資料なし）

~~~diff
- 00676910 ["INT_ADD", "register:40f0:8", ["const:676910:8", "const:4:8"]]
- 00676910 ["CALL", null, ["callee:00442930:8"]]
+ 00676950 ["INT_ADD", "register:40f0:8", ["const:676950:8", "const:4:8"]]
+ 00676950 ["CALL", null, ["callee:00442930:8"]]
- 00676910 bytes f82ff797
+ 00676950 bytes f82ff797
- 0067690c ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0067690c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067690c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067690c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067694c ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 0067694c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067694c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067694c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067690c bytes 00c00391
+ 0067694c bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf358d733be612165ef3c3983ea05d0"></a>

### [`0067692c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067692c.md) → [`0067696c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067696c.md) FUN_0067696c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006769d8",
      "incomplete_value": false,
      "site": "006769dc",
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
      "definition_site": "00676998",
      "incomplete_value": false,
      "site": "0067699c",
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
      "006769d8",
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
      "006769d8",
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

- 旧版 [`0067699c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067692c.md#insn-0067699c) · [`00676998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067692c.md#insn-00676998)
- 新版 `006769dc`（命令位置の公開資料なし） · `006769d8`（命令位置の公開資料なし）

~~~diff
- 0067699c ["INT_ADD", "register:40f0:8", ["const:67699c:8", "const:4:8"]]
- 0067699c ["CALL", null, ["callee:00442930:8"]]
+ 006769dc ["INT_ADD", "register:40f0:8", ["const:6769dc:8", "const:4:8"]]
+ 006769dc ["CALL", null, ["callee:00442930:8"]]
- 0067699c bytes d52ff797
+ 006769dc bytes d52ff797
- 00676998 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00676998 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00676998 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00676998 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006769d8 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 006769d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006769d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006769d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00676998 bytes 00c00391
+ 006769d8 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f58e68b7615b43b4d36e175081456b2"></a>

### [`00676a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a64.md) → [`00676aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676aa4.md) FUN_00676aa4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006741b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006741b0.md) [`00a87284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a87284.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`006741f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/006741f0.md) [`00a8747c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a8747c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00676ab0",
      "incomplete_value": false,
      "site": "00676ab4",
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
      "definition_site": "00676a70",
      "incomplete_value": false,
      "site": "00676a74",
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
      "00676ab0",
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
      "00676ab0",
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

- 旧版 [`00676a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a64.md#insn-00676a74) · [`00676a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a64.md#insn-00676a70)
- 新版 `00676ab4`（命令位置の公開資料なし） · `00676ab0`（命令位置の公開資料なし）

~~~diff
- 00676a74 ["INT_ADD", "register:40f0:8", ["const:676a74:8", "const:4:8"]]
- 00676a74 ["CALL", null, ["callee:0043b778:8"]]
+ 00676ab4 ["INT_ADD", "register:40f0:8", ["const:676ab4:8", "const:4:8"]]
+ 00676ab4 ["CALL", null, ["callee:0043b778:8"]]
- 00676a74 bytes 3113f797
+ 00676ab4 bytes 3113f797
- 00676a70 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00676a70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00676a70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00676a70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00676ab0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00676ab0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00676ab0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00676ab0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00676a70 bytes 00303c91
+ 00676ab0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a316812ce40141b5ccf3f5a278debaf8"></a>

### [`00677670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677670.md) → [`006776b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/006776b0.md) _INIT_94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006776ec",
      "incomplete_value": true,
      "site": "00677708",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006776ac",
      "incomplete_value": true,
      "site": "006776c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067778c",
      "incomplete_value": true,
      "site": "006777a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067774c",
      "incomplete_value": true,
      "site": "00677768",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006778e0",
      "incomplete_value": true,
      "site": "006778e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006778a0",
      "incomplete_value": true,
      "site": "006778a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
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
      "006776ec",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00677710",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00677730",
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
      "006776ec",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00677710",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00677730",
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

- 旧版 [`00677708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677670.md#insn-00677708) · [`006778a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677670.md#insn-006778a4) · [`0067769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677670.md#insn-0067769c)
- 新版 `00677748`（命令位置の公開資料なし） · `006778e4`（命令位置の公開資料なし） · `006776dc`（命令位置の公開資料なし）

~~~diff
- 00677708 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00677708 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00677708 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00677708 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00677748 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00677748 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00677748 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00677748 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00677708 bytes 4a553a91
+ 00677748 bytes 4a893d91
- 006778a4 ["INT_ADD", "register:40f0:8", ["const:6778a4:8", "const:4:8"]]
- 006778a4 ["CALL", null, ["callee:00c57e30:8"]]
+ 006778e4 ["INT_ADD", "register:40f0:8", ["const:6778e4:8", "const:4:8"]]
+ 006778e4 ["CALL", null, ["callee:00c57e30:8"]]
- 006778a4 bytes 63801794
+ 006778e4 bytes 53811794
- 0067769c ["COPY", "tmp:0:8", ["const:210:8"]]
- 0067769c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0067769c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0067769c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006776dc ["COPY", "tmp:0:8", ["const:610:8"]]
+ 006776dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006776dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006776dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0067769c bytes 73420891
+ 006776dc bytes 73421891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77245db059d596cf911f85fa01b3a20e"></a>

### [`006788a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md) → [`006788e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00678/006788e0.md) FUN_006788e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 19件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 19件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00678a20",
      "incomplete_value": true,
      "site": "00678a30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:164:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006789e0",
      "incomplete_value": true,
      "site": "006789f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:124:8"
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
      "definition_site": "00678a24",
      "incomplete_value": true,
      "site": "00678a34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006789e4",
      "incomplete_value": true,
      "site": "006789f4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00678a28",
      "incomplete_value": true,
      "site": "00678a38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006789e8",
      "incomplete_value": true,
      "site": "006789f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00678a20",
      "READ",
      [
        "storage",
        "002c0124",
        null,
        "string"
      ]
    ],
    [
      "00678a24",
      "READ",
      [
        "storage",
        "002c0134",
        null,
        "string"
      ]
    ],
    [
      "00678a28",
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00678a20",
      "READ",
      [
        "storage",
        "002c0164",
        null,
        "string"
      ]
    ],
    [
      "00678a24",
      "READ",
      [
        "storage",
        "002c0174",
        null,
        "string"
      ]
    ],
    [
      "00678a28",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00678c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md#insn-00678c6c) · [`00678cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md#insn-00678cc8) · [`00678d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md#insn-00678d84)
- 新版 `00678cac`（命令位置の公開資料なし） · `00678d08`（命令位置の公開資料なし） · `00678dc4`（命令位置の公開資料なし）

~~~diff
- 00678c6c ["INT_ADD", "register:40f0:8", ["const:678c6c:8", "const:4:8"]]
- 00678c6c ["CALL", null, ["callee:005ccd04:8"]]
+ 00678cac ["INT_ADD", "register:40f0:8", ["const:678cac:8", "const:4:8"]]
+ 00678cac ["CALL", null, ["callee:005ccd04:8"]]
- 00678c6c bytes 1650fd97
+ 00678cac bytes 1650fd97
- 00678cc8 ["INT_ADD", "register:40f0:8", ["const:678cc8:8", "const:4:8"]]
- 00678cc8 ["CALL", null, ["ram:47acb4:8"]]
+ 00678d08 ["INT_ADD", "register:40f0:8", ["const:678d08:8", "const:4:8"]]
+ 00678d08 ["CALL", null, ["ram:47acf4:8"]]
- 00678cc8 bytes fb07f897
+ 00678d08 bytes fb07f897
- 00678d84 ["INT_ADD", "register:40f0:8", ["const:678d84:8", "const:4:8"]]
- 00678d84 ["CALL", null, ["ram:47acb4:8"]]
+ 00678dc4 ["INT_ADD", "register:40f0:8", ["const:678dc4:8", "const:4:8"]]
+ 00678dc4 ["CALL", null, ["ram:47acf4:8"]]
- 00678d84 bytes cc07f897
+ 00678dc4 bytes cc07f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eceb7ce0616b4e255555445c312a47b0"></a>

### [`0067a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md) → [`0067a3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067a/0067a3a4.md) FUN_0067a3a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) · 呼出先 13件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00758800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758800.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) · 呼出先 13件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00758840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/00758840.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 77.11% / 新版 77.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 73件, `store_destination` 37件, `store_value` 48件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067a4a0",
      "incomplete_value": true,
      "site": "0067a4a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067a460",
      "incomplete_value": true,
      "site": "0067a460",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067a4b8",
      "incomplete_value": true,
      "site": "0067a4b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067a478",
      "incomplete_value": true,
      "site": "0067a478",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
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
      "definition_site": "0067a4bc",
      "incomplete_value": true,
      "site": "0067a4bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0067a47c",
      "incomplete_value": true,
      "site": "0067a47c",
      "value": [
        "LOAD",
        "8",
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
      "0067a404",
      "DATA",
      [
        "storage",
        "00c743b8",
        null,
        "pointer"
      ]
    ],
    [
      "0067a470",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067a490",
      "READ",
      [
        "storage",
        "002b2dda",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067a404",
      "DATA",
      [
        "storage",
        "00c747b8",
        null,
        "pointer"
      ]
    ],
    [
      "0067a470",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067a490",
      "READ",
      [
        "storage",
        "002b2e1a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067a6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md#insn-0067a6d4) · [`0067a85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md#insn-0067a85c) · [`0067ad28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md#insn-0067ad28)
- 新版 `0067a89c`（命令位置の公開資料なし） · `0067ad68`（命令位置の公開資料なし）

~~~diff
- 0067a6d4 ["COPY", "register:4040:8", ["const:2b2000:8"]]
- 0067a6d4 bytes c8e1ff90
- 0067a85c ["INT_ADD", "register:40f0:8", ["const:67a85c:8", "const:4:8"]]
- 0067a85c ["CALL", null, ["callee:00c53d00:8"]]
+ 0067a89c ["INT_ADD", "register:40f0:8", ["const:67a89c:8", "const:4:8"]]
+ 0067a89c ["CALL", null, ["callee:00c53d00:8"]]
- 0067a85c bytes 21641794
+ 0067a89c bytes 19651794
- 0067ad28 ["INT_ADD", "register:40f0:8", ["const:67ad28:8", "const:4:8"]]
- 0067ad28 ["CALL", null, ["callee:00c53d00:8"]]
+ 0067ad68 ["INT_ADD", "register:40f0:8", ["const:67ad68:8", "const:4:8"]]
+ 0067ad68 ["CALL", null, ["callee:00c53d00:8"]]
- 0067ad28 bytes ee621794
+ 0067ad68 bytes e6631794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d127e91a14344ed4bb685a4c52e84ee"></a>

### [`0067b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b7b4.md) → [`0067b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067b7f4.md) FUN_0067b7f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0067b810",
      "incomplete_value": false,
      "site": "0067b814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067b7d0",
      "incomplete_value": false,
      "site": "0067b7d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "0067b814",
      "DATA",
      [
        "storage",
        "00c743b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0067b814",
      "DATA",
      [
        "storage",
        "00c747b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b7b4.md#insn-0067b7d0) · [`0067b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b7b4.md#insn-0067b80c) · [`0067b820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b7b4.md#insn-0067b820)
- 新版 `0067b810`（命令位置の公開資料なし） · `0067b84c`（命令位置の公開資料なし） · `0067b860`（命令位置の公開資料なし）

~~~diff
- 0067b7d0 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0067b7d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067b7d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067b7d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067b810 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0067b810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067b810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067b810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067b7d0 bytes 08e10e91
+ 0067b810 bytes 08e11e91
- 0067b80c ["INT_ADD", "register:40f0:8", ["const:67b80c:8", "const:4:8"]]
- 0067b80c ["CALL", null, ["callee:00c53d00:8"]]
+ 0067b84c ["INT_ADD", "register:40f0:8", ["const:67b84c:8", "const:4:8"]]
+ 0067b84c ["CALL", null, ["callee:00c53d00:8"]]
- 0067b80c bytes 35601794
+ 0067b84c bytes 2d611794
- 0067b820 ["COPY", "register:0:8", ["register:4040:8"]]
- 0067b820 ["INT_ADD", "register:40f0:8", ["const:67b820:8", "const:4:8"]]
- 0067b820 ["CALLIND", null, ["register:0:8"]]
+ 0067b860 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0067b860 ["INT_ADD", "register:40f0:8", ["const:67b860:8", "const:4:8"]]
+ 0067b860 ["CALLIND", null, ["register:0:8"]]
- 0067b820 bytes 00013fd6
+ 0067b860 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-906cde4697fd5c88f823cc2f21e008de"></a>

### [`0067b8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b8a0.md) → [`0067b8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067b8e0.md) FUN_0067b8e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0067b8fc",
      "incomplete_value": false,
      "site": "0067b900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067b8bc",
      "incomplete_value": false,
      "site": "0067b8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "0067b900",
      "DATA",
      [
        "storage",
        "00c743b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0067b900",
      "DATA",
      [
        "storage",
        "00c747b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067b8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b8a0.md#insn-0067b8bc) · [`0067b8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b8a0.md#insn-0067b8f8) · [`0067b90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b8a0.md#insn-0067b90c)
- 新版 `0067b8fc`（命令位置の公開資料なし） · `0067b938`（命令位置の公開資料なし） · `0067b94c`（命令位置の公開資料なし）

~~~diff
- 0067b8bc ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0067b8bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067b8bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067b8bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067b8fc ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0067b8fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067b8fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067b8fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067b8bc bytes 08e10e91
+ 0067b8fc bytes 08e11e91
- 0067b8f8 ["INT_ADD", "register:40f0:8", ["const:67b8f8:8", "const:4:8"]]
- 0067b8f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0067b938 ["INT_ADD", "register:40f0:8", ["const:67b938:8", "const:4:8"]]
+ 0067b938 ["CALL", null, ["callee:00c53d00:8"]]
- 0067b8f8 bytes fa5f1794
+ 0067b938 bytes f2601794
- 0067b90c ["COPY", "register:0:8", ["register:4040:8"]]
- 0067b90c ["INT_ADD", "register:40f0:8", ["const:67b90c:8", "const:4:8"]]
- 0067b90c ["CALLIND", null, ["register:0:8"]]
+ 0067b94c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0067b94c ["INT_ADD", "register:40f0:8", ["const:67b94c:8", "const:4:8"]]
+ 0067b94c ["CALLIND", null, ["register:0:8"]]
- 0067b90c bytes 00013fd6
+ 0067b94c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134d1b28eb99362cef6f44656d5cd4ee"></a>

### [`0067b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b994.md) → [`0067b9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067b9d4.md) _INIT_95

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067ba10",
      "incomplete_value": true,
      "site": "0067ba2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067b9d0",
      "incomplete_value": true,
      "site": "0067b9ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ba34",
      "incomplete_value": true,
      "site": "0067ba50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067b9f4",
      "incomplete_value": true,
      "site": "0067ba10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ba54",
      "incomplete_value": true,
      "site": "0067ba70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067ba14",
      "incomplete_value": true,
      "site": "0067ba30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067ba10",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0067ba34",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0067ba54",
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
      "0067ba10",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0067ba34",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0067ba54",
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

- 旧版 [`0067ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b994.md#insn-0067ba0c) · [`0067ba2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b994.md#insn-0067ba2c) · [`0067bbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b994.md#insn-0067bbc8)
- 新版 `0067ba4c`（命令位置の公開資料なし） · `0067ba6c`（命令位置の公開資料なし） · `0067bc08`（命令位置の公開資料なし）

~~~diff
- 0067ba0c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0067ba0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067ba0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067ba0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067ba4c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0067ba4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067ba4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067ba4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067ba0c bytes 4a093691
+ 0067ba4c bytes 4a093791
- 0067ba2c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0067ba2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067ba2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067ba2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067ba6c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0067ba6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067ba6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067ba6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067ba2c bytes 4a553a91
+ 0067ba6c bytes 4a893d91
- 0067bbc8 ["INT_ADD", "register:40f0:8", ["const:67bbc8:8", "const:4:8"]]
- 0067bbc8 ["CALL", null, ["callee:00c57e30:8"]]
+ 0067bc08 ["INT_ADD", "register:40f0:8", ["const:67bc08:8", "const:4:8"]]
+ 0067bc08 ["CALL", null, ["callee:00c57e30:8"]]
- 0067bbc8 bytes 9a6f1794
+ 0067bc08 bytes 8a701794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-166c6c8dfa7e85f9071fcd38225f9c84"></a>

### [`0067bd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067bd24.md) → [`0067bd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067bd64.md) FUN_0067bd64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0067bda8",
      "incomplete_value": false,
      "site": "0067bdb4",
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
      "definition_site": "0067bd68",
      "incomplete_value": false,
      "site": "0067bd74",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067be08",
      "incomplete_value": true,
      "site": "0067be08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067bdc8",
      "incomplete_value": true,
      "site": "0067bdc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76d:8"
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
      "definition_site": "0067c1fc",
      "incomplete_value": true,
      "site": "0067c1fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:27f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067c1bc",
      "incomplete_value": true,
      "site": "0067c1bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b2:8"
              ]
            ]
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
      "0067bdb4",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0067bdf8",
      "READ",
      [
        "storage",
        "002ab76d",
        null,
        "string"
      ]
    ],
    [
      "0067c1ec",
      "READ",
      [
        "storage",
        "0029f1b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067bdb4",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0067bdf8",
      "READ",
      [
        "storage",
        "002ab7ad",
        null,
        "string"
      ]
    ],
    [
      "0067c1ec",
      "READ",
      [
        "storage",
        "0029f27f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067bd24.md#insn-0067c1fc) · [`0067c2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067bd24.md#insn-0067c2e0) · [`0067c360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067bd24.md#insn-0067c360)
- 新版 `0067c23c`（命令位置の公開資料なし） · `0067c320`（命令位置の公開資料なし） · `0067c3a0`（命令位置の公開資料なし）

~~~diff
- 0067c1fc ["INT_ADD", "register:40f0:8", ["const:67c1fc:8", "const:4:8"]]
- 0067c1fc ["CALL", null, ["callee:0048791c:8"]]
+ 0067c23c ["INT_ADD", "register:40f0:8", ["const:67c23c:8", "const:4:8"]]
+ 0067c23c ["CALL", null, ["callee:0048791c:8"]]
- 0067c1fc bytes b82df897
+ 0067c23c bytes b82df897
- 0067c2e0 ["INT_ADD", "register:40f0:8", ["const:67c2e0:8", "const:4:8"]]
- 0067c2e0 ["CALL", null, ["callee:0048793c:8"]]
+ 0067c320 ["INT_ADD", "register:40f0:8", ["const:67c320:8", "const:4:8"]]
+ 0067c320 ["CALL", null, ["callee:0048793c:8"]]
- 0067c2e0 bytes 872df897
+ 0067c320 bytes 872df897
- 0067c360 ["INT_ADD", "register:40f0:8", ["const:67c360:8", "const:4:8"]]
- 0067c360 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0067c3a0 ["INT_ADD", "register:40f0:8", ["const:67c3a0:8", "const:4:8"]]
+ 0067c3a0 ["CALL", null, ["callee:00c57fb0:8"]]
- 0067c360 bytes 146e1794
+ 0067c3a0 bytes 046f1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bca17e852f4d9541a67483cb76a0befc"></a>

### [`0067c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c58c.md) → [`0067c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c5cc.md) FUN_0067c5cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)
- 新版 呼出元 1件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.84% / 新版 98.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0067c6e8",
      "incomplete_value": true,
      "site": "0067c6ec",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067c6a8",
      "incomplete_value": true,
      "site": "0067c6ac",
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
            "const:f0:8"
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
      "0067c6e8",
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
      "0067c6e8",
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

- 旧版 [`0067c6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c58c.md#insn-0067c6ac) · [`0067c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c58c.md#insn-0067c5d4) · [`0067c6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c58c.md#insn-0067c6a8)
- 新版 `0067c6ec`（命令位置の公開資料なし） · `0067c614`（命令位置の公開資料なし） · `0067c6e8`（命令位置の公開資料なし）

~~~diff
- 0067c6ac ["INT_ADD", "register:40f0:8", ["const:67c6ac:8", "const:4:8"]]
- 0067c6ac ["CALL", null, ["callee:00442930:8"]]
+ 0067c6ec ["INT_ADD", "register:40f0:8", ["const:67c6ec:8", "const:4:8"]]
+ 0067c6ec ["CALL", null, ["callee:00442930:8"]]
- 0067c6ac bytes 9118f797
+ 0067c6ec bytes 9118f797
- 0067c5d4 ["INT_ADD", "register:40f0:8", ["const:67c5d4:8", "const:4:8"]]
- 0067c5d4 ["CALL", null, ["callee:0046d7b0:8"]]
+ 0067c614 ["INT_ADD", "register:40f0:8", ["const:67c614:8", "const:4:8"]]
+ 0067c614 ["CALL", null, ["callee:0046d7b0:8"]]
- 0067c5d4 bytes 67c4f797
+ 0067c614 bytes 67c4f797
- 0067c6a8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0067c6a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067c6a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067c6a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067c6e8 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 0067c6e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c6e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c6e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067c6a8 bytes 00c00391
+ 0067c6e8 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98e365608d1b8499f144b09d5a3f7147"></a>

### [`0067c7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7d4.md) → [`0067c814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c814.md) FUN_0067c814

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0067bd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067bd24.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0067bd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067b/0067bd64.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0067c820",
      "incomplete_value": false,
      "site": "0067c824",
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
      "definition_site": "0067c7e0",
      "incomplete_value": false,
      "site": "0067c7e4",
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
      "0067c820",
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
      "0067c820",
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

- 旧版 [`0067c7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7d4.md#insn-0067c7e4) · [`0067c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7d4.md#insn-0067c7e0)
- 新版 `0067c824`（命令位置の公開資料なし） · `0067c820`（命令位置の公開資料なし）

~~~diff
- 0067c7e4 ["INT_ADD", "register:40f0:8", ["const:67c7e4:8", "const:4:8"]]
- 0067c7e4 ["CALL", null, ["callee:0043b778:8"]]
+ 0067c824 ["INT_ADD", "register:40f0:8", ["const:67c824:8", "const:4:8"]]
+ 0067c824 ["CALL", null, ["callee:0043b778:8"]]
- 0067c7e4 bytes d5fbf697
+ 0067c824 bytes d5fbf697
- 0067c7e0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0067c7e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067c7e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067c7e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067c820 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0067c820 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c820 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c820 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067c7e0 bytes 00303c91
+ 0067c820 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4778435fbb1bf3e49500aafa44c697b5"></a>

### [`0067c7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7e8.md) → [`0067c828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c828.md) FUN_0067c828

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0067c72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c72c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`0067c76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c76c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0067c834",
      "incomplete_value": false,
      "site": "0067c838",
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
      "definition_site": "0067c7f4",
      "incomplete_value": false,
      "site": "0067c7f8",
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
      "0067c834",
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
      "0067c834",
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

- 旧版 [`0067c7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7e8.md#insn-0067c7f8) · [`0067c7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7e8.md#insn-0067c7f4)
- 新版 `0067c838`（命令位置の公開資料なし） · `0067c834`（命令位置の公開資料なし）

~~~diff
- 0067c7f8 ["INT_ADD", "register:40f0:8", ["const:67c7f8:8", "const:4:8"]]
- 0067c7f8 ["CALL", null, ["callee:00442930:8"]]
+ 0067c838 ["INT_ADD", "register:40f0:8", ["const:67c838:8", "const:4:8"]]
+ 0067c838 ["CALL", null, ["callee:00442930:8"]]
- 0067c7f8 bytes 3e18f797
+ 0067c838 bytes 3e18f797
- 0067c7f4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0067c7f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067c7f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067c7f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067c834 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0067c834 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c834 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067c834 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067c7f4 bytes 00303c91
+ 0067c834 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4f09a59515e767e74d0235a5591ae5"></a>

### [`0067c7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7fc.md) → [`0067c83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067c83c.md) _INIT_96

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067c878",
      "incomplete_value": true,
      "site": "0067c894",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067c838",
      "incomplete_value": true,
      "site": "0067c854",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067c89c",
      "incomplete_value": true,
      "site": "0067c8b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067c85c",
      "incomplete_value": true,
      "site": "0067c878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067c8bc",
      "incomplete_value": true,
      "site": "0067c8d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067c87c",
      "incomplete_value": true,
      "site": "0067c898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067c878",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0067c89c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0067c8bc",
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
      "0067c878",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0067c89c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0067c8bc",
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

- 旧版 [`0067c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7fc.md#insn-0067c874) · [`0067c894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7fc.md#insn-0067c894) · [`0067ca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c7fc.md#insn-0067ca30)
- 新版 `0067c8b4`（命令位置の公開資料なし） · `0067c8d4`（命令位置の公開資料なし） · `0067ca70`（命令位置の公開資料なし）

~~~diff
- 0067c874 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0067c874 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067c874 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067c874 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067c8b4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0067c8b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067c8b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067c8b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067c874 bytes 4a093691
+ 0067c8b4 bytes 4a093791
- 0067c894 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0067c894 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067c894 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067c894 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067c8d4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0067c8d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067c8d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067c8d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067c894 bytes 4a553a91
+ 0067c8d4 bytes 4a893d91
- 0067ca30 ["INT_ADD", "register:40f0:8", ["const:67ca30:8", "const:4:8"]]
- 0067ca30 ["CALL", null, ["callee:00c57e30:8"]]
+ 0067ca70 ["INT_ADD", "register:40f0:8", ["const:67ca70:8", "const:4:8"]]
+ 0067ca70 ["CALL", null, ["callee:00c57e30:8"]]
- 0067ca30 bytes 006c1794
+ 0067ca70 bytes f06c1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12ad2469f4c32d78d891071d9f30a145"></a>

### [`0067cb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067cb8c.md) → [`0067cbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067cbcc.md) FUN_0067cbcc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009d9790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d9790.md) [`009db81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009db81c.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488518.md)
- 新版 呼出元 2件 [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) [`009db9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009db9b8.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488558.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.56% / 新版 91.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0067cc14",
      "incomplete_value": false,
      "site": "0067cc18",
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
      "definition_site": "0067cbd4",
      "incomplete_value": false,
      "site": "0067cbd8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067cc88",
      "incomplete_value": true,
      "site": "0067cc9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ed7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067cc48",
      "incomplete_value": true,
      "site": "0067cc5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0a:8"
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
      "definition_site": "0067cd10",
      "incomplete_value": true,
      "site": "0067cd20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067ccd0",
      "incomplete_value": true,
      "site": "0067cce0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b5:8"
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
      "0067cc18",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0067cc38",
      "READ",
      [
        "storage",
        "002aeb21",
        null,
        "string"
      ]
    ],
    [
      "0067cc88",
      "READ",
      [
        "storage",
        "002a8e0a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067cc18",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0067cc38",
      "READ",
      [
        "storage",
        "002aeb61",
        null,
        "string"
      ]
    ],
    [
      "0067cc88",
      "READ",
      [
        "storage",
        "002a8ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067cf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067cb8c.md#insn-0067cf1c) · [`0067cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067cb8c.md#insn-0067cf90) · [`0067cbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067cb8c.md#insn-0067cbc8)
- 新版 `0067cf5c`（命令位置の公開資料なし） · `0067cfd0`（命令位置の公開資料なし） · `0067cc08`（命令位置の公開資料なし）

~~~diff
- 0067cf1c ["INT_ADD", "register:40f0:8", ["const:67cf1c:8", "const:4:8"]]
- 0067cf1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0067cf5c ["INT_ADD", "register:40f0:8", ["const:67cf5c:8", "const:4:8"]]
+ 0067cf5c ["CALL", null, ["callee:00c57eb0:8"]]
- 0067cf1c bytes e56a1794
+ 0067cf5c bytes d56b1794
- 0067cf90 ["INT_ADD", "register:40f0:8", ["const:67cf90:8", "const:4:8"]]
- 0067cf90 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0067cfd0 ["INT_ADD", "register:40f0:8", ["const:67cfd0:8", "const:4:8"]]
+ 0067cfd0 ["CALL", null, ["callee:00c57fb0:8"]]
- 0067cf90 bytes 086b1794
+ 0067cfd0 bytes f86b1794
- 0067cbc8 ["INT_ADD", "register:40f0:8", ["const:67cbc8:8", "const:4:8"]]
- 0067cbc8 ["CALL", null, ["callee:00487e20:8"]]
+ 0067cc08 ["INT_ADD", "register:40f0:8", ["const:67cc08:8", "const:4:8"]]
+ 0067cc08 ["CALL", null, ["callee:00487e20:8"]]
- 0067cbc8 bytes 862cf897
+ 0067cc08 bytes 862cf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7769f8b7305dc9f52153b03f57a96d6"></a>

### [`0067d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d0ec.md) → [`0067d12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d12c.md) FUN_0067d12c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0067cb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067cb8c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0067cbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067c/0067cbcc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0067d138",
      "incomplete_value": false,
      "site": "0067d13c",
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
      "definition_site": "0067d0f8",
      "incomplete_value": false,
      "site": "0067d0fc",
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
      "0067d138",
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
      "0067d138",
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

- 旧版 [`0067d0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d0ec.md#insn-0067d0fc) · [`0067d0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d0ec.md#insn-0067d0f8)
- 新版 `0067d13c`（命令位置の公開資料なし） · `0067d138`（命令位置の公開資料なし）

~~~diff
- 0067d0fc ["INT_ADD", "register:40f0:8", ["const:67d0fc:8", "const:4:8"]]
- 0067d0fc ["CALL", null, ["callee:0043b778:8"]]
+ 0067d13c ["INT_ADD", "register:40f0:8", ["const:67d13c:8", "const:4:8"]]
+ 0067d13c ["CALL", null, ["callee:0043b778:8"]]
- 0067d0fc bytes 8ff9f697
+ 0067d13c bytes 8ff9f697
- 0067d0f8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0067d0f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067d0f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067d0f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0067d138 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0067d138 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0067d138 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0067d138 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067d0f8 bytes 00303c91
+ 0067d138 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e74228b24e8b8a1cf04cc5f1e3d10a8f"></a>

### [`0067d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d100.md) → [`0067d140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d140.md) _INIT_97

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
      "definition_site": "0067d17c",
      "incomplete_value": true,
      "site": "0067d198",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d13c",
      "incomplete_value": true,
      "site": "0067d158",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d1a0",
      "incomplete_value": true,
      "site": "0067d1bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d160",
      "incomplete_value": true,
      "site": "0067d17c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d1c0",
      "incomplete_value": true,
      "site": "0067d1dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0067d180",
      "incomplete_value": true,
      "site": "0067d19c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0067d17c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0067d1a0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0067d1c0",
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
      "0067d17c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0067d1a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0067d1c0",
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

- 旧版 [`0067d178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d100.md#insn-0067d178) · [`0067d198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d100.md#insn-0067d198) · [`0067d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d100.md#insn-0067d260)
- 新版 `0067d1b8`（命令位置の公開資料なし） · `0067d1d8`（命令位置の公開資料なし） · `0067d2a0`（命令位置の公開資料なし）

~~~diff
- 0067d178 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0067d178 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067d178 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067d178 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067d1b8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0067d1b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067d1b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067d1b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067d178 bytes 4a093691
+ 0067d1b8 bytes 4a093791
- 0067d198 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0067d198 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0067d198 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0067d198 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0067d1d8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0067d1d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0067d1d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0067d1d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0067d198 bytes 4a553a91
+ 0067d1d8 bytes 4a893d91
- 0067d260 ["INT_ADD", "register:40f0:8", ["const:67d260:8", "const:4:8"]]
- 0067d260 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0067d2a0 ["INT_ADD", "register:40f0:8", ["const:67d2a0:8", "const:4:8"]]
+ 0067d2a0 ["CALL", null, ["callee:0043b7f8:8"]]
- 0067d260 bytes 56f9f697
+ 0067d2a0 bytes 56f9f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f255e362c0c84cc5937849fde07ac8d0"></a>

### [`0067d490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md) → [`0067d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d4d0.md) FUN_0067d4d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) · 呼出先 15件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) [`0067e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e370.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) · 呼出先 15件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) [`0067e3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e3b0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_value` 19件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0067d508",
      "incomplete_value": false,
      "site": "0067d518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067d4c8",
      "incomplete_value": false,
      "site": "0067d4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "0067d618",
      "incomplete_value": true,
      "site": "0067d618",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067d5d8",
      "incomplete_value": true,
      "site": "0067d5d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067d630",
      "incomplete_value": true,
      "site": "0067d630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067d5f0",
      "incomplete_value": true,
      "site": "0067d5f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed6:8"
              ]
            ]
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
      "0067d518",
      "DATA",
      [
        "storage",
        "00c743d8",
        null,
        "pointer"
      ]
    ],
    [
      "0067d5e8",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067d608",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067d518",
      "DATA",
      [
        "storage",
        "00c747d8",
        null,
        "pointer"
      ]
    ],
    [
      "0067d5e8",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067d608",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067d614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md#insn-0067d614) · [`0067d634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md#insn-0067d634) · [`0067d758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md#insn-0067d758)
- 新版 `0067d654`（命令位置の公開資料なし） · `0067d674`（命令位置の公開資料なし） · `0067d798`（命令位置の公開資料なし）

~~~diff
- 0067d614 ["INT_ADD", "register:40f0:8", ["const:67d614:8", "const:4:8"]]
- 0067d614 ["CALL", null, ["callee:00633374:8"]]
+ 0067d654 ["INT_ADD", "register:40f0:8", ["const:67d654:8", "const:4:8"]]
+ 0067d654 ["CALL", null, ["callee:00633374:8"]]
- 0067d614 bytes 48d7fe97
+ 0067d654 bytes 48d7fe97
- 0067d634 ["INT_ADD", "register:40f0:8", ["const:67d634:8", "const:4:8"]]
- 0067d634 ["CALL", null, ["callee:00c53d00:8"]]
+ 0067d674 ["INT_ADD", "register:40f0:8", ["const:67d674:8", "const:4:8"]]
+ 0067d674 ["CALL", null, ["callee:00c53d00:8"]]
- 0067d634 bytes ab581794
+ 0067d674 bytes a3591794
- 0067d758 ["INT_ADD", "register:40f0:8", ["const:67d758:8", "const:4:8"]]
- 0067d758 ["CALL", null, ["callee:00633374:8"]]
+ 0067d798 ["INT_ADD", "register:40f0:8", ["const:67d798:8", "const:4:8"]]
+ 0067d798 ["CALL", null, ["callee:00633374:8"]]
- 0067d758 bytes f7d6fe97
+ 0067d798 bytes f7d6fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fe5b3001e65e8959838055874569cb0"></a>

### [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) → [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) FUN_0067e19c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`0067d490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067d/0067d490.md) [`006b01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b0/006b01f8.md) [`0073b9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073b/0073b9bc.md) [`007548d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00754/007548d0.md) [`00758190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758190.md) · 呼出先 10件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00b2d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d874.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 13件 [`0067d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d4d0.md) [`006b0238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b0/006b0238.md) [`0073b9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b9fc.md) [`00754910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00754/00754910.md) [`007581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/007581d0.md) · 呼出先 10件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00b2dc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2dc9c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0067e1cc",
      "incomplete_value": false,
      "site": "0067e1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e18c",
      "incomplete_value": false,
      "site": "0067e190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "definition_site": "0067e210",
      "incomplete_value": true,
      "site": "0067e210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e1d0",
      "incomplete_value": true,
      "site": "0067e1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:785:8"
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
      "definition_site": "0067e228",
      "incomplete_value": true,
      "site": "0067e228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ffc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e1e8",
      "incomplete_value": true,
      "site": "0067e1e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fbc:8"
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
      "0067e1d0",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ],
    [
      "0067e1e0",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067e200",
      "READ",
      [
        "storage",
        "002ab785",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0067e1d0",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ],
    [
      "0067e1e0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0067e200",
      "READ",
      [
        "storage",
        "002ab7c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067e208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md#insn-0067e208) · [`0067e228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md#insn-0067e228) · [`0067e2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md#insn-0067e2b8)
- 新版 `0067e248`（命令位置の公開資料なし） · `0067e268`（命令位置の公開資料なし） · `0067e2f8`（命令位置の公開資料なし）

~~~diff
- 0067e208 ["INT_ADD", "register:40f0:8", ["const:67e208:8", "const:4:8"]]
- 0067e208 ["CALL", null, ["callee:0047e60c:8"]]
+ 0067e248 ["INT_ADD", "register:40f0:8", ["const:67e248:8", "const:4:8"]]
+ 0067e248 ["CALL", null, ["callee:0047e60c:8"]]
- 0067e208 bytes f100f897
+ 0067e248 bytes f100f897
- 0067e228 ["INT_ADD", "register:40f0:8", ["const:67e228:8", "const:4:8"]]
- 0067e228 ["CALL", null, ["callee:00c53d00:8"]]
+ 0067e268 ["INT_ADD", "register:40f0:8", ["const:67e268:8", "const:4:8"]]
+ 0067e268 ["CALL", null, ["callee:00c53d00:8"]]
- 0067e228 bytes ae551794
+ 0067e268 bytes a6561794
- 0067e2b8 ["INT_ADD", "register:40f0:8", ["const:67e2b8:8", "const:4:8"]]
- 0067e2b8 ["CALL", null, ["callee:00c57e80:8"]]
+ 0067e2f8 ["INT_ADD", "register:40f0:8", ["const:67e2f8:8", "const:4:8"]]
+ 0067e2f8 ["CALL", null, ["callee:00c57e80:8"]]
- 0067e2b8 bytes f2651794
+ 0067e2f8 bytes e2661794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1f35179f48481542c42cc238cf2e744"></a>

### [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) → [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) FUN_0067e7f8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 30件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 30件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 9件, `store_destination` 3件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0067e850",
      "incomplete_value": false,
      "site": "0067e850",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e810",
      "incomplete_value": false,
      "site": "0067e810",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0067e848",
      "incomplete_value": true,
      "site": "0067e850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e808",
      "incomplete_value": true,
      "site": "0067e810",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0067e854",
      "incomplete_value": false,
      "site": "0067e854",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067e814",
      "incomplete_value": false,
      "site": "0067e814",
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
            "const:578:8"
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
      "0067e848",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0067e84c",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "0067e850",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0067e848",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0067e84c",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "0067e850",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067e808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md#insn-0067e808) · [`0067e810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md#insn-0067e810) · [`0067e814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md#insn-0067e814)
- 新版 `0067e848`（命令位置の公開資料なし） · `0067e850`（命令位置の公開資料なし） · `0067e854`（命令位置の公開資料なし）

~~~diff
- 0067e808 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
- 0067e808 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0067e848 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
+ 0067e848 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0067e808 bytes c9be42f9
+ 0067e848 bytes c9be44f9
- 0067e810 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 0067e810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0067e850 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 0067e850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0067e810 bytes 09b502f9
+ 0067e850 bytes 09b504f9
- 0067e814 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
- 0067e814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0067e854 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
+ 0067e854 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0067e814 bytes cabe02f9
+ 0067e854 bytes cabe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf7dd73406eb87c417a86f77350da013"></a>

### [`0067fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md) → [`0067fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067fdac.md) FUN_0067fdac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 27件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 27件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0046ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee04.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.56% / 新版 94.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `call_target` 12件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00680804",
      "incomplete_value": true,
      "site": "00680808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:300:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006807c4",
      "incomplete_value": true,
      "site": "006807c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00680824",
      "incomplete_value": true,
      "site": "00680830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006807e4",
      "incomplete_value": true,
      "site": "006807f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 106,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068098c",
      "incomplete_value": true,
      "site": "00680990",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068094c",
      "incomplete_value": true,
      "site": "00680950",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0067fdf8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0067fe18",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0067fe20",
      "PARAM",
      [
        "storage",
        "00c743e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0067fdf8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0067fe18",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0067fe20",
      "PARAM",
      [
        "storage",
        "00c747e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md#insn-0067ff10) · [`006800b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md#insn-006800b8) · [`006801bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md#insn-006801bc)
- 新版 `0067ff50`（命令位置の公開資料なし） · `006800f8`（命令位置の公開資料なし） · `006801fc`（命令位置の公開資料なし）

~~~diff
- 0067ff10 ["INT_ADD", "register:40f0:8", ["const:67ff10:8", "const:4:8"]]
- 0067ff10 ["CALL", null, ["ram:47acb4:8"]]
+ 0067ff50 ["INT_ADD", "register:40f0:8", ["const:67ff50:8", "const:4:8"]]
+ 0067ff50 ["CALL", null, ["ram:47acf4:8"]]
- 0067ff10 bytes 69ebf797
+ 0067ff50 bytes 69ebf797
- 006800b8 ["INT_ADD", "register:40f0:8", ["const:6800b8:8", "const:4:8"]]
- 006800b8 ["CALL", null, ["ram:47acb4:8"]]
+ 006800f8 ["INT_ADD", "register:40f0:8", ["const:6800f8:8", "const:4:8"]]
+ 006800f8 ["CALL", null, ["ram:47acf4:8"]]
- 006800b8 bytes ffeaf797
+ 006800f8 bytes ffeaf797
- 006801bc ["INT_ADD", "register:40f0:8", ["const:6801bc:8", "const:4:8"]]
- 006801bc ["CALL", null, ["callee:00682464:8"]]
+ 006801fc ["INT_ADD", "register:40f0:8", ["const:6801fc:8", "const:4:8"]]
+ 006801fc ["CALL", null, ["callee:00682464:8"]]
- 006801bc bytes 9a080094
+ 006801fc bytes 9a080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e676607e014920069ba6c8a97e236b"></a>

### [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) → [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) FUN_00680e08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 41件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 41件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件, `call_target` 25件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00681f70",
      "incomplete_value": false,
      "site": "00681f70",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "00681f30",
      "incomplete_value": false,
      "site": "00681f30",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00681f74",
      "incomplete_value": false,
      "site": "00681f74",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00681f34",
      "incomplete_value": false,
      "site": "00681f34",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00681f70",
      "incomplete_value": false,
      "site": "00681f74",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "00681f30",
      "incomplete_value": false,
      "site": "00681f34",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
      "00680e48",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00680e54",
      "READ",
      [
        "storage",
        "00ca4b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00680e64",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00680e48",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00680e54",
      "READ",
      [
        "storage",
        "00ca4f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00680e64",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00680e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md#insn-00680e40) · [`00680e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md#insn-00680e7c) · [`00680ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md#insn-00680ee0)
- 新版 `00680e80`（命令位置の公開資料なし） · `00680ebc`（命令位置の公開資料なし） · `00680f20`（命令位置の公開資料なし）

~~~diff
- 00680e40 ["INT_ADD", "register:40f0:8", ["const:680e40:8", "const:4:8"]]
- 00680e40 ["CALL", null, ["callee:00c58610:8"]]
+ 00680e80 ["INT_ADD", "register:40f0:8", ["const:680e80:8", "const:4:8"]]
+ 00680e80 ["CALL", null, ["callee:00c58610:8"]]
- 00680e40 bytes f45c1794
+ 00680e80 bytes e45d1794
- 00680e7c ["INT_ADD", "register:40f0:8", ["const:680e7c:8", "const:4:8"]]
- 00680e7c ["CALL", null, ["ram:46c984:8"]]
+ 00680ebc ["INT_ADD", "register:40f0:8", ["const:680ebc:8", "const:4:8"]]
+ 00680ebc ["CALL", null, ["ram:46c9c4:8"]]
- 00680e7c bytes c2aef797
+ 00680ebc bytes c2aef797
- 00680ee0 ["INT_ADD", "register:40f0:8", ["const:680ee0:8", "const:4:8"]]
- 00680ee0 ["CALL", null, ["ram:46c984:8"]]
+ 00680f20 ["INT_ADD", "register:40f0:8", ["const:680f20:8", "const:4:8"]]
+ 00680f20 ["CALL", null, ["ram:46c9c4:8"]]
- 00680ee0 bytes a9aef797
+ 00680f20 bytes a9aef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7020441c26b973c002a2ffdc8d7b1bab"></a>

### [`00681fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md) → [`00681ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00681/00681ff8.md) FUN_00681ff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006821b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821b4.md) · 呼出先 6件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006821d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821d8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`006821f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/006821f4.md) · 呼出先 6件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682218.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.85% / 新版 96.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0068200c",
      "incomplete_value": false,
      "site": "00682014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00681fcc",
      "incomplete_value": false,
      "site": "00681fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "006821ac",
      "incomplete_value": false,
      "site": "006821b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068216c",
      "incomplete_value": false,
      "site": "00682170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "00682014",
      "DATA",
      [
        "storage",
        "00c743d8",
        null,
        "pointer"
      ]
    ],
    [
      "006821b0",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00682014",
      "DATA",
      [
        "storage",
        "00c747d8",
        null,
        "pointer"
      ]
    ],
    [
      "006821b0",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00682130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md#insn-00682130) · [`00681fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md#insn-00681fcc) · [`00681fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md#insn-00681fe8)
- 新版 `00682170`（命令位置の公開資料なし） · `0068200c`（命令位置の公開資料なし） · `00682028`（命令位置の公開資料なし）

~~~diff
- 00682130 ["INT_ADD", "register:40f0:8", ["const:682130:8", "const:4:8"]]
- 00682130 ["CALL", null, ["callee:00c53d00:8"]]
+ 00682170 ["INT_ADD", "register:40f0:8", ["const:682170:8", "const:4:8"]]
+ 00682170 ["CALL", null, ["callee:00c53d00:8"]]
- 00682130 bytes ec451794
+ 00682170 bytes e4461794
- 00681fcc ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00681fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00681fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00681fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0068200c ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0068200c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0068200c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0068200c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00681fcc bytes 08610f91
+ 0068200c bytes 08611f91
- 00681fe8 ["INT_ADD", "register:40f0:8", ["const:681fe8:8", "const:4:8"]]
- 00681fe8 ["CALL", null, ["callee:00682218:8"]]
+ 00682028 ["INT_ADD", "register:40f0:8", ["const:682028:8", "const:4:8"]]
+ 00682028 ["CALL", null, ["callee:00682218:8"]]
- 00681fe8 bytes 7c000094
+ 00682028 bytes 7c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c7f2532841f2dca6dc2886a9a09a72"></a>

### [`00682224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682224.md) → [`00682264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682264.md) FUN_00682264

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0068227c",
      "incomplete_value": false,
      "site": "00682280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0068223c",
      "incomplete_value": false,
      "site": "00682240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "00682280",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00682280",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068223c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682224.md#insn-0068223c) · [`00682250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682224.md#insn-00682250) · [`00682264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682224.md#insn-00682264)
- 新版 `0068227c`（命令位置の公開資料なし） · `00682290`（命令位置の公開資料なし） · `006822a4`（命令位置の公開資料なし）

~~~diff
- 0068223c ["COPY", "tmp:0:8", ["const:410:8"]]
- 0068223c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0068223c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0068223c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0068227c ["COPY", "tmp:0:8", ["const:810:8"]]
+ 0068227c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0068227c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0068227c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0068223c bytes 08411091
+ 0068227c bytes 08412091
- 00682250 ["INT_ADD", "register:40f0:8", ["const:682250:8", "const:4:8"]]
- 00682250 ["CALL", null, ["callee:00c53d00:8"]]
+ 00682290 ["INT_ADD", "register:40f0:8", ["const:682290:8", "const:4:8"]]
+ 00682290 ["CALL", null, ["callee:00c53d00:8"]]
- 00682250 bytes a4451794
+ 00682290 bytes 9c461794
- 00682264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00682264 ["INT_ADD", "register:40f0:8", ["const:682264:8", "const:4:8"]]
- 00682264 ["CALLIND", null, ["register:0:8"]]
+ 006822a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006822a4 ["INT_ADD", "register:40f0:8", ["const:6822a4:8", "const:4:8"]]
+ 006822a4 ["CALLIND", null, ["register:0:8"]]
- 00682264 bytes 00013fd6
+ 006822a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d11c56427c80acb0e4003da197fd90"></a>

### [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) → [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) FUN_00682324

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`00681fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md) [`00682224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682224.md) [`00682280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682280.md) [`00682400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682400.md) [`006b74cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b74cc.md) · 呼出先 4件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 27件 [`00681ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00681/00681ff8.md) [`00682264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682264.md) [`006822c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/006822c0.md) [`00682440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682440.md) [`006b750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b750c.md) · 呼出先 4件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00682340",
      "incomplete_value": false,
      "site": "00682344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00682300",
      "incomplete_value": false,
      "site": "00682304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "00682344",
      "DATA",
      [
        "storage",
        "00c74430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00682344",
      "DATA",
      [
        "storage",
        "00c74830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00682300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md#insn-00682300) · [`00682318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md#insn-00682318) · [`00682340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md#insn-00682340)
- 新版 `00682340`（命令位置の公開資料なし） · `00682358`（命令位置の公開資料なし） · `00682380`（命令位置の公開資料なし）

~~~diff
- 00682300 ["COPY", "tmp:0:8", ["const:430:8"]]
- 00682300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00682300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00682300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00682340 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00682340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00682340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00682340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00682300 bytes 08c11091
+ 00682340 bytes 08c12091
- 00682318 ["INT_ADD", "register:40f0:8", ["const:682318:8", "const:4:8"]]
- 00682318 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00682358 ["INT_ADD", "register:40f0:8", ["const:682358:8", "const:4:8"]]
+ 00682358 ["CALL", null, ["callee:00c57eb0:8"]]
- 00682318 bytes e6551794
+ 00682358 bytes d6561794
- 00682340 ["INT_ADD", "register:40f0:8", ["const:682340:8", "const:4:8"]]
- 00682340 ["CALL", null, ["callee:00c53d00:8"]]
+ 00682380 ["INT_ADD", "register:40f0:8", ["const:682380:8", "const:4:8"]]
+ 00682380 ["CALL", null, ["callee:00c53d00:8"]]
- 00682340 bytes 68451794
+ 00682380 bytes 60461794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0517828d3476d46b582d8608a0056f2"></a>

### [`00682568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682568.md) → [`006825a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/006825a8.md) _INIT_98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00682608",
      "incomplete_value": true,
      "site": "00682624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006825c8",
      "incomplete_value": true,
      "site": "006825e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00682684",
      "incomplete_value": true,
      "site": "006826a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00682644",
      "incomplete_value": true,
      "site": "00682660",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
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
      "definition_site": "006826a4",
      "incomplete_value": true,
      "site": "006826e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00682664",
      "incomplete_value": true,
      "site": "006826a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3c:8"
              ]
            ]
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
      "006825e4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00682608",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00682628",
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
      "006825e4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00682608",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00682628",
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

- 旧版 [`0068279c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682568.md#insn-0068279c) · [`00682594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682568.md#insn-00682594) · [`006825a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682568.md#insn-006825a0)
- 新版 `006827dc`（命令位置の公開資料なし） · `006825d4`（命令位置の公開資料なし） · `006825e0`（命令位置の公開資料なし）

~~~diff
- 0068279c ["INT_ADD", "register:40f0:8", ["const:68279c:8", "const:4:8"]]
- 0068279c ["CALL", null, ["callee:00c57e30:8"]]
+ 006827dc ["INT_ADD", "register:40f0:8", ["const:6827dc:8", "const:4:8"]]
+ 006827dc ["CALL", null, ["callee:00c57e30:8"]]
- 0068279c bytes a5541794
+ 006827dc bytes 95551794
- 00682594 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00682594 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00682594 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00682594 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006825d4 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 006825d4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006825d4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006825d4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00682594 bytes 73c20991
+ 006825d4 bytes 73c21991
- 006825a0 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 006825a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006825a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006825a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006825e0 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 006825e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006825e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006825e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006825a0 bytes 29993b91
+ 006825e0 bytes 29993c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673b92b936155ee6b03ef2f5f0d96200"></a>

### [`00682aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682aa4.md) → [`00682ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682ae4.md) FUN_00682ae4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0067fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md)
- 新版 呼出元 1件 [`0067fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067fdac.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.42% / 新版 96.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006833f4",
      "incomplete_value": false,
      "site": "006833f4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "006833b4",
      "incomplete_value": false,
      "site": "006833b4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 69,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006833f8",
      "incomplete_value": false,
      "site": "006833f8",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006833b8",
      "incomplete_value": false,
      "site": "006833b8",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006833f4",
      "incomplete_value": false,
      "site": "006833f8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "006833b4",
      "incomplete_value": false,
      "site": "006833b8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 70,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00682ce0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00682ebc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00682f78",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "00682ce0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00682ebc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00682f78",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00682c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682aa4.md#insn-00682c60) · [`00682ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682aa4.md#insn-00682ca0) · [`00682ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682aa4.md#insn-00682ce0)
- 新版 `00682ca0`（命令位置の公開資料なし） · `00682ce0`（命令位置の公開資料なし） · `00682d20`（命令位置の公開資料なし）

~~~diff
- 00682c60 ["INT_ADD", "register:40f0:8", ["const:682c60:8", "const:4:8"]]
- 00682c60 ["CALL", null, ["callee:00859b4c:8"]]
+ 00682ca0 ["INT_ADD", "register:40f0:8", ["const:682ca0:8", "const:4:8"]]
+ 00682ca0 ["CALL", null, ["callee:00859b4c:8"]]
- 00682c60 bytes ab5b0794
+ 00682ca0 bytes ab5b0794
- 00682ca0 ["INT_ADD", "register:40f0:8", ["const:682ca0:8", "const:4:8"]]
- 00682ca0 ["CALL", null, ["ram:46c984:8"]]
+ 00682ce0 ["INT_ADD", "register:40f0:8", ["const:682ce0:8", "const:4:8"]]
+ 00682ce0 ["CALL", null, ["ram:46c9c4:8"]]
- 00682ca0 bytes 39a7f797
+ 00682ce0 bytes 39a7f797
- 00682ce0 ["INT_ADD", "register:40f0:8", ["const:682ce0:8", "const:4:8"]]
- 00682ce0 ["CALL", null, ["callee:009dce40:8"]]
+ 00682d20 ["INT_ADD", "register:40f0:8", ["const:682d20:8", "const:4:8"]]
+ 00682d20 ["CALL", null, ["callee:009dce40:8"]]
- 00682ce0 bytes f1670d94
+ 00682d20 bytes 48680d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f1ad904750e227e21346a026cc6d34"></a>

### [`006834a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/006834a0.md) → [`006834e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00683/006834e0.md) FUN_006834e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)
- 新版 呼出元 1件 [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.60% / 新版 98.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068362c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006835ec",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006836ac",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068366c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006838b4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00683874",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 24,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068362c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006836ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00683780",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "0068362c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006836ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00683780",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006835ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/006834a0.md#insn-006835ec) · [`0068366c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/006834a0.md#insn-0068366c) · [`00683860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/006834a0.md#insn-00683860)
- 新版 `0068362c`（命令位置の公開資料なし） · `006836ac`（命令位置の公開資料なし） · `006838a0`（命令位置の公開資料なし）

~~~diff
- 006835ec ["INT_ADD", "register:40f0:8", ["const:6835ec:8", "const:4:8"]]
- 006835ec ["CALL", null, ["ram:46c984:8"]]
+ 0068362c ["INT_ADD", "register:40f0:8", ["const:68362c:8", "const:4:8"]]
+ 0068362c ["CALL", null, ["ram:46c9c4:8"]]
- 006835ec bytes e6a4f797
+ 0068362c bytes e6a4f797
- 0068366c ["INT_ADD", "register:40f0:8", ["const:68366c:8", "const:4:8"]]
- 0068366c ["CALL", null, ["ram:46c984:8"]]
+ 006836ac ["INT_ADD", "register:40f0:8", ["const:6836ac:8", "const:4:8"]]
+ 006836ac ["CALL", null, ["ram:46c9c4:8"]]
- 0068366c bytes c6a4f797
+ 006836ac bytes c6a4f797
- 00683860 ["INT_ADD", "register:40f0:8", ["const:683860:8", "const:4:8"]]
- 00683860 ["CALL", null, ["callee:00467860:8"]]
+ 006838a0 ["INT_ADD", "register:40f0:8", ["const:6838a0:8", "const:4:8"]]
+ 006838a0 ["CALL", null, ["callee:00467860:8"]]
- 00683860 bytes f08ff797
+ 006838a0 bytes f08ff797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4013202dca4c2ebf53f375734dd7e343"></a>

### [`00683a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683a7c.md) → [`00683abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00683/00683abc.md) FUN_00683abc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.40% / 新版 98.40%

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
      "site": "00683b68",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00683b28",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00683c3c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00683bfc",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00683b68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00683c3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00683b68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00683c3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00683b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683a7c.md#insn-00683b28) · [`00683bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683a7c.md#insn-00683bfc) · [`00683c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683a7c.md#insn-00683c3c)
- 新版 `00683b68`（命令位置の公開資料なし） · `00683c3c`（命令位置の公開資料なし） · `00683c7c`（命令位置の公開資料なし）

~~~diff
- 00683b28 ["INT_ADD", "register:40f0:8", ["const:683b28:8", "const:4:8"]]
- 00683b28 ["CALL", null, ["ram:46c984:8"]]
+ 00683b68 ["INT_ADD", "register:40f0:8", ["const:683b68:8", "const:4:8"]]
+ 00683b68 ["CALL", null, ["ram:46c9c4:8"]]
- 00683b28 bytes 97a3f797
+ 00683b68 bytes 97a3f797
- 00683bfc ["INT_ADD", "register:40f0:8", ["const:683bfc:8", "const:4:8"]]
- 00683bfc ["CALL", null, ["ram:46c984:8"]]
+ 00683c3c ["INT_ADD", "register:40f0:8", ["const:683c3c:8", "const:4:8"]]
+ 00683c3c ["CALL", null, ["ram:46c9c4:8"]]
- 00683bfc bytes 62a3f797
+ 00683c3c bytes 62a3f797
- 00683c3c ["INT_ADD", "register:40f0:8", ["const:683c3c:8", "const:4:8"]]
- 00683c3c ["CALL", null, ["callee:00468804:8"]]
+ 00683c7c ["INT_ADD", "register:40f0:8", ["const:683c7c:8", "const:4:8"]]
+ 00683c7c ["CALL", null, ["callee:00468804:8"]]
- 00683c3c bytes e292f797
+ 00683c7c bytes e292f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3445cf677ed96db9b097975c171319b6"></a>

### [`00683c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683c70.md) → [`00683cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00683/00683cb0.md) _INIT_99

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00683cec",
      "incomplete_value": true,
      "site": "00683d08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00683cac",
      "incomplete_value": true,
      "site": "00683cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00683cec",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00683d10",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00683d30",
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
      "00683cec",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00683d10",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00683d30",
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

- 旧版 [`00683d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683c70.md#insn-00683d08) · [`00683c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683c70.md#insn-00683c9c) · [`00683ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/00683c70.md#insn-00683ca4)
- 新版 `00683d48`（命令位置の公開資料なし） · `00683cdc`（命令位置の公開資料なし）

~~~diff
- 00683d08 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00683d08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00683d08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00683d08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00683d48 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00683d48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00683d48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00683d48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00683d08 bytes 4a553a91
+ 00683d48 bytes 4a893d91
- 00683c9c ["COPY", "tmp:0:8", ["const:288:8"]]
- 00683c9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00683c9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00683c9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00683cdc ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00683cdc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00683cdc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00683cdc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00683c9c bytes 73220a91
+ 00683cdc bytes 73221a91
- 00683ca4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00683ca4 bytes a9e1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d82cf26c0385dee00620b6538e081d2"></a>

### [`00684000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684000.md) → [`00684040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684040.md) _INIT_100

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0068407c",
      "incomplete_value": true,
      "site": "00684098",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0068403c",
      "incomplete_value": true,
      "site": "00684058",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006840c0",
      "incomplete_value": true,
      "site": "006840dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00684080",
      "incomplete_value": true,
      "site": "0068409c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006840e0",
      "incomplete_value": true,
      "site": "006840f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006840a0",
      "incomplete_value": true,
      "site": "006840b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
      "0068407c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006840a0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006840c0",
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
      "0068407c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006840a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006840c0",
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

- 旧版 [`00684078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684000.md#insn-00684078) · [`00684098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684000.md#insn-00684098) · [`00684234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684000.md#insn-00684234)
- 新版 `006840b8`（命令位置の公開資料なし） · `006840d8`（命令位置の公開資料なし） · `00684274`（命令位置の公開資料なし）

~~~diff
- 00684078 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00684078 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00684078 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00684078 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006840b8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006840b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006840b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006840b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00684078 bytes 4a093691
+ 006840b8 bytes 4a093791
- 00684098 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00684098 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00684098 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00684098 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006840d8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006840d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006840d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006840d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00684098 bytes 4a553a91
+ 006840d8 bytes 4a893d91
- 00684234 ["INT_ADD", "register:40f0:8", ["const:684234:8", "const:4:8"]]
- 00684234 ["CALL", null, ["callee:00c57e30:8"]]
+ 00684274 ["INT_ADD", "register:40f0:8", ["const:684274:8", "const:4:8"]]
+ 00684274 ["CALL", null, ["callee:00c57e30:8"]]
- 00684234 bytes ff4d1794
+ 00684274 bytes ef4e1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfeae142297d8cac511a2da450200ba5"></a>

### [`0068452c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/0068452c.md) → [`0068456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/0068456c.md) FUN_0068456c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 11件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`00684390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684390.md) [`00691a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/00691a8c.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 11件 [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`006843d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006843d0.md) [`00691acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691acc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.25% / 新版 84.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006845a4",
      "incomplete_value": false,
      "site": "006845a8",
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
      "definition_site": "00684564",
      "incomplete_value": false,
      "site": "00684568",
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
      "definition_site": "006845d0",
      "incomplete_value": true,
      "site": "006845d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00684590",
      "incomplete_value": true,
      "site": "00684590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e96:8"
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
      "definition_site": "006845c8",
      "incomplete_value": true,
      "site": "006845d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00684588",
      "incomplete_value": true,
      "site": "00684594",
      "value": [
        "LOAD",
        "8",
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
      "006845a8",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006845c0",
      "READ",
      [
        "storage",
        "002b0e96",
        null,
        "string"
      ]
    ],
    [
      "006845c8",
      "READ",
      [
        "storage",
        "002b0e9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006845a8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006845c0",
      "READ",
      [
        "storage",
        "002b0ed6",
        null,
        "string"
      ]
    ],
    [
      "006845c8",
      "READ",
      [
        "storage",
        "002b0edd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068465c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/0068452c.md#insn-0068465c) · [`006846d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/0068452c.md#insn-006846d0) · [`00684558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/0068452c.md#insn-00684558)
- 新版 `0068469c`（命令位置の公開資料なし） · `00684710`（命令位置の公開資料なし） · `00684598`（命令位置の公開資料なし）

~~~diff
- 0068465c ["INT_ADD", "register:40f0:8", ["const:68465c:8", "const:4:8"]]
- 0068465c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0068469c ["INT_ADD", "register:40f0:8", ["const:68469c:8", "const:4:8"]]
+ 0068469c ["CALL", null, ["callee:00c57eb0:8"]]
- 0068465c bytes 154d1794
+ 0068469c bytes 054e1794
- 006846d0 ["INT_ADD", "register:40f0:8", ["const:6846d0:8", "const:4:8"]]
- 006846d0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00684710 ["INT_ADD", "register:40f0:8", ["const:684710:8", "const:4:8"]]
+ 00684710 ["CALL", null, ["callee:00c57fb0:8"]]
- 006846d0 bytes 384d1794
+ 00684710 bytes 284e1794
- 00684558 ["INT_ADD", "register:40f0:8", ["const:684558:8", "const:4:8"]]
- 00684558 ["CALL", null, ["callee:00487e20:8"]]
+ 00684598 ["INT_ADD", "register:40f0:8", ["const:684598:8", "const:4:8"]]
+ 00684598 ["CALL", null, ["callee:00487e20:8"]]
- 00684558 bytes 220ef897
+ 00684598 bytes 220ef897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93a4bcde4ce93fd2d8d77731648409e"></a>

### [`006847bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md) → [`006847fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/006847fc.md) FUN_006847fc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00694ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ad4.md) · 呼出先 10件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`005c1804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00694b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694b14.md) · 呼出先 10件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`005c1844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1844.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006848f0",
      "incomplete_value": true,
      "site": "006848f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "006848b0",
      "incomplete_value": true,
      "site": "006848b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00684970",
      "incomplete_value": true,
      "site": "00684978",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00684930",
      "incomplete_value": true,
      "site": "00684938",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d0:8"
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
      "006848dc",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "00684970",
      "READ",
      [
        "storage",
        "002c29d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006848dc",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "00684970",
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068483c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md#insn-0068483c) · [`00684858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md#insn-00684858) · [`0068488c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/006847bc.md#insn-0068488c)
- 新版 `0068487c`（命令位置の公開資料なし） · `00684898`（命令位置の公開資料なし） · `006848cc`（命令位置の公開資料なし）

~~~diff
- 0068483c ["INT_ADD", "register:40f0:8", ["const:68483c:8", "const:4:8"]]
- 0068483c ["CALL", null, ["callee:00c57e90:8"]]
+ 0068487c ["INT_ADD", "register:40f0:8", ["const:68487c:8", "const:4:8"]]
+ 0068487c ["CALL", null, ["callee:00c57e90:8"]]
- 0068483c bytes 954c1794
+ 0068487c bytes 854d1794
- 00684858 ["INT_ADD", "register:40f0:8", ["const:684858:8", "const:4:8"]]
- 00684858 ["CALL", null, ["callee:00c58000:8"]]
+ 00684898 ["INT_ADD", "register:40f0:8", ["const:684898:8", "const:4:8"]]
+ 00684898 ["CALL", null, ["callee:00c58000:8"]]
- 00684858 bytes ea4c1794
+ 00684898 bytes da4d1794
- 0068488c ["INT_ADD", "register:40f0:8", ["const:68488c:8", "const:4:8"]]
- 0068488c ["CALL", null, ["callee:00470994:8"]]
+ 006848cc ["INT_ADD", "register:40f0:8", ["const:6848cc:8", "const:4:8"]]
+ 006848cc ["CALL", null, ["callee:00470994:8"]]
- 0068488c bytes 32b0f797
+ 006848cc bytes 32b0f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f15a1f08054788ea58bb2d7fb091c83"></a>

### [`00684a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684a68.md) → [`00684aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684aa8.md) FUN_00684aa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00685aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685aa4.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00685ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ae4.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00684b64",
      "incomplete_value": true,
      "site": "00684b64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:3bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00684b24",
      "incomplete_value": true,
      "site": "00684b24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:37d:8"
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
      "00684b54",
      "READ",
      [
        "storage",
        "002b637d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00684b54",
      "READ",
      [
        "storage",
        "002b63bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00684b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684a68.md#insn-00684b64) · [`00684acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684a68.md#insn-00684acc) · [`00684ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684a68.md#insn-00684ae8)
- 新版 `00684ba4`（命令位置の公開資料なし） · `00684b0c`（命令位置の公開資料なし） · `00684b28`（命令位置の公開資料なし）

~~~diff
- 00684b64 ["INT_ADD", "register:40f0:8", ["const:684b64:8", "const:4:8"]]
- 00684b64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00684ba4 ["INT_ADD", "register:40f0:8", ["const:684ba4:8", "const:4:8"]]
+ 00684ba4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00684b64 bytes d34b1794
+ 00684ba4 bytes c34c1794
- 00684acc ["INT_ADD", "register:40f0:8", ["const:684acc:8", "const:4:8"]]
- 00684acc ["CALL", null, ["callee:0044108c:8"]]
+ 00684b0c ["INT_ADD", "register:40f0:8", ["const:684b0c:8", "const:4:8"]]
+ 00684b0c ["CALL", null, ["callee:0044108c:8"]]
- 00684acc bytes 60f1f697
+ 00684b0c bytes 60f1f697
- 00684ae8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00684ae8 ["INT_ADD", "register:40f0:8", ["const:684ae8:8", "const:4:8"]]
- 00684ae8 ["CALLIND", null, ["register:0:8"]]
+ 00684b28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00684b28 ["INT_ADD", "register:40f0:8", ["const:684b28:8", "const:4:8"]]
+ 00684b28 ["CALLIND", null, ["register:0:8"]]
- 00684ae8 bytes 00013fd6
+ 00684b28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6785ca333038122ec43f6de371b22c77"></a>

### [`00685208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685208.md) → [`00685248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685248.md) FUN_00685248

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00692498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692498.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`006924d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/006924d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006852d8",
      "incomplete_value": false,
      "site": "006852dc",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00685298",
      "incomplete_value": false,
      "site": "0068529c",
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
            "const:d34:8"
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
      "006852d8",
      "PARAM",
      [
        "storage",
        "002b3d34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006852d8",
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068529c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685208.md#insn-0068529c) · [`00685290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685208.md#insn-00685290) · [`00685298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685208.md#insn-00685298)
- 新版 `006852dc`（命令位置の公開資料なし） · `006852d0`（命令位置の公開資料なし） · `006852d8`（命令位置の公開資料なし）

~~~diff
- 0068529c ["INT_ADD", "register:40f0:8", ["const:68529c:8", "const:4:8"]]
- 0068529c ["CALL", null, ["callee:00442930:8"]]
+ 006852dc ["INT_ADD", "register:40f0:8", ["const:6852dc:8", "const:4:8"]]
+ 006852dc ["CALL", null, ["callee:00442930:8"]]
- 0068529c bytes 95f5f697
+ 006852dc bytes 95f5f697
- 00685290 ["INT_ADD", "register:40f0:8", ["const:685290:8", "const:4:8"]]
- 00685290 ["CALL", null, ["callee:006924d8:8"]]
+ 006852d0 ["INT_ADD", "register:40f0:8", ["const:6852d0:8", "const:4:8"]]
+ 006852d0 ["CALL", null, ["callee:006924d8:8"]]
- 00685290 bytes 82340094
+ 006852d0 bytes 82340094
- 00685298 ["COPY", "tmp:0:8", ["const:d34:8"]]
- 00685298 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00685298 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00685298 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006852d8 ["COPY", "tmp:0:8", ["const:d74:8"]]
+ 006852d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006852d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006852d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00685298 bytes 00d03491
+ 006852d8 bytes 00d03591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

