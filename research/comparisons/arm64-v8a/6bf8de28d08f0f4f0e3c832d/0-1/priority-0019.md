# v16.0.0 → v16.0.1 · 最優先の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-f4030c8089c391ed7ff76e4b2e3f1f7e"></a>

### [`0058d798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d798.md) → [`0058d7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md) FUN_0058d7d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d834",
      "incomplete_value": true,
      "site": "0058d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d7f4",
      "incomplete_value": true,
      "site": "0058d7f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8de:8"
              ]
            ]
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
      "0058d828",
      "READ",
      [
        "storage",
        "002ad8de",
        null,
        "string"
      ]
    ],
    [
      "0058d848",
      "READ",
      [
        "storage",
        "002afb08",
        null,
        "string"
      ]
    ],
    [
      "0058d84c",
      "READ",
      [
        "storage",
        "002afb16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d828",
      "READ",
      [
        "storage",
        "002ad91e",
        null,
        "string"
      ]
    ],
    [
      "0058d848",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ],
    [
      "0058d84c",
      "READ",
      [
        "storage",
        "002afb56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d798.md#insn-0058d7c4) · [`0058d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d798.md#insn-0058d7cc) · [`0058d7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d798.md#insn-0058d7e4)
- 新版 [`0058d804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d804) · [`0058d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d80c) · [`0058d824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d824)

~~~diff
- 0058d7c4 ["INT_ADD", "register:40f0:8", ["const:58d7c4:8", "const:4:8"]]
- 0058d7c4 ["CALL", null, ["callee:00589840:8"]]
+ 0058d804 ["INT_ADD", "register:40f0:8", ["const:58d804:8", "const:4:8"]]
+ 0058d804 ["CALL", null, ["callee:00589840:8"]]
- 0058d7c4 bytes 0ff0ff97
+ 0058d804 bytes 0ff0ff97
- 0058d7cc ["INT_ADD", "register:40f0:8", ["const:58d7cc:8", "const:4:8"]]
- 0058d7cc ["CALL", null, ["callee:00588e6c:8"]]
+ 0058d80c ["INT_ADD", "register:40f0:8", ["const:58d80c:8", "const:4:8"]]
+ 0058d80c ["CALL", null, ["callee:00588e6c:8"]]
- 0058d7cc bytes 98edff97
+ 0058d80c bytes 98edff97
- 0058d7e4 ["COPY", "tmp:0:8", ["const:8de:8"]]
- 0058d7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058d7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058d7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058d824 ["COPY", "tmp:0:8", ["const:91e:8"]]
+ 0058d824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058d824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058d824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058d7e4 bytes 08792391
+ 0058d824 bytes 08792491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09cc5fce2dc11d2a703f08bdfa57a59"></a>

### [`0058d970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d970.md) → [`0058d9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md) FUN_0058d9b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058da24",
      "incomplete_value": true,
      "site": "0058da30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:547:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d9e4",
      "incomplete_value": true,
      "site": "0058d9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:507:8"
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
      "definition_site": "0058da34",
      "incomplete_value": true,
      "site": "0058da34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058d9f4",
      "incomplete_value": true,
      "site": "0058d9f4",
      "value": [
        "LOAD",
        "8",
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
      "0058da24",
      "READ",
      [
        "storage",
        "002bb507",
        null,
        "string"
      ]
    ],
    [
      "0058da28",
      "READ",
      [
        "storage",
        "002bb515",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058da24",
      "READ",
      [
        "storage",
        "002bb547",
        null,
        "string"
      ]
    ],
    [
      "0058da28",
      "READ",
      [
        "storage",
        "002bb555",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058da34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d970.md#insn-0058da34) · [`0058d9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d970.md#insn-0058d9a0) · [`0058d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d970.md#insn-0058d9ac)
- 新版 [`0058da74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058da74) · [`0058d9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058d9e0) · [`0058d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058d9ec)

~~~diff
- 0058da34 ["INT_ADD", "register:40f0:8", ["const:58da34:8", "const:4:8"]]
- 0058da34 ["CALL", null, ["callee:00589144:8"]]
+ 0058da74 ["INT_ADD", "register:40f0:8", ["const:58da74:8", "const:4:8"]]
+ 0058da74 ["CALL", null, ["callee:00589144:8"]]
- 0058da34 bytes b4edff97
+ 0058da74 bytes b4edff97
- 0058d9a0 ["INT_ADD", "register:40f0:8", ["const:58d9a0:8", "const:4:8"]]
- 0058d9a0 ["CALL", null, ["callee:00589840:8"]]
+ 0058d9e0 ["INT_ADD", "register:40f0:8", ["const:58d9e0:8", "const:4:8"]]
+ 0058d9e0 ["CALL", null, ["callee:00589840:8"]]
- 0058d9a0 bytes 98efff97
+ 0058d9e0 bytes 98efff97
- 0058d9ac ["INT_ADD", "register:40f0:8", ["const:58d9ac:8", "const:4:8"]]
- 0058d9ac ["CALL", null, ["callee:00588e6c:8"]]
+ 0058d9ec ["INT_ADD", "register:40f0:8", ["const:58d9ec:8", "const:4:8"]]
+ 0058d9ec ["CALL", null, ["callee:00588e6c:8"]]
- 0058d9ac bytes 20edff97
+ 0058d9ec bytes 20edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4e5efc053755b89c37dbb1b6e3e4c4"></a>

### [`0058db4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md) → [`0058db8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md) FUN_0058db8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dc00",
      "incomplete_value": true,
      "site": "0058dc08",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:40d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dbc0",
      "incomplete_value": true,
      "site": "0058dbc8",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:340:8"
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
      "definition_site": "0058dc0c",
      "incomplete_value": true,
      "site": "0058dc0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058dbcc",
      "incomplete_value": true,
      "site": "0058dbcc",
      "value": [
        "LOAD",
        "8",
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
      "0058dc00",
      "READ",
      [
        "storage",
        "002a4340",
        null,
        "string"
      ]
    ],
    [
      "0058dc04",
      "READ",
      [
        "storage",
        "002a434e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dc00",
      "READ",
      [
        "storage",
        "002a440d",
        null,
        "string"
      ]
    ],
    [
      "0058dc04",
      "READ",
      [
        "storage",
        "002a441b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md#insn-0058dc0c) · [`0058db78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md#insn-0058db78) · [`0058db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058db4c.md#insn-0058db80)
- 新版 [`0058dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dc4c) · [`0058dbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dbb8) · [`0058dbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dbc0)

~~~diff
- 0058dc0c ["INT_ADD", "register:40f0:8", ["const:58dc0c:8", "const:4:8"]]
- 0058dc0c ["CALL", null, ["callee:00589144:8"]]
+ 0058dc4c ["INT_ADD", "register:40f0:8", ["const:58dc4c:8", "const:4:8"]]
+ 0058dc4c ["CALL", null, ["callee:00589144:8"]]
- 0058dc0c bytes 3eedff97
+ 0058dc4c bytes 3eedff97
- 0058db78 ["INT_ADD", "register:40f0:8", ["const:58db78:8", "const:4:8"]]
- 0058db78 ["CALL", null, ["callee:00589840:8"]]
+ 0058dbb8 ["INT_ADD", "register:40f0:8", ["const:58dbb8:8", "const:4:8"]]
+ 0058dbb8 ["CALL", null, ["callee:00589840:8"]]
- 0058db78 bytes 22efff97
+ 0058dbb8 bytes 22efff97
- 0058db80 ["INT_ADD", "register:40f0:8", ["const:58db80:8", "const:4:8"]]
- 0058db80 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058dbc0 ["INT_ADD", "register:40f0:8", ["const:58dbc0:8", "const:4:8"]]
+ 0058dbc0 ["CALL", null, ["callee:00588e6c:8"]]
- 0058db80 bytes abecff97
+ 0058dbc0 bytes abecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b84a10ec0f30240a486ae63d4864636"></a>

### [`0058dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058dd20.md) → [`0058dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md) FUN_0058dd60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ddd0",
      "incomplete_value": true,
      "site": "0058ddd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dd90",
      "incomplete_value": true,
      "site": "0058dd98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:903:8"
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
      "definition_site": "0058dddc",
      "incomplete_value": true,
      "site": "0058dddc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058dd9c",
      "incomplete_value": true,
      "site": "0058dd9c",
      "value": [
        "LOAD",
        "8",
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
      "0058ddd0",
      "READ",
      [
        "storage",
        "002a7903",
        null,
        "string"
      ]
    ],
    [
      "0058ddd4",
      "READ",
      [
        "storage",
        "002a7911",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058ddd0",
      "READ",
      [
        "storage",
        "002a79df",
        null,
        "string"
      ]
    ],
    [
      "0058ddd4",
      "READ",
      [
        "storage",
        "002a79ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058dddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058dd20.md#insn-0058dddc) · [`0058dd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058dd20.md#insn-0058dd4c) · [`0058dd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058dd20.md#insn-0058dd54)
- 新版 [`0058de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058de1c) · [`0058dd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058dd8c) · [`0058dd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058dd94)

~~~diff
- 0058dddc ["INT_ADD", "register:40f0:8", ["const:58dddc:8", "const:4:8"]]
- 0058dddc ["CALL", null, ["callee:00589144:8"]]
+ 0058de1c ["INT_ADD", "register:40f0:8", ["const:58de1c:8", "const:4:8"]]
+ 0058de1c ["CALL", null, ["callee:00589144:8"]]
- 0058dddc bytes caecff97
+ 0058de1c bytes caecff97
- 0058dd4c ["INT_ADD", "register:40f0:8", ["const:58dd4c:8", "const:4:8"]]
- 0058dd4c ["CALL", null, ["callee:00589840:8"]]
+ 0058dd8c ["INT_ADD", "register:40f0:8", ["const:58dd8c:8", "const:4:8"]]
+ 0058dd8c ["CALL", null, ["callee:00589840:8"]]
- 0058dd4c bytes adeeff97
+ 0058dd8c bytes adeeff97
- 0058dd54 ["INT_ADD", "register:40f0:8", ["const:58dd54:8", "const:4:8"]]
- 0058dd54 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058dd94 ["INT_ADD", "register:40f0:8", ["const:58dd94:8", "const:4:8"]]
+ 0058dd94 ["CALL", null, ["callee:00588e6c:8"]]
- 0058dd54 bytes 36ecff97
+ 0058dd94 bytes 36ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cf4070d779ba03d416449828ac9a4c4"></a>

### [`0058def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058def0.md) → [`0058df30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md) FUN_0058df30

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.43% / 新版 89.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058df8c",
      "incomplete_value": true,
      "site": "0058df8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058df4c",
      "incomplete_value": true,
      "site": "0058df4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91a:8"
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
      "definition_site": "0058dfac",
      "incomplete_value": true,
      "site": "0058dfb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058df6c",
      "incomplete_value": true,
      "site": "0058df74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dfa8",
      "incomplete_value": true,
      "site": "0058dfb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:943:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058df68",
      "incomplete_value": true,
      "site": "0058df78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0058df7c",
      "READ",
      [
        "storage",
        "002a791a",
        null,
        "string"
      ]
    ],
    [
      "0058dfa8",
      "READ",
      [
        "storage",
        "002ac903",
        null,
        "string"
      ]
    ],
    [
      "0058dfa8",
      "READ",
      [
        "storage",
        "002ac913",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058df7c",
      "READ",
      [
        "storage",
        "002a79f6",
        null,
        "string"
      ]
    ],
    [
      "0058dfa8",
      "READ",
      [
        "storage",
        "002ac943",
        null,
        "string"
      ]
    ],
    [
      "0058dfa8",
      "READ",
      [
        "storage",
        "002ac953",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058def0.md#insn-0058df34) · [`0058dfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058def0.md#insn-0058dfb4) · [`0058dfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058def0.md#insn-0058dfcc)
- 新版 [`0058df74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058df74) · [`0058dff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058dff4) · [`0058e00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058e00c)

~~~diff
- 0058df34 ["COPY", "tmp:0:8", ["const:91a:8"]]
- 0058df34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058df34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058df34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058df74 ["COPY", "tmp:0:8", ["const:9f6:8"]]
+ 0058df74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058df74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058df74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058df34 bytes 29692491
+ 0058df74 bytes 29d92791
- 0058dfb4 ["INT_ADD", "register:40f0:8", ["const:58dfb4:8", "const:4:8"]]
- 0058dfb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058dff4 ["INT_ADD", "register:40f0:8", ["const:58dff4:8", "const:4:8"]]
+ 0058dff4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058dfb4 bytes bf261b94
+ 0058dff4 bytes af271b94
- 0058dfcc ["INT_ADD", "register:40f0:8", ["const:58dfcc:8", "const:4:8"]]
- 0058dfcc ["CALL", null, ["callee:00589144:8"]]
+ 0058e00c ["INT_ADD", "register:40f0:8", ["const:58e00c:8", "const:4:8"]]
+ 0058e00c ["CALL", null, ["callee:00589144:8"]]
- 0058dfcc bytes 4eecff97
+ 0058e00c bytes 4eecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a038dc4ff4df5235bb1e4e8b09094a"></a>

### [`0058e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e150.md) → [`0058e190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md) FUN_0058e190

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e1f4",
      "incomplete_value": true,
      "site": "0058e1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:929:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e1b4",
      "incomplete_value": true,
      "site": "0058e1b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e9:8"
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
      "definition_site": "0058e210",
      "incomplete_value": true,
      "site": "0058e218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e1d0",
      "incomplete_value": true,
      "site": "0058e1d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e20c",
      "incomplete_value": true,
      "site": "0058e21c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e1cc",
      "incomplete_value": true,
      "site": "0058e1dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f22:8"
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
      "0058e1e0",
      "READ",
      [
        "storage",
        "002ad8e9",
        null,
        "string"
      ]
    ],
    [
      "0058e20c",
      "READ",
      [
        "storage",
        "002b4f22",
        null,
        "string"
      ]
    ],
    [
      "0058e20c",
      "READ",
      [
        "storage",
        "002b4f32",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e1e0",
      "READ",
      [
        "storage",
        "002ad929",
        null,
        "string"
      ]
    ],
    [
      "0058e20c",
      "READ",
      [
        "storage",
        "002b4f62",
        null,
        "string"
      ]
    ],
    [
      "0058e20c",
      "READ",
      [
        "storage",
        "002b4f72",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e150.md#insn-0058e198) · [`0058e218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e150.md#insn-0058e218) · [`0058e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e150.md#insn-0058e230)
- 新版 [`0058e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e1d8) · [`0058e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e258) · [`0058e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e270)

~~~diff
- 0058e198 ["COPY", "tmp:0:8", ["const:8e9:8"]]
- 0058e198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e1d8 ["COPY", "tmp:0:8", ["const:929:8"]]
+ 0058e1d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e1d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e1d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e198 bytes 29a52391
+ 0058e1d8 bytes 29a52491
- 0058e218 ["INT_ADD", "register:40f0:8", ["const:58e218:8", "const:4:8"]]
- 0058e218 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058e258 ["INT_ADD", "register:40f0:8", ["const:58e258:8", "const:4:8"]]
+ 0058e258 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058e218 bytes 26261b94
+ 0058e258 bytes 16271b94
- 0058e230 ["INT_ADD", "register:40f0:8", ["const:58e230:8", "const:4:8"]]
- 0058e230 ["CALL", null, ["callee:00589144:8"]]
+ 0058e270 ["INT_ADD", "register:40f0:8", ["const:58e270:8", "const:4:8"]]
+ 0058e270 ["CALL", null, ["callee:00589144:8"]]
- 0058e230 bytes b5ebff97
+ 0058e270 bytes b5ebff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2cc4ed0756d9c44b781b9ed9a00954"></a>

### [`0058e338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e338.md) → [`0058e378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md) FUN_0058e378

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e3f4",
      "incomplete_value": true,
      "site": "0058e3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e3b4",
      "incomplete_value": true,
      "site": "0058e3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e3f0",
      "incomplete_value": true,
      "site": "0058e400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:64a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e3b0",
      "incomplete_value": true,
      "site": "0058e3c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60a:8"
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
      "definition_site": "0058e3f0",
      "incomplete_value": true,
      "site": "0058e400",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058e3b0",
      "incomplete_value": true,
      "site": "0058e3c0",
      "value": [
        "LOAD",
        "16",
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
      "0058e3f0",
      "READ",
      [
        "storage",
        "002ab60a",
        null,
        "string"
      ]
    ],
    [
      "0058e3f0",
      "READ",
      [
        "storage",
        "002ab61a",
        null,
        "string"
      ]
    ],
    [
      "0058e3f4",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e3f0",
      "READ",
      [
        "storage",
        "002ab64a",
        null,
        "string"
      ]
    ],
    [
      "0058e3f0",
      "READ",
      [
        "storage",
        "002ab65a",
        null,
        "string"
      ]
    ],
    [
      "0058e3f4",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e338.md#insn-0058e3fc) · [`0058e414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e338.md#insn-0058e414) · [`0058e36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e338.md#insn-0058e36c)
- 新版 [`0058e43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e43c) · [`0058e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e454) · [`0058e3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e3ac)

~~~diff
- 0058e3fc ["INT_ADD", "register:40f0:8", ["const:58e3fc:8", "const:4:8"]]
- 0058e3fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058e43c ["INT_ADD", "register:40f0:8", ["const:58e43c:8", "const:4:8"]]
+ 0058e43c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058e3fc bytes ad251b94
+ 0058e43c bytes 9d261b94
- 0058e414 ["INT_ADD", "register:40f0:8", ["const:58e414:8", "const:4:8"]]
- 0058e414 ["CALL", null, ["callee:00589144:8"]]
+ 0058e454 ["INT_ADD", "register:40f0:8", ["const:58e454:8", "const:4:8"]]
+ 0058e454 ["CALL", null, ["callee:00589144:8"]]
- 0058e414 bytes 3cebff97
+ 0058e454 bytes 3cebff97
- 0058e36c ["INT_ADD", "register:40f0:8", ["const:58e36c:8", "const:4:8"]]
- 0058e36c ["CALL", null, ["callee:00589840:8"]]
+ 0058e3ac ["INT_ADD", "register:40f0:8", ["const:58e3ac:8", "const:4:8"]]
+ 0058e3ac ["CALL", null, ["callee:00589840:8"]]
- 0058e36c bytes 25edff97
+ 0058e3ac bytes 25edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58af958749ab5e4a8f7c41cec732ce7c"></a>

### [`0058e708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e708.md) → [`0058e748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md) FUN_0058e748

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e7c4",
      "incomplete_value": true,
      "site": "0058e7cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e784",
      "incomplete_value": true,
      "site": "0058e78c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e7c0",
      "incomplete_value": true,
      "site": "0058e7d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e780",
      "incomplete_value": true,
      "site": "0058e790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
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
      "definition_site": "0058e7c0",
      "incomplete_value": true,
      "site": "0058e7d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058e780",
      "incomplete_value": true,
      "site": "0058e790",
      "value": [
        "LOAD",
        "16",
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
      "0058e7c0",
      "READ",
      [
        "storage",
        "002b4f62",
        null,
        "string"
      ]
    ],
    [
      "0058e7c0",
      "READ",
      [
        "storage",
        "002b4f72",
        null,
        "string"
      ]
    ],
    [
      "0058e7c4",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e7c0",
      "READ",
      [
        "storage",
        "002b4fa2",
        null,
        "string"
      ]
    ],
    [
      "0058e7c0",
      "READ",
      [
        "storage",
        "002b4fb2",
        null,
        "string"
      ]
    ],
    [
      "0058e7c4",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e708.md#insn-0058e7cc) · [`0058e73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e708.md#insn-0058e73c) · [`0058e744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e708.md#insn-0058e744)
- 新版 [`0058e80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e80c) · [`0058e77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e77c) · [`0058e784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e784)

~~~diff
- 0058e7cc ["INT_ADD", "register:40f0:8", ["const:58e7cc:8", "const:4:8"]]
- 0058e7cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058e80c ["INT_ADD", "register:40f0:8", ["const:58e80c:8", "const:4:8"]]
+ 0058e80c ["CALL", null, ["callee:00c57eb0:8"]]
- 0058e7cc bytes b9241b94
+ 0058e80c bytes a9251b94
- 0058e73c ["INT_ADD", "register:40f0:8", ["const:58e73c:8", "const:4:8"]]
- 0058e73c ["CALL", null, ["callee:00589840:8"]]
+ 0058e77c ["INT_ADD", "register:40f0:8", ["const:58e77c:8", "const:4:8"]]
+ 0058e77c ["CALL", null, ["callee:00589840:8"]]
- 0058e73c bytes 31ecff97
+ 0058e77c bytes 31ecff97
- 0058e744 ["INT_ADD", "register:40f0:8", ["const:58e744:8", "const:4:8"]]
- 0058e744 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058e784 ["INT_ADD", "register:40f0:8", ["const:58e784:8", "const:4:8"]]
+ 0058e784 ["CALL", null, ["callee:00588e6c:8"]]
- 0058e744 bytes bae9ff97
+ 0058e784 bytes bae9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be70b7da7bbf52e0c77a153cca75502"></a>

### [`0058e8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md) → [`0058e92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md) FUN_0058e92c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e988",
      "incomplete_value": true,
      "site": "0058e988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e948",
      "incomplete_value": true,
      "site": "0058e948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:297:8"
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
      "definition_site": "0058e9a8",
      "incomplete_value": true,
      "site": "0058e9b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e968",
      "incomplete_value": true,
      "site": "0058e970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "0058e9a4",
      "incomplete_value": true,
      "site": "0058e9b4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058e964",
      "incomplete_value": true,
      "site": "0058e974",
      "value": [
        "LOAD",
        "16",
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
      "0058e978",
      "READ",
      [
        "storage",
        "002c1297",
        null,
        "string"
      ]
    ],
    [
      "0058e9a4",
      "READ",
      [
        "storage",
        "002a4377",
        null,
        "string"
      ]
    ],
    [
      "0058e9a4",
      "READ",
      [
        "storage",
        "002a4387",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e978",
      "READ",
      [
        "storage",
        "002c12d7",
        null,
        "string"
      ]
    ],
    [
      "0058e9a4",
      "READ",
      [
        "storage",
        "002a4444",
        null,
        "string"
      ]
    ],
    [
      "0058e9a4",
      "READ",
      [
        "storage",
        "002a4454",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md#insn-0058e930) · [`0058e9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md#insn-0058e9b0) · [`0058e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e8ec.md#insn-0058e9c0)
- 新版 [`0058e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058e970) · [`0058e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058e9f0) · [`0058ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058ea00)

~~~diff
- 0058e930 ["COPY", "tmp:0:8", ["const:297:8"]]
- 0058e930 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e930 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e930 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e970 ["COPY", "tmp:0:8", ["const:2d7:8"]]
+ 0058e970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e930 bytes 295d0a91
+ 0058e970 bytes 295d0b91
- 0058e9b0 ["INT_ADD", "register:40f0:8", ["const:58e9b0:8", "const:4:8"]]
- 0058e9b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058e9f0 ["INT_ADD", "register:40f0:8", ["const:58e9f0:8", "const:4:8"]]
+ 0058e9f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058e9b0 bytes 40241b94
+ 0058e9f0 bytes 30251b94
- 0058e9c0 ["INT_ADD", "register:40f0:8", ["const:58e9c0:8", "const:4:8"]]
- 0058e9c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0058ea00 ["INT_ADD", "register:40f0:8", ["const:58ea00:8", "const:4:8"]]
+ 0058ea00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0058e9c0 bytes 3c241b94
+ 0058ea00 bytes 2c251b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c48c4b2cbb7821ed00313b4d17b430"></a>

### [`0058ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md) → [`0058ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md) FUN_0058ecc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) · 呼出先 2件 [`0058d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058d/0058d130.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) · 呼出先 2件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0058ece8",
      "incomplete_value": false,
      "site": "0058ecf4",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058eca8",
      "incomplete_value": false,
      "site": "0058ecb4",
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
            "const:bc0:8"
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
      "0058ecf4",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ecf4",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md#insn-0058ec9c) · [`0058eca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md#insn-0058eca8) · [`0058ecc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ec80.md#insn-0058ecc0)
- 新版 [`0058ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ecdc) · [`0058ece8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ece8) · [`0058ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ed00)

~~~diff
- 0058ec9c ["INT_ADD", "register:40f0:8", ["const:58ec9c:8", "const:4:8"]]
- 0058ec9c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058ecdc ["INT_ADD", "register:40f0:8", ["const:58ecdc:8", "const:4:8"]]
+ 0058ecdc ["CALL", null, ["callee:00c57e90:8"]]
- 0058ec9c bytes 7d231b94
+ 0058ecdc bytes 6d241b94
- 0058eca8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0058eca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058eca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058eca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ece8 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0058ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058eca8 bytes 08012f91
+ 0058ece8 bytes 08013f91
- 0058ecc0 ["INT_ADD", "register:40f0:8", ["const:58ecc0:8", "const:4:8"]]
- 0058ecc0 ["CALL", null, ["callee:0058d170:8"]]
+ 0058ed00 ["INT_ADD", "register:40f0:8", ["const:58ed00:8", "const:4:8"]]
+ 0058ed00 ["CALL", null, ["callee:0058d170:8"]]
- 0058ecc0 bytes 1cf9ff97
+ 0058ed00 bytes 1cf9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4932d2021499aef571ebc763affd3d97"></a>

### [`0058ee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ee60.md) → [`0058eea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md) FUN_0058eea0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e84.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00597ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec4.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ef0c",
      "incomplete_value": true,
      "site": "0058ef1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058eecc",
      "incomplete_value": true,
      "site": "0058eedc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0058eee8",
      "READ",
      [
        "storage",
        "002b748b",
        null,
        "string"
      ]
    ],
    [
      "0058ef0c",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058eee8",
      "READ",
      [
        "storage",
        "002b74cb",
        null,
        "string"
      ]
    ],
    [
      "0058ef0c",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ee84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ee60.md#insn-0058ee84) · [`0058ee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ee60.md#insn-0058ee8c) · [`0058eea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058ee60.md#insn-0058eea4)
- 新版 [`0058eec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eec4) · [`0058eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eecc) · [`0058eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eee4)

~~~diff
- 0058ee84 ["INT_ADD", "register:40f0:8", ["const:58ee84:8", "const:4:8"]]
- 0058ee84 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058eec4 ["INT_ADD", "register:40f0:8", ["const:58eec4:8", "const:4:8"]]
+ 0058eec4 ["CALL", null, ["callee:00588e6c:8"]]
- 0058ee84 bytes eae7ff97
+ 0058eec4 bytes eae7ff97
- 0058ee8c ["INT_ADD", "register:40f0:8", ["const:58ee8c:8", "const:4:8"]]
- 0058ee8c ["CALL", null, ["callee:0058915c:8"]]
+ 0058eecc ["INT_ADD", "register:40f0:8", ["const:58eecc:8", "const:4:8"]]
+ 0058eecc ["CALL", null, ["callee:0058915c:8"]]
- 0058ee8c bytes a4e8ff97
+ 0058eecc bytes a4e8ff97
- 0058eea4 ["COPY", "tmp:0:8", ["const:48b:8"]]
- 0058eea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058eea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058eea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058eee4 ["COPY", "tmp:0:8", ["const:4cb:8"]]
+ 0058eee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058eee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058eee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058eea4 bytes 082d1291
+ 0058eee4 bytes 082d1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20beffac818e1ece665676dd9d32004d"></a>

### [`0058f00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f00c.md) → [`0058f04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md) FUN_0058f04c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f0c0",
      "incomplete_value": true,
      "site": "0058f0cc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f080",
      "incomplete_value": true,
      "site": "0058f08c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:940:8"
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
      "0058f0bc",
      "READ",
      [
        "storage",
        "002a2091",
        null,
        "string"
      ]
    ],
    [
      "0058f0bc",
      "READ",
      [
        "storage",
        "002a20a1",
        null,
        "string"
      ]
    ],
    [
      "0058f0c0",
      "READ",
      [
        "storage",
        "002c2940",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058f0bc",
      "READ",
      [
        "storage",
        "002a215e",
        null,
        "string"
      ]
    ],
    [
      "0058f0bc",
      "READ",
      [
        "storage",
        "002a216e",
        null,
        "string"
      ]
    ],
    [
      "0058f0c0",
      "READ",
      [
        "storage",
        "002c2980",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f00c.md#insn-0058f038) · [`0058f040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f00c.md#insn-0058f040) · [`0058f06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f00c.md#insn-0058f06c)
- 新版 [`0058f078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f078) · [`0058f080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f080) · [`0058f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f0ac)

~~~diff
- 0058f038 ["INT_ADD", "register:40f0:8", ["const:58f038:8", "const:4:8"]]
- 0058f038 ["CALL", null, ["callee:00588e6c:8"]]
+ 0058f078 ["INT_ADD", "register:40f0:8", ["const:58f078:8", "const:4:8"]]
+ 0058f078 ["CALL", null, ["callee:00588e6c:8"]]
- 0058f038 bytes 7de7ff97
+ 0058f078 bytes 7de7ff97
- 0058f040 ["INT_ADD", "register:40f0:8", ["const:58f040:8", "const:4:8"]]
- 0058f040 ["CALL", null, ["callee:0058915c:8"]]
+ 0058f080 ["INT_ADD", "register:40f0:8", ["const:58f080:8", "const:4:8"]]
+ 0058f080 ["CALL", null, ["callee:0058915c:8"]]
- 0058f040 bytes 37e8ff97
+ 0058f080 bytes 37e8ff97
- 0058f06c ["INT_ADD", "register:40f0:8", ["const:58f06c:8", "const:4:8"]]
- 0058f06c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058f0ac ["INT_ADD", "register:40f0:8", ["const:58f0ac:8", "const:4:8"]]
+ 0058f0ac ["CALL", null, ["callee:00c57e90:8"]]
- 0058f06c bytes 89221b94
+ 0058f0ac bytes 79231b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636e88adf4f2b731c4c942258ce3be2d"></a>

### [`0058f268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f268.md) → [`0058f2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f2a8.md) Java_jp_co_ponos_battlecats_MyActivity_shareComplete

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058f2cc",
      "incomplete_value": true,
      "site": "0058f2cc",
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
      "definition_site": "0058f28c",
      "incomplete_value": true,
      "site": "0058f28c",
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
              [
                "leaf",
                "const:ca6000:8"
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
    "guard": [
      [
        "FALL_THROUGH",
        "0058f28c"
      ],
      [
        "FALL_THROUGH",
        "0058f2cc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0058f2cc",
      "incomplete_value": true,
      "site": "0058f2e4",
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
      "definition_site": "0058f28c",
      "incomplete_value": true,
      "site": "0058f2a4",
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
              [
                "leaf",
                "const:ca6000:8"
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
      "0058f2c8",
      "READ",
      [
        "storage",
        "00ca6000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f2c8",
      "READ",
      [
        "storage",
        "00ca6400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f268.md#insn-0058f2cc) · [`0058f288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f268.md#insn-0058f288) · [`0058f2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f268.md#insn-0058f2a8)
- 新版 [`0058f30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f2a8.md#insn-0058f30c) · [`0058f2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f2a8.md#insn-0058f2c8) · [`0058f2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f2a8.md#insn-0058f2e8)

~~~diff
- 0058f2cc ["INT_ADD", "register:40f0:8", ["const:58f2cc:8", "const:4:8"]]
- 0058f2cc ["CALL", null, ["callee:00c57ee0:8"]]
+ 0058f30c ["INT_ADD", "register:40f0:8", ["const:58f30c:8", "const:4:8"]]
+ 0058f30c ["CALL", null, ["callee:00c57ee0:8"]]
- 0058f2cc bytes 05221b94
+ 0058f30c bytes f5221b94
- 0058f288 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0058f288 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058f2c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
+ 0058f2c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0058f288 bytes 000140f9
+ 0058f2c8 bytes 000142f9
- 0058f2a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f2a8 ["INT_ADD", "register:40f0:8", ["const:58f2a8:8", "const:4:8"]]
- 0058f2a8 ["CALLIND", null, ["register:0:8"]]
+ 0058f2e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f2e8 ["INT_ADD", "register:40f0:8", ["const:58f2e8:8", "const:4:8"]]
+ 0058f2e8 ["CALLIND", null, ["register:0:8"]]
- 0058f2a8 bytes 00013fd6
+ 0058f2e8 bytes 00013fd6
~~~


<a id="compare-1c7a3afb198e1fc1182089aa89eace34"></a>

### [`0058f5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f5f8.md) → [`0058f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f638.md) FUN_0058f638

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
      "definition_site": "0058f63c",
      "incomplete_value": false,
      "site": "0058f640",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f5fc",
      "incomplete_value": false,
      "site": "0058f600",
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
            "const:bc0:8"
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
      "0058f640",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f640",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f5f8.md#insn-0058f5fc)
- 新版 [`0058f63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f638.md#insn-0058f63c)

~~~diff
- 0058f5fc ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0058f5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f63c ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0058f63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f5fc bytes 08012f91
+ 0058f63c bytes 08013f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10d1c5cc659a777207b8776efe75eb7"></a>

### [`0058f608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f608.md) → [`0058f648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md) FUN_0058f648

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
      "definition_site": "0058f658",
      "incomplete_value": false,
      "site": "0058f660",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f618",
      "incomplete_value": false,
      "site": "0058f620",
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
            "const:bc0:8"
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
      "0058f660",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f660",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f608.md#insn-0058f618) · [`0058f624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f608.md#insn-0058f624)
- 新版 [`0058f658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md#insn-0058f658) · [`0058f664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md#insn-0058f664)

~~~diff
- 0058f618 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0058f618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f658 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0058f658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f618 bytes 08012f91
+ 0058f658 bytes 08013f91
- 0058f624 ["INT_ADD", "register:40f0:8", ["const:58f624:8", "const:4:8"]]
- 0058f624 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0058f664 ["INT_ADD", "register:40f0:8", ["const:58f664:8", "const:4:8"]]
+ 0058f664 ["CALL", null, ["callee:00c57ea0:8"]]
- 0058f624 bytes 1f211b94
+ 0058f664 bytes 0f221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b12167b304d63c56cfbb36837afccdf5"></a>

### [`0058f638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f638.md) → [`0058f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md) FUN_0058f678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)

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
      "definition_site": "0058f688",
      "incomplete_value": false,
      "site": "0058f690",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f648",
      "incomplete_value": false,
      "site": "0058f650",
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
            "const:b38:8"
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
      "0058f690",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f690",
      "DATA",
      [
        "storage",
        "00c6cf38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f638.md#insn-0058f648) · [`0058f658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f638.md#insn-0058f658)
- 新版 [`0058f688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md#insn-0058f688) · [`0058f698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md#insn-0058f698)

~~~diff
- 0058f648 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0058f648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f688 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0058f688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f648 bytes 08e12c91
+ 0058f688 bytes 08e13c91
- 0058f658 ["INT_ADD", "register:40f0:8", ["const:58f658:8", "const:4:8"]]
- 0058f658 ["CALL", null, ["callee:0058a8bc:8"]]
+ 0058f698 ["INT_ADD", "register:40f0:8", ["const:58f698:8", "const:4:8"]]
+ 0058f698 ["CALL", null, ["callee:0058a8bc:8"]]
- 0058f658 bytes 89ecff97
+ 0058f698 bytes 89ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7819c1a19d72c7450e491e7dd0a0ac7e"></a>

### [`0058f670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md) → [`0058f6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md) _INIT_34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0057a918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a918.md) [`0058cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc40.md) [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a958.md) [`0058cc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cc80.md) [`00bfa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f6dc",
      "incomplete_value": false,
      "site": "0058f6dc",
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
                "const:398:8"
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
      "definition_site": "0058f69c",
      "incomplete_value": false,
      "site": "0058f69c",
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
                "const:f98:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f6e0",
      "incomplete_value": false,
      "site": "0058f6e0",
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
                "const:398:8"
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
      "definition_site": "0058f6a0",
      "incomplete_value": false,
      "site": "0058f6a0",
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
                "const:f98:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f6e4",
      "incomplete_value": false,
      "site": "0058f6e4",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f6a4",
      "incomplete_value": false,
      "site": "0058f6a4",
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
      "0058f6c0",
      "PARAM",
      [
        "storage",
        "00ca5f98",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f6d4",
      "PARAM",
      [
        "storage",
        "0057a918",
        null,
        null
      ]
    ],
    [
      "0058f6d8",
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
      "0058f6c0",
      "PARAM",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f6d4",
      "PARAM",
      [
        "storage",
        "0057a958",
        null,
        null
      ]
    ],
    [
      "0058f6d8",
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

- 旧版 [`0058f680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md#insn-0058f680) · [`0058f6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md#insn-0058f6a8) · [`0058f6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md#insn-0058f6c0)
- 新版 [`0058f6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f6c0) · [`0058f6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f6e8) · [`0058f700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f700)

~~~diff
- 0058f680 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0058f680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058f680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058f680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058f6c0 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0058f6c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058f6c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058f6c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058f680 bytes 21603e91
+ 0058f6c0 bytes 21600e91
- 0058f6a8 ["INT_ADD", "register:40f0:8", ["const:58f6a8:8", "const:4:8"]]
- 0058f6a8 ["CALL", null, ["callee:00c57e30:8"]]
+ 0058f6e8 ["INT_ADD", "register:40f0:8", ["const:58f6e8:8", "const:4:8"]]
+ 0058f6e8 ["CALL", null, ["callee:00c57e30:8"]]
- 0058f6a8 bytes e2201b94
+ 0058f6e8 bytes d2211b94
- 0058f6c0 ["INT_ADD", "register:40f0:8", ["const:58f6c0:8", "const:4:8"]]
- 0058f6c0 ["CALL", null, ["callee:00c57e30:8"]]
+ 0058f700 ["INT_ADD", "register:40f0:8", ["const:58f700:8", "const:4:8"]]
+ 0058f700 ["CALL", null, ["callee:00c57e30:8"]]
- 0058f6c0 bytes dc201b94
+ 0058f700 bytes cc211b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e1456ac89c6e06339e0364d261a839"></a>

### [`0058f748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md) → [`0058f788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md) FUN_0058f788

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f7e0",
      "incomplete_value": false,
      "site": "0058f7e0",
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
                "const:474:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f7a0",
      "incomplete_value": false,
      "site": "0058f7a0",
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
                "const:74:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f7e8",
      "incomplete_value": false,
      "site": "0058f7e8",
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
                "const:474:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f7a8",
      "incomplete_value": false,
      "site": "0058f7a8",
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
                "const:74:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058f898",
      "incomplete_value": true,
      "site": "0058f898",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f858",
      "incomplete_value": true,
      "site": "0058f858",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
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
      "0058f7d4",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7e0",
      "WRITE",
      [
        "storage",
        "00ca6080",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7e8",
      "WRITE",
      [
        "storage",
        "00ca6078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f7d4",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7e0",
      "WRITE",
      [
        "storage",
        "00ca6480",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f7e8",
      "WRITE",
      [
        "storage",
        "00ca6478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md#insn-0058f858) · [`0058f870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md#insn-0058f870) · [`0058f78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md#insn-0058f78c)
- 新版 [`0058f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f898) · [`0058f8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f8b0) · [`0058f7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f7cc)

~~~diff
- 0058f858 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f858 ["INT_ADD", "register:40f0:8", ["const:58f858:8", "const:4:8"]]
- 0058f858 ["CALLIND", null, ["register:0:8"]]
+ 0058f898 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f898 ["INT_ADD", "register:40f0:8", ["const:58f898:8", "const:4:8"]]
+ 0058f898 ["CALLIND", null, ["register:0:8"]]
- 0058f858 bytes 00013fd6
+ 0058f898 bytes 00013fd6
- 0058f870 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f870 ["INT_ADD", "register:40f0:8", ["const:58f870:8", "const:4:8"]]
- 0058f870 ["CALLIND", null, ["register:0:8"]]
+ 0058f8b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f8b0 ["INT_ADD", "register:40f0:8", ["const:58f8b0:8", "const:4:8"]]
+ 0058f8b0 ["CALLIND", null, ["register:0:8"]]
- 0058f870 bytes 00013fd6
+ 0058f8b0 bytes 00013fd6
- 0058f78c ["COPY", "tmp:0:8", ["const:74:8"]]
- 0058f78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f7cc ["COPY", "tmp:0:8", ["const:474:8"]]
+ 0058f7cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f7cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f7cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f78c bytes 08d10191
+ 0058f7cc bytes 08d11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90ea3d3ededdb9e1fc73306048cf7c17"></a>

### [`0058f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md) → [`0058f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md) FUN_0058f900

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f9dc",
      "incomplete_value": false,
      "site": "0058f9dc",
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
                "const:518:8"
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
      "definition_site": "0058f99c",
      "incomplete_value": false,
      "site": "0058f99c",
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
                "const:118:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f9e4",
      "incomplete_value": false,
      "site": "0058f9e4",
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
                "const:518:8"
              ]
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
      "definition_site": "0058f9a4",
      "incomplete_value": false,
      "site": "0058f9a4",
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
                "const:118:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "0058f9e4",
      "incomplete_value": false,
      "site": "0058f9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058f9a4",
      "incomplete_value": false,
      "site": "0058f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058f920",
      "READ",
      [
        "storage",
        "00ca6030",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f948",
      "READ",
      [
        "storage",
        "00ca6038",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f94c",
      "WRITE",
      [
        "storage",
        "00ca6030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f920",
      "READ",
      [
        "storage",
        "00ca6430",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f948",
      "READ",
      [
        "storage",
        "00ca6438",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f94c",
      "WRITE",
      [
        "storage",
        "00ca6430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md#insn-0058f95c) · [`0058f968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md#insn-0058f968) · [`0058f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md#insn-0058f988)
- 新版 [`0058f99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f99c) · [`0058f9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f9a8) · [`0058f9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f9c8)

~~~diff
- 0058f95c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:110:8"]]
- 0058f95c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058f99c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 0058f99c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0058f95c bytes 808a40f9
+ 0058f99c bytes 808a42f9
- 0058f968 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f968 ["INT_ADD", "register:40f0:8", ["const:58f968:8", "const:4:8"]]
- 0058f968 ["CALLIND", null, ["register:0:8"]]
+ 0058f9a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f9a8 ["INT_ADD", "register:40f0:8", ["const:58f9a8:8", "const:4:8"]]
+ 0058f9a8 ["CALLIND", null, ["register:0:8"]]
- 0058f968 bytes 00013fd6
+ 0058f9a8 bytes 00013fd6
- 0058f988 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0058f988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f9c8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0058f9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f988 bytes 08010391
+ 0058f9c8 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4099135d192caf84a10fb2630dcfcb3"></a>

### [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) → [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) FUN_0058fa48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043afbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) [`0043b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b26c.md) [`00467d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d04.md) · 呼出先 5件 [`0058f748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f748.md) [`0058f8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f8c0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0043affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043affc.md) [`0043b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b2ac.md) [`00467d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d44.md) · 呼出先 5件 [`0058f788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md) [`0058f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.16% / 新版 81.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa88",
      "incomplete_value": false,
      "site": "0058fa88",
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
            "const:45c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa48",
      "incomplete_value": false,
      "site": "0058fa48",
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
            "const:5c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa90",
      "incomplete_value": false,
      "site": "0058fa90",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa50",
      "incomplete_value": false,
      "site": "0058fa50",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa98",
      "incomplete_value": false,
      "site": "0058fa98",
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
            "const:464:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa58",
      "incomplete_value": false,
      "site": "0058fa58",
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
            "const:64:8"
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
      "0058fa88",
      "WRITE",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa90",
      "WRITE",
      [
        "storage",
        "00ca6060",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa98",
      "WRITE",
      [
        "storage",
        "00ca6064",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fa88",
      "WRITE",
      [
        "storage",
        "00ca645c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa90",
      "WRITE",
      [
        "storage",
        "00ca6460",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fa98",
      "WRITE",
      [
        "storage",
        "00ca6464",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md#insn-0058fa48) · [`0058fa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md#insn-0058fa50) · [`0058fa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md#insn-0058fa58)
- 新版 [`0058fa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa88) · [`0058fa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa90) · [`0058fa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa98)

~~~diff
- 0058fa48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c:8"]]
- 0058fa48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
+ 0058fa88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:45c:8"]]
+ 0058fa88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0058fa48 bytes 045d00b9
+ 0058fa88 bytes 045d04b9
- 0058fa50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
- 0058fa50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
+ 0058fa90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:460:8"]]
+ 0058fa90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0058fa50 bytes 056100b9
+ 0058fa90 bytes 056104b9
- 0058fa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:64:8"]]
- 0058fa58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0058fa98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:464:8"]]
+ 0058fa98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0058fa58 bytes 006500b9
+ 0058fa98 bytes 006504b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cace7b90d9926a31f0a3be2d4c076083"></a>

### [`0058fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md) → [`0058fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md) FUN_0058fb80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0061a08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a08c.md) [`008ab8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab8a4.md) [`008ac918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md) [`008d92c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92c8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0061a0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a0cc.md) [`008ab8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab8e8.md) [`008ac95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac95c.md) [`008d9464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9464.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb9c",
      "incomplete_value": false,
      "site": "0058fb9c",
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
            "const:464:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fb5c",
      "incomplete_value": false,
      "site": "0058fb5c",
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
            "const:64:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fba4",
      "incomplete_value": false,
      "site": "0058fba4",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fb64",
      "incomplete_value": false,
      "site": "0058fb64",
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
            "const:68:8"
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
      "definition_site": "0058fbb0",
      "incomplete_value": false,
      "site": "0058fbb0",
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
            "const:46c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fb70",
      "incomplete_value": false,
      "site": "0058fb70",
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
            "const:6c:8"
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
      "0058fb90",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb9c",
      "WRITE",
      [
        "storage",
        "00ca6064",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fba4",
      "WRITE",
      [
        "storage",
        "00ca6068",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fb90",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb9c",
      "WRITE",
      [
        "storage",
        "00ca6464",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fba4",
      "WRITE",
      [
        "storage",
        "00ca6468",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md#insn-0058fb5c) · [`0058fb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md#insn-0058fb64) · [`0058fb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md#insn-0058fb70)
- 新版 [`0058fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fb9c) · [`0058fba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fba4) · [`0058fbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fbb0)

~~~diff
- 0058fb5c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:64:8"]]
- 0058fb5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0058fb9c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:464:8"]]
+ 0058fb9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0058fb5c bytes 886500b9
+ 0058fb9c bytes 886504b9
- 0058fb64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
- 0058fb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0058fba4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:468:8"]]
+ 0058fba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0058fb64 bytes 096900b9
+ 0058fba4 bytes 096904b9
- 0058fb70 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:6c:8"]]
- 0058fb70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0058fbb0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:46c:8"]]
+ 0058fbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0058fb70 bytes 4b6d00b9
+ 0058fbb0 bytes 4b6d04b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ee77c9f0e39c919e26dd7935f65716"></a>

### [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) → [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) FUN_0058fbc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00591af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591af4.md) [`00591b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591b80.md) [`00591c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md) [`00591d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00591b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md) [`00591bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591bc0.md) [`00591c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md) [`00591dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 38.71% / 新版 38.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fbfc",
      "incomplete_value": false,
      "site": "0058fbfc",
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
                "const:518:8"
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
      "definition_site": "0058fbbc",
      "incomplete_value": false,
      "site": "0058fbbc",
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
                "const:118:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fc00",
      "incomplete_value": false,
      "site": "0058fc00",
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
                "const:518:8"
              ]
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
      "definition_site": "0058fbc0",
      "incomplete_value": false,
      "site": "0058fbc0",
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
                "const:118:8"
              ]
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fc00",
      "incomplete_value": false,
      "site": "0058fc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058fbc0",
      "incomplete_value": false,
      "site": "0058fbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "0058fbd4",
      "READ",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fbe8",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fbe8",
      "READ",
      [
        "storage",
        "00ca60c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fbd4",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fbe8",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fbe8",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md#insn-0058fbb0) · [`0058fbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md#insn-0058fbec)
- 新版 [`0058fbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md#insn-0058fbf0) · [`0058fbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md#insn-0058fbe4) · [`0058fc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md#insn-0058fc2c)

~~~diff
- 0058fbb0 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0058fbb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058fbb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058fbb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058fbf0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0058fbf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058fbf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058fbf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058fbb0 bytes 21600491
+ 0058fbf0 bytes 21601491
+ 0058fbe4 ["COPY", "register:4048:8", ["const:ca6000:8"]]
+ 0058fbe4 bytes a93800f0
- 0058fbec ["COPY", "register:0:8", ["register:4040:8"]]
- 0058fbec ["INT_ADD", "register:40f0:8", ["const:58fbec:8", "const:4:8"]]
- 0058fbec ["CALLIND", null, ["register:0:8"]]
+ 0058fc2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058fc2c ["INT_ADD", "register:40f0:8", ["const:58fc2c:8", "const:4:8"]]
+ 0058fc2c ["CALLIND", null, ["register:0:8"]]
- 0058fbec bytes 00013fd6
+ 0058fc2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81615b4698b6604a58485c674cc4a3cd"></a>

### [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) → [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) FUN_0058fcd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 44.00% / 新版 44.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058fcd8",
      "READ",
      [
        "storage",
        "00ca6100",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcec",
      "READ",
      [
        "storage",
        "00ca60f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0058fccc",
      "READ",
      [
        "storage",
        "00ca60e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fcd8",
      "READ",
      [
        "storage",
        "00ca6500",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcec",
      "READ",
      [
        "storage",
        "00ca64f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fd0c",
      "READ",
      [
        "storage",
        "00ca64e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md#insn-0058fcdc) · [`0058fd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md#insn-0058fd00)
- 新版 [`0058fd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md#insn-0058fd00)

~~~diff
- 0058fcdc ["INT_RIGHT", "register:4070:8", ["register:4070:8", "const:7:8"]]
- 0058fcdc bytes cefd47d3
- 0058fd00 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0058fd00 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0058fd00 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0058fd00 ["COPY", "tmp:1:8", ["register:4080:8"]]
- 0058fd00 bytes eb03909a
+ 0058fd00 ["COPY", "tmp:0:8", ["register:4060:8"]]
+ 0058fd00 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0058fd00 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0058fd00 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0058fd00 bytes 6d010c8b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653b7b9189cccfd75609a34ebc4a880e"></a>

### [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) → [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) FUN_0058fd9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 1件 [`00590378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590378.md)
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fe34",
      "incomplete_value": true,
      "site": "0058fe3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058fdf4",
      "incomplete_value": true,
      "site": "0058fdfc",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fe38",
      "incomplete_value": true,
      "site": "0058fe40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:4c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fdf8",
      "incomplete_value": true,
      "site": "0058fe00",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:c0:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fe50",
      "incomplete_value": false,
      "site": "0058fe50",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fe10",
      "incomplete_value": false,
      "site": "0058fe10",
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
            "const:100:8"
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
      "0058fdb4",
      "READ",
      [
        "storage",
        "00ca60e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fdd4",
      "READ",
      [
        "storage",
        "00ca60f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fdd4",
      "READ",
      [
        "storage",
        "00ca6100",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fdb4",
      "READ",
      [
        "storage",
        "00ca64e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fdd4",
      "READ",
      [
        "storage",
        "00ca64f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fdd4",
      "READ",
      [
        "storage",
        "00ca6500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md#insn-0058fdb4) · [`0058fe10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md#insn-0058fe10) · [`0058fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md#insn-0058fd6c)
- 新版 [`0058fdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fdf4) · [`0058fe50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fe50) · [`0058fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fdac)

~~~diff
- 0058fdb4 ["INT_ADD", "register:40f0:8", ["const:58fdb4:8", "const:4:8"]]
- 0058fdb4 ["CALL", null, ["callee:005903b8:8"]]
+ 0058fdf4 ["INT_ADD", "register:40f0:8", ["const:58fdf4:8", "const:4:8"]]
+ 0058fdf4 ["CALL", null, ["callee:005903b8:8"]]
- 0058fdb4 bytes 71010094
+ 0058fdf4 bytes 71010094
- 0058fe10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 0058fe10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0058fe50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 0058fe50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0058fe10 bytes 098100f9
+ 0058fe50 bytes 098102f9
- 0058fd6c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0058fd6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058fd6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058fd6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058fdac ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0058fdac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058fdac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058fdac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058fd6c bytes 29810391
+ 0058fdac bytes 29811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda2aaeab37fc32abe26270a3f08270b"></a>

### [`0058fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md) → [`0058fe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md) FUN_0058fe60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) · 呼出先 1件 [`00c57f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f90.md)
- 新版 呼出元 1件 [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 1件 [`00c58390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58390.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fec8",
      "incomplete_value": false,
      "site": "0058fec8",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fe88",
      "incomplete_value": false,
      "site": "0058fe88",
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
            "const:108:8"
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
      "0058fe80",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe94",
      "READ",
      [
        "storage",
        "00ca60c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe94",
      "READ",
      [
        "storage",
        "00ca60cc",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fe80",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe94",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe94",
      "READ",
      [
        "storage",
        "00ca64cc",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fe48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md#insn-0058fe48) · [`0058fe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md#insn-0058fe88) · [`0058fe38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md#insn-0058fe38)
- 新版 [`0058fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fe88) · [`0058fec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fec8) · [`0058fe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fe78)

~~~diff
- 0058fe48 ["INT_ADD", "register:40f0:8", ["const:58fe48:8", "const:4:8"]]
- 0058fe48 ["CALL", null, ["callee:00c58390:8"]]
+ 0058fe88 ["INT_ADD", "register:40f0:8", ["const:58fe88:8", "const:4:8"]]
+ 0058fe88 ["CALL", null, ["callee:00c58390:8"]]
- 0058fe48 bytes 52201b94
+ 0058fe88 bytes 42211b94
- 0058fe88 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0058fe88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:108:8"]]
- 0058fe88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058fec8 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0058fec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
+ 0058fec8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058fe88 bytes 09210439
+ 0058fec8 bytes 09211439
- 0058fe38 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0058fe38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058fe38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058fe38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058fe78 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0058fe78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058fe78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058fe78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058fe38 bytes 73020391
+ 0058fe78 bytes 73021391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-654e82ccb7f3128098dc910e9193766c"></a>

### [`0058fea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fea0.md) → [`0058fee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md) FUN_0058fee0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a668.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fef0",
      "incomplete_value": false,
      "site": "0058fef0",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058feb0",
      "incomplete_value": false,
      "site": "0058feb0",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fef8",
      "incomplete_value": true,
      "site": "0058fef8",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058feb8",
      "incomplete_value": true,
      "site": "0058feb8",
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
            "const:c0:8"
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
      "0058feec",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fef0",
      "WRITE",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fef8",
      "WRITE",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058feec",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fef0",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fef8",
      "WRITE",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fea0.md#insn-0058feb0) · [`0058feb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fea0.md#insn-0058feb8) · [`0058feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fea0.md#insn-0058feac)
- 新版 [`0058fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058fef0) · [`0058fef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058fef8) · [`0058feec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058feec)

~~~diff
- 0058feb0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058feb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:108:8"]]
- 0058feb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058fef0 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058fef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
+ 0058fef0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058feb0 bytes 2a210439
+ 0058fef0 bytes 2a211439
- 0058feb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 0058feb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 0058fef8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 0058fef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058feb8 bytes 0031803d
+ 0058fef8 bytes 0031813d
- 0058feac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 0058feac ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0058feac ["COPY", "register:5030:8", ["const:0:8"]]
- 0058feac ["COPY", "register:5038:8", ["const:0:8"]]
+ 0058feec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 0058feec ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0058feec ["COPY", "register:5030:8", ["const:0:8"]]
+ 0058feec ["COPY", "register:5038:8", ["const:0:8"]]
- 0058feac bytes 0131c03d
+ 0058feec bytes 0131c13d
~~~


<a id="compare-5e47d866374ba904b0b54ff882982c67"></a>

### [`0058fec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fec0.md) → [`0058ff00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md) FUN_0058ff00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055a66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a66c.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0055a6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6ac.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff14",
      "incomplete_value": true,
      "site": "0058ff14",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fed4",
      "incomplete_value": true,
      "site": "0058fed4",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff20",
      "incomplete_value": true,
      "site": "0058ff20",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fee0",
      "incomplete_value": true,
      "site": "0058fee0",
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
            "const:c0:8"
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
      "0058ff10",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff14",
      "WRITE",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff20",
      "WRITE",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ff10",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff14",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff20",
      "WRITE",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fec0.md#insn-0058fed4) · [`0058fee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fec0.md#insn-0058fee0) · [`0058fed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fec0.md#insn-0058fed0)
- 新版 [`0058ff14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff14) · [`0058ff20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff20) · [`0058ff10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff10)

~~~diff
- 0058fed4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058fed4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:108:8"]]
- 0058fed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff14 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058ff14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
+ 0058ff14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058fed4 bytes 2a210439
+ 0058ff14 bytes 2a211439
- 0058fee0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 0058fee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 0058ff20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 0058ff20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058fee0 bytes 0031803d
+ 0058ff20 bytes 0031813d
- 0058fed0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 0058fed0 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0058fed0 ["COPY", "register:5030:8", ["const:0:8"]]
- 0058fed0 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0058ff10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
+ 0058ff10 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0058ff10 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0058ff10 ["COPY", "register:5038:8", ["const:0:8"]]
- 0058fed0 bytes 0131c03d
+ 0058ff10 bytes 0131c13d
~~~


<a id="compare-cc5fad589aa5043026633f1a3de1082c"></a>

### [`0058fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md) → [`0058ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md) FUN_0058ff28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055a670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a670.md) [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b0.md) [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff3c",
      "incomplete_value": false,
      "site": "0058ff3c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fefc",
      "incomplete_value": false,
      "site": "0058fefc",
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
            "const:108:8"
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
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca60c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff3c",
      "WRITE",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff3c",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md#insn-0058fefc) · [`0058fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md#insn-0058fee8) · [`0058feec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md#insn-0058feec)
- 新版 [`0058ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md#insn-0058ff3c) · [`0058ff2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md#insn-0058ff2c)

~~~diff
- 0058fefc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058fefc ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:108:8"]]
- 0058fefc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff3c ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058ff3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
+ 0058ff3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058fefc bytes 2a210439
+ 0058ff3c bytes 2a211439
- 0058fee8 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0058fee8 bytes a83800f0
- 0058feec ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0058feec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058feec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058feec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ff2c ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0058ff2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ff2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ff2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058feec bytes 08010391
+ 0058ff2c bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53c620637115c2ab56f0f5f1133b4653"></a>

### [`0058ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md) → [`0058ffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md) FUN_0058ffa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) · 呼出先 0件 
- 新版 呼出元 5件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.91% / 新版 65.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 5件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fff0",
      "incomplete_value": false,
      "site": "0058fff0",
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
                "const:518:8"
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
      "definition_site": "0058ffb0",
      "incomplete_value": false,
      "site": "0058ffb0",
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
                "const:118:8"
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fff8",
      "incomplete_value": false,
      "site": "0058fff8",
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
                "const:518:8"
              ]
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
      "definition_site": "0058ffb8",
      "incomplete_value": false,
      "site": "0058ffb8",
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
                "const:118:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fff8",
      "incomplete_value": false,
      "site": "0058fff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058ffb8",
      "incomplete_value": false,
      "site": "0058ffb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "0058ffc8",
      "READ",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ffe4",
      "PARAM",
      [
        "storage",
        "00ca6118",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ffe8",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ffc8",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ffe4",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ffe8",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ffe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md#insn-0058ffe8) · [`0058ff88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md#insn-0058ff88) · [`0058ff9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md#insn-0058ff9c)
- 新版 [`00590028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-00590028) · [`0058ffc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-0058ffc8) · [`0058ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-0058ffdc)

~~~diff
- 0058ffe8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0058ffe8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0058ffe8 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:108:8"]]
- 0058ffe8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590028 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590028 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590028 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:508:8"]]
+ 00590028 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0058ffe8 bytes df220439
+ 00590028 bytes df221439
- 0058ff88 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:108:8"]]
- 0058ff88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0058ff88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0058ffc8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:508:8"]]
+ 0058ffc8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0058ffc8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0058ff88 bytes c8224439
+ 0058ffc8 bytes c8225439
- 0058ff9c ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0058ff9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ffdc ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0058ffdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ffdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ffdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ff9c bytes 08010391
+ 0058ffdc bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360fc66090a1dd1570fc7847bc78f712"></a>

### [`00590018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590018.md) → [`00590058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md) FUN_00590058

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`00551448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551448.md) [`005514dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005514dc.md) [`00551570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551570.md) [`005517bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/005517bc.md) [`0055192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/0055192c.md) · 呼出先 0件 
- 新版 呼出元 13件 [`00551488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551488.md) [`0055151c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/0055151c.md) [`005515b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/005515b0.md) [`005517fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/005517fc.md) [`0055196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/0055196c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005900d0",
      "incomplete_value": true,
      "site": "005900d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590090",
      "incomplete_value": true,
      "site": "00590090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00590074",
      "READ",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0059008c",
      "PARAM",
      [
        "storage",
        "00ca6118",
        null,
        "undefined8"
      ]
    ],
    [
      "00590090",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590074",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0059008c",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590090",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590018.md#insn-00590090) · [`00590034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590018.md#insn-00590034) · [`00590038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590018.md#insn-00590038)
- 新版 [`005900d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md#insn-005900d0) · [`00590074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md#insn-00590074)

~~~diff
- 00590090 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590090 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590090 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:108:8"]]
- 00590090 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 005900d0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 005900d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 005900d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:508:8"]]
+ 005900d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590090 bytes bf220439
+ 005900d0 bytes bf221439
- 00590034 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:108:8"]]
- 00590034 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00590034 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00590074 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
+ 00590074 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00590074 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00590034 bytes a8224439
+ 00590074 bytes a8225439
- 00590038 ["COPY", "register:40b0:8", ["const:ca6000:8"]]
- 00590038 bytes b63800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09639e70885974afea661e33e752f773"></a>

### [`005900b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005900b8.md) → [`005900f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md) FUN_005900f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 62.90% / 新版 62.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590184",
      "incomplete_value": true,
      "site": "00590184",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590144",
      "incomplete_value": true,
      "site": "00590144",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0059019c",
      "incomplete_value": true,
      "site": "0059019c",
      "value": [
        "LOAD",
        "8",
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059015c",
      "incomplete_value": true,
      "site": "0059015c",
      "value": [
        "LOAD",
        "8",
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
                "const:48:8"
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
      "definition_site": "00590188",
      "incomplete_value": true,
      "site": "0059019c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
    "old": {
      "definition_site": "00590148",
      "incomplete_value": true,
      "site": "0059015c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:110:8"
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
      "0059011c",
      "READ",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "00590140",
      "PARAM",
      [
        "storage",
        "00ca6118",
        null,
        "undefined8"
      ]
    ],
    [
      "00590144",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059011c",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "00590140",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590144",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059011c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005900b8.md#insn-0059011c) · [`00590140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005900b8.md#insn-00590140) · [`00590144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005900b8.md#insn-00590144)
- 新版 [`0059015c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-0059015c) · [`00590180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-00590180) · [`00590184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-00590184)

~~~diff
- 0059011c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 0059011c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0059011c ["COPY", "register:5008:8", ["const:0:8"]]
- 0059011c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0059015c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
+ 0059015c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0059015c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0059015c ["COPY", "register:5010:8", ["const:0:8"]]
- 0059011c bytes 20ad46fd
+ 0059015c bytes 20cd46fd
- 00590140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00590140 ["INT_ADD", "register:40f0:8", ["const:590140:8", "const:4:8"]]
- 00590140 ["CALLIND", null, ["register:0:8"]]
+ 00590180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00590180 ["INT_ADD", "register:40f0:8", ["const:590180:8", "const:4:8"]]
+ 00590180 ["CALLIND", null, ["register:0:8"]]
- 00590140 bytes 00013fd6
+ 00590180 bytes 00013fd6
- 00590144 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590144 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590144 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:108:8"]]
- 00590144 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590184 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590184 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590184 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:508:8"]]
+ 00590184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590144 bytes 3f230439
+ 00590184 bytes 3f231439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98ebc03bd37c0cf79c1734c1c49ce73"></a>

### [`005901b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005901b0.md) → [`005901f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md) FUN_005901f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590248",
      "incomplete_value": false,
      "site": "00590248",
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
                "const:518:8"
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
      "definition_site": "00590208",
      "incomplete_value": false,
      "site": "00590208",
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
                "const:118:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590250",
      "incomplete_value": false,
      "site": "00590250",
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
                "const:518:8"
              ]
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
      "definition_site": "00590210",
      "incomplete_value": false,
      "site": "00590210",
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
                "const:118:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00590250",
      "incomplete_value": false,
      "site": "00590250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "00590210",
      "incomplete_value": false,
      "site": "00590210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00590214",
      "READ",
      [
        "storage",
        "00ca6108",
        null,
        "undefined1"
      ]
    ],
    [
      "0059023c",
      "PARAM",
      [
        "storage",
        "00ca6118",
        null,
        "undefined8"
      ]
    ],
    [
      "00590240",
      "READ",
      [
        "storage",
        "00ca60c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590214",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0059023c",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590240",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005901d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005901b0.md#insn-005901d4) · [`005901f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005901b0.md#insn-005901f4) · [`005901fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/005901b0.md#insn-005901fc)
- 新版 [`00590214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-00590214) · [`00590234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-00590234) · [`0059023c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-0059023c)

~~~diff
- 005901d4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:108:8"]]
- 005901d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 005901d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00590214 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:508:8"]]
+ 00590214 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00590214 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 005901d4 bytes 28234439
+ 00590214 bytes 28235439
- 005901f4 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 005901f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005901f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005901f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590234 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00590234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005901f4 bytes 08010391
+ 00590234 bytes 08011391
- 005901fc ["COPY", "tmp:0:8", ["const:118:8"]]
- 005901fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005901fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005901fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059023c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0059023c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059023c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059023c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005901fc bytes 21600491
+ 0059023c bytes 21601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4ffe7144a42b756f1a2bebcc73ff40"></a>

### [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) → [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) FUN_00590db8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00592370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) · 呼出先 17件 [`00550bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bc4.md) [`00555234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md) [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`005923b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md) · 呼出先 17件 [`00550c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c04.md) [`00555274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555274.md) [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590de4",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590da4",
      "incomplete_value": false,
      "site": "00590db0",
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
            "const:c10:8"
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
      "definition_site": "00590e24",
      "incomplete_value": true,
      "site": "00590e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:22f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590de4",
      "incomplete_value": true,
      "site": "00590de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:162:8"
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
      "definition_site": "00590e64",
      "incomplete_value": true,
      "site": "00590e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cfa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e24",
      "incomplete_value": true,
      "site": "00590e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cba:8"
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
      "00590df0",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ],
    [
      "00590e14",
      "READ",
      [
        "storage",
        "002a0162",
        null,
        "string"
      ]
    ],
    [
      "00590e54",
      "READ",
      [
        "storage",
        "002b3cba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00590df0",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ],
    [
      "00590e14",
      "READ",
      [
        "storage",
        "002a022f",
        null,
        "string"
      ]
    ],
    [
      "00590e54",
      "READ",
      [
        "storage",
        "002b3cfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md#insn-00590da4) · [`00590ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md#insn-00590ea8) · [`00590ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md#insn-00590ee8)
- 新版 [`00590de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590de4) · [`00590ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590ee8) · [`00590f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590f28)

~~~diff
- 00590da4 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00590da4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590da4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590da4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590de4 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00590de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590da4 bytes 29413091
+ 00590de4 bytes 29410091
- 00590ea8 ["INT_ADD", "register:40f0:8", ["const:590ea8:8", "const:4:8"]]
- 00590ea8 ["CALL", null, ["callee:00c58610:8"]]
+ 00590ee8 ["INT_ADD", "register:40f0:8", ["const:590ee8:8", "const:4:8"]]
+ 00590ee8 ["CALL", null, ["callee:00c58610:8"]]
- 00590ea8 bytes da1c1b94
+ 00590ee8 bytes ca1d1b94
- 00590ee8 ["INT_ADD", "register:40f0:8", ["const:590ee8:8", "const:4:8"]]
- 00590ee8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00590f28 ["INT_ADD", "register:40f0:8", ["const:590f28:8", "const:4:8"]]
+ 00590f28 ["CALL", null, ["callee:00c53d00:8"]]
- 00590ee8 bytes 7e0a1b94
+ 00590f28 bytes 760b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17873e7a93cdc3347f7a4d59501b663"></a>

### [`00591278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591278.md) → [`005912b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md) FUN_005912b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f60.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a360.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591384",
      "incomplete_value": false,
      "site": "00591384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591344",
      "incomplete_value": false,
      "site": "00591344",
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
            "const:e30:8"
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
      "definition_site": "0059139c",
      "incomplete_value": true,
      "site": "005913a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059135c",
      "incomplete_value": true,
      "site": "00591364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591314",
      "incomplete_value": true,
      "site": "00591318",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005912d4",
      "incomplete_value": true,
      "site": "005912d8",
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
              "LOAD"
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
      "00591310",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00591314",
      "READ",
      [
        "storage",
        "00ca3a44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059131c",
      "READ",
      [
        "storage",
        "00ca3a48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00591310",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00591314",
      "READ",
      [
        "storage",
        "00ca3e44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059131c",
      "READ",
      [
        "storage",
        "00ca3e48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005912d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591278.md#insn-005912d8) · [`00591324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591278.md#insn-00591324) · [`005912b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591278.md#insn-005912b4)
- 新版 [`00591318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-00591318) · [`00591364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-00591364) · [`005912f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-005912f4)

~~~diff
- 005912d8 ["INT_ADD", "register:40f0:8", ["const:5912d8:8", "const:4:8"]]
- 005912d8 ["CALL", null, ["callee:00c5a380:8"]]
+ 00591318 ["INT_ADD", "register:40f0:8", ["const:591318:8", "const:4:8"]]
+ 00591318 ["CALL", null, ["callee:00c5a380:8"]]
- 005912d8 bytes 2a231b94
+ 00591318 bytes 1a241b94
- 00591324 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 00591324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591364 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00591364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591324 bytes 08813791
+ 00591364 bytes 08810791
- 005912b4 ["INT_ADD", "register:40f0:8", ["const:5912b4:8", "const:4:8"]]
- 005912b4 ["CALL", null, ["callee:00c5a360:8"]]
+ 005912f4 ["INT_ADD", "register:40f0:8", ["const:5912f4:8", "const:4:8"]]
+ 005912f4 ["CALL", null, ["callee:00c5a360:8"]]
- 005912b4 bytes 2b231b94
+ 005912f4 bytes 1b241b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65535bc6cd871f45aa1a26aab03c076d"></a>

### [`005913c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005913c0.md) → [`00591400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md) FUN_00591400

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f60.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a360.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005914dc",
      "incomplete_value": false,
      "site": "005914e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059149c",
      "incomplete_value": false,
      "site": "005914a4",
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
            "const:de0:8"
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
      "definition_site": "005914fc",
      "incomplete_value": false,
      "site": "005914fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005914bc",
      "incomplete_value": false,
      "site": "005914bc",
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
            "const:e30:8"
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
      "definition_site": "00591514",
      "incomplete_value": true,
      "site": "00591518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005914d4",
      "incomplete_value": true,
      "site": "005914d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
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
      "00591460",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00591464",
      "READ",
      [
        "storage",
        "00ca3a44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059146c",
      "READ",
      [
        "storage",
        "00ca3a48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00591460",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00591464",
      "READ",
      [
        "storage",
        "00ca3e44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059146c",
      "READ",
      [
        "storage",
        "00ca3e48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005913c0.md#insn-00591428) · [`00591498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005913c0.md#insn-00591498) · [`00591518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005913c0.md#insn-00591518)
- 新版 [`00591468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-00591468) · [`005914d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-005914d8) · [`00591558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-00591558)

~~~diff
- 00591428 ["INT_ADD", "register:40f0:8", ["const:591428:8", "const:4:8"]]
- 00591428 ["CALL", null, ["callee:00c5a380:8"]]
+ 00591468 ["INT_ADD", "register:40f0:8", ["const:591468:8", "const:4:8"]]
+ 00591468 ["CALL", null, ["callee:00c5a380:8"]]
- 00591428 bytes d6221b94
+ 00591468 bytes c6231b94
- 00591498 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005914d8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00591498 bytes c83600f0
+ 005914d8 bytes e8360090
- 00591518 ["INT_ADD", "register:40f0:8", ["const:591518:8", "const:4:8"]]
- 00591518 ["CALL", null, ["callee:00c5a3e0:8"]]
+ 00591558 ["INT_ADD", "register:40f0:8", ["const:591558:8", "const:4:8"]]
+ 00591558 ["CALL", null, ["callee:00c5a3e0:8"]]
- 00591518 bytes b2221b94
+ 00591558 bytes a2231b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ced13a4ec6c51147fc95ca93a19fe1"></a>

### [`005915bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005915bc.md) → [`005915fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md) FUN_005915fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a400.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591640",
      "incomplete_value": false,
      "site": "00591648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591600",
      "incomplete_value": false,
      "site": "00591608",
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
            "const:f50:8"
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
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591620",
      "incomplete_value": false,
      "site": "00591620",
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
            "const:fa0:8"
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
      "00591648",
      "DATA",
      [
        "storage",
        "00c6cf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00591660",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591648",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ],
    [
      "00591660",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005915f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005915bc.md#insn-005915f0) · [`005915f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005915bc.md#insn-005915f8) · [`005915fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/005915bc.md#insn-005915fc)
- 新版 [`00591630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-00591630) · [`00591638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-00591638) · [`0059163c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-0059163c)

~~~diff
- 005915f0 ["INT_ADD", "register:40f0:8", ["const:5915f0:8", "const:4:8"]]
- 005915f0 ["CALL", null, ["callee:00c5a400:8"]]
+ 00591630 ["INT_ADD", "register:40f0:8", ["const:591630:8", "const:4:8"]]
+ 00591630 ["CALL", null, ["callee:00c5a400:8"]]
- 005915f0 bytes 84221b94
+ 00591630 bytes 74231b94
- 005915f8 ["INT_ADD", "register:40f0:8", ["const:5915f8:8", "const:4:8"]]
- 005915f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00591638 ["INT_ADD", "register:40f0:8", ["const:591638:8", "const:4:8"]]
+ 00591638 ["CALL", null, ["callee:00c57e90:8"]]
- 005915f8 bytes 26191b94
+ 00591638 bytes 161a1b94
- 005915fc ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0059163c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005915fc bytes c83600f0
+ 0059163c bytes e8360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c1df209d5cc6fa9af8bc50d732ce46"></a>

### [`00591748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md) → [`00591788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md) FUN_00591788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)

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
      "definition_site": "005917a0",
      "incomplete_value": false,
      "site": "005917ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:ea7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591760",
      "incomplete_value": false,
      "site": "0059176c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e67:8"
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
      "005917a0",
      "PARAM",
      [
        "storage",
        "002bee67",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005917a0",
      "PARAM",
      [
        "storage",
        "002beea7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md#insn-0059176c) · [`00591760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591748.md#insn-00591760)
- 新版 [`005917ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md#insn-005917ac) · [`005917a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md#insn-005917a0)

~~~diff
- 0059176c ["INT_ADD", "register:40f0:8", ["const:59176c:8", "const:4:8"]]
- 0059176c ["CALL", null, ["callee:00592578:8"]]
+ 005917ac ["INT_ADD", "register:40f0:8", ["const:5917ac:8", "const:4:8"]]
+ 005917ac ["CALL", null, ["callee:00592578:8"]]
- 0059176c bytes 73030094
+ 005917ac bytes 73030094
- 00591760 ["COPY", "tmp:0:8", ["const:e67:8"]]
- 00591760 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591760 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591760 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005917a0 ["COPY", "tmp:0:8", ["const:ea7:8"]]
+ 005917a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005917a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005917a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591760 bytes 219c3991
+ 005917a0 bytes 219c3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83f3e4c651c7a94d98ff8f054952576"></a>

### [`00591800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md) → [`00591840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md) FUN_00591840

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)

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
      "definition_site": "00591858",
      "incomplete_value": false,
      "site": "00591864",
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
            "const:2d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591818",
      "incomplete_value": false,
      "site": "00591824",
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
            "const:20a:8"
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
      "00591858",
      "PARAM",
      [
        "storage",
        "002a320a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591858",
      "PARAM",
      [
        "storage",
        "002a32d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md#insn-00591824) · [`00591818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591800.md#insn-00591818)
- 新版 [`00591864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md#insn-00591864) · [`00591858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md#insn-00591858)

~~~diff
- 00591824 ["INT_ADD", "register:40f0:8", ["const:591824:8", "const:4:8"]]
- 00591824 ["CALL", null, ["callee:00592578:8"]]
+ 00591864 ["INT_ADD", "register:40f0:8", ["const:591864:8", "const:4:8"]]
+ 00591864 ["CALL", null, ["callee:00592578:8"]]
- 00591824 bytes 45030094
+ 00591864 bytes 45030094
- 00591818 ["COPY", "tmp:0:8", ["const:20a:8"]]
- 00591818 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591818 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591818 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591858 ["COPY", "tmp:0:8", ["const:2d7:8"]]
+ 00591858 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591858 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591858 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591818 bytes 21280891
+ 00591858 bytes 215c0b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b65c83b117a165df870abaaf56220d"></a>

### [`00591848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md) → [`00591888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md) FUN_00591888

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592538.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005918a0",
      "incomplete_value": false,
      "site": "005918b0",
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
            "const:934:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591860",
      "incomplete_value": false,
      "site": "00591870",
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
            "const:8f4:8"
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
      "005918a0",
      "PARAM",
      [
        "storage",
        "002ad8f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005918a0",
      "PARAM",
      [
        "storage",
        "002ad934",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md#insn-00591870) · [`00591860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591848.md#insn-00591860)
- 新版 [`005918b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md#insn-005918b0) · [`005918a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md#insn-005918a0)

~~~diff
- 00591870 ["INT_ADD", "register:40f0:8", ["const:591870:8", "const:4:8"]]
- 00591870 ["CALL", null, ["callee:00592578:8"]]
+ 005918b0 ["INT_ADD", "register:40f0:8", ["const:5918b0:8", "const:4:8"]]
+ 005918b0 ["CALL", null, ["callee:00592578:8"]]
- 00591870 bytes 32030094
+ 005918b0 bytes 32030094
- 00591860 ["COPY", "tmp:0:8", ["const:8f4:8"]]
- 00591860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005918a0 ["COPY", "tmp:0:8", ["const:934:8"]]
+ 005918a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005918a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005918a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591860 bytes 21d02391
+ 005918a0 bytes 21d02491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c224dfaea2051c98963d8cba2124345"></a>

### [`00591978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591978.md) → [`005919b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md) FUN_005919b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md)

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
      "definition_site": "005919e0",
      "incomplete_value": false,
      "site": "005919f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005919a0",
      "incomplete_value": false,
      "site": "005919b0",
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
            "const:dc0:8"
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
      "definition_site": "005919e4",
      "incomplete_value": true,
      "site": "005919f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005919a4",
      "incomplete_value": true,
      "site": "005919b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
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
      "005919e0",
      "PARAM",
      [
        "storage",
        "00c6cdc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005919e4",
      "READ",
      [
        "storage",
        "00c9aee0",
        null,
        "pointer"
      ]
    ],
    [
      "005919e4",
      "PARAM",
      [
        "storage",
        "00c6d0e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005919e0",
      "PARAM",
      [
        "storage",
        "00c6d1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005919e4",
      "READ",
      [
        "storage",
        "00c9b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "005919e4",
      "PARAM",
      [
        "storage",
        "00c6d4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005919b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591978.md#insn-005919b0) · [`005919f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591978.md#insn-005919f0) · [`00591994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591978.md#insn-00591994)
- 新版 [`005919f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-005919f0) · [`00591a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-00591a30) · [`005919d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-005919d4)

~~~diff
- 005919b0 ["INT_ADD", "register:40f0:8", ["const:5919b0:8", "const:4:8"]]
- 005919b0 ["CALL", null, ["callee:00c58610:8"]]
+ 005919f0 ["INT_ADD", "register:40f0:8", ["const:5919f0:8", "const:4:8"]]
+ 005919f0 ["CALL", null, ["callee:00c58610:8"]]
- 005919b0 bytes 181a1b94
+ 005919f0 bytes 081b1b94
- 005919f0 ["INT_ADD", "register:40f0:8", ["const:5919f0:8", "const:4:8"]]
- 005919f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00591a30 ["INT_ADD", "register:40f0:8", ["const:591a30:8", "const:4:8"]]
+ 00591a30 ["CALL", null, ["callee:00c53d00:8"]]
- 005919f0 bytes bc071b94
+ 00591a30 bytes b4081b94
- 00591994 ["COPY", "register:4010:8", ["const:c9a000:8"]]
+ 005919d4 ["COPY", "register:4010:8", ["const:c9b000:8"]]
- 00591994 bytes 423800b0
+ 005919d4 bytes 423800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace98d054c4eb8b3996590ab012acd92"></a>

### [`00591c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md) → [`00591c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md) FUN_00591c7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fa0.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3a0.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591cbc",
      "incomplete_value": true,
      "site": "00591cc8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591c7c",
      "incomplete_value": true,
      "site": "00591c88",
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
            "const:d30:8"
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
      "definition_site": "00591ce0",
      "incomplete_value": false,
      "site": "00591cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ca0",
      "incomplete_value": false,
      "site": "00591cb0",
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
            "const:d48:8"
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
      "definition_site": "00591ce8",
      "incomplete_value": false,
      "site": "00591cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ca8",
      "incomplete_value": false,
      "site": "00591cb0",
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
            "const:d58:8"
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
      "00591cb4",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591cbc",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ce0",
      "PARAM",
      [
        "storage",
        "00c6cd48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591cb4",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591cbc",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591ce0",
      "PARAM",
      [
        "storage",
        "00c6d148",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md#insn-00591c70) · [`00591c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md#insn-00591c88) · [`00591cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591c3c.md#insn-00591cb0)
- 新版 [`00591cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cb0) · [`00591cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cc8) · [`00591cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cf0)

~~~diff
- 00591c70 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 00591cb0 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 00591c70 bytes c13600f0
+ 00591cb0 bytes e1360090
- 00591c88 ["INT_ADD", "register:40f0:8", ["const:591c88:8", "const:4:8"]]
- 00591c88 ["CALL", null, ["callee:00c58610:8"]]
+ 00591cc8 ["INT_ADD", "register:40f0:8", ["const:591cc8:8", "const:4:8"]]
+ 00591cc8 ["CALL", null, ["callee:00c58610:8"]]
- 00591c88 bytes 62191b94
+ 00591cc8 bytes 521a1b94
- 00591cb0 ["INT_ADD", "register:40f0:8", ["const:591cb0:8", "const:4:8"]]
- 00591cb0 ["CALL", null, ["callee:00c58610:8"]]
+ 00591cf0 ["INT_ADD", "register:40f0:8", ["const:591cf0:8", "const:4:8"]]
+ 00591cf0 ["CALL", null, ["callee:00c58610:8"]]
- 00591cb0 bytes 58191b94
+ 00591cf0 bytes 481a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6541318a011dacfa271fbb5956ed8e0"></a>

### [`00591d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md) → [`00591dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md) FUN_00591dc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb84.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c59f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f70.md) [`00c59fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59fa0.md) [`00c5a0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a0d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3a0.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591e34",
      "incomplete_value": false,
      "site": "00591e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591df4",
      "incomplete_value": false,
      "site": "00591dfc",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591e50",
      "incomplete_value": false,
      "site": "00591e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e10",
      "incomplete_value": false,
      "site": "00591e20",
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
            "const:d48:8"
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
      "definition_site": "00591e58",
      "incomplete_value": false,
      "site": "00591e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e18",
      "incomplete_value": false,
      "site": "00591e20",
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
            "const:d58:8"
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
      "00591e04",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e0c",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e2c",
      "PARAM",
      [
        "storage",
        "00c6cd48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591e04",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e0c",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e2c",
      "PARAM",
      [
        "storage",
        "00c6d148",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md#insn-00591dfc) · [`00591e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md#insn-00591e20) · [`00591dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/00591d84.md#insn-00591dc0)
- 新版 [`00591e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e3c) · [`00591e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e60) · [`00591e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e00)

~~~diff
- 00591dfc ["INT_ADD", "register:40f0:8", ["const:591dfc:8", "const:4:8"]]
- 00591dfc ["CALL", null, ["callee:00c58610:8"]]
+ 00591e3c ["INT_ADD", "register:40f0:8", ["const:591e3c:8", "const:4:8"]]
+ 00591e3c ["CALL", null, ["callee:00c58610:8"]]
- 00591dfc bytes 05191b94
+ 00591e3c bytes f5191b94
- 00591e20 ["INT_ADD", "register:40f0:8", ["const:591e20:8", "const:4:8"]]
- 00591e20 ["CALL", null, ["callee:00c58610:8"]]
+ 00591e60 ["INT_ADD", "register:40f0:8", ["const:591e60:8", "const:4:8"]]
+ 00591e60 ["CALL", null, ["callee:00c58610:8"]]
- 00591e20 bytes fc181b94
+ 00591e60 bytes ec191b94
- 00591dc0 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 00591e00 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 00591dc0 bytes c13600f0
+ 00591e00 bytes e1360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de68514f52aedb5b68766542843eabe"></a>

### [`00592080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md) → [`005920c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md) FUN_005920c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00592108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592108.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005920e8",
      "incomplete_value": false,
      "site": "00592104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920a8",
      "incomplete_value": false,
      "site": "005920c4",
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
            "const:d70:8"
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
      "definition_site": "005920f0",
      "incomplete_value": false,
      "site": "00592104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920b0",
      "incomplete_value": false,
      "site": "005920c4",
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
            "const:d80:8"
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
      "005920e8",
      "PARAM",
      [
        "storage",
        "00c6cd70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005920f0",
      "PARAM",
      [
        "storage",
        "00c6cd80",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005920e8",
      "PARAM",
      [
        "storage",
        "00c6d170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005920f0",
      "PARAM",
      [
        "storage",
        "00c6d180",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005920c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md#insn-005920c4) · [`005920a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md#insn-005920a4) · [`005920a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592080.md#insn-005920a8)
- 新版 [`00592104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-00592104) · [`005920e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-005920e4) · [`005920e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-005920e8)

~~~diff
- 005920c4 ["INT_ADD", "register:40f0:8", ["const:5920c4:8", "const:4:8"]]
- 005920c4 ["CALL", null, ["callee:00c58610:8"]]
+ 00592104 ["INT_ADD", "register:40f0:8", ["const:592104:8", "const:4:8"]]
+ 00592104 ["CALL", null, ["callee:00c58610:8"]]
- 005920c4 bytes 53181b94
+ 00592104 bytes 43191b94
- 005920a4 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 005920e4 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 005920a4 bytes c13600d0
+ 005920e4 bytes c13600f0
- 005920a8 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005920a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005920a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005920a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005920e8 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 005920e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005920e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005920e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005920a8 bytes 21c03591
+ 005920e8 bytes 21c00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70549b37f574f85c9a477a18c5983d04"></a>

### [`00592370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) → [`005923b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md) FUN_005923b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0043b0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) · 呼出先 2件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0043b0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b0e8.md) · 呼出先 2件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "005923d4",
      "incomplete_value": false,
      "site": "005923e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592394",
      "incomplete_value": false,
      "site": "005923a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "005923e0",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005923e0",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md#insn-00592388) · [`00592394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md#insn-00592394) · [`005923a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md#insn-005923a8)
- 新版 [`005923c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923c8) · [`005923d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923d4) · [`005923e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923e8)

~~~diff
- 00592388 ["INT_ADD", "register:40f0:8", ["const:592388:8", "const:4:8"]]
- 00592388 ["CALL", null, ["callee:00c57e90:8"]]
+ 005923c8 ["INT_ADD", "register:40f0:8", ["const:5923c8:8", "const:4:8"]]
+ 005923c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00592388 bytes c2151b94
+ 005923c8 bytes b2161b94
- 00592394 ["COPY", "tmp:0:8", ["const:60:8"]]
- 00592394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005923d4 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 005923d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005923d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005923d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592394 bytes 08810191
+ 005923d4 bytes 08811191
- 005923a8 ["INT_ADD", "register:40f0:8", ["const:5923a8:8", "const:4:8"]]
- 005923a8 ["CALL", null, ["callee:00590db8:8"]]
+ 005923e8 ["INT_ADD", "register:40f0:8", ["const:5923e8:8", "const:4:8"]]
+ 005923e8 ["CALL", null, ["callee:00590db8:8"]]
- 005923a8 bytes 74faff97
+ 005923e8 bytes 74faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9163435806732087b4f83aff3ee59eea"></a>

### [`005923dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005923dc.md) → [`0059241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md) FUN_0059241c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00592434",
      "incomplete_value": false,
      "site": "00592438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005923f4",
      "incomplete_value": false,
      "site": "005923f8",
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
            "const:c10:8"
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
      "00592438",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592438",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005923f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005923dc.md#insn-005923f0) · [`005923f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005923dc.md#insn-005923f4) · [`00592408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005923dc.md#insn-00592408)
- 新版 [`00592430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592430) · [`00592434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592434) · [`00592448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592448)

~~~diff
- 005923f0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592430 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005923f0 bytes c83600d0
+ 00592430 bytes c83600f0
- 005923f4 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 005923f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005923f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005923f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592434 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00592434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005923f4 bytes 08413091
+ 00592434 bytes 08410091
- 00592408 ["INT_ADD", "register:40f0:8", ["const:592408:8", "const:4:8"]]
- 00592408 ["CALL", null, ["callee:00c53d00:8"]]
+ 00592448 ["INT_ADD", "register:40f0:8", ["const:592448:8", "const:4:8"]]
+ 00592448 ["CALL", null, ["callee:00c53d00:8"]]
- 00592408 bytes 36051b94
+ 00592448 bytes 2e061b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f42e5f184ef42c529e3f227debbdd4"></a>

### [`00592478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592478.md) → [`005924b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md) FUN_005924b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005924d0",
      "incomplete_value": false,
      "site": "005924d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592490",
      "incomplete_value": false,
      "site": "00592494",
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
            "const:c10:8"
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
      "005924d4",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005924d4",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005924d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592478.md#insn-005924d4) · [`0059248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592478.md#insn-0059248c) · [`00592490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592478.md#insn-00592490)
- 新版 [`00592514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-00592514) · [`005924cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-005924cc) · [`005924d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-005924d0)

~~~diff
- 005924d4 ["INT_ADD", "register:40f0:8", ["const:5924d4:8", "const:4:8"]]
- 005924d4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00592514 ["INT_ADD", "register:40f0:8", ["const:592514:8", "const:4:8"]]
+ 00592514 ["CALL", null, ["callee:00c53d00:8"]]
- 005924d4 bytes 03051b94
+ 00592514 bytes fb051b94
- 0059248c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005924cc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059248c bytes c83600d0
+ 005924cc bytes c83600f0
- 00592490 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00592490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005924d0 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 005924d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005924d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005924d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592490 bytes 08413091
+ 005924d0 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7240e24bd6fbc935db43922ed3012e35"></a>

### [`00592584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592584.md) → [`005925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925c4.md) FUN_005925c4

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
      "definition_site": "005925c8",
      "incomplete_value": false,
      "site": "005925cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592588",
      "incomplete_value": false,
      "site": "0059258c",
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
            "const:de0:8"
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
      "005925cc",
      "DATA",
      [
        "storage",
        "00c6cde0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005925cc",
      "DATA",
      [
        "storage",
        "00c6d1e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592584.md#insn-00592584) · [`00592588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592584.md#insn-00592588)
- 新版 [`005925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925c4.md#insn-005925c4) · [`005925c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925c4.md#insn-005925c8)

~~~diff
- 00592584 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005925c4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592584 bytes c83600d0
+ 005925c4 bytes c83600f0
- 00592588 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 00592588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005925c8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 005925c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005925c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005925c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592588 bytes 08813791
+ 005925c8 bytes 08810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e8b3adcaf0d27d19e4c6355aa2a728"></a>

### [`00592594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592594.md) → [`005925d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md) FUN_005925d4

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
      "definition_site": "005925e4",
      "incomplete_value": false,
      "site": "005925ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005925a4",
      "incomplete_value": false,
      "site": "005925ac",
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
            "const:de0:8"
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
      "005925ec",
      "DATA",
      [
        "storage",
        "00c6cde0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005925ec",
      "DATA",
      [
        "storage",
        "00c6d1e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005925a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592594.md#insn-005925a0) · [`005925a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592594.md#insn-005925a4) · [`005925b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592594.md#insn-005925b0)
- 新版 [`005925e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md#insn-005925e0) · [`005925e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md#insn-005925e4) · [`005925f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md#insn-005925f0)

~~~diff
- 005925a0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005925e0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005925a0 bytes c83600d0
+ 005925e0 bytes c83600f0
- 005925a4 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 005925a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005925a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005925a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005925e4 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 005925e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005925e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005925e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005925a4 bytes 08813791
+ 005925e4 bytes 08810791
- 005925b0 ["INT_ADD", "register:40f0:8", ["const:5925b0:8", "const:4:8"]]
- 005925b0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005925f0 ["INT_ADD", "register:40f0:8", ["const:5925f0:8", "const:4:8"]]
+ 005925f0 ["CALL", null, ["callee:00c57ea0:8"]]
- 005925b0 bytes 3c151b94
+ 005925f0 bytes 2c161b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-288049ecf70e653ae1bde1bb53e05c76"></a>

### [`005925d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005925d4.md) → [`00592614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md) FUN_00592614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a550.md)

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
      "definition_site": "0059262c",
      "incomplete_value": false,
      "site": "00592630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005925ec",
      "incomplete_value": false,
      "site": "005925f0",
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
            "const:e30:8"
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
      "00592630",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592630",
      "DATA",
      [
        "storage",
        "00c6d230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005925e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005925d4.md#insn-005925e8) · [`005925ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005925d4.md#insn-005925ec) · [`005925f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005925d4.md#insn-005925f4)
- 新版 [`00592628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-00592628) · [`0059262c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-0059262c) · [`00592634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-00592634)

~~~diff
- 005925e8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592628 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005925e8 bytes c83600d0
+ 00592628 bytes c83600f0
- 005925ec ["COPY", "tmp:0:8", ["const:e30:8"]]
- 005925ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005925ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005925ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059262c ["COPY", "tmp:0:8", ["const:230:8"]]
+ 0059262c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059262c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059262c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005925ec bytes 08c13891
+ 0059262c bytes 08c10891
- 005925f4 ["INT_ADD", "register:40f0:8", ["const:5925f4:8", "const:4:8"]]
- 005925f4 ["CALL", null, ["callee:00555288:8"]]
+ 00592634 ["INT_ADD", "register:40f0:8", ["const:592634:8", "const:4:8"]]
+ 00592634 ["CALL", null, ["callee:00555288:8"]]
- 005925f4 bytes 150bff97
+ 00592634 bytes 150bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee37f18dab5a116e48fa09aa0f23f930"></a>

### [`0059261c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059261c.md) → [`0059265c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md) FUN_0059265c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a150.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a550.md)

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
      "definition_site": "00592674",
      "incomplete_value": false,
      "site": "00592678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592634",
      "incomplete_value": false,
      "site": "00592638",
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
            "const:e30:8"
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
      "00592678",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592678",
      "DATA",
      [
        "storage",
        "00c6d230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059261c.md#insn-00592630) · [`00592634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059261c.md#insn-00592634) · [`0059263c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059261c.md#insn-0059263c)
- 新版 [`00592670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-00592670) · [`00592674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-00592674) · [`0059267c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-0059267c)

~~~diff
- 00592630 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592670 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592630 bytes c83600d0
+ 00592670 bytes c83600f0
- 00592634 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00592634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592674 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00592674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592634 bytes 08c13891
+ 00592674 bytes 08c10891
- 0059263c ["INT_ADD", "register:40f0:8", ["const:59263c:8", "const:4:8"]]
- 0059263c ["CALL", null, ["callee:00555288:8"]]
+ 0059267c ["INT_ADD", "register:40f0:8", ["const:59267c:8", "const:4:8"]]
+ 0059267c ["CALL", null, ["callee:00555288:8"]]
- 0059263c bytes 030bff97
+ 0059267c bytes 030bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-160009e6b865d01ae8bbda703b345ad8"></a>

### [`0059280c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059280c.md) → [`0059284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059284c.md) FUN_0059284c

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
      "definition_site": "00592850",
      "incomplete_value": false,
      "site": "00592854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592810",
      "incomplete_value": false,
      "site": "00592814",
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
      "00592854",
      "DATA",
      [
        "storage",
        "00c6ce98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592854",
      "DATA",
      [
        "storage",
        "00c6d298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059280c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059280c.md#insn-0059280c) · [`00592810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059280c.md#insn-00592810)
- 新版 [`0059284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059284c.md#insn-0059284c) · [`00592850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059284c.md#insn-00592850)

~~~diff
- 0059280c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0059284c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059280c bytes c83600d0
+ 0059284c bytes c83600f0
- 00592810 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00592810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592850 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00592850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592810 bytes 08613a91
+ 00592850 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c6190a766d85f05059f1073c2f6130"></a>

### [`0059281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059281c.md) → [`0059285c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md) FUN_0059285c

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
      "definition_site": "0059286c",
      "incomplete_value": false,
      "site": "00592874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059282c",
      "incomplete_value": false,
      "site": "00592834",
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
      "00592874",
      "DATA",
      [
        "storage",
        "00c6ce98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592874",
      "DATA",
      [
        "storage",
        "00c6d298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059281c.md#insn-00592828) · [`0059282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059281c.md#insn-0059282c) · [`00592838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059281c.md#insn-00592838)
- 新版 [`00592868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md#insn-00592868) · [`0059286c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md#insn-0059286c) · [`00592878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md#insn-00592878)

~~~diff
- 00592828 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592868 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592828 bytes c83600d0
+ 00592868 bytes c83600f0
- 0059282c ["COPY", "tmp:0:8", ["const:e98:8"]]
- 0059282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059286c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0059286c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059286c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059286c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059282c bytes 08613a91
+ 0059286c bytes 08610a91
- 00592838 ["INT_ADD", "register:40f0:8", ["const:592838:8", "const:4:8"]]
- 00592838 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00592878 ["INT_ADD", "register:40f0:8", ["const:592878:8", "const:4:8"]]
+ 00592878 ["CALL", null, ["callee:00c57ea0:8"]]
- 00592838 bytes 9a141b94
+ 00592878 bytes 8a151b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c052880d80b03b4e8aafd8a248aa0e55"></a>

### [`0059285c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059285c.md) → [`0059289c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md) FUN_0059289c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a560.md)

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
      "definition_site": "005928b4",
      "incomplete_value": false,
      "site": "005928b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592874",
      "incomplete_value": false,
      "site": "00592878",
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
            "const:ee8:8"
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
      "005928b8",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005928b8",
      "DATA",
      [
        "storage",
        "00c6d2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059285c.md#insn-00592870) · [`00592874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059285c.md#insn-00592874) · [`0059287c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/0059285c.md#insn-0059287c)
- 新版 [`005928b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928b0) · [`005928b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928b4) · [`005928bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928bc)

~~~diff
- 00592870 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005928b0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592870 bytes c83600d0
+ 005928b0 bytes c83600f0
- 00592874 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00592874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005928b4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 005928b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005928b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005928b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592874 bytes 08a13b91
+ 005928b4 bytes 08a10b91
- 0059287c ["INT_ADD", "register:40f0:8", ["const:59287c:8", "const:4:8"]]
- 0059287c ["CALL", null, ["callee:00555288:8"]]
+ 005928bc ["INT_ADD", "register:40f0:8", ["const:5928bc:8", "const:4:8"]]
+ 005928bc ["CALL", null, ["callee:00555288:8"]]
- 0059287c bytes 730aff97
+ 005928bc bytes 730aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2391ae873106e449fc02c1beeb6a71cd"></a>

### [`005928a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928a4.md) → [`005928e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md) FUN_005928e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a560.md)

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
      "definition_site": "005928fc",
      "incomplete_value": false,
      "site": "00592900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005928bc",
      "incomplete_value": false,
      "site": "005928c0",
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
            "const:ee8:8"
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
      "00592900",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592900",
      "DATA",
      [
        "storage",
        "00c6d2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005928b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928a4.md#insn-005928b8) · [`005928bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928a4.md#insn-005928bc) · [`005928c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005928a4.md#insn-005928c4)
- 新版 [`005928f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-005928f8) · [`005928fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-005928fc) · [`00592904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-00592904)

~~~diff
- 005928b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005928f8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005928b8 bytes c83600d0
+ 005928f8 bytes c83600f0
- 005928bc ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 005928bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005928bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005928bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005928fc ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 005928fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005928fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005928fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005928bc bytes 08a13b91
+ 005928fc bytes 08a10b91
- 005928c4 ["INT_ADD", "register:40f0:8", ["const:5928c4:8", "const:4:8"]]
- 005928c4 ["CALL", null, ["callee:00555288:8"]]
+ 00592904 ["INT_ADD", "register:40f0:8", ["const:592904:8", "const:4:8"]]
+ 00592904 ["CALL", null, ["callee:00555288:8"]]
- 005928c4 bytes 610aff97
+ 00592904 bytes 610aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a1dfcb770ff19ec06dd8c5a30d76672"></a>

### [`00592938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592938.md) → [`00592978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592978.md) FUN_00592978

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
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "00592980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059293c",
      "incomplete_value": false,
      "site": "00592940",
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
            "const:f50:8"
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
      "00592980",
      "DATA",
      [
        "storage",
        "00c6cf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592980",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592938.md#insn-00592938) · [`0059293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592938.md#insn-0059293c)
- 新版 [`00592978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592978.md#insn-00592978) · [`0059297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592978.md#insn-0059297c)

~~~diff
- 00592938 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592978 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592938 bytes c83600d0
+ 00592978 bytes c83600f0
- 0059293c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0059293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059297c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0059297c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059297c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059297c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059293c bytes 08413d91
+ 0059297c bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cb4f51cbd60a8d1247e1beebe2bcea5"></a>

### [`00592948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592948.md) → [`00592988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md) FUN_00592988

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
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "005929a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592958",
      "incomplete_value": false,
      "site": "00592960",
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
            "const:f50:8"
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
      "005929a0",
      "DATA",
      [
        "storage",
        "00c6cf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929a0",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592948.md#insn-00592954) · [`00592958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592948.md#insn-00592958) · [`00592964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592948.md#insn-00592964)
- 新版 [`00592994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md#insn-00592994) · [`00592998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md#insn-00592998) · [`005929a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md#insn-005929a4)

~~~diff
- 00592954 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592994 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592954 bytes c83600d0
+ 00592994 bytes c83600f0
- 00592958 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00592958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592998 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 00592998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592958 bytes 08413d91
+ 00592998 bytes 08410d91
- 00592964 ["INT_ADD", "register:40f0:8", ["const:592964:8", "const:4:8"]]
- 00592964 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005929a4 ["INT_ADD", "register:40f0:8", ["const:5929a4:8", "const:4:8"]]
+ 005929a4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00592964 bytes 4f141b94
+ 005929a4 bytes 3f151b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07745aaff7c6a202a3c1d94e6a0a787"></a>

### [`00592988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592988.md) → [`005929c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md) FUN_005929c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c5a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a570.md)

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
      "definition_site": "005929e0",
      "incomplete_value": false,
      "site": "005929e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005929a0",
      "incomplete_value": false,
      "site": "005929a4",
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
            "const:fa0:8"
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
      "005929e4",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929e4",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592988.md#insn-0059299c) · [`005929a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592988.md#insn-005929a0) · [`005929a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592988.md#insn-005929a8)
- 新版 [`005929dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929dc) · [`005929e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929e0) · [`005929e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929e8)

~~~diff
- 0059299c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005929dc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0059299c bytes c83600d0
+ 005929dc bytes c83600f0
- 005929a0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 005929a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005929a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005929a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929e0 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005929e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005929a0 bytes 08813e91
+ 005929e0 bytes 08810e91
- 005929a8 ["INT_ADD", "register:40f0:8", ["const:5929a8:8", "const:4:8"]]
- 005929a8 ["CALL", null, ["callee:00555288:8"]]
+ 005929e8 ["INT_ADD", "register:40f0:8", ["const:5929e8:8", "const:4:8"]]
+ 005929e8 ["CALL", null, ["callee:00555288:8"]]
- 005929a8 bytes 280aff97
+ 005929e8 bytes 280aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08022f0d9c43fe17f39eba18aad0c4bc"></a>

### [`005929d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005929d0.md) → [`00592a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md) FUN_00592a10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a570.md)

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
      "definition_site": "00592a28",
      "incomplete_value": false,
      "site": "00592a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005929e8",
      "incomplete_value": false,
      "site": "005929ec",
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
            "const:fa0:8"
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
      "00592a2c",
      "DATA",
      [
        "storage",
        "00c6cfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592a2c",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005929e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005929d0.md#insn-005929e4) · [`005929e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005929d0.md#insn-005929e8) · [`005929f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/005929d0.md#insn-005929f0)
- 新版 [`00592a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a24) · [`00592a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a28) · [`00592a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a30)

~~~diff
- 005929e4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592a24 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005929e4 bytes c83600d0
+ 00592a24 bytes c83600f0
- 005929e8 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 005929e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005929e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005929e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592a28 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00592a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005929e8 bytes 08813e91
+ 00592a28 bytes 08810e91
- 005929f0 ["INT_ADD", "register:40f0:8", ["const:5929f0:8", "const:4:8"]]
- 005929f0 ["CALL", null, ["callee:00555288:8"]]
+ 00592a30 ["INT_ADD", "register:40f0:8", ["const:592a30:8", "const:4:8"]]
+ 00592a30 ["CALL", null, ["callee:00555288:8"]]
- 005929f0 bytes 160aff97
+ 00592a30 bytes 160aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec24efd6f6b41be2face11dfcd93d24"></a>

### [`00592b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md) → [`00592b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md) FUN_00592b6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0059168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059168c.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a1b0.md)
- 新版 呼出元 1件 [`005916cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a5b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592b94",
      "incomplete_value": false,
      "site": "00592bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592b54",
      "incomplete_value": false,
      "site": "00592b6c",
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
            "const:fd8:8"
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
      "definition_site": "00592bb0",
      "incomplete_value": false,
      "site": "00592bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592b70",
      "incomplete_value": false,
      "site": "00592b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "00592bac",
      "DATA",
      [
        "storage",
        "00c6cfd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592bb0",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592bac",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592bb0",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md#insn-00592b44) · [`00592b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md#insn-00592b50) · [`00592b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592b2c.md#insn-00592b54)
- 新版 [`00592b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b84) · [`00592b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b90) · [`00592b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b94)

~~~diff
- 00592b44 ["INT_ADD", "register:40f0:8", ["const:592b44:8", "const:4:8"]]
- 00592b44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00592b84 ["INT_ADD", "register:40f0:8", ["const:592b84:8", "const:4:8"]]
+ 00592b84 ["CALL", null, ["callee:00c57e90:8"]]
- 00592b44 bytes d3131b94
+ 00592b84 bytes c3141b94
- 00592b50 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592b90 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592b50 bytes c83600d0
+ 00592b90 bytes c83600f0
- 00592b54 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00592b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592b94 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 00592b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592b54 bytes 08613f91
+ 00592b94 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9352c64f42eac6944940e02835d6acf1"></a>

### [`00592bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592bd4.md) → [`00592c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c14.md) FUN_00592c14

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
      "definition_site": "00592c18",
      "incomplete_value": false,
      "site": "00592c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592bd8",
      "incomplete_value": false,
      "site": "00592bdc",
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
            "const:fd8:8"
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
      "00592c1c",
      "DATA",
      [
        "storage",
        "00c6cfd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c1c",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592bd4.md#insn-00592bd4) · [`00592bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592bd4.md#insn-00592bd8)
- 新版 [`00592c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c14.md#insn-00592c14) · [`00592c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c14.md#insn-00592c18)

~~~diff
- 00592bd4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592c14 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592bd4 bytes c83600d0
+ 00592c14 bytes c83600f0
- 00592bd8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00592bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c18 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 00592c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592bd8 bytes 08613f91
+ 00592c18 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2057a6ee6cc5875dc5ebc2d2566a63"></a>

### [`00592be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592be4.md) → [`00592c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md) FUN_00592c24

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
      "definition_site": "00592c34",
      "incomplete_value": false,
      "site": "00592c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592bf4",
      "incomplete_value": false,
      "site": "00592bfc",
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
            "const:fd8:8"
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
      "00592c3c",
      "DATA",
      [
        "storage",
        "00c6cfd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c3c",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592be4.md#insn-00592bf0) · [`00592bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592be4.md#insn-00592bf4) · [`00592c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592be4.md#insn-00592c00)
- 新版 [`00592c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md#insn-00592c30) · [`00592c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md#insn-00592c34) · [`00592c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md#insn-00592c40)

~~~diff
- 00592bf0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00592c30 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00592bf0 bytes c83600d0
+ 00592c30 bytes c83600f0
- 00592bf4 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00592bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c34 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 00592c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592bf4 bytes 08613f91
+ 00592c34 bytes 08610f91
- 00592c00 ["INT_ADD", "register:40f0:8", ["const:592c00:8", "const:4:8"]]
- 00592c00 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00592c40 ["INT_ADD", "register:40f0:8", ["const:592c40:8", "const:4:8"]]
+ 00592c40 ["CALL", null, ["callee:00c57ea0:8"]]
- 00592c00 bytes a8131b94
+ 00592c40 bytes 98141b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fda04fb2066bafca0b5e6bcb3637897"></a>

### [`00592c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c74.md) → [`00592cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md) FUN_00592cb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00592ccc",
      "incomplete_value": false,
      "site": "00592cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c8c",
      "incomplete_value": false,
      "site": "00592c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "00592cd0",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592cd0",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c74.md#insn-00592cd0) · [`00592c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c74.md#insn-00592c8c) · [`00592ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592c74.md#insn-00592ca0)
- 新版 [`00592d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592d10) · [`00592ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592ccc) · [`00592ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592ce0)

~~~diff
- 00592cd0 ["INT_ADD", "register:40f0:8", ["const:592cd0:8", "const:4:8"]]
- 00592cd0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00592d10 ["INT_ADD", "register:40f0:8", ["const:592d10:8", "const:4:8"]]
+ 00592d10 ["CALL", null, ["callee:00c53d00:8"]]
- 00592cd0 bytes 04031b94
+ 00592d10 bytes fc031b94
- 00592c8c ["COPY", "tmp:0:8", ["const:28:8"]]
- 00592c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592ccc ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00592ccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592ccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592ccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c8c bytes 08a10091
+ 00592ccc bytes 08a11091
- 00592ca0 ["INT_ADD", "register:40f0:8", ["const:592ca0:8", "const:4:8"]]
- 00592ca0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00592ce0 ["INT_ADD", "register:40f0:8", ["const:592ce0:8", "const:4:8"]]
+ 00592ce0 ["CALL", null, ["callee:00c53d00:8"]]
- 00592ca0 bytes 10031b94
+ 00592ce0 bytes 08041b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c9f91f2894064b7a2958e4349309199"></a>

### [`00592d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592d40.md) → [`00592d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md) FUN_00592d80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00592d98",
      "incomplete_value": false,
      "site": "00592d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592d58",
      "incomplete_value": false,
      "site": "00592d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "00592d9c",
      "DATA",
      [
        "storage",
        "00c6d028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d9c",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592d40.md#insn-00592d9c) · [`00592d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592d40.md#insn-00592d58) · [`00592d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592d40.md#insn-00592d6c)
- 新版 [`00592ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592ddc) · [`00592d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592d98) · [`00592dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592dac)

~~~diff
- 00592d9c ["INT_ADD", "register:40f0:8", ["const:592d9c:8", "const:4:8"]]
- 00592d9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00592ddc ["INT_ADD", "register:40f0:8", ["const:592ddc:8", "const:4:8"]]
+ 00592ddc ["CALL", null, ["callee:00c53d00:8"]]
- 00592d9c bytes d1021b94
+ 00592ddc bytes c9031b94
- 00592d58 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00592d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d98 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00592d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592d58 bytes 08a10091
+ 00592d98 bytes 08a11091
- 00592d6c ["INT_ADD", "register:40f0:8", ["const:592d6c:8", "const:4:8"]]
- 00592d6c ["CALL", null, ["callee:00c53d00:8"]]
+ 00592dac ["INT_ADD", "register:40f0:8", ["const:592dac:8", "const:4:8"]]
+ 00592dac ["CALL", null, ["callee:00c53d00:8"]]
- 00592d6c bytes dd021b94
+ 00592dac bytes d5031b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca08da5b628dcb10354ae10b1248e44d"></a>

### [`00592f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592f78.md) → [`00592fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md) FUN_00592fb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00592ff0",
      "incomplete_value": false,
      "site": "00593004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592fb0",
      "incomplete_value": false,
      "site": "00592fc4",
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
            "const:d20:8"
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
      "definition_site": "00592ff8",
      "incomplete_value": false,
      "site": "00593004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592fb8",
      "incomplete_value": false,
      "site": "00592fc4",
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
            "const:d30:8"
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
      "00592ff0",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592ff8",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592ff0",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592ff8",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592f78.md#insn-00592fc4) · [`00592fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592f78.md#insn-00592fac) · [`00592fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592f78.md#insn-00592fb0)
- 新版 [`00593004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00593004) · [`00592fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00592fec) · [`00592ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00592ff0)

~~~diff
- 00592fc4 ["INT_ADD", "register:40f0:8", ["const:592fc4:8", "const:4:8"]]
- 00592fc4 ["CALL", null, ["callee:00c58610:8"]]
+ 00593004 ["INT_ADD", "register:40f0:8", ["const:593004:8", "const:4:8"]]
+ 00593004 ["CALL", null, ["callee:00c58610:8"]]
- 00592fc4 bytes 93141b94
+ 00593004 bytes 83151b94
- 00592fac ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 00592fec ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 00592fac bytes c13600d0
+ 00592fec bytes c13600f0
- 00592fb0 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00592fb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00592fb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00592fb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00592ff0 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00592ff0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00592ff0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00592ff0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00592fb0 bytes 21803491
+ 00592ff0 bytes 21800491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2481c105c46bf9a3c72587c8f41115ca"></a>

### [`00593134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593134.md) → [`00593174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md) FUN_00593174

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ad0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005931b4",
      "incomplete_value": true,
      "site": "005931c0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593174",
      "incomplete_value": true,
      "site": "00593180",
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
            "const:d30:8"
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
      "005931ac",
      "PARAM",
      [
        "storage",
        "00c6cd20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005931b4",
      "PARAM",
      [
        "storage",
        "00c6cd30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005931ac",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005931b4",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593134.md#insn-00593180) · [`00593168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593134.md#insn-00593168) · [`0059316c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593134.md#insn-0059316c)
- 新版 [`005931c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931c0) · [`005931a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931a8) · [`005931ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931ac)

~~~diff
- 00593180 ["INT_ADD", "register:40f0:8", ["const:593180:8", "const:4:8"]]
- 00593180 ["CALL", null, ["callee:00c58610:8"]]
+ 005931c0 ["INT_ADD", "register:40f0:8", ["const:5931c0:8", "const:4:8"]]
+ 005931c0 ["CALL", null, ["callee:00c58610:8"]]
- 00593180 bytes 24141b94
+ 005931c0 bytes 14151b94
- 00593168 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 005931a8 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 00593168 bytes c13600b0
+ 005931a8 bytes c13600d0
- 0059316c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0059316c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0059316c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0059316c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005931ac ["COPY", "tmp:0:8", ["const:120:8"]]
+ 005931ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005931ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005931ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0059316c bytes 21803491
+ 005931ac bytes 21800491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a73e67ed5b74679a2713fa55d9d430"></a>

### [`005932f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/005932f0.md) → [`00593330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593330.md) FUN_00593330

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
      "definition_site": "00593334",
      "incomplete_value": false,
      "site": "00593338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005932f4",
      "incomplete_value": false,
      "site": "005932f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "00593338",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593338",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005932f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/005932f0.md#insn-005932f4)
- 新版 [`00593334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593330.md#insn-00593334)

~~~diff
- 005932f4 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005932f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005932f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005932f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593334 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00593334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005932f4 bytes 08810191
+ 00593334 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdf3c30b7a5ed588a82c96d719f2af93"></a>

### [`00593300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593300.md) → [`00593340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md) FUN_00593340

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
      "definition_site": "00593350",
      "incomplete_value": false,
      "site": "00593358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593310",
      "incomplete_value": false,
      "site": "00593318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "00593358",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593358",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593300.md#insn-00593310) · [`0059331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593300.md#insn-0059331c)
- 新版 [`00593350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md#insn-00593350) · [`0059335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md#insn-0059335c)

~~~diff
- 00593310 ["COPY", "tmp:0:8", ["const:60:8"]]
- 00593310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593350 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00593350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593310 bytes 08810191
+ 00593350 bytes 08811191
- 0059331c ["INT_ADD", "register:40f0:8", ["const:59331c:8", "const:4:8"]]
- 0059331c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0059335c ["INT_ADD", "register:40f0:8", ["const:59335c:8", "const:4:8"]]
+ 0059335c ["CALL", null, ["callee:00c57ea0:8"]]
- 0059331c bytes e1111b94
+ 0059335c bytes d1121b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8f1bbc8b79cd70ee43d6009e2ef509"></a>

### [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) → [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) FUN_00593380

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00446d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d30.md) [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00593784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593784.md)
- 新版 呼出元 1件 [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md) [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`005937c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/005937c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005933c0",
      "incomplete_value": false,
      "site": "005933c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593380",
      "incomplete_value": false,
      "site": "00593384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "005933c4",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005933c4",
      "DATA",
      [
        "storage",
        "00c6d4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md#insn-00593380) · [`00593388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md#insn-00593388) · [`005933dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md#insn-005933dc)
- 新版 [`005933c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-005933c0) · [`005933c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-005933c8) · [`0059341c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-0059341c)

~~~diff
- 00593380 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00593380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005933c0 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005933c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005933c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005933c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593380 bytes 08c10291
+ 005933c0 bytes 08c11291
- 00593388 ["INT_ADD", "register:40f0:8", ["const:593388:8", "const:4:8"]]
- 00593388 ["CALL", null, ["callee:00555288:8"]]
+ 005933c8 ["INT_ADD", "register:40f0:8", ["const:5933c8:8", "const:4:8"]]
+ 005933c8 ["CALL", null, ["callee:00555288:8"]]
- 00593388 bytes b007ff97
+ 005933c8 bytes b007ff97
- 005933dc ["INT_ADD", "register:40f0:8", ["const:5933dc:8", "const:4:8"]]
- 005933dc ["CALL", null, ["callee:0043bb20:8"]]
+ 0059341c ["INT_ADD", "register:40f0:8", ["const:59341c:8", "const:4:8"]]
+ 0059341c ["CALL", null, ["callee:0043bb20:8"]]
- 005933dc bytes c1a1fa97
+ 0059341c bytes c1a1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd93750f9f08d98c139ca9ddfc6e87f"></a>

### [`00593c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md) → [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) FUN_00593ca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059121c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00591/0059121c.md) · 呼出先 21件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) · 呼出先 21件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594190",
      "incomplete_value": false,
      "site": "0059419c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594150",
      "incomplete_value": false,
      "site": "0059415c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593d90",
      "incomplete_value": false,
      "site": "00593d9c",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593d50",
      "incomplete_value": false,
      "site": "00593d5c",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593dbc",
      "incomplete_value": false,
      "site": "00593dc4",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593d7c",
      "incomplete_value": false,
      "site": "00593d84",
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
            "const:ba0:8"
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
      "00593d90",
      "PARAM",
      [
        "storage",
        "002b61e8",
        null,
        "string"
      ]
    ],
    [
      "00593dbc",
      "PARAM",
      [
        "storage",
        "002b4ba0",
        null,
        null
      ]
    ],
    [
      "00593ed4",
      "PARAM",
      [
        "storage",
        "002a016d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00593d90",
      "PARAM",
      [
        "storage",
        "002b6228",
        null,
        "string"
      ]
    ],
    [
      "00593dbc",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ],
    [
      "00593ed4",
      "PARAM",
      [
        "storage",
        "002a023a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md#insn-00593d5c) · [`00593d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md#insn-00593d84) · [`00593ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593c64.md#insn-00593ea0)
- 新版 [`00593d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593d9c) · [`00593dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593dc4) · [`00593ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593ee0)

~~~diff
- 00593d5c ["INT_ADD", "register:40f0:8", ["const:593d5c:8", "const:4:8"]]
- 00593d5c ["CALL", null, ["callee:00c57f60:8"]]
+ 00593d9c ["INT_ADD", "register:40f0:8", ["const:593d9c:8", "const:4:8"]]
+ 00593d9c ["CALL", null, ["callee:00c57f60:8"]]
- 00593d5c bytes 810f1b94
+ 00593d9c bytes 71101b94
- 00593d84 ["INT_ADD", "register:40f0:8", ["const:593d84:8", "const:4:8"]]
- 00593d84 ["CALL", null, ["callee:00c57f70:8"]]
+ 00593dc4 ["INT_ADD", "register:40f0:8", ["const:593dc4:8", "const:4:8"]]
+ 00593dc4 ["CALL", null, ["callee:00c57f70:8"]]
- 00593d84 bytes 7b0f1b94
+ 00593dc4 bytes 6b101b94
- 00593ea0 ["INT_ADD", "register:40f0:8", ["const:593ea0:8", "const:4:8"]]
- 00593ea0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00593ee0 ["INT_ADD", "register:40f0:8", ["const:593ee0:8", "const:4:8"]]
+ 00593ee0 ["CALL", null, ["callee:00c57f60:8"]]
- 00593ea0 bytes 300f1b94
+ 00593ee0 bytes 20101b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0129ba0961685a57cd56eb545473ef2"></a>

### [`00594860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594860.md) → [`005948a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948a0.md) FUN_005948a0

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
      "definition_site": "005948a4",
      "incomplete_value": false,
      "site": "005948a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594864",
      "incomplete_value": false,
      "site": "00594868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "005948a8",
      "DATA",
      [
        "storage",
        "00c6d108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005948a8",
      "DATA",
      [
        "storage",
        "00c6d508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594860.md#insn-00594864)
- 新版 [`005948a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948a0.md#insn-005948a4)

~~~diff
- 00594864 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00594864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005948a4 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 005948a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005948a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005948a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594864 bytes 08210491
+ 005948a4 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4ff2d24ea379337daf53476b24d900"></a>

### [`00594870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594870.md) → [`005948b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md) FUN_005948b0

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
      "definition_site": "005948c0",
      "incomplete_value": false,
      "site": "005948c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594880",
      "incomplete_value": false,
      "site": "00594888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "005948c8",
      "DATA",
      [
        "storage",
        "00c6d108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005948c8",
      "DATA",
      [
        "storage",
        "00c6d508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594870.md#insn-00594880) · [`0059488c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594870.md#insn-0059488c)
- 新版 [`005948c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md#insn-005948c0) · [`005948cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md#insn-005948cc)

~~~diff
- 00594880 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00594880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005948c0 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 005948c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005948c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005948c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594880 bytes 08210491
+ 005948c0 bytes 08211491
- 0059488c ["INT_ADD", "register:40f0:8", ["const:59488c:8", "const:4:8"]]
- 0059488c ["CALL", null, ["callee:00c57ea0:8"]]
+ 005948cc ["INT_ADD", "register:40f0:8", ["const:5948cc:8", "const:4:8"]]
+ 005948cc ["CALL", null, ["callee:00c57ea0:8"]]
- 0059488c bytes 850c1b94
+ 005948cc bytes 750d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb9589328760e52c79c38e210a11670"></a>

### [`005948a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md) → [`005948e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md) FUN_005948e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00555248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555248.md) [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a240.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a640.md)

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
      "definition_site": "005948f4",
      "incomplete_value": false,
      "site": "005948f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005948b4",
      "incomplete_value": false,
      "site": "005948b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "005948f8",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005948f8",
      "DATA",
      [
        "storage",
        "00c6d4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md#insn-005948b4) · [`005948bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md#insn-005948bc) · [`005948c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md#insn-005948c8)
- 新版 [`005948f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-005948f4) · [`005948fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-005948fc) · [`00594908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-00594908)

~~~diff
- 005948b4 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 005948b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005948b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005948b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005948f4 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005948f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005948f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005948f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005948b4 bytes 08c10291
+ 005948f4 bytes 08c11291
- 005948bc ["INT_ADD", "register:40f0:8", ["const:5948bc:8", "const:4:8"]]
- 005948bc ["CALL", null, ["callee:00555288:8"]]
+ 005948fc ["INT_ADD", "register:40f0:8", ["const:5948fc:8", "const:4:8"]]
+ 005948fc ["CALL", null, ["callee:00555288:8"]]
- 005948bc bytes 6302ff97
+ 005948fc bytes 6302ff97
- 005948c8 ["INT_ADD", "register:40f0:8", ["const:5948c8:8", "const:4:8"]]
- 005948c8 ["CALL", null, ["callee:00c5a640:8"]]
+ 00594908 ["INT_ADD", "register:40f0:8", ["const:594908:8", "const:4:8"]]
+ 00594908 ["CALL", null, ["callee:00c5a640:8"]]
- 005948c8 bytes 5e161b94
+ 00594908 bytes 4e171b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f90f34227cb6f6cc68928a514e66ef77"></a>

### [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) → [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) FUN_00594938

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00588488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588488.md) · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005884c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059496c",
      "incomplete_value": false,
      "site": "0059497c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059492c",
      "incomplete_value": false,
      "site": "0059493c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "definition_site": "00594aa0",
      "incomplete_value": true,
      "site": "00594aac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594a60",
      "incomplete_value": true,
      "site": "00594a6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:cf8:8"
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
      "0059497c",
      "DATA",
      [
        "storage",
        "00c6d158",
        null,
        "undefined *"
      ]
    ],
    [
      "00594aa0",
      "READ",
      [
        "storage",
        "002c3cf8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059497c",
      "DATA",
      [
        "storage",
        "00c6d558",
        null,
        "undefined *"
      ]
    ],
    [
      "00594aa0",
      "READ",
      [
        "storage",
        "002c3d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059492c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md#insn-0059492c) · [`00594960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md#insn-00594960) · [`00594978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md#insn-00594978)
- 新版 [`0059496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-0059496c) · [`005949a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-005949a0) · [`005949b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-005949b8)

~~~diff
- 0059492c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0059492c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059492c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059492c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059496c ["COPY", "tmp:0:8", ["const:558:8"]]
+ 0059496c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059496c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059496c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059492c bytes 29610591
+ 0059496c bytes 29611591
- 00594960 ["INT_ADD", "register:40f0:8", ["const:594960:8", "const:4:8"]]
- 00594960 ["CALL", null, ["callee:00c57e90:8"]]
+ 005949a0 ["INT_ADD", "register:40f0:8", ["const:5949a0:8", "const:4:8"]]
+ 005949a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00594960 bytes 4c0c1b94
+ 005949a0 bytes 3c0d1b94
- 00594978 ["INT_ADD", "register:40f0:8", ["const:594978:8", "const:4:8"]]
- 00594978 ["CALL", null, ["callee:00c58090:8"]]
+ 005949b8 ["INT_ADD", "register:40f0:8", ["const:5949b8:8", "const:4:8"]]
+ 005949b8 ["CALL", null, ["callee:00c58090:8"]]
- 00594978 bytes c60c1b94
+ 005949b8 bytes b60d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925c82bca22847e3b3a2ce1591053226"></a>

### [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) → [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) FUN_00594b6c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005948f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948f8.md) · 呼出先 12件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f4ec.md) [`0055f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f500.md) [`0055f520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f520.md) [`00595150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md)
- 新版 呼出元 1件 [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) · 呼出先 12件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f52c.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md) [`0055f560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f560.md) [`00595190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595190.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.23% / 新版 97.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00594cf4",
      "incomplete_value": true,
      "site": "00594d04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594cb4",
      "incomplete_value": true,
      "site": "00594cc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1f:8"
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
      "00594cf4",
      "READ",
      [
        "storage",
        "002afb1f",
        null,
        "string"
      ]
    ],
    [
      "00594cf8",
      "READ",
      [
        "storage",
        "002afb2a",
        null,
        "string"
      ]
    ],
    [
      "00594cfc",
      "READ",
      [
        "storage",
        "002c2640",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00594cf4",
      "READ",
      [
        "storage",
        "002afb5f",
        null,
        "string"
      ]
    ],
    [
      "00594cf8",
      "READ",
      [
        "storage",
        "002afb6a",
        null,
        "string"
      ]
    ],
    [
      "00594cfc",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md#insn-00594d04) · [`00594b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md#insn-00594b80) · [`00594b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md#insn-00594b9c)
- 新版 [`00594d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594d44) · [`00594bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594bc0) · [`00594bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594bdc)

~~~diff
- 00594d04 ["INT_ADD", "register:40f0:8", ["const:594d04:8", "const:4:8"]]
- 00594d04 ["CALL", null, ["callee:005951d0:8"]]
+ 00594d44 ["INT_ADD", "register:40f0:8", ["const:594d44:8", "const:4:8"]]
+ 00594d44 ["CALL", null, ["callee:005951d0:8"]]
- 00594d04 bytes 23010094
+ 00594d44 bytes 23010094
- 00594b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00594b80 ["INT_ADD", "register:40f0:8", ["const:594b80:8", "const:4:8"]]
- 00594b80 ["CALLIND", null, ["register:0:8"]]
+ 00594bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00594bc0 ["INT_ADD", "register:40f0:8", ["const:594bc0:8", "const:4:8"]]
+ 00594bc0 ["CALLIND", null, ["register:0:8"]]
- 00594b80 bytes 00013fd6
+ 00594bc0 bytes 00013fd6
- 00594b9c ["COPY", "register:0:8", ["register:4048:8"]]
- 00594b9c ["INT_ADD", "register:40f0:8", ["const:594b9c:8", "const:4:8"]]
- 00594b9c ["CALLIND", null, ["register:0:8"]]
+ 00594bdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00594bdc ["INT_ADD", "register:40f0:8", ["const:594bdc:8", "const:4:8"]]
+ 00594bdc ["CALLIND", null, ["register:0:8"]]
- 00594b9c bytes 20013fd6
+ 00594bdc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d290152891c8509a86c12a60f217be5"></a>

### [`00594f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594f78.md) → [`00594fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md) FUN_00594fb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058855c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/0058855c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0058859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058859c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00594fd0",
      "incomplete_value": false,
      "site": "00594fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594f90",
      "incomplete_value": false,
      "site": "00594f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00594fd4",
      "DATA",
      [
        "storage",
        "00c6d158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594fd4",
      "DATA",
      [
        "storage",
        "00c6d558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594f78.md#insn-00594fd4) · [`00594f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594f78.md#insn-00594f90) · [`00594fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594f78.md#insn-00594fa0)
- 新版 [`00595014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00595014) · [`00594fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00594fd0) · [`00594fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00594fe0)

~~~diff
- 00594fd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00594fd4 ["INT_ADD", "register:40f0:8", ["const:594fd4:8", "const:4:8"]]
- 00594fd4 ["CALLIND", null, ["register:0:8"]]
+ 00595014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595014 ["INT_ADD", "register:40f0:8", ["const:595014:8", "const:4:8"]]
+ 00595014 ["CALLIND", null, ["register:0:8"]]
- 00594fd4 bytes 00013fd6
+ 00595014 bytes 00013fd6
- 00594f90 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00594f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594fd0 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00594fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594f90 bytes 08610591
+ 00594fd0 bytes 08611591
- 00594fa0 ["INT_ADD", "register:40f0:8", ["const:594fa0:8", "const:4:8"]]
- 00594fa0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00594fe0 ["INT_ADD", "register:40f0:8", ["const:594fe0:8", "const:4:8"]]
+ 00594fe0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00594fa0 bytes c40a1b94
+ 00594fe0 bytes b40b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ec0c35a631db178f26bd21feb5c120"></a>

### [`0059532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059532c.md) → [`0059536c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md) FUN_0059536c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595444",
      "incomplete_value": false,
      "site": "00595448",
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
            "const:67e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595404",
      "incomplete_value": false,
      "site": "00595408",
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
            "const:5a2:8"
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
      "definition_site": "00595474",
      "incomplete_value": false,
      "site": "00595478",
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
      "definition_site": "00595434",
      "incomplete_value": false,
      "site": "00595438",
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
      "005953e4",
      "PARAM",
      [
        "storage",
        "002ae6ba",
        null,
        null
      ]
    ],
    [
      "005953e4",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ],
    [
      "00595444",
      "PARAM",
      [
        "storage",
        "002a75a2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005953e4",
      "PARAM",
      [
        "storage",
        "002ae6fa",
        null,
        null
      ]
    ],
    [
      "005953e4",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ],
    [
      "00595444",
      "PARAM",
      [
        "storage",
        "002a767e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059532c.md#insn-00595408) · [`00595438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059532c.md#insn-00595438) · [`00595390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059532c.md#insn-00595390)
- 新版 [`00595448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-00595448) · [`00595478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-00595478) · [`005953d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-005953d0)

~~~diff
- 00595408 ["INT_ADD", "register:40f0:8", ["const:595408:8", "const:4:8"]]
- 00595408 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00595448 ["INT_ADD", "register:40f0:8", ["const:595448:8", "const:4:8"]]
+ 00595448 ["CALL", null, ["callee:00c57fe0:8"]]
- 00595408 bytes f6091b94
+ 00595448 bytes e60a1b94
- 00595438 ["INT_ADD", "register:40f0:8", ["const:595438:8", "const:4:8"]]
- 00595438 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00595478 ["INT_ADD", "register:40f0:8", ["const:595478:8", "const:4:8"]]
+ 00595478 ["CALL", null, ["callee:00c57fe0:8"]]
- 00595438 bytes ea091b94
+ 00595478 bytes da0a1b94
- 00595390 ["COPY", "tmp:0:8", ["const:6ba:8"]]
- 00595390 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00595390 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00595390 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005953d0 ["COPY", "tmp:0:8", ["const:6fa:8"]]
+ 005953d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005953d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005953d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00595390 bytes 29e91a91
+ 005953d0 bytes 29e91b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c3ec32235e521c077511fc8cacfc99"></a>

### [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) → [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) FUN_00595580

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) · 呼出先 2件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) · 呼出先 2件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00595594",
      "incomplete_value": false,
      "site": "0059559c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595554",
      "incomplete_value": false,
      "site": "0059555c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "0059559c",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059559c",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md#insn-00595554) · [`00595584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md#insn-00595584) · [`00595598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md#insn-00595598)
- 新版 [`00595594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-00595594) · [`005955c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-005955c4) · [`005955d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-005955d8)

~~~diff
- 00595554 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00595554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595594 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00595594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595554 bytes 08a10791
+ 00595594 bytes 08a11791
- 00595584 ["INT_ADD", "register:40f0:8", ["const:595584:8", "const:4:8"]]
- 00595584 ["CALL", null, ["callee:00c53cd0:8"]]
+ 005955c4 ["INT_ADD", "register:40f0:8", ["const:5955c4:8", "const:4:8"]]
+ 005955c4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00595584 bytes cbf81a94
+ 005955c4 bytes c3f91a94
- 00595598 ["COPY", "register:0:8", ["register:4040:8"]]
- 00595598 ["INT_ADD", "register:40f0:8", ["const:595598:8", "const:4:8"]]
- 00595598 ["CALLIND", null, ["register:0:8"]]
+ 005955d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005955d8 ["INT_ADD", "register:40f0:8", ["const:5955d8:8", "const:4:8"]]
+ 005955d8 ["CALLIND", null, ["register:0:8"]]
- 00595598 bytes 00013fd6
+ 005955d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41db0fb27d8f7fa3008d11dd260cbbd0"></a>

### [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) → [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) FUN_0059568c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) · 呼出先 4件 [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) · 呼出先 4件 [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005956e0",
      "incomplete_value": false,
      "site": "005956e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005956a0",
      "incomplete_value": false,
      "site": "005956a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "definition_site": "00595734",
      "incomplete_value": false,
      "site": "00595738",
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
      "definition_site": "005956f4",
      "incomplete_value": false,
      "site": "005956f8",
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
      "005956e4",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00595738",
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
      "005956e4",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595738",
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

- 旧版 [`00595668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md#insn-00595668) · [`00595688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md#insn-00595688) · [`005956a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md#insn-005956a0)
- 新版 [`005956a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956a8) · [`005956c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956c8) · [`005956e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956e0)

~~~diff
- 00595668 ["INT_ADD", "register:40f0:8", ["const:595668:8", "const:4:8"]]
- 00595668 ["CALL", null, ["callee:00595870:8"]]
+ 005956a8 ["INT_ADD", "register:40f0:8", ["const:5956a8:8", "const:4:8"]]
+ 005956a8 ["CALL", null, ["callee:00595870:8"]]
- 00595668 bytes 72000094
+ 005956a8 bytes 72000094
- 00595688 ["INT_ADD", "register:40f0:8", ["const:595688:8", "const:4:8"]]
- 00595688 ["CALL", null, ["callee:00c57e90:8"]]
+ 005956c8 ["INT_ADD", "register:40f0:8", ["const:5956c8:8", "const:4:8"]]
+ 005956c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00595688 bytes 02091b94
+ 005956c8 bytes f2091b94
- 005956a0 ["COPY", "tmp:0:8", ["const:278:8"]]
- 005956a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005956a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005956a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005956e0 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 005956e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005956e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005956e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005956a0 bytes 08e10991
+ 005956e0 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf2e2fae17f526f8d13cbc3829203bea"></a>

### [`00595744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595744.md) → [`00595784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md) FUN_00595784

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0059579c",
      "incomplete_value": false,
      "site": "005957a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059575c",
      "incomplete_value": false,
      "site": "00595764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "005957a4",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005957a4",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059575c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595744.md#insn-0059575c) · [`00595774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595744.md#insn-00595774) · [`00595788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595744.md#insn-00595788)
- 新版 [`0059579c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-0059579c) · [`005957b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-005957b4) · [`005957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-005957c8)

~~~diff
- 0059575c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0059575c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059575c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059575c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059579c ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 0059579c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059579c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059579c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059575c bytes 08a10791
+ 0059579c bytes 08a11791
- 00595774 ["COPY", "register:0:8", ["register:4040:8"]]
- 00595774 ["INT_ADD", "register:40f0:8", ["const:595774:8", "const:4:8"]]
- 00595774 ["CALLIND", null, ["register:0:8"]]
+ 005957b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005957b4 ["INT_ADD", "register:40f0:8", ["const:5957b4:8", "const:4:8"]]
+ 005957b4 ["CALLIND", null, ["register:0:8"]]
- 00595774 bytes 00013fd6
+ 005957b4 bytes 00013fd6
- 00595788 ["INT_ADD", "register:40f0:8", ["const:595788:8", "const:4:8"]]
- 00595788 ["CALL", null, ["callee:00c53d00:8"]]
+ 005957c8 ["INT_ADD", "register:40f0:8", ["const:5957c8:8", "const:4:8"]]
+ 005957c8 ["CALL", null, ["callee:00c53d00:8"]]
- 00595788 bytes 56f81a94
+ 005957c8 bytes 4ef91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa7d336da1dce23d8b6aef0ef6c0fc70"></a>

### [`005957bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/005957bc.md) → [`005957fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md) FUN_005957fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00595814",
      "incomplete_value": false,
      "site": "0059581c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005957d4",
      "incomplete_value": false,
      "site": "005957dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "0059581c",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059581c",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059581c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/005957bc.md#insn-0059581c) · [`005957d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/005957bc.md#insn-005957d4) · [`005957ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/005957bc.md#insn-005957ec)
- 新版 [`0059585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-0059585c) · [`00595814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-00595814) · [`0059582c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-0059582c)

~~~diff
- 0059581c ["INT_ADD", "register:40f0:8", ["const:59581c:8", "const:4:8"]]
- 0059581c ["CALL", null, ["callee:00c57e80:8"]]
+ 0059585c ["INT_ADD", "register:40f0:8", ["const:59585c:8", "const:4:8"]]
+ 0059585c ["CALL", null, ["callee:00c57e80:8"]]
- 0059581c bytes 99081b94
+ 0059585c bytes 89091b94
- 005957d4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 005957d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005957d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005957d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595814 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00595814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005957d4 bytes 08a10791
+ 00595814 bytes 08a11791
- 005957ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005957ec ["INT_ADD", "register:40f0:8", ["const:5957ec:8", "const:4:8"]]
- 005957ec ["CALLIND", null, ["register:0:8"]]
+ 0059582c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059582c ["INT_ADD", "register:40f0:8", ["const:59582c:8", "const:4:8"]]
+ 0059582c ["CALLIND", null, ["register:0:8"]]
- 005957ec bytes 00013fd6
+ 0059582c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6215cef87b1b541dce686211b79a405"></a>

### [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) → [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) FUN_005959dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md)
- 新版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595a74",
      "incomplete_value": false,
      "site": "00595a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595a34",
      "incomplete_value": false,
      "site": "00595a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "definition_site": "00595b08",
      "incomplete_value": false,
      "site": "00595b0c",
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
      "definition_site": "00595ac8",
      "incomplete_value": false,
      "site": "00595acc",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595c98",
      "incomplete_value": true,
      "site": "00595c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595c58",
      "incomplete_value": true,
      "site": "00595c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
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
      "00595a78",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00595b0c",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "00595c5c",
      "READ",
      [
        "storage",
        "00c636e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595a78",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595b0c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "00595c5c",
      "READ",
      [
        "storage",
        "00c63ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md#insn-00595c5c) · [`00595c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md#insn-00595c9c) · [`005959c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md#insn-005959c0)
- 新版 [`00595c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595c9c) · [`00595cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595cdc) · [`00595a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595a00)

~~~diff
- 00595c5c ["INT_ADD", "register:40f0:8", ["const:595c5c:8", "const:4:8"]]
- 00595c5c ["CALL", null, ["callee:004594d0:8"]]
+ 00595c9c ["INT_ADD", "register:40f0:8", ["const:595c9c:8", "const:4:8"]]
+ 00595c9c ["CALL", null, ["callee:004594d0:8"]]
- 00595c5c bytes 0d0efb97
+ 00595c9c bytes 0d0efb97
- 00595c9c ["INT_ADD", "register:40f0:8", ["const:595c9c:8", "const:4:8"]]
- 00595c9c ["CALL", null, ["callee:00440ec0:8"]]
+ 00595cdc ["INT_ADD", "register:40f0:8", ["const:595cdc:8", "const:4:8"]]
+ 00595cdc ["CALL", null, ["callee:00440ec0:8"]]
- 00595c9c bytes 79acfa97
+ 00595cdc bytes 79acfa97
- 005959c0 ["INT_ADD", "register:40f0:8", ["const:5959c0:8", "const:4:8"]]
- 005959c0 ["CALL", null, ["callee:00595870:8"]]
+ 00595a00 ["INT_ADD", "register:40f0:8", ["const:595a00:8", "const:4:8"]]
+ 00595a00 ["CALL", null, ["callee:00595870:8"]]
- 005959c0 bytes 9cffff97
+ 00595a00 bytes 9cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-219e25e809c78e450ab9c7fd222fd6b5"></a>

### [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) → [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) FUN_00595d1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 15件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`0045bdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045b/0045bdb8.md) [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md)
- 新版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 15件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.46% / 新版 93.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595fe4",
      "incomplete_value": true,
      "site": "00595fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595fa4",
      "incomplete_value": true,
      "site": "00595fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
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
      "definition_site": "0059603c",
      "incomplete_value": false,
      "site": "00596040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:6f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595ffc",
      "incomplete_value": false,
      "site": "00596000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:61a:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596050",
      "incomplete_value": true,
      "site": "00596054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596010",
      "incomplete_value": true,
      "site": "00596014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00595dfc",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "00595e80",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00595f44",
      "READ",
      [
        "storage",
        "00c636e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595dfc",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "00595e80",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595f44",
      "READ",
      [
        "storage",
        "00c63ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md#insn-00595fa8) · [`00596000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md#insn-00596000) · [`00596014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md#insn-00596014)
- 新版 [`00595fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00595fe8) · [`00596040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00596040) · [`00596054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00596054)

~~~diff
- 00595fa8 ["INT_ADD", "register:40f0:8", ["const:595fa8:8", "const:4:8"]]
- 00595fa8 ["CALL", null, ["callee:004594d0:8"]]
+ 00595fe8 ["INT_ADD", "register:40f0:8", ["const:595fe8:8", "const:4:8"]]
+ 00595fe8 ["CALL", null, ["callee:004594d0:8"]]
- 00595fa8 bytes 3a0dfb97
+ 00595fe8 bytes 3a0dfb97
- 00596000 ["INT_ADD", "register:40f0:8", ["const:596000:8", "const:4:8"]]
- 00596000 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00596040 ["INT_ADD", "register:40f0:8", ["const:596040:8", "const:4:8"]]
+ 00596040 ["CALL", null, ["callee:00c57fe0:8"]]
- 00596000 bytes f8061b94
+ 00596040 bytes e8071b94
- 00596014 ["INT_ADD", "register:40f0:8", ["const:596014:8", "const:4:8"]]
- 00596014 ["CALL", null, ["callee:004594d0:8"]]
+ 00596054 ["INT_ADD", "register:40f0:8", ["const:596054:8", "const:4:8"]]
+ 00596054 ["CALL", null, ["callee:004594d0:8"]]
- 00596014 bytes 1f0dfb97
+ 00596054 bytes 1f0dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012069f490fdc4467a1dda72c7cd4a51"></a>

### [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) → [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) FUN_005960f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 3件 [`00596464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md) [`005967f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 3件 [`005964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md) [`00596838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596158",
      "incomplete_value": false,
      "site": "00596160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596118",
      "incomplete_value": false,
      "site": "00596120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "00596180",
      "incomplete_value": false,
      "site": "00596188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596140",
      "incomplete_value": false,
      "site": "00596148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00596160",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00596188",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "005961b4",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596160",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "00596188",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "005961b4",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md#insn-00596160) · [`00596110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md#insn-00596110) · [`00596118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md#insn-00596118)
- 新版 [`005961a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-005961a0) · [`00596150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-00596150) · [`00596158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-00596158)

~~~diff
- 00596160 ["INT_ADD", "register:40f0:8", ["const:596160:8", "const:4:8"]]
- 00596160 ["CALL", null, ["callee:00c57e90:8"]]
+ 005961a0 ["INT_ADD", "register:40f0:8", ["const:5961a0:8", "const:4:8"]]
+ 005961a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00596160 bytes 4c061b94
+ 005961a0 bytes 3c071b94
- 00596110 ["INT_ADD", "register:40f0:8", ["const:596110:8", "const:4:8"]]
- 00596110 ["CALL", null, ["callee:00c57e90:8"]]
+ 00596150 ["INT_ADD", "register:40f0:8", ["const:596150:8", "const:4:8"]]
+ 00596150 ["CALL", null, ["callee:00c57e90:8"]]
- 00596110 bytes 60061b94
+ 00596150 bytes 50071b94
- 00596118 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00596118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596158 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00596158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596118 bytes 08210891
+ 00596158 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e8146298120b74d89f5765f2b10e92"></a>

### [`00596464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md) → [`005964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md) FUN_005964a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005965f4",
      "incomplete_value": false,
      "site": "005965f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005965b4",
      "incomplete_value": false,
      "site": "005965b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "00596694",
      "incomplete_value": false,
      "site": "00596698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596654",
      "incomplete_value": false,
      "site": "00596658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "00596794",
      "incomplete_value": false,
      "site": "0059679c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596754",
      "incomplete_value": false,
      "site": "0059675c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00596588",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ],
    [
      "005965b4",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ],
    [
      "005965f8",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596588",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ],
    [
      "005965b4",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ],
    [
      "005965f8",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059654c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md#insn-0059654c) · [`00596504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md#insn-00596504) · [`00596524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596464.md#insn-00596524)
- 新版 [`0059658c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-0059658c) · [`00596544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-00596544) · [`00596564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-00596564)

~~~diff
- 0059654c ["INT_ADD", "register:40f0:8", ["const:59654c:8", "const:4:8"]]
- 0059654c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0059658c ["INT_ADD", "register:40f0:8", ["const:59658c:8", "const:4:8"]]
+ 0059658c ["CALL", null, ["callee:00c57fe0:8"]]
- 0059654c bytes a5051b94
+ 0059658c bytes 95061b94
- 00596504 ["INT_ADD", "register:40f0:8", ["const:596504:8", "const:4:8"]]
- 00596504 ["CALL", null, ["callee:00c57e90:8"]]
+ 00596544 ["INT_ADD", "register:40f0:8", ["const:596544:8", "const:4:8"]]
+ 00596544 ["CALL", null, ["callee:00c57e90:8"]]
- 00596504 bytes 63051b94
+ 00596544 bytes 53061b94
- 00596524 ["INT_ADD", "register:40f0:8", ["const:596524:8", "const:4:8"]]
- 00596524 ["CALL", null, ["callee:00c57f40:8"]]
+ 00596564 ["INT_ADD", "register:40f0:8", ["const:596564:8", "const:4:8"]]
+ 00596564 ["CALL", null, ["callee:00c57f40:8"]]
- 00596524 bytes 87051b94
+ 00596564 bytes 77061b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89329b0316928420db04cccc72fe17f3"></a>

### [`005967f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md) → [`00596838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md) FUN_00596838

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005960b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005960b4.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596bf4",
      "incomplete_value": false,
      "site": "00596bf8",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596bb4",
      "incomplete_value": false,
      "site": "00596bb8",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005969ac",
      "incomplete_value": false,
      "site": "005969b8",
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
            "const:ab1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059696c",
      "incomplete_value": false,
      "site": "00596978",
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
            "const:a71:8"
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
      "0059688c",
      "READ",
      [
        "storage",
        "00c9aee8",
        null,
        "pointer"
      ]
    ],
    [
      "00596908",
      "PARAM",
      [
        "storage",
        "002aea71",
        null,
        null
      ]
    ],
    [
      "00596978",
      "PARAM",
      [
        "storage",
        "002a321e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059688c",
      "READ",
      [
        "storage",
        "00c9b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00596908",
      "PARAM",
      [
        "storage",
        "002aeab1",
        null,
        null
      ]
    ],
    [
      "00596978",
      "PARAM",
      [
        "storage",
        "002a32eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md#insn-00596978) · [`00596840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md#insn-00596840) · [`00596848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005967f8.md#insn-00596848)
- 新版 [`005969b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-005969b8) · [`00596880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-00596880) · [`00596888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-00596888)

~~~diff
- 00596978 ["INT_ADD", "register:40f0:8", ["const:596978:8", "const:4:8"]]
- 00596978 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005969b8 ["INT_ADD", "register:40f0:8", ["const:5969b8:8", "const:4:8"]]
+ 005969b8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00596978 bytes 9a041b94
+ 005969b8 bytes 8a051b94
- 00596840 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
+ 00596880 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
- 00596840 bytes 35380090
+ 00596880 bytes 353800b0
- 00596848 ["COPY", "tmp:0:8", ["const:21e:8"]]
- 00596848 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00596848 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00596848 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00596888 ["COPY", "tmp:0:8", ["const:2eb:8"]]
+ 00596888 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00596888 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00596888 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00596848 bytes 947a0891
+ 00596888 bytes 94ae0b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c3a59b66d79b8edc092ab84dfd658e"></a>

### [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) → [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) FUN_00596d10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00459fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459fb0.md) [`0045a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a730.md) [`004600cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00460/004600cc.md) · 呼出先 5件 [`00595540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595540.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 14件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) [`0045a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md) [`0046010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md) · 呼出先 5件 [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596d68",
      "incomplete_value": false,
      "site": "00596d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d28",
      "incomplete_value": false,
      "site": "00596d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "definition_site": "00596d98",
      "incomplete_value": false,
      "site": "00596da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d58",
      "incomplete_value": false,
      "site": "00596d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "00596d68",
      "DATA",
      [
        "storage",
        "00c6d2d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596da0",
      "DATA",
      [
        "storage",
        "00c6d1e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596d68",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596da0",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md#insn-00596d20) · [`00596d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md#insn-00596d04) · [`00596d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md#insn-00596d18)
- 新版 [`00596d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d60) · [`00596d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d44) · [`00596d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d58)

~~~diff
- 00596d20 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00596d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596d60 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00596d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d20 bytes 08610b91
+ 00596d60 bytes 08611b91
- 00596d04 ["INT_ADD", "register:40f0:8", ["const:596d04:8", "const:4:8"]]
- 00596d04 ["CALL", null, ["callee:00595580:8"]]
+ 00596d44 ["INT_ADD", "register:40f0:8", ["const:596d44:8", "const:4:8"]]
+ 00596d44 ["CALL", null, ["callee:00595580:8"]]
- 00596d04 bytes 0ffaff97
+ 00596d44 bytes 0ffaff97
- 00596d18 ["INT_ADD", "register:40f0:8", ["const:596d18:8", "const:4:8"]]
- 00596d18 ["CALL", null, ["callee:00c57e90:8"]]
+ 00596d58 ["INT_ADD", "register:40f0:8", ["const:596d58:8", "const:4:8"]]
+ 00596d58 ["CALL", null, ["callee:00c57e90:8"]]
- 00596d18 bytes 5e031b94
+ 00596d58 bytes 4e041b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7cb9c03c7feacfd78838edf6d08bc7"></a>

### [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) → [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) FUN_00596f2c

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 42件 [`0045031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/0045031c.md) [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) · 呼出先 6件 [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 42件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) · 呼出先 6件 [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596f6c",
      "incomplete_value": false,
      "site": "00596f7c",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596f2c",
      "incomplete_value": false,
      "site": "00596f3c",
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
            "const:398:8"
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
      "definition_site": "00596f74",
      "incomplete_value": false,
      "site": "00596f7c",
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
    "old": {
      "definition_site": "00596f34",
      "incomplete_value": false,
      "site": "00596f3c",
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
            "const:718:8"
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
      "00596f6c",
      "PARAM",
      [
        "storage",
        "00c63398",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596f74",
      "PARAM",
      [
        "storage",
        "00c63718",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00596f6c",
      "PARAM",
      [
        "storage",
        "00c63798",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596f74",
      "PARAM",
      [
        "storage",
        "00c63b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md#insn-00596f3c) · [`00596f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md#insn-00596f7c) · [`00596f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md#insn-00596f10)
- 新版 [`00596f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596f7c) · [`00596fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596fbc) · [`00596f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596f50)

~~~diff
- 00596f3c ["INT_ADD", "register:40f0:8", ["const:596f3c:8", "const:4:8"]]
- 00596f3c ["CALL", null, ["callee:00c58610:8"]]
+ 00596f7c ["INT_ADD", "register:40f0:8", ["const:596f7c:8", "const:4:8"]]
+ 00596f7c ["CALL", null, ["callee:00c58610:8"]]
- 00596f3c bytes b5041b94
+ 00596f7c bytes a5051b94
- 00596f7c ["INT_ADD", "register:40f0:8", ["const:596f7c:8", "const:4:8"]]
- 00596f7c ["CALL", null, ["callee:00c53d00:8"]]
+ 00596fbc ["INT_ADD", "register:40f0:8", ["const:596fbc:8", "const:4:8"]]
+ 00596fbc ["CALL", null, ["callee:00c53d00:8"]]
- 00596f7c bytes 59f21a94
+ 00596fbc bytes 51f31a94
- 00596f10 ["INT_ADD", "register:40f0:8", ["const:596f10:8", "const:4:8"]]
- 00596f10 ["CALL", null, ["callee:00596d10:8"]]
+ 00596f50 ["INT_ADD", "register:40f0:8", ["const:596f50:8", "const:4:8"]]
+ 00596f50 ["CALL", null, ["callee:00596d10:8"]]
- 00596f10 bytes 70ffff97
+ 00596f50 bytes 70ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71fe6e5cc4dfd046f34d34b41233ee12"></a>

### [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) → [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md) FUN_0059701c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00496a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md) [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) · 呼出先 6件 [`00596ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00496a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md) [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) · 呼出先 6件 [`00596e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059705c",
      "incomplete_value": false,
      "site": "0059706c",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059701c",
      "incomplete_value": false,
      "site": "0059702c",
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
            "const:398:8"
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
      "definition_site": "00597064",
      "incomplete_value": false,
      "site": "0059706c",
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
    "old": {
      "definition_site": "00597024",
      "incomplete_value": false,
      "site": "0059702c",
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
            "const:718:8"
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
      "0059705c",
      "PARAM",
      [
        "storage",
        "00c63398",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00597064",
      "PARAM",
      [
        "storage",
        "00c63718",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0059705c",
      "PARAM",
      [
        "storage",
        "00c63798",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00597064",
      "PARAM",
      [
        "storage",
        "00c63b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059702c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md#insn-0059702c) · [`0059706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md#insn-0059706c) · [`00597000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md#insn-00597000)
- 新版 [`0059706c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-0059706c) · [`005970ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-005970ac) · [`00597040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-00597040)

~~~diff
- 0059702c ["INT_ADD", "register:40f0:8", ["const:59702c:8", "const:4:8"]]
- 0059702c ["CALL", null, ["callee:00c58610:8"]]
+ 0059706c ["INT_ADD", "register:40f0:8", ["const:59706c:8", "const:4:8"]]
+ 0059706c ["CALL", null, ["callee:00c58610:8"]]
- 0059702c bytes 79041b94
+ 0059706c bytes 69051b94
- 0059706c ["INT_ADD", "register:40f0:8", ["const:59706c:8", "const:4:8"]]
- 0059706c ["CALL", null, ["callee:00c53d00:8"]]
+ 005970ac ["INT_ADD", "register:40f0:8", ["const:5970ac:8", "const:4:8"]]
+ 005970ac ["CALL", null, ["callee:00c53d00:8"]]
- 0059706c bytes 1df21a94
+ 005970ac bytes 15f31a94
- 00597000 ["INT_ADD", "register:40f0:8", ["const:597000:8", "const:4:8"]]
- 00597000 ["CALL", null, ["callee:00596e1c:8"]]
+ 00597040 ["INT_ADD", "register:40f0:8", ["const:597040:8", "const:4:8"]]
+ 00597040 ["CALL", null, ["callee:00596e1c:8"]]
- 00597000 bytes 77ffff97
+ 00597040 bytes 77ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2145266e5c3c870aa97d82873bf389"></a>

### [`005970d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d4.md) → [`00597114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md) FUN_00597114

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0059712c",
      "incomplete_value": false,
      "site": "00597130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005970ec",
      "incomplete_value": false,
      "site": "005970f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00597130",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00597130",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005970ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d4.md#insn-005970ec) · [`0059712c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d4.md#insn-0059712c)
- 新版 [`0059712c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md#insn-0059712c) · [`0059716c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md#insn-0059716c)

~~~diff
- 005970ec ["COPY", "tmp:0:8", ["const:278:8"]]
- 005970ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005970ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005970ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059712c ["COPY", "tmp:0:8", ["const:678:8"]]
+ 0059712c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059712c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059712c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005970ec bytes 08e10991
+ 0059712c bytes 08e11991
- 0059712c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059712c ["INT_ADD", "register:40f0:8", ["const:59712c:8", "const:4:8"]]
- 0059712c ["CALLIND", null, ["register:0:8"]]
+ 0059716c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059716c ["INT_ADD", "register:40f0:8", ["const:59716c:8", "const:4:8"]]
+ 0059716c ["CALLIND", null, ["register:0:8"]]
- 0059712c bytes 00013fd6
+ 0059716c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a6500869f71591b4e9dcd7bcc990289"></a>

### [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) → [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) FUN_0059719c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005971b8",
      "incomplete_value": false,
      "site": "005971bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597178",
      "incomplete_value": false,
      "site": "0059717c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "005971bc",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005971bc",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md#insn-00597178) · [`005971b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md#insn-005971b4) · [`005971c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md#insn-005971c4)
- 新版 [`005971b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-005971b8) · [`005971f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-005971f4) · [`00597204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-00597204)

~~~diff
- 00597178 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00597178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005971b8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 005971b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005971b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005971b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597178 bytes 08e10991
+ 005971b8 bytes 08e11991
- 005971b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005971b4 ["INT_ADD", "register:40f0:8", ["const:5971b4:8", "const:4:8"]]
- 005971b4 ["CALLIND", null, ["register:0:8"]]
+ 005971f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005971f4 ["INT_ADD", "register:40f0:8", ["const:5971f4:8", "const:4:8"]]
+ 005971f4 ["CALLIND", null, ["register:0:8"]]
- 005971b4 bytes 00013fd6
+ 005971f4 bytes 00013fd6
- 005971c4 ["INT_ADD", "register:40f0:8", ["const:5971c4:8", "const:4:8"]]
- 005971c4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00597204 ["INT_ADD", "register:40f0:8", ["const:597204:8", "const:4:8"]]
+ 00597204 ["CALL", null, ["callee:00c57eb0:8"]]
- 005971c4 bytes 3b021b94
+ 00597204 bytes 2b031b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff713879b96ff3dedfb6e16257edf34"></a>

### [`005971dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md) → [`0059721c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md) FUN_0059721c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md) [`00766fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766fdc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md) [`0076701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/0076701c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00597228",
      "incomplete_value": false,
      "site": "0059722c",
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
      "definition_site": "005971e8",
      "incomplete_value": false,
      "site": "005971ec",
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
      "00597228",
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
      "00597228",
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

- 旧版 [`005971ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md#insn-005971ec) · [`005971e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md#insn-005971e8)
- 新版 [`0059722c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md#insn-0059722c) · [`00597228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md#insn-00597228)

~~~diff
- 005971ec ["INT_ADD", "register:40f0:8", ["const:5971ec:8", "const:4:8"]]
- 005971ec ["CALL", null, ["callee:0043b778:8"]]
+ 0059722c ["INT_ADD", "register:40f0:8", ["const:59722c:8", "const:4:8"]]
+ 0059722c ["CALL", null, ["callee:0043b778:8"]]
- 005971ec bytes 5391fa97
+ 0059722c bytes 5391fa97
- 005971e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005971e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005971e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005971e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00597228 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00597228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00597228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00597228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005971e8 bytes 00303c91
+ 00597228 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92fa6a033cd6360e843367c1b57580ca"></a>

### [`005978a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005978a0.md) → [`005978e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md) FUN_005978e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059777c.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005977bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005977bc.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597948",
      "incomplete_value": true,
      "site": "0059794c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "0059790c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:ef0:8"
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
      "00597948",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00597948",
      "PARAM",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00597948",
      "READ",
      [
        "storage",
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00597948",
      "PARAM",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005978a0.md#insn-0059790c) · [`005978dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005978a0.md#insn-005978dc) · [`005978fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005978a0.md#insn-005978fc)
- 新版 [`0059794c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059794c) · [`0059791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059791c) · [`0059793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059793c)

~~~diff
- 0059790c ["INT_ADD", "register:40f0:8", ["const:59790c:8", "const:4:8"]]
- 0059790c ["CALL", null, ["callee:00c58280:8"]]
+ 0059794c ["INT_ADD", "register:40f0:8", ["const:59794c:8", "const:4:8"]]
+ 0059794c ["CALL", null, ["callee:00c58280:8"]]
- 0059790c bytes 5d011b94
+ 0059794c bytes 4d021b94
- 005978dc ["INT_ADD", "register:40f0:8", ["const:5978dc:8", "const:4:8"]]
- 005978dc ["CALL", null, ["callee:00c59dd0:8"]]
+ 0059791c ["INT_ADD", "register:40f0:8", ["const:59791c:8", "const:4:8"]]
+ 0059791c ["CALL", null, ["callee:00c59dd0:8"]]
- 005978dc bytes 3d081b94
+ 0059791c bytes 2d091b94
- 005978fc ["INT_ADD", "register:40f0:8", ["const:5978fc:8", "const:4:8"]]
- 005978fc ["CALL", null, ["callee:00c58270:8"]]
+ 0059793c ["INT_ADD", "register:40f0:8", ["const:59793c:8", "const:4:8"]]
+ 0059793c ["CALL", null, ["callee:00c58270:8"]]
- 005978fc bytes 5d011b94
+ 0059793c bytes 4d021b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dbb71f37326648cf25604b3100ad334"></a>

### [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md) → [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md) FUN_00597a94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`009bab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md) · 呼出先 9件 [`00597c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 2件 [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`009bad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009bad00.md) · 呼出先 9件 [`00597c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597b4c",
      "incomplete_value": true,
      "site": "00597b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00597b0c",
      "incomplete_value": true,
      "site": "00597b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00597ac8",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00597acc",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ae4",
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
      "00597ac8",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00597acc",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ae4",
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

- 旧版 [`00597ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md#insn-00597ad0) · [`00597a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md#insn-00597a88) · [`00597a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md#insn-00597a8c)
- 新版 [`00597b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597b10) · [`00597ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597ac8) · [`00597acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597acc)

~~~diff
- 00597ad0 ["INT_ADD", "register:40f0:8", ["const:597ad0:8", "const:4:8"]]
- 00597ad0 ["CALL", null, ["callee:00c581e0:8"]]
+ 00597b10 ["INT_ADD", "register:40f0:8", ["const:597b10:8", "const:4:8"]]
+ 00597b10 ["CALL", null, ["callee:00c581e0:8"]]
- 00597ad0 bytes c4001b94
+ 00597b10 bytes b4011b94
- 00597a88 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:888:8"]]
- 00597a88 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597ac8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
+ 00597ac8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00597a88 bytes 5a4744f9
+ 00597ac8 bytes 5a4746f9
- 00597a8c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:7b8:8"]]
- 00597a8c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597acc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:bb8:8"]]
+ 00597acc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00597a8c bytes 39df43f9
+ 00597acc bytes 39df45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58bab96aad4865b191d6b73cd1336136"></a>

### [`00597c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md) → [`00597c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md) FUN_00597c40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md) · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md) · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

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
      "definition_site": "00597ca0",
      "incomplete_value": true,
      "site": "00597ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597c60",
      "incomplete_value": true,
      "site": "00597c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
      "definition_site": "00597ce4",
      "incomplete_value": true,
      "site": "00597ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00597ca4",
      "incomplete_value": true,
      "site": "00597ca8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00597ca0",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ca0",
      "PARAM",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597ce4",
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
      "00597ca0",
      "READ",
      [
        "storage",
        "00c9b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ca0",
      "PARAM",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597ce4",
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

- 旧版 [`00597c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md#insn-00597c64) · [`00597ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md#insn-00597ca4) · [`00597ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597c00.md#insn-00597ca8)
- 新版 [`00597ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ca4) · [`00597ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ce4) · [`00597ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ce8)

~~~diff
- 00597c64 ["INT_ADD", "register:40f0:8", ["const:597c64:8", "const:4:8"]]
- 00597c64 ["CALL", null, ["callee:00c58280:8"]]
+ 00597ca4 ["INT_ADD", "register:40f0:8", ["const:597ca4:8", "const:4:8"]]
+ 00597ca4 ["CALL", null, ["callee:00c58280:8"]]
- 00597c64 bytes 87001b94
+ 00597ca4 bytes 77011b94
- 00597ca4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
- 00597ca4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597ce4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
+ 00597ce4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00597ca4 bytes 211844f9
+ 00597ce4 bytes 211846f9
- 00597ca8 ["INT_ADD", "register:40f0:8", ["const:597ca8:8", "const:4:8"]]
- 00597ca8 ["CALL", null, ["callee:00c58280:8"]]
+ 00597ce8 ["INT_ADD", "register:40f0:8", ["const:597ce8:8", "const:4:8"]]
+ 00597ce8 ["CALL", null, ["callee:00c58280:8"]]
- 00597ca8 bytes 76001b94
+ 00597ce8 bytes 66011b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845841b9491659543134d0f54ae96b26"></a>

### [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) → [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) FUN_00597ed0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`005ac9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ac9d0.md) [`005b7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7144.md) [`005b776c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b776c.md) [`005b7cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7cb8.md) [`005b809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b809c.md) · 呼出先 0件 
- 新版 呼出元 18件 [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) [`005b77ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md) [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597ed8",
      "incomplete_value": false,
      "site": "00597edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597e98",
      "incomplete_value": false,
      "site": "00597e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "00597edc",
      "DATA",
      [
        "storage",
        "00c6d328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00597edc",
      "DATA",
      [
        "storage",
        "00c6d728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md#insn-00597e98)
- 新版 [`00597ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md#insn-00597ed8)

~~~diff
- 00597e98 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00597e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597ed8 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00597ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597e98 bytes 08a10c91
+ 00597ed8 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96cd12e760e95ac852d9d702fe24342d"></a>

### [`00597ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md) → [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) FUN_00597efc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) [`005aca04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005aca04.md) [`005ace80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ac/005ace80.md) · 呼出先 24件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0044ff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044ff1c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md)
- 新版 呼出元 4件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005983a4",
      "incomplete_value": true,
      "site": "005983ac",
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
      "definition_site": "00598364",
      "incomplete_value": true,
      "site": "0059836c",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005983b4",
      "incomplete_value": true,
      "site": "005983b4",
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
                "const:f0:8"
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
      "definition_site": "00598374",
      "incomplete_value": true,
      "site": "00598374",
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
                "const:f0:8"
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
    "ordinal": 45,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005983b4",
      "incomplete_value": true,
      "site": "005983b4",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598374",
      "incomplete_value": true,
      "site": "00598374",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
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
      "00597f9c",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "00597fac",
      "READ",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00597fb8",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00597f9c",
      "READ",
      [
        "storage",
        "00c9b300",
        null,
        "pointer"
      ]
    ],
    [
      "00597fac",
      "READ",
      [
        "storage",
        "00ca65d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00597fb8",
      "READ",
      [
        "storage",
        "00ca65d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md#insn-00597ff8) · [`00598008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md#insn-00598008) · [`00598410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md#insn-00598410)
- 新版 [`00598038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598038) · [`00598048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598048) · [`00598450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598450)

~~~diff
- 00597ff8 ["INT_ADD", "register:40f0:8", ["const:597ff8:8", "const:4:8"]]
- 00597ff8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00598038 ["INT_ADD", "register:40f0:8", ["const:598038:8", "const:4:8"]]
+ 00598038 ["CALL", null, ["callee:00c580b0:8"]]
- 00597ff8 bytes 2eff1a94
+ 00598038 bytes 1e001b94
- 00598008 ["INT_ADD", "register:40f0:8", ["const:598008:8", "const:4:8"]]
- 00598008 ["CALL", null, ["callee:00c57f70:8"]]
+ 00598048 ["INT_ADD", "register:40f0:8", ["const:598048:8", "const:4:8"]]
+ 00598048 ["CALL", null, ["callee:00c57f70:8"]]
- 00598008 bytes dafe1a94
+ 00598048 bytes caff1a94
- 00598410 ["INT_ADD", "register:40f0:8", ["const:598410:8", "const:4:8"]]
- 00598410 ["CALL", null, ["callee:00c57e90:8"]]
+ 00598450 ["INT_ADD", "register:40f0:8", ["const:598450:8", "const:4:8"]]
+ 00598450 ["CALL", null, ["callee:00c57e90:8"]]
- 00598410 bytes a0fd1a94
+ 00598450 bytes 90fe1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70cbef50e39db41ac5da1698974b08d4"></a>

### [`00598afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md) → [`00598b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md) FUN_00598b3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) · 呼出先 3件 [`0059a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) · 呼出先 3件 [`0059a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598bdc",
      "incomplete_value": false,
      "site": "00598be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598b9c",
      "incomplete_value": false,
      "site": "00598ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "00598be0",
      "DATA",
      [
        "storage",
        "00c6d390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598be0",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md#insn-00598b3c) · [`00598b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md#insn-00598b78) · [`00598b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md#insn-00598b8c)
- 新版 [`00598b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598b7c) · [`00598bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598bb8) · [`00598bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598bcc)

~~~diff
- 00598b3c ["COPY", "register:0:8", ["register:4048:8"]]
- 00598b3c ["INT_ADD", "register:40f0:8", ["const:598b3c:8", "const:4:8"]]
- 00598b3c ["CALLIND", null, ["register:0:8"]]
+ 00598b7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00598b7c ["INT_ADD", "register:40f0:8", ["const:598b7c:8", "const:4:8"]]
+ 00598b7c ["CALLIND", null, ["register:0:8"]]
- 00598b3c bytes 20013fd6
+ 00598b7c bytes 20013fd6
- 00598b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598b78 ["INT_ADD", "register:40f0:8", ["const:598b78:8", "const:4:8"]]
- 00598b78 ["CALLIND", null, ["register:0:8"]]
+ 00598bb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598bb8 ["INT_ADD", "register:40f0:8", ["const:598bb8:8", "const:4:8"]]
+ 00598bb8 ["CALLIND", null, ["register:0:8"]]
- 00598b78 bytes 00013fd6
+ 00598bb8 bytes 00013fd6
- 00598b8c ["INT_ADD", "register:40f0:8", ["const:598b8c:8", "const:4:8"]]
- 00598b8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00598bcc ["INT_ADD", "register:40f0:8", ["const:598bcc:8", "const:4:8"]]
+ 00598bcc ["CALL", null, ["callee:00c57e90:8"]]
- 00598b8c bytes c1fb1a94
+ 00598bcc bytes b1fc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee05c44dba45f8621a5ed24c554cdd8f"></a>

### [`00598d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md) → [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) FUN_00598dc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md) [`005991dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005991dc.md) [`0059a458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a458.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059921c.md) [`0059a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a498.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598fe0",
      "incomplete_value": false,
      "site": "00598fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598fa0",
      "incomplete_value": false,
      "site": "00598fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "00598ec4",
      "PARAM",
      [
        "storage",
        "00ca6188",
        null,
        "undefined1"
      ]
    ],
    [
      "00598fe0",
      "DATA",
      [
        "storage",
        "00c6d480",
        null,
        "undefined *"
      ]
    ],
    [
      "00599050",
      "READ",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598ec4",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "00598fe0",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ],
    [
      "00599050",
      "READ",
      [
        "storage",
        "00c6d8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md#insn-00598dac) · [`00598dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md#insn-00598dcc) · [`00598de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598d80.md#insn-00598de0)
- 新版 [`00598dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598dec) · [`00598e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598e0c) · [`00598e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598e20)

~~~diff
- 00598dac ["INT_ADD", "register:40f0:8", ["const:598dac:8", "const:4:8"]]
- 00598dac ["CALL", null, ["callee:00597efc:8"]]
+ 00598dec ["INT_ADD", "register:40f0:8", ["const:598dec:8", "const:4:8"]]
+ 00598dec ["CALL", null, ["callee:00597efc:8"]]
- 00598dac bytes 44fcff97
+ 00598dec bytes 44fcff97
- 00598dcc ["INT_ADD", "register:40f0:8", ["const:598dcc:8", "const:4:8"]]
- 00598dcc ["CALL", null, ["callee:00c53d00:8"]]
+ 00598e0c ["INT_ADD", "register:40f0:8", ["const:598e0c:8", "const:4:8"]]
+ 00598e0c ["CALL", null, ["callee:00c53d00:8"]]
- 00598dcc bytes c5ea1a94
+ 00598e0c bytes bdeb1a94
- 00598de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598de0 ["INT_ADD", "register:40f0:8", ["const:598de0:8", "const:4:8"]]
- 00598de0 ["CALLIND", null, ["register:0:8"]]
+ 00598e20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598e20 ["INT_ADD", "register:40f0:8", ["const:598e20:8", "const:4:8"]]
+ 00598e20 ["CALLIND", null, ["register:0:8"]]
- 00598de0 bytes 00013fd6
+ 00598e20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c1981e28489433e8a0379cb7de88f13"></a>

### [`0059921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md) → [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) FUN_0059925c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00597ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597ebc.md) [`0059ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ad78.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059adb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599424",
      "incomplete_value": false,
      "site": "0059942c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005993e4",
      "incomplete_value": false,
      "site": "005993ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00599318",
      "incomplete_value": false,
      "site": "00599320",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005992d8",
      "incomplete_value": false,
      "site": "005992e0",
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
            "const:188:8"
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
      "00599318",
      "PARAM",
      [
        "storage",
        "00ca6188",
        null,
        "undefined1"
      ]
    ],
    [
      "0059942c",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ],
    [
      "005994b8",
      "READ",
      [
        "storage",
        "00c6d528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599318",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "0059942c",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ],
    [
      "005994b8",
      "READ",
      [
        "storage",
        "00c6d928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005992e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md#insn-005992e0) · [`0059924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md#insn-0059924c) · [`0059926c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059921c.md#insn-0059926c)
- 新版 [`00599320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-00599320) · [`0059928c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-0059928c) · [`005992ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-005992ac)

~~~diff
- 005992e0 ["INT_ADD", "register:40f0:8", ["const:5992e0:8", "const:4:8"]]
- 005992e0 ["CALL", null, ["callee:0044108c:8"]]
+ 00599320 ["INT_ADD", "register:40f0:8", ["const:599320:8", "const:4:8"]]
+ 00599320 ["CALL", null, ["callee:0044108c:8"]]
- 005992e0 bytes 5b9ffa97
+ 00599320 bytes 5b9ffa97
- 0059924c ["INT_ADD", "register:40f0:8", ["const:59924c:8", "const:4:8"]]
- 0059924c ["CALL", null, ["callee:00597efc:8"]]
+ 0059928c ["INT_ADD", "register:40f0:8", ["const:59928c:8", "const:4:8"]]
+ 0059928c ["CALL", null, ["callee:00597efc:8"]]
- 0059924c bytes 1cfbff97
+ 0059928c bytes 1cfbff97
- 0059926c ["INT_ADD", "register:40f0:8", ["const:59926c:8", "const:4:8"]]
- 0059926c ["CALL", null, ["callee:00c53d00:8"]]
+ 005992ac ["INT_ADD", "register:40f0:8", ["const:5992ac:8", "const:4:8"]]
+ 005992ac ["CALL", null, ["callee:00c53d00:8"]]
- 0059926c bytes 9de91a94
+ 005992ac bytes 95ea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2165029dfe5c36717d58f8873fe5e6e5"></a>

### [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) → [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) FUN_005996b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005997c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005997c4.md) [`00769084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`007690c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007690c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005996dc",
      "incomplete_value": false,
      "site": "005996ec",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059969c",
      "incomplete_value": false,
      "site": "005996ac",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599734",
      "value": [
        "leaf",
        "ram:7690c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005996f4",
      "value": [
        "leaf",
        "ram:769084:8"
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
      "005996dc",
      "PARAM",
      [
        "storage",
        "00ca6170",
        null,
        "undefined1"
      ]
    ],
    [
      "00599734",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769084"
      ]
    ]
  ],
  "added": [
    [
      "005996dc",
      "PARAM",
      [
        "storage",
        "00ca6570",
        null,
        "undefined1"
      ]
    ],
    [
      "00599734",
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

- 旧版 [`005996ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md#insn-005996ac) · [`005996f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md#insn-005996f4) · [`00599734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md#insn-00599734)
- 新版 [`005996ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-005996ec) · [`00599734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-00599734) · [`00599774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-00599774)

~~~diff
- 005996ac ["INT_ADD", "register:40f0:8", ["const:5996ac:8", "const:4:8"]]
- 005996ac ["CALL", null, ["callee:0044108c:8"]]
+ 005996ec ["INT_ADD", "register:40f0:8", ["const:5996ec:8", "const:4:8"]]
+ 005996ec ["CALL", null, ["callee:0044108c:8"]]
- 005996ac bytes 689efa97
+ 005996ec bytes 689efa97
- 005996f4 ["INT_ADD", "register:40f0:8", ["const:5996f4:8", "const:4:8"]]
- 005996f4 ["CALL", null, ["ram:769084:8"]]
+ 00599734 ["INT_ADD", "register:40f0:8", ["const:599734:8", "const:4:8"]]
+ 00599734 ["CALL", null, ["ram:7690c4:8"]]
- 005996f4 bytes 643e0794
+ 00599734 bytes 643e0794
- 00599734 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599734 ["INT_ADD", "register:40f0:8", ["const:599734:8", "const:4:8"]]
- 00599734 ["CALLIND", null, ["register:0:8"]]
+ 00599774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599774 ["INT_ADD", "register:40f0:8", ["const:599774:8", "const:4:8"]]
+ 00599774 ["CALLIND", null, ["register:0:8"]]
- 00599734 bytes 00013fd6
+ 00599774 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

